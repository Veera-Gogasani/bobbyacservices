/* BOBBY – UPI "Pay" (phones only) + Google review request after returning from the UPI app.
   Tapping Pay opens upi://pay with BOBBY's exact QR details: Android shows every installed UPI app
   (Google Pay, PhonePe, …) to choose from, iPhone opens the UPI app. If nothing opens, a small popup offers
   the QR code instead. The website never sees the payment result; the review popup appears on return. */
(function () {
  var modal = document.getElementById('payModal');
  if (!modal) return;
  var ua = navigator.userAgent || '';
  var android = /Android/i.test(ua);
  var ios = /iPhone|iPad|iPod/i.test(ua) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  if (!android && !ios) return;                       // desktop / web: Pay stays hidden

  var VPA = modal.getAttribute('data-upi'), QP = modal.getAttribute('data-qp');
  var rev = document.getElementById('revModal');
  var noapp = modal.querySelector('.pay-noapp');
  var KEY = 'bobby-pay-launch', DONE = 'bobby-rev-asked';
  var lastFocus = null, timer = null, launched = 0, away = false, AWAY = 'bobby-pay-away';

  function ss(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); if (v === null) sessionStorage.removeItem(k); else sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  // show every Pay button (they ship hidden so desktops never see them)
  document.querySelectorAll('[data-pay]').forEach(function (b) { b.hidden = false; });
  var bar = document.querySelector('.mbar'); if (bar) bar.classList.add('has-pay');

  // exactly the payee details from BOBBY's own QR code: no amount / note (apps decline those for personal accounts)
  function query() { return 'pa=' + encodeURIComponent(VPA).replace('%40', '@') + '&' + QP; }
  function link() { return 'upi://pay?' + query(); }
  function refresh() { document.querySelectorAll('[data-pay], #payModal [data-app]').forEach(function (a) { a.setAttribute('href', link()); }); }
  refresh();

  function open(showNoapp) {
    if (!modal.classList.contains('open')) lastFocus = document.activeElement;
    refresh(); if (noapp) noapp.hidden = !showNoapp; var qd = modal.querySelector('[data-qr]'); if (qd) qd.open = !!showNoapp;
    modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
  }
  function close(m) {
    m = m || modal; m.classList.remove('open'); m.setAttribute('aria-hidden', 'true');
    if (!document.querySelector('.modal.open')) document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) try { lastFocus.focus({ preventScroll: true }); } catch (e) {}
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
    if (t && (away || ss(AWAY)) && Date.now() - t > 2500 && Date.now() - t < 45 * 60 * 1000) askReview();
  }
  document.addEventListener('visibilitychange', function () {
    if (document.hidden) { if (timer) { clearTimeout(timer); timer = null; } if (launched || ss(KEY)) { away = true; ss(AWAY, '1'); } }   // the UPI app opened
    else returned();
  });
  window.addEventListener('pageshow', function (e) { if (e.persisted) returned(); });
  window.addEventListener('pagehide', function () { if (timer) { clearTimeout(timer); timer = null; } });

  // ---------- clicks ----------
  document.addEventListener('click', function (e) {
    var t = e.target.closest ? e.target : null; if (!t) return;
    var go = t.closest('[data-pay], #payModal [data-app]');
    if (go) {                                                          // let the browser follow upi://pay
      var dc = document.querySelector('.drawer.open [data-close]'); if (dc) dc.click();
      launched = Date.now(); away = false; ss(AWAY, null); ss(KEY, String(launched)); if (noapp) noapp.hidden = true;
      if (timer) clearTimeout(timer);
      timer = setTimeout(function () {                                 // still here after 2.5 s: no UPI app opened
        timer = null; if (!document.hidden && !away) open(true);
      }, 2500);
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

  // deep links: #pay opens the popup; #pay-noapp = Android fallback when the chosen app is not installed
  function hash() {
    if (location.hash === '#pay') open(false);
    else if (location.hash === '#pay-noapp') { launched = 0; away = false; ss(KEY, null); ss(AWAY, null); open(true); history.replaceState(null, '', location.pathname + location.search); }
  }
  window.addEventListener('hashchange', hash); hash();
  returned();   // page was reloaded after returning from the UPI app
})();
