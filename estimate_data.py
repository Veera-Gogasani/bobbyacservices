# -*- coding: utf-8 -*-
"""Quick Estimate tool: indicative service price ranges for Narasaraopet (approved by the owner, 24 Nov 2026).
Spare-part prices come straight from spare_parts.py (the AC Spare Parts page), so both always match.
Estimates are indicative only; the final price is confirmed after inspection."""
import spare_parts as SPD

EST_REVIEW = '24 November 2026'

# Step 1 categories: id, (en, te, hi), icon key (from build.ICONS)
EST_CATS = [
    ('ac', ("AC Services", "ఏసీ సేవలు", "एसी सेवाएं"), 'ac'),
    ('washer', ("Washing Machine", "వాషింగ్ మెషిన్", "वॉशिंग मशीन"), 'washer'),
    ('fridge', ("Fridge", "ఫ్రిజ్", "फ्रिज"), 'fridge'),
    ('cooler', ("Cooler", "కూలర్", "कूलर"), 'cooler'),
    ('fan', ("Ceiling Fan", "సీలింగ్ ఫ్యాన్", "सीलिंग फैन"), 'fan'),
    ('elec', ("Home Electrical", "ఇంటి ఎలక్ట్రికల్", "घरेलू इलेक्ट्रिकल"), 'bolt'),
]

# key, category, (en, te, hi) label, unit key, min, max, plus_parts
EST_SERVICES = [
    ('ac_servicing', 'ac', ("AC general servicing (split / window)", "ఏసీ జనరల్ సర్వీసింగ్ (స్ప్లిట్ / విండో)", "एसी जनरल सर्विसिंग (स्प्लिट / विंडो)"), 'ac', 500, 700, False),
    ('ac_deepclean', 'ac', ("AC deep cleaning (jet wash)", "ఏసీ డీప్ క్లీనింగ్ (జెట్ వాష్)", "एसी डीप क्लीनिंग (जेट वॉश)"), 'ac', 900, 1500, False),
    ('ac_repair', 'ac', ("AC repair – inspection / visit charge", "ఏసీ రిపేర్ – తనిఖీ / విజిట్ చార్జ్", "एसी रिपेयर – जांच / विज़िट चार्ज"), 'ac', 300, 500, True),
    ('ac_gas', 'ac', ("AC gas filling (with leak check)", "ఏసీ గ్యాస్ ఫిల్లింగ్ (లీక్ చెక్‌తో)", "एसी गैस फिलिंग (लीक चेक के साथ)"), 'ac', 2000, 3500, False),
    ('ac_install', 'ac', ("Split AC installation", "స్ప్లిట్ ఏసీ ఇన్‌స్టాలేషన్", "स्प्लिट एसी इंस्टॉलेशन"), 'ac', 1500, 2500, False),
    ('ac_uninstall', 'ac', ("AC uninstallation", "ఏసీ అన్‌ఇన్‌స్టాలేషన్", "एसी अनइंस्टॉलेशन"), 'ac', 700, 1000, False),
    ('washer', 'washer', ("Washing machine repair – visit charge", "వాషింగ్ మెషిన్ రిపేర్ – విజిట్ చార్జ్", "वॉशिंग मशीन रिपेयर – विज़िट चार्ज"), 'unit', 300, 500, True),
    ('fridge', 'fridge', ("Refrigerator repair – visit charge", "ఫ్రిజ్ రిపేర్ – విజిట్ చార్జ్", "फ्रिज रिपेयर – विज़िट चार्ज"), 'unit', 300, 500, True),
    ('cooler', 'cooler', ("Air cooler repair / service", "ఎయిర్ కూలర్ రిపేర్ / సర్వీస్", "एयर कूलर रिपेयर / सर्विस"), 'unit', 250, 400, False),
    ('fan', 'fan', ("Ceiling fan repair", "సీలింగ్ ఫ్యాన్ రిపేర్", "सीलिंग फैन रिपेयर"), 'fan', 200, 350, False),
    ('elec_visit', 'elec', ("Electrical inspection / visit charge", "ఎలక్ట్రికల్ తనిఖీ / విజిట్ చార్జ్", "इलेक्ट्रिकल जांच / विज़िट चार्ज"), 'visit', 200, 400, True),
    ('elec_switch', 'elec', ("Switch / socket replacement", "స్విచ్ / సాకెట్ మార్పు", "स्विच / सॉकेट बदलना"), 'point', 100, 200, True),
    ('elec_fit', 'elec', ("Fan / light fitting", "ఫ్యాన్ / లైట్ ఫిట్టింగ్", "पंखा / लाइट फिटिंग"), 'point', 200, 400, False),
    ('elec_mcb', 'elec', ("MCB / wiring fault check & repair", "ఎంసీబీ / వైరింగ్ లోపం తనిఖీ & రిపేర్", "MCB / वायरिंग खराबी जांच और रिपेयर"), 'visit', 300, 600, True),
]

EST_STRINGS = {
 'est.btn': ("Get Estimate", "అంచనా పొందండి", "अनुमान पाएं"),
 'est.h': ("Get a Quick Estimate", "త్వరిత అంచనా పొందండి", "तुरंत अनुमान पाएं"),
 'est.sub': ("Tick the services you need. Prices are typical ranges in Narasaraopet.", "మీకు కావలసిన సేవలను ఎంచుకోండి. ధరలు నరసరావుపేటలో సాధారణ శ్రేణులు.", "ज़रूरी सेवाएं चुनें। कीमतें नरसरावपेट की सामान्य रेंज हैं।"),
 'est.svc': ("Services", "సేవలు", "सेवाएं"),
 'est.u.ac': ("per AC", "ఒక్కో ఏసీకి", "प्रति एसी"),
 'est.u.unit': ("per appliance", "ఒక్కో ఉపకరణానికి", "प्रति उपकरण"),
 'est.u.fan': ("per fan", "ఒక్కో ఫ్యాన్‌కు", "प्रति पंखा"),
 'est.u.visit': ("per visit", "ఒక్కో విజిట్‌కు", "प्रति विज़िट"),
 'est.u.point': ("per point", "ఒక్కో పాయింట్‌కు", "प्रति पॉइंट"),
 'est.step1': ("1. What do you need help with?", "1. మీకు ఏ సహాయం కావాలి?", "1. आपको किसमें मदद चाहिए?"),
 'est.step1.p': ("Select one or more.", "ఒకటి లేదా ఎక్కువ ఎంచుకోండి.", "एक या अधिक चुनें।"),
 'est.step2': ("2. Choose services", "2. సేవలను ఎంచుకోండి", "2. सेवाएं चुनें"),
 'est.pickcat': ("Select a category above to see services and prices.", "సేవలు, ధరలు చూడటానికి పైన ఒక విభాగాన్ని ఎంచుకోండి.", "सेवाएं और कीमतें देखने के लिए ऊपर एक श्रेणी चुनें।"),
 'est.plusparts': ("+ parts if needed", "+ అవసరమైతే విడిభాగాలు", "+ ज़रूरत हो तो पार्ट्स"),
 'est.parts': ("Add AC spare parts (optional)", "ఏసీ విడిభాగాలు జోడించండి (ఐచ్ఛికం)", "एसी स्पेयर पार्ट्स जोड़ें (वैकल्पिक)"),
 'est.parts.p': ("Prices from our AC Spare Parts list. The technician confirms which part your AC needs.", "మా ఏసీ స్పేర్ పార్ట్స్ జాబితా నుండి ధరలు. మీ ఏసీకి ఏ విడిభాగం కావాలో టెక్నీషియన్ నిర్ధారిస్తారు.", "कीमतें हमारी एसी स्पेयर पार्ट्स सूची से। आपके एसी को कौन-सा पार्ट चाहिए, टेक्नीशियन पुष्टि करते हैं।"),
 'est.pick': ("Choose a spare part", "విడిభాగాన్ని ఎంచుకోండి", "स्पेयर पार्ट चुनें"),
 'est.add': ("Add", "జోడించు", "जोड़ें"),
 'est.sum': ("Your estimate", "మీ అంచనా", "आपका अनुमान"),
 'est.total': ("Estimated total", "అంచనా మొత్తం", "अनुमानित कुल"),
 'est.empty': ("Select at least one service to see your estimate.", "అంచనా చూడటానికి కనీసం ఒక సేవను ఎంచుకోండి.", "अनुमान देखने के लिए कम से कम एक सेवा चुनें।"),
 'est.note': ("This is only an estimate, not the final price. The final price depends on inspection, spare parts and the service needed, and may vary. Work starts only after you approve the final quote.",
              "ఇది అంచనా మాత్రమే, తుది ధర కాదు. తుది ధర తనిఖీ, విడిభాగాలు మరియు అవసరమైన సేవపై ఆధారపడుతుంది, మారవచ్చు. మీరు తుది కొటేషన్ ఒప్పుకున్న తర్వాతే పని మొదలవుతుంది.",
              "यह केवल अनुमान है, अंतिम कीमत नहीं। अंतिम कीमत जांच, स्पेयर पार्ट्स और ज़रूरी सेवा पर निर्भर करती है और बदल सकती है। अंतिम कोटेशन मंज़ूर करने के बाद ही काम शुरू होता है।"),
 'est.pdf': ("Download PDF", "PDF డౌన్‌లోడ్", "PDF डाउनलोड"),
 'est.wa': ("Send on WhatsApp", "వాట్సాప్‌లో పంపండి", "व्हाट्सऐप पर भेजें"),
 'est.remove': ("Remove", "తొలగించు", "हटाएं"),
 'est.loading': ("Loading…", "లోడ్ అవుతోంది…", "लोड हो रहा है…"),
}

def inr(n): return '{:,}'.format(n)

def estimate_json():
    """Data the estimator downloads when it opens (kept out of every page to stay light)."""
    labels = {'en': {}, 'te': {}, 'hi': {}}
    for k, v in EST_STRINGS.items():
        for i, L in enumerate(('en', 'te', 'hi')): labels[L][k] = v[i]
    services = []
    for key, cat, lab, unit, lo, hi, plus in EST_SERVICES:
        services.append({'id': key, 'cat': cat, 'name': dict(zip(('en', 'te', 'hi'), lab)), 'unit': unit, 'min': lo, 'max': hi, 'plus': plus})
    cats_out = [{'id': c, 'name': dict(zip(('en', 'te', 'hi'), lab)), 'icon': icon} for c, lab, icon in EST_CATS]
    cats = dict(SPD.CATEGORIES)
    parts = [{'id': p['id'], 'name': p['name'], 'cat': cats[p['cat']], 'min': p['price'][0], 'max': p['price'][1],
              'unit': SPD.UNIT_LABEL[p['unit']]} for p in SPD.PARTS if p['price']]
    return {'cats': cats_out, 'reviewed': EST_REVIEW, 'partsReviewed': SPD.PRICE_REVIEW, 'labels': labels, 'services': services, 'parts': parts}
