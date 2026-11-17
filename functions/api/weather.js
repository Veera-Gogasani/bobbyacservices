/**
 * GET /api/weather            -> weather for the visitor's approximate city (Cloudflare request.cf) + Narasaraopet + Amaravati
 * GET /api/weather?q=Guntur   -> same, with the first card for a manually chosen place
 * Data: Open-Meteo (no API key). Responses cached ~10 minutes. Visitor IPs are never read or stored;
 * only Cloudflare's city-level coordinates are used, rounded to ~1 km before any request or cache key.
 */
const FIXED = [
  { id: 'narasaraopet', name: 'Narasaraopet', region: 'Andhra Pradesh', country: 'IN', lat: 16.23488, lon: 80.04927 }, // Open-Meteo geocoding
  { id: 'amaravati', name: 'Amaravati', region: 'Andhra Pradesh', country: 'IN', lat: 16.514, lon: 80.516 },           // Open-Meteo geocoding
];
const TTL = 600; // seconds
const CURRENT = 'temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code,is_day';

const num = (v) => (typeof v === 'number' && Number.isFinite(v) ? v : null);
const r2 = (v) => Math.round(v * 100) / 100;

async function cachedJson(url, ctx) {
  const cache = caches.default;
  const key = new Request(url);
  let res = await cache.match(key);
  if (!res) {
    const up = await fetch(url, { cf: { cacheTtl: TTL, cacheEverything: true } });
    if (!up.ok) throw new Error('upstream ' + up.status);
    res = new Response(up.body, up);
    res.headers.set('Cache-Control', `public, max-age=${TTL}`);
    ctx.waitUntil(cache.put(key, res.clone()));
  }
  return res.json();
}

async function geocode(q, ctx) {
  const url = 'https://geocoding-api.open-meteo.com/v1/search?count=1&language=en&format=json&name=' + encodeURIComponent(q);
  const j = await cachedJson(url, ctx);
  const g = j && j.results && j.results[0];
  if (!g) return null;
  return { id: 'you', name: g.name, region: g.admin1 || '', country: g.country_code || '', lat: g.latitude, lon: g.longitude, source: 'manual' };
}

export async function onRequestGet(ctx) {
  const { request } = ctx;
  const url = new URL(request.url);
  const q = (url.searchParams.get('q') || '').replace(/[^\p{L}\p{M}\s.,'-]/gu, '').trim().slice(0, 60);
  let you = null;
  try {
    if (q) you = await geocode(q, ctx);
    else {
      const cf = request.cf || {};
      const lat = parseFloat(cf.latitude), lon = parseFloat(cf.longitude);
      if (Number.isFinite(lat) && Number.isFinite(lon)) {
        you = { id: 'you', name: cf.city || '', region: cf.region || '', country: cf.country || '', lat, lon, source: 'network' };
      }
    }
  } catch (e) { you = null; }

  const locs = [you, ...FIXED].filter(Boolean);
  const wurl = 'https://api.open-meteo.com/v1/forecast?timezone=Asia%2FKolkata&temperature_unit=celsius&wind_speed_unit=kmh'
    + '&latitude=' + locs.map((l) => r2(l.lat)).join(',') + '&longitude=' + locs.map((l) => r2(l.lon)).join(',') + '&current=' + CURRENT;

  let data = null;
  try { data = await cachedJson(wurl, ctx); } catch (e) { data = null; }
  const list = Array.isArray(data) ? data : data ? [data] : [];

  const card = (l, w) => {
    const c = w && w.current;
    return {
      id: l.id, name: l.name, region: l.region, country: l.country, source: l.source || 'fixed',
      ok: !!c && num(c.temperature_2m) !== null,
      temp: c ? num(c.temperature_2m) : null, feels: c ? num(c.apparent_temperature) : null,
      humidity: c ? num(c.relative_humidity_2m) : null, wind: c ? num(c.wind_speed_10m) : null,
      code: c ? num(c.weather_code) : null, isDay: c ? c.is_day === 1 : null, time: c ? c.time : null,
    };
  };
  const cards = locs.map((l, i) => card(l, list[i]));
  if (!you) cards.unshift({ id: 'you', ok: false, unavailable: true, query: q || null });

  return new Response(JSON.stringify({ tz: 'Asia/Kolkata', ttl: TTL, cards }), {
    headers: {
      'Content-Type': 'application/json; charset=utf-8',
      'Cache-Control': 'private, max-age=300',
      'X-Robots-Tag': 'noindex',
    },
  });
}
