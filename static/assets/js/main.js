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
    return fetch('/assets/i18n/' + l + '.json?v=' + (document.documentElement.getAttribute('data-iv') || '1'), { cache: 'force-cache' }).then(function (r) { return r.json(); }).then(function (j) { dict[l] = j; return j; });
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
    document.querySelectorAll('.bookform').forEach(function (f) { if (f._renderLoc) f._renderLoc(); if (f._renderCount) f._renderCount(); });
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
    var target = inlineForm || (bookModal && bookModal.querySelector('form'));
    if (target && target.classList.contains('is-done')) target.querySelector('.bd-new').click();   /* fresh form after a booking */
    if (inlineForm) {
      preset(inlineForm, svc);
      inlineForm.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
      setTimeout(function () { inlineForm.elements.name.focus({ preventScroll: true }); }, 400);
    } else if (bookModal) {
      preset(bookModal.querySelector('form'), svc); openModal(bookModal);
    }
  });
  if (inlineForm && location.hash === '#book') setTimeout(function () { inlineForm.scrollIntoView(); }, 200);

  /* ---------- location helpers ---------- */
  var NSR = { lat: HOME[0], lng: HOME[1] };                     /* Narasaraopet – search bias */
  var revCache = {}, revLast = 0;
  function fmt(s, o) { return s.replace(/\{(\w+)\}/g, function (_, k) { return o[k]; }); }
  /* Reverse geocode (OpenStreetMap Nominatim, max ~1 request/second) */
  function reverseGeo(lat, lng) {
    var key = (+lat).toFixed(5) + ',' + (+lng).toFixed(5);
    if (revCache[key]) return Promise.resolve(revCache[key]);
    var wait = Math.max(0, 1100 - (Date.now() - revLast)); revLast = Date.now() + wait;
    return new Promise(function (r) { setTimeout(r, wait); }).then(function () {
      return fetch('https://nominatim.openstreetmap.org/reverse?format=jsonv2&zoom=18&addressdetails=1&lat=' + lat + '&lon=' + lng,
        { headers: { 'Accept-Language': lang + ',en' } });
    }).then(function (r) { return r.json(); }).then(function (j) {
      var a = (j && j.address) || {}, parts = [];
      [a.house_number && a.road ? a.house_number + ' ' + a.road : (a.road || a.pedestrian), a.neighbourhood || a.suburb || a.quarter || a.hamlet,
       a.village || a.town || a.city || a.county, a.postcode].forEach(function (p) { if (p && parts.indexOf(p) < 0) parts.push(p); });
      var s = parts.join(', ') || (j && j.display_name ? j.display_name.split(',').slice(0, 4).join(',') : '');
      revCache[key] = s; return s;
    }).catch(function () { return ''; });
  }
  /* Pasted Google Maps links / "lat, lng" text → coordinates */
  function parseCoords(q) {
    var m = q.match(/!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)/) || q.match(/@(-?\d+\.\d+),\s*(-?\d+\.\d+)/) ||
            q.match(/[?&](?:q|query|ll|destination)=(-?\d+\.\d+),\s*(-?\d+\.\d+)/) || q.match(/^\s*(-?\d{1,2}\.\d{3,})\s*[, ]\s*(-?\d{1,3}\.\d{3,})\s*$/);
    if (!m) return null;
    var la = +m[1], lo = +m[2];
    return (la > 5 && la < 38 && lo > 67 && lo < 98) ? { lat: la, lng: lo } : null;   /* inside India */
  }
  function distKm(a, b) {
    var R = 6371, dLa = (b.lat - a.lat) * Math.PI / 180, dLo = (b.lng - a.lng) * Math.PI / 180;
    var x = Math.sin(dLa / 2) * Math.sin(dLa / 2) + Math.cos(a.lat * Math.PI / 180) * Math.cos(b.lat * Math.PI / 180) * Math.sin(dLo / 2) * Math.sin(dLo / 2);
    return 2 * R * Math.asin(Math.sqrt(x));
  }
  /* Place search: Photon (typo-tolerant, biased to Narasaraopet) → Nominatim fallbacks */
  function searchPlaces(q) {
    var photon = 'https://photon.komoot.io/api/?limit=8&lat=' + NSR.lat + '&lon=' + NSR.lng + '&location_bias_scale=0.6&q=' + encodeURIComponent(q);
    function fromPhoton(j) {
      return ((j && j.features) || []).map(function (f) {
        var p = f.properties || {}, c = f.geometry.coordinates;
        var sub = [p.street, p.district || p.locality, p.city || p.county, p.state].filter(Boolean);
        return { lat: c[1], lng: c[0], name: p.name || p.street || sub[0] || q, sub: sub.filter(function (s) { return s !== p.name; }).slice(0, 3).join(', '), country: p.countrycode };
      }).filter(function (r) { return r.country === 'IN'; });
    }
    function nomi(extra, bounded) {
      return fetch('https://nominatim.openstreetmap.org/search?format=jsonv2&limit=6&countrycodes=in&addressdetails=1&viewbox=79.80,16.45,80.30,16.00' + (bounded ? '&bounded=1' : '') + '&q=' + encodeURIComponent(q + extra),
        { headers: { 'Accept-Language': lang + ',en' } }).then(function (r) { return r.json(); }).then(function (res) {
        return (res || []).map(function (r) { var d = (r.display_name || '').split(','); return { lat: +r.lat, lng: +r.lon, name: r.name || d[0], sub: d.slice(1, 4).join(',').trim() }; });
      });
    }
    return fetch(photon).then(function (r) { return r.json(); }).then(fromPhoton).catch(function () { return []; }).then(function (list) {
      if (list.length) return list;
      return nomi('', true).then(function (l) { return l.length ? l : nomi(', Narasaraopet', false); })
        .then(function (l) { return l.length ? l : nomi(', Palnadu, Andhra Pradesh', false); }).catch(function () { return []; });
    }).then(function (list) {
      list.forEach(function (r) { r.km = distKm(NSR, r); });
      return list.sort(function (a, b) { return a.km - b.km; }).slice(0, 6);
    });
  }

  /* ---------- location: current position (high-accuracy GPS, best of several readings) ---------- */
  function setLoc(form, lat, lng, acc, addr) {
    form.elements.lat.value = (+lat).toFixed(6); form.elements.lng.value = (+lng).toFixed(6);
    form._acc = acc || null; form._locErr = null; form.elements.addr.value = addr || ''; form._renderLoc();
    if (!addr) reverseGeo(lat, lng).then(function (a) {
      if (form.elements.lat.value !== (+lat).toFixed(6)) return;
      form.elements.addr.value = a; form._renderLoc();
      var area = form.elements.area; if (a && !area.value.trim()) { area.value = a.slice(0, 120); var w = area.closest('.field'); if (w) w.classList.remove('err'); }
    });
  }
  function initLoc(form) {
    var box = form.querySelector('.loc-status');
    form._renderLoc = function () {
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (form._locBusy) { box.className = 'loc-status busy'; box.textContent = form._liveAcc ? fmt(strip(t('f.loc.improving')), { m: Math.round(form._liveAcc) }) : strip(t('f.loc.getting')); return; }
      if (lat && lng) {
        var weak = form._acc && form._acc > 80;
        box.className = 'loc-status ok' + (weak ? ' weak' : '');
        var addr = form.elements.addr.value;
        box.innerHTML = '<span class="ls-main">✓ ' + strip(t('f.loc.ok')) + (form._acc ? ' (±' + Math.round(form._acc) + ' m)' : '') + '</span>' +
          (addr ? '<span class="ls-addr">' + addr.replace(/</g, '&lt;') + '</span>' : '') +
          (weak ? '<span class="ls-weak">' + fmt(strip(t('f.loc.weak')), { m: Math.round(form._acc) }) + '</span>' : '') +
          '<span class="ls-act"><a href="' + gmap(lat, lng) + '" target="_blank" rel="noopener">' + strip(t('f.loc.view')) + '</a> · <button type="button" class="ls-adj">' + strip(t('f.loc.adjust')) + '</button> · <button type="button" class="loc-clear">' + strip(t('f.loc.clear')) + '</button></span>';
        box.querySelector('.loc-clear').addEventListener('click', function () { form.elements.lat.value = ''; form.elements.lng.value = ''; form.elements.addr.value = ''; form._acc = null; form._renderLoc(); });
        box.querySelector('.ls-adj').addEventListener('click', function () { openPicker(form); });
        return;
      }
      if (form._locErr) { box.className = 'loc-status err'; box.textContent = strip(t(form._locErr)); return; }
      box.className = 'loc-status'; box.textContent = '';
    };
    form.querySelector('.loc-cur').addEventListener('click', function () {
      if (!window.isSecureContext) { form._locErr = 'f.loc.insecure'; form._renderLoc(); return; }
      if (!navigator.geolocation) { form._locErr = 'f.loc.fail'; form._renderLoc(); return; }
      if (form._watch != null) navigator.geolocation.clearWatch(form._watch);
      form._locBusy = true; form._locErr = null; form._liveAcc = null; form._renderLoc();
      var best = null, done = false;
      function stop() { done = true; navigator.geolocation.clearWatch(form._watch); form._watch = null; clearTimeout(form._geoT); clearTimeout(form._geoT2); form._locBusy = false; form._liveAcc = null; }
      function finish() {
        if (done) return; stop();
        setLoc(form, best.latitude, best.longitude, best.accuracy);
        if (best.accuracy > 80) openPicker(form);                 /* weak fix: let the customer confirm the pin */
      }
      function fail(key) { if (done) return; stop(); form._locErr = key; form._renderLoc(); }
      form._watch = navigator.geolocation.watchPosition(function (pos) {
        if (done) return;
        if (!best || pos.coords.accuracy < best.accuracy) best = pos.coords;
        form._liveAcc = best.accuracy; form._renderLoc();
        if (best.accuracy <= 20) finish();                        /* precise enough – stop early */
      }, function (err) {
        if (best) return finish();
        fail(err && err.code === 1 ? 'f.loc.denied' : 'f.loc.fail');
      }, { enableHighAccuracy: true, timeout: 20000, maximumAge: 0 });
      form._geoT = setTimeout(function () { if (best) finish(); }, 12000);          /* best reading after 12 s */
      form._geoT2 = setTimeout(function () { if (best) finish(); else fail('f.loc.fail'); }, 25000);
    });
    form.querySelector('.loc-map').addEventListener('click', function () { openPicker(form); });
  }

  /* ---------- location: choose on map (Leaflet, centre-pin picker, street + satellite) ---------- */
  var mapModal = document.getElementById('mapModal'), pick = null, leafletReady = null, pickForm = null, addrTimer = null;
  function loadLeaflet() {
    if (leafletReady) return leafletReady;
    leafletReady = new Promise(function (res, rej) {
      var css = document.createElement('link'); css.rel = 'stylesheet'; css.href = '/assets/vendor/leaflet/leaflet.css'; document.head.appendChild(css);
      var s = document.createElement('script'); s.src = '/assets/vendor/leaflet/leaflet.js'; s.onload = res; s.onerror = function () { leafletReady = null; rej(); }; document.head.appendChild(s);
    });
    return leafletReady;
  }
  function mapMsg(key, raw) { var m = mapModal.querySelector('.map-msg'); m.textContent = key ? strip(t(key)) : (raw || ''); }
  function pinAddr() {
    var el = mapModal.querySelector('.map-addr'); clearTimeout(addrTimer);
    var c = pick.map.getCenter(); el.textContent = '📍 ' + c.lat.toFixed(5) + ', ' + c.lng.toFixed(5);
    addrTimer = setTimeout(function () {
      reverseGeo(c.lat.toFixed(6), c.lng.toFixed(6)).then(function (a) {
        var now = pick.map.getCenter(); if (Math.abs(now.lat - c.lat) > 1e-6 || Math.abs(now.lng - c.lng) > 1e-6) return;
        el.textContent = '📍 ' + (a || c.lat.toFixed(5) + ', ' + c.lng.toFixed(5)); pick.addr = a;
      });
    }, 700);
    pick.addr = '';
  }
  function goTo(lat, lng, zoom, acc) {
    pick.map.setView([lat, lng], zoom || 18);
    if (pick.accCircle) { pick.map.removeLayer(pick.accCircle); pick.accCircle = null; }
    if (acc) pick.accCircle = L.circle([lat, lng], { radius: acc, color: '#1688D4', weight: 1, fillOpacity: .08, interactive: false }).addTo(pick.map);
  }
  function openPicker(form) {
    pickForm = form; openModal(mapModal); mapMsg('');
    var sug = mapModal.querySelector('.map-sug'); sug.hidden = true;
    loadLeaflet().then(function () {
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (!pick) {
        pick = { map: L.map('pickMap', { zoomControl: true, maxZoom: 19 }).setView(HOME, 14) };
        pick.street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19, attribution: '&copy; OpenStreetMap contributors' }).addTo(pick.map);
        pick.sat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', { maxZoom: 19, maxNativeZoom: 18, attribution: 'Imagery &copy; Esri' });
        pick.map.on('move', function () { mapModal.querySelector('.pick-wrap').classList.add('moving'); });
        pick.map.on('moveend', function () { mapModal.querySelector('.pick-wrap').classList.remove('moving'); pinAddr(); });
        mapModal.querySelectorAll('.map-layers button').forEach(function (b) {
          b.addEventListener('click', function () {
            var sat = b.dataset.layer === 'sat';
            mapModal.querySelectorAll('.map-layers button').forEach(function (x) { x.classList.toggle('on', x === b); });
            if (sat) { pick.map.removeLayer(pick.street); pick.sat.addTo(pick.map); } else { pick.map.removeLayer(pick.sat); pick.street.addTo(pick.map); }
          });
        });
      }
      setTimeout(function () {
        pick.map.invalidateSize();
        if (lat && lng) goTo(+lat, +lng, 18, form._acc); else { goTo(HOME[0], HOME[1], 14); }
        pinAddr();
      }, 90);
    }).catch(function () { mapMsg('f.loc.fail'); });
  }
  if (mapModal) {
    var sInput = mapModal.querySelector('.map-search input'), sList = mapModal.querySelector('.map-sug'), sTimer = null, sSeq = 0, sItems = [], sAct = -1;
    function closeSug() { sList.hidden = true; sList.innerHTML = ''; sItems = []; sAct = -1; sInput.setAttribute('aria-expanded', 'false'); }
    function choose(r) { closeSug(); mapMsg(''); if (pick) goTo(r.lat, r.lng, r.zoom || 18); }
    function runSearch(q, auto) {
      q = q.trim(); if (!q || !pick) return closeSug();
      var c = parseCoords(q); if (c) { choose({ lat: c.lat, lng: c.lng, zoom: 19 }); return; }
      if (q.length < 3) return closeSug();
      var seq = ++sSeq; mapMsg('map.searching');
      searchPlaces(q).then(function (list) {
        if (seq !== sSeq) return;
        mapMsg(list.length ? '' : 'map.noresult');
        if (!list.length) return closeSug();
        if (!auto && list.length === 1) return choose(list[0]);
        sItems = list; sAct = -1;
        sList.innerHTML = list.map(function (r, i) {
          return '<li role="option" id="ms' + i + '" data-i="' + i + '"><b>' + String(r.name).replace(/</g, '&lt;') + '</b><small>' + String(r.sub || '').replace(/</g, '&lt;') + (r.km < 200 ? ' · ' + (r.km < 10 ? r.km.toFixed(1) : Math.round(r.km)) + ' km' : '') + '</small></li>';
        }).join('');
        sList.hidden = false; sInput.setAttribute('aria-expanded', 'true');
      });
    }
    sInput.addEventListener('input', function () { clearTimeout(sTimer); var v = sInput.value; if (parseCoords(v)) return runSearch(v); sTimer = setTimeout(function () { runSearch(v, true); }, 450); });
    sInput.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
        if (!sItems.length) return; e.preventDefault();
        sAct = (sAct + (e.key === 'ArrowDown' ? 1 : -1) + sItems.length) % sItems.length;
        [].forEach.call(sList.children, function (li, i) { li.classList.toggle('act', i === sAct); });
        sInput.setAttribute('aria-activedescendant', 'ms' + sAct);
      } else if (e.key === 'Enter') { e.preventDefault(); if (sAct >= 0) choose(sItems[sAct]); else { clearTimeout(sTimer); runSearch(sInput.value, false); } }
      else if (e.key === 'Escape' && !sList.hidden) { e.stopPropagation(); closeSug(); }
    });
    sList.addEventListener('mousedown', function (e) { var li = e.target.closest('li'); if (li) { e.preventDefault(); choose(sItems[+li.dataset.i]); } });
    mapModal.querySelector('.map-go').addEventListener('click', function () { clearTimeout(sTimer); runSearch(sInput.value, false); });
    mapModal.querySelector('.map-use').addEventListener('click', function () {
      if (pick && pickForm) {
        var c = pick.map.getCenter(), same = pickForm.elements.lat.value && Math.abs(+pickForm.elements.lat.value - c.lat) < 2e-6 && Math.abs(+pickForm.elements.lng.value - c.lng) < 2e-6;
        setLoc(pickForm, c.lat, c.lng, same ? pickForm._acc : null, pick.addr || '');
        if (pick.addr && !pickForm.elements.area.value.trim()) pickForm.elements.area.value = pick.addr.slice(0, 120);
      }
      closeSug(); closeModal(mapModal);
    });
    mapModal.querySelector('.map-me').addEventListener('click', function () {
      if (!window.isSecureContext) return mapMsg('f.loc.insecure');
      if (!navigator.geolocation || !pick) return mapMsg('f.loc.fail');
      mapMsg('f.loc.getting');
      var best = null, w = navigator.geolocation.watchPosition(function (pos) {
        if (!best || pos.coords.accuracy < best.accuracy) best = pos.coords;
        mapMsg('', fmt(strip(t('f.loc.improving')), { m: Math.round(best.accuracy) }));
        if (best.accuracy <= 20) end();
      }, function (err) { if (!best) { navigator.geolocation.clearWatch(w); mapMsg(err && err.code === 1 ? 'f.loc.denied' : 'f.loc.fail'); } }, { enableHighAccuracy: true, timeout: 20000, maximumAge: 0 });
      var ended = false;
      function end() { if (ended) return; ended = true; navigator.geolocation.clearWatch(w); if (best) { mapMsg(''); goTo(best.latitude, best.longitude, 18, best.accuracy); } }
      setTimeout(end, 12000);
    });
  }

  /* ---------- booking forms (Contact page + pop-up) ---------- */
  var NAME_RE = /^[\p{L}\p{M} .'-]{2,60}$/u;
  function today() { var d = new Date(); d.setMinutes(d.getMinutes() - d.getTimezoneOffset()); return d.toISOString().slice(0, 10); }
  document.querySelectorAll('.bookform').forEach(function (form) {
    var started = Date.now(), msgEl = form.querySelector('.form-msg'), done = form.querySelector('.book-done');
    var phoneEl = form.elements.phone, pcount = form.querySelector('.pcount');
    initLoc(form);
    if (form.elements.date) form.elements.date.min = today();
    function setErr(name, key) {
      var f = form.elements[name], wrap = f.closest('.field');
      wrap.classList.add('err'); f.setAttribute('aria-invalid', 'true');
      var em = wrap.querySelector('.emsg'); em.setAttribute('data-i18n', key); em.innerHTML = t(key); return f;
    }
    function clearErr(f) { var w = f.closest && f.closest('.field'); if (w) w.classList.remove('err'); if (f.removeAttribute) f.removeAttribute('aria-invalid'); }
    function check(name) {
      var el = form.elements[name], v = (el.value || '').trim();
      switch (name) {
        case 'name': return NAME_RE.test(v) ? null : (v ? 'f.err.name' : 'f.err.req');
        case 'phone': return /^[6-9]\d{9}$/.test(v) ? null : (v ? 'f.err.phone' : 'f.err.req');
        case 'appliance': case 'service': return v ? null : 'f.err.req';
        case 'area': return v.length >= 3 ? null : (v ? 'f.err.area' : 'f.err.req');
        case 'date': return !v || v >= today() ? null : 'f.err.date';
      }
      return null;
    }
    function renderCount() { var n = phoneEl.value.length; pcount.textContent = n ? fmt(strip(t('f.phone.count')), { n: n }) : ''; pcount.classList.toggle('full', n === 10); }
    /* phone: digits only, strip +91 / leading 0 when pasted, max 10 */
    phoneEl.addEventListener('input', function () {
      var d = phoneEl.value.replace(/\D/g, '');
      if (d.length > 10) d = d.replace(/^(?:91|0)(?=\d{10}$)/, '');
      phoneEl.value = d.slice(0, 10); renderCount();
    });
    phoneEl.addEventListener('paste', function (e) {
      var txt = (e.clipboardData || window.clipboardData).getData('text'); if (!txt) return;
      e.preventDefault(); var d = txt.replace(/\D/g, '').replace(/^(?:91|0)(?=\d{10}$)/, '');
      phoneEl.value = d.slice(0, 10); renderCount(); clearErr(phoneEl);
    });
    ['name', 'phone', 'area', 'date'].forEach(function (n) {
      var el = form.elements[n]; if (!el) return;
      el.addEventListener('blur', function () { if (el.value.trim()) { var k = check(n); if (k) setErr(n, k); } });
    });
    form.addEventListener('input', function (e) { if (e.target.name && !check(e.target.name)) clearErr(e.target); });
    form.addEventListener('change', function (e) { if (e.target.name && !check(e.target.name)) clearErr(e.target); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.elements.company.value) return;                 /* honeypot */
      if (Date.now() - started < 2000) return;                 /* too fast = bot */
      var first = null;
      ['name', 'phone', 'appliance', 'service', 'area', 'date'].forEach(function (n) {
        if (!form.elements[n]) return; clearErr(form.elements[n]);
        var k = check(n); if (k) { var f = setErr(n, k); first = first || f; }
      });
      if (first) { first.focus(); first.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' }); return; }
      function val(n) { var el = form.elements[n]; return el.tagName === 'SELECT' ? el.options[el.selectedIndex].text : el.value.trim(); }
      var lines = ['*' + strip(t('f.wa.title')) + ' – BOBBY AC Repair & Home Appliance Services*',
        strip(t('f.name')) + ': ' + val('name'),
        strip(t('f.phone')) + ': +91 ' + val('phone'),
        strip(t('f.appliance')) + ': ' + val('appliance') + (val('brand') ? ' (' + val('brand') + ')' : ''),
        strip(t('f.service')) + ': ' + val('service'),
        strip(t('f.area')) + ': ' + val('area')];
      var lat = form.elements.lat.value, lng = form.elements.lng.value;
      if (lat && lng) {
        lines.push('📍 ' + strip(t('f.wa.loc')) + ': ' + gmap(lat, lng) + (form._acc ? ' (±' + Math.round(form._acc) + ' m)' : ''));
        if (form.elements.addr.value) lines.push(strip(t('f.wa.addr')) + ': ' + form.elements.addr.value);
      }
      if (val('date')) lines.push(strip(t('f.date')) + ': ' + val('date'));
      if (val('msg')) lines.push(strip(t('f.msg')) + ': ' + val('msg').slice(0, 500));
      var url = waUrl(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
      /* thank-you screen */
      msgEl.textContent = '';
      done.querySelector('.bd-again').href = url;
      form.classList.add('is-done'); done.hidden = false;
      setTimeout(function () { done.focus({ preventScroll: true }); done.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' }); }, 30);
    });
    done.querySelector('.bd-new').addEventListener('click', function () {
      form.reset(); form.elements.lat.value = ''; form.elements.lng.value = ''; form.elements.addr.value = ''; form._acc = null; form._locErr = null;
      form._renderLoc(); renderCount(); form.classList.remove('is-done'); done.hidden = true; started = Date.now();
      form.elements.name.focus();
    });
    form._renderCount = renderCount;
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
      var mid = idx + Math.floor((p - 1) / 2);
      slides.forEach(function (s, k) { var vis = k >= idx && k < idx + p; s.setAttribute('aria-hidden', vis ? 'false' : 'true'); s.classList.toggle('is-focus', p > 1 && k === mid); });
      [].forEach.call(dotsBox.children, function (d, k) { d.setAttribute('aria-current', 'false'); }); var cd = dotsBox.children[idx]; if (cd) { void cd.offsetWidth; cd.setAttribute('aria-current', 'true'); }
      var single = m === 0; prev.disabled = single; next.disabled = single;
    }
    function play() { clearInterval(timer); rc.classList.toggle('is-paused', reduce || stopped || hover); if (!reduce && !stopped && !hover && maxIdx() > 0) timer = setInterval(function () { go(idx + 1); }, DELAY); }
    function pause() { clearInterval(timer); rc.classList.add('is-paused'); }
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
    rc.classList.add('is-js'); rc.style.setProperty('--rc-delay', DELAY / 1000 + 's');
    buildDots(); go(0); play();
  });
})();
