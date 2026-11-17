/* BOBBY – motion hero preview v2 (no libraries). Everything namespaced bobby-hero. */
(function () {
  'use strict';
  var bobbyHeroRoot = document.documentElement;
  var bobbyHeroReduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bobbyHeroSmall = window.matchMedia('(max-width: 760px)');
  bobbyHeroRoot.classList.remove('bobby-hero-nojs');
  bobbyHeroRoot.classList.add('bobby-hero-js');

  var hero = document.getElementById('bobby-hero');
  var slides = [].slice.call(hero.querySelectorAll('.bobby-hero-slide'));
  var caps = [].slice.call(hero.querySelectorAll('.bobby-hero-cap'));
  var tabs = [].slice.call(hero.querySelectorAll('.bobby-hero-tab'));
  var cur = hero.querySelector('.bobby-hero-cur');
  var bar = hero.querySelector('.bobby-hero-progress span');
  var DELAY = 5500, idx = 0, timer = null, hold = false, busy = false;
  hero.style.setProperty('--bh-delay', DELAY / 1000 + 's');

  function setColors(s) { hero.style.setProperty('--bh-bg', s.dataset.bg); hero.style.setProperty('--bh-bg2', s.dataset.bg2); }

  function bobbyHeroGo(n, user) {
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
    setColors(nxt);
    var img = nxt.querySelector('img'); if (img && img.loading === 'lazy') img.loading = 'eager';
    idx = n;
    if (user) hold = true;
    bobbyHeroPlay();
  }
  function bobbyHeroPlay() {
    clearTimeout(timer);
    bar.classList.remove('is-run'); void bar.offsetWidth;
    if (bobbyHeroReduce || hold) { hero.classList.add('is-paused'); bar.style.transform = 'scaleX(1)'; return; }
    bar.style.transform = ''; bar.classList.add('is-run'); hero.classList.remove('is-paused');
    timer = setTimeout(function () { bobbyHeroGo(idx + 1); }, DELAY);
  }

  hero.querySelector('.bobby-hero-next').addEventListener('click', function () { bobbyHeroGo(idx + 1, true); });
  hero.querySelector('.bobby-hero-prev').addEventListener('click', function () { bobbyHeroGo(idx - 1, true); });
  tabs.forEach(function (t) { t.addEventListener('click', function () { bobbyHeroGo(+t.dataset.go, true); }); });
  hero.addEventListener('keydown', function (e) {
    if (e.target.closest('a,input')) return;
    if (e.key === 'ArrowRight') { bobbyHeroGo(idx + 1, true); e.preventDefault(); }
    if (e.key === 'ArrowLeft') { bobbyHeroGo(idx - 1, true); e.preventDefault(); }
  });
  /* swipe */
  var sx = null, sy = null;
  hero.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; sy = e.touches[0].clientY; }, { passive: true });
  hero.addEventListener('touchend', function (e) {
    if (sx === null) return; var dx = e.changedTouches[0].clientX - sx, dy = e.changedTouches[0].clientY - sy; sx = null;
    if (Math.abs(dx) > 50 && Math.abs(dx) > Math.abs(dy) * 1.3) bobbyHeroGo(idx + (dx < 0 ? 1 : -1), true);
  });
  document.addEventListener('visibilitychange', function () { if (document.hidden) clearTimeout(timer); else bobbyHeroPlay(); });

  /* pointer parallax for product + floating objects */
  if (!bobbyHeroReduce && window.matchMedia('(pointer: fine)').matches) {
    hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      hero.style.setProperty('--mx', ((e.clientX - r.left) / r.width - 0.5).toFixed(3));
      hero.style.setProperty('--my', ((e.clientY - r.top) / r.height - 0.5).toFixed(3));
    });
    hero.addEventListener('pointerleave', function () { hero.style.setProperty('--mx', 0); hero.style.setProperty('--my', 0); });
  }

  /* scroll: hero stage recedes, nav turns frosted */
  var nav = document.querySelector('.bobby-hero-nav'), ticking = false;
  function onScroll() {
    if (ticking) return; ticking = true;
    requestAnimationFrame(function () {
      var y = window.scrollY || 0;
      nav.classList.toggle('is-scrolled', y > hero.offsetHeight - 90);
      if (!bobbyHeroReduce && !bobbyHeroSmall.matches) hero.style.setProperty('--bobby-hero-p', Math.min(1, y / (hero.offsetHeight * 0.85)).toFixed(3));
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* section reveals */
  var items = document.querySelectorAll('.bobby-hero-reveal');
  if (!('IntersectionObserver' in window) || bobbyHeroReduce) [].forEach.call(items, function (i) { i.classList.add('is-in'); });
  else {
    var io = new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('is-in'); io.unobserve(x.target); } }); }, { rootMargin: '0px 0px -10% 0px', threshold: .12 });
    [].forEach.call(items, function (i) { io.observe(i); });
  }

  /* mobile menu */
  var burger = document.querySelector('.bobby-hero-burger'), menu = document.getElementById('bobby-hero-menu');
  function closeMenu() { menu.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); burger.setAttribute('aria-label', 'Open menu'); }
  burger.addEventListener('click', function () { var o = !menu.classList.contains('is-open'); menu.classList.toggle('is-open', o); burger.setAttribute('aria-expanded', String(o)); burger.setAttribute('aria-label', o ? 'Close menu' : 'Open menu'); });
  menu.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });

  /* language selector – Telugu/Hindi live on the main site */
  var lb = document.querySelector('.bobby-hero-lang-btn'), lm = document.getElementById('bobby-hero-lang-menu');
  function lang(o) { lm.hidden = !o; lb.setAttribute('aria-expanded', String(o)); }
  lb.addEventListener('click', function (e) { e.stopPropagation(); lang(lm.hidden); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.bobby-hero-lang')) lang(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { lang(false); closeMenu(); } });
  [].forEach.call(document.querySelectorAll('[data-bobby-hero-lang]'), function (a) { a.addEventListener('click', function () { try { localStorage.setItem('bobby-lang', a.dataset.bobbyHeroLang); } catch (e) {} }); });

  setColors(slides[0]);
  hero.setAttribute('tabindex', '-1');
  bobbyHeroPlay();
})();

/* ===== Preview 2: realistic motion layer ===== */
(function () {
  'use strict';
  var body = document.body, hero = document.getElementById('bobby-hero');
  var pre = document.querySelector('.bh2-pre');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* pre-header: measure height, slide away on scroll */
  function preH() { body.style.setProperty('--pre-h', pre.offsetHeight + 'px'); }
  preH(); window.addEventListener('resize', preH);
  var up = false;
  window.addEventListener('scroll', function () {
    var u = (window.scrollY || 0) > 40;
    if (u !== up) { up = u; pre.classList.toggle('is-hidden', u); body.classList.toggle('bh2-up', u); }
  }, { passive: true });

  /* number tickers inside the appliances */
  function tick(el, from, to, dur, fmt) {
    if (!el) return; if (reduce) { el.textContent = fmt(to); return; }
    var t0 = null;
    requestAnimationFrame(function step(ts) {
      if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = fmt(Math.round(from + (to - from) * e));
      if (k < 1) requestAnimationFrame(step);
    });
  }
  var washerTimer = null;
  function onActive(slide) {
    if (slide.classList.contains('bobby-hero-slide-ac')) {
      var t = slide.querySelector('.bh2-temp'); t.textContent = '30°';
      setTimeout(function () { tick(t, 30, 24, 1800, function (v) { return v + '°'; }); }, 700);
    }
    if (slide.classList.contains('bobby-hero-slide-washer')) {
      var w = slide.querySelector('.bh2-timer'), s = 42;
      clearInterval(washerTimer);
      washerTimer = setInterval(function () { s = s > 1 ? s - 1 : 42; w.textContent = '0:' + ('0' + s).slice(-2); }, 1000);
    }
  }
  var slides = [].slice.call(document.querySelectorAll('.bobby-hero-slide'));
  var mo = new MutationObserver(function (list) {
    list.forEach(function (m) {
      var s = m.target, on = s.classList.contains('is-active');
      if (on && !s._bh2on) onActive(s);
      s._bh2on = on;
    });
  });
  slides.forEach(function (s) { s._bh2on = s.classList.contains('is-active'); mo.observe(s, { attributes: true, attributeFilter: ['class'] }); });
  onActive(slides[0]);

  if (reduce || !window.matchMedia('(pointer: fine)').matches) return;

  /* cursor spotlight */
  hero.addEventListener('pointermove', function (e) {
    var r = hero.getBoundingClientRect();
    hero.style.setProperty('--cx', (e.clientX - r.left) + 'px');
    hero.style.setProperty('--cy', (e.clientY - r.top) + 'px');
  });

  /* magnetic buttons */
  [].forEach.call(document.querySelectorAll('.bh2-magnet'), function (b) {
    b.addEventListener('pointermove', function (e) {
      var r = b.getBoundingClientRect();
      b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * 0.25).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * 0.35).toFixed(1) + 'px)';
    });
    b.addEventListener('pointerleave', function () { b.style.transform = ''; });
  });
})();
