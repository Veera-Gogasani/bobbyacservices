// GET /api/phonepe/config -> tells the website whether PhonePe checkout is switched on (no secrets returned)
import { cfg, json } from '../../../functions_lib/phonepe.js';
export async function onRequestGet({ env }) {
  const c = cfg(env);
  return json({ enabled: c.ok, mode: c.ok ? c.mode : null });
}
