// POST /api/phonepe/pay  { amount: "1500", mobile?: "9xxxxxxxxx" } -> { redirectUrl, order }
import { cfg, token, newOrderId, rupeesToPaise, json, sameOrigin } from '../../../functions_lib/phonepe.js';

export async function onRequestPost({ request, env }) {
  const c = cfg(env);
  if (!c.ok) return json({ error: 'not_configured' }, 503);
  if (!sameOrigin(request)) return json({ error: 'forbidden' }, 403);
  let body = {};
  try { body = await request.json(); } catch (e) { return json({ error: 'bad_request' }, 400); }
  const amount = rupeesToPaise(body.amount);
  if (!amount) return json({ error: 'bad_amount' }, 400);
  const mobile = String(body.mobile || '').replace(/\D/g, '').slice(-10);

  const order = newOrderId();
  const origin = new URL(request.url).origin;
  const req = {
    merchantOrderId: order,
    amount,                                                      // paise
    expireAfter: 1200,                                           // 20 minutes to complete payment
    metaInfo: { udf1: 'website', udf2: 'BOBBY AC Services' },
    paymentFlow: {
      type: 'PG_CHECKOUT',
      message: 'BOBBY AC Repair & Home Appliance Services',
      merchantUrls: { redirectUrl: `${origin}/payment/?order=${order}` },
    },
  };
  if (/^[6-9]\d{9}$/.test(mobile)) req.prefillUserLoginDetails = { phoneNumber: mobile };
  try {
    const auth = await token(c);
    const r = await fetch(c.hosts.pg + '/checkout/v2/pay', { method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: auth }, body: JSON.stringify(req) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok || !j.redirectUrl) return json({ error: 'gateway_error', code: j.code || r.status }, 502);
    return json({ redirectUrl: j.redirectUrl, order });
  } catch (e) {
    return json({ error: String(e.message).startsWith('auth_failed') ? 'auth_failed' : 'gateway_unreachable' }, 502);
  }
}
