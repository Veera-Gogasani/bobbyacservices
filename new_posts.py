# -*- coding: utf-8 -*-
"""Five SEO articles (Nov 2026). English body; Telugu/Hindi title + excerpt.
Each post: seo (title tag), desc (meta description), faq (Q/A -> on-page FAQ + FAQPage schema),
sources (outbound references), local (adds the Narasaraopet contact box)."""

def fig(src, alt, cap, w=800, h=500):
    return (f'<figure class="post-fig"><img src="{src}" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">'
            f'<figcaption>{cap}</figcaption></figure>')

TEL = '<a href="tel:+918374889163">+91 83748 89163</a>'

NEW_POSTS = [
# ------------------------------------------------------------------ 1. AC repair in Narasaraopet (local)
{
 'slug': 'ac-repair-in-narasaraopet', 'img': 'blog_repair', 'svc': 'ac_repair', 'link': '/ac-services/#ac-repair',
 'date': '2026-11-20', 'local': True,
 'seo': 'AC Repair in Narasaraopet – Common Problems & Fixes | BOBBY',
 'desc': 'AC repair in Narasaraopet: AC not cooling, water leakage, noise, tripping and gas leaks explained, plus how to book a doorstep AC technician.',
 'title': ("AC Repair in Narasaraopet: Common AC Problems, Repair Solutions & Doorstep Service",
           "నరసరావుపేటలో ఏసీ రిపేర్: సాధారణ ఏసీ సమస్యలు, పరిష్కారాలు & ఇంటి వద్దకే సర్వీస్",
           "नरसरावपेट में एसी रिपेयर: आम एसी समस्याएँ, समाधान और घर पर सर्विस"),
 'excerpt': ("The AC problems we see most in Narasaraopet homes, what usually causes them, what a proper repair involves, and how to get a technician at your doorstep.",
             "నరసరావుపేట ఇళ్లలో ఎక్కువగా కనిపించే ఏసీ సమస్యలు, వాటి కారణాలు, సరైన రిపేర్‌లో ఏముంటుంది, ఇంటి వద్దకే టెక్నీషియన్‌ను ఎలా బుక్ చేయాలి.",
             "नरसरावपेट के घरों में सबसे आम एसी समस्याएँ, उनके कारण, सही रिपेयर में क्या होता है, और घर पर टेक्नीशियन कैसे बुलाएँ।"),
 'body': """<p class="lead-q"><b>Quick answer:</b> most AC breakdowns in Narasaraopet come down to six problems: weak cooling, water leakage, unusual noise, the AC not switching on, frequent tripping, and refrigerant (gas) leaks. Many start small and get expensive when ignored. A good technician inspects first, explains the fault, gives you an estimate, and only then repairs.</p>
<p>Narasaraopet summers regularly push past 40°C, and ACs here run long hours in dusty conditions. That is harder on an air conditioner than the "average" use manufacturers design for, which is why the same handful of faults keep coming up. This guide walks through each one, what normally causes it, what you can safely check yourself, and what a proper repair looks like.</p>
<h2>1. AC running but not cooling</h2>
<p>This is the most common complaint we get. Usual causes, from simplest to most serious:</p>
<ul><li><b>Clogged filters</b> blocking airflow (the cheapest fix of all).</li><li><b>Wrong mode or setting</b>: Fan or Dry mode instead of Cool, or a timer/eco mode limiting output.</li><li><b>Dirty indoor coil or outdoor condenser</b>: the AC cannot move heat out of the room.</li><li><b>Low refrigerant caused by a leak</b>: weak cooling, sometimes ice on the copper pipes.</li><li><b>Electrical faults</b>: a weak capacitor, failed sensor, or PCB problem stopping the compressor.</li></ul>
<p>Our detailed guide <a href="/blog/why-is-my-ac-not-cooling/">Why is my AC not cooling properly?</a> covers the safe checks you can do before calling anyone.</p>
""" + fig('/assets/img/parts/cap_dual.webp', 'AC dual run capacitor, a common cause of the compressor not starting', 'A weak run capacitor is one of the most common reasons an outdoor unit hums but the compressor does not start.', 480, 480) + """
<h2>2. Water leaking from the indoor unit</h2>
<p>Water dripping inside the room almost always means the condensate cannot drain away: a blocked drain pipe, a dirty drain tray, a kinked or badly sloped pipe, or an indoor unit that is not mounted level. Leaving it is risky because water can reach wiring and damage walls. Read more in <a href="/blog/why-is-your-ac-leaking-water/">Why is your AC leaking water?</a></p>
<h2>3. Unusual noise or vibration</h2>
<ul><li><b>Rattling</b>: loose panels, mounting bolts or debris in the outdoor fan.</li><li><b>Squealing or grinding</b>: worn fan-motor bearings.</li><li><b>Clicking that repeats</b>: relay or electrical issues.</li><li><b>Hissing or bubbling</b>: possible refrigerant leak.</li></ul>
<p>Noise is worth checking early: a worn motor caught in time is a small repair; a seized one can take other parts with it.</p>
<h2>4. AC not switching on</h2>
<p>Check the obvious first: remote batteries, the wall switch, the MCB, and whether the stabiliser (if you have one) is showing a fault. If power is reaching the unit but nothing happens, the cause is usually a blown fuse, a failed PCB, a faulty sensor or a wiring fault. Please do not open the electrical panel yourself.</p>
<h2>5. AC tripping the MCB or switching off by itself</h2>
<p>Repeated tripping points to an electrical problem: a shorted compressor or fan motor, a damaged capacitor, loose terminals, or wiring that is too thin for the AC's load. A unit that cuts out after a few minutes may also be overheating because the outdoor unit is dirty or boxed in with no airflow.</p>
<h2>6. Refrigerant (gas) leak</h2>
<p>Refrigerant does not get "used up". If the gas is low, there is a leak somewhere, usually at flare joints, brazed joints, or a corroded coil. Topping up without finding the leak means paying again a few weeks later. A proper job is: find the leak, repair it, pressure-test, vacuum the system, then charge the correct amount. See <a href="/blog/ac-gas-filling-when-is-it-required/">AC gas filling: when is it actually required?</a></p>
<h2>Repair or replace? A quick guide</h2>
<div class="table-wrap"><table><thead><tr><th>Situation</th><th>Usually worth it</th></tr></thead><tbody>
<tr><td>Filters, drain, capacitor, sensor, fan motor</td><td>Repair: low-cost parts, big improvement</td></tr>
<tr><td>Gas leak at a joint</td><td>Repair the leak, then refill</td></tr>
<tr><td>PCB fault on a fairly new AC</td><td>Repair or replace the board</td></tr>
<tr><td>Compressor failure on a 10+ year old fixed-speed AC</td><td>Compare the repair estimate with a new energy-efficient AC</td></tr>
</tbody></table></div>
<h2>What a proper AC repair visit should include</h2>
<ol><li><b>Inspection first</b>: checking the indoor and outdoor units, electrical readings and cooling performance.</li><li><b>A clear explanation</b> of the fault in simple language.</li><li><b>An estimate before work starts</b>, with your approval needed for any parts.</li><li><b>The repair</b> using suitable tools and parts.</li><li><b>Testing</b> the AC after the repair and telling you about anything else that needs attention.</li></ol>
<p>That is exactly how we work at BOBBY. You can read our <a href="/about/">trust principles</a>, see all <a href="/ac-services/">AC services</a>, or check the <a href="/ac-spare-parts/">AC spare parts price guide</a> to get a feel for part costs before you book.</p>
<h2>Areas we cover around Narasaraopet</h2>
<p>We provide doorstep AC repair in Narasaraopet town and nearby areas within roughly 20 km, including Arundelpet and surrounding colonies. Service availability depends on location and scheduling, so share your area when you book and we will confirm the visit time.</p>""",
 'faq': [
  ("How quickly can I get an AC technician in Narasaraopet?", "Call or WhatsApp +91 83748 89163 with your area and the problem. We confirm a visit time based on location and that day's schedule; urgent breakdowns are prioritised where possible."),
  ("Do you charge for inspection?", "Any applicable visit or inspection charge is told to you before the technician comes. Repair charges are explained and approved by you before any work starts."),
  ("Which AC brands do you repair?", "We are an independent multi-brand service and work on split and window ACs from major brands such as LG, Daikin, Voltas, Samsung, Blue Star, Panasonic, Hitachi, Carrier, Godrej and Haier."),
  ("My AC needs gas. Can you just fill it?", "Low gas means a leak. We check for the leak first, repair it, and then charge the correct amount, otherwise the gas escapes again and you pay twice."),
  ("Is it safe to keep using an AC that is leaking water?", "It is best to switch it off and get it checked. Water can reach wiring and damage walls, and the cause is usually a simple drain blockage."),
 ],
 'sources': [("BOBBY guide: Why is my AC not cooling?", "/blog/why-is-my-ac-not-cooling/"), ("BOBBY guide: AC gas filling", "/blog/ac-gas-filling-when-is-it-required/"), ("BOBBY: AC spare parts price guide", "/ac-spare-parts/")],
},
# ------------------------------------------------------------------ 2. Reduce AC electricity bill
{
 'slug': 'how-to-reduce-ac-electricity-bill', 'img': 'blog_power', 'svc': 'ac_servicing', 'link': '/ac-services/#ac-servicing',
 'date': '2026-11-20',
 'seo': 'How to Reduce AC Electricity Bill: 12 Tips for India | BOBBY',
 'desc': '12 practical ways to reduce your AC electricity bill in India: the BEE-recommended 24°C setting, filter cleaning, inverter use, tonnage and star ratings.',
 'title': ("How to Reduce Your AC Electricity Bill in India: 12 Practical Power-Saving Tips",
           "భారతదేశంలో ఏసీ కరెంట్ బిల్లు తగ్గించడం ఎలా: 12 ఆచరణాత్మక విద్యుత్ పొదుపు చిట్కాలు",
           "भारत में एसी का बिजली बिल कैसे कम करें: बिजली बचाने के 12 व्यावहारिक टिप्स"),
 'excerpt': ("Simple, proven ways to cut AC power use in Indian homes, from the BEE-recommended 24°C setting to filter cleaning and choosing the right tonnage.",
             "భారతీయ ఇళ్లలో ఏసీ కరెంట్ వినియోగం తగ్గించే సులభమైన మార్గాలు: BEE సిఫార్సు చేసిన 24°C సెట్టింగ్ నుంచి ఫిల్టర్ క్లీనింగ్, సరైన టన్నేజ్ వరకు.",
             "भारतीय घरों में एसी की बिजली खपत घटाने के आसान तरीके: BEE के सुझाए 24°C सेटिंग से लेकर फ़िल्टर सफ़ाई और सही टन क्षमता तक।"),
 'body': """<p class="lead-q"><b>Quick answer:</b> the single biggest saving is the temperature setting. India's Bureau of Energy Efficiency (BEE) estimates that raising the AC setting by 1°C saves about 6% electricity, and moving from 20°C to 24°C saves about 24%. After that, clean filters, a well-ventilated outdoor unit, inverter operation and regular servicing make the biggest difference.</p>
<p>In most Indian homes the air conditioner is the largest single electricity load in summer. The good news is that you do not need to suffer the heat to cut the bill. These 12 tips are ordered roughly by how much they save for how little effort.</p>
<h2>1. Set the temperature to 24°C (or higher)</h2>
<p>BEE recommends 24°C as the default setting, and since 2020 star-labelled room ACs sold in India ship with a 24°C default. Each degree lower adds roughly 6% to consumption. Setting 18°C does not cool the room faster; it only keeps the compressor running longer.</p>
<h2>2. Use the fan with the AC</h2>
<p>A ceiling fan on low speed spreads cool air and makes 25–26°C feel like 23–24°C, so you can keep the thermostat higher.</p>
<h2>3. Clean the filters every 2–3 weeks in summer</h2>
<p>Dusty filters reduce airflow, make the compressor run longer and cut cooling. Slide them out, rinse with plain water, dry fully and refit. It takes five minutes and costs nothing.</p>
""" + fig('/assets/img/parts/filter.webp', 'Split AC air filter that should be cleaned every two to three weeks in summer', 'A clean filter is the cheapest efficiency upgrade your AC will ever get.', 480, 480) + """
<h2>4. Keep the outdoor unit shaded and breathing</h2>
<p>The outdoor unit throws heat out. Direct afternoon sun, dust on the condenser fins, or walls and grills boxing it in force it to work harder. Keep at least a foot of open space around it and keep plants, boxes and clothes away from it.</p>
<h2>5. Service the AC before summer</h2>
<p>A full service (coil cleaning, drain check, outdoor unit cleaning, electrical checks) restores cooling efficiency that slowly drops with dust build-up. See <a href="/blog/when-should-you-service-your-ac/">when to service your AC</a>.</p>
<h2>6. Seal the room</h2>
<p>Close doors and windows, use curtains or blinds on sun-facing windows, and block gaps under doors. Every bit of hot air that leaks in must be cooled again.</p>
<h2>7. Use sleep mode and timers</h2>
<p>Sleep mode gradually raises the set temperature at night as your body cools. A timer that switches the AC off in the early morning, when it is cooler outside, can save several hours of running a night.</p>
<h2>8. Let an inverter AC run steadily</h2>
<p>Inverter ACs save power by slowing the compressor down once the room is cool. Switching them on and off repeatedly wastes that advantage. Set a sensible temperature and let it run.</p>
<h2>9. Choose the right tonnage</h2>
<div class="table-wrap"><table><thead><tr><th>Room size (approx.)</th><th>Typical AC size</th></tr></thead><tbody>
<tr><td>Up to 120 sq ft</td><td>0.8–1 ton</td></tr><tr><td>120–180 sq ft</td><td>1–1.5 ton</td></tr><tr><td>180–250 sq ft</td><td>1.5–2 ton</td></tr></tbody></table></div>
<p>Top-floor rooms, west-facing walls, large windows and kitchens need more capacity. An undersized AC runs flat out all day; an oversized one cycles inefficiently and does not remove humidity well.</p>
<h2>10. Read the BEE star label properly</h2>
<p>BEE tightened its star rating thresholds from 1 January 2026, so a model rated 5-star under the 2025 table is rated 4-star under the new one. Compare the <b>ISEER value</b> printed on the label (higher is better) and check the label's validity period, not just the star count.</p>
<h2>11. Avoid heat sources in the AC room</h2>
<p>Ovens, irons, old incandescent bulbs and lots of electronics all add heat. Switch them off or use them elsewhere while the AC is running.</p>
<h2>12. Fix gas leaks and electrical faults promptly</h2>
<p>An AC with low refrigerant or a weak capacitor runs much longer for the same cooling. If cooling drops or the bill jumps without a reason, book a check rather than lowering the temperature further.</p>
<h2>How much can you actually save?</h2>
<p>As a rough example using BEE's figure: if your AC uses 300 units a month at 20°C, running it at 24°C could save around 70 units a month. Try the <a href="/faqs/#ac-electricity-cost-calculator">AC electricity cost calculator</a> on our FAQs page to estimate your own running cost.</p>""",
 'faq': [
  ("What is the best AC temperature to save electricity?", "24°C is the BEE-recommended default. Each degree higher saves roughly 6%, so 25–26°C with a fan saves even more while staying comfortable."),
  ("Does an inverter AC really save electricity?", "Yes, when it is allowed to run steadily. It slows the compressor once the room is cool instead of switching fully on and off, which uses less power over a long day."),
  ("How much electricity does a 1.5 ton AC use per hour?", "It varies with star rating, outside temperature and settings, but a 1.5 ton inverter AC typically uses well under 1.5 units an hour once the room is cool. Check the annual kWh on the BEE label for your model."),
  ("Does cleaning the AC filter reduce the bill?", "Yes. Clogged filters reduce airflow so the AC runs longer for the same cooling. Cleaning them every 2–3 weeks in summer is the cheapest saving there is."),
  ("Did the AC star ratings change in 2026?", "Yes. BEE's revised star rating table came into force on 1 January 2026 with stricter ISEER thresholds, so compare the ISEER value and label year, not just the stars."),
 ],
 'sources': [("BEE: Raising AC setting by 1°C can save 6% power", "https://udit.beeindia.gov.in/bee-raising-ac-setting-by-1-can-save-6-power/"),
             ("Business Standard: BEE 2020 mandate of 24°C default for room ACs", "https://www.business-standard.com/india-news/india-standardise-air-conditioner-temperature-20-28-degree-celsius-125061001221_1.html"),
             ("Business Today: revised BEE star ratings from 1 January 2026", "https://www.businesstoday.in/india/story/5-star-acs-refrigerators-to-get-costlier-from-january-2026-heres-why-508978-2025-12-31")],
},
# ------------------------------------------------------------------ 3. Best AC brand in India
{
 'slug': 'best-ac-brand-in-india', 'img': 'blog_brands', 'svc': 'ac_install', 'link': '/ac-services/#ac-installation',
 'date': '2026-11-20',
 'seo': 'Best AC Brand in India 2026: LG vs Daikin vs Voltas | BOBBY',
 'desc': 'Which AC brand is best in India in 2026? LG, Daikin, Voltas, Samsung and Blue Star compared on efficiency, service network, spare parts and warranty.',
 'title': ("Which AC Brand Is Best in India in 2026? LG vs Daikin vs Voltas vs Samsung vs Blue Star & More",
           "2026లో భారతదేశంలో ఏ ఏసీ బ్రాండ్ ఉత్తమం? LG, Daikin, Voltas, Samsung, Blue Star పోలిక",
           "2026 में भारत में कौन सा एसी ब्रांड सबसे अच्छा है? LG, Daikin, Voltas, Samsung, Blue Star की तुलना"),
 'excerpt': ("A practical, technician's-eye comparison of the main AC brands in India, and the checklist that matters more than the logo: efficiency, service and spare parts.",
             "భారతదేశంలోని ప్రధాన ఏసీ బ్రాండ్‌లపై టెక్నీషియన్ దృష్టితో పోలిక, లోగో కంటే ముఖ్యమైన అంశాలు: సామర్థ్యం, సర్వీస్, విడిభాగాలు.",
             "भारत के मुख्य एसी ब्रांडों की टेक्नीशियन की नज़र से तुलना, और लोगो से ज़्यादा ज़रूरी बातें: एफ़िशिएंसी, सर्विस और स्पेयर पार्ट्स।"),
 'body': """<p class="lead-q"><b>Quick answer:</b> there is no single "best" AC brand for everyone. Voltas, LG, Daikin, Blue Star and Samsung are the brands most Indian buyers shortlist, and all of them make good inverter ACs. The better question is which model gives you a high ISEER rating, the right tonnage, a strong local service network and easy spare parts in your town.</p>
<p>This is BOBBY's editorial comparison, written from the point of view of technicians who install, service and repair all of these brands in Narasaraopet. It is not an official ranking and we are not paid by any brand.</p>
<h2>How we compared the brands</h2>
<ul><li><b>Energy efficiency</b>: ISEER values and star ratings under the revised BEE 2026 table.</li><li><b>Cooling performance in Indian heat</b>: how models cope with 40°C+ afternoons.</li><li><b>Service network</b>: how easy it is to get authorised service in smaller towns.</li><li><b>Spare-parts availability</b>: how quickly common parts (PCBs, motors, capacitors, sensors) can be sourced.</li><li><b>Warranty</b>: especially compressor warranty length.</li></ul>
<h2>The main AC brands in India at a glance</h2>
<div class="table-wrap"><table><thead><tr><th>Brand</th><th>Known for</th><th>Good fit for</th></tr></thead><tbody>
<tr><td><b>Voltas</b> (Tata group)</td><td>India's market leader by share, very wide range and dealer reach</td><td>Value buyers who want easy availability anywhere</td></tr>
<tr><td><b>LG</b></td><td>Widely owned, strong inverter line-up, smart features</td><td>Buyers wanting features and a big service network</td></tr>
<tr><td><b>Daikin</b></td><td>AC specialist, reputation for efficient inverter models</td><td>Long-hours users who value efficiency</td></tr>
<tr><td><b>Blue Star</b></td><td>Indian AC specialist since 1943, residential and commercial</td><td>Buyers who prefer a cooling specialist</td></tr>
<tr><td><b>Samsung</b></td><td>Fast-growing in room ACs, design and smart features</td><td>Smart-home and design-focused buyers</td></tr>
<tr><td><b>Panasonic / Hitachi / Carrier</b></td><td>Established global names with premium options</td><td>Buyers comfortable with slightly fewer local service points</td></tr>
<tr><td><b>Lloyd / Godrej / Haier</b></td><td>Competitive pricing</td><td>Budget-conscious buyers who check local service first</td></tr>
</tbody></table></div>
<p>Market-share figures vary by report and year; Reuters, for example, described Voltas as India's AC market leader with nearly an 18% share in 2025, and Samsung said it reached about 10% of room-AC sales in the March 2025 quarter. Treat these as context, not as proof of quality.</p>
<h2>LG vs Daikin vs Voltas: what actually differs?</h2>
<p>In everyday use, the differences between well-chosen models from these three brands are smaller than the differences between a 3-star and a 5-star model, or between a correctly and incorrectly sized AC. Where they differ in practice:</p>
<ul><li><b>Voltas</b>: easiest to find at every price point; good value in the 3-star inverter segment.</li><li><b>LG</b>: feature-rich (dual inverter, Wi-Fi models) with a large service footprint.</li><li><b>Daikin</b>: often chosen for efficiency and quiet operation in long-hours use.</li></ul>
<h2>What matters more than the brand</h2>
<ol><li><b>ISEER and star rating</b> under the 2026 BEE table: a higher ISEER means lower running cost. Our <a href="/blog/how-to-reduce-ac-electricity-bill/">AC electricity saving guide</a> explains why.</li><li><b>Inverter compressor</b> if you run the AC more than a few hours a day.</li><li><b>Correct tonnage</b> for your room size, floor and sun exposure.</li><li><b>Copper condenser coil</b> or good anti-corrosion coating if you live in a dusty or coastal area.</li><li><b>Compressor warranty</b>: check the years and what it covers.</li><li><b>Local service and spare parts</b>: ask your dealer who services the brand in your town.</li><li><b>Installation quality</b>: a poor installation (bad flaring, no vacuum, wrong pipe length) hurts any brand. See our <a href="/ac-services/#ac-installation">AC installation service</a>.</li></ol>
<h2>Split or window?</h2>
<p>If you are also deciding between the two types, read <a href="/blog/split-ac-vs-window-ac/">Split AC vs window AC: which is right for your home?</a></p>
<h2>Our honest recommendation</h2>
<p>Shortlist two or three models from different major brands in the right tonnage, compare their ISEER values, compressor warranty and price, and then pick the one with the best local service support. Whichever brand you choose, BOBBY can install it, service it and repair it. See the <a href="/brands/">brands we service</a>.</p>""",
 'faq': [
  ("Which AC brand is number one in India?", "By market share, Voltas has been reported as India's room-AC leader in recent years, with LG, Daikin, Blue Star and Samsung close behind. Market leadership does not automatically mean the best model for your room."),
  ("Is Daikin better than LG?", "Both make good inverter ACs. Daikin is often chosen for efficiency and quiet operation; LG for features and a large service network. Compare the specific models' ISEER, warranty and local service."),
  ("Which AC brand has the best after-sales service?", "It depends on your town. Ask the dealer which authorised service centre covers your area and how fast parts arrive. An independent multi-brand technician can also help after warranty."),
  ("Is a 5-star AC worth the extra cost?", "If you run the AC for many hours a day, usually yes: the higher ISEER pays back through lower bills. For occasional use, a 3-star inverter AC can be the better value."),
  ("Do 2025 and 2026 star ratings mean the same thing?", "No. BEE's thresholds were tightened from 1 January 2026, so a 2025 5-star model is roughly a 4-star model on the new table. Compare ISEER values directly."),
 ],
 'sources': [("Reuters via MarketScreener: Voltas, India's AC market leader", "https://www.marketscreener.com/news/india-s-top-ac-maker-bets-on-first-time-buyers-to-drive-summer-demand-rebound-ce7e5adbdc89ff24"),
             ("Outlook Business: Samsung's room-AC market share", "https://www.outlookbusiness.com/corporate/samsung-aims-for-10-market-share-in-room-air-conditioner-segment"),
             ("Digit: BEE ISEER thresholds revised from 1 January 2026", "https://www.digit.in/features/home-appliances/lgs-2026-ac-lineup-is-focused-towards-energy-efficiency-heres-how-it-will-save-your-money.html")],
},
# ------------------------------------------------------------------ 4. AC servicing in Narasaraopet (local)
{
 'slug': 'ac-servicing-in-narasaraopet', 'img': 'blog_service', 'svc': 'ac_servicing', 'link': '/ac-services/#ac-servicing',
 'date': '2026-11-20', 'local': True,
 'seo': 'AC Servicing in Narasaraopet: Service vs Deep Clean | BOBBY',
 'desc': 'AC servicing in Narasaraopet: general service vs deep cleaning, a full checklist, how often to service in Palnadu heat, and doorstep booking.',
 'title': ("AC Servicing in Narasaraopet: General Service vs Deep Cleaning, and What's Included",
           "నరసరావుపేటలో ఏసీ సర్వీసింగ్: జనరల్ సర్వీస్ vs డీప్ క్లీనింగ్, ఇందులో ఏముంటుంది",
           "नरसरावपेट में एसी सर्विसिंग: जनरल सर्विस बनाम डीप क्लीनिंग, और इसमें क्या शामिल है"),
 'excerpt': ("The difference between a general AC service and a deep cleaning, a full checklist of what each should include, and the right servicing schedule for Narasaraopet's heat and dust.",
             "జనరల్ ఏసీ సర్వీస్ మరియు డీప్ క్లీనింగ్ మధ్య తేడా, ప్రతి దానిలో ఉండాల్సిన పూర్తి చెక్‌లిస్ట్, నరసరావుపేట వేడి, దుమ్ముకు సరైన సర్వీసింగ్ షెడ్యూల్.",
             "जनरल एसी सर्विस और डीप क्लीनिंग में अंतर, हर एक की पूरी चेकलिस्ट, और नरसरावपेट की गर्मी व धूल के लिए सही सर्विसिंग शेड्यूल।"),
 'body': """<p class="lead-q"><b>Quick answer:</b> a <b>general service</b> cleans the filters, indoor unit surface and outdoor unit and checks the drain, electricals and cooling. A <b>deep cleaning</b> goes further: it jet-washes the indoor coil and blower with a cleaning bag to remove the dust, mould and grime that a general service cannot reach. In Narasaraopet, most homes need a full service before summer and a second one after heavy use.</p>
<p>"AC service" can mean anything from a quick filter wash to a full strip-down clean, which is why prices and results vary so much. This guide explains exactly what each type of service should include so you know what you are paying for.</p>
<h2>General service vs deep cleaning</h2>
<div class="table-wrap"><table><thead><tr><th></th><th>General service</th><th>Deep cleaning</th></tr></thead><tbody>
<tr><td>Filters washed</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Indoor coil</td><td>Surface clean</td><td>Jet-washed with coil cleaner</td></tr>
<tr><td>Blower wheel (fan inside)</td><td>Light clean</td><td>Washed to remove dust and mould</td></tr>
<tr><td>Drain tray and pipe</td><td>Checked and flushed</td><td>Cleaned thoroughly</td></tr>
<tr><td>Outdoor condenser</td><td>Cleaned</td><td>Cleaned</td></tr>
<tr><td>Best for</td><td>Routine, regular maintenance</td><td>Bad smell, weak airflow, black spots, long gap since last service</td></tr>
</tbody></table></div>
""" + fig('/assets/img/parts/blower_wheel.webp', 'Split AC indoor blower wheel that collects dust and mould', 'The indoor blower wheel collects dust and mould that only a deep cleaning can properly remove.', 480, 480) + """
<h2>Our AC servicing checklist</h2>
<ul><li>Filters removed, washed and dried</li><li>Indoor coil (evaporator) cleaned and inspected for damage</li><li>Blower wheel and louvres cleaned</li><li>Drain tray and drain pipe flushed and checked for slope and leaks</li><li>Outdoor condenser coil and fan cleaned</li><li>Electrical connections, capacitor and stabiliser checked</li><li>Outdoor unit mounting and ventilation checked</li><li>Cooling performance tested after the service</li></ul>
<p>If we find a deeper problem during the service (a weak capacitor, a refrigerant leak, a noisy motor), we explain it and give you an estimate first. Nothing extra is done without your approval.</p>
<h2>How often should you service your AC in Narasaraopet?</h2>
<ul><li><b>February–March</b>: a full service before the peak heat.</li><li><b>July–August</b>: a second service if the AC runs most of the day.</li><li><b>Every 2–3 weeks in summer</b>: rinse the filters yourself.</li><li><b>Deep cleaning</b>: once a year for heavy users, or whenever there is a smell or weak airflow.</li></ul>
<p>For signs your AC is overdue, see <a href="/blog/when-should-you-service-your-ac/">when should you service your air conditioner?</a></p>
<h2>Why servicing matters here</h2>
<p>Summer heat and dust in the Palnadu region mean filters and coils clog faster than in cooler cities. A clogged AC cools less, uses more electricity (see our <a href="/blog/how-to-reduce-ac-electricity-bill/">power-saving tips</a>) and puts extra strain on the compressor, the most expensive part to replace.</p>
<h2>What we do not do</h2>
<p>We do not "top up" gas as part of a service. Refrigerant only needs attention if there is a leak, and that is diagnosed and quoted separately. See <a href="/blog/ac-gas-filling-when-is-it-required/">when AC gas filling is actually required</a>.</p>
<p>Book <a href="/ac-services/#ac-servicing">AC servicing</a> or <a href="/ac-services/#ac-deep-cleaning">AC deep cleaning</a>, or see all <a href="/ac-services/">AC services</a>.</p>""",
 'faq': [
  ("How long does AC servicing take?", "A general service usually takes about 45–60 minutes per split AC. A deep cleaning takes longer because the indoor unit is washed thoroughly."),
  ("Is AC deep cleaning necessary every time?", "No. A general service is enough for routine maintenance. Deep cleaning is recommended once a year for heavy users, or when there is a bad smell, weak airflow or visible black spots."),
  ("Will servicing improve cooling?", "If dust is the problem, yes: clean filters and coils restore airflow and heat transfer. If cooling is still weak after a service, there may be a gas leak or electrical fault that needs diagnosis."),
  ("Does AC servicing include gas filling?", "No. Gas is only needed if there is a leak. We check and explain any refrigerant issue separately and quote before any work."),
  ("Do you service window ACs too?", "Yes, we service both split and window ACs from all major brands in and around Narasaraopet."),
 ],
 'sources': [("BOBBY guide: When should you service your AC?", "/blog/when-should-you-service-your-ac/"), ("BOBBY: AC servicing & deep cleaning", "/ac-services/#ac-servicing")],
},
# ------------------------------------------------------------------ 5. AC technician near me (local)
{
 'slug': 'ac-technician-near-me', 'img': 'blog_tech', 'svc': 'ac_repair', 'link': '/ac-services/',
 'date': '2026-11-20', 'local': True,
 'seo': 'AC Technician Near Me: How to Choose the Right One | BOBBY',
 'desc': 'Looking for an AC technician or AC mechanic near me? How to choose a reliable AC repair professional, questions to ask and red flags to avoid.',
 'title': ("Looking for an AC Technician Near Me? How to Find a Reliable AC Repair Professional",
           "నా దగ్గర ఏసీ టెక్నీషియన్ కోసం చూస్తున్నారా? నమ్మకమైన ఏసీ రిపేర్ నిపుణుడిని ఎలా ఎంచుకోవాలి",
           "पास में एसी टेक्नीशियन ढूँढ रहे हैं? भरोसेमंद एसी रिपेयर प्रोफ़ेशनल कैसे चुनें"),
 'excerpt': ("How to tell a good AC technician from a risky one: what to ask before the visit, what a proper diagnosis looks like, and the red flags that cost you money.",
             "మంచి ఏసీ టెక్నీషియన్‌ను ఎలా గుర్తించాలి: విజిట్‌కు ముందు ఏమి అడగాలి, సరైన నిర్ధారణ ఎలా ఉంటుంది, డబ్బు నష్టపరిచే హెచ్చరిక సంకేతాలు.",
             "अच्छे एसी टेक्नीशियन को कैसे पहचानें: विज़िट से पहले क्या पूछें, सही जाँच कैसी होती है, और पैसे बर्बाद करने वाले ख़तरे के संकेत।"),
 'body': """<p class="lead-q"><b>Quick answer:</b> a reliable AC technician near you inspects before recommending anything, explains the fault in plain language, gives an estimate before starting, uses proper tools (gauges, vacuum pump, leak detection), and tests the AC before leaving. Be wary of anyone who suggests "gas filling" without checking for a leak, or who will not tell you the charges upfront.</p>
<p>When your AC stops cooling in the middle of summer, it is tempting to call the first number you find. A few minutes of checking can save you a repeat visit, an unnecessary part, or a gas refill that leaks out again in a week.</p>
<h2>Questions to ask before you book</h2>
<ol><li><b>Do you work on my brand and type?</b> (split, window, inverter)</li><li><b>Is there a visit or inspection charge?</b> Get it clear before the visit.</li><li><b>When can you come?</b> A realistic time slot is better than a vague "today".</li><li><b>Will you give an estimate before doing any repair?</b> The answer should be yes.</li><li><b>Do you carry common parts?</b> Capacitors, sensors and fuses are often fixed in one visit.</li></ol>
<h2>What a proper diagnosis looks like</h2>
<ul><li>Checking supply voltage and the stabiliser</li><li>Inspecting filters, coils and the drain</li><li>Measuring temperatures at the indoor unit and the copper pipes</li><li>Checking the outdoor unit: compressor, fan motor, capacitor</li><li>Using pressure gauges if a refrigerant problem is suspected</li></ul>
""" + fig('/assets/img/art/about-photo-sm.webp', 'BOBBY AC technician in uniform with tool bag beside a split AC in Narasaraopet', 'A uniformed technician with the right tools is a good first sign.', 768, 512) + """
<h2>Red flags to watch for</h2>
<ul><li><b>"You need gas" without a leak check.</b> Refrigerant does not get used up; low gas means a leak.</li><li><b>No price until the work is done.</b> You should approve the estimate first.</li><li><b>Replacing the PCB or compressor straight away</b> without testing the cheaper parts (capacitor, sensor, wiring) first.</li><li><b>No vacuum pump</b> for installation or gas work: moisture left in the system damages the compressor.</li><li><b>Leaving without testing</b> the cooling.</li></ul>
<h2>Authorised service centre or independent technician?</h2>
<p>If your AC is under warranty, use the brand's authorised service so the warranty stays valid. After the warranty, a good independent multi-brand technician is often faster and more flexible, especially in smaller towns. What matters is the same either way: inspection, explanation, estimate, careful work and testing.</p>
<h2>Looking for an AC technician near Narasaraopet?</h2>
<p>BOBBY provides doorstep AC repair, servicing, installation, uninstallation and gas leak repair in Narasaraopet and nearby areas within about 20 km. We are an independent multi-brand service. Every visit follows the same rules: <a href="/about/">inspect before repair, explain before proceeding, estimate before work</a>.</p>
<p>See the most common faults in <a href="/blog/ac-repair-in-narasaraopet/">AC repair in Narasaraopet</a>, browse <a href="/ac-services/">all AC services</a>, or read our <a href="/faqs/">FAQs</a>.</p>""",
 'faq': [
  ("How do I find a good AC mechanic near me?", "Look for someone who explains charges upfront, inspects before recommending repairs, gives an estimate before work, carries proper tools, and has genuine local reviews."),
  ("Should I use the authorised service centre or a local technician?", "Use authorised service while the AC is under warranty. After that, a reliable independent multi-brand technician is a good option, especially for faster doorstep visits."),
  ("Why does a technician need gauges and a vacuum pump?", "Gauges show whether refrigerant pressure is correct; a vacuum pump removes air and moisture before charging gas. Skipping them leads to poor cooling and compressor damage."),
  ("Is BOBBY available on weekends?", "Call or WhatsApp +91 83748 89163 with your area and preferred time and we will confirm availability for that day."),
 ],
 'sources': [("BOBBY: Our trust principles", "/about/"), ("BOBBY: Contact & booking", "/contact/")],
},
]

NEW_STRINGS = {
 'blog.toc': ("In this article", "ఈ ఆర్టికల్‌లో", "इस लेख में"),
 'blog.faqh': ("Frequently asked questions", "తరచుగా అడిగే ప్రశ్నలు", "अक्सर पूछे जाने वाले सवाल"),
 'blog.src': ("Sources & further reading", "మూలాలు & మరింత చదవడానికి", "स्रोत और आगे पढ़ें"),
 'blog.lang': ("This article is currently available in English.", "ఈ ఆర్టికల్ ప్రస్తుతం ఆంగ్లంలో అందుబాటులో ఉంది.", "यह लेख अभी अंग्रेज़ी में उपलब्ध है।"),
 'blog.local.h': ("Need AC repair or servicing in Narasaraopet?", "నరసరావుపేటలో ఏసీ రిపేర్ లేదా సర్వీసింగ్ కావాలా?", "नरसरावपेट में एसी रिपेयर या सर्विसिंग चाहिए?"),
 'blog.local.p': ("Doorstep AC inspection, servicing, installation and repair. Service availability depends on location and scheduling.",
                  "ఇంటి వద్దకే ఏసీ తనిఖీ, సర్వీసింగ్, ఇన్‌స్టాలేషన్ మరియు రిపేర్. సర్వీస్ లభ్యత ప్రాంతం మరియు షెడ్యూల్‌పై ఆధారపడి ఉంటుంది.",
                  "घर पर एसी जाँच, सर्विसिंग, इंस्टॉलेशन और रिपेयर। सर्विस उपलब्धता जगह और शेड्यूल पर निर्भर करती है।"),
}
