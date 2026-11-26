/**
 * PhonePe Payment Gateway (Standard Checkout v2) helper for BOBBY's Cloudflare Pages Functions.
 * Credentials live ONLY in Cloudflare environment variables (never in the website code):
 *   PHONEPE_CLIENT_ID, PHONEPE_CLIENT_SECRET, PHONEPE_CLIENT_VERSION (default "1"),
 *   PHONEPE_ENV = "sandbox" (testing) or "production" (real money). Default: sandbox.
 * Docs: https://developer.phonepe.com/payment-gateway/website-integration/standard-checkout/api-integration/api-integration-website
 */
const HOSTS = {
  sandbox:    { auth: 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token', pg: 'https://api-preprod.phonepe.com/apis/pg-sandbox' },
  production: { auth: 'https://api.phonepe.com/apis/identity-manager/v1/oauth/token',  pg: 'https://api.phonepe.com/apis/pg' },
};
export const MIN_RUPEES = 1, MAX_RUPEES = 100000;
export const ORDER_RE = /^BOBBY-[0-9]{8}-[0-9]{6}-[A-Z0-9]{6}$/;

export function cfg(env) {
  const mode = String(env.PHONEPE_ENV || 'sandbox').toLowerCase() === 'production' ? 'production' : 'sandbox';
  const ok = !!(env.PHONEPE_CLIENT_ID && env.PHONEPE_CLIENT_SECRET);
  return { ok, mode, hosts: HOSTS[mode], id: env.PHONEPE_CLIENT_ID, secret: env.PHONEPE_CLIENT_SECRET, version: String(env.PHONEPE_CLIENT_VERSION || '1') };
}

let cached = null;   // { key, token, exp } – reused while valid inside this worker instance
export async function token(c, fetchImpl = fetch) {
  const key = c.mode + ':' + c.id;
  const now = Math.floor(Date.now() / 1000);
  if (cached && cached.key === key && cached.exp - 120 > now) return cached.token;
  const body = new URLSearchParams({ client_id: c.id, client_version: c.version, client_secret: c.secret, grant_type: 'client_credentials' });
  const r = await fetchImpl(c.hosts.auth, { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body });
  const j = await r.json().catch(() => ({}));
  if (!r.ok || !j.access_token) throw new Error('auth_failed_' + r.status);
  cached = { key, token: (j.token_type || 'O-Bearer') + ' ' + j.access_token, exp: Number(j.expires_at) || now + 600 };
  return cached.token;
}

export function newOrderId(d = new Date()) {
  const ist = new Date(d.getTime() + 330 * 60000);             // IST timestamp in the ID, easy to match in PhonePe dashboard
  const p = (n, l = 2) => String(n).padStart(l, '0');
  const rnd = Array.from(crypto.getRandomValues(new Uint8Array(6)), b => 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'[b % 32]).join('');
  return `BOBBY-${ist.getUTCFullYear()}${p(ist.getUTCMonth() + 1)}${p(ist.getUTCDate())}-${p(ist.getUTCHours())}${p(ist.getUTCMinutes())}${p(ist.getUTCSeconds())}-${rnd}`;
}

export function rupeesToPaise(v) {
  const s = String(v == null ? '' : v).replace(/[,\s₹]/g, '');
  if (!/^\d{1,6}(\.\d{1,2})?$/.test(s)) return null;
  const paise = Math.round(parseFloat(s) * 100);
  return paise >= MIN_RUPEES * 100 && paise <= MAX_RUPEES * 100 ? paise : null;
}

export function json(data, status = 200) {
  return new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Robots-Tag': 'noindex' } });
}

export function sameOrigin(request) {
  const o = request.headers.get('Origin');
  if (!o) return true;                                          // same-origin fetches may omit Origin
  try { return new URL(o).host === new URL(request.url).host; } catch (e) { return false; }
}
