# -*- coding: utf-8 -*-
"""Blog batch 2 (24 Nov 2026): 8 long-form SEO/AEO articles. English body; title/excerpt in EN/TE/HI.
Facts are checked against the linked sources; BOBBY prices are the owner-approved estimator ranges."""

def fig(src, alt, cap, w=800, h=500):
    return (f'<figure class="post-fig"><img src="{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">'
            f'<figcaption>{cap}</figcaption></figure>')

TEL = '<a href="tel:+918374889163">+91 83748 89163</a>'
EST = lambda svc, txt='Get a quick estimate': f'<a href="#estimate" data-estimate="{svc}">{txt}</a>'
D = '2026-11-24'

NEW_POSTS2 = [
# ------------------------------------------------------------------ 3. AC stops cooling in summer
{
 'slug': 'why-does-ac-stop-cooling-in-summer', 'img': 'blog_summer', 'svc': 'ac_repair', 'link': '/ac-repair-narasaraopet/', 'date': D, 'local': True,
 'seo': 'Why Does an AC Stop Cooling in Summer? Causes & Fixes | BOBBY',
 'desc': 'Why ACs lose cooling when it is 40–45°C outside: dirty condensers, weak capacitors, low gas, voltage drops and undersized ACs, plus safe checks and when to call a technician.',
 'title': ('Why Does an AC Stop Cooling During Summer? Causes, Checks & Fixes',
           'వేసవిలో ఏసీ ఎందుకు కూలింగ్ ఆపేస్తుంది? కారణాలు, తనిఖీలు & పరిష్కారాలు',
           'गर्मी में एसी ठंडा करना क्यों बंद कर देता है? कारण, जांच और समाधान'),
 'excerpt': ('Your AC cooled fine in March but struggles in May? Here is why peak summer exposes weak parts, what you can check safely, and what needs a technician.',
             'మార్చిలో బాగా కూల్ చేసిన ఏసీ మేలో ఇబ్బంది పడుతోందా? వేసవి వేడి బలహీన భాగాలను ఎలా బయటపెడుతుందో, మీరు చేయగల తనిఖీలు, టెక్నీషియన్ అవసరమైనవి ఇక్కడ.',
             'मार्च में ठीक ठंडा करने वाला एसी मई में संघर्ष कर रहा है? जानिए गर्मी कमज़ोर पार्ट्स को कैसे उजागर करती है, क्या खुद जांचें और कब टेक्नीशियन बुलाएं।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> an AC usually stops cooling in peak summer because the outdoor unit cannot throw heat out fast enough. A dusty condenser coil, a weak capacitor, low refrigerant from a slow leak, low voltage, or an AC that is too small for the room all show up first when it is 42–45°C outside. Clean filters and give the outdoor unit open air first; if cooling is still weak, get the AC inspected before the compressor overheats.</p>'
'<p>Many Narasaraopet homes notice the same pattern every year: the AC is comfortable in March, but by late April and May the room never gets properly cold, the outdoor unit runs non-stop, and the electricity bill jumps. That is not bad luck. Heat removal gets much harder as the outside temperature climbs, and any small weakness that went unnoticed in mild weather is suddenly exposed.</p>'
'<h2>Why summer is the real test for an AC</h2>'
'<p>An AC does not "make cold". It moves heat from your room to the outdoor unit, and the outdoor condenser coil releases that heat into outside air. The hotter that outside air is, the harder the condenser has to work. India\'s BEE star rating uses the ISEER method precisely because Indian ACs must keep working across a wide range of outdoor temperatures, up to the mid-40s. In Palnadu district, IMD heatwave warnings in April and May often mean outdoor units sit in direct sun at 45°C or more.</p>'
'<p>So the AC has less "spare capacity" in summer. A coil that is 20% blocked with dust, or a capacitor that has lost some strength, may be fine at 32°C but fail to keep up at 44°C.</p>'
+ fig('/assets/img/parts/coil_condenser.webp', 'AC outdoor condenser coil', 'The outdoor condenser coil must release all the heat taken from your room. Dust and blocked fins are the No. 1 summer problem.') +
'<h2>7 common reasons an AC stops cooling in summer</h2>'
'<h3>1. Dirty condenser coil or blocked outdoor unit</h3>'
'<p>Dust, leaves, bird nests or a wall placed too close in front of the outdoor unit trap hot air. The unit keeps recycling its own hot exhaust. Look for a unit that is very hot to touch and blowing weak, hot air. A proper <a href="/ac-outdoor-unit-cleaning-narasaraopet/">outdoor unit cleaning</a> often restores cooling in one visit.</p>'
'<h3>2. Clogged indoor filters and coil</h3>'
'<p>If the indoor filter is choked, less room air passes over the cold coil. The coil can even freeze, and then airflow drops further. Filters should be washed every 2 weeks in summer.</p>'
'<h3>3. Weak or failed capacitor</h3>'
'<p>The capacitor helps the compressor and fan motor start. Heat ages capacitors quickly. A weak one may let the fan spin but the compressor struggle or click on and off. It is a common, inexpensive part; see indicative prices on our <a href="/ac-spare-parts/">AC spare parts price list</a>.</p>'
'<h3>4. Low refrigerant because of a leak</h3>'
'<p>Gas does not "get used up". If it is low, it has leaked from a joint or coil. Symptoms include ice on the copper pipes, hissing, or cooling that gets slowly worse. The fix is to find and repair the leak first, then charge the correct amount; read <a href="/blog/ac-gas-filling-cost-r32-vs-r410a/">AC gas filling cost: R32 vs R410A</a>.</p>'
'<h3>5. Low or fluctuating voltage</h3>'
'<p>Summer evenings bring peak power demand. Low voltage makes the compressor draw more current and overheat, and protection may cut it out. A suitable stabiliser (for non-inverter ACs) and healthy wiring help.</p>'
'<h3>6. AC too small for the room or heat load</h3>'
'<p>A top-floor bedroom with a sun-facing wall, or a room with many people, may simply need more capacity than a 1-ton AC can give at 44°C.</p>'
'<h3>7. Wrong settings</h3>'
'<p>Eco, sleep or Dry mode, a very low fan speed, or a timer can all limit cooling. Since BEE rules, new star-labelled ACs default to 24°C, which is efficient but may feel warm in a hot room until it settles.</p>'
'<h2>Safe checks you can do before calling</h2>'
'<table><thead><tr><th>Check</th><th>What to look for</th></tr></thead><tbody>'
'<tr><td>Mode and setting</td><td>Cool mode, 24–26°C, fan on Auto or High</td></tr>'
'<tr><td>Indoor filters</td><td>Wash with plain water, dry fully, refit</td></tr>'
'<tr><td>Outdoor unit</td><td>At least 1–2 feet of open space in front; nothing covering it</td></tr>'
'<tr><td>Doors and windows</td><td>Closed; curtains drawn on sun-facing glass</td></tr>'
'<tr><td>Ice on pipes</td><td>If you see ice, switch off and call: do not keep running</td></tr>'
'</tbody></table>'
'<p>Do not open electrical covers, touch capacitors (they can hold a charge) or try to add gas yourself.</p>'
'<h2>When to call a technician</h2>'
'<ul><li>The outdoor unit fan runs but air indoors is not cold.</li><li>The outdoor unit hums, clicks or keeps switching on and off.</li><li>Ice forms on the pipes or the indoor coil.</li><li>The MCB trips or there is a burning smell (switch off immediately).</li><li>Cooling stays weak after cleaning filters and clearing the outdoor unit.</li></ul>'
'<p>BOBBY inspects the AC first, explains the fault and gives you an estimate before any repair. You can also ' + EST('ac_repair', 'check a quick estimate online') + ' or book <a href="/ac-repair-narasaraopet/">AC repair in Narasaraopet</a>.</p>'
'<h2>How to keep your AC cooling all summer</h2>'
'<ul><li>Get a full <a href="/ac-servicing-narasaraopet/">AC service</a> in February–March, before the heat; see <a href="/blog/best-time-to-service-ac-in-andhra-pradesh/">the best time to service your AC in Andhra Pradesh</a>.</li><li>Wash filters every two weeks from April to June.</li><li>Shade the outdoor unit from direct afternoon sun without blocking its airflow.</li><li>Use 24–26°C with a ceiling fan instead of 18°C.</li></ul>'
 ),
 'faq': [('Why does my AC cool at night but not in the afternoon?', 'In the afternoon the outdoor temperature is highest, so the condenser has the hardest job. A dirty condenser, a weak capacitor or low gas often shows up only during the hottest hours.'),
         ('Does an AC need gas every summer?', 'No. Refrigerant does not get used up. If your AC needs gas every year, there is a leak that should be found and repaired.'),
         ('Can low voltage stop my AC from cooling?', 'Yes. Low voltage can make the compressor overheat and cut out. A suitable stabiliser for non-inverter ACs and healthy wiring help.'),
         ('How much does it cost to fix an AC that is not cooling?', 'It depends on the cause: cleaning, a capacitor, a leak repair or gas. BOBBY inspects first and gives an estimate before starting work.')],
 'sources': [('BEE – Star labelling schedule for room air conditioners (ISEER, 24°C default)', 'https://beeindia.gov.in/sites/default/files/Schedule_24_LCAC.pdf'),
             ('LG India – What AC star ratings mean (ISEER tested up to high temperatures)', 'https://www.lg.com/in/magazine/what-star-ratings-really-mean-when-buying-an-ac-in-india/'),
             ('BOBBY – Why is my AC not cooling? (detailed troubleshooting)', '/blog/why-is-my-ac-not-cooling/'),
             ('BOBBY – AC spare parts price list', '/ac-spare-parts/')],
},
# ------------------------------------------------------------------ 4. Gas filling cost R32 vs R410A
{
 'slug': 'ac-gas-filling-cost-r32-vs-r410a', 'img': 'blog_gascost', 'svc': 'ac_gas', 'link': '/ac-gas-filling-narasaraopet/', 'date': D, 'local': True,
 'seo': 'AC Gas Filling Cost in 2026 – R32 vs R410A Explained | BOBBY',
 'desc': 'AC gas filling cost explained: typical price ranges, R32 vs R410A vs R22 differences, what affects the price, and why a leak check must come before any refill.',
 'title': ('AC Gas Filling Cost – R32 vs R410A Explained (2026 Guide)',
           'ఏసీ గ్యాస్ ఫిల్లింగ్ ఖర్చు – R32 vs R410A వివరణ (2026 గైడ్)',
           'एसी गैस फिलिंग की कीमत – R32 बनाम R410A (2026 गाइड)'),
 'excerpt': ('What AC gas filling really costs, how R32 and R410A differ, what pushes the price up, and how to avoid paying for gas that leaks out again.',
             'ఏసీ గ్యాస్ ఫిల్లింగ్ నిజంగా ఎంత ఖర్చవుతుంది, R32, R410A మధ్య తేడా, ధర పెరగడానికి కారణాలు, మళ్లీ లీకయ్యే గ్యాస్‌కు డబ్బు వృథా కాకుండా ఎలా.',
             'एसी गैस फिलिंग असल में कितने की पड़ती है, R32 और R410A में अंतर, कीमत किससे बढ़ती है, और दोबारा लीक होने वाली गैस पर पैसा बर्बाद होने से कैसे बचें।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> in 2026, AC gas filling for a typical home split AC in India usually costs about ₹2,000–₹3,500, and can reach ₹4,500 in some cities or for larger units. In Narasaraopet, BOBBY\'s estimate range is ₹2,000–₹3,500 per AC, including a leak check. R32 is now the most common gas in new Indian ACs; R410A is found in many older and some commercial units. The bigger cost question is not the gas type but whether a leak is repaired first.</p>'
'<h2>Typical AC gas filling charges in India (2026)</h2>'
'<table><thead><tr><th>AC type</th><th>Common gas</th><th>Typical range</th></tr></thead><tbody>'
'<tr><td>Split AC, 1–1.5 ton</td><td>R32 / R410A</td><td>₹2,000 – ₹3,500</td></tr>'
'<tr><td>Split AC, 2 ton</td><td>R32 / R410A</td><td>₹2,500 – ₹4,500</td></tr>'
'<tr><td>Window AC (older)</td><td>R22 / R32</td><td>₹1,800 – ₹3,000</td></tr>'
'<tr><td>Leak repair (brazing / flare joint)</td><td>–</td><td>Extra, quoted after inspection</td></tr>'
'</tbody></table>'
'<p>These are market ranges reported by large national service platforms; local prices vary with the gas price, how much refrigerant is needed and the work involved. For your own AC in Narasaraopet, ' + EST('ac_gas', 'see a quick estimate here') + ' or read our <a href="/ac-gas-filling-narasaraopet/">AC gas filling service</a> page.</p>'
'<h2>R32 vs R410A: what is the difference?</h2>'
'<table><thead><tr><th></th><th>R32</th><th>R410A</th><th>R22 (old)</th></tr></thead><tbody>'
'<tr><td>Global warming potential (GWP)</td><td>675</td><td>about 2,088</td><td>about 1,810</td></tr>'
'<tr><td>Ozone depletion</td><td>Zero</td><td>Zero</td><td>Depletes ozone (being phased out)</td></tr>'
'<tr><td>Composition</td><td>Single gas</td><td>Blend of two gases</td><td>Single gas</td></tr>'
'<tr><td>Top-up</td><td>Can be topped up on site</td><td>Usually recover and recharge fully</td><td>Old units only</td></tr>'
'<tr><td>Where you find it</td><td>Most new inverter split ACs</td><td>Older split and some commercial ACs</td><td>Older window/split ACs</td></tr>'
'</tbody></table>'
'<p>R32 has roughly one-third the global warming impact of R410A, which is why most manufacturers have moved to it. Because R32 is a single-component gas, it can be topped up without changing its composition; R410A is a blend, so a careful technician usually recovers it and recharges by weight. Both R32 and R410A run at high pressure, so the right gauges and tools matter.</p>'
+ fig('/assets/img/art/ac_gas-sm.webp', 'Technician checking AC refrigerant pressure with gauges', 'Pressure check with a gauge manifold: the first step before any refill.') +
'<h2>Never mix gases</h2>'
'<p>Your AC is designed for one refrigerant; it is printed on the outdoor unit\'s rating sticker. Filling R32 into an R410A system (or the reverse) damages performance and can harm the compressor. A genuine technician always reads the sticker first.</p>'
'<h2>What affects the price</h2>'
'<ul><li><b>How much gas is needed:</b> a small top-up costs less than a full recharge after a big leak.</li><li><b>Leak repair:</b> finding and brazing or re-flaring the leak adds cost but saves you a repeat refill.</li><li><b>Vacuuming:</b> after a leak or repair, the system should be vacuumed to remove air and moisture before charging.</li><li><b>Pipe length and tonnage:</b> bigger ACs and long pipe runs hold more refrigerant.</li><li><b>Inverter vs non-inverter:</b> not usually a big price difference for gas itself.</li></ul>'
'<h2>The honest way to fill AC gas</h2>'
'<ol><li>Check cooling, airflow and filters: many "gas problems" are actually dirty coils.</li><li>Measure the pressure against the gas type on the sticker.</li><li>If low, find the leak (joints, valves, coils) and repair it.</li><li>Vacuum the system.</li><li>Charge the correct gas to the manufacturer\'s standard.</li><li>Test cooling and pressures before leaving.</li></ol>'
'<p>This is exactly how BOBBY handles gas filling in Narasaraopet. If you are told your AC "needs gas every year", there is a leak; see <a href="/blog/ac-gas-filling-when-is-it-required/">when AC gas filling is really required</a>.</p>'
 ),
 'faq': [('How much does AC gas filling cost in Narasaraopet?', "BOBBY's estimate range is ₹2,000–₹3,500 per AC, including a leak check. Any leak repair is quoted after inspection, before work starts."),
         ('Is R32 better than R410A?', 'R32 has about one-third of the global warming potential of R410A, zero ozone impact and is easier to top up, which is why most new ACs use it. Your AC must always be filled with the gas it was designed for.'),
         ('Can R32 be filled in an R410A AC?', 'No. Never mix or switch refrigerants. Use only the gas printed on the outdoor unit sticker.'),
         ('How long does AC gas filling last?', 'In a leak-free AC, many years. If gas is needed again within months, the leak was not found and repaired.')],
 'sources': [('LG – R-32 refrigerant explained (GWP comparison: R-22, R-410A, R-32)', 'https://www.lg.com/global/business/insights/hvac/blog/r32-refrigerant-explained/'),
             ('Panasonic – R32, an environmentally friendly refrigerant', 'https://www.panasonic.com/ae/consumer/air-solutions/residential-air-conditioners-learn/features-explanation/r32-an-environmentally-friendly-refrigerant.html'),
             ('NoBroker – AC gas filling charges in India 2026 (market ranges)', 'https://www.nobroker.in/ac-services/ac-gas-filling-charges-acprd'),
             ('BOBBY – AC gas filling in Narasaraopet', '/ac-gas-filling-narasaraopet/')],
},
# ------------------------------------------------------------------ 5. Refrigerator not cooling
{
 'slug': 'refrigerator-not-cooling-causes-solutions', 'img': 'blog_fridge', 'svc': 'fridge', 'link': '/refrigerator-repair-narasaraopet/', 'date': D, 'local': True,
 'seo': 'Refrigerator Not Cooling? Common Causes & Solutions | BOBBY',
 'desc': 'Refrigerator not cooling? Check temperature settings, door seals, condenser coils, airflow and the compressor. Safe fixes, warning signs and when to call a technician.',
 'title': ('Refrigerator Not Cooling – Common Causes and Solutions',
           'ఫ్రిజ్ కూల్ కావడం లేదా – సాధారణ కారణాలు, పరిష్కారాలు',
           'फ्रिज ठंडा नहीं कर रहा – आम कारण और समाधान'),
 'excerpt': ('A warm fridge puts food at risk. Learn the right temperature, the 8 most common causes, what you can fix safely at home and when you need a technician.',
             'వెచ్చని ఫ్రిజ్ ఆహారాన్ని ప్రమాదంలో పడేస్తుంది. సరైన ఉష్ణోగ్రత, 8 సాధారణ కారణాలు, ఇంట్లో సురక్షితంగా చేయగలవి, టెక్నీషియన్ ఎప్పుడు అవసరమో తెలుసుకోండి.',
             'गर्म फ्रिज खाने को खतरे में डालता है। सही तापमान, 8 आम कारण, घर पर क्या सुरक्षित रूप से ठीक करें और कब टेक्नीशियन बुलाएं, जानिए।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> a refrigerator should stay at or below 4°C, with the freezer at about −18°C. If it is not cooling, check the temperature setting, the door gasket, the space behind the fridge and the condenser coils first. If the compressor is silent, it clicks repeatedly, or the freezer is cold but the fridge section is warm, it usually needs a technician.</p>'
'<h2>What temperature should a fridge be?</h2>'
'<p>Food-safety agencies such as the US FDA recommend keeping the refrigerator at or below 4°C (40°F) and the freezer at −18°C (0°F). Above 4°C, bacteria grow faster and food spoils sooner. Most fridge dials do not show actual temperatures, so an inexpensive fridge thermometer is the easiest way to check.</p>'
'<h2>8 common reasons a refrigerator stops cooling</h2>'
'<table><thead><tr><th>Cause</th><th>Signs</th><th>Can you fix it?</th></tr></thead><tbody>'
'<tr><td>Wrong thermostat setting</td><td>Everything slightly warm</td><td>Yes: set to the middle/recommended level</td></tr>'
'<tr><td>Door not sealing</td><td>Frost near the door, gasket dirty or loose</td><td>Clean it; replace if torn</td></tr>'
'<tr><td>No space behind fridge</td><td>Hot sides, compressor runs long</td><td>Yes: leave gap at back and sides</td></tr>'
'<tr><td>Dusty condenser coils</td><td>Weak cooling, high bills</td><td>Gentle cleaning (unplugged)</td></tr>'
'<tr><td>Overloaded / blocked vents</td><td>Cold in some places, warm in others</td><td>Yes: rearrange food</td></tr>'
'<tr><td>Defrost problem (frost-free)</td><td>Freezer iced up, fridge warm</td><td>Technician</td></tr>'
'<tr><td>Fan or sensor fault</td><td>No airflow inside, uneven cooling</td><td>Technician</td></tr>'
'<tr><td>Compressor / relay / gas leak</td><td>Compressor silent or clicking, no cooling</td><td>Technician</td></tr>'
'</tbody></table>'
+ fig('/assets/img/art/fridge-sm.webp', 'Technician checking a double door refrigerator', 'A quick inspection tells whether it is a setting, seal, airflow or sealed-system problem.') +
'<h2>Safe checks you can do at home</h2>'
'<ol><li><b>Check power and setting:</b> make sure it is plugged in properly and the thermostat is not on the lowest level.</li><li><b>Paper test on the door seal:</b> close the door on a sheet of paper. If it slides out easily, the gasket is not sealing. Clean it with warm water and mild soap.</li><li><b>Give it space:</b> manufacturers recommend a gap of about 5–10 cm at the back and sides so heat can escape.</li><li><b>Clean the coils:</b> unplug the fridge and gently brush dust from the condenser coils at the back or bottom.</li><li><b>Do not overpack:</b> leave room around the air vents inside.</li><li><b>Wait 24 hours</b> after cleaning or moving the fridge for temperatures to settle.</li></ol>'
'<h2>Warning signs that need a technician</h2>'
'<ul><li>The compressor is silent, or clicks on and off every few minutes.</li><li>The freezer is cold but the fridge section is warm (often a defrost or fan fault in frost-free models).</li><li>Heavy ice keeps building up on the back wall.</li><li>Water collects under or inside the fridge.</li><li>A burning smell or the fridge trips the MCB.</li></ul>'
'<p>BOBBY repairs single door and double door refrigerators at your home in Narasaraopet: inspection first, estimate before work. The visit charge is typically ₹300–₹500 plus parts if needed; ' + EST('fridge', 'see a quick estimate') + ' or book <a href="/refrigerator-repair-narasaraopet/">refrigerator repair</a>.</p>'
'<h2>Tips to keep a fridge cooling well</h2>'
'<ul><li>Let hot food cool before putting it in.</li><li>Clean the door gasket monthly.</li><li>Do not keep the fridge next to a stove or in direct sun.</li><li>Use a stabiliser if your area has frequent voltage swings.</li><li>Read our <a href="/blog/how-to-maintain-your-refrigerator/">refrigerator maintenance guide</a>.</li></ul>'
 ),
 'faq': [('What is the right temperature for a refrigerator?', 'At or below 4°C for the fridge and about −18°C for the freezer, as recommended by food-safety agencies such as the US FDA.'),
         ('Why is my freezer cold but the fridge warm?', 'In frost-free fridges this is often a defrost or fan problem that stops cold air moving from the freezer to the fridge. It needs a technician.'),
         ('How do I know if the door seal is bad?', 'Close the door on a sheet of paper. If it slides out easily, the gasket is not sealing. Frost near the door is another sign.'),
         ('Do you repair fridges at home in Narasaraopet?', 'Yes. BOBBY repairs refrigerators at your doorstep in Narasaraopet and nearby areas within about 20 km.')],
 'sources': [('US FDA – Are you storing food safely? (4°C fridge / −18°C freezer)', 'https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely'),
             ('LG India – Refrigerator not cooling: troubleshooting', 'https://www.lg.com/in/support/product-support/troubleshoot/help-library/cs-CT52006627-20155295251040/'),
             ('Samsung – Why your refrigerator is not cooling (clearance and coils)', 'https://www.samsung.com/au/support/home-appliances/why-your-samsung-refrigerator-is-not-cooling/'),
             ('BOBBY – Refrigerator repair in Narasaraopet', '/refrigerator-repair-narasaraopet/')],
},
# ------------------------------------------------------------------ 6. Washing machine not spinning
{
 'slug': 'washing-machine-not-spinning-causes-repair', 'img': 'blog_washer', 'svc': 'washer', 'link': '/washing-machine-repair-narasaraopet/', 'date': D, 'local': True,
 'seo': 'Washing Machine Not Spinning? Causes & Repair Options | BOBBY',
 'desc': 'Washing machine not spinning? Unbalanced loads, drain blockages, door locks, belts, motors and control boards explained, with safe checks and repair options.',
 'title': ('Washing Machine Not Spinning – Causes and Repair Options',
           'వాషింగ్ మెషిన్ తిరగడం లేదా – కారణాలు, రిపేర్ మార్గాలు',
           'वॉशिंग मशीन स्पिन नहीं कर रही – कारण और रिपेयर विकल्प'),
 'excerpt': ('Clothes still soaking wet? Find out why washing machines stop spinning, what to check safely, and when the belt, motor or control board needs repair.',
             'బట్టలు ఇంకా తడిగానే ఉన్నాయా? వాషింగ్ మెషిన్ ఎందుకు తిరగడం ఆపుతుంది, సురక్షితంగా ఏమి చూడాలి, బెల్ట్, మోటార్ లేదా బోర్డు రిపేర్ ఎప్పుడు అవసరం.',
             'कपड़े अब भी भीगे हैं? जानिए वॉशिंग मशीन स्पिन क्यों बंद करती है, सुरक्षित रूप से क्या जांचें और कब बेल्ट, मोटर या बोर्ड रिपेयर चाहिए।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> most washing machines that stop spinning have an unbalanced load, water that has not drained (blocked filter or hose), or a door/lid lock that is not engaging. Machines will not spin until water drains and the load is balanced. If the drum still does not turn with a small, even load, the drive belt, motor, motor capacitor or control board may need repair.</p>'
'<h2>Why the spin cycle stops</h2>'
'<p>Modern washing machines protect themselves. Sensors check the load balance, water level and door lock before high-speed spin. If any check fails, the machine slows down, keeps trying to rebalance, or stops with an error code. That is why the first checks are simple ones.</p>'
'<h2>Common causes, from simple to serious</h2>'
'<h3>1. Unbalanced load</h3>'
'<p>One heavy item (a blanket or jeans) or a tangled bedsheet throws the drum off-balance. Samsung, for example, shows codes such as "Ub" or "Ur" for this. Redistribute the clothes or add similar items, then run Spin only.</p>'
'<h3>2. Water not draining</h3>'
'<p>A machine will not spin while water remains. Check for a kinked or blocked drain hose, and on front loaders clean the debris (pump) filter near the bottom front. Coins, hair clips and lint often block it.</p>'
'<h3>3. Machine not level</h3>'
'<p>An uneven floor makes the machine vibrate and the sensors cut the spin. Adjust the legs until it sits firm and level.</p>'
'<h3>4. Lid or door lock problem</h3>'
'<p>If the lock does not engage, the machine will not spin for safety. A worn lock or a faulty switch needs replacement.</p>'
'<h3>5. Worn or broken drive belt</h3>'
'<p>Common in older top loaders and semi-automatics: the motor runs (you hear it) but the drum barely turns.</p>'
'<h3>6. Motor, capacitor or coupling fault</h3>'
'<p>A humming sound with no movement can point to a weak motor capacitor or a motor/coupling issue.</p>'
'<h3>7. Control board or sensor fault</h3>'
'<p>Repeated error codes after the basics are checked usually point to a sensor or the PCB.</p>'
+ fig('/assets/img/art/washer-sm.webp', 'Technician repairing a front load washing machine', 'Doorstep diagnosis: drain, balance, lock, belt, motor and board are checked in order.') +
'<h2>Quick checks before you call</h2>'
'<table><thead><tr><th>Check</th><th>How</th></tr></thead><tbody>'
'<tr><td>Balance the load</td><td>Spread clothes evenly; avoid washing one heavy item alone</td></tr>'
'<tr><td>Drain hose</td><td>Straight, not kinked, outlet not blocked</td></tr>'
'<tr><td>Debris filter (front load)</td><td>Unplug, place a tray, open and clean the filter</td></tr>'
'<tr><td>Level</td><td>Machine firm on all four feet</td></tr>'
'<tr><td>Restart</td><td>Switch off at the wall for 1 minute, then run Spin only</td></tr>'
'</tbody></table>'
'<p>Always unplug the machine before opening the filter, and never try to open the back panel yourself.</p>'
'<h2>Repair options</h2>'
'<table><thead><tr><th>Fault</th><th>Typical fix</th></tr></thead><tbody>'
'<tr><td>Blocked drain pump / filter</td><td>Clean or replace drain pump</td></tr>'
'<tr><td>Door / lid lock</td><td>Replace lock or switch</td></tr>'
'<tr><td>Drive belt</td><td>Replace belt</td></tr>'
'<tr><td>Motor capacitor / motor</td><td>Replace capacitor; repair or replace motor</td></tr>'
'<tr><td>PCB / sensor</td><td>Diagnose, repair or replace board / sensor</td></tr>'
'</tbody></table>'
'<p>BOBBY repairs top load, front load and semi-automatic machines at your home in Narasaraopet. The visit charge is typically ₹300–₹500 plus parts; ' + EST('washer', 'get a quick estimate') + ' or book <a href="/washing-machine-repair-narasaraopet/">washing machine repair</a>.</p>'
 ),
 'faq': [('Why does my washing machine fill and wash but not spin?', 'Usually the load is unbalanced, water has not drained fully, or the door lock is not engaging. If those are fine, the belt, motor or control board needs checking.'),
         ('What does the UE or UB code mean?', 'On many machines it means an unbalanced load. Redistribute the clothes and run a spin cycle. Check your manual, as codes vary by brand.'),
         ('Can a blocked filter stop spinning?', 'Yes. The machine will not spin until the water drains, and a blocked debris filter or drain hose is a common cause.'),
         ('Do you repair semi-automatic machines?', 'Yes. BOBBY repairs semi-automatic, top load and front load washing machines at home.')],
 'sources': [('Samsung – What to do if your washing machine is not spinning', 'https://www.samsung.com/ie/support/home-appliances/what-to-do-if-your-washing-machine-is-not-spinning/'),
             ('Samsung – Solution for no spinning (drain filter and hose)', 'https://www.samsung.com/sa_en/support/home-appliances/solution-for-no-spinning-of-washing-machine/'),
             ('BOBBY – Washing machine repair in Narasaraopet', '/washing-machine-repair-narasaraopet/')],
},
# ------------------------------------------------------------------ 7. Best time to service AC in AP
{
 'slug': 'best-time-to-service-ac-in-andhra-pradesh', 'img': 'blog_season', 'svc': 'ac_servicing', 'link': '/ac-servicing-narasaraopet/', 'date': D, 'local': True,
 'seo': 'Best Time to Service Your AC in Andhra Pradesh – Season Guide | BOBBY',
 'desc': 'When to service your AC in Andhra Pradesh: a month-by-month plan for Narasaraopet and coastal AP, why February–March is ideal, and what to do after the monsoon.',
 'title': ('Best Time to Service Your AC in Andhra Pradesh (Month-by-Month Guide)',
           'ఆంధ్రప్రదేశ్‌లో ఏసీ సర్వీస్ చేయించడానికి సరైన సమయం (నెలవారీ గైడ్)',
           'आंध्र प्रदेश में एसी सर्विस का सही समय (महीने-दर-महीने गाइड)'),
 'excerpt': ('Beat the April rush: a simple AC service calendar for Andhra Pradesh\'s climate, from the pre-summer service to the post-monsoon check.',
             'ఏప్రిల్ రద్దీకి ముందే: ఆంధ్రప్రదేశ్ వాతావరణానికి తగ్గ సులభమైన ఏసీ సర్వీస్ క్యాలెండర్, వేసవి ముందు సర్వీస్ నుండి వర్షాకాలం తర్వాత తనిఖీ వరకు.',
             'अप्रैल की भीड़ से पहले: आंध्र प्रदेश के मौसम के हिसाब से आसान एसी सर्विस कैलेंडर, गर्मी से पहले की सर्विस से मानसून के बाद की जांच तक।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> in Andhra Pradesh the best time to service your AC is February to mid-March, before the summer heat and the April–May rush. Plan a second check after the monsoon (October–November) if your AC runs a lot, and wash the filters every two weeks during peak summer.</p>'
'<h2>Why timing matters in Andhra Pradesh</h2>'
'<p>Coastal Andhra and Palnadu district get long, hot summers. IMD heatwave alerts in April and May regularly report 44–46°C in many districts. That is when every AC in town is running flat out, and when technicians are busiest. A dirty or slightly faulty AC that limps through March often fails in the first heatwave. Servicing it a few weeks earlier means better cooling, lower bills and no waiting for a technician in 45°C heat.</p>'
'<h2>A simple AC service calendar for Andhra Pradesh</h2>'
'<table><thead><tr><th>Months</th><th>Weather</th><th>What to do</th></tr></thead><tbody>'
'<tr><td>Jan</td><td>Mild, dry</td><td>Run the AC 10 minutes once a week; book your summer service slot</td></tr>'
'<tr><td><b>Feb – mid-Mar</b></td><td>Warming up</td><td><b>Full pre-summer service</b>: filters, indoor coil, outdoor condenser, drain, electrical check, cooling test</td></tr>'
'<tr><td>Apr – Jun</td><td>Peak heat (42–46°C)</td><td>Wash filters every 2 weeks; keep outdoor unit clear; book repairs early</td></tr>'
'<tr><td>Jul – Sep</td><td>Monsoon, humid</td><td>Use Dry mode on humid days; check drain for leaks</td></tr>'
'<tr><td>Oct – Nov</td><td>Post-monsoon</td><td>Second service for heavily used ACs; check for rust and drain blockages</td></tr>'
'<tr><td>Dec</td><td>Cooler</td><td>Cover the outdoor unit loosely only if unused; keep vents clear</td></tr>'
'</tbody></table>'
+ fig('/assets/img/art/ac_servicing-sm.webp', 'Technician servicing a split AC indoor unit', 'A pre-summer service in February or March prepares the AC for April–May heat.') +
'<h2>What a proper pre-summer service includes</h2>'
'<ul><li>Filter washing and indoor coil cleaning.</li><li>Outdoor condenser coil and fin cleaning (see <a href="/ac-outdoor-unit-cleaning-narasaraopet/">outdoor unit cleaning</a>).</li><li>Drain line flushing to prevent leaks.</li><li>Electrical connections and capacitor check.</li><li>Refrigerant pressure and cooling performance check.</li></ul>'
'<p>If your AC smells musty or airflow is weak, choose <a href="/ac-deep-cleaning-narasaraopet/">AC deep cleaning</a> instead of a basic service.</p>'
'<h2>How often should you service an AC?</h2>'
'<p>For most homes in Andhra Pradesh: one full service before summer, and a second after the monsoon if the AC runs many hours a day, is near a dusty road, or is in a shop or clinic. Filters should be cleaned far more often: every two weeks in peak summer.</p>'
'<h2>Book before the rush</h2>'
'<p>BOBBY\'s AC general servicing in Narasaraopet is typically ₹500–₹700 per AC. ' + EST('ac_servicing', 'Check a quick estimate') + ' or book <a href="/ac-servicing-narasaraopet/">AC servicing</a> early in the season.</p>'
 ),
 'faq': [('Which month is best for AC servicing in Andhra Pradesh?', 'February to mid-March, before summer heat and before technicians get busy in April and May.'),
         ('Should I service my AC after the monsoon?', 'Yes, if it runs a lot. A post-monsoon check in October–November clears drains and catches rust or leaks early.'),
         ('How often should I clean AC filters in summer?', 'About every two weeks from April to June, more often in dusty areas.'),
         ('Is servicing worth it if the AC is cooling fine?', 'Yes. Cleaning keeps it efficient, lowers power bills and catches small faults before the hottest weeks.')],
 'sources': [('Deccan Chronicle – IMD heatwave alerts across Andhra Pradesh (45°C+)', 'https://www.deccanchronicle.com/southern-states/andhra-pradesh/mercury-crosses-45c-heatwave-to-continue-in-ap-1958726'),
             ('BEE – Room air conditioner star labelling schedule', 'https://beeindia.gov.in/sites/default/files/Schedule_24_LCAC.pdf'),
             ('BOBBY – When should you service your AC?', '/blog/when-should-you-service-your-ac/'),
             ('BOBBY – AC servicing in Narasaraopet', '/ac-servicing-narasaraopet/')],
},
# ------------------------------------------------------------------ 8. AC installation checklist
{
 'slug': 'ac-installation-checklist-indian-homes', 'img': 'blog_install', 'svc': 'ac_install', 'link': '/ac-installation-narasaraopet/', 'date': D, 'local': True,
 'seo': 'AC Installation Checklist for Indian Homes – 15 Points | BOBBY',
 'desc': 'A 15-point AC installation checklist for Indian homes: placement, power supply, copper pipe, drain slope, outdoor stand, vacuum test and handover checks for split ACs.',
 'title': ('AC Installation Checklist for Indian Homes (15 Points to Check)',
           'భారతీయ ఇళ్లకు ఏసీ ఇన్‌స్టాలేషన్ చెక్‌లిస్ట్ (చూడాల్సిన 15 అంశాలు)',
           'भारतीय घरों के लिए एसी इंस्टॉलेशन चेकलिस्ट (जांचने के 15 बिंदु)'),
 'excerpt': ('Bad installation causes most AC leaks, noise and weak cooling. Use this 15-point checklist before, during and after your split AC is installed.',
             'చాలా ఏసీ లీకులు, శబ్దం, బలహీన కూలింగ్‌కు తప్పు ఇన్‌స్టాలేషనే కారణం. స్ప్లిట్ ఏసీ ఇన్‌స్టాలేషన్ ముందు, సమయంలో, తర్వాత ఈ 15 అంశాల చెక్‌లిస్ట్ వాడండి.',
             'ज़्यादातर एसी लीक, आवाज़ और कमज़ोर कूलिंग की वजह खराब इंस्टॉलेशन है। स्प्लिट एसी इंस्टॉलेशन से पहले, दौरान और बाद में यह 15-बिंदु चेकलिस्ट अपनाएं।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> a good split AC installation needs the right location for both units, a dedicated power point with proper earthing, correctly sized and sealed copper pipes, a drain pipe with a continuous downward slope, a firm outdoor stand with space to breathe, a vacuum test before start-up, and a full cooling test before the technician leaves.</p>'
'<p>Most "AC problems" we are called for in the first year (water dripping indoors, noisy outdoor units, weak cooling, gas leaks) trace back to the installation. Use this checklist whether you buy online, from a showroom or shift an old AC.</p>'
'<h2>Before installation: plan the location</h2>'
'<ol><li><b>Indoor unit height and position:</b> about 7–8 feet high, on a strong wall, where air reaches the whole room, away from direct heat sources.</li><li><b>Outdoor unit location:</b> shaded if possible, with open space in front and at the sides so hot air can escape; not facing a wall closely.</li><li><b>Distance between units:</b> as short as practical. Very long pipe runs reduce efficiency and may need extra gas.</li><li><b>Power point:</b> a dedicated socket and wiring suitable for the AC load, with proper earthing and an MCB.</li><li><b>Stabiliser:</b> check whether your model needs one; many inverter ACs have a wide voltage range, older non-inverter ACs often need one.</li></ol>'
+ fig('/assets/img/parts/copper_set.webp', 'Copper pipe set for split AC installation', 'Correctly sized, insulated copper pipes with tight flare joints prevent gas leaks.') +
'<h2>During installation: what to watch</h2>'
'<ol start="6"><li><b>Wall bracket level:</b> the indoor unit must be level (or tilted slightly to the drain side as the manual says).</li><li><b>Copper pipes:</b> correct size for your model, insulated, with clean flare joints tightened properly.</li><li><b>Drain pipe slope:</b> a continuous downward slope with no loops, so water never flows back.</li><li><b>Wiring:</b> neat, secured connections; no loose joints or tape-only connections.</li><li><b>Outdoor stand:</b> firm wall bracket or level base with anti-vibration pads.</li><li><b>Wall hole sealing:</b> sealed after piping to keep out water, insects and hot air.</li><li><b>Vacuuming:</b> the pipes and indoor coil should be vacuumed before releasing refrigerant, to remove air and moisture.</li></ol>'
'<h2>After installation: handover checks</h2>'
'<ol start="13"><li><b>Leak check</b> at all joints.</li><li><b>Cooling test:</b> cold air within minutes, outdoor fan and compressor running smoothly, no unusual noise.</li><li><b>Drain test:</b> pour a little water in the indoor tray or watch condensate after 20–30 minutes; it should drain outside, not drip indoors.</li></ol>'
'<table><thead><tr><th>Common extra</th><th>When you may need it</th></tr></thead><tbody>'
'<tr><td>Extra copper pipe</td><td>Units more than the standard kit length apart</td></tr>'
'<tr><td>Outdoor stand / bracket</td><td>Wall mounting the outdoor unit</td></tr>'
'<tr><td>Extra drain pipe</td><td>Long drain route</td></tr>'
'<tr><td>Wiring / socket</td><td>No suitable power point near the AC</td></tr>'
'</tbody></table>'
'<p>A genuine installer tells you about any extras and their cost <b>before</b> starting. Indicative prices for pipes, brackets and drain pipe are on our <a href="/ac-spare-parts/">AC spare parts price list</a>.</p>'
'<h2>Book a proper installation</h2>'
'<p>BOBBY installs split and window ACs and handles AC shifting in Narasaraopet. Split AC installation is typically ₹1,500–₹2,500; ' + EST('ac_install', 'get a quick estimate') + ' or see <a href="/ac-installation-narasaraopet/">AC installation &amp; shifting</a>.</p>'
 ),
 'faq': [('How high should a split AC indoor unit be installed?', 'Typically about 7–8 feet from the floor, on a strong wall, where air can reach the whole room. Follow your model\'s manual.'),
         ('Is vacuuming necessary during AC installation?', 'Yes. Vacuuming removes air and moisture from the pipes before releasing refrigerant, which protects cooling performance and the compressor.'),
         ('Why does a new AC drip water indoors?', 'Usually the drain pipe does not slope continuously downward, or the indoor unit is not level.'),
         ('How much does split AC installation cost in Narasaraopet?', "BOBBY's estimate is typically ₹1,500–₹2,500; extra pipe, stand or wiring is quoted before work starts.")],
 'sources': [('LG India – AC installation, service and repair guide', 'https://www.lg.com/in/magazine/ac-installation-service-repair-guide/'),
             ('BEE – Room air conditioner star labelling schedule', 'https://beeindia.gov.in/sites/default/files/Schedule_24_LCAC.pdf'),
             ('BOBBY – AC installation & shifting in Narasaraopet', '/ac-installation-narasaraopet/'),
             ('BOBBY – AC spare parts price list', '/ac-spare-parts/')],
},
# ------------------------------------------------------------------ 9. Identify a genuine technician
{
 'slug': 'how-to-identify-genuine-ac-repair-technician', 'img': 'blog_genuine', 'svc': 'ac_repair', 'link': '/ac-repair-narasaraopet/', 'date': D, 'local': True,
 'seo': 'How to Identify a Genuine AC Repair Technician – Red Flags | BOBBY',
 'desc': 'How to spot a genuine AC repair technician and avoid scams: verification checks, written estimates, old-part proof, gas-filling red flags and how to complain.',
 'title': ('How to Identify a Genuine AC Repair Technician (and Avoid Scams)',
           'నిజమైన ఏసీ రిపేర్ టెక్నీషియన్‌ను ఎలా గుర్తించాలి (మోసాలు నివారించడం)',
           'असली एसी रिपेयर टेक्नीशियन को कैसे पहचानें (और धोखे से बचें)'),
 'excerpt': ('Fake "authorised" callers, unnecessary gas refills and swapped parts are common. Here are the checks and red flags every customer should know.',
             'నకిలీ "అధీకృత" కాల్స్, అవసరం లేని గ్యాస్ ఫిల్లింగ్, మార్చిన విడిభాగాలు సాధారణం. ప్రతి కస్టమర్ తెలుసుకోవాల్సిన తనిఖీలు, హెచ్చరిక సంకేతాలు ఇవి.',
             'नकली "अधिकृत" कॉल, बेवजह गैस भरना और पार्ट्स बदल देना आम है। हर ग्राहक को ये जांच और चेतावनी संकेत जानने चाहिए।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> a genuine AC technician has a verifiable business (real phone number, address and reviews), inspects before quoting, explains the fault, gives you a clear estimate before work, shows you old parts, and gives a bill. Be careful with anyone who demands advance payment, says your AC "needs gas every year", refuses to show old parts, or claims to be "authorised" without proof.</p>'
'<h2>Why this matters</h2>'
'<p>Search "AC repair near me" and you will find many numbers. Some are excellent local technicians; others are call-centre listings that pretend to be a brand\'s service centre, quote low on the phone and inflate the bill at your door. The checks below protect you either way.</p>'
'<h2>Green flags: signs of a genuine technician</h2>'
'<ul><li><b>Verifiable identity:</b> a real business name, local address and a phone number that matches their Google Maps listing and reviews.</li><li><b>Honest about status:</b> independent technicians say they are independent; brand service centres can be verified on the brand\'s official website.</li><li><b>Inspection first:</b> they check filters, coils, pressure and electricals before deciding what is wrong.</li><li><b>Clear estimate before work:</b> labour and parts explained, and work starts only after you agree.</li><li><b>Shows the problem:</b> the dirty coil, the bulging capacitor, the oily leak point.</li><li><b>Old parts returned:</b> you can see what was replaced.</li><li><b>Bill or written note</b> of the work done and charges.</li></ul>'
+ fig('/assets/img/art/about-photo-sm.webp', 'BOBBY AC technician in uniform', 'A real technician with a local address, phone number and reviews is easy to verify.') +
'<h2>Red flags: common AC repair scams</h2>'
'<table><thead><tr><th>Red flag</th><th>Why it is a problem</th></tr></thead><tbody>'
'<tr><td>"Your AC needs gas every year"</td><td>Gas does not get used up; repeated filling means an unrepaired leak</td></tr>'
'<tr><td>Gas filled without a leak check</td><td>The new gas will leak out again</td></tr>'
'<tr><td>Advance payment demanded online</td><td>Common in fake service-centre listings</td></tr>'
'<tr><td>"Compressor gone" without testing</td><td>Expensive diagnosis without proof</td></tr>'
'<tr><td>Refuses to show or return old parts</td><td>Parts may not have been replaced</td></tr>'
'<tr><td>Claims "authorised" but the brand site does not list them</td><td>Misleading identity</td></tr>'
'<tr><td>Price changes heavily after the job</td><td>No clear estimate was given</td></tr>'
'</tbody></table>'
'<p>Compare part prices with an independent reference such as our <a href="/ac-spare-parts/">AC spare parts price list</a> before agreeing to a costly replacement.</p>'
'<h2>Questions to ask on the phone</h2>'
'<ol><li>Where are you based, and do you cover my area?</li><li>Is there a visit or inspection charge?</li><li>Will you give me an estimate before starting work?</li><li>Do you give a bill and return old parts?</li><li>Are you independent or a brand service centre?</li></ol>'
'<h2>If something goes wrong</h2>'
'<p>Keep the bill, photos and messages. You can register a complaint with India\'s National Consumer Helpline by calling 1915 or 1800-11-4000, or online at consumerhelpline.gov.in.</p>'
'<h2>How BOBBY works</h2>'
'<p>BOBBY is an independent multi-brand AC and appliance service in Narasaraopet, run by Yalamanda Gogasani ("Bobby"), at Arundelpet, Narasaraopet. We inspect first, explain the fault, give an estimate before work, and you approve before anything is done. ' + EST('ac_repair', 'See typical prices in our estimator') + ' or call ' + TEL + '.</p>'
 ),
 'faq': [('How do I know if an AC technician is genuine?', 'Check for a real business name, local address and a phone number matching Google reviews; ask for an estimate before work, old parts and a bill.'),
         ('Is it a scam if my AC needs gas every year?', 'It usually means a leak has not been repaired. A genuine technician finds and fixes the leak before refilling.'),
         ('Should I pay in advance for AC repair?', 'Be cautious. Genuine local technicians typically inspect first and are paid after the work you approved.'),
         ('Where can I complain about a bad repair service?', "India's National Consumer Helpline: call 1915 or 1800-11-4000, or register at consumerhelpline.gov.in.")],
 'sources': [('National Consumer Helpline (Govt. of India) – register a complaint', 'https://consumerhelpline.gov.in/'),
             ('Department of Consumer Affairs – helpline numbers', 'https://consumeraffairs.nic.in'),
             ('BOBBY – AC technician near me: how to choose', '/blog/ac-technician-near-me/'),
             ('BOBBY – AC spare parts price list', '/ac-spare-parts/')],
},
# ------------------------------------------------------------------ 10. Local complete guide
{
 'slug': 'home-appliance-repair-services-narasaraopet-guide', 'img': 'blog_local', 'svc': 'ac_repair', 'link': '/appliance-services/', 'date': D, 'local': True,
 'seo': 'Home Appliance Repair Services in Narasaraopet – Complete Guide | BOBBY',
 'desc': 'Complete guide to home appliance repair in Narasaraopet: AC, refrigerator, washing machine, air cooler, ceiling fan and electrical repairs, typical charges, areas covered and booking.',
 'title': ('Home Appliance Repair Services in Narasaraopet – Complete Guide',
           'నరసరావుపేటలో గృహోపకరణాల రిపేర్ సేవలు – పూర్తి గైడ్',
           'नरसरावपेट में घरेलू उपकरण रिपेयर सेवाएं – पूरी गाइड'),
 'excerpt': ('Everything Narasaraopet households need to know about getting ACs, fridges, washing machines, coolers and fans repaired at home: services, typical charges, areas and booking.',
             'నరసరావుపేట కుటుంబాలు ఏసీలు, ఫ్రిజ్‌లు, వాషింగ్ మెషిన్లు, కూలర్లు, ఫ్యాన్లను ఇంటి వద్దే రిపేర్ చేయించుకోవడానికి తెలుసుకోవాల్సినవి: సేవలు, సాధారణ ఛార్జీలు, ప్రాంతాలు, బుకింగ్.',
             'नरसरावपेट के परिवारों के लिए एसी, फ्रिज, वॉशिंग मशीन, कूलर और पंखे घर पर रिपेयर कराने की पूरी जानकारी: सेवाएं, सामान्य शुल्क, इलाके और बुकिंग।'),
 'body': (
'<p class="lead-q"><b>Quick answer:</b> BOBBY AC Repair &amp; Home Appliance Services provides doorstep repair for ACs, refrigerators, washing machines, air coolers, ceiling fans and basic home electrical work in Narasaraopet and nearby villages within about 20 km. The technician inspects first and gives an estimate before work. Book by calling or WhatsApp ' + TEL + '.</p>'
'<h2>Services available at your doorstep</h2>'
'<table><thead><tr><th>Appliance</th><th>Common work</th><th>Service page</th></tr></thead><tbody>'
'<tr><td>Air conditioner</td><td>Repair, servicing, deep cleaning, gas filling, PCB repair, installation &amp; shifting</td><td><a href="/ac-services/">AC services</a></td></tr>'
'<tr><td>Refrigerator</td><td>Not cooling, ice build-up, leaks, noise, compressor checks</td><td><a href="/refrigerator-repair-narasaraopet/">Refrigerator repair</a></td></tr>'
'<tr><td>Washing machine</td><td>Not spinning, not draining, leaks, error codes</td><td><a href="/washing-machine-repair-narasaraopet/">Washing machine repair</a></td></tr>'
'<tr><td>Air cooler</td><td>Pump, motor, pads, water flow</td><td><a href="/air-cooler-repair-narasaraopet/">Air cooler repair</a></td></tr>'
'<tr><td>Ceiling fan</td><td>Slow speed, noise, wobble, not running</td><td><a href="/ceiling-fan-repair-narasaraopet/">Ceiling fan repair</a></td></tr>'
'<tr><td>Home electrical</td><td>Switches, sockets, fan/light fitting, MCB and wiring faults</td><td>Call to book</td></tr>'
'</tbody></table>'
'<h2>Typical charges (estimate ranges)</h2>'
'<table><thead><tr><th>Service</th><th>Typical range</th></tr></thead><tbody>'
'<tr><td>AC general servicing</td><td>₹500 – ₹700 per AC</td></tr>'
'<tr><td>AC deep cleaning</td><td>₹900 – ₹1,500 per AC</td></tr>'
'<tr><td>AC repair inspection / visit</td><td>₹300 – ₹500 + parts</td></tr>'
'<tr><td>AC gas filling (with leak check)</td><td>₹2,000 – ₹3,500</td></tr>'
'<tr><td>Split AC installation</td><td>₹1,500 – ₹2,500</td></tr>'
'<tr><td>Refrigerator / washing machine visit</td><td>₹300 – ₹500 + parts</td></tr>'
'<tr><td>Air cooler repair / service</td><td>₹250 – ₹400</td></tr>'
'<tr><td>Ceiling fan repair</td><td>₹200 – ₹350</td></tr>'
'</tbody></table>'
'<p>These are estimates, not final prices. The final price depends on inspection, spare parts and the work needed, and work starts only after you approve. Build your own estimate and download it as a PDF with our ' + EST('', 'Get Estimate tool') + '.</p>'
+ fig('/assets/img/art/ac_repair-sm.webp', 'BOBBY technician inspecting an AC outdoor unit', 'Inspection first, estimate before work: the same process for every appliance.') +
'<h2>Areas covered</h2>'
'<p>Narasaraopet town, including Arundelpet, Prakash Nagar, Ramireddipet, Navodaya Nagar, Barampet, Guntur Road, Islampet, Sattenapalli Road, Vinukonda Road and Palnadu Road, plus Rompicherla and other villages within about 20 km. Not sure about your area? Call or WhatsApp to confirm.</p>'
'<h2>How booking works</h2>'
'<ol><li>Call or WhatsApp ' + TEL + ', or use the <a href="/contact/#book">booking form</a>.</li><li>Share the appliance, brand, problem and your area.</li><li>We confirm a visit time.</li><li>The technician inspects and gives an estimate.</li><li>You approve; the work is done and tested.</li></ol>'
'<h2>Brands we service</h2>'
'<p>As an independent multi-brand service, BOBBY works on popular brands including LG, Samsung, Daikin, Voltas, Blue Star, Panasonic, Hitachi, Carrier, Godrej and Haier. BOBBY is not an authorised service centre of these brands; see <a href="/brands/">brands we service</a>.</p>'
'<h2>Helpful guides</h2>'
'<ul><li><a href="/blog/why-does-ac-stop-cooling-in-summer/">Why does an AC stop cooling in summer?</a></li><li><a href="/blog/refrigerator-not-cooling-causes-solutions/">Refrigerator not cooling: causes and solutions</a></li><li><a href="/blog/washing-machine-not-spinning-causes-repair/">Washing machine not spinning</a></li><li><a href="/blog/how-to-identify-genuine-ac-repair-technician/">How to identify a genuine AC repair technician</a></li></ul>'
 ),
 'faq': [('Who provides home appliance repair in Narasaraopet?', 'BOBBY AC Repair & Home Appliance Services offers doorstep repair for ACs, refrigerators, washing machines, air coolers, ceiling fans and basic electrical work in Narasaraopet and nearby areas within about 20 km.'),
         ('Do you come to my home?', 'Yes. It is a doorstep service; most repairs are done at your home after inspection and your approval.'),
         ('How can I get a price before booking?', 'Use the Get Estimate tool on the website for typical ranges and a PDF, then call or WhatsApp to confirm. The final price is given after inspection.'),
         ('Which areas do you cover?', 'Narasaraopet town and nearby villages within about 20 km, including Arundelpet, Prakash Nagar, Ramireddipet, Navodaya Nagar, Barampet, Guntur Road, Islampet, Sattenapalli Road, Vinukonda Road, Palnadu Road and Rompicherla.')],
 'sources': [('BOBBY – AC services in Narasaraopet', '/ac-services/'),
             ('BOBBY – Appliance services', '/appliance-services/'),
             ('BOBBY – Contact & booking', '/contact/'),
             ('National Consumer Helpline (Govt. of India)', 'https://consumerhelpline.gov.in/')],
},
]

# ---- extra depth: inserted before each article's final section ----
EXTRA = {
'why-does-ac-stop-cooling-in-summer': (
'<h2>Inverter vs non-inverter ACs in extreme heat</h2>'
'<p>Inverter ACs slow the compressor down instead of switching it on and off, so they usually handle long hot days more smoothly and use less power. But they depend on sensors and an electronic board, and in very high heat or voltage swings they may reduce output to protect themselves. Non-inverter ACs run the compressor at full speed and are more sensitive to low voltage and a weak capacitor. Either way, a clean outdoor unit is the single biggest factor in summer performance.</p>'),
'ac-gas-filling-cost-r32-vs-r410a': (
'<h2>Signs your AC really needs gas</h2>'
'<ul><li>Cooling has dropped gradually over weeks, not suddenly.</li><li>Ice or frost on the thinner copper pipe or the indoor coil.</li><li>The outdoor unit runs, but the large pipe is not cold to touch.</li><li>Oily marks at pipe joints or valves (refrigerant carries oil).</li><li>A hissing sound near the joints.</li></ul>'
'<p>If cooling stopped suddenly, or the outdoor fan is not running, the problem is more likely electrical (capacitor, contactor, PCB) than gas.</p>'
'<h2>Gas filling in inverter ACs</h2>'
'<p>Most inverter ACs in India use R32. The process is the same (leak check, repair, vacuum, charge by weight to the nameplate figure), but inverter systems are sensitive to overcharging, so "adding a little extra" is a mistake. A correct charge matters for efficiency and compressor life.</p>'
'<h2>How to avoid overpaying</h2>'
'<ul><li>Ask for the pressure reading before and after.</li><li>Ask where the leak was and how it was fixed.</li><li>Confirm the gas type matches the outdoor unit sticker.</li><li>Get the price confirmed before the work starts.</li></ul>'),
'refrigerator-not-cooling-causes-solutions': (
'<h2>Direct cool vs frost-free: different problems</h2>'
'<p><b>Direct cool</b> (usually single door) fridges cool by natural convection and need manual defrosting. Thick ice on the freezer plate blocks cooling, so defrost when ice is more than about half a centimetre thick. <b>Frost-free</b> fridges use a fan and an automatic defrost heater; when the defrost system or fan fails, the freezer may stay cold while the lower fridge section warms up.</p>'
'<h2>Power cuts and voltage</h2>'
'<p>Frequent power cuts and low voltage are hard on fridge compressors. After a power cut, give the fridge a few minutes before switching on repeatedly, and use a suitable stabiliser if your area sees big voltage swings. Keep the door closed during outages: a full freezer stays cold much longer than a half-empty one.</p>'
'<h2>Repair or replace?</h2>'
'<p>Most cooling problems (thermostat, relay, fan, door seal, defrost parts) are worth repairing. A compressor or major gas-leak repair on a very old fridge is where it makes sense to compare the repair cost with a new, more efficient model. Look at the BEE star label on a new fridge to compare annual power use.</p>'),
'washing-machine-not-spinning-causes-repair': (
'<h2>Top load, front load and semi-automatic: where spin problems come from</h2>'
'<table><thead><tr><th>Type</th><th>Most common spin issues</th></tr></thead><tbody>'
'<tr><td>Semi-automatic</td><td>Spin lid switch, spin motor capacitor, brake or belt in the spin tub</td></tr>'
'<tr><td>Top load (fully automatic)</td><td>Unbalanced load, drain pump, lid lock, belt or clutch/gearbox</td></tr>'
'<tr><td>Front load</td><td>Debris filter blockage, door lock, unbalance sensor, motor or board</td></tr>'
'</tbody></table>'
'<h2>How to prevent spin problems</h2>'
'<ul><li>Do not overload, and do not wash a single heavy item alone.</li><li>Clean the front loader debris filter every month or two.</li><li>Empty pockets: coins and hairpins are the top cause of drain pump damage.</li><li>Use the right amount of detergent; too much foam can stop the spin.</li><li>Keep the machine level and on a firm floor.</li></ul>'),
'best-time-to-service-ac-in-andhra-pradesh': (
'<h2>Signs you should not wait for the "right" month</h2>'
'<ul><li>Water dripping from the indoor unit.</li><li>Burning smell, sparks or the MCB tripping (switch off immediately).</li><li>Ice on pipes or sudden loss of cooling.</li><li>Loud rattling or grinding from either unit.</li></ul>'
'<p>These need a repair visit straight away, whatever the season.</p>'
'<h2>What you can do between services</h2>'
'<ul><li>Wash the filters (switch off first, dry fully before refitting).</li><li>Keep 1–2 feet of open space in front of the outdoor unit.</li><li>Wipe the indoor unit body and vanes with a dry cloth.</li><li>Use 24–26°C with a ceiling fan; it is gentler on the AC and your bill.</li></ul>'
'<h2>Shops, clinics and offices</h2>'
'<p>ACs that run 10–14 hours a day in commercial spaces collect dust much faster. For these, a service every three to four months, plus monthly filter cleaning, keeps cooling and power use under control.</p>'),
'ac-installation-checklist-indian-homes': (
'<h2>Window AC installation tips</h2>'
'<ul><li>Fit it slightly tilted outward (as per the manual) so water drains outside.</li><li>Seal gaps around the frame to keep out hot air, dust and rain.</li><li>Leave the rear and sides open outside the wall so the condenser can breathe.</li><li>Use a strong frame or stand; never rest the weight on loose bricks.</li></ul>'
'<h2>Common installation mistakes to avoid</h2>'
'<table><thead><tr><th>Mistake</th><th>Result</th></tr></thead><tbody>'
'<tr><td>Skipping vacuuming</td><td>Moisture in the system, weaker cooling, compressor stress</td></tr>'
'<tr><td>Drain pipe with a loop or upward bend</td><td>Water dripping indoors</td></tr>'
'<tr><td>Outdoor unit facing a wall closely</td><td>Hot air recirculates, poor cooling in summer</td></tr>'
'<tr><td>Loose flare joints</td><td>Gas leaks within weeks or months</td></tr>'
'<tr><td>Shared or undersized socket</td><td>Overheated wiring, trips</td></tr>'
'</tbody></table>'
'<h2>Shifting an AC to a new house</h2>'
'<p>When moving, the gas should be pumped down into the outdoor unit before uninstalling, the pipes capped, and the system vacuumed and leak-tested again at the new home. Rough uninstallation is a common cause of gas loss.</p>'),
'how-to-identify-genuine-ac-repair-technician': (
'<h2>What a fair inspection looks like</h2>'
'<ol><li>The technician asks about the problem and when it started.</li><li>Checks settings, filters, indoor and outdoor units.</li><li>Measures pressure and electrical values when relevant.</li><li>Explains the cause in simple language and shows you.</li><li>Gives options (repair now, monitor, or replace) with prices.</li></ol>'
'<h2>Brand warranty and independent technicians</h2>'
'<p>If your AC is still under the manufacturer\'s warranty, contact the brand\'s official service channel first so the warranty is not affected. For ACs out of warranty, a good independent local technician is often quicker and more affordable. A genuine one will tell you this honestly rather than pretend to be "authorised".</p>'),
'home-appliance-repair-services-narasaraopet-guide': (
'<h2>Why choose a local technician</h2>'
'<ul><li><b>Faster visits:</b> no long call-centre chain; you talk directly to the person who comes.</li><li><b>Knows local conditions:</b> summer heat, dust and voltage swings in Palnadu district.</li><li><b>Accountable:</b> a real address in town and a reputation to keep.</li><li><b>Follow-up:</b> easy to call back if something needs another look.</li></ul>'
'<h2>Getting ready for the technician visit</h2>'
'<ul><li>Note the brand, model and any error code shown.</li><li>Clear space around the appliance and the outdoor unit.</li><li>Keep the warranty card or old bills handy.</li><li>Describe when the problem happens (all the time, only in the afternoon, only on spin).</li></ul>'
'<h2>Seasonal checklist for Narasaraopet homes</h2>'
'<table><thead><tr><th>Season</th><th>What to do</th></tr></thead><tbody>'
'<tr><td>Feb – Mar</td><td>AC service and cooler check before summer</td></tr>'
'<tr><td>Apr – Jun</td><td>Wash AC filters every 2 weeks; clean fridge coils</td></tr>'
'<tr><td>Jul – Sep</td><td>Watch for AC drain leaks and washing machine drain issues</td></tr>'
'<tr><td>Oct – Nov</td><td>Post-monsoon AC check; service ceiling fans</td></tr>'
'</tbody></table>'),
}
DESC_FIX = {
'why-does-ac-stop-cooling-in-summer': 'Why ACs lose cooling at 40–45°C: dirty condensers, weak capacitors, low gas, low voltage and undersized ACs, plus safe checks and when to call a technician.',
'refrigerator-not-cooling-causes-solutions': 'Refrigerator not cooling? Check settings, door seals, condenser coils, airflow and the compressor. Safe fixes and when to call a technician.',
'ac-installation-checklist-indian-homes': 'A 15-point AC installation checklist for Indian homes: placement, power, copper pipe, drain slope, outdoor stand, vacuum test and handover.',
'home-appliance-repair-services-narasaraopet-guide': 'Doorstep repair in Narasaraopet for ACs, fridges, washing machines, coolers, fans and electrical work: typical charges, areas and booking.',
}
for _p in NEW_POSTS2:
    _x = EXTRA.get(_p['slug'])
    if _x:
        _i = _p['body'].rfind('<h2>')
        _p['body'] = _p['body'][:_i] + _x + _p['body'][_i:]
    if _p['slug'] in DESC_FIX: _p['desc'] = DESC_FIX[_p['slug']]
