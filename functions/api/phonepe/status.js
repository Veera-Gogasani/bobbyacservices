// GET /api/phonepe/status?order=BOBBY-... -> { state: COMPLETED | PENDING | FAILED, amount (rupees) }
// The website trusts ONLY this server-side check (never the redirect itself) before saying "payment successful".
import { cfg, token, json, ORDER_RE } from '../../../functions_lib/phonepe.js';

export async function onRequestGet({ request, env }) {
  const c = cfg(env);
  if (!c.ok) return json({ error: 'not_configured' }, 503);
  const order = new URL(request.url).searchParams.get('order') || '';
  if (!ORDER_RE.test(order)) return json({ error: 'bad_order' }, 400);
  try {
    const auth = await token(c);
    const r = await fetch(`${c.hosts.pg}/checkout/v2/order/${encodeURIComponent(order)}/status?details=false`, { headers: { 'Content-Type': 'application/json', Authorization: auth } });
    const j = await r.json().catch(() => ({}));
    if (!r.ok || !j.state) return json({ error: 'gateway_error', code: j.code || r.status }, 502);
    const state = ['COMPLETED', 'FAILED', 'PENDING'].includes(j.state) ? j.state : 'PENDING';
    return json({ order, state, amount: typeof j.amount === 'number' ? j.amount / 100 : null });
  } catch (e) {
    return json({ error: String(e.message).startsWith('auth_failed') ? 'auth_failed' : 'gateway_unreachable' }, 502);
  }
}
