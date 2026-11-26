/* BOBBY – UPI "Pay" popup (phones only) + Google review request after returning from the UPI app.
   UPI apps decline payments to a personal account when a website pre-fills them (upi://pay links), so instead
   a tap copies BOBBY's UPI ID to the clipboard and opens PhonePe / Google Pay; the customer pastes it inside
   the app (which is allowed). The QR code is the other option. The website never sees the payment result;
   the review popup appears when the customer comes back. */
(function () {
  var modal = document.getElementById('payModal');
  if (!modal) return;
  var ua = navigator.userAgent || '';
  var android = /Android/i.test(ua);
  var ios = /iPhone|iPad|iPod/i.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  if (!android && !ios) return;                       // desktop / web: Pay stays hidden

  var VPA = modal.getAttribute('data-upi');
  var rev = document.getElementById('revModal');
  var noapp = modal.querySelector('.pay-noapp'), copied = modal.querySelector('.pay-copied');
  var PKG = { phonepe: 'com.phonepe.app', gpay: 'com.google.android.apps.nbu.paisa.user' };
  var IOS = { phonepe: 'phonepe://', gpay: 'gpay://' };
  var KEY = 'bobby-pay-launch', AWAY = 'bobby-pay-away', DONE = 'bobby-rev-asked';
  var lastFocus = null, timer = null, launched = 0, away = false, blurred = false;

  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  // show every Pay button (they ship hidden so desktops never see them)
  document.querySelectorAll('[data-pay]').forEach(function (b) { b.hidden = false; });
  var bar = document.querySelector('.mbar'); if (bar) bar.classList.add('has-pay');

  // opens the app's home screen (no payment pre-filled, so the app never declines it)
  function appLink(app) {
    if (ios) return IOS[app];
    var back = location.href.split('#')[0] + '#pay-noapp';
    return 'intent:#Intent;action=android.intent.action.MAIN;category=android.intent.category.LAUNCHER;package=' + PKG[app] +
      ';S.browser_fallback_url=' + encodeURIComponent(back) + ';end';
  }

  function open(showNoapp) {
    if (!modal.classList.contains('open')) lastFocus = document.activeElement;
    if (noapp) noapp.hidden = !showNoapp;
    var qd = modal.querySelector('[data-qr]'); if (qd && showNoapp) qd.open = true;
    modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
  }
  function close(m) {
    m = m || modal; m.classList.remove('open'); m.setAttribute('aria-hidden', 'true');
    if (!document.querySelector('.modal.open')) document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
  }

  function copy(text) {
    return new Promise(function (ok) {
      function fallback() {
        var ta = document.createElement('textarea'); ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
        document.body.appendChild(ta); ta.select(); ta.setSelectionRange(0, text.length);
        try { document.execCommand('copy'); } catch (e) {} document.body.removeChild(ta); ok();
      }
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(ok, fallback); else fallback();
    });
  }

  // ---------- review request after coming back from the UPI app ----------
  function askReview() {
    ss(KEY, null); ss(AWAY, null); launched = 0; away = false;
    if (!rev || ss(DONE)) return;
    ss(DONE, '1');
    close(modal);
    rev.classList.add('open'); rev.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
    var b = rev.querySelector('[data-rev-go]'); if (b) setTimeout(function () { try { b.focus({ preventScroll: true }); } catch (e) {} }, 80);
  }
  function returned() {
    var t = launched || +ss(KEY) || 0;
    if (t && (away || ss(AWAY)) && Date.now() - t > 4000 && Date.now() - t < 45 * 60 * 1000) askReview();
  }
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { if (timer) { clearTimeout(timer); timer = null; } if (launched || ss(KEY)) { away = true; ss(AWAY, '1'); } }
    else returned();
  });
  window.addEventListener('blur', function () { if (launched) { blurred = true; if (timer) { clearTimeout(timer); timer = null; } } });
  window.addEventListener('pageshow', function (e) { if (e.persisted) returned(); });
  window.addEventListener('pagehide', function () { if (timer) { clearTimeout(timer); timer = null; } });

  // ---------- clicks ----------
  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target : null; if (!t) return;
    if (t.closest('[data-pay]')) {
      e.preventDefault();
      var dc = document.querySelector('.drawer.open [data-close]'); if (dc) dc.click();
      open(false); return;
    }
    var app = t.closest('#payModal [data-open]');
    if (app) {
      e.preventDefault();
      var url = appLink(app.getAttribute('data-open'));
      if (noapp) noapp.hidden = true;
      copy(VPA).then(function () {
        if (copied) copied.hidden = false;
        launched = Date.now(); away = false; blurred = false; ss(AWAY, null); ss(KEY, String(launched));
        if (timer) clearTimeout(timer);
        if (ios) timer = setTimeout(function () {                    // iPhone: nothing opened -> app not installed
          timer = null; if (!document.hidden && !away && !blurred && document.hasFocus()) { if (noapp) noapp.hidden = false; }
        }, 3000);
        setTimeout(function () { location.href = url; }, 350);        // let the customer see "UPI ID copied"
      });
      return;
    }
    if (t.closest('#payModal [data-close-pay]')) { close(modal); return; }
    if (t.closest('#revModal [data-rev-go]')) { ls('bobby-reviewed', '1'); setTimeout(function () { close(rev); }, 300); return; }
    if (t.closest('#revModal [data-close-rev]')) { close(rev); return; }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (rev && rev.classList.contains('open')) { e.stopPropagation(); close(rev); }
    else if (modal.classList.contains('open')) { e.stopPropagation(); close(modal); }
  }, true);

  // #pay opens the popup; #pay-noapp = Android fallback when the chosen app is not installed
  function hash() {
    if (location.hash === '#pay') open(false);
    else if (location.hash === '#pay-noapp') { launched = 0; away = false; ss(KEY, null); ss(AWAY, null); open(true); history.replaceState(null, '', location.pathname + location.search); }
  }
  window.addEventListener('hashchange', hash); hash();
  returned();   // page was reloaded after returning from the UPI app
})();
