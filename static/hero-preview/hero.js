/* THE BOBBY COOLING EXPERIENCE – isolated hero preview script (no libraries; everything namespaced bobby-hero) */
(function () {
  'use strict';
  var bobbyHeroRoot = document.documentElement;
  var bobbyHeroReduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bobbyHeroSmall = window.matchMedia('(max-width: 760px)');
  bobbyHeroRoot.classList.remove('bobby-hero-nojs');
  bobbyHeroRoot.classList.add('bobby-hero-js');

  /* intro plays once per browser session; later visits get the resting state quickly */
  try {
    if (sessionStorage.getItem('bobby-hero-seen')) bobbyHeroRoot.classList.add('bobby-hero-quick');
    sessionStorage.setItem('bobby-hero-seen', '1');
  } catch (e) {}
  var bobbyHeroQuick = bobbyHeroRoot.classList.contains('bobby-hero-quick') || bobbyHeroReduce;

  /* ---------- AC display: 32° summer heat → 24° comfort ---------- */
  function bobbyHeroTemp() {
    var el = document.querySelector('.bobby-hero-temp');
    if (!el) return;
    if (bobbyHeroQuick) { el.textContent = '24°'; return; }
    var from = 32, to = 24, start = null, dur = 1600;
    setTimeout(function () {
      requestAnimationFrame(function step(ts) {
        if (!start) start = ts;
        var k = Math.min(1, (ts - start) / dur);
        el.textContent = Math.round(from - (from - to) * (1 - Math.pow(1 - k, 3))) + '°';
        if (k < 1) requestAnimationFrame(step);
      });
    }, 2000);
  }

  /* ---------- airflow particles & snowflakes ---------- */
  function bobbyHeroParticles() {
    var box = document.querySelector('.bobby-hero-particles');
    if (!box || bobbyHeroReduce) return;
    var n = 18, html = '';
    for (var i = 0; i < n; i++) {
      var flake = i % 4 === 0;
      var x0 = 4 + Math.random() * 18, y0 = 2 + Math.random() * 14;
      var x1 = 45 + Math.random() * 55, y1 = 30 + Math.random() * 65;
      var style = '--x0:' + x0 + 'cqw;--y0:' + y0 + 'cqh;' +
        '--s:' + (flake ? (10 + Math.random() * 8) + 'px' : (3 + Math.random() * 5) + 'px') + ';' +
        '--t:' + (5 + Math.random() * 4).toFixed(1) + 's;' +
        '--dl:' + ((bobbyHeroQuick ? 0 : 2.4) + Math.random() * 4).toFixed(2) + 's;';
      /* percentages of the airflow box (fallback for browsers without container units handled below) */
      style = style.replace('cqw', '%').replace('cqh', '%');
      html += '<i class="' + (flake ? 'bobby-hero-flake' : '') + '" style="' + style +
        '--x1:' + 0 + 'px;--y1:0px" data-x1="' + x1 + '" data-y1="' + y1 + '" data-x0="' + x0 + '" data-y0="' + y0 + '">' + (flake ? '❄' : '') + '</i>';
    }
    box.innerHTML = html;
    /* convert % paths into pixels of the airflow box so translate() works everywhere */
    function size() {
      var w = box.clientWidth, h = box.clientHeight;
      [].forEach.call(box.children, function (p) {
        p.style.setProperty('--x0', (p.dataset.x0 / 100 * w) + 'px');
        p.style.setProperty('--y0', (p.dataset.y0 / 100 * h) + 'px');
        p.style.setProperty('--x1', (p.dataset.x1 / 100 * w) + 'px');
        p.style.setProperty('--y1', (p.dataset.y1 / 100 * h) + 'px');
      });
    }
    size();
    window.addEventListener('resize', size);
  }

  /* ---------- scroll-responsive hero + nav ---------- */
  var bobbyHeroEl = document.getElementById('bobby-hero');
  var bobbyHeroNav = document.querySelector('.bobby-hero-nav');
  var bobbyHeroTicking = false;
  function bobbyHeroOnScroll() {
    if (bobbyHeroTicking) return;
    bobbyHeroTicking = true;
    requestAnimationFrame(function () {
      var y = window.scrollY || 0;
      bobbyHeroNav.classList.toggle('is-scrolled', y > 30);
      if (!bobbyHeroReduce && !bobbyHeroSmall.matches && bobbyHeroEl) {
        var p = Math.max(0, Math.min(1, y / (bobbyHeroEl.offsetHeight * 0.9)));
        bobbyHeroEl.style.setProperty('--bobby-hero-p', p.toFixed(3));
      }
      bobbyHeroTicking = false;
    });
  }
  window.addEventListener('scroll', bobbyHeroOnScroll, { passive: true });
  bobbyHeroOnScroll();

  /* ---------- layered pointer parallax (desktop only) ---------- */
  function bobbyHeroParallax() {
    if (bobbyHeroReduce || !window.matchMedia('(pointer: fine)').matches) return;
    var layers = [].slice.call(document.querySelectorAll('.bobby-hero-layer[data-depth]'));
    var tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
    function loop() {
      cx += (tx - cx) * 0.08; cy += (ty - cy) * 0.08;
      layers.forEach(function (l) {
        var d = parseFloat(l.dataset.depth);
        l.style.translate = (cx * d * -28).toFixed(2) + 'px ' + (cy * d * -18).toFixed(2) + 'px';
      });
      raf = (Math.abs(tx - cx) > 0.001 || Math.abs(ty - cy) > 0.001) ? requestAnimationFrame(loop) : null;
    }
    bobbyHeroEl.addEventListener('pointermove', function (e) {
      if (bobbyHeroSmall.matches) return;
      var r = bobbyHeroEl.getBoundingClientRect();
      tx = (e.clientX - r.left) / r.width - 0.5; ty = (e.clientY - r.top) / r.height - 0.5;
      if (!raf) raf = requestAnimationFrame(loop);
    });
    bobbyHeroEl.addEventListener('pointerleave', function () { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(loop); });
  }

  /* ---------- scroll reveals ---------- */
  function bobbyHeroReveals() {
    var items = document.querySelectorAll('.bobby-hero-reveal');
    if (!('IntersectionObserver' in window) || bobbyHeroReduce) { [].forEach.call(items, function (i) { i.classList.add('is-in'); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.12 });
    [].forEach.call(items, function (i) { io.observe(i); });
  }

  /* ---------- mobile menu ---------- */
  var bobbyHeroBurger = document.querySelector('.bobby-hero-burger');
  var bobbyHeroMenu = document.getElementById('bobby-hero-menu');
  function bobbyHeroCloseMenu() { bobbyHeroMenu.classList.remove('is-open'); bobbyHeroBurger.setAttribute('aria-expanded', 'false'); bobbyHeroBurger.setAttribute('aria-label', 'Open menu'); }
  bobbyHeroBurger.addEventListener('click', function () {
    var open = !bobbyHeroMenu.classList.contains('is-open');
    bobbyHeroMenu.classList.toggle('is-open', open);
    bobbyHeroBurger.setAttribute('aria-expanded', String(open));
    bobbyHeroBurger.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  });
  bobbyHeroMenu.addEventListener('click', function (e) { if (e.target.closest('a')) bobbyHeroCloseMenu(); });

  /* ---------- language selector (Telugu/Hindi live on the main site) ---------- */
  var bobbyHeroLangBtn = document.querySelector('.bobby-hero-lang-btn');
  var bobbyHeroLangMenu = document.getElementById('bobby-hero-lang-menu');
  function bobbyHeroLangToggle(open) { bobbyHeroLangMenu.hidden = !open; bobbyHeroLangBtn.setAttribute('aria-expanded', String(open)); }
  bobbyHeroLangBtn.addEventListener('click', function (e) { e.stopPropagation(); bobbyHeroLangToggle(bobbyHeroLangMenu.hidden); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.bobby-hero-lang')) bobbyHeroLangToggle(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { bobbyHeroLangToggle(false); bobbyHeroCloseMenu(); } });
  [].forEach.call(document.querySelectorAll('[data-bobby-hero-lang]'), function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem('bobby-lang', a.getAttribute('data-bobby-hero-lang')); } catch (e) {} });
  });

  bobbyHeroTemp();
  bobbyHeroParticles();
  bobbyHeroParallax();
  bobbyHeroReveals();
})();
