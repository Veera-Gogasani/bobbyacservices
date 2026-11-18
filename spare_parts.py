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
    dict(id='indoor-fan-motor', cat='motors', name='Indoor Fan Motor (Split AC)', desc='Drives the indoor blower that pushes cool air into the room.',
         price=(1500, 1750), unit='piece', basis='ratecard', img='motor_indoor', src=['royal', 'easy', 'care'],
         note='Royal/Easy ₹1,500; Care ₹1,750 (fan motor – split AC).'),
    dict(id='blower-motor', cat='motors', name='Indoor Blower Motor (incl. DC type)', desc='Indoor blower motor; DC/BLDC versions are used in many inverter models.',
         price=(2099, 3000), unit='piece', basis='ratecard', img='motor_blower', src=['care', 'easy', 'iitbhu', 'royal'],
         note='Care ₹2,099; Easy ₹2,200; IIT BHU ₹2,900; Royal ₹3,000 (DC).'),
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
    dict(id='condenser-1t', cat='refrigeration', name='Condenser Coil – 1 Ton', desc='Outdoor copper coil that releases heat. Replaced when leaking or badly corroded.',
         price=(3799, 4500), unit='piece', basis='ratecard', img='coil_condenser', src=['care', 'royal', 'easy'],
         note='Care ₹3,799; Royal/Easy ₹4,500.'),
    dict(id='condenser-15t', cat='refrigeration', name='Condenser Coil – 1.5 Ton', desc='Outdoor copper coil for 1–1.5 Ton split ACs.',
         price=(4399, 5900), unit='piece', basis='ratecard', img='coil_condenser', src=['care', 'royal', 'easy'],
         note='Care ₹4,399; Royal/Easy ₹5,900 (1–1.5 T).'),
    dict(id='condenser-2t', cat='refrigeration', name='Condenser Coil – 2 Ton', desc='Outdoor copper coil for 1.5–2 Ton split ACs.',
         price=(4799, 6500), unit='piece', basis='ratecard', img='coil_condenser', src=['care', 'royal', 'easy'],
         note='Care ₹4,799; Royal/Easy ₹6,500 (1.5–2 T).'),
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
    dict(id='copper-pipe', cat='install', name='Copper Pipe', desc='Refrigerant pipe between indoor and outdoor units.',
         price=(750, 750), unit='metre', basis='ratecard', img='copper_pipe', src=['royal', 'easy'],
         note='Royal/Easy ₹750 per metre.'),
    dict(id='copper-pipe-set', cat='install', name='Copper Pipe Set (with Insulation & Wire)', desc='Pair of copper pipes with insulation and connecting wire – typical extension per metre.',
         price=(840, 840), unit='metre', basis='ratecard', img='copper_set', src=['care'],
         note='Care ₹840 per metre (with insulation, wire).'),
    dict(id='drain-pipe', cat='install', name='Drain Pipe (Flexible / Hard)', desc='Carries condensed water away from the indoor unit.',
         price=(100, 100), unit='metre', basis='ratecard', img='drain_pipe', src=['royal', 'easy'],
         note='Royal/Easy ₹100 per metre.'),
    dict(id='odu-bracket', cat='install', name='Outdoor Unit Bracket / Wall Stand', desc='Steel wall stand that holds the outdoor unit. Rusted stands should be replaced for safety.',
         price=(700, 1150), unit='set', basis='ratecard', img='bracket', src=['royal', 'care', 'easy', 'iitbhu'],
         note='Royal ₹700; Care ₹710 (split AC wall stand); Easy ₹750; IIT BHU ₹1,150.'),
    dict(id='remote', cat='install', name='AC Remote (Compatible / Universal)', desc='Replacement or universal remote. Compatibility depends on brand and model.',
         price=(299, 750), unit='piece', basis='mixed', img='remote', src=['apna', 'care'],
         note='ApnaSpare ₹299–₹399 (30+ compatible/universal remotes incl. Voltas, Daikin, Hitachi, Carrier, Whirlpool, part only); Care ₹750 (universal remote).'),
    dict(id='remote-pcb', cat='install', name='Remote with Receiver PCB Set', desc='Remote plus matching receiver/display board, used when both are faulty or missing.',
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
