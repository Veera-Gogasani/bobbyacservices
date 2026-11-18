# -*- coding: utf-8 -*-
"""
BOBBY – Residential AC spare parts: indicative market prices (customer reference only).

RESEARCH DATE: 18 November 2026  (update PRICE_REVIEW only after prices are genuinely re-checked)

Every price range below is taken from the listed public sources – nothing is invented.
Where no source supports a figure, the item shows "Price on request".

Price basis (shown on the page as a small tag):
  'online'   – part-only online retail price (ApnaSpare listing)
  'ratecard' – service-provider rate cards / rate contract (may include fitting; GST basis varies)
  'mixed'    – range combines online part prices and service rate cards
"""

PRICE_REVIEW = '18 November 2026'

# Product photos courtesy of ApnaSpare (used with the site owner's permission), served at 256px via their image CDN.
# Parts without a matching ApnaSpare product keep the BOBBY illustration (static/assets/img/parts/).
PHOTO_BASE = 'https://apnaspare.com/_next/image?url=https%3A%2F%2Fapnaspare.s3.ap-south-1.amazonaws.com%2Fproduct%2F{f}&w=256&q=75'
PHOTOS = {
    'run-capacitor': 'bced9846-3752-45e6-9897-fa07a9693985-IMG_2116_nobg.jpg',
    'fan-capacitor': '05f9fdc5-dbe5-452f-862f-135b5a0fd23e-IMG_2118_nobg.jpg',
    'dual-capacitor': '3fe6c438-8b6b-453c-adbb-39a2887bd605-IMG_2190_nobg.jpg',
    'start-capacitor': '79627c81-dc07-411a-947e-eb43ec5d97c8-IMG_2132_nobg.jpg',
    'universal-pcb': '83b9461b-9fa1-4363-a403-1668eaad89bb-IMG_20260906_123053_nobg.jpg',
    'contactor': '77bf2bb3-6d69-4ce9-b2c4-75707383ea31-IMG_20260419_113312_nobg.jpg',
    'outdoor-fan-motor': '78878c94-af81-4ad7-91bf-db119ee2d59d-IMG_20260419_144028_nobg.jpg',
    'service-valve': '74660846-92ec-4442-beb6-ca65c4b2c1e2-IMG_20260905_164413_nobg.jpg',
    'flare-nut': 'd1c11e45-f7cd-4c0a-8e8f-354fc5023b31-IMG_20260620_100414_nobg.jpg',
    'remote': 'b5430528-3749-4c88-8d1a-8b1ae565eb9a-ve309-light_nobg.jpg',
    'coil-cleaner': 'd6ccb2cb-e2f9-41bc-9263-f013246f889e-IMG_20260419_142053_nobg.jpg',
}

def photo_url(part):
    f = PHOTOS.get(part['id'])
    return PHOTO_BASE.format(f=f) if f else None

SOURCES = {
    'apna':   ('ApnaSpare – Air Conditioner spare parts listing (online retail, part-only prices)', 'https://apnaspare.com/products?parent_category=air-conditioner-spare-parts'),
    'royal':  ('Royal Aircon Services – Spare Parts Rate Card (incl. GST)', 'https://royalairconservices.com/spare-parts-price-list/'),
    'care':   ('Care My Appliance – AC Service Cost Estimation', 'https://caremyappliance.com/pricing/'),
    'easy':   ('Easy Repair – AC Spare Parts Rate Card (incl. GST)', 'https://easyrepair.co.in/ac-repair-and-service/'),
    'iitbhu': ('IIT (BHU) – Rate Contract for AC spares, FY 2023-24 (service incl., GST extra)', 'https://iitbhu.ac.in/contents/institute/2023/notification/noti_ipcell_ac_676.pdf'),
}
# Checked but not used: Leenspire Solutions (https://www.leenspiresolutions.com/spare-parts-price-list/) now redirects to a
# microwave-oven price page – no AC spare-part prices available on 18 Nov 2026.

CATEGORIES = [
    ('electrical', 'Electrical Components'),
    ('motors', 'Motors & Fans'),
    ('refrigeration', 'Refrigeration Components'),
    ('install', 'Installation Accessories'),
    ('remote', 'AC Remote Controls'),
]

# Each part: id, category, name, application, (low, high) or None, unit, basis, condition, image key, source keys, research note
PARTS = [
    # ---------------- A. Electrical ----------------
    dict(id='run-capacitor', cat='electrical', name='AC Run Capacitor (Compressor)', desc='Helps the compressor motor start and run. A weak capacitor causes humming, tripping or no cooling.',
         price=(290, 500), unit='piece', basis='ratecard', img='cap_run', src=['care', 'royal', 'easy', 'iitbhu'],
         note='Care ₹390 (25–60 MFD); Royal/Easy ₹500 (all ratings); IIT BHU ₹290–₹450 (36–60 MFD).'),
    dict(id='fan-capacitor', cat='electrical', name='Fan Capacitor', desc='Low-value capacitor for indoor/outdoor fan motors. A failed one makes the fan slow or stops it.',
         price=(130, 400), unit='piece', basis='mixed', img='cap_fan', src=['apna', 'care', 'royal', 'easy'],
         note='ApnaSpare ₹130–₹160 (3.15–8 MFD, part only); Care ₹240 (2.5–10 MFD); Royal/Easy ₹400.'),
    dict(id='dual-capacitor', cat='electrical', name='Dual Run Capacitor (Compressor + Fan)', desc='Combined capacitor serving both compressor and outdoor fan in many split ACs.',
         price=(230, 475), unit='piece', basis='mixed', img='cap_dual', src=['apna', 'care'],
         note='ApnaSpare ₹230 (DVM 8+5 to 12+5 MFD); Care ₹475 (combo).'),
    dict(id='start-capacitor', cat='electrical', name='Compressor Start Capacitor', desc='Electrolytic capacitor that gives a hard-starting compressor an extra push at switch-on. Used only on some models.',
         price=(200, 200), unit='piece', basis='online', img='cap_start', src=['apna'],
         note='ApnaSpare ₹200 (Indtech 40–60 / 60–80 MFD), part only.'),
    dict(id='universal-pcb', cat='electrical', name='Universal AC Control PCB (New)', desc='Aftermarket universal control board kit used when the original board is unavailable or uneconomical to repair.',
         price=(1300, 1460), unit='set', basis='mixed', img='pcb_universal', src=['apna', 'care'],
         note='ApnaSpare ₹1,300 (ADN9000 kit); Care ₹1,460 (convert PCB with remote).'),
    dict(id='original-pcb', cat='electrical', name='Original Brand PCB (New Replacement)', desc='Genuine model-specific indoor or outdoor board. Price depends entirely on brand and model.',
         price=None, unit='piece', basis='ratecard', img='pcb_original', src=[],
         note='Brand/model specific – sources list branded parts "at MRP". Price on request.'),
    dict(id='pcb-repair', cat='electrical', name='Non-Inverter PCB Repair', desc='Repair of the existing board (component-level), not a new board.',
         price=(1200, 2500), unit='repair', basis='ratecard', img='pcb_repair', src=['care', 'royal', 'easy'],
         note='Care ₹1,450; Royal ₹1,200 (outdoor) / ₹2,000 (indoor); Easy ₹1,500 / ₹2,500.'),
    dict(id='inverter-pcb-repair', cat='electrical', name='Inverter PCB Repair', desc='Repair of an inverter AC board. Not the price of a new original inverter PCB.',
         price=(3000, 5500), unit='repair', basis='ratecard', img='pcb_inverter', src=['care', 'royal', 'easy'],
         note='Care ₹4,400; Royal ₹3,500 (outdoor) / ₹5,500 (indoor); Easy ₹3,000.'),
    dict(id='sensor', cat='electrical', name='Temperature Sensor / Thermistor', desc='Room or coil sensor that tells the PCB the temperature. Faulty sensors cause wrong cut-off or error codes.',
         price=(330, 450), unit='piece', basis='ratecard', img='sensor', src=['care', 'royal', 'easy', 'iitbhu'],
         note='Care ₹330; Royal/Easy ₹350; IIT BHU ₹450.'),
    dict(id='contactor', cat='electrical', name='AC Contactor / Relay', desc='Switches power to the compressor and outdoor fan. Burnt contacts stop the outdoor unit.',
         price=(280, 1450), unit='piece', basis='mixed', img='contactor', src=['apna', 'care', 'iitbhu'],
         note='ApnaSpare ₹280–₹320 (contactor relay); Care ₹480 (general) / ₹1,450 (Daikin, O-General); IIT BHU relay ₹450.'),
    dict(id='pcb-fuse', cat='electrical', name='PCB Fuse', desc='Protects the control board. Usually replaced together with finding the cause of the blown fuse.',
         price=(100, 130), unit='piece', basis='ratecard', img='fuse', src=['care', 'royal', 'easy'],
         note='Royal/Easy ₹100; Care ₹130 (fuse change in PCB).'),
    dict(id='connector-wire', cat='electrical', name='Connecting Wire (Indoor–Outdoor)', desc='Multi-core cable between indoor and outdoor units.',
         price=(95, 150), unit='metre', basis='ratecard', img='wire', src=['care', 'royal', 'easy'],
         note='Care ₹95/m; Royal/Easy ₹150/m (4-core).'),

    # ---------------- B. Motors & fans ----------------
    dict(id='indoor-fan-motor', cat='motors', name='Indoor Fan / Blower Motor (AC or DC type)', desc='Drives the indoor blower that pushes cool air into the room. Inverter models usually use a DC (BLDC) motor.',
         price=(1500, 3000), unit='piece', basis='ratecard', img='motor_indoor', src=['royal', 'easy', 'care', 'iitbhu'],
         variants=[('AC motor – non-inverter split AC', (1500, 1750)), ('Blower motor – split AC', (2099, 2900)), ('DC / BLDC motor – inverter split AC', (2200, 3000))],
         note='Royal/Easy ₹1,500; Care ₹1,750 (fan motor) / ₹2,099 (blower); Easy ₹2,200 and Royal ₹3,000 (DC); IIT BHU ₹2,900.'),
    dict(id='outdoor-fan-motor', cat='motors', name='Outdoor Fan Motor (Condenser)', desc='Runs the outdoor fan that cools the condenser coil. A failed motor causes high pressure and poor cooling.',
         price=(1200, 4000), unit='piece', basis='mixed', img='motor_outdoor', src=['apna', 'royal', 'easy', 'iitbhu'],
         note='ApnaSpare ₹1,200–₹1,320 (part only, 45–68 W); Royal/Easy ₹2,000; IIT BHU ₹4,000.'),
    dict(id='window-fan-motor', cat='motors', name='Window AC Fan Motor', desc='Double-shaft motor that drives both the blower and the condenser fan in a window AC.',
         price=(2580, 2950), unit='piece', basis='ratecard', img='motor_window', src=['care', 'iitbhu'],
         note='Care ₹2,580; IIT BHU ₹2,950 (blower motor – window AC).'),
    dict(id='swing-motor', cat='motors', name='Swing Motor (Louver Motor)', desc='Small stepper motor that moves the air-flow flap up and down.',
         price=(380, 400), unit='piece', basis='ratecard', img='motor_swing', src=['care', 'royal', 'easy'],
         note='Care ₹380; Royal/Easy ₹400.'),
    dict(id='fan-blade', cat='motors', name='Outdoor Fan Blade', desc='Propeller blade on the outdoor fan motor. Cracked blades cause noise and vibration.',
         price=(600, 680), unit='piece', basis='ratecard', img='fan_blade', src=['royal', 'easy', 'care'],
         note='Royal/Easy ₹600; Care ₹680.'),
    dict(id='swing-blade', cat='motors', name='Swing Blade (Louver)', desc='Horizontal flap on the indoor unit that directs air flow.',
         price=(380, 400), unit='piece', basis='ratecard', img='swing_blade', src=['care', 'royal', 'easy'],
         note='Care ₹380; Royal/Easy ₹400.'),
    dict(id='blower-wheel', cat='motors', name='Indoor Blower Wheel (Cross-flow Fan)', desc='Long cylindrical fan inside the indoor unit. Broken fins cause noise and weak air.',
         price=(1050, 1050), unit='piece', basis='ratecard', img='blower_wheel', src=['care'],
         note='Care ₹1,050 (blower replaced) – single source.'),

    # ---------------- C. Refrigeration ----------------
    dict(id='compressor', cat='refrigeration', name='Compressor – Non-Inverter (New)', desc='Heart of the AC that pumps refrigerant. Price rises with tonnage (1 / 1.5 / 2 Ton).',
         price=(5000, 10600), unit='piece', basis='ratecard', img='compressor', src=['royal', 'easy', 'care', 'iitbhu'],
         note='Royal/Easy ₹5,000; Care ₹6,450 (0.8–1 T) / ₹7,399 (1.5 T) / ₹9,050 (2 T); IIT BHU ₹7,300 (1 T) / ₹8,050 (1.5 T) / ₹10,600 (2 T).'),
    dict(id='compressor-inverter', cat='refrigeration', name='Compressor – Inverter (New)', desc='Model-specific inverter (BLDC) compressor. Must match the outdoor PCB and refrigerant.',
         price=None, unit='piece', basis='ratecard', img='compressor_inv', src=[],
         note='No reliable public price for new inverter compressors – model-specific quotation.'),
    dict(id='compressor-refurb', cat='refrigeration', name='Compressor – Inverter (Refurbished)', desc='Refurbished, not new. Listed separately so condition is clear; warranty terms differ from new parts.',
         price=(7500, 7500), unit='piece', basis='ratecard', img='compressor_refurb', src=['royal', 'easy'], condition='Refurbished',
         note='Royal/Easy ₹7,500 (refurb compressor – inverter AC).'),
    dict(id='condenser-coil', cat='refrigeration', name='Condenser Coil (Outdoor) – 1 / 1.5 / 2 Ton', desc='Outdoor copper coil that releases heat. Replaced when leaking or badly corroded. Price depends on tonnage.',
         price=(3799, 6500), unit='piece', basis='ratecard', img='coil_condenser', src=['care', 'royal', 'easy'],
         variants=[('1 Ton', (3799, 4500)), ('1.5 Ton', (4399, 5900)), ('2 Ton', (4799, 6500))],
         note='Care ₹3,799 / ₹4,399 / ₹4,799; Royal/Easy ₹4,500 / ₹5,900 / ₹6,500 (1 / 1.5 / 2 Ton).'),
    dict(id='evaporator', cat='refrigeration', name='Evaporator / Cooling Coil (Split AC)', desc='Indoor coil that absorbs heat from room air. Leaks here cause repeated gas loss.',
         price=(6000, 9600), unit='piece', basis='ratecard', img='coil_evap', src=['royal', 'easy', 'care'],
         note='Royal/Easy ₹6,000 (up to 1.5 T) / ₹9,600 (1.5–2 T); Care ₹6,450.'),
    dict(id='expansion-valve', cat='refrigeration', name='Expansion Valve', desc='Controls refrigerant flow into the cooling coil (used in many inverter models).',
         price=(900, 1099), unit='piece', basis='ratecard', img='exp_valve', src=['royal', 'easy', 'care'],
         note='Royal/Easy ₹900; Care ₹1,099.'),
    dict(id='capillary', cat='refrigeration', name='Capillary Tube (with Filter)', desc='Thin copper tube that meters refrigerant in non-inverter ACs. Blockage causes poor cooling.',
         price=(250, 375), unit='set', basis='ratecard', img='capillary', src=['royal', 'easy', 'care', 'iitbhu'],
         note='Royal/Easy ₹250 (capillary); Care ₹330 and IIT BHU ₹375 (capillary + filter).'),
    dict(id='service-valve', cat='refrigeration', name='Service Valve (3-Way)', desc='Brass valve on the outdoor unit where pipes connect and gas is charged.',
         price=(350, 550), unit='piece', basis='mixed', img='service_valve', src=['apna', 'royal', 'easy'],
         note='ApnaSpare ₹350 (3/8") / ₹490 (5/8"), part only; Royal/Easy ₹550.'),
    dict(id='flare-nut', cat='refrigeration', name='Flare Nut', desc='Brass nut that joins copper pipes to valves. Cracked nuts are a common leak point.',
         price=(90, 160), unit='piece', basis='mixed', img='flare_nut', src=['apna', 'royal', 'easy', 'care'],
         note='ApnaSpare ₹90 (5/16") to ₹160 (1/2 x 5/8" heavy), part only; Royal/Easy ₹100; Care ₹140.'),
    dict(id='pin-valve', cat='refrigeration', name='Pin Valve (Schrader Valve)', desc='Small valve core in the service port used to check pressure and charge gas.',
         price=(50, 50), unit='piece', basis='ratecard', img='pin_valve', src=['royal', 'easy'],
         note='Royal/Easy ₹50.'),

    # ---------------- D. Installation & accessories ----------------
    dict(id='copper-pipe', cat='install', name='Copper Pipe Extension (per metre)', desc='Refrigerant pipe between indoor and outdoor units, charged per extra metre beyond the standard installation length.',
         price=(750, 840), unit='metre', basis='ratecard', img='copper_set', src=['royal', 'easy', 'care'],
         variants=[('Copper pipe only', 750), ('Copper pipe set with insulation & connecting wire', 840)],
         note='Royal/Easy ₹750 per metre (copper pipe); Care ₹840 per metre (with insulation, wire).'),
    dict(id='drain-pipe', cat='install', name='Drain Pipe (Flexible / Hard)', desc='Carries condensed water away from the indoor unit.',
         price=(100, 100), unit='metre', basis='ratecard', img='drain_pipe', src=['royal', 'easy'],
         note='Royal/Easy ₹100 per metre.'),
    dict(id='odu-bracket', cat='install', name='Outdoor Unit Bracket / Wall Stand', desc='Steel wall stand that holds the outdoor unit. Rusted stands should be replaced for safety.',
         price=(700, 1150), unit='set', basis='ratecard', img='bracket', src=['royal', 'care', 'easy', 'iitbhu'],
         note='Royal ₹700; Care ₹710 (split AC wall stand); Easy ₹750; IIT BHU ₹1,150.'),
    dict(id='remote-pcb', cat='remote', name='Remote with Receiver PCB Set', desc='Remote plus matching receiver/display board, used when both are faulty or missing.',
         price=(2700, 2700), unit='set', basis='ratecard', img='remote_pcb', src=['iitbhu'],
         note='IIT BHU ₹2,700 (remote with PCB circuit – split AC), FY 2023-24.'),
    dict(id='water-tray', cat='install', name='Indoor Drain / Water Tray', desc='Collects condensed water under the cooling coil. Cracked trays cause water leakage.',
         price=(470, 470), unit='piece', basis='ratecard', img='water_tray', src=['care'],
         note='Care ₹470 – single source.'),
    dict(id='air-filter', cat='install', name='Air Filter (Indoor Unit)', desc='Washable dust filter. Size and clip type vary by model.',
         price=(300, 300), unit='piece', basis='ratecard', img='filter', src=['iitbhu'],
         note='IIT BHU ₹300 (air filter, window/split), FY 2023-24 – model-specific in practice.'),
    dict(id='coil-cleaner', cat='install', name='AC Coil Cleaner Foam Spray', desc='Foam cleaner for indoor/outdoor coils (350 g can).',
         price=(240, 240), unit='piece', basis='online', img='coil_cleaner', src=['apna'],
         note='ApnaSpare ₹240 (Vinam 350 g / 450 ml).'),
    dict(id='anti-rust', cat='install', name='Anti-Rust Coating (Coil)', desc='Protective spray/coating for coils and joints to slow corrosion.',
         price=(230, 300), unit='application', basis='ratecard', img='anti_rust', src=['care', 'royal', 'easy'],
         note='Care ₹230 (anti-rust spray); Royal/Easy ₹300 (anti-rust coating).'),
]

# ---------------- ApnaSpare catalogue (every AC listing, 18 Nov 2026) ----------------
import json as _json, os as _os, re as _re
_CAT = _json.load(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'data', 'apnaspare_ac_2026-11-18.json'), encoding='utf-8'))['items']

def _short(t):
    """Readable model name from an ApnaSpare title (keeps size / rating / model code)."""
    code = _re.search(r'\|\s*([A-Z][A-Z0-9][A-Z0-9\-]{1,14})\s*\|', t)
    head = _re.split(r'\s+[–—]\s+|\s+\|\s+', t)[0].strip()
    head = _re.sub(r'\s+Compatible Replacement Remote.*$', '', head)
    if code and code.group(1) not in head:
        head += ' (' + code.group(1) + ')'
    return _re.sub(r'\s{2,}', ' ', head)

def _variants(items):
    """(name, price) per listing; names that collide are extended with their distinguishing detail."""
    names = [_short(i['t']) for i in items]
    out = []
    for i, n in zip(items, names):
        if names.count(n) > 1:
            segs = _re.split(r'\s+[–—]\s+|\s+\|\s+', i['t'])
            extra = segs[1] if len(segs) > 1 else ''
            extra = _re.sub(r'\s*Refrigeration Pipe Bending Tool.*$', '', extra)
            n = (n + ' – ' + extra[:48].rstrip(' ,&')) if extra else n
        out.append((n, i['p']))
    return sorted(set(out), key=lambda v: (v[1], v[0]))

def _fam(key, pred=None):
    return [it for it in _CAT if it['c'] == key and (pred is None or pred(it['t']))]

_RB = ['LG', 'Voltas', 'Daikin', 'Samsung', 'Blue Star', 'Hitachi', 'Panasonic', 'Lloyd', 'Godrej', 'Carrier', 'Haier',
       'Whirlpool', 'O General', 'Onida', 'Mitsubishi']
_OTHER = ['IFB', 'Midea', 'Hisense', 'Kelvinator', 'Croma', 'Videocon', 'MarQ', 'Gree', 'Electrolux', 'BPL', 'Amstrad', 'Acer', 'Azure', 'Akabishi', 'Ryoku']

def remote_group(t):
    tl = t.lower()
    if _re.search(r'universal|5000-in-1|baba 2001', tl): return 'universal'
    m = _re.match(r'AC Remote Control Suitable for (\w+)', t)
    if m: return m.group(1)
    lead = _re.split(r' AC Remote| Remote', t)[0]
    if _re.search(r',|&', lead) or _re.match(r'(AC-\d|AC Remote No|\d+A? AC Remote)', t): return 'multi'
    if tl.startswith('akabishi'): return 'Mitsubishi'
    if tl.startswith('ryoku'): return 'Hitachi'
    for b in _RB:
        if tl.startswith(b.lower()): return b
    for b in _OTHER:
        if tl.startswith(b.lower()): return 'other'
    return 'generic'   # model-coded LCD replacements (VE / Azone series)

PHOTOS.update({
    'square-capacitor': '95ed502b-a971-4fc0-b776-0e8b102b2325-IMG_20260419_105934_nobg.jpg',
    'condenser-union': '227e599c-337a-4259-831b-2a80c5839d08-IMG_20260419_110240_nobg.jpg',
    'tube-bender': '35356230-71ce-48ea-af36-3a97f43d1dae-IMG_20260425_103503_nobg.jpg',
    'run-capacitor': '93665b6a-7ba5-4571-98dd-483deaef3760-IMG_2068_nobg.jpg',
    'dual-capacitor': '54d35957-ea35-4dcf-bacd-52bdefd7307f-IMG_2089_nobg.jpg',
    'remote-universal': 'b5430528-3749-4c88-8d1a-8b1ae565eb9a-ve309-light_nobg.jpg',
    'remote-lg': '0f8d0bc5-bb78-40b3-993d-14cf566b1a49-lgremote2_nobg.jpg',
    'remote-voltas': 'c956ac34-b47e-457b-bf05-0cea993398aa-voltas248_nobg.jpg',
    'remote-daikin': '896bbed7-38ce-4c16-bc9b-51515c055816-ve132c_nobg.jpg',
    'remote-samsung': 'ec6a6228-7259-4302-960f-c241daef23fb-ve11_nobg.jpg',
    'remote-blue-star': '4c69d94b-c9da-42a0-8783-8104ec9eb69b-bluestar310_nobg.jpg',
    'remote-hitachi': 'fdc7cb89-d6c4-416f-93c1-e1adf31fc11b-ve272a_nobg.jpg',
    'remote-panasonic': 'c0394813-7483-45bf-afb5-057ad261b181-PanasonicA75C3623_nobg.jpg',
    'remote-lloyd': '3074066c-e155-4174-b97e-9fdac91156d1-ac253_nobg.jpg',
    'remote-godrej': '6466b9c7-c40d-4690-b643-801d0259b35d-ac125_nobg.jpg',
    'remote-carrier': '51e5d74e-c274-441c-b4c4-3941cca9b525-ve148a_nobg.jpg',
    'remote-haier': '2d9d4df1-4fa5-4516-b5ab-2b4c04b7a40f-ac190_nobg.jpg',
    'remote-whirlpool': 'a477f462-d13c-4ad1-8159-30f99c39a942-whirlpool225_nobg.jpg',
    'remote-o-general': '0f6c30e3-2ae3-4d02-be00-be0f6177134a-ac252a_nobg.jpg',
    'remote-onida': '5607439c-cb43-4538-905a-62259a377043-ve191a_nobg.jpg',
    'remote-mitsubishi': '45d41cb1-007a-47d3-ac91-084f6b8ec232-ac122_nobg.jpg',
    'remote-other': '9122b0ee-db13-4140-a779-366e4013ba6b-ksailm01-kelvinator_nobg.jpg',
    'remote-multi': '3e704cef-edb1-44fa-a63a-c866e0bd4301-41_nobg.jpg',
    'remote-generic': '9a7904f4-c421-4448-b305-44ebb8dd3850-ve307_nobg.jpg',
})

_BYID = {p['id']: p for p in PARTS}

def _attach(pid, items, merge_low=True):
    """Attach ApnaSpare variants to an existing row and widen its range with the online prices."""
    p = _BYID[pid]
    p['variants'] = _variants(items)
    lo = min(i['p'] for i in items); hi = max(i['p'] for i in items)
    if p['price']:
        p['price'] = (min(lo, p['price'][0]), max(hi, p['price'][1]))
    else:
        p['price'] = (lo, hi)
    if 'apna' not in p['src']: p['src'] = ['apna'] + p['src']
    if p['basis'] == 'ratecard': p['basis'] = 'mixed'

_attach('run-capacitor', _fam('compcap'))
_attach('dual-capacitor', _fam('dual') + _fam('dualsmall'))
_attach('fan-capacitor', _fam('fancap'))
_attach('start-capacitor', _fam('startcap'))
_attach('contactor', _fam('contactor'))
_attach('universal-pcb', _fam('upcb'))
_attach('outdoor-fan-motor', _fam('odmotor'))
_attach('service-valve', _fam('svalve'))
_attach('flare-nut', _fam('flarenut'))
_attach('coil-cleaner', _fam('cleaner'))
_BYID['run-capacitor']['note'] = 'ApnaSpare ₹230–₹260 (Uniqe 30–55 MFD, part only); Care ₹390; IIT BHU ₹290–₹450; Royal/Easy ₹500.'
_BYID['dual-capacitor']['note'] = 'ApnaSpare ₹230–₹300 (Uniqe 36+2 to 60+4 MFD and DVM Gold 8+5 to 12+5 MFD, part only); Care ₹475.'
_BYID['dual-capacitor']['desc'] = 'Combined capacitor serving both the compressor and the outdoor fan in most split ACs. Rating must match the label (e.g. 45+4 MFD).'
_BYID['contactor']['note'] = 'ApnaSpare ₹280 (1-pole) to ₹320 (4-pole), part only; Care ₹480 / ₹1,450 (Daikin, O-General); IIT BHU relay ₹450.'
_BYID['outdoor-fan-motor']['note'] = 'ApnaSpare ₹1,200–₹1,320 (Voltas 54W, Samsung 45W, LG/Haier 68W, Panasonic 58W, part only); Royal/Easy ₹2,000; IIT BHU ₹4,000.'

def _new(**kw):
    kw.setdefault('src', ['apna']); kw.setdefault('basis', 'online'); kw.setdefault('unit', 'piece')
    items = kw.pop('items')
    kw['variants'] = _variants(items)
    kw['price'] = (min(i['p'] for i in items), max(i['p'] for i in items))
    PARTS.append(kw); _BYID[kw['id']] = kw

_new(id='square-capacitor', cat='electrical', name='Square / PCB Capacitor (1–8 MFD)', img='cap_fan',
     desc='Small square fan capacitors used on indoor fan circuits and PCBs. Match the MFD value and pin type.',
     items=_fam('squarecap'), note='ApnaSpare ₹50 (2 MFD PCB) to ₹100 (8 MFD), Uniqe, part only.')
_new(id='condenser-union', cat='refrigeration', name='Condenser Union (Brass)', img='flare_nut',
     desc='Brass union that joins two copper pipes of the same size, used when extending or repairing refrigerant lines.',
     items=_fam('union'), note='ApnaSpare ₹99 (1/4") / ₹220 (5/8") / ₹270 (3/4"), part only.')
_new(id='tube-bender', cat='install', name='Spring Tube Bender (Copper Pipe)', img='copper_pipe',
     desc='Inner spring used by technicians to bend copper pipe without kinking it during installation.',
     items=_fam('bender'), note='ApnaSpare ₹190 (3/8" 3 ft) to ₹320 (5/8" 6 ft). Installation tool, not a part fitted to the AC.')

_RNAME = {'universal': 'Universal AC Remote (Multi-brand)', 'multi': 'Multi-brand Compatible AC Remote',
          'generic': 'Generic LCD Replacement AC Remote (VE / Azone series)', 'other': 'AC Remote – Other Brands'}
_RDESC = {'universal': '5000-in-1 and universal remotes that can be set to most AC brands using a brand code.',
          'multi': 'One remote model that fits several brands (e.g. Voltas, Lloyd, Godrej, Videocon). Check the model code on your old remote.',
          'generic': 'Model-coded compatible remotes matched to the button layout of many Indian AC brands.',
          'other': 'Compatible remotes for IFB, Midea, Hisense, Kelvinator, Croma, Videocon, MarQ, Gree, Electrolux, BPL, Amstrad, Acer and Azure ACs.'}
_rg = {}
for it in _fam('remote'):
    _rg.setdefault(remote_group(it['t']), []).append(it)
for g in ['universal'] + _RB + ['multi', 'other', 'generic']:
    if g not in _rg: continue
    rid = 'remote-' + g.lower().replace(' ', '-')
    _new(id=rid, cat='remote', img='remote', items=_rg[g],
         name=_RNAME.get(g, g + ' AC Remote (Compatible)'),
         desc=_RDESC.get(g, f'Compatible replacement remotes for {g} split and window ACs. Match the model code printed on the back of your old remote.'),
         note=f'ApnaSpare – {len(_rg[g])} {g if g in _RB else ""} remote models, part only.'.replace('  ', ' '))
_BYID['remote-universal']['price'] = (_BYID['remote-universal']['price'][0], 750)
_BYID['remote-universal']['src'] = ['apna', 'care']; _BYID['remote-universal']['basis'] = 'mixed'
_BYID['remote-universal']['note'] += ' Care ₹750 (universal remote).'

# ---------------- display order: most frequently replaced first in every category ----------------
ORDER = {
    'electrical': ['dual-capacitor', 'run-capacitor', 'fan-capacitor', 'contactor', 'sensor', 'pcb-repair', 'inverter-pcb-repair',
                   'universal-pcb', 'pcb-fuse', 'start-capacitor', 'connector-wire', 'square-capacitor', 'original-pcb'],
    'motors': ['outdoor-fan-motor', 'indoor-fan-motor', 'swing-motor', 'fan-blade', 'blower-wheel', 'swing-blade', 'window-fan-motor'],
    'refrigeration': ['flare-nut', 'capillary', 'service-valve', 'pin-valve', 'compressor', 'condenser-coil',
                      'evaporator', 'expansion-valve', 'condenser-union', 'compressor-inverter', 'compressor-refurb'],
    'install': ['copper-pipe', 'drain-pipe', 'odu-bracket', 'coil-cleaner', 'anti-rust', 'air-filter', 'water-tray', 'tube-bender'],
    'remote': ['remote-universal'] + ['remote-' + b.lower().replace(' ', '-') for b in _RB] + ['remote-multi', 'remote-other', 'remote-generic', 'remote-pcb'],
}
_seq = [i for c, _ in CATEGORIES for i in ORDER[c]]
assert sorted(_seq) == sorted(_BYID), (set(_seq) ^ set(_BYID))
assert len(_seq) == len(set(_seq)), 'duplicate row'
PARTS[:] = [_BYID[i] for i in _seq]
VARIANT_TOTAL = sum(len(p.get('variants', [])) for p in PARTS)

UNIT_LABEL = {'piece': 'per piece', 'metre': 'per metre', 'set': 'per set', 'repair': 'per repair', 'application': 'per application'}
BASIS_LABEL = {'online': 'Online part price', 'ratecard': 'Service rate-card price', 'mixed': 'Online + rate-card range'}

def inr(n):
    s = str(int(n))
    if len(s) <= 3: return '₹' + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head: parts.insert(0, head)
    return '₹' + ','.join(parts) + ',' + tail

def price_text(p):
    if not p['price']: return 'Price on request'
    lo, hi = p['price']
    return inr(lo) if lo == hi else f'{inr(lo)}–{inr(hi)}'

if __name__ == '__main__':
    for p in PARTS:
        print(f"{p['cat']:14} {p['name']:45} {price_text(p):18} {UNIT_LABEL[p['unit']]:15} {','.join(p['src'])}")
    print(len(PARTS), 'parts')
