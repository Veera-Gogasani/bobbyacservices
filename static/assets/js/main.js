/* BOBBY AC Repair & Services — site script (no dependencies) */
(function () {
  'use strict';
  var WA = '918374889163';
  var LANGS = { en: 'English', te: 'తెలుగు', hi: 'हिन्दी' };
  var FONTS = {
    te: 'https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&display=swap',
    hi: 'https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap'
  };
  var dict = { en: null, te: null, hi: null };
  var lang = 'en';
  var root = document.documentElement;
  root.classList.remove('no-js');

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function t(key) { var d = dict[lang] || dict.en; return (d && d[key]) || (dict.en && dict.en[key]) || ''; }

  /* ---------- WhatsApp links ---------- */
  function waUrl(msg) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg); }
  function strip(html) { var d = document.createElement('div'); d.innerHTML = html; return d.textContent; }
  function updateWaLinks() {
    document.querySelectorAll('[data-wa]').forEach(function (a) {
      var kind = a.getAttribute('data-wa');
      var msg;
      if (kind === 'feedback') msg = t('wa.feedback');
      else if (kind && kind !== 'default') msg = t('wa.service').replace('{service}', strip(t('svc.' + kind + '.name')));
      else msg = t('wa.default');
      if (msg) a.href = waUrl(msg);
    });
  }

  /* ---------- i18n ---------- */
  function loadDict(l) {
    if (dict[l]) return Promise.resolve(dict[l]);
    return fetch('/assets/i18n/' + l + '.json', { cache: 'force-cache' })
      .then(function (r) { return r.json(); })
      .then(function (j) { dict[l] = j; return j; });
  }
  function loadFont(l) {
    if (!FONTS[l] || document.getElementById('font-' + l)) return;
    var link = document.createElement('link');
    link.id = 'font-' + l; link.rel = 'stylesheet'; link.href = FONTS[l];
    document.head.appendChild(link);
  }
  function apply() {
    var d = dict[lang]; if (!d) return;
    document.querySelectorAll('[data-i18n]').forEach(function (el) { var v = d[el.getAttribute('data-i18n')]; if (v) el.innerHTML = v; });
    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-ph')]; if (v) el.setAttribute('placeholder', strip(v)); });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-aria')]; if (v) el.setAttribute('aria-label', strip(v)); });
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-alt')]; if (v) el.setAttribute('alt', strip(v)); });
    var tk = root.getAttribute('data-title-key');
    if (tk && d[tk]) document.title = strip(d[tk]) + ' | BOBBY AC Repair & Services';
    root.setAttribute('lang', lang);
    document.querySelectorAll('.lang-code').forEach(function (el) { el.textContent = lang.toUpperCase(); });
    document.querySelectorAll('.lang-menu button').forEach(function (b) { b.setAttribute('aria-checked', b.getAttribute('data-lang') === lang ? 'true' : 'false'); });
    updateWaLinks();
  }
  function setLang(l, save) {
    if (!LANGS[l]) l = 'en';
    lang = l; if (save) store('bobby-lang', l);
    loadFont(l);
    Promise.all([loadDict('en'), loadDict(l)]).then(apply).catch(function () { lang = 'en'; });
  }

  /* language menu */
  document.querySelectorAll('.lang').forEach(function (box) {
    var btn = box.querySelector('.lang-btn');
    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = box.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    box.querySelectorAll('.lang-menu button').forEach(function (b) {
      b.addEventListener('click', function () {
        setLang(b.getAttribute('data-lang'), true);
        box.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus();
      });
    });
  });
  document.addEventListener('click', function () { document.querySelectorAll('.lang.open').forEach(function (b) { b.classList.remove('open'); b.querySelector('.lang-btn').setAttribute('aria-expanded', 'false'); }); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.lang.open').forEach(function (b) { b.classList.remove('open'); });
    closeDrawer();
  });

  /* ---------- header + drawer ---------- */
  var hdr = document.querySelector('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

  var drawer = document.getElementById('drawer');
  var burger = document.querySelector('.burger');
  function openDrawer() { if (!drawer) return; drawer.classList.add('open'); drawer.setAttribute('aria-hidden', 'false'); burger.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; var f = drawer.querySelector('.drawer-x'); if (f) f.focus(); }
  function closeDrawer() { if (!drawer || !drawer.classList.contains('open')) return; drawer.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true'); burger.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; burger.focus(); }
  if (burger) burger.addEventListener('click', openDrawer);
  if (drawer) {
    drawer.querySelectorAll('[data-close]').forEach(function (el) { el.addEventListener('click', closeDrawer); });
    drawer.querySelectorAll('nav a').forEach(function (a) { a.addEventListener('click', closeDrawer); });
  }

  /* ---------- reveal on scroll ---------- */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var els = document.querySelectorAll('.reveal, .timeline');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  /* subtle parallax on hero photo */
  var hp = document.querySelector('.hero-visual');
  if (hp && !reduce && window.innerWidth > 960) {
    window.addEventListener('scroll', function () { var y = window.scrollY; if (y < 900) hp.style.transform = 'translateY(' + (y * 0.06) + 'px)'; }, { passive: true });
  }

  /* ---------- booking form ---------- */
  var form = document.getElementById('bookForm');
  if (form) {
    var started = Date.now();
    var msgEl = document.getElementById('formMsg');
    function fieldErr(id, key) {
      var f = document.getElementById(id); var wrap = f.closest('.field');
      wrap.classList.add('err'); var em = wrap.querySelector('.emsg'); em.setAttribute('data-i18n', key); em.innerHTML = t(key); return f;
    }
    form.addEventListener('input', function (e) { var w = e.target.closest('.field'); if (w) w.classList.remove('err'); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.hp input').value) return;           /* honeypot */
      if (Date.now() - started < 2500) return;                     /* too fast = bot */
      form.querySelectorAll('.field').forEach(function (w) { w.classList.remove('err'); });
      var first = null;
      ['fName', 'fAppliance', 'fService', 'fArea'].forEach(function (id) {
        if (!document.getElementById(id).value.trim()) { var f = fieldErr(id, 'f.err.req'); first = first || f; }
      });
      var phone = document.getElementById('fPhone').value.replace(/\D/g, '').replace(/^(91|0)(?=\d{10}$)/, '');
      if (!/^[6-9]\d{9}$/.test(phone)) { var p = fieldErr('fPhone', 'f.err.phone'); first = first || p; }
      if (first) { first.focus(); return; }
      function val(id) { var el = document.getElementById(id); return el.tagName === 'SELECT' ? el.options[el.selectedIndex].text : el.value.trim(); }
      var lines = ['*' + strip(t('f.wa.title')) + ' – BOBBY AC Repair & Services*',
        strip(t('f.name')) + ': ' + val('fName'),
        strip(t('f.phone')) + ': ' + phone,
        strip(t('f.appliance')) + ': ' + val('fAppliance') + (val('fBrand') ? ' (' + val('fBrand') + ')' : ''),
        strip(t('f.service')) + ': ' + val('fService'),
        strip(t('f.area')) + ': ' + val('fArea')];
      if (val('fDate')) lines.push(strip(t('f.date')) + ': ' + val('fDate'));
      if (val('fMsg')) lines.push(strip(t('f.msg')) + ': ' + val('fMsg').slice(0, 500));
      msgEl.setAttribute('data-i18n', 'f.ok'); msgEl.innerHTML = t('f.ok');
      window.open(waUrl(lines.join('\n')), '_blank', 'noopener');
    });
  }

  /* year */
  document.querySelectorAll('.yr').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* start */
  var saved = store('bobby-lang');
  loadDict('en').then(function () { if (saved && saved !== 'en' && LANGS[saved]) setLang(saved, false); else updateWaLinks(); }).catch(function () {});
})();
