/* Dev tool: renders the CTA banner artwork (indoor unit + cool airflow beams on navy). Not shipped. */
import * as THREE from 'three';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';
import { buildIndoor, buildAirflow } from '../ac-assembly/models.js';
const W = 960, H = 820;
const r = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true }); r.setSize(W, H); r.setPixelRatio(1);
r.outputColorSpace = THREE.SRGBColorSpace; r.toneMapping = THREE.ACESFilmicToneMapping; r.toneMappingExposure = 1.05;
document.body.appendChild(r.domElement);
const s = new THREE.Scene(); s.background = new THREE.Color(0x0B1F3A);
const pm = new THREE.PMREMGenerator(r); s.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture; s.environmentIntensity = 0.5;
s.add(new THREE.HemisphereLight(0xDDEBFF, 0x0B1F3A, 0.6));
const k = new THREE.DirectionalLight(0xFFFFFF, 2.0); k.position.set(1.5, 2, 3); s.add(k);
const fill = new THREE.PointLight(0x6EC1FF, 3.0, 4, 1.5); fill.position.set(0.2, -0.9, 0.9); s.add(fill);
/* faint wall plane behind the unit */
const wall = new THREE.Mesh(new THREE.PlaneGeometry(8, 6), new THREE.MeshStandardMaterial({ color: 0x0E2443, roughness: 0.95 })); wall.position.set(0, -1.2, -0.12); s.add(wall);
const ind = buildIndoor(false); s.add(ind.unit);
ind.P.louverPivot.rotation.x = 0.55; ind.P.setDisplay('22°', 1.6);
const air = buildAirflow(false); air.group.position.set(0, -0.14, 0.13); s.add(air.group); air.update(3.2, 1.0);
const cam = new THREE.PerspectiveCamera(30, W / H, 0.05, 30);
cam.position.set(-0.72, -0.7, 2.8); cam.lookAt(0.02, -0.46, 0); cam.updateProjectionMatrix();
r.render(s, cam);
window.__done = true;
