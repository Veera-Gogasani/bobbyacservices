/* Footer: compact live weather (all pages). Data: /api/weather (Cloudflare Pages Function, Open-Meteo),
   falling back to Open-Meteo directly for the two fixed cities. Refreshes every 15 minutes. */
(function () {
  'use strict';
  var box = document.querySelector('.fw');
  if (!box) return;
  var REFRESH = 15 * 60 * 1000, STORE = 'bobby-weather-city';
  var FIXED = [{ id: 'narasaraopet', name: 'Narasaraopet', lat: 16.23488, lon: 80.04927 }, { id: 'amaravati', name: 'Amaravati', lat: 16.514, lon: 80.516 }];
  var rows = {}; [].forEach.call(box.querySelectorAll('[data-fw]'), function (r) { rows[r.getAttribute('data-fw')] = r; });
  var form = box.querySelector('.fw-form'), input = form.querySelector('input'), changeBtn = box.querySelector('.fw-change'), autoBtn = box.querySelector('.fw-auto'), timeEl = box.querySelector('.fw-time');
  var timer = null, started = false, last = null;

  function store(v) { try { if (v === undefined) return localStorage.getItem(STORE); if (v === null) localStorage.removeItem(STORE); else localStorage.setItem(STORE, v); } catch (e) { return null; } }
  function lang() { return document.documentElement.getAttribute('lang') || 'en'; }
  var T = {
    en: { clear: 'Clear', clearN: 'Clear night', sunny: 'Mainly sunny', pc: 'Partly cloudy', over: 'Overcast', fog: 'Foggy', drizzle: 'Drizzle', rain: 'Rain', heavy: 'Heavy rain', showers: 'Showers', snow: 'Snow', storm: 'Thunderstorm', feels: 'feels', na: 'Unavailable', unav: 'Location unavailable', nf: 'not found', upd: 'Updated', approx: 'approx.' },
    te: { clear: 'నిర్మలం', clearN: 'నిర్మల రాత్రి', sunny: 'ఎండగా', pc: 'కొంత మేఘావృతం', over: 'మేఘావృతం', fog: 'పొగమంచు', drizzle: 'చినుకులు', rain: 'వర్షం', heavy: 'భారీ వర్షం', showers: 'జల్లులు', snow: 'మంచు', storm: 'ఉరుములతో వర్షం', feels: 'అనుభూతి', na: 'అందుబాటులో లేదు', unav: 'ప్రాంతం అందుబాటులో లేదు', nf: 'దొరకలేదు', upd: 'అప్‌డేట్', approx: 'సుమారు' },
    hi: { clear: 'साफ़', clearN: 'साफ़ रात', sunny: 'धूप', pc: 'आंशिक बादल', over: 'बादल', fog: 'कोहरा', drizzle: 'बूंदाबांदी', rain: 'बारिश', heavy: 'तेज़ बारिश', showers: 'बौछारें', snow: 'बर्फ़', storm: 'आंधी-तूफ़ान', feels: 'महसूस', na: 'उपलब्ध नहीं', unav: 'लोकेशन उपलब्ध नहीं', nf: 'नहीं मिला', upd: 'अपडेट', approx: 'लगभग' }
  };
  function t(k) { return (T[lang()] || T.en)[k] || T.en[k]; }

  function cond(c, day) {
    var n = day === false;
    if (c === 0) return [n ? 'clearN' : 'clear', n ? 'moon' : 'sun'];
    if (c === 1) return [n ? 'clearN' : 'sunny', n ? 'moon' : 'sun'];
    if (c === 2) return ['pc', n ? 'pcn' : 'pcd'];
    if (c === 3) return ['over', 'cloud'];
    if (c === 45 || c === 48) return ['fog', 'fog'];
    if (c >= 51 && c <= 57) return ['drizzle', 'rain'];
    if (c >= 61 && c <= 67) return [c >= 65 ? 'heavy' : 'rain', 'rain'];
    if (c >= 71 && c <= 77) return ['snow', 'snow'];
    if (c >= 80 && c <= 82) return ['showers', 'rain'];
    if (c >= 85 && c <= 86) return ['snow', 'snow'];
    if (c >= 95) return ['storm', 'storm'];
    return ['over', 'cloud'];
  }
  var CL = '<path d="M20 46h26a10 10 0 000-20 14 14 0 00-27-3 10 10 0 001 23z" fill="#E3EEF7"/>';
  var SUN = '<g class="fx-rays" stroke="#FFB061" stroke-width="4" stroke-linecap="round">' + [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) { return '<line x1="32" y1="5" x2="32" y2="12" transform="rotate(' + a + ' 32 32)"/>'; }).join('') + '</g><circle cx="32" cy="32" r="13" fill="#FF9F43"/>';
  var MOON = '<path d="M38 12a20 20 0 1 0 14 30 16 16 0 1 1-14-30z" fill="#F5E6B8"/>';
  function icon(k) {
    var s = {
      sun: SUN, moon: MOON + '<circle class="fx-star" cx="12" cy="14" r="2.4" fill="#fff"/><circle class="fx-star" cx="54" cy="50" r="2" fill="#fff"/>',
      pcd: '<g transform="translate(-8 -8) scale(.8)">' + SUN + '</g><g class="fx-cloud" transform="translate(4 8)">' + CL + '</g>',
      pcn: '<g transform="translate(-6 -8) scale(.75)">' + MOON + '</g><g class="fx-cloud" transform="translate(4 8)">' + CL + '</g>',
      cloud: '<g transform="translate(-8 -6) scale(.8)" opacity=".7">' + CL + '</g><g class="fx-cloud" transform="translate(4 6)">' + CL + '</g>',
      fog: '<g transform="translate(0 -6)">' + CL + '</g><g stroke="#CFE2F5" stroke-width="4" stroke-linecap="round"><line x1="12" y1="48" x2="50" y2="48"/><line x1="18" y1="56" x2="54" y2="56"/></g>',
      rain: '<g class="fx-cloud" transform="translate(0 -8)">' + CL + '</g><g class="fx-rain" stroke="#56C8FF" stroke-width="4" stroke-linecap="round"><line x1="24" y1="44" x2="21" y2="51"/><line x1="34" y1="44" x2="31" y2="51"/><line x1="44" y1="44" x2="41" y2="51"/></g>',
      storm: '<g transform="translate(0 -8)"><path d="M20 46h26a10 10 0 000-20 14 14 0 00-27-3 10 10 0 001 23z" fill="#B9C9DA"/></g><path class="fx-bolt" d="M34 38l-8 13h7l-3 10 11-15h-7l4-8z" fill="#FFB061"/>',
      snow: '<g transform="translate(0 -8)">' + CL + '</g><g fill="#fff"><circle cx="24" cy="48" r="2.6"/><circle cx="34" cy="51" r="2.6"/><circle cx="44" cy="48" r="2.6"/></g>'
    }[k] || '';
    return '<svg viewBox="0 0 64 64" aria-hidden="true" focusable="false">' + s + '</svg>';
  }
  function n(v) { return typeof v === 'number' && isFinite(v) ? Math.round(v) : null; }
  function istTime(iso) {
    try {
      var d = iso ? new Date(iso + (/[zZ]|[+-]\d\d:?\d\d$/.test(iso) ? '' : '+05:30')) : new Date(); if (isNaN(d)) d = new Date();
      return new Intl.DateTimeFormat(lang() === 'en' ? 'en-IN' : lang() + '-IN', { timeZone: 'Asia/Kolkata', hour: 'numeric', minute: '2-digit', hour12: true }).format(d) + ' IST';
    } catch (e) { return ''; }
  }

  function render(id, d) {
    var r = rows[id]; if (!r) return;
    var sub = r.querySelector('.fw-sub'), temp = r.querySelector('.fw-temp'), ic = r.querySelector('.fw-ic');
    r.classList.remove('is-loading', 'is-na');
    sub.removeAttribute('data-i18n');
    var tv = n(d && d.temp);
    if (!d || !d.ok || tv === null) {
      r.classList.add('is-na'); ic.innerHTML = ''; temp.textContent = '—';
      sub.textContent = id === 'you' ? (d && d.query ? '“' + d.query + '” ' + t('nf') : t('unav')) : t('na');
      r.title = sub.textContent; return;
    }
    var c = cond(d.code, d.isDay), parts = [t(c[0])];
    if (n(d.feels) !== null) parts.push(t('feels') + ' ' + n(d.feels) + '°');
    if (n(d.humidity) !== null) parts.push('💧' + n(d.humidity) + '%');
    if (n(d.wind) !== null) parts.push(n(d.wind) + ' km/h');
    if (id === 'you') {
      var place = [d.name, d.region].filter(Boolean).join(', ') || '—';
      r.querySelector('b').removeAttribute('data-i18n');
      r.querySelector('b').textContent = place;
      if (d.source === 'network') parts.unshift(t('approx'));
    }
    ic.innerHTML = icon(c[1]); temp.textContent = tv + '°C';
    sub.textContent = parts.join(' · ');
    r.title = (id === 'you' ? r.querySelector('b').textContent : r.querySelector('b').textContent) + ': ' + tv + '°C, ' + parts.join(', ');
    if (d.time) timeEl.textContent = t('upd') + ' ' + istTime(d.time);
  }

  function api(q) {
    return fetch('/api/weather' + (q ? '?q=' + encodeURIComponent(q) : ''), { headers: { Accept: 'application/json' } }).then(function (r) {
      if (!r.ok || (r.headers.get('content-type') || '').indexOf('json') < 0) throw new Error('api'); return r.json();
    });
  }
  function direct(q) {
    var geo = q ? fetch('https://geocoding-api.open-meteo.com/v1/search?count=1&language=en&format=json&name=' + encodeURIComponent(q)).then(function (r) { return r.json(); })
      .then(function (j) { var g = j && j.results && j.results[0]; return g ? { id: 'you', name: g.name, region: g.admin1 || '', lat: g.latitude, lon: g.longitude, source: 'manual' } : null; }).catch(function () { return null; }) : Promise.resolve(null);
    return geo.then(function (you) {
      var locs = [you].concat(FIXED).filter(Boolean);
      return fetch('https://api.open-meteo.com/v1/forecast?timezone=Asia%2FKolkata&latitude=' + locs.map(function (l) { return l.lat; }).join(',') + '&longitude=' + locs.map(function (l) { return l.lon; }).join(',') +
        '&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code,is_day').then(function (r) { return r.json(); }).then(function (data) {
        var list = Array.isArray(data) ? data : [data];
        var cards = locs.map(function (l, i) { var c = list[i] && list[i].current; return { id: l.id, name: l.name, region: l.region, source: l.source, ok: !!c && typeof c.temperature_2m === 'number', temp: c && c.temperature_2m, feels: c && c.apparent_temperature, humidity: c && c.relative_humidity_2m, wind: c && c.wind_speed_10m, code: c && c.weather_code, isDay: c ? c.is_day === 1 : null, time: c && c.time }; });
        if (!you) cards.unshift({ id: 'you', ok: false, unavailable: true, query: q || null });
        return { cards: cards };
      });
    });
  }
  function load() {
    var q = store() || ''; autoBtn.hidden = !q;
    api(q).catch(function () { return direct(q); }).then(function (res) {
      last = res; var seen = {};
      (res.cards || []).forEach(function (c) { seen[c.id] = 1; render(c.id, c); });
      Object.keys(rows).forEach(function (id) { if (!seen[id]) render(id, null); });
    }).catch(function () { Object.keys(rows).forEach(function (id) { render(id, null); }); });
    clearTimeout(timer); timer = setTimeout(function tick() { if (document.hidden) { timer = setTimeout(tick, 60000); return; } load(); }, REFRESH);
  }
  function start() { if (started) return; started = true; load(); }

  changeBtn.addEventListener('click', function () { form.hidden = !form.hidden; if (!form.hidden) { input.value = store() || ''; input.focus(); } });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = input.value.replace(/[^\p{L}\p{M}\s.,'-]/gu, '').trim().slice(0, 60); if (!v) return input.focus();
    store(v); form.hidden = true; rows.you.classList.add('is-loading'); load();
  });
  autoBtn.addEventListener('click', function () { store(null); rows.you.classList.add('is-loading'); load(); });
  /* re-render text when the visitor switches language */
  new MutationObserver(function () { if (last) (last.cards || []).forEach(function (c) { render(c.id, c); }); }).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) { if (en[0].isIntersecting) { io.disconnect(); start(); } }, { rootMargin: '800px 0px' });
    io.observe(box);
  }
  function later() { setTimeout(start, 3000); }
  if (document.readyState === 'complete') later(); else window.addEventListener('load', later);
})();
