/* BOBBY AC Repair & Home Appliance Services — site script (no build step) */
(function () {
  'use strict';
  var WA = '918374889163';
  var HOME = [16.2371462, 80.0339778];          /* business location (Google listing) – map start point */
  var LANGS = { en: 'English', te: 'తెలుగు', hi: 'हिन्दी' };
  var FONTS = {
    te: 'https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu:wght@400;500;600;700;800&display=swap',
    hi: 'https://fonts.googleapis.com/css2?family=Noto+Sans+Devanagari:wght@400;500;600;700;800&display=swap'
  };
  var dict = { en: null, te: null, hi: null };
  var lang = 'en';
  var root = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  root.classList.remove('no-js');

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function t(key) { var d = dict[lang] || dict.en; return (d && d[key]) || (dict.en && dict.en[key]) || ''; }
  function strip(html) { var d = document.createElement('div'); d.innerHTML = html; return d.textContent; }
  function waUrl(msg) { return 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg); }
  function gmap(lat, lng) { return 'https://maps.google.com/?q=' + lat + ',' + lng; }

  /* ---------- WhatsApp chat links ---------- */
  function updateWaLinks() {
    document.querySelectorAll('[data-wa]').forEach(function (a) {
      var kind = a.getAttribute('data-wa'), msg;
      if (kind === 'feedback') msg = t('wa.feedback');
      else if (kind && kind !== 'default') msg = t('wa.service').replace('{service}', strip(t('svc.' + kind + '.name')));
      else msg = t('wa.default');
      if (msg) a.href = waUrl(msg);
    });
  }

  /* ---------- i18n ---------- */
  function loadDict(l) {
    if (dict[l]) return Promise.resolve(dict[l]);
    return fetch('/assets/i18n/' + l + '.json', { cache: 'force-cache' }).then(function (r) { return r.json(); }).then(function (j) { dict[l] = j; return j; });
  }
  function loadFont(l) {
    if (!FONTS[l] || document.getElementById('font-' + l)) return;
    var link = document.createElement('link'); link.id = 'font-' + l; link.rel = 'stylesheet'; link.href = FONTS[l];
    document.head.appendChild(link);
  }
  function apply() {
    var d = dict[lang]; if (!d) return;
    document.querySelectorAll('[data-i18n]').forEach(function (el) { var v = d[el.getAttribute('data-i18n')]; if (v) el.innerHTML = v; });
    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-ph')]; if (v) el.setAttribute('placeholder', strip(v)); });
    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-aria')]; if (v) el.setAttribute('aria-label', strip(v)); });
    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) { var v = d[el.getAttribute('data-i18n-alt')]; if (v) el.setAttribute('alt', strip(v)); });
    var tk = root.getAttribute('data-title-key');
    if (tk && d[tk]) document.title = strip(d[tk]) + ' | BOBBY AC Repair & Home Appliance Services';
    root.setAttribute('lang', lang);
    document.querySelectorAll('.lang-code').forEach(function (el) { el.textContent = lang.toUpperCase(); });
    document.querySelectorAll('.lang-menu button').forEach(function (b) { b.setAttribute('aria-checked', b.getAttribute('data-lang') === lang ? 'true' : 'false'); });
    updateWaLinks();
    document.querySelectorAll('.bookform').forEach(function (f) { if (f._renderLoc) f._renderLoc(); });
  }
  function setLang(l, save) {
    if (!LANGS[l]) l = 'en';
    lang = l; if (save) store('bobby-lang', l);
    loadFont(l);
    Promise.all([loadDict('en'), loadDict(l)]).then(apply).catch(function () { lang = 'en'; });
  }
  document.querySelectorAll('.lang').forEach(function (box) {
    var btn = box.querySelector('.lang-btn');
    btn.addEventListener('click', function (e) { e.stopPropagation(); var open = box.classList.toggle('open'); btn.setAttribute('aria-expanded', open ? 'true' : 'false'); });
    box.querySelectorAll('.lang-menu button').forEach(function (b) {
      b.addEventListener('click', function () { setLang(b.getAttribute('data-lang'), true); box.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus(); });
    });
  });
  document.addEventListener('click', function () { document.querySelectorAll('.lang.open').forEach(function (b) { b.classList.remove('open'); b.querySelector('.lang-btn').setAttribute('aria-expanded', 'false'); }); });

  /* ---------- header + drawer ---------- */
  var hdr = document.querySelector('.hdr');
  function onScroll() { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var drawer = document.getElementById('drawer'), burger = document.querySelector('.burger');
  function openDrawer() { if (!drawer) return; drawer.classList.add('open'); drawer.setAttribute('aria-hidden', 'false'); burger.setAttribute('aria-expanded', 'true'); document.body.style.overflow = 'hidden'; var f = drawer.querySelector('.drawer-x'); if (f) f.focus(); }
  function closeDrawer() { if (!drawer || !drawer.classList.contains('open')) return; drawer.classList.remove('open'); drawer.setAttribute('aria-hidden', 'true'); burger.setAttribute('aria-expanded', 'false'); document.body.style.overflow = ''; }
  if (burger) burger.addEventListener('click', openDrawer);
  if (drawer) {
    drawer.querySelectorAll('[data-close]').forEach(function (el) { el.addEventListener('click', closeDrawer); });
    drawer.querySelectorAll('nav a').forEach(function (a) { a.addEventListener('click', closeDrawer); });
  }

  /* ---------- reveal on scroll ---------- */
  var els = document.querySelectorAll('.reveal, .timeline');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }
  var hp = document.querySelector('.hero-visual');
  if (hp && !reduce && window.innerWidth > 960) {
    window.addEventListener('scroll', function () { var y = window.scrollY; if (y < 900) hp.style.transform = 'translateY(' + (y * 0.06) + 'px)'; }, { passive: true });
  }

  /* ---------- modals ---------- */
  var openModals = [], lastFocus = [];
  function openModal(m) {
    if (!m) return;
    lastFocus.push(document.activeElement);
    m.classList.add('open'); m.setAttribute('aria-hidden', 'false'); openModals.push(m);
    document.body.style.overflow = 'hidden';
    setTimeout(function () { var f = m.querySelector('input:not([type=hidden]):not([tabindex="-1"]), select, button'); if (f) f.focus(); }, 60);
  }
  function closeModal(m) {
    m = m || openModals[openModals.length - 1]; if (!m) return;
    m.classList.remove('open'); m.setAttribute('aria-hidden', 'true');
    openModals = openModals.filter(function (x) { return x !== m; });
    if (!openModals.length) document.body.style.overflow = '';
    var lf = lastFocus.pop(); if (lf && lf.focus) lf.focus();
  }
  document.querySelectorAll('.modal').forEach(function (m) {
    m.querySelectorAll('[data-close-modal]').forEach(function (el) { el.addEventListener('click', function () { closeModal(m); }); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.lang.open').forEach(function (b) { b.classList.remove('open'); });
    if (openModals.length) closeModal(); else closeDrawer();
  });

  /* ---------- Book buttons -> booking form ---------- */
  var PRESET = {
    ac_repair: ['', 'repair'], ac_servicing: ['', 'service'], ac_install: ['', 'install'], ac_uninstall: ['', 'uninstall'],
    ac_gas: ['', 'gas'], fridge: ['fridge', ''], washer: ['washer', ''], cooler: ['cooler', ''], fan: ['fan', '']
  };
  function preset(form, svc) {
    var p = PRESET[svc]; if (!p) return;
    if (p[0]) form.elements.appliance.value = p[0];
    if (p[1]) form.elements.service.value = p[1];
  }
  var bookModal = document.getElementById('bookModal');
  var inlineForm = document.getElementById('book');
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-book]');
    if (!a) return;
    e.preventDefault(); closeDrawer();
    var svc = a.getAttribute('data-book');
    if (inlineForm) {
      preset(inlineForm, svc);
      inlineForm.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      setTimeout(function () { inlineForm.elements.name.focus({ preventScroll: true }); }, 400);
    } else if (bookModal) {
      preset(bookModal.querySelector('form'), svc); openModal(bookModal);
    }
  });
  if (inlineForm && location.hash === '#book') setTimeout(function () { inlineForm.scrollIntoView(); }, 200);

  /* ---------- location: current position ---------- */
  function setLoc(form, lat, lng, acc) {
    form.elements.lat.value = (+lat).toFixed(6); form.elements.lng.value = (+lng).toFixed(6);
    form._acc = acc || null; form._locErr = null; form._renderLoc();
  }
  function initLoc(form) {
    var box = form.querySelector('.loc-status');
    form._renderLoc = function () {
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (form._locBusy) { box.className = 'loc-status busy'; box.textContent = strip(t('f.loc.getting')); return; }
      if (lat && lng) {
        box.className = 'loc-status ok';
        box.innerHTML = '<span>✓ ' + strip(t('f.loc.ok')) + (form._acc ? ' (±' + Math.round(form._acc) + ' m)' : '') + '</span> ' +
          '<a href="' + gmap(lat, lng) + '" target="_blank" rel="noopener">' + strip(t('f.loc.view')) + '</a> · <button type="button" class="loc-clear">' + strip(t('f.loc.clear')) + '</button>';
        box.querySelector('.loc-clear').addEventListener('click', function () { form.elements.lat.value = ''; form.elements.lng.value = ''; form._acc = null; form._renderLoc(); });
        return;
      }
      if (form._locErr) { box.className = 'loc-status err'; box.textContent = strip(t(form._locErr)); return; }
      box.className = 'loc-status'; box.textContent = '';
    };
    form.querySelector('.loc-cur').addEventListener('click', function () {
      if (!navigator.geolocation) { form._locErr = 'f.loc.fail'; form._renderLoc(); return; }
      form._locBusy = true; form._locErr = null; form._renderLoc();
      navigator.geolocation.getCurrentPosition(function (pos) {
        form._locBusy = false; setLoc(form, pos.coords.latitude, pos.coords.longitude, pos.coords.accuracy);
      }, function (err) {
        form._locBusy = false; form._locErr = err && err.code === 1 ? 'f.loc.denied' : 'f.loc.fail'; form._renderLoc();
      }, { enableHighAccuracy: true, timeout: 15000, maximumAge: 60000 });
    });
    form.querySelector('.loc-map').addEventListener('click', function () { openPicker(form); });
  }

  /* ---------- location: choose on map (Leaflet + OpenStreetMap, no API key) ---------- */
  var mapModal = document.getElementById('mapModal'), pick = null, leafletReady = null, pickForm = null, chosen = null;
  function loadLeaflet() {
    if (leafletReady) return leafletReady;
    leafletReady = new Promise(function (res, rej) {
      var css = document.createElement('link'); css.rel = 'stylesheet'; css.href = '/assets/vendor/leaflet/leaflet.css'; document.head.appendChild(css);
      var s = document.createElement('script'); s.src = '/assets/vendor/leaflet/leaflet.js'; s.onload = res; s.onerror = rej; document.head.appendChild(s);
    });
    return leafletReady;
  }
  function mapMsg(key) { var m = mapModal.querySelector('.map-msg'); m.textContent = key ? strip(t(key)) : ''; }
  function setPin(latlng, zoom) {
    chosen = latlng;
    if (!pick.marker) {
      pick.marker = L.marker(latlng, { draggable: true, autoPan: true }).addTo(pick.map);
      pick.marker.on('dragend', function () { chosen = pick.marker.getLatLng(); });
    } else pick.marker.setLatLng(latlng);
    if (zoom) pick.map.setView(latlng, zoom);
    mapModal.querySelector('.map-use').disabled = false;
  }
  function openPicker(form) {
    pickForm = form; openModal(mapModal); mapMsg('');
    loadLeaflet().then(function () {
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (!pick) {
        pick = { map: L.map('pickMap', { zoomControl: true }).setView(HOME, 14) };
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap contributors' }).addTo(pick.map);
        pick.map.on('click', function (e) { setPin(e.latlng); });
      }
      setTimeout(function () { pick.map.invalidateSize(); }, 80);
      if (lat && lng) setPin(L.latLng(+lat, +lng), 17);
      else if (pick.marker) { pick.map.removeLayer(pick.marker); pick.marker = null; chosen = null; mapModal.querySelector('.map-use').disabled = true; pick.map.setView(HOME, 14); }
    }).catch(function () { mapMsg('f.loc.fail'); });
  }
  if (mapModal) {
    mapModal.querySelector('.map-use').addEventListener('click', function () {
      if (chosen && pickForm) setLoc(pickForm, chosen.lat, chosen.lng);
      closeModal(mapModal);
    });
    mapModal.querySelector('.map-me').addEventListener('click', function () {
      if (!navigator.geolocation || !pick) return mapMsg('f.loc.fail');
      mapMsg('f.loc.getting');
      navigator.geolocation.getCurrentPosition(function (pos) { mapMsg(''); setPin(L.latLng(pos.coords.latitude, pos.coords.longitude), 18); },
        function (err) { mapMsg(err && err.code === 1 ? 'f.loc.denied' : 'f.loc.fail'); }, { enableHighAccuracy: true, timeout: 15000 });
    });
    mapModal.querySelector('.map-search').addEventListener('submit', function (e) {
      e.preventDefault();
      var q = this.querySelector('input').value.trim(); if (!q || !pick) return;
      var url = 'https://nominatim.openstreetmap.org/search?format=json&limit=1&countrycodes=in&viewbox=79.95,16.32,80.12,16.15&q=' + encodeURIComponent(q + ', Narasaraopet');
      mapMsg('f.loc.getting');
      fetch(url, { headers: { 'Accept-Language': lang } }).then(function (r) { return r.json(); }).then(function (res) {
        if (!res || !res.length) return mapMsg('map.noresult');
        mapMsg(''); setPin(L.latLng(+res[0].lat, +res[0].lon), 17);
      }).catch(function () { mapMsg('map.noresult'); });
    });
  }

  /* ---------- booking forms (Contact page + pop-up) ---------- */
  document.querySelectorAll('.bookform').forEach(function (form) {
    var started = Date.now(), msgEl = form.querySelector('.form-msg');
    initLoc(form);
    function fieldErr(name, key) {
      var f = form.elements[name], wrap = f.closest('.field');
      wrap.classList.add('err'); var em = wrap.querySelector('.emsg'); em.setAttribute('data-i18n', key); em.innerHTML = t(key); return f;
    }
    form.addEventListener('input', function (e) { var w = e.target.closest('.field'); if (w) w.classList.remove('err'); });
    form.addEventListener('change', function (e) { var w = e.target.closest('.field'); if (w) w.classList.remove('err'); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.elements.company.value) return;                 /* honeypot */
      if (Date.now() - started < 2000) return;                 /* too fast = bot */
      form.querySelectorAll('.field').forEach(function (w) { w.classList.remove('err'); });
      var first = null;
      ['name', 'appliance', 'service', 'area'].forEach(function (n) { if (!form.elements[n].value.trim()) { var f = fieldErr(n, 'f.err.req'); first = first || f; } });
      var phone = form.elements.phone.value.replace(/\D/g, '').replace(/^(91|0)(?=\d{10}$)/, '');
      if (!/^[6-9]\d{9}$/.test(phone)) { var p = fieldErr('phone', 'f.err.phone'); first = first || p; }
      if (first) { first.focus(); return; }
      function val(n) { var el = form.elements[n]; return el.tagName === 'SELECT' ? el.options[el.selectedIndex].text : el.value.trim(); }
      var lines = ['*' + strip(t('f.wa.title')) + ' – BOBBY AC Repair & Home Appliance Services*',
        strip(t('f.name')) + ': ' + val('name'),
        strip(t('f.phone')) + ': ' + phone,
        strip(t('f.appliance')) + ': ' + val('appliance') + (val('brand') ? ' (' + val('brand') + ')' : ''),
        strip(t('f.service')) + ': ' + val('service'),
        strip(t('f.area')) + ': ' + val('area')];
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (lat && lng) lines.push('📍 ' + strip(t('f.wa.loc')) + ': ' + gmap(lat, lng));
      if (val('date')) lines.push(strip(t('f.date')) + ': ' + val('date'));
      if (val('msg')) lines.push(strip(t('f.msg')) + ': ' + val('msg').slice(0, 500));
      msgEl.setAttribute('data-i18n', 'f.ok'); msgEl.innerHTML = t('f.ok');
      window.open(waUrl(lines.join('\n')), '_blank', 'noopener');
    });
  });

  /* ---------- count-up stats ---------- */
  var counts = document.querySelectorAll('.count[data-to]');
  function runCount(el) {
    var to = +el.getAttribute('data-to'); if (!to) return;
    if (reduce) { el.textContent = to; return; }
    var t0 = null; el.textContent = '0';
    function f(ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / 1400); el.textContent = Math.round(to * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(f); }
    requestAnimationFrame(f);
  }
  if ('IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { runCount(e.target); cio.unobserve(e.target); } }); }, { threshold: 0.6 });
    counts.forEach(function (c) { if (c.getAttribute('data-to')) cio.observe(c); });
  }

  /* ---------- reviews carousel ---------- */
  document.querySelectorAll('.rev-carousel').forEach(function (car) {
    var tr = car.querySelector('.rev-track');
    function step(dir) { var card = tr.querySelector('.rev-card'); var w = card ? card.getBoundingClientRect().width + 18 : 300;
      if (dir > 0 && tr.scrollLeft + tr.clientWidth >= tr.scrollWidth - 4) tr.scrollTo({ left: 0 }); else tr.scrollBy({ left: dir * w }); }
    car.querySelector('.rev-prev').addEventListener('click', function () { step(-1); });
    car.querySelector('.rev-next').addEventListener('click', function () { step(1); });
    if (!reduce) { var tm = setInterval(function () { step(1); }, 5000);
      ['pointerdown', 'focusin', 'mouseenter'].forEach(function (ev) { car.addEventListener(ev, function () { clearInterval(tm); }); }); }
  });

  document.querySelectorAll('.yr').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* start */
  var saved = store('bobby-lang');
  loadDict('en').then(function () { if (saved && saved !== 'en' && LANGS[saved]) setLang(saved, false); else { updateWaLinks(); document.querySelectorAll('.bookform').forEach(function (f) { f._renderLoc(); }); } }).catch(function () {});

  /* ---------- review carousel component ---------- */
  document.querySelectorAll('[data-rc]').forEach(function (rc) {
    var track = rc.querySelector('.rc-track'), slides = [].slice.call(track.children);
    var prev = rc.querySelector('.rc-prev'), next = rc.querySelector('.rc-next'), dotsBox = rc.querySelector('.rc-dots');
    var idx = 0, timer = null, stopped = false, hover = false, DELAY = 5500;
    function per() { return parseInt(getComputedStyle(rc).getPropertyValue('--per'), 10) || 1; }
    function maxIdx() { return Math.max(0, slides.length - per()); }
    function buildDots() {
      dotsBox.innerHTML = '';
      for (var i = 0; i <= maxIdx(); i++) {
        var d = document.createElement('button'); d.type = 'button'; d.className = 'rc-dot';
        d.setAttribute('aria-label', 'Go to slide ' + (i + 1)); d.dataset.i = i;
        d.addEventListener('click', function () { userAct(); go(+this.dataset.i); });
        dotsBox.appendChild(d);
      }
    }
    function go(i) {
      var m = maxIdx(); idx = i > m ? 0 : (i < 0 ? m : i);
      var step = slides.length > 1 ? slides[1].offsetLeft - slides[0].offsetLeft : 0;
      track.style.transform = 'translate3d(' + (-idx * step) + 'px,0,0)';
      var p = per();
      slides.forEach(function (s, k) { var vis = k >= idx && k < idx + p; s.setAttribute('aria-hidden', vis ? 'false' : 'true'); });
      [].forEach.call(dotsBox.children, function (d, k) { d.setAttribute('aria-current', k === idx ? 'true' : 'false'); });
      var single = m === 0; prev.disabled = single; next.disabled = single;
    }
    function play() { clearInterval(timer); if (!reduce && !stopped && !hover && maxIdx() > 0) timer = setInterval(function () { go(idx + 1); }, DELAY); }
    function pause() { clearInterval(timer); }
    function userAct() { stopped = true; pause(); }
    prev.addEventListener('click', function () { userAct(); go(idx - 1); });
    next.addEventListener('click', function () { userAct(); go(idx + 1); });
    rc.addEventListener('mouseenter', function () { hover = true; pause(); });
    rc.addEventListener('mouseleave', function () { hover = false; play(); });
    rc.addEventListener('focusin', function () { hover = true; pause(); });
    rc.addEventListener('focusout', function () { hover = false; play(); });
    rc.setAttribute('tabindex', '0');
    rc.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { userAct(); go(idx - 1); e.preventDefault(); }
      else if (e.key === 'ArrowRight') { userAct(); go(idx + 1); e.preventDefault(); }
    });
    var x0 = null, y0 = null;
    track.addEventListener('pointerdown', function (e) { x0 = e.clientX; y0 = e.clientY; });
    track.addEventListener('pointerup', function (e) {
      if (x0 === null) return; var dx = e.clientX - x0, dy = e.clientY - y0; x0 = null;
      if (Math.abs(dx) > 40 && Math.abs(dx) > Math.abs(dy)) { userAct(); go(idx + (dx < 0 ? 1 : -1)); }
    });
    track.addEventListener('pointercancel', function () { x0 = null; });
    document.addEventListener('visibilitychange', function () { document.hidden ? pause() : play(); });
    var lastPer = per(), rt;
    window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { if (per() !== lastPer) { lastPer = per(); buildDots(); } go(Math.min(idx, maxIdx())); }, 120); });
    buildDots(); go(0); play();
  });
})();
