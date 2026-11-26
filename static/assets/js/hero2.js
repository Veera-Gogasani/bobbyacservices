/* Home "2nd hero": animated service slider (no libraries). Plays only while on screen. */
(function () {
  'use strict';
  var hero = document.getElementById('services-showcase');
  if (!hero) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(pointer: fine)').matches;
  var slides = [].slice.call(hero.querySelectorAll('.bobby-hero-slide'));
  var caps = [].slice.call(hero.querySelectorAll('.bobby-hero-cap'));
  var tabs = [].slice.call(hero.querySelectorAll('.bobby-hero-tab'));
  var cur = hero.querySelector('.bobby-hero-cur');
  var bar = hero.querySelector('.bobby-hero-progress span');
  var DELAY = 5500, RESUME = 12000, idx = 0, timer = null, hold = false, busy = false, inView = false, washer = null;
  hero.style.setProperty('--bh-delay', DELAY / 1000 + 's');

  function colors(s) { hero.style.setProperty('--bh-bg', s.dataset.bg); hero.style.setProperty('--bh-bg2', s.dataset.bg2); }
  function tick(el, from, to, dur, fmt) {
    if (!el) return; if (reduce) { el.textContent = fmt(to); return; }
    var t0 = null;
    requestAnimationFrame(function step(ts) {
      if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / dur);
      el.textContent = fmt(Math.round(from + (to - from) * (1 - Math.pow(1 - k, 3))));
      if (k < 1) requestAnimationFrame(step);
    });
  }
  function onActive(s) {
    clearInterval(washer);
    if (s.classList.contains('bobby-hero-slide-ac')) {
      var t = s.querySelector('.bh2-temp'); t.textContent = '30°';
      setTimeout(function () { tick(t, 30, 24, 1800, function (v) { return v + '°'; }); }, 700);
    }
    if (s.classList.contains('bobby-hero-slide-washer')) {
      var w = s.querySelector('.bh2-timer'), sec = 42;
      washer = setInterval(function () { sec = sec > 1 ? sec - 1 : 42; w.textContent = '0:' + ('0' + sec).slice(-2); }, 1000);
    }
  }
  function go(n, user) {
    n = (n + slides.length) % slides.length;
    if (n === idx || busy) return;
    busy = true;
    var old = slides[idx], nxt = slides[n];
    old.classList.remove('is-active'); old.classList.add('is-leaving'); old.setAttribute('aria-hidden', 'true');
    setTimeout(function () { old.classList.remove('is-leaving'); busy = false; }, 900);
    nxt.classList.add('is-active'); nxt.setAttribute('aria-hidden', 'false');
    caps[idx].classList.remove('is-active'); caps[n].classList.add('is-active');
    tabs[idx].classList.remove('is-active'); tabs[idx].setAttribute('aria-selected', 'false');
    tabs[n].classList.add('is-active'); tabs[n].setAttribute('aria-selected', 'true');
    cur.textContent = ('0' + (n + 1)).slice(-2);
    colors(nxt); idx = n; onActive(nxt);
    if (user) hold = true;
    play();
  }
  function play() {
    clearTimeout(timer);
    bar.classList.remove('is-run'); void bar.offsetWidth;
    var shown = !hero.classList.contains('hero-duo-panel') || hero.classList.contains('is-on');
    if (hold || !inView || !shown) { hero.classList.add('is-paused'); if (hold) { bar.style.transform = 'scaleX(1)'; timer = setTimeout(function () { hold = false; play(); }, RESUME); } return; }
    bar.style.transform = ''; bar.classList.add('is-run'); hero.classList.remove('is-paused');
    timer = setTimeout(function () {
      if (idx === slides.length - 1 && window.bobbyDuo && window.bobbyDuo.next()) return;
      go(idx + 1);
    }, DELAY);
  }

  hero.querySelector('.bobby-hero-next').addEventListener('click', function () { go(idx + 1, true); });
  hero.querySelector('.bobby-hero-prev').addEventListener('click', function () { go(idx - 1, true); });
  tabs.forEach(function (t) { t.addEventListener('click', function () { go(+t.dataset.go, true); }); });
  hero.addEventListener('keydown', function (e) {
    if (e.target.closest('a,input')) return;
    if (e.key === 'ArrowRight') { go(idx + 1, true); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { go(idx - 1, true); e.preventDefault(); }
  });
  var sx = null, sy = null;
  hero.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  hero.addEventListener('touchend', function (e) {
    if (sx === null) return; var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy; sx = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.3) go(idx + (dx < 0 ? 1 : -1), true);
  });

  /* autoplay + heavy animation only while visible */
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (en) {
      inView = en[0].isIntersecting;
      hero.classList.toggle('bh2-off', !inView);
      play();
    }, { threshold: 0.35 }).observe(hero);
  } else { inView = true; }
  document.addEventListener('visibilitychange', function () { if (document.hidden) clearTimeout(timer); else play(); });

  if (fine && !reduce) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', ((e.clientX - r.left) / r.width - 0.5).toFixed(3));
      hero.style.setProperty('--my', ((e.clientY - r.top) / r.height - 0.5).toFixed(3));
      hero.style.setProperty('--cx', (e.clientX - r.left) + 'px');
      hero.style.setProperty('--cy', (e.clientY - r.top) + 'px');
    });
    hero.addEventListener('pointerleave', function () { hero.style.setProperty('--mx', 0); hero.style.setProperty('--my', 0); });
    [].forEach.call(hero.querySelectorAll('.bh2-magnet'), function (b) {
      b.addEventListener('pointermove', function (e) {
        var r = b.getBoundingClientRect();
        b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * 0.25).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * 0.35).toFixed(1) + 'px)';
      });
      b.addEventListener('pointerleave', function () { b.style.transform = ''; });
    });
  }

  colors(slides[0]); onActive(slides[0]); play();

  /* ---- two heroes: classic hero first (default), then the services showcase, alternating ---- */
  var duo = document.getElementById('hero-duo');
  if (!duo) return;
  var panels = [].slice.call(duo.querySelectorAll('.hero-duo-panel'));   /* 0 = classic, 1 = showcase */
  var dots = [].slice.call(document.querySelectorAll('.hero-duo-pager button'));
  panels.forEach(function (p, i) { if (i) p.classList.add('is-gone'); });   /* hidden hero: skip all its rendering work */
  var SHOW = panels.indexOf(hero), cur2 = 0, duoTimer = null, duoHold = false, HOLD_CLASSIC = 8000, duoHover = false, duoVisible = true;
  function scheduleBack() {                 /* while the classic hero is shown, switch to the showcase after a pause */
    clearTimeout(duoTimer);
    duoTimer = setTimeout(function again() {
      if (!duoVisible || document.hidden) { duoTimer = setTimeout(again, 1500); return; }
      show(SHOW);
    }, HOLD_CLASSIC);
  }
  function show(n) {
    if (n === cur2) return;
    var old = panels[cur2], nxt = panels[n], fwd = n > cur2 || (cur2 === panels.length - 1 && n === 0);
    nxt.classList.remove('is-gone');
    if (!fwd) { nxt.classList.add('is-back'); void nxt.offsetWidth; nxt.classList.remove('is-back'); }
    old.classList.remove('is-on'); old.classList.toggle('is-out', fwd);
    if (!fwd) old.style.transform = 'translate3d(100%,0,0)';
    nxt.classList.remove('is-out'); nxt.style.transform = ''; nxt.classList.add('is-on');
    setTimeout(function () { old.classList.remove('is-out'); old.style.transform = ''; if (!old.classList.contains('is-on')) old.classList.add('is-gone'); }, 1150);
    old.setAttribute('aria-hidden', 'true'); old.inert = true;
    nxt.removeAttribute('aria-hidden'); nxt.inert = false;
    dots[cur2].classList.remove('is-on'); dots[cur2].setAttribute('aria-selected', 'false');
    dots[n].classList.add('is-on'); dots[n].setAttribute('aria-selected', 'true');
    cur2 = n;
    clearTimeout(duoTimer); clearTimeout(timer);
    if (n === SHOW) {                       /* showcase: play its slides from the first one */
      hold = false; inView = true;
      if (idx !== 0) { busy = false; go(0); } else play();
    } else {
      hero.classList.add('is-paused');
      var restart = nxt.querySelectorAll('.anim'); [].forEach.call(restart, function (el) { el.style.animation = 'none'; void el.offsetWidth; el.style.animation = ''; });
      scheduleBack();
    }
  }
  /* called by the showcase after its last slide: go back to the classic hero */
  window.bobbyDuo = { next: function () { show(1 - SHOW); return true; } };
  /* a pager click shows that hero; auto-switching resumes on its own after a short pause */
  dots.forEach(function (d) { d.addEventListener('click', function () { var n = +d.dataset.duo; if (n === cur2) return; show(n); if (n !== SHOW) { clearTimeout(duoTimer); duoTimer = setTimeout(scheduleBack, RESUME - HOLD_CLASSIC); } }); });
  if ('IntersectionObserver' in window) new IntersectionObserver(function (en) { duoVisible = en[0].isIntersecting; }, { threshold: 0.35 }).observe(duo);
  panels.forEach(function (p, i) { p.inert = i !== cur2; });
  scheduleBack();
})();
/* real hero photo: when the photo ends up small (short screens), hide the floating chips so they don't cover it */
(function () {
  var ph = document.querySelector('.hero-photo-real'); if (!ph || !window.ResizeObserver) return;
  var vis = ph.closest('.hero-visual');
  new ResizeObserver(function () { vis.classList.toggle('is-tight', ph.getBoundingClientRect().width < 260); }).observe(ph);
})();
