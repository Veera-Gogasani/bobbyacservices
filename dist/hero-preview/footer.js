/* BOBBY footer – live weather (preview). Data: /api/weather (Cloudflare Pages Function) with an
   Open-Meteo fallback for the two fixed cities. No libraries; all identifiers prefixed bobby-footer. */
(function () {
  'use strict';
  var bobbyFooterRoot = document.querySelector('.bobby-footer');
  if (!bobbyFooterRoot) return;
  var REFRESH_MS = 15 * 60 * 1000, TZ = 'Asia/Kolkata', STORE = 'bobby-footer-city';
  var FIXED = { narasaraopet: { lat: 16.23488, lon: 80.04927, name: 'Narasaraopet' }, amaravati: { lat: 16.514, lon: 80.516, name: 'Amaravati' } };
  var cards = {};
  [].forEach.call(bobbyFooterRoot.querySelectorAll('[data-bobby-footer-card]'), function (c) { cards[c.getAttribute('data-bobby-footer-card')] = c; });
  var form = bobbyFooterRoot.querySelector('.bobby-footer-wform'), input = form.querySelector('input'), resetBtn = form.querySelector('.bobby-footer-wreset');
  var refreshBtn = bobbyFooterRoot.querySelector('.bobby-footer-refresh');
  var timer = null, started = false, busy = false;

  function bobbyFooterStore(v) { try { if (v === undefined) return localStorage.getItem(STORE); if (v === null) localStorage.removeItem(STORE); else localStorage.setItem(STORE, v); } catch (e) { return null; } }

  /* ---- WMO weather codes → label + icon type ---- */
  function bobbyFooterCond(code, isDay) {
    var c = code, n = isDay === false;
    if (c === 0) return { t: n ? 'Clear night' : 'Clear sky', i: n ? 'moon' : 'sun' };
    if (c === 1) return { t: n ? 'Mostly clear' : 'Mainly sunny', i: n ? 'moon' : 'sun' };
    if (c === 2) return { t: 'Partly cloudy', i: n ? 'pcn' : 'pcd' };
    if (c === 3) return { t: 'Overcast', i: 'cloud' };
    if (c === 45 || c === 48) return { t: 'Foggy', i: 'fog' };
    if (c >= 51 && c <= 57) return { t: 'Drizzle', i: 'rain' };
    if (c >= 61 && c <= 67) return { t: c >= 65 ? 'Heavy rain' : 'Rain', i: 'rain' };
    if (c >= 71 && c <= 77) return { t: 'Snow', i: 'snow' };
    if (c >= 80 && c <= 82) return { t: 'Rain showers', i: 'rain' };
    if (c >= 85 && c <= 86) return { t: 'Snow showers', i: 'snow' };
    if (c >= 95) return { t: 'Thunderstorm', i: 'storm' };
    return { t: 'Weather', i: 'cloud' };
  }
  var CL = '<path d="M20 46h26a10 10 0 000-20 14 14 0 00-27-3 10 10 0 001 23z" fill="#E3EEF7"/>';
  function bobbyFooterIcon(type) {
    var sun = '<g class="bobby-footer-rays" stroke="#FFB061" stroke-width="3.5" stroke-linecap="round">' +
      [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) { return '<line x1="32" y1="6" x2="32" y2="12" transform="rotate(' + a + ' 32 32)"/>'; }).join('') + '</g><circle cx="32" cy="32" r="13" fill="#FF9F43"/>';
    var moon = '<path d="M38 12a20 20 0 1 0 14 30 16 16 0 1 1-14-30z" fill="#F5E6B8"/><circle class="bobby-footer-star" cx="12" cy="14" r="2" fill="#fff"/><circle class="bobby-footer-star" cx="54" cy="12" r="1.6" fill="#fff"/><circle class="bobby-footer-star" cx="50" cy="52" r="1.8" fill="#fff"/>';
    var svg = {
      sun: sun,
      moon: moon,
      pcd: '<g transform="translate(-8 -8) scale(.8)">' + sun + '</g><g class="bobby-footer-cloud" transform="translate(4 8)">' + CL + '</g>',
      pcn: '<g transform="translate(-6 -8) scale(.75)"><path d="M38 12a20 20 0 1 0 14 30 16 16 0 1 1-14-30z" fill="#F5E6B8"/></g><g class="bobby-footer-cloud" transform="translate(4 8)">' + CL + '</g>',
      cloud: '<g class="bobby-footer-cloud b" transform="translate(-8 -6) scale(.8)" opacity=".7">' + CL + '</g><g class="bobby-footer-cloud" transform="translate(4 6)">' + CL + '</g>',
      fog: '<g class="bobby-footer-cloud" transform="translate(0 -6)">' + CL + '</g><g class="bobby-footer-fog" stroke="#CFE2F5" stroke-width="3.5" stroke-linecap="round"><line x1="12" y1="48" x2="50" y2="48"/><line x1="18" y1="55" x2="54" y2="55"/></g>',
      rain: '<g class="bobby-footer-cloud" transform="translate(0 -8)">' + CL + '</g><g class="bobby-footer-rain" stroke="#56C8FF" stroke-width="3.5" stroke-linecap="round"><line x1="24" y1="44" x2="21" y2="51"/><line x1="34" y1="44" x2="31" y2="51"/><line x1="44" y1="44" x2="41" y2="51"/></g>',
      storm: '<g transform="translate(0 -8)"><path d="M20 46h26a10 10 0 000-20 14 14 0 00-27-3 10 10 0 001 23z" fill="#B9C9DA"/></g><path class="bobby-footer-bolt" d="M34 38l-8 13h7l-3 10 11-15h-7l4-8z" fill="#FFB061"/>',
      snow: '<g class="bobby-footer-cloud" transform="translate(0 -8)">' + CL + '</g><g class="bobby-footer-rain" fill="#fff"><circle cx="24" cy="48" r="2.4"/><circle cx="34" cy="50" r="2.4"/><circle cx="44" cy="48" r="2.4"/></g>'
    }[type] || '';
    return '<svg viewBox="0 0 64 64" role="img" aria-hidden="true">' + svg + '</svg>';
  }

  function bobbyFooterTime(iso) {
    try {
      var d = iso ? new Date(iso + (/[zZ]|[+-]\d\d:?\d\d$/.test(iso) ? '' : '+05:30')) : new Date();
      if (isNaN(d)) d = new Date();
      return new Intl.DateTimeFormat('en-IN', { timeZone: TZ, hour: 'numeric', minute: '2-digit', hour12: true, day: 'numeric', month: 'short' }).format(d) + ' IST';
    } catch (e) { return ''; }
  }
  var fmtNum = function (v, d) { return (typeof v === 'number' && isFinite(v)) ? (d ? v.toFixed(d) : Math.round(v)) : null; };

  function bobbyFooterSet(card, html, sel) { var el = card.querySelector(sel); if (el) el.innerHTML = html; }
  function bobbyFooterPlace(card, text) { card.querySelector('.bobby-footer-wplace span').textContent = text; }

  function bobbyFooterRender(id, d) {
    var card = cards[id]; if (!card) return;
    card.classList.remove('is-loading', 'is-error', 'is-unavailable');
    var t = fmtNum(d && d.temp);
    if (!d || !d.ok || t === null) {
      card.classList.add(d && d.unavailable ? 'is-unavailable' : 'is-error');
      if (id === 'you') bobbyFooterPlace(card, d && d.query ? '“' + d.query + '” not found' : 'Location unavailable');
      bobbyFooterSet(card, '', '.bobby-footer-wicon');
      bobbyFooterSet(card, id === 'you' ? 'Location unavailable' : 'Weather unavailable', '.bobby-footer-wtemp');
      bobbyFooterSet(card, id === 'you' ? 'Type your town below to see its weather.' : 'Please try again shortly.', '.bobby-footer-wcond');
      ['feels', 'humidity', 'wind'].forEach(function (k) { card.querySelector('[data-k="' + k + '"]').textContent = '—'; });
      card.querySelector('.bobby-footer-wtime span').textContent = 'Not updated';
      return;
    }
    if (id === 'you') {
      var place = [d.name, d.region].filter(Boolean).join(', ') || 'Your area';
      if (d.country && d.country !== 'IN') place += ' · ' + d.country;
      bobbyFooterPlace(card, place + (d.source === 'network' ? ' (approx.)' : ''));
    }
    var cond = bobbyFooterCond(d.code, d.isDay);
    bobbyFooterSet(card, bobbyFooterIcon(cond.i), '.bobby-footer-wicon');
    card.querySelector('.bobby-footer-wtemp').innerHTML = t + '<sup>°C</sup>';
    card.querySelector('.bobby-footer-wtemp').setAttribute('aria-label', t + ' degrees Celsius');
    card.querySelector('.bobby-footer-wcond').textContent = cond.t;
    var f = fmtNum(d.feels), h = fmtNum(d.humidity), w = fmtNum(d.wind);
    card.querySelector('[data-k="feels"]').textContent = f === null ? '—' : f + '°C';
    card.querySelector('[data-k="humidity"]').textContent = h === null ? '—' : h + '%';
    card.querySelector('[data-k="wind"]').textContent = w === null ? '—' : w + ' km/h';
    card.querySelector('.bobby-footer-wtime span').textContent = 'Updated ' + bobbyFooterTime(d.time);
  }

  /* ---- data sources ---- */
  function bobbyFooterFromApi(q) {
    return fetch('/api/weather' + (q ? '?q=' + encodeURIComponent(q) : ''), { headers: { Accept: 'application/json' } }).then(function (r) {
      if (!r.ok || (r.headers.get('content-type') || '').indexOf('json') < 0) throw new Error('api');
      return r.json();
    });
  }
  /* Fallback (e.g. local preview without Functions): call Open-Meteo directly for the fixed cities / a typed town */
  function bobbyFooterDirect(q) {
    var geo = q ? fetch('https://geocoding-api.open-meteo.com/v1/search?count=1&language=en&format=json&name=' + encodeURIComponent(q)).then(function (r) { return r.json(); })
      .then(function (j) { var g = j && j.results && j.results[0]; return g ? { id: 'you', name: g.name, region: g.admin1 || '', country: g.country_code || '', lat: g.latitude, lon: g.longitude, source: 'manual' } : null; }).catch(function () { return null; })
      : Promise.resolve(null);
    return geo.then(function (you) {
      var locs = [you, { id: 'narasaraopet', name: 'Narasaraopet', lat: FIXED.narasaraopet.lat, lon: FIXED.narasaraopet.lon }, { id: 'amaravati', name: 'Amaravati', lat: FIXED.amaravati.lat, lon: FIXED.amaravati.lon }].filter(Boolean);
      var url = 'https://api.open-meteo.com/v1/forecast?timezone=Asia%2FKolkata&latitude=' + locs.map(function (l) { return l.lat; }).join(',') + '&longitude=' + locs.map(function (l) { return l.lon; }).join(',') +
        '&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code,is_day';
      return fetch(url).then(function (r) { return r.json(); }).then(function (data) {
        var list = Array.isArray(data) ? data : [data];
        var out = locs.map(function (l, i) {
          var c = list[i] && list[i].current;
          return { id: l.id, name: l.name, region: l.region, country: l.country, source: l.source, ok: !!c && typeof c.temperature_2m === 'number', temp: c && c.temperature_2m, feels: c && c.apparent_temperature, humidity: c && c.relative_humidity_2m, wind: c && c.wind_speed_10m, code: c && c.weather_code, isDay: c ? c.is_day === 1 : null, time: c && c.time };
        });
        if (!you) out.unshift({ id: 'you', ok: false, unavailable: true, query: q || null });
        return { cards: out };
      });
    });
  }

  function bobbyFooterLoad() {
    if (busy) return; busy = true; refreshBtn.classList.add('is-spin');
    var q = bobbyFooterStore() || '';
    resetBtn.hidden = !q; if (q && !input.value) input.value = q;
    bobbyFooterFromApi(q).catch(function () { return bobbyFooterDirect(q); }).then(function (res) {
      var seen = {};
      (res.cards || []).forEach(function (c) { seen[c.id] = 1; bobbyFooterRender(c.id, c); });
      Object.keys(cards).forEach(function (id) { if (!seen[id]) bobbyFooterRender(id, null); });
    }).catch(function () { Object.keys(cards).forEach(function (id) { bobbyFooterRender(id, null); }); })
      .then(function () { busy = false; refreshBtn.classList.remove('is-spin'); });
    clearTimeout(timer); timer = setTimeout(function tick() { if (document.hidden) { timer = setTimeout(tick, 60000); return; } bobbyFooterLoad(); }, REFRESH_MS);
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = input.value.replace(/[^\p{L}\p{M}\s.,'-]/gu, '').trim().slice(0, 60);
    if (!v) { input.focus(); return; }
    bobbyFooterStore(v); cards.you.classList.add('is-loading'); bobbyFooterPlace(cards.you, 'Loading ' + v + '…'); bobbyFooterLoad();
  });
  resetBtn.addEventListener('click', function () { bobbyFooterStore(null); input.value = ''; cards.you.classList.add('is-loading'); bobbyFooterPlace(cards.you, 'Detecting…'); bobbyFooterLoad(); });
  refreshBtn.addEventListener('click', bobbyFooterLoad);

  /* load when the footer is about to appear */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) { if (en[0].isIntersecting && !started) { started = true; io.disconnect(); bobbyFooterLoad(); } }, { rootMargin: '600px 0px' });
    io.observe(bobbyFooterRoot);
  } else { started = true; bobbyFooterLoad(); }
})();
