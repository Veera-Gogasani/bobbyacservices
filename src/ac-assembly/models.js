/* Procedural 3D models for the BOBBY split-AC assembly story.
   Units are metres. Indoor unit ≈ 0.92 × 0.30 × 0.22, outdoor unit ≈ 0.80 × 0.56 × 0.30. Front faces +Z. */
import * as THREE from 'three';
import { RoundedBoxGeometry } from 'three/examples/jsm/geometries/RoundedBoxGeometry.js';

const M = {};
export function materials(low) {
  if (M.ready) return M;
  const std = (o) => new THREE.MeshStandardMaterial(o);
  M.white = std({ color: 0xF3F6F9, roughness: 0.32, metalness: 0.0 });
  M.whiteMatte = std({ color: 0xE8EDF2, roughness: 0.55 });
  M.grey = std({ color: 0xC3CCD5, roughness: 0.45 });
  M.cabinet = std({ color: 0xE9ECEF, roughness: 0.42, metalness: 0.15 });
  M.dark = std({ color: 0x1D2733, roughness: 0.5, metalness: 0.2 });
  M.black = std({ color: 0x14181E, roughness: 0.38, metalness: 0.45 });
  M.alu = std({ color: 0xC7D0D9, roughness: 0.3, metalness: 0.85 });
  M.copper = std({ color: 0xC9784A, roughness: 0.28, metalness: 1.0 });
  M.brass = std({ color: 0xCFA645, roughness: 0.3, metalness: 0.95 });
  M.steel = std({ color: 0x9AA6B2, roughness: 0.35, metalness: 0.9 });
  M.pcb = std({ color: 0x1F7A4C, roughness: 0.6, metalness: 0.1 });
  M.chip = std({ color: 0x15191F, roughness: 0.4 });
  M.blowerMat = std({ color: 0xD9E3EC, roughness: 0.45 });
  M.foam = std({ color: 0x23282F, roughness: 0.92 });
  M.hose = std({ color: 0xB8C2CC, roughness: 0.6 });
  M.cable = std({ color: 0xE6E9EC, roughness: 0.5 });
  M.filter = std({ color: 0x8FC6EE, roughness: 0.8, transparent: true, opacity: 0.75, side: THREE.DoubleSide });
  M.glass = std({ color: 0x0B141E, roughness: 0.12, metalness: 0.3 });
  M.fanBlade = std({ color: 0x2B3440, roughness: 0.5, side: THREE.DoubleSide });
  M.ready = true;
  return M;
}

/* ---------- small helpers ---------- */
function mesh(geo, mat, x = 0, y = 0, z = 0) { const m = new THREE.Mesh(geo, mat); m.position.set(x, y, z); m.castShadow = true; m.receiveShadow = true; return m; }
function rbox(w, h, d, r, mat, x, y, z, seg = 3) { return mesh(new RoundedBoxGeometry(w, h, d, seg, r), mat, x, y, z); }
function box(w, h, d, mat, x, y, z) { return mesh(new THREE.BoxGeometry(w, h, d), mat, x, y, z); }
function cylX(r, len, mat, x, y, z, seg = 24) { const m = mesh(new THREE.CylinderGeometry(r, r, len, seg), mat, x, y, z); m.rotation.z = Math.PI / 2; return m; }
function cylY(r, len, mat, x, y, z, seg = 24) { return mesh(new THREE.CylinderGeometry(r, r, len, seg), mat, x, y, z); }
function cylZ(r, len, mat, x, y, z, seg = 24) { const m = mesh(new THREE.CylinderGeometry(r, r, len, seg), mat, x, y, z); m.rotation.x = Math.PI / 2; return m; }
function tube(points, r, mat, seg = 64, radial = 10) {
  const c = new THREE.CatmullRomCurve3(points.map((p) => new THREE.Vector3(...p)), false, 'catmullrom', 0.2);
  const m = new THREE.Mesh(new THREE.TubeGeometry(c, seg, r, radial, false), mat); m.castShadow = true; return m;
}
/* fin pack: n thin aluminium plates spread along X */
function fins(n, w, h, d, mat) {
  const g = new THREE.BoxGeometry(0.0016, h, d);
  const im = new THREE.InstancedMesh(g, mat, n); const o = new THREE.Object3D();
  for (let i = 0; i < n; i++) { o.position.set(-w / 2 + (i + 0.5) * (w / n), 0, 0); o.updateMatrix(); im.setMatrixAt(i, o.matrix); }
  im.castShadow = true; return im;
}
function canvasTex(w, h, draw) {
  const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h);
  const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 4; return t;
}
function part(name) { const g = new THREE.Group(); g.name = name; return g; }

/* ======================= INDOOR UNIT ======================= */
export function buildIndoor(low) {
  const m = materials(low);
  const unit = new THREE.Group(); unit.name = 'indoor';
  const P = {};
  const W = 0.92, H = 0.30, D = 0.22;

  /* 1 casing / chassis */
  P.casing = part('casing');
  P.casing.add(rbox(W, H, 0.014, 0.006, m.white, 0, 0, -D / 2 + 0.007));
  P.casing.add(rbox(W, 0.016, D - 0.02, 0.006, m.white, 0, H / 2 - 0.008, 0));
  P.casing.add(rbox(0.016, H, D - 0.02, 0.006, m.white, -W / 2 + 0.008, 0, 0));
  P.casing.add(rbox(0.016, H, D - 0.02, 0.006, m.white, W / 2 - 0.008, 0, 0));
  P.casing.add(rbox(W - 0.04, 0.02, 0.07, 0.006, m.whiteMatte, 0, -H / 2 + 0.03, -0.065));
  for (const x of [-0.3, 0, 0.3]) P.casing.add(box(0.012, H - 0.04, 0.03, m.whiteMatte, x, 0, -D / 2 + 0.03)); /* ribs */

  /* 2 evaporator coil (front slab, tilted) */
  P.coil = part('coil');
  const coilG = new THREE.Group(); coilG.position.set(0, 0.03, 0.035); coilG.rotation.x = -0.32;
  coilG.add(fins(low ? 70 : 120, 0.80, 0.19, 0.036, m.alu));
  for (let i = 0; i < 6; i++) { const y = -0.08 + i * 0.032; coilG.add(cylX(0.0048, 0.82, m.copper, 0, y, i % 2 ? 0.008 : -0.008, 10)); }
  for (const sx of [-1, 1]) for (let i = 0; i < 3; i++) {
    const tor = mesh(new THREE.TorusGeometry(0.016, 0.0048, 8, 16, Math.PI), m.copper, sx * 0.41, -0.064 + i * 0.064, 0);
    tor.rotation.y = sx > 0 ? -Math.PI / 2 : Math.PI / 2; tor.rotation.x = Math.PI / 2; coilG.add(tor);
  }
  coilG.add(box(0.012, 0.2, 0.04, m.steel, -0.405, 0, 0)); coilG.add(box(0.012, 0.2, 0.04, m.steel, 0.405, 0, 0));
  P.coil.add(coilG);

  /* 3 cross-flow blower */
  P.blower = part('blower');
  const bl = new THREE.Group(); bl.position.set(-0.02, -0.055, -0.02);
  const n = low ? 24 : 36; const bladeG = new THREE.BoxGeometry(0.74, 0.0035, 0.02);
  const blades = new THREE.InstancedMesh(bladeG, m.blowerMat, n); const o = new THREE.Object3D();
  for (let i = 0; i < n; i++) { const a = (i / n) * Math.PI * 2; o.position.set(0, Math.cos(a) * 0.037, Math.sin(a) * 0.037); o.rotation.set(a + 0.55, 0, 0); o.updateMatrix(); blades.setMatrixAt(i, o.matrix); }
  blades.castShadow = true; bl.add(blades);
  for (const x of [-0.37, -0.185, 0, 0.185, 0.37]) bl.add(cylX(0.046, 0.006, m.blowerMat, x, 0, 0, 28));
  bl.add(cylX(0.008, 0.78, m.steel, 0, 0, 0, 10));
  P.blower.add(bl); P.blowerSpin = bl;

  /* 4 indoor fan motor */
  P.motor = part('motor');
  P.motor.add(cylX(0.036, 0.075, m.dark, 0.405, -0.055, -0.02, 28));
  P.motor.add(cylX(0.04, 0.008, m.steel, 0.37, -0.055, -0.02, 28));
  P.motor.add(box(0.05, 0.012, 0.07, m.grey, 0.405, -0.1, -0.02));

  /* 5 air filter */
  P.filter = part('filter');
  const tex = canvasTex(256, 128, (c, w, h) => { c.fillStyle = '#9ccdf0'; c.fillRect(0, 0, w, h); c.strokeStyle = 'rgba(30,80,130,.55)'; c.lineWidth = 1;
    for (let x = 0; x < w; x += 6) { c.beginPath(); c.moveTo(x, 0); c.lineTo(x, h); c.stroke(); } for (let y = 0; y < h; y += 6) { c.beginPath(); c.moveTo(0, y); c.lineTo(w, y); c.stroke(); } });
  tex.wrapS = tex.wrapT = THREE.RepeatWrapping; tex.repeat.set(3, 1);
  const fMat = m.filter.clone(); fMat.map = tex;
  const fl = new THREE.Group(); fl.position.set(0, 0.035, 0.066); fl.rotation.x = -0.32;
  for (const sx of [-0.2, 0.2]) { fl.add(mesh(new THREE.PlaneGeometry(0.38, 0.2), fMat, sx, 0, 0)); fl.add(box(0.38, 0.006, 0.006, m.grey, sx, 0.1, 0)); fl.add(box(0.38, 0.006, 0.006, m.grey, sx, -0.1, 0)); fl.add(box(0.006, 0.2, 0.006, m.grey, sx - 0.19, 0, 0)); fl.add(box(0.006, 0.2, 0.006, m.grey, sx + 0.19, 0, 0)); }
  P.filter.add(fl);

  /* 6 drain pan */
  P.pan = part('pan');
  P.pan.add(rbox(0.82, 0.014, 0.075, 0.004, m.grey, 0, -0.092, 0.052));
  P.pan.add(box(0.82, 0.02, 0.006, m.grey, 0, -0.082, 0.087));
  P.pan.add(box(0.006, 0.02, 0.075, m.grey, -0.41, -0.082, 0.052)); P.pan.add(box(0.006, 0.02, 0.075, m.grey, 0.41, -0.082, 0.052));

  /* 7 drain hose (leaves the pan at the left, runs out of the back) */
  P.hose = part('hose');
  P.hose.add(tube([[-0.405, -0.095, 0.05], [-0.43, -0.12, 0.02], [-0.44, -0.13, -0.05], [-0.44, -0.14, -0.13], [-0.43, -0.19, -0.2]], 0.009, m.hose, 48, 12));
  P.hoseEnd = new THREE.Vector3(-0.43, -0.19, -0.2);

  /* 8 temperature sensor (clipped to the coil, wire to the PCB) */
  P.sensor = part('sensor');
  P.sensor.add(mesh(new THREE.CapsuleGeometry(0.0055, 0.022, 4, 10), m.steel, 0.33, 0.07, 0.07));
  P.sensor.add(tube([[0.33, 0.085, 0.07], [0.36, 0.11, 0.06], [0.39, 0.1, 0.04], [0.405, 0.07, 0.035]], 0.0018, m.dark, 24, 6));

  /* 9 control PCB (right-hand electrical box) */
  P.pcb = part('pcb');
  const pb = new THREE.Group(); pb.position.set(0.405, 0.045, 0.03);
  pb.add(box(0.006, 0.09, 0.13, m.pcb, 0, 0, 0));
  for (const [y, z, s] of [[0.02, 0.03, 0.022], [-0.015, -0.03, 0.016], [0.025, -0.035, 0.012], [-0.025, 0.035, 0.014]]) pb.add(box(0.008, s, s, m.chip, -0.006, y, z));
  pb.add(mesh(new THREE.CylinderGeometry(0.006, 0.006, 0.016, 12), m.alu, -0.012, -0.03, 0.0)).rotation.z = Math.PI / 2;
  pb.add(box(0.01, 0.02, 0.012, m.whiteMatte, -0.007, 0.035, -0.005));
  P.pcb.add(pb);

  /* 10 display panel (with temperature read-out) */
  P.display = part('display');
  P.dispCanvas = document.createElement('canvas'); P.dispCanvas.width = 256; P.dispCanvas.height = 96;
  P.dispTex = new THREE.CanvasTexture(P.dispCanvas); P.dispTex.colorSpace = THREE.SRGBColorSpace;
  P.dispMat = new THREE.MeshStandardMaterial({ color: 0x0B141E, roughness: 0.15, metalness: 0.3, emissive: 0xffffff, emissiveMap: P.dispTex, emissiveIntensity: 0 });
  P.setDisplay = (txt, on) => { const c = P.dispCanvas.getContext('2d'); c.fillStyle = '#000'; c.fillRect(0, 0, 256, 96); c.fillStyle = '#56C8FF'; c.font = 'bold 64px Arial'; c.textAlign = 'center'; c.textBaseline = 'middle'; c.fillText(txt, 128, 50); c.fillStyle = '#3EE07A'; c.beginPath(); c.arc(28, 48, 8, 0, 7); c.fill(); P.dispTex.needsUpdate = true; P.dispMat.emissiveIntensity = on; };
  P.setDisplay('24°', 0);
  P.display.add(rbox(0.1, 0.038, 0.006, 0.003, P.dispMat, 0.31, -0.035, D / 2 + 0.006));

  /* 11 louver + swing motor */
  P.louver = part('louver');
  P.louverPivot = new THREE.Group(); P.louverPivot.position.set(0, -0.137, 0.1);
  const lshape = new THREE.Shape(); lshape.moveTo(0, 0); lshape.quadraticCurveTo(0.03, -0.006, 0.06, 0.004); lshape.lineTo(0.06, 0.009); lshape.quadraticCurveTo(0.03, 0, 0, 0.005); lshape.closePath();
  const lgeo = new THREE.ExtrudeGeometry(lshape, { depth: 0.78, bevelEnabled: false }); lgeo.rotateY(-Math.PI / 2); lgeo.translate(0.39, 0, 0.0);
  const lv = mesh(lgeo, m.white, 0, 0, 0); lv.rotation.x = 0; P.louverPivot.add(lv); P.louver.add(P.louverPivot);
  P.louver.add(box(0.028, 0.026, 0.02, m.dark, -0.41, -0.112, 0.07));

  /* 12 front panel (hinged at the top) */
  P.front = part('front');
  P.frontPivot = new THREE.Group(); P.frontPivot.position.set(0, H / 2 - 0.004, D / 2 - 0.004);
  const fp = rbox(W - 0.004, 0.245, 0.014, 0.006, m.white, 0, -0.1225, 0.004, 4); P.frontPivot.add(fp);
  const logo = canvasTex(512, 64, (c, w, h) => { c.clearRect(0, 0, w, h); c.fillStyle = '#7A8C9E'; c.font = 'bold 40px Arial'; c.textAlign = 'left'; c.fillText('BOBBY', 6, 46); c.fillStyle = '#B0BDCA'; c.font = '22px Arial'; c.fillText('INVERTER · COOL', 170, 44); });
  const lm = new THREE.Mesh(new THREE.PlaneGeometry(0.2, 0.025), new THREE.MeshBasicMaterial({ map: logo, transparent: true }));
  lm.position.set(-0.3, -0.05, 0.0115); P.frontPivot.add(lm);
  P.frontPivot.add(box(W - 0.06, 0.004, 0.002, m.grey, 0, -0.2, 0.0115));
  P.front.add(P.frontPivot);

  const order = ['casing', 'coil', 'blower', 'motor', 'filter', 'pan', 'hose', 'sensor', 'pcb', 'display', 'louver', 'front'];
  for (const k of order) unit.add(P[k]);
  /* anchors used for leader lines (local positions of each part's visual centre) */
  const anchors = { casing: [-0.3, 0.12, -0.1], coil: [0.15, 0.07, 0.05], blower: [-0.15, -0.055, -0.02], motor: [0.405, -0.055, 0.0], filter: [-0.2, 0.05, 0.08],
    pan: [0.2, -0.09, 0.09], hose: [-0.44, -0.15, -0.1], sensor: [0.33, 0.07, 0.07], pcb: [0.405, 0.045, 0.06], display: [0.31, -0.035, 0.12], louver: [0, -0.125, 0.11], front: [-0.1, 0.05, 0.12] };
  /* exploded offsets (landscape); portrait layouts compress X */
  const explode = { casing: [0, 0.02, -0.28], coil: [0.0, 0.34, 0.06], blower: [-0.05, -0.36, -0.05], motor: [0.48, -0.22, 0], filter: [-0.42, 0.3, 0.22],
    pan: [0.15, -0.3, 0.28], hose: [-0.55, -0.2, 0.1], sensor: [0.56, 0.24, 0.12], pcb: [0.6, 0.02, 0.2], display: [0.62, -0.36, 0.3], louver: [-0.3, -0.5, 0.25], front: [0, 0.58, 0.12] };
  return { unit, P, order, anchors, explode };
}

/* ======================= OUTDOOR UNIT ======================= */
export function buildOutdoor(low) {
  const m = materials(low);
  const unit = new THREE.Group(); unit.name = 'outdoor';
  const P = {}; const W = 0.8, H = 0.56, D = 0.3;

  /* 1 cabinet frame: base pan, right side, partition, back-right panel */
  P.cabinet = part('cabinet');
  P.cabinet.add(rbox(W, 0.03, D, 0.006, m.cabinet, 0, -H / 2 + 0.015, 0));
  for (const [x, z] of [[-0.3, 0.1], [0.3, 0.1], [-0.3, -0.1], [0.3, -0.1]]) P.cabinet.add(box(0.06, 0.02, 0.05, m.dark, x, -H / 2 - 0.01, z));
  P.cabinet.add(rbox(0.012, H, D, 0.004, m.cabinet, W / 2 - 0.006, 0, 0));
  P.cabinet.add(box(0.008, H - 0.05, D - 0.04, m.cabinet, 0.13, -0.01, 0));
  P.cabinet.add(rbox(0.26, H, 0.012, 0.004, m.cabinet, 0.27, 0, -D / 2 + 0.006));

  /* 2 compressor */
  P.compressor = part('compressor');
  const cp = new THREE.Group(); cp.position.set(0.26, -0.12, 0.02);
  cp.add(cylY(0.075, 0.2, m.black, 0, 0, 0, 32));
  const dome = mesh(new THREE.SphereGeometry(0.075, 32, 12, 0, Math.PI * 2, 0, Math.PI / 2), m.black, 0, 0.1, 0); dome.scale.y = 0.55; cp.add(dome);
  const domeB = mesh(new THREE.SphereGeometry(0.075, 32, 12, 0, Math.PI * 2, 0, Math.PI / 2), m.black, 0, -0.1, 0); domeB.scale.y = -0.4; cp.add(domeB);
  cp.add(cylY(0.09, 0.012, m.steel, 0, -0.13, 0, 32));
  cp.add(box(0.05, 0.03, 0.03, m.dark, 0.0, 0.07, 0.075));
  cp.add(tube([[0.0, 0.14, 0.0], [0.0, 0.2, 0.0], [0.05, 0.22, -0.02], [0.08, 0.2, -0.06]], 0.006, m.copper, 24, 8));
  cp.add(tube([[-0.07, 0.0, 0.0], [-0.1, 0.05, 0.0], [-0.1, 0.12, -0.04]], 0.008, m.copper, 24, 8));
  P.compressor.add(cp);

  /* 3 condenser coil (L-shaped, back + left side) */
  P.condenser = part('condenser');
  const back = new THREE.Group(); back.position.set(-0.11, 0.0, -0.125); back.add(fins(low ? 90 : 150, 0.52, 0.48, 0.03, m.alu));
  for (let i = 0; i < 8; i++) back.add(cylX(0.0045, 0.53, m.copper, 0, -0.21 + i * 0.06, i % 2 ? 0.007 : -0.007, 10));
  const side = new THREE.Group(); side.position.set(-0.385, 0.0, 0.0); side.rotation.y = Math.PI / 2; side.add(fins(low ? 40 : 70, 0.22, 0.48, 0.03, m.alu));
  P.condenser.add(back, side);
  for (let i = 0; i < 4; i++) { const t = mesh(new THREE.TorusGeometry(0.03, 0.0045, 8, 16, Math.PI), m.copper, 0.15, -0.18 + i * 0.12, -0.125); t.rotation.y = -Math.PI / 2; P.condenser.add(t); }
  P.condenser.add(box(0.01, 0.48, 0.03, m.steel, 0.155, 0, -0.125));

  /* 4 outdoor fan (3-blade propeller) */
  P.fan = part('fan');
  P.fanSpin = new THREE.Group(); P.fanSpin.position.set(-0.115, 0.0, 0.085);
  const bs = new THREE.Shape(); bs.moveTo(0.02, -0.02); bs.bezierCurveTo(0.08, -0.07, 0.17, -0.07, 0.205, -0.02); bs.bezierCurveTo(0.21, 0.03, 0.15, 0.06, 0.02, 0.03); bs.closePath();
  const bgeo = new THREE.ExtrudeGeometry(bs, { depth: 0.004, bevelEnabled: false });
  for (let i = 0; i < 3; i++) { const b = mesh(bgeo, m.fanBlade, 0, 0, 0); b.rotation.z = (i / 3) * Math.PI * 2; b.rotation.y = 0.0; const pivot = new THREE.Group(); pivot.rotation.z = (i / 3) * Math.PI * 2; b.rotation.set(0.35, 0, 0); pivot.add(b); P.fanSpin.add(pivot); }
  P.fanSpin.add(cylZ(0.035, 0.05, m.fanBlade, 0, 0, 0, 24));
  P.fan.add(P.fanSpin);

  /* 5 outdoor fan motor on its bracket */
  P.fmotor = part('fmotor');
  P.fmotor.add(cylZ(0.055, 0.07, m.dark, -0.115, 0, 0.025, 28));
  P.fmotor.add(box(0.02, 0.5, 0.012, m.steel, -0.115, 0, -0.012));
  P.fmotor.add(box(0.3, 0.015, 0.012, m.steel, -0.115, 0.0, -0.012));

  /* 6 main control PCB in the electrical box */
  P.mpcb = part('mpcb');
  const eb = new THREE.Group(); eb.position.set(0.26, 0.18, 0.06);
  eb.add(box(0.2, 0.12, 0.004, m.grey, 0, 0, -0.03));
  eb.add(box(0.16, 0.1, 0.005, m.pcb, 0, 0, -0.025));
  for (const [x, y, s] of [[-0.04, 0.02, 0.03], [0.03, -0.02, 0.022], [0.05, 0.03, 0.014]]) eb.add(box(s, s, 0.008, m.chip, x, y, -0.02));
  eb.add(box(0.03, 0.045, 0.02, m.alu, -0.05, -0.025, -0.014));
  P.mpcb.add(eb);

  /* 7 capacitor */
  P.capacitor = part('capacitor');
  P.capacitor.add(cylY(0.022, 0.07, m.alu, 0.33, 0.1, 0.09, 24));
  P.capacitor.add(cylY(0.012, 0.012, m.dark, 0.33, 0.14, 0.09, 12));

  /* 8 refrigerant service valves (right side) */
  P.valves = part('valves');
  for (const [z, r] of [[0.06, 0.016], [-0.02, 0.022]]) {
    const v = new THREE.Group(); v.position.set(W / 2 + 0.02, -0.17, z);
    v.add(box(0.04, 0.05, 0.035, m.brass, 0, 0, 0)); v.add(cylX(r * 0.75, 0.03, m.brass, 0.032, 0, 0, 6)); v.add(cylY(0.01, 0.03, m.brass, 0, 0.038, 0, 6));
    v.add(tube([[-0.02, 0, 0], [-0.06, 0.02, 0], [-0.1, 0.06, 0]], r * 0.45, m.copper, 16, 8));
    P.valves.add(v);
  }
  P.valveTip = new THREE.Vector3(W / 2 + 0.055, -0.17, 0.02);

  /* 9 electrical terminal block */
  P.terminal = part('terminal');
  const tb = new THREE.Group(); tb.position.set(W / 2 + 0.006, 0.07, 0.02);
  tb.add(box(0.012, 0.03, 0.09, m.whiteMatte, 0, 0, 0));
  for (let i = 0; i < 4; i++) tb.add(cylX(0.005, 0.008, m.brass, 0.008, 0, -0.033 + i * 0.022, 8));
  P.terminal.add(tb);

  /* (closing) top lid + front panels */
  P.close = part('close');
  P.close.add(rbox(W, 0.014, D, 0.005, m.cabinet, 0, H / 2 - 0.007, 0));
  const fs = new THREE.Shape(); fs.moveTo(-0.27, -0.28); fs.lineTo(0.27, -0.28); fs.lineTo(0.27, 0.28); fs.lineTo(-0.27, 0.28); fs.closePath();
  const hole = new THREE.Path(); hole.absarc(0, 0, 0.215, 0, Math.PI * 2, true); fs.holes.push(hole);
  const fpg = new THREE.ExtrudeGeometry(fs, { depth: 0.01, bevelEnabled: false, curveSegments: 48 });
  P.close.add(mesh(fpg, m.cabinet, -0.115, 0, D / 2 - 0.01));
  P.close.add(rbox(0.245, H, 0.012, 0.004, m.cabinet, 0.278, 0, D / 2 - 0.004));
  for (let i = 0; i < 5; i++) P.close.add(box(0.2, 0.006, 0.004, m.grey, 0.278, 0.05 - i * 0.03, D / 2 + 0.004)); /* louvres on the right panel */
  const lg = canvasTex(256, 48, (c, w, h) => { c.fillStyle = '#7A8C9E'; c.font = 'bold 34px Arial'; c.fillText('BOBBY', 4, 36); });
  const lgm = new THREE.Mesh(new THREE.PlaneGeometry(0.11, 0.02), new THREE.MeshBasicMaterial({ map: lg, transparent: true })); lgm.position.set(0.278, 0.2, D / 2 + 0.003); P.close.add(lgm);

  /* 10 protective grille */
  P.grille = part('grille');
  const gr = new THREE.Group(); gr.position.set(-0.115, 0, D / 2 + 0.006);
  for (let r = 0.05; r <= 0.215; r += 0.033) gr.add(mesh(new THREE.TorusGeometry(r, 0.0022, 6, 56), m.dark, 0, 0, 0));
  for (let i = 0; i < 8; i++) { const s = box(0.43, 0.004, 0.004, m.dark, 0, 0, 0); s.rotation.z = (i / 8) * Math.PI; gr.add(s); }
  P.grille.add(gr);

  const order = ['cabinet', 'compressor', 'condenser', 'fan', 'fmotor', 'mpcb', 'capacitor', 'valves', 'terminal', 'close', 'grille'];
  for (const k of order) unit.add(P[k]);
  const anchors = { cabinet: [0.32, -0.27, 0.1], compressor: [0.26, -0.08, 0.09], condenser: [-0.3, 0.15, -0.12], fan: [-0.03, 0.12, 0.09], fmotor: [-0.115, 0, 0.06],
    mpcb: [0.26, 0.18, 0.04], capacitor: [0.33, 0.1, 0.11], valves: [0.43, -0.17, 0.06], terminal: [0.41, 0.07, 0.02], close: [0, 0.27, 0.1], grille: [-0.2, 0.15, 0.16] };
  const explode = { cabinet: [0, -0.25, 0], compressor: [0.5, 0.05, 0.25], condenser: [-0.5, 0.15, -0.3], fan: [-0.35, 0.05, 0.55], fmotor: [-0.55, -0.2, 0.35],
    mpcb: [0.4, 0.45, 0.2], capacitor: [0.62, 0.3, 0.3], valves: [0.58, -0.25, 0.25], terminal: [0.6, 0.12, 0.12], close: [0, 0.55, 0.5], grille: [-0.1, 0.0, 0.8] };
  return { unit, P, order, anchors, explode };
}

/* ======================= ROOM / INSTALLATION SET ======================= */
export function buildRoom(low) {
  const m = materials(low);
  const g = new THREE.Group(); g.name = 'room';
  const fade = [];
  const std = (o) => { const mm = new THREE.MeshStandardMaterial(Object.assign({ transparent: true, opacity: 0 }, o)); fade.push(mm); return mm; };
  const wallIn = std({ color: 0xEDE6DA, roughness: 0.9 });
  const wallOut = std({ color: 0xD9D4CC, roughness: 0.95 });
  const wallCut = std({ color: 0xA9A196, roughness: 0.95 });
  const floor = std({ color: 0xB98C62, roughness: 0.7 });
  const ground = std({ color: 0x8E9A86, roughness: 1 });
  const skirt = std({ color: 0xFFFFFF, roughness: 0.6 });
  const trim = std({ color: 0x9AA6B2, roughness: 0.4, metalness: 0.7 });
  /* back wall: inside (x < 1.0) and outside facade (x > 1.2) */
  const bw = box(3.6, 3.0, 0.2, wallIn, -0.8, 1.5, -0.1); bw.castShadow = false; g.add(bw);
  const ow = box(2.4, 3.0, 0.2, wallOut, 2.3, 1.5, -0.1); ow.castShadow = false; g.add(ow);
  /* side wall (exterior wall in section, with sleeve) */
  const sw = box(0.2, 3.0, 0.9, wallCut, 1.1, 1.5, 0.35); sw.castShadow = false; g.add(sw);
  const fl = box(3.6, 0.06, 2.6, floor, -0.8, -0.03, 1.2); fl.castShadow = false; g.add(fl);
  const gd = box(2.4, 0.04, 2.6, ground, 2.3, -0.06, 1.2); gd.castShadow = false; g.add(gd);
  g.add(box(3.6, 0.08, 0.02, skirt, -0.8, 0.04, 0.01));
  /* window on the inside wall for context */
  g.add(box(0.9, 1.0, 0.03, std({ color: 0xBFE2FF, roughness: 0.2, metalness: 0.1 }), -1.4, 1.5, 0.01));
  g.add(box(0.96, 0.05, 0.05, skirt, -1.4, 0.98, 0.03)); g.add(box(0.96, 0.05, 0.05, skirt, -1.4, 2.02, 0.03));
  /* wall sleeve through the side wall */
  const sleeve = new THREE.Mesh(new THREE.CylinderGeometry(0.06, 0.06, 0.24, 24, 1, true), std({ color: 0xF2F2F2, roughness: 0.5, side: THREE.DoubleSide }));
  sleeve.rotation.z = Math.PI / 2; sleeve.position.set(1.1, 2.05, 0.11); g.add(sleeve);
  for (const x of [0.99, 1.21]) { const r = new THREE.Mesh(new THREE.TorusGeometry(0.065, 0.012, 8, 24), std({ color: 0xF7F7F7, roughness: 0.5 })); r.rotation.y = Math.PI / 2; r.position.set(x, 2.05, 0.11); g.add(r); }
  /* outdoor brackets (L-shape) */
  for (const x of [1.55, 2.05]) { g.add(box(0.04, 0.5, 0.04, trim, x, 0.62, 0.02)); g.add(box(0.04, 0.04, 0.42, trim, x, 0.43, 0.21)); const d = box(0.03, 0.03, 0.5, trim, x, 0.6, 0.12); d.rotation.x = 0.75; g.add(d); }
  /* indoor wall-mounting plate */
  g.add(box(0.7, 0.18, 0.006, trim, 0.45, 2.05, 0.004));
  return { group: g, fade };
}

/* pipe bundle + cable + drain from indoor unit (mounted) through the sleeve to the outdoor valves */
export function buildPiping(low) {
  const m = materials(low);
  const mk = (pts, r, mat, seg) => { const t = tube(pts, r, mat, seg, low ? 8 : 12); t.geometry.setDrawRange(0, 0); return t; };
  const run = (dx, dz) => [[0.88, 2.0 + dx, 0.08 + dz], [0.96, 2.04 + dx, 0.1 + dz], [1.26, 2.04 + dx, 0.11 + dz], [2.38, 2.0 + dx, 0.12 + dz], [2.46, 1.85 + dx, 0.14 + dz], [2.46, 0.9 + dx, 0.17 + dz], [2.4, 0.66 + dx, 0.2 + dz], [2.25, 0.6 + dx, 0.2 + dz]];
  const insul = mk(run(0, 0), 0.028, m.foam, 160);
  const gas = mk(run(-0.012, 0.03), 0.0075, m.copper, 160);
  const liq = mk(run(0.01, 0.034), 0.005, m.copper, 160);
  const cable = mk(run(0.035, -0.01), 0.0055, m.cable, 160);
  const drain = mk([[0.47, 1.91, 0.02], [0.55, 1.95, 0.05], [0.9, 1.98, 0.06], [1.3, 1.96, 0.06], [2.6, 1.9, 0.07], [2.66, 1.7, 0.08], [2.66, 0.25, 0.1], [2.75, 0.05, 0.2]], 0.011, m.hose, 160);
  return { insul, gas, liq, cable, drain, all: [insul, gas, liq, cable, drain] };
}

/* translucent cool-air ribbons + particles */
export function buildAirflow(low) {
  const ribbons = new THREE.Group();
  const mats = [];
  const uni = { uTime: { value: 0 }, uAmt: { value: 0 } };
  for (let i = 0; i < (low ? 4 : 6); i++) {
    const spread = (i - 2.5) * 0.11;
    const curve = new THREE.CatmullRomCurve3([new THREE.Vector3(spread * 0.6, 0, 0), new THREE.Vector3(spread * 0.9, -0.25, 0.45), new THREE.Vector3(spread * 1.3, -0.75, 1.0), new THREE.Vector3(spread * 1.7, -1.3, 1.6)]);
    const seg = 60, w = 0.09 + (i % 3) * 0.025; const pos = []; const uv = []; const idx = [];
    for (let s = 0; s <= seg; s++) { const t = s / seg; const p = curve.getPoint(t); const tan = curve.getTangent(t); const side = new THREE.Vector3(1, 0, 0); const n = new THREE.Vector3().crossVectors(tan, side).normalize();
      const ww = w * (0.6 + t * 1.6); pos.push(p.x - ww, p.y + n.y * 0.0, p.z, p.x + ww, p.y, p.z); uv.push(t, 0, t, 1); if (s < seg) { const a = s * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); } }
    const geo = new THREE.BufferGeometry(); geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); geo.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); geo.setIndex(idx);
    const mat = new THREE.ShaderMaterial({ transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, side: THREE.DoubleSide,
      uniforms: { uTime: uni.uTime, uAmt: uni.uAmt, uOff: { value: i * 0.37 } },
      vertexShader: 'varying vec2 vUv; void main(){ vUv=uv; gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);} ',
      fragmentShader: 'uniform float uTime; uniform float uAmt; uniform float uOff; varying vec2 vUv; void main(){ float head=uAmt*1.15; if(vUv.x>head) discard; float edge=smoothstep(0.0,0.35,vUv.y)*smoothstep(1.0,0.65,vUv.y); float stripes=0.55+0.45*sin((vUv.x*9.0-uTime*1.4+uOff)*6.2831); float fade=(1.0-vUv.x)*smoothstep(0.0,0.06,vUv.x)*smoothstep(head,head-0.15,vUv.x); float a=edge*fade*stripes*0.17; gl_FragColor=vec4(vec3(0.55,0.85,1.0),a);} ' });
    mats.push(mat); const r = new THREE.Mesh(geo, mat); r.userData.curve = curve; ribbons.add(r);
  }
  /* particles following the ribbon curves */
  const N = low ? 140 : 320; const pg = new THREE.BufferGeometry(); const pp = new Float32Array(N * 3); const seed = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { seed[i * 3] = Math.random(); seed[i * 3 + 1] = Math.floor(Math.random() * ribbons.children.length); seed[i * 3 + 2] = (Math.random() - 0.5); }
  pg.setAttribute('position', new THREE.BufferAttribute(pp, 3));
  const dot = canvasTex(64, 64, (c) => { const gr = c.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, 'rgba(220,245,255,1)'); gr.addColorStop(1, 'rgba(120,200,255,0)'); c.fillStyle = gr; c.fillRect(0, 0, 64, 64); });
  const pm = new THREE.PointsMaterial({ size: 0.028, map: dot, transparent: true, depthWrite: false, blending: THREE.AdditiveBlending, opacity: 0 });
  const points = new THREE.Points(pg, pm);
  const update = (time, amt) => {
    uni.uTime.value = time; uni.uAmt.value = amt; pm.opacity = Math.min(1, amt * 1.4) * 0.6;
    for (let i = 0; i < N; i++) { const r = ribbons.children[seed[i * 3 + 1]]; let t = (seed[i * 3] + time * 0.08) % 1; if (t > amt * 1.1) t = t * amt; const p = r.userData.curve.getPoint(t);
      pp[i * 3] = p.x + seed[i * 3 + 2] * 0.2 * (0.3 + t); pp[i * 3 + 1] = p.y + Math.sin(time * 2 + i) * 0.02; pp[i * 3 + 2] = p.z + seed[i * 3 + 2] * 0.1; }
    pg.attributes.position.needsUpdate = true;
  };
  const group = new THREE.Group(); group.add(ribbons, points);
  return { group, update };
}
