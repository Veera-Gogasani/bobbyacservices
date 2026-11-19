/* BOBBY — interactive split-AC explorer (home page).
   Five stages (system, indoor, outdoor, installation, cooling), numbered hotspots, click-to-select,
   rotate / zoom / reset, and render-on-demand. The HTML panel (a2-ui.js) drives stages and selection. */
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { buildIndoor, buildOutdoor, buildRoom, buildPiping, buildAirflow, buildClearance } from './models.js';

const A = new THREE.Vector3(0.45, 2.05, 0.12);   /* indoor unit on the wall */
const B = new THREE.Vector3(1.8, 0.77, 0.2);     /* outdoor unit on brackets */
const IN_LIST = ['front', 'filter', 'coil', 'blower', 'motor', 'pan', 'hose', 'sensor', 'pcb', 'display', 'louver', 'casing'];
const OUT_LIST = ['cabinet', 'compressor', 'condenser', 'fan', 'fmotor', 'mpcb', 'capacitor', 'valves', 'terminal', 'grille'];
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const lerp = (a, b, t) => a + (b - a) * t;
const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

function init(sec) {
  const view = sec.querySelector('.a2-view'), host = sec.querySelector('.a2-canvas'), hot = sec.querySelector('.a2-hot');
  const tools = sec.querySelector('.a2-tools'), dragHint = sec.querySelector('.a2-drag');
  const low = Math.min(screen.width, screen.height) < 600 || (navigator.deviceMemory || 8) < 4;
  const goStatic = () => { sec.classList.add('a2-static'); };
  let renderer;
  try { renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' }); } catch (e) { goStatic(); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio || 1, low ? 1.5 : 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.toneMappingExposure = 1.02;
  renderer.shadowMap.enabled = !low; renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  host.appendChild(renderer.domElement);
  const cvs = renderer.domElement;
  cvs.addEventListener('webglcontextlost', (e) => { e.preventDefault(); goStatic(); });

  /* ---------- scene ---------- */
  const scene = new THREE.Scene();
  const NAVY = new THREE.Color(0x0B1F3A), NIGHT = new THREE.Color(0x07152A);
  scene.background = NAVY.clone();
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.04).texture; scene.environmentIntensity = 0.65;
  const hemi = new THREE.HemisphereLight(0xE4EEFF, 0x1A2638, 0.75); scene.add(hemi);
  const key = new THREE.DirectionalLight(0xFFF4E6, 2.2); key.position.set(2.4, 4.4, 4.6); key.castShadow = !low;
  key.shadow.mapSize.set(1024, 1024); Object.assign(key.shadow.camera, { left: -2.6, right: 2.6, top: 2.6, bottom: -2.6, near: 1, far: 12 }); key.shadow.bias = -0.0004; key.shadow.normalBias = 0.02;
  key.target.position.set(1.1, 1.2, 0.3); scene.add(key, key.target);
  const rim = new THREE.DirectionalLight(0x7CC4FF, 1.4); rim.position.set(-3, 2.2, -2); scene.add(rim);
  const coolLight = new THREE.PointLight(0x6EC1FF, 0, 3.4, 1.5); coolLight.position.copy(A).add(new THREE.Vector3(0, -0.7, 0.9)); scene.add(coolLight);
  const shadowCatcher = new THREE.Mesh(new THREE.PlaneGeometry(8, 8), new THREE.ShadowMaterial({ opacity: 0.28 }));
  shadowCatcher.rotation.x = -Math.PI / 2; shadowCatcher.position.y = 0.002; shadowCatcher.receiveShadow = true; scene.add(shadowCatcher);

  const ind = buildIndoor(low), out = buildOutdoor(low), room = buildRoom(low), pipe = buildPiping(low), air = buildAirflow(low), clear = buildClearance();
  scene.add(ind.unit, out.unit, room.group, air.group, clear); pipe.all.forEach((m) => scene.add(m));
  ind.unit.position.copy(A); out.unit.position.copy(B);
  air.group.position.copy(A).add(new THREE.Vector3(0, -0.14, 0.13)); air.group.visible = false;
  clear.position.copy(B).add(new THREE.Vector3(-0.1, 0, 0.47)); clear.visible = false;
  /* faint wall between "inside" and "outside" for the system view */
  const ghostWall = new THREE.Mesh(new THREE.BoxGeometry(0.2, 2.9, 0.9), new THREE.MeshStandardMaterial({ color: 0x8FA6BF, transparent: true, opacity: 0, roughness: 0.9, depthWrite: false }));
  ghostWall.position.set(1.1, 1.45, 0.35); scene.add(ghostWall);

  /* rim light + focus dimming + highlight shader hook on cloned materials */
  const RIM = new THREE.Color(0x8FD3FF), HI = new THREE.Color(0xFF9F43);
  const hook = (m) => {
    const u = { uRim: { value: 0.14 }, uRimColor: { value: RIM }, uDim: { value: 1 }, uHi: { value: 0 }, uHiColor: { value: HI } }; m.userData.u = u;
    m.onBeforeCompile = (sh) => {
      Object.assign(sh.uniforms, u);
      sh.fragmentShader = 'uniform float uRim; uniform vec3 uRimColor; uniform float uDim; uniform float uHi; uniform vec3 uHiColor;\n' + sh.fragmentShader.replace('#include <dithering_fragment>',
        '#include <dithering_fragment>\n float fres = pow(1.0 - clamp(abs(dot(normalize(normal), normalize(vViewPosition))), 0.0, 1.0), 2.0);\n' +
        ' gl_FragColor.rgb = gl_FragColor.rgb * uDim + uRimColor * fres * uRim * uDim + uHiColor * (fres * 0.85 + 0.07) * uHi;');
    };
    m.customProgramCacheKey = () => 'a2-rim';
  };
  const groups = {};
  const register = (keyName, obj) => { const mats = []; obj.traverse((o) => { if (o.isMesh && o.material && o.material.isMeshStandardMaterial) { o.material = o.material.clone(); hook(o.material); mats.push(o.material); } });
    groups[keyName] = { obj, mats, dim: 1, hi: 0, op: 1, tDim: 1, tHi: 0, tOp: 1 }; obj.userData.key = keyName; };
  ind.order.forEach((k) => register('in.' + k, ind.P[k]));
  out.order.forEach((k) => register('out.' + k, out.P[k]));
  [['pipe.insul', pipe.insul], ['pipe.gas', pipe.gas], ['pipe.liq', pipe.liq], ['pipe.cable', pipe.cable], ['pipe.drain', pipe.drain]].forEach(([k, o]) => register(k, o));
  ind.order.forEach((k) => { ind.P[k].userData.home = ind.P[k].position.clone(); });
  out.order.forEach((k) => { out.P[k].userData.home = out.P[k].position.clone(); });
  const applyLook = (g) => { for (const m of g.mats) { m.userData.u.uDim.value = g.dim; m.userData.u.uHi.value = g.hi;
    const base = m.userData.baseOp ?? (m.userData.baseOp = m.opacity); m.opacity = base * g.op; m.transparent = g.op < 0.999 || base < 1; m.depthWrite = g.op > 0.5; } g.obj.visible = g.op > 0.01; };

  /* ---------- cooling-process helpers: refrigerant flow dots + warm/heat arrows ---------- */
  const flow = new THREE.Group(); scene.add(flow);
  const dotTex = (() => { const c = document.createElement('canvas'); c.width = c.height = 64; const x = c.getContext('2d'); const g = x.createRadialGradient(32, 32, 0, 32, 32, 32); g.addColorStop(0, '#fff'); g.addColorStop(1, 'rgba(255,255,255,0)'); x.fillStyle = g; x.fillRect(0, 0, 64, 64); return new THREE.CanvasTexture(c); })();
  const mkDots = (curve, color, n) => { const g = new THREE.BufferGeometry(); const a = new Float32Array(n * 3); g.setAttribute('position', new THREE.BufferAttribute(a, 3));
    const pts = new THREE.Points(g, new THREE.PointsMaterial({ color, size: 0.05, map: dotTex, transparent: true, depthWrite: false, depthTest: false, blending: THREE.AdditiveBlending, opacity: 0 }));
    pts.renderOrder = 12; pts.frustumCulled = false; flow.add(pts); return { pts, curve, n, a, g }; };
  const hotLine = mkDots(pipe.gas.geometry.parameters.path, 0xFF9F43, 22);       /* heat carried to the outdoor unit */
  const coldLine = mkDots(pipe.liq.geometry.parameters.path, 0x6EC8FF, 22);      /* cooled refrigerant returning indoors */
  const coneGeo = new THREE.ConeGeometry(0.03, 0.08, 14); coneGeo.rotateX(Math.PI / 2);
  const mkArrows = (color, n, from, to) => { const list = []; for (let i = 0; i < n; i++) { const m = new THREE.Mesh(coneGeo, new THREE.MeshBasicMaterial({ color, transparent: true, opacity: 0, depthWrite: false }));
    m.userData = { from: from(i, n), to: to(i, n), off: i / n }; m.position.copy(m.userData.from); m.lookAt(m.userData.to); flow.add(m); list.push(m); } return list; };
  const warmIn = mkArrows(0xFFA95C, 5, (i, n) => new THREE.Vector3(A.x - 0.3 + 0.6 * i / (n - 1), A.y + 0.42, A.z + 0.1), (i, n) => new THREE.Vector3(A.x - 0.3 + 0.6 * i / (n - 1), A.y + 0.17, A.z + 0.02));
  const heatOut = mkArrows(0xFF7A3D, 6, (i) => new THREE.Vector3(B.x - 0.12 + Math.cos(i * 1.05) * 0.12, B.y + Math.sin(i * 1.05) * 0.12, B.z + 0.18), (i) => new THREE.Vector3(B.x - 0.12 + Math.cos(i * 1.05) * 0.22, B.y + Math.sin(i * 1.05) * 0.22 + 0.06, B.z + 0.72));
  flow.visible = false;

  /* ---------- camera + controls ---------- */
  const camera = new THREE.PerspectiveCamera(32, 1, 0.05, 50);
  const controls = new OrbitControls(camera, cvs);
  controls.enableDamping = !reduce; controls.dampingFactor = 0.08; controls.enablePan = false; controls.rotateSpeed = 0.7; controls.zoomSpeed = 0.8;
  controls.minPolarAngle = 0.35; controls.maxPolarAngle = 1.62; controls.autoRotateSpeed = 1.1;
  cvs.style.touchAction = 'pan-y';                       /* vertical swipes still scroll the page on phones */
  view.addEventListener('wheel', (e) => { if (!e.ctrlKey && !e.metaKey) e.stopPropagation(); }, { capture: true });   /* wheel scrolls the page; ctrl+wheel zooms */

  const box = new THREE.Box3(), tmp = new THREE.Vector3(), tmp2 = new THREE.Vector3();
  let w = 1, h = 1;
  const fitDist = (hw, hh) => { const t = Math.tan(THREE.MathUtils.degToRad(camera.fov / 2)); return Math.max(hh / t, hw / (t * camera.aspect)) * (camera.aspect < 1.1 ? 1.24 : 1.12); };
  const unitExtents = (U) => { const st = U.order.map((k) => U.P[k].position.clone()); U.order.forEach((k) => { U.P[k].position.copy(U.P[k].userData.home).add(tmp.set(...U.explode[k]).multiply(exS)); });
    const sp = U.unit.position.clone(); U.unit.position.set(0, 0, 0); U.unit.updateMatrixWorld(true); box.makeEmpty(); U.order.forEach((k) => { if (k !== 'close') box.expandByObject(U.P[k]); });
    U.order.forEach((k, i) => U.P[k].position.copy(st[i])); U.unit.position.copy(sp); U.unit.updateMatrixWorld(true);
    return [Math.max(-box.min.x, box.max.x), Math.max(-box.min.y, box.max.y), Math.max(-box.min.z, box.max.z)]; };
  let exIn = [1, 1, 1], exOut = [1, 1, 1];
  const exS = new THREE.Vector3(1, 1, 1);   /* portrait screens stack parts more vertically */
  const PRESET = [
    () => ({ t: new THREE.Vector3(1.13, 1.4, 0.2), az: -0.08, el: 0.12, d: fitDist(1.05, 0.98) + 0.7 }),
    () => ({ t: A.clone().add(new THREE.Vector3(-0.2, -0.08, 0.26)), az: 0.55, el: 0.22, d: fitDist(exIn[0], exIn[1]) + exIn[2] * 0.85 }),
    () => ({ t: B.clone().add(new THREE.Vector3(0.04, 0.06, 0.2)), az: 0.5, el: 0.24, d: fitDist(exOut[0] * 1.02, exOut[1] * 1.05) + exOut[2] }),
    () => ({ t: new THREE.Vector3(1.12, 1.32, 0.35), az: 0.12, el: 0.16, d: fitDist(1.55, 1.25) + 0.5 }),
    () => ({ t: new THREE.Vector3(0.95, 1.42, 0.5), az: -0.2, el: 0.07, d: fitDist(1.3, 0.98) + 0.4 }),
  ];
  function resize() {
    w = view.clientWidth; h = view.clientHeight; renderer.setSize(w, h, false);
    camera.aspect = w / Math.max(1, h); camera.updateProjectionMatrix();
    if (camera.aspect < 1.1) exS.set(0.62, 1.45, 0.9); else exS.set(1, 1, 1);
    exIn = unitExtents(ind); exOut = unitExtents(out);
    controls.minDistance = 0.5; controls.maxDistance = 9; request();
  }

  let camTween = null;
  function goCamera(p, dur = 900) {
    const fromT = controls.target.clone(), fromP = camera.position.clone();
    const toP = new THREE.Vector3(Math.sin(p.az) * Math.cos(p.el), Math.sin(p.el), Math.cos(p.az) * Math.cos(p.el)).multiplyScalar(p.d).add(p.t);
    if (reduce || dur === 0) { camTween = null; controls.target.copy(p.t); camera.position.copy(toP); controls.update(); request(); return; }
    camTween = { t0: performance.now(), dur, fromT, fromP, toT: p.t.clone(), toP }; request();
  }

  /* ---------- stages + selection ---------- */
  let stage = 0, selPart = null, exInT = 0, exOutT = 0, exInV = 0, exOutV = 0, pipeDraw = 1, roomV = 0, roomT = 0, coolV = 0, coolT = 0, wallV = 0, wallT = 0, spotOp = 1;
  const HOT = {
    0: [['sys1', () => ind.unit, [0, 0.02, 0.13]], ['sys2', () => out.unit, [-0.12, 0.05, 0.17]], ['sys3', null, [1.6, 2.05, 0.13]], ['sys4', null, [2.47, 1.45, 0.16]], ['sys5', null, [2.66, 0.9, 0.1]]],
    1: IN_LIST.map((k) => [k, () => ind.P[k], ind.anchors[k]]),
    2: OUT_LIST.map((k) => [k, () => out.P[k], out.anchors[k]]),
    3: [['ins1', null, [0.12, 2.18, 0.04]], ['ins2', null, [1.21, 2.05, 0.12]], ['ins3', null, [1.55, 0.47, 0.32]], ['ins4', null, [2.25, 0.62, 0.24]], ['ins5', null, [2.45, 1.55, 0.18]], ['ins6', null, [2.66, 0.75, 0.1]], ['ins7', null, [1.32, 2.03, 0.13]]],
    4: [['cool1', null, [A.x, A.y + 0.3, A.z + 0.06]], ['cool2', null, [A.x - 0.25, A.y + 0.07, A.z + 0.2]], ['cool3', null, [A.x + 0.1, A.y + 0.04, A.z + 0.2]], ['cool4', null, [A.x + 0.2, A.y - 0.55, A.z + 0.6]], ['cool5', null, [2.0, 2.0, 0.14]], ['cool6', null, [B.x - 0.12, B.y + 0.2, B.z + 0.5]]],
  };
  const LINK = {
    sys1: ind.order.map((k) => 'in.' + k), sys2: out.order.map((k) => 'out.' + k), sys3: ['pipe.insul', 'pipe.gas', 'pipe.liq'], sys4: ['pipe.cable'], sys5: ['pipe.drain'],
    ins3: out.order.map((k) => 'out.' + k), ins4: ['pipe.insul', 'pipe.gas', 'pipe.liq'], ins5: ['pipe.cable', 'out.terminal'], ins6: ['pipe.drain', 'in.hose'], ins7: ['out.valves'],
    cool1: ['in.front', 'in.casing'], cool2: ['in.filter'], cool3: ['in.coil'], cool4: ['in.blower', 'in.louver'], cool5: ['pipe.gas', 'out.compressor'], cool6: ['out.condenser', 'out.fan'],
  };
  IN_LIST.forEach((k) => { LINK[k] = ['in.' + k]; }); OUT_LIST.forEach((k) => { LINK[k] = ['out.' + k]; });
  LINK.cabinet = ['out.cabinet', 'out.close'];

  let spots = [];
  function buildSpots() {
    hot.innerHTML = ''; spots = (HOT[stage] || []).map(([part, obj, an], i) => {
      const b = document.createElement('button'); b.type = 'button'; b.tabIndex = -1; b.className = 'a2-spot'; b.dataset.part = part;
      b.innerHTML = '<i class="dot"></i><i class="ln"></i><span class="tag"><span class="num">' + String(i + 1).padStart(2, '0') + '</span><span class="lab"></span></span>';
      b.addEventListener('click', (e) => { e.stopPropagation(); if (window.A2UI) window.A2UI.select(part); });
      hot.appendChild(b); return { b, part, obj, an };
    });
    labelSpots();
  }
  function labelSpots() {
    const panel = sec.querySelector('.a2-panel:not([hidden])'); if (!panel) return;
    const names = [...panel.querySelectorAll('.a2-item .nm')].map((n) => n.textContent);
    spots.forEach((s, i) => { const l = s.b.querySelector('.lab'); if (l.textContent !== (names[i] || '')) l.textContent = names[i] || ''; });
  }
  const v3 = new THREE.Vector3();
  let cycleIdx = -1, cycleT = 0;
  function placeSpots() {
    const camDir = camera.getWorldDirection(tmp2);
    spots.forEach((s, i) => {
      v3.set(...s.an); if (s.obj) s.obj().localToWorld(v3);
      const facing = tmp.copy(v3).sub(camera.position).normalize().dot(camDir) > 0;
      v3.project(camera);
      const x = (v3.x * 0.5 + 0.5) * w, y = (-v3.y * 0.5 + 0.5) * h;
      const vis = facing && x > 8 && x < w - 8 && y > 8 && y < h - 8 && spotOp > 0.05;
      s.b.style.transform = `translate3d(${x.toFixed(1)}px,${y.toFixed(1)}px,0)`;
      /* marker sits a little away from the part, joined by a fine connector line */
      let dx = x - w / 2, dy = y - h * 0.46; const L = Math.hypot(dx, dy) || 1; const off = w < 560 ? 30 : 40;
      dx = (dx / L) * off; dy = (dy / L) * off - 6;
      if (s.dx !== dx.toFixed(0) || s.dy !== dy.toFixed(0)) { s.dx = dx.toFixed(0); s.dy = dy.toFixed(0);
        s.b.style.setProperty('--dx', s.dx + 'px'); s.b.style.setProperty('--dy', s.dy + 'px');
        s.b.style.setProperty('--len', Math.hypot(dx, dy).toFixed(0) + 'px'); s.b.style.setProperty('--ang', Math.atan2(dy, dx).toFixed(3) + 'rad');
        s.b.classList.toggle('left', dx < 0); }
      s.b.style.opacity = vis ? ((selPart && selPart !== s.part ? 0.5 : 1) * spotOp).toFixed(3) : '0'; s.b.style.pointerEvents = vis ? 'auto' : 'none';
      s.b.classList.toggle('on', selPart === s.part); s.b.classList.toggle('cyc', stage === 4 && !selPart && cycleIdx === i);
    });
  }

  function setStage(i) {
    stage = i; selPart = null;
    exInT = i === 1 ? 1 : 0; exOutT = i === 2 ? 1 : 0;
    roomT = i >= 3 ? 1 : 0; coolT = i === 4 ? 1 : 0; wallT = i === 0 ? 1 : 0;
    if (i === 3) pipeDraw = 0;
    for (const k in groups) { groups[k].tHi = 0; groups[k].tDim = 1; }
    buildSpots(); spotOp = 0;
    goCamera(PRESET[i](), 1000);
    controls.autoRotate = false; tools.querySelector('[data-act="rotate"]').setAttribute('aria-pressed', 'false');
    request();
  }
  function select(part) {
    selPart = part;
    const lit = part ? (LINK[part] || []) : [];
    const stageKeys = stage === 1 ? ind.order.map((k) => 'in.' + k) : stage === 2 ? out.order.map((k) => 'out.' + k) : Object.keys(groups);
    for (const k in groups) { const g = groups[k]; const inStage = stageKeys.includes(k);
      g.tHi = lit.includes(k) ? 1 : 0; g.tDim = part && inStage && !lit.includes(k) ? 0.55 : 1; }
    const base = PRESET[stage]();
    if (part) {
      const s = spots.find((x) => x.part === part);
      if (s) { v3.set(...s.an); if (s.obj) s.obj().localToWorld(v3); const close = stage === 1 || stage === 2; base.t.lerp(v3, close ? 0.45 : 0.3); base.d *= close ? 0.78 : 0.86; }
      const cur = camera.position.clone().sub(controls.target); base.az = Math.atan2(cur.x, cur.z); base.el = Math.asin(clamp(cur.y / cur.length(), -1, 1));
    }
    goCamera(base, 800); request();
  }
  sec.addEventListener('a2:stage', (e) => setStage(e.detail.stage));
  sec.addEventListener('a2:select', (e) => select(e.detail.part));

  /* click a part in the 3D view to select it */
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2(); let downX = 0, downY = 0;
  const stopAuto = () => { controls.autoRotate = false; tools.querySelector('[data-act="rotate"]').setAttribute('aria-pressed', 'false'); };
  cvs.addEventListener('pointerdown', (e) => { downX = e.clientX; downY = e.clientY; stopAuto(); dragHint.classList.add('gone'); });
  cvs.addEventListener('pointerup', (e) => {
    if (Math.hypot(e.clientX - downX, e.clientY - downY) > 6 || !window.A2UI) return;
    const r = cvs.getBoundingClientRect(); ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
    ray.setFromCamera(ndc, camera);
    const pickable = stage === 1 ? IN_LIST.map((k) => ind.P[k]) : stage === 2 ? OUT_LIST.map((k) => out.P[k]) : stage === 0 ? [ind.unit, out.unit, pipe.insul, pipe.cable, pipe.drain] : [];
    const hit = ray.intersectObjects(pickable, true).find((x) => x.object.visible); if (!hit) return;
    let o = hit.object; while (o && !o.userData.key && o !== ind.unit && o !== out.unit) o = o.parent;
    const key = o && o.userData.key ? o.userData.key : o === ind.unit ? 'in.' : 'out.';
    let part = null;
    if (stage === 0) part = key.startsWith('in.') ? 'sys1' : key.startsWith('out.') ? 'sys2' : key === 'pipe.cable' ? 'sys4' : key === 'pipe.drain' ? 'sys5' : 'sys3';
    else { const k2 = key.split('.')[1]; part = k2 === 'close' ? 'cabinet' : k2; }
    if (part) window.A2UI.select(part);
  });

  tools.hidden = false; dragHint.hidden = false;
  tools.addEventListener('click', (e) => {
    const b = e.target.closest('[data-act]'); if (!b) return; const act = b.dataset.act;
    if (act === 'rotate') { controls.autoRotate = !controls.autoRotate; b.setAttribute('aria-pressed', String(controls.autoRotate)); }
    if (act === 'zin' || act === 'zout') { const d = camera.position.clone().sub(controls.target); const L = clamp(d.length() * (act === 'zin' ? 0.8 : 1.25), controls.minDistance, controls.maxDistance);
      goCamera({ t: controls.target.clone(), az: Math.atan2(d.x, d.z), el: Math.asin(clamp(d.y / d.length(), -1, 1)), d: L }, 450); }
    if (act === 'reset') { if (window.A2UI && window.A2UI.selected !== null) window.A2UI.clear(); else goCamera(PRESET[stage](), 800); }
    request();
  });

  /* ---------- render on demand ---------- */
  let active = false, raf = 0, last = performance.now(), time = 0;
  function request() { if (active && !raf) raf = requestAnimationFrame(loop); }
  controls.addEventListener('change', request);
  new IntersectionObserver((es) => { active = es[0].isIntersecting; if (active) { last = performance.now(); request(); } }, { rootMargin: '80px 0px' }).observe(view);
  new ResizeObserver(() => { resize(); }).observe(view);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) { last = performance.now(); request(); } });

  const approach = (cur, tgt, k) => (Math.abs(tgt - cur) < 0.002 ? tgt : cur + (tgt - cur) * k);
  const wallInC = new THREE.Color(0xEDE6DA), wallOutC = new THREE.Color(0xD9D4CC), duskIn = new THREE.Color(0x14294A), duskOut = new THREE.Color(0x1F3048), floorC = new THREE.Color(0xFFFFFF), duskFloor = new THREE.Color(0x3A4B66);
  function step(dt) {
    let moving = false; const k = reduce ? 1 : 1 - Math.exp(-dt * 7);
    if (camTween) { const t = clamp((performance.now() - camTween.t0) / camTween.dur); const e = ease(t);
      controls.target.lerpVectors(camTween.fromT, camTween.toT, e); camera.position.lerpVectors(camTween.fromP, camTween.toP, e); if (t >= 1) camTween = null; moving = true; }
    const ek = reduce ? 1 : 1 - Math.exp(-dt * 4);
    const nIn = approach(exInV, exInT, ek), nOut = approach(exOutV, exOutT, ek);
    if (nIn !== exInV || nOut !== exOutV) moving = true; exInV = nIn; exOutV = nOut;
    const nr = approach(roomV, roomT, k), nc = approach(coolV, coolT, reduce ? 1 : 1 - Math.exp(-dt * 3)), nw = approach(wallV, wallT, k);
    if (nr !== roomV || nc !== coolV || nw !== wallV) moving = true; roomV = nr; coolV = nc; wallV = nw;
    if (pipeDraw < 1) { pipeDraw = reduce ? 1 : Math.min(1, pipeDraw + dt / 2.4); moving = true; }
    const ns = approach(spotOp, camTween ? 0 : 1, 1 - Math.exp(-dt * 6)); if (ns !== spotOp) moving = true; spotOp = ns;

    /* exploded offsets along logical directions, staggered so parts separate in order */
    const pose = (U, ex, list) => { const n = list.length; U.order.forEach((key) => { const g = U.P[key]; const i = Math.max(0, list.indexOf(key));
      const e = ease(clamp(ex * 1.25 - (i / n) * 0.25)); g.position.copy(g.userData.home).add(tmp.set(...U.explode[key]).multiply(exS).multiplyScalar(e)); }); };
    pose(ind, exInV, IN_LIST); pose(out, exOutV, OUT_LIST);
    const setOp = (prefix, v) => { for (const kk in groups) if (kk.startsWith(prefix)) groups[kk].tOp = v; };
    setOp('in.', stage !== 2 ? 1 : 0); setOp('out.', stage !== 1 ? 1 : 0); setOp('pipe.', stage === 0 || stage >= 3 ? 1 : 0);
    groups['out.close'].tOp = stage === 1 ? 0 : 1 - clamp(exOutV * 4);
    for (const kk in groups) { const g = groups[kk]; const nd = approach(g.dim, g.tDim, k), nh = approach(g.hi, g.tHi, k), no = approach(g.op, g.tOp, reduce ? 1 : 1 - Math.exp(-dt * 6));
      if (nd !== g.dim || nh !== g.hi || no !== g.op || g.first === undefined) { g.first = 1; g.dim = nd; g.hi = nh; g.op = no; applyLook(g); moving = true; } }
    const dr = (m, f) => { const c = m.geometry.index.count; m.geometry.setDrawRange(0, Math.floor(c * clamp(f) / 6) * 6); };
    const pd = stage === 3 ? pipeDraw : 1;
    dr(pipe.insul, pd); dr(pipe.gas, pd * 1.1); dr(pipe.liq, pd * 1.1); dr(pipe.cable, stage === 3 ? clamp(pipeDraw * 1.3 - 0.3) : 1); dr(pipe.drain, stage === 3 ? clamp(pipeDraw * 1.5 - 0.5) : 1);
    room.group.visible = roomV > 0.01; for (const m of room.fade) { m.opacity = roomV; m.transparent = roomV < 0.999; m.depthWrite = roomV > 0.5; }
    ghostWall.material.opacity = 0.16 * wallV; ghostWall.visible = wallV > 0.01;
    clear.visible = stage === 3 && roomV > 0.5; clear.material.opacity = 0.85 * roomV;
    shadowCatcher.visible = roomV < 0.95 && stage !== 1;

    /* cooling mood: darker room, cool light, airflow beams, refrigerant flow, heat arrows */
    const cv = coolV; air.group.visible = cv > 0.02; flow.visible = cv > 0.02;
    if (cv > 0.02 && !reduce) { time += dt; moving = true; }
    air.update(reduce ? 2.0 : time, cv);
    coolLight.intensity = 2.4 * cv; key.intensity = lerp(2.2, 0.9, cv); hemi.intensity = lerp(0.75, 0.32, cv); scene.environmentIntensity = lerp(0.65, 0.35, cv);
    scene.background.copy(NAVY).lerp(NIGHT, cv);
    room.mats.wallIn.color.copy(wallInC).lerp(duskIn, cv); room.mats.wallOut.color.copy(wallOutC).lerp(duskOut, cv); room.mats.floor.color.copy(floorC).lerp(duskFloor, cv * 0.9);
    const fl = (o, dir) => { for (let i = 0; i < o.n; i++) { const t = (((i / o.n) + time * 0.12 * dir) % 1 + 1) % 1; const p = o.curve.getPointAt(t); o.a[i * 3] = p.x; o.a[i * 3 + 1] = p.y + 0.012; o.a[i * 3 + 2] = p.z + 0.03; } o.g.attributes.position.needsUpdate = true; o.pts.material.opacity = cv * 0.95; };
    if (cv > 0.02) { fl(hotLine, 1); fl(coldLine, -1); }
    const arr = (list) => list.forEach((m) => { const t = (m.userData.off + (reduce ? 0.5 : time) * 0.45) % 1; m.position.lerpVectors(m.userData.from, m.userData.to, t); m.material.opacity = cv * Math.sin(t * Math.PI) * 0.95; });
    arr(warmIn); arr(heatOut);
    ind.P.louverPivot.rotation.x = lerp(-1.5, 0.55, ease(cv));
    const disp = cv * 1.6; if (Math.abs(ind.P.dispMat.emissiveIntensity - disp) > 0.01) ind.P.setDisplay('24°', disp);
    if (cv > 0.02 && !reduce) { ind.P.blowerSpin.rotation.x -= dt * 14 * cv; out.P.fanSpin.rotation.z -= dt * 12 * cv; }
    if (stage === 4 && !selPart && !reduce) { cycleT += dt; if (cycleT > 2.6) { cycleT = 0; cycleIdx = (cycleIdx + 1) % 6; } } else { cycleIdx = -1; cycleT = 0; }
    if (controls.autoRotate) moving = true;
    return moving;
  }
  function loop(now) {
    raf = 0; if (!active) return;
    const dt = Math.min(0.05, (now - last) / 1000); last = now;
    const moving = step(dt);
    const changed = controls.update();
    renderer.render(scene, camera); placeSpots();
    if (moving || changed) raf = requestAnimationFrame(loop);
  }

  new MutationObserver(() => labelSpots()).observe(sec.querySelector('.a2-side'), { subtree: true, characterData: true, childList: true });

  resize();
  setStage(window.A2UI ? window.A2UI.stage : 0);
  goCamera(PRESET[stage](), 0);
  for (let i = 0; i < 40; i++) step(0.05);
  spotOp = 1; renderer.render(scene, camera); placeSpots();
  sec.classList.add('a2-ready');
  /* test hooks */
  window.__a2 = {
    settle: () => { for (let i = 0; i < 80; i++) { if (camTween) camTween.t0 -= 200; step(0.05); } spotOp = 1; controls.update(); renderer.render(scene, camera); placeSpots(); },
  };
}

const s = document.getElementById('ac-assembly');
if (s && !s.classList.contains('a2-static')) {
  if (window.A2UI) init(s); else window.addEventListener('load', () => init(s));
}
