/* BOBBY — scroll-driven 3D split-AC assembly & installation story.
   Loaded lazily by an inline loader in the home page when the section nears the viewport. */
import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { buildIndoor, buildOutdoor, buildRoom, buildPiping, buildAirflow } from './models.js';

/* ---------- timeline (fractions of the pinned scroll) ---------- */
const T = { s1: [0, 0.06], ind: [0.06, 0.38], indDone: [0.38, 0.43], outIntro: [0.43, 0.46], out: [0.46, 0.68], ins: [0.68, 0.86], cool: [0.86, 1] };
const STAGES = [0, T.ind[0], T.outIntro[0], T.ins[0], T.cool[0]];
const A = new THREE.Vector3(0.45, 2.05, 0.12);   /* indoor unit mounted position */
const B = new THREE.Vector3(1.8, 0.77, 0.2);     /* outdoor unit on brackets */
const IN_KEYS = ['in1', 'in2', 'in3', 'in4', 'in5', 'in6', 'in7', 'in8', 'in9', 'in10', 'in11', 'in12'];
const OUT_ORDER = ['cabinet', 'compressor', 'condenser', 'fan', 'fmotor', 'mpcb', 'capacitor', 'valves', 'terminal', 'grille'];
const INS_KEYS = ['ins1', 'ins2', 'ins3', 'ins4', 'ins5', 'ins6', 'ins7'];

const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const seg = (p, [a, b]) => clamp((p - a) / (b - a));
const ease = (t) => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
const smooth = (a, b, t) => { const x = clamp((t - a) / (b - a)); return x * x * (3 - 2 * x); };
const lerp = (a, b, t) => a + (b - a) * t;

function init(sec) {
  const stage = sec.querySelector('.asm-stage'), track = sec.querySelector('.asm-track');
  const host = sec.querySelector('.asm-canvas');
  const card = sec.querySelector('.asm-card'), cN = card.querySelector('.n'), cT = card.querySelector('.t'), cD = card.querySelector('.d');
  const svg = sec.querySelector('.asm-lines'), path = svg.querySelector('path'), dot = svg.querySelector('circle');
  const bar = sec.querySelector('.asm-bar i'), steps = [...sec.querySelectorAll('.asm-steps button')];
  const cur = sec.querySelector('.asm-cur'), intro = sec.querySelector('.asm-intro'), finalEl = sec.querySelector('.asm-final');
  const tagsBox = sec.querySelector('.asm-tags'), note = sec.querySelector('.asm-note');
  const txt = (k) => { const li = sec.querySelector('.asm-data [data-k="' + k + '"]'); return li ? [li.querySelector('b').innerHTML, li.querySelector('span').innerHTML] : ['', '']; };
  const lbl = (k) => { const e = sec.querySelector('[data-i18n="asm.' + k + '"]'); return e ? e.innerHTML : ''; };

  const W0 = () => stage.clientWidth, H0 = () => stage.clientHeight;
  const low = Math.min(screen.width, screen.height) < 600 || (navigator.deviceMemory || 8) < 4;
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' }); }
  catch (e) { sec.classList.add('asm-static'); return; }
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, low ? 1.5 : 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.0;
  renderer.shadowMap.enabled = !low; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  host.appendChild(renderer.domElement);
  renderer.domElement.addEventListener('webglcontextlost', (e) => { e.preventDefault(); sec.classList.add('asm-static'); active = false; });

  const scene = new THREE.Scene();
  const navy = new THREE.Color(0x071A33), coolBg = new THREE.Color(0x06223F);
  scene.background = navy.clone(); scene.fog = new THREE.Fog(0x071A33, 12, 34);
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.55;
  const hemi = new THREE.HemisphereLight(0xDDEBFF, 0x1B2A3D, 0.7); scene.add(hemi);
  const key = new THREE.DirectionalLight(0xFFF3E2, 2.1); key.position.set(2.2, 4.2, 4.5); key.castShadow = !low;
  key.shadow.mapSize.set(1024, 1024); Object.assign(key.shadow.camera, { left: -2.5, right: 2.5, top: 2.5, bottom: -2.5, near: 1, far: 12 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02;
  key.target.position.set(1.1, 1.2, 0.3); scene.add(key, key.target);
  const rim = new THREE.DirectionalLight(0x6FB7FF, 1.2); rim.position.set(-3, 2, -2); scene.add(rim);
  const coolLight = new THREE.PointLight(0x7CCBFF, 0, 3.2, 1.6); coolLight.position.copy(A).add(new THREE.Vector3(0, -0.6, 0.8)); scene.add(coolLight);
  const camera = new THREE.PerspectiveCamera(34, 1, 0.05, 40);

  /* ---------- models ---------- */
  const ind = buildIndoor(low), out = buildOutdoor(low), room = buildRoom(low), pipe = buildPiping(low), air = buildAirflow(low);
  scene.add(ind.unit, out.unit, room.group, air.group); pipe.all.forEach((m) => scene.add(m));
  ind.unit.position.copy(A); out.unit.position.copy(B);
  air.group.position.copy(A).add(new THREE.Vector3(0, -0.15, 0.14)); air.group.visible = false;
  room.group.visible = false;
  /* per-part material clones so a single part can be highlighted */
  const prep = (U) => { for (const k of U.order) { const g = U.P[k]; g.userData.mats = []; g.userData.home = g.position.clone();
    g.traverse((o) => { if (o.isMesh && o.material && o.material.isMeshStandardMaterial) { o.material = o.material.clone(); g.userData.mats.push(o.material); } }); } };
  prep(ind); prep(out);
  const highlight = (g, v) => { for (const m of g.userData.mats) { m.emissive.setHex(0x2F8CFF); m.emissiveIntensity = v * 0.38; } };
  /* outdoor display text hooks */
  const valveAnchor = out.P.valveTip;

  /* ---------- layout ---------- */
  let w = 1, h = 1, portrait = false, mobile = false;
  const bbIn = { ex: new THREE.Vector3(), as: new THREE.Vector3() }, bbOut = { ex: new THREE.Vector3(), as: new THREE.Vector3() };
  const exScale = new THREE.Vector3(1, 1, 1);
  const measure = (U, store) => {
    const save = U.unit.position.clone(), rotY = U.unit.rotation.y; U.unit.position.set(0, 0, 0); U.unit.rotation.set(0, 0, 0);
    const st = U.order.map((k) => [U.P[k].scale.x, U.P[k].visible, U.P[k].rotation.clone()]);
    for (const k of U.order) { U.P[k].scale.setScalar(1); U.P[k].visible = true; U.P[k].rotation.set(0, 0, 0); }
    U.unit.updateMatrixWorld(true);
    const b = new THREE.Box3();
    for (const k of U.order) { const g = U.P[k]; g.position.copy(g.userData.home).add(new THREE.Vector3(...U.explode[k]).multiply(exScale)); }
    U.unit.updateMatrixWorld(true); b.setFromObject(U.unit); store.ex.set(Math.max(-b.min.x, b.max.x), Math.max(-b.min.y, b.max.y), Math.max(-b.min.z, b.max.z));
    for (const k of U.order) U.P[k].position.copy(U.P[k].userData.home);
    U.unit.updateMatrixWorld(true); b.setFromObject(U.unit); store.as.set(Math.max(-b.min.x, b.max.x), Math.max(-b.min.y, b.max.y), Math.max(-b.min.z, b.max.z));
    U.order.forEach((k, i) => { U.P[k].scale.setScalar(st[i][0]); U.P[k].visible = st[i][1]; U.P[k].rotation.copy(st[i][2]); });
    U.unit.position.copy(save); U.unit.rotation.y = rotY;
  };
  let region = { top: 0, bottom: 0, side: 0 };
  function resize() {
    w = W0(); h = H0(); portrait = w / h < 0.95; mobile = w < 760;
    renderer.setSize(w, h, false);
    const hdr = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--hdr')) || 76;
    region = mobile ? { top: hdr + 54, bottom: Math.min(h * 0.34, 230) + (document.querySelector('.mbar') ? 74 : 0), side: 0 }
                    : { top: hdr + 70, bottom: 92, side: Math.min(340, w * 0.24) };
    exScale.set(portrait ? 0.5 : 1, portrait ? 1.35 : 1, portrait ? 0.8 : 1);
    measure(ind, bbIn); measure(out, bbOut);
    camera.aspect = w / h;
    const cy = (region.top + (h - region.bottom)) / 2;
    camera.setViewOffset(w, h, 0, h / 2 - cy, w, h); camera.updateProjectionMatrix();
  }
  /* distance that fits half extents hw/hh into the free region */
  const fit = (hw, hh, hd) => {
    const t = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2));
    const rh = (h - region.top - region.bottom) / h, rw = (w - region.side * 2) / w;
    return Math.max(hh / (t * rh), hw / (t * camera.aspect * rw)) * 1.08 + hd;
  };

  /* ---------- labels ---------- */
  const tags = [];
  const tag = (i) => { if (!tags[i]) { const d = document.createElement('span'); tagsBox.appendChild(d); tags[i] = d; } return tags[i]; };
  const v3 = new THREE.Vector3();
  const toScreen = (obj, a) => { v3.set(a[0], a[1], a[2]); obj.localToWorld(v3); v3.project(camera); return [(v3.x * 0.5 + 0.5) * w, (-v3.y * 0.5 + 0.5) * h + 0, v3.z]; };
  /* setViewOffset shifts the image; projected y must be shifted the same way */
  const shiftY = () => 0; /* projectionMatrix already includes the view offset */
  let shown = '';
  function setCard(k, n, total, op, anchorXY) {
    const [t, d] = k ? (k.startsWith('#') ? [lbl(k.slice(1)), lbl(k.slice(1) + '.d') || lbl(k.slice(1) + '.p')] : txt(k)) : ['', ''];
    if (cT.innerHTML !== t) cT.innerHTML = t; if (cD.innerHTML !== d) cD.innerHTML = d;
    const nn = n ? String(n).padStart(2, '0') + ' / ' + String(total).padStart(2, '0') : ''; if (cN.textContent !== nn) cN.textContent = nn;
    card.style.opacity = op.toFixed(3); svg.style.opacity = anchorXY ? op.toFixed(3) : 0;
    card.classList.toggle('on', op > 0.5);
    if (k !== shown) { shown = k; card.setAttribute('aria-hidden', k ? 'false' : 'true'); }
    if (!anchorXY || op <= 0.01) return;
    let [ax, ay] = anchorXY; ay += shiftY();
    const cw = card.offsetWidth, ch = card.offsetHeight;
    let cx, cyy, lx, ly;
    if (mobile) {
      cx = (w - cw) / 2; cyy = h - region.bottom + 10; lx = clamp(ax, cx + 24, cx + cw - 24); ly = cyy;
    } else {
      const right = ax > w * 0.5;
      cx = right ? Math.min(w - cw - 96, Math.max(ax + 90, w * 0.62)) : Math.max(28, Math.min(ax - 90 - cw, w * 0.38 - cw));
      cyy = clamp(ay - ch / 2 - 40, region.top - 20, h - region.bottom - ch);
      if (right && ax + 70 + cw > w - 96 && ax - 70 - cw > 16) { cx = ax - 70 - cw; }
      else if (!right && ax - 70 - cw < 16 && ax + 70 + cw < w - 96) { cx = ax + 70; }
      const onRight = cx > ax; lx = onRight ? cx : cx + cw; ly = cyy + ch / 2;
    }
    card.style.transform = `translate3d(${cx.toFixed(1)}px,${cyy.toFixed(1)}px,0)`;
    const mx = mobile ? ax : (ax + lx) / 2;
    path.setAttribute('d', mobile ? `M${ax.toFixed(1)},${ay.toFixed(1)} L${lx.toFixed(1)},${(ly - 2).toFixed(1)}` : `M${ax.toFixed(1)},${ay.toFixed(1)} L${mx.toFixed(1)},${ly.toFixed(1)} L${lx.toFixed(1)},${ly.toFixed(1)}`);
    dot.setAttribute('cx', ax.toFixed(1)); dot.setAttribute('cy', ay.toFixed(1));
  }

  /* ---------- per-unit animation ---------- */
  const tmp = new THREE.Vector3();
  /* f(k) returns arrival 0..1 per part (0 exploded, 1 seated) and highlight 0..1 */
  function poseUnit(U, keys, slotSeg, p, time, appearSeg, extra) {
    const n = keys.length; const sp = seg(p, slotSeg); const app = seg(p, appearSeg);
    let active = -1, activeT = 0, explodedness = 0;
    keys.forEach((k, i) => {
      const g = U.P[k]; const a = sp * n - i; /* local slot progress */
      const arrive = ease(clamp(a / 0.55)); const hl = a > 0.45 && a < 1.25 ? Math.sin(clamp((a - 0.45) / 0.8) * Math.PI) : 0;
      if (a >= 0 && a < 1) { active = i; activeT = a; }
      const e = 1 - arrive; explodedness += e / n;
      const ex = U.explode[k];
      tmp.set(ex[0] * exScale.x, ex[1] * exScale.y, ex[2] * exScale.z).multiplyScalar(e);
      tmp.y += Math.sin(time * 0.9 + i * 1.7) * 0.012 * e;
      g.position.copy(g.userData.home).add(tmp);
      g.rotation.set(Math.sin(time * 0.5 + i) * 0.12 * e, (i % 2 ? 0.35 : -0.35) * e + Math.sin(time * 0.4 + i) * 0.1 * e, 0);
      const ap = clamp(app * (n + 3) - i * 1.0, 0, 1); const sc = 0.001 + ease(ap) * 0.999;
      g.scale.setScalar(sc); g.visible = sc > 0.01;
      highlight(g, hl);
    });
    if (extra) extra(sp);
    return { active, activeT, explodedness, appear: app };
  }

  /* ---------- camera rig ---------- */
  const camT = new THREE.Vector3(), camPos = new THREE.Vector3();
  const orbit = (target, dist, az, el) => { camPos.set(Math.sin(az) * Math.cos(el), Math.sin(el), Math.cos(az) * Math.cos(el)).multiplyScalar(dist).add(target); };

  /* ---------- state + loop ---------- */
  let slow = 0.016, nF = 0, target = 0, prog = 0, active = false, last = performance.now(), time = 0, lastDisp = '';
  const readScroll = () => { const r = track.getBoundingClientRect(); const total = track.offsetHeight - stage.offsetHeight; target = clamp(-r.top / Math.max(1, total)); };
  window.addEventListener('scroll', readScroll, { passive: true });
  const ro = new ResizeObserver(() => { resize(); readScroll(); }); ro.observe(stage);
  new IntersectionObserver((es) => { active = es[0].isIntersecting; if (active) { last = performance.now(); requestAnimationFrame(loop); } }, { rootMargin: '10% 0px' }).observe(sec);
  steps.forEach((b, i) => b.addEventListener('click', () => {
    const total = track.offsetHeight - stage.offsetHeight; const top = track.getBoundingClientRect().top + window.scrollY;
    window.scrollTo({ top: top + total * (STAGES[i] + (i ? 0.012 : 0)), behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
  }));
  const roomOpacity = (v) => { room.group.visible = v > 0.002; for (const m of room.fade) { m.opacity = v; m.transparent = v < 0.999; m.depthWrite = v > 0.5; } };
  const mixColor = new THREE.Color();
  const keyWarm = new THREE.Color(0xFFF3E2), keyCool = new THREE.Color(0xE4F1FF);
  const wallWarm = new THREE.Color(0xEDE6DA), wallCool = new THREE.Color(0xDCE8F2);

  function frame(p, dt) {
    time += dt;
    /* ---------- indoor ---------- */
    const indoorDoneT = seg(p, T.indDone);
    const iS = poseUnit(ind, ind.order, T.ind, p, time, [0.004, T.s1[1] - 0.004]);
    /* front panel hinge: arrives open, closes in "indoor done", subtle open/close, then shut */
    const fpA = seg(p, [T.ind[0] + (T.ind[1] - T.ind[0]) * 11 / 12, T.ind[1]]);
    let hinge = -0.95 * (1 - smooth(0.2, 1, fpA) * 0.25);
    hinge = lerp(hinge, 0, smooth(0, 0.35, indoorDoneT));
    hinge += -0.55 * Math.sin(Math.PI * clamp((indoorDoneT - 0.4) / 0.45));
    if (p > T.indDone[1]) hinge = 0;
    ind.P.frontPivot.rotation.x = hinge;
    /* louver closed until cooling, then opens and swings gently */
    const coolT = seg(p, T.cool);
    ind.P.louverPivot.rotation.x = lerp(-1.5, 0.55 + Math.sin(time * 0.8) * 0.12 * smooth(0.4, 1, coolT), smooth(0.05, 0.35, coolT));
    /* whole-unit slow turn while exploded */
    ind.unit.rotation.y = Math.sin(time * 0.25) * 0.22 * iS.explodedness;
    /* indoor waits in front of the wall until it is hooked on the plate during installation */
    const insP = seg(p, T.ins); const insN = INS_KEYS.length; const slot = (i) => clamp(insP * insN - i);
    ind.unit.position.copy(A).add(tmp.set(0, 0.0, 0.32 * (1 - smooth(0.35, 0.9, slot(0)))));
    /* ---------- outdoor ---------- */
    const oS = poseUnit(out, OUT_ORDER, T.out, p, time, [T.outIntro[0], T.outIntro[1] - 0.004], (sp) => {
      /* top lid + front panels close during the grille slot (just before the grille) */
      const a = sp * 10 - 9; const c = ease(clamp(a / 0.45)); const g = out.P.close;
      tmp.set(0, 0.55 * exScale.y, 0.5 * exScale.z).multiplyScalar(1 - c); g.position.copy(g.userData.home).add(tmp); g.rotation.set(0, 0, 0);
      g.scale.setScalar(p > T.outIntro[0] ? 1 : 0.001); g.visible = p > T.outIntro[0] && (c > 0 || a > -1.2); highlight(g, 0);
      const gr = out.P.grille; const ga = ease(clamp((a - 0.35) / 0.4)); tmp.set(-0.1 * exScale.x, 0, 0.8 * exScale.z).multiplyScalar(1 - ga); gr.position.copy(gr.userData.home).add(tmp);
      gr.rotation.set(0, 0, 0);
    });
    out.unit.rotation.y = -0.35 * oS.explodedness + Math.sin(time * 0.25) * 0.2 * oS.explodedness;
    out.unit.position.copy(B).add(tmp.set(0, 0.22 * (1 - smooth(0.3, 0.9, slot(2))), 0.25 * (1 - smooth(0.3, 0.9, slot(2)))));
    out.unit.visible = p > T.outIntro[0] - 0.01;
    /* ---------- room, piping ---------- */
    const roomV = smooth(0, 0.5, slot(0)) * (p >= T.ins[0] ? 1 : 0);
    roomOpacity(roomV);
    const dr = (m, f) => { const c = m.geometry.index.count; m.geometry.setDrawRange(0, Math.floor(c * clamp(f) / 6) * 6); m.visible = f > 0.002; };
    dr(pipe.insul, slot(3)); dr(pipe.gas, slot(3) * 1.15); dr(pipe.liq, slot(3) * 1.1); dr(pipe.cable, slot(4)); dr(pipe.drain, slot(5));
    /* ---------- cooling ---------- */
    air.group.visible = coolT > 0.15;
    const airAmt = smooth(0.18, 0.75, coolT); air.update(time, airAmt);
    coolLight.intensity = 2.2 * airAmt;
    ind.P.blowerSpin.rotation.x -= dt * 14 * smooth(0.1, 0.3, coolT);
    out.P.fanSpin.rotation.z -= dt * 11 * smooth(0.1, 0.3, coolT);
    const dispOn = smooth(0.0, 0.12, coolT);
    const temp = coolT > 0.15 ? String(Math.round(lerp(26, 22, smooth(0.25, 0.85, coolT)))) + '°' : '24°';
    if (temp !== lastDisp || Math.abs(ind.P.dispMat.emissiveIntensity - dispOn * 1.6) > 0.01) { ind.P.setDisplay(temp, dispOn * 1.6); lastDisp = temp; }
    mixColor.copy(navy).lerp(coolBg, airAmt); scene.background.copy(mixColor); scene.fog.color.copy(mixColor);
    key.color.copy(keyWarm).lerp(keyCool, airAmt);
    room.fade[0].color.copy(wallWarm).lerp(wallCool, airAmt);

    /* ---------- camera ---------- */
    const ex = (bb, e) => [lerp(bb.as.x, bb.ex.x, e), lerp(bb.as.y, bb.ex.y, e), lerp(bb.as.z, bb.ex.z, e)];
    const [ihw, ihh, ihd] = ex(bbIn, Math.max(iS.explodedness, p < T.ind[0] ? 1 : 0));
    const dIn = fit(ihw, ihh, ihd);
    const [ohw, ohh, ohd] = ex(bbOut, Math.max(oS.explodedness, p < T.out[0] ? 1 : 0));
    const dOut = fit(ohw, ohh, ohd);
    const tIn = tmp.copy(ind.unit.position).clone();
    let az = lerp(-0.55, 0.32, smooth(0, 1, seg(p, [0, T.ind[1]]))), el = 0.16;
    camT.copy(tIn); let dist = dIn;
    /* indoor done: gentle push in */
    if (p >= T.indDone[0]) { const k = smooth(0, 1, indoorDoneT); dist = lerp(dIn, dIn * 0.92, k); az = lerp(0.32, 0.12, k); }
    /* to outdoor */
    const toOut = smooth(T.indDone[1] - 0.012, T.outIntro[1], p);
    if (toOut > 0) { camT.lerp(out.unit.position, toOut); dist = lerp(dist, dOut, toOut); az = lerp(az, lerp(0.5, -0.3, seg(p, T.out)), toOut); el = lerp(el, 0.2, toOut); }
    /* installation: wide residential shot that eases toward each step */
    const insK = smooth(0, 0.6, slot(0)) * (p >= T.ins[0] ? 1 : 0);
    if (insK > 0) {
      const wide = new THREE.Vector3(1.15, 1.32, 0.35);
      const dWide = fit(portrait ? 1.35 : 1.75, 1.15, 0.6);
      const step = Math.min(insN - 1, Math.floor(insP * insN));
      const foc = [new THREE.Vector3(0.45, 2.0, 0.1), new THREE.Vector3(1.1, 2.05, 0.1), B, new THREE.Vector3(1.9, 1.5, 0.15), new THREE.Vector3(2.0, 1.4, 0.15), new THREE.Vector3(1.6, 1.2, 0.1), new THREE.Vector3(1.15, 1.6, 0.1)][step];
      const wt = wide.clone().lerp(foc, 0.22);
      camT.lerp(wt, insK); dist = lerp(dist, dWide * 0.97, insK); az = lerp(az, lerp(-0.12, 0.14, insP), insK); el = lerp(el, 0.1, insK);
    }
    /* cooling: move into the room and push slowly */
    const ck = smooth(0, 0.5, coolT);
    if (ck > 0) {
      const room = new THREE.Vector3(portrait ? 0.45 : 0.62, 1.55, 0.5);
      camT.lerp(room, ck); dist = lerp(dist, fit(portrait ? 0.7 : 1.15, 0.85, 0.5) * lerp(1, 0.9, smooth(0.5, 1, coolT)), ck); az = lerp(az, -0.18 + 0.08 * coolT, ck); el = lerp(el, 0.04, ck);
    }
    orbit(camT, dist, az, el); camera.position.copy(camPos); camera.lookAt(camT);
    camera.updateMatrixWorld();

    /* ---------- HUD ---------- */
    bar.style.transform = `scaleX(${p.toFixed(4)})`;
    let si = 0; for (let i = 0; i < STAGES.length; i++) if (p >= STAGES[i] - 0.0005) si = i;
    steps.forEach((b, i) => { const on = i === si; if (b.classList.contains('on') !== on) { b.classList.toggle('on', on); on ? b.setAttribute('aria-current', 'step') : b.removeAttribute('aria-current'); } });
    if (cur) { const s = String(si + 1).padStart(2, '0') + ' / ' + steps[si].querySelector('span').innerHTML; if (cur.innerHTML !== s) cur.innerHTML = s; }
    intro.style.opacity = (1 - smooth(T.s1[1] - 0.02, T.s1[1] + 0.005, p)).toFixed(3);
    note.style.opacity = (smooth(T.outIntro[0], T.outIntro[0] + 0.01, p) * (1 - smooth(T.out[0] + 0.01, T.out[0] + 0.03, p))).toFixed(3);
    const fin = smooth(0.93, 0.975, p); finalEl.style.opacity = fin.toFixed(3); finalEl.classList.toggle('on', fin > 0.5);

    /* name tags while parts appear (desktop / tablet) */
    const tagOn = (U, keys, k0, s, from, to) => { keys.forEach((k, i) => { const t = tag(k0 + i); const o = mobile ? 0 : clamp((s.appear * (keys.length + 3) - i - 0.6) * 2) * (1 - smooth(from, to, p));
      t.style.opacity = o.toFixed(3); if (o > 0.01) { const [x, y] = toScreen(U.P[k], U.anchors[k]); t.style.transform = `translate3d(${x.toFixed(1)}px,${(y + shiftY()).toFixed(1)}px,0)`; const nm = k0 < 20 ? txt(IN_KEYS[i])[0] : txt('out' + (i + 1))[0]; if (t.innerHTML !== nm) t.innerHTML = nm; } }); };
    tagOn(ind, ind.order, 0, iS, T.s1[1] - 0.012, T.s1[1]);
    tagOn(out, OUT_ORDER, 20, oS, T.out[0] - 0.008, T.out[0] + 0.002);

    /* label card */
    const fade = (t) => smooth(0.02, 0.14, t) * (1 - smooth(0.88, 0.99, t));
    if (p >= T.ind[0] && p < T.ind[1] && iS.active >= 0) {
      const k = ind.order[iS.active];
      setCard(IN_KEYS[iS.active], iS.active + 1, 12, fade(iS.activeT), toScreen(ind.P[k], ind.anchors[k]));
    } else if (p >= T.indDone[0] && p < T.indDone[1]) {
      setCard('#indoor.done', 0, 0, fade(indoorDoneT), toScreen(ind.P.front, ind.anchors.front));
    } else if (p >= T.out[0] && p < T.out[1] && oS.active >= 0) {
      const k = OUT_ORDER[oS.active];
      setCard('out' + (oS.active + 1), oS.active + 1, 10, fade(oS.activeT), toScreen(out.P[k], out.anchors[k]));
    } else if (p >= T.ins[0] && p < T.ins[1]) {
      const st = Math.min(insN - 1, Math.floor(insP * insN)); const lt = insP * insN - st;
      const anc = [[0.45, 2.05, 0.01], [1.22, 2.05, 0.11], [1.55, 0.5, 0.3], [2.44, 1.3, 0.17], [2.25, 0.84, 0.21], [2.66, 0.9, 0.1], [1.26, 2.05, 0.13]][st];
      const sp = toScreen(scene, anc);
      setCard(INS_KEYS[st], st + 1, 7, fade(lt), sp);
    } else if (p >= T.cool[0] && p < 0.93) {
      setCard('#cool', 0, 0, smooth(0.05, 0.2, coolT) * (1 - smooth(0.4, 0.5, coolT)), toScreen(ind.unit, [0.31, -0.035, 0.12]));
    } else setCard('', 0, 0, 0, null);
  }

  function loop(now) {
    if (!active) return;
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    /* adaptive resolution for slower phones */
    slow = slow * 0.95 + dt * 0.05; if (++nF % 45 === 0 && slow > 0.036 && renderer.getPixelRatio() > 0.76) { renderer.setPixelRatio(renderer.getPixelRatio() - 0.25); renderer.setSize(w, h, false); }
    const k = 1 - Math.pow(0.0015, dt); prog += (target - prog) * k; if (Math.abs(target - prog) < 0.00005) prog = target;
    frame(prog, dt);
    renderer.render(scene, camera);
    requestAnimationFrame(loop);
  }
  resize(); readScroll(); prog = target; frame(prog, 0.016); renderer.render(scene, camera);
  sec.classList.add('asm-ready');
  /* test hook */
  window.__asm = { render: (p) => { prog = target = p; frame(p, 0.016); renderer.render(scene, camera); }, canvas: renderer.domElement };
}

const s = document.getElementById('ac-assembly');
if (s && !s.classList.contains('asm-static')) init(s);
