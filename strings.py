# -*- coding: utf-8 -*-
# Every visible string on the site: key -> (English, Telugu, Hindi)
S = {}
def add(d):
    S.update(d)

# ---------- common ----------
add({
 'brand.tagline': ("Complete Appliance Care at Your Doorstep.", "మీ ఇంటి వద్దకే పూర్తి అప్లయెన్స్ సంరక్షణ.", "आपके दरवाज़े पर संपूर्ण अप्लायंस केयर।"),
 'nav.home': ("Home", "హోమ్", "होम"),
 'nav.about': ("About Us", "మా గురించి", "हमारे बारे में"),
 'nav.ac': ("AC Services", "ఏసీ సేవలు", "एसी सेवाएँ"),
 'nav.appliance': ("Appliance Services", "అప్లయెన్స్ సేవలు", "अप्लायंस सेवाएँ"),
 'nav.brands': ("Brands We Service", "బ్రాండ్లు", "ब्रांड्स"),
 'nav.faqs': ("FAQs", "ప్రశ్నలు", "सवाल-जवाब"),
 'nav.contact': ("Contact Us", "సంప్రదించండి", "संपर्क करें"),
 'nav.blog': ("Blog", "బ్లాగ్", "ब्लॉग"),
 'nav.menu': ("Menu", "మెనూ", "मेनू"),
 'nav.close': ("Close menu", "మెనూ మూసివేయండి", "मेनू बंद करें"),
 'lang.label': ("Language", "భాష", "भाषा"),
 'btn.call': ("Call Now", "కాల్ చేయండి", "कॉल करें"),
 'btn.callnum': ("Call +91 83748 89163", "కాల్: +91 83748 89163", "कॉल: +91 83748 89163"),
 'btn.wa': ("WhatsApp", "వాట్సాప్", "व्हाट्सऐप"),
 'btn.wabook': ("Book on WhatsApp", "వాట్సాప్‌లో బుక్", "व्हाट्सऐप पर बुक करें"),
 'btn.wachat': ("Chat on WhatsApp", "వాట్సాప్‌లో చాట్ చేయండి", "व्हाट्सऐप पर चैट करें"),
 'btn.book': ("Book Now", "ఇప్పుడే బుక్ చేయండి", "अभी बुक करें"),
 'btn.bookac': ("Book AC Service", "ఏసీ సర్వీస్ బుక్ చేయండి", "एसी सर्विस बुक करें"),
 'btn.more': ("Read more", "ఇంకా చదవండి", "और पढ़ें"),
 'btn.allac': ("View all AC services", "అన్ని ఏసీ సేవలు చూడండి", "सभी एसी सेवाएँ देखें"),
 'btn.allapp': ("View appliance services", "అప్లయెన్స్ సేవలు చూడండి", "अप्लायंस सेवाएँ देखें"),
 'btn.allfaq': ("See all FAQs", "అన్ని ప్రశ్నలు చూడండి", "सभी सवाल देखें"),
 'btn.allblog': ("Visit the Knowledge Centre", "నాలెడ్జ్ సెంటర్ చూడండి", "नॉलेज सेंटर देखें"),
 'btn.contact': ("Contact Us", "సంప్రదించండి", "संपर्क करें"),
 'btn.home': ("Back to Home", "హోమ్‌కు వెళ్ళండి", "होम पर जाएँ"),
 'price.from': ("Starting from", "ప్రారంభ ధర", "शुरुआती कीमत"),
 'price.note': ("Final price is confirmed after inspection, before work begins.", "తనిఖీ తర్వాత, పని మొదలయ్యే ముందే తుది ధర నిర్ధారించబడుతుంది.", "अंतिम कीमत जाँच के बाद, काम शुरू होने से पहले तय होती है।"),
 'price.onvisit': ("Estimate after inspection", "తనిఖీ తర్వాత అంచనా", "जाँच के बाद अनुमान"),
 'wa.default': ("Hello BOBBY AC REPAIR & HOME APPLIANCE SERVICES, I need AC/appliance service in Narasaraopet. Please contact me.",
                "హలో BOBBY AC REPAIR & HOME APPLIANCE SERVICES, నాకు నరసరావుపేటలో ఏసీ/అప్లయెన్స్ సర్వీస్ కావాలి. దయచేసి నన్ను సంప్రదించండి.",
                "नमस्ते BOBBY AC REPAIR & HOME APPLIANCE SERVICES, मुझे नरसरावपेट में एसी/अप्लायंस सर्विस चाहिए। कृपया मुझसे संपर्क करें।"),
 'wa.service': ("Hello BOBBY AC REPAIR & HOME APPLIANCE SERVICES, I need {service} in Narasaraopet. Please contact me.",
                "హలో BOBBY AC REPAIR & HOME APPLIANCE SERVICES, నాకు నరసరావుపేటలో {service} కావాలి. దయచేసి నన్ను సంప్రదించండి.",
                "नमस्ते BOBBY AC REPAIR & HOME APPLIANCE SERVICES, मुझे नरसरावपेट में {service} चाहिए। कृपया मुझसे संपर्क करें।"),
 'wa.feedback': ("Hello BOBBY AC REPAIR & HOME APPLIANCE SERVICES, I would like to share feedback about my service.",
                 "హలో BOBBY AC REPAIR & HOME APPLIANCE SERVICES, నా సర్వీస్ గురించి అభిప్రాయం చెప్పాలనుకుంటున్నాను.",
                 "नमस्ते BOBBY AC REPAIR & HOME APPLIANCE SERVICES, मैं अपनी सर्विस के बारे में राय देना चाहता/चाहती हूँ।"),
 'crumb.home': ("Home", "హోమ్", "होम"),
 'skip': ("Skip to main content", "ప్రధాన విషయానికి వెళ్ళండి", "मुख्य सामग्री पर जाएँ"),
 'loc.short': ("Narasaraopet, Andhra Pradesh", "నరసరావుపేట, ఆంధ్రప్రదేశ్", "नरसरावपेट, आंध्र प्रदेश"),
 'mbar.call': ("Call Now", "కాల్", "कॉल"),
 'mbar.wa': ("WhatsApp", "వాట్సాప్", "व्हाट्सऐप"),
})

# ---------- services ----------
SERVICES = ['ac_repair','ac_servicing','ac_install','ac_uninstall','ac_gas','fridge','washer','cooler','fan']
add({
 'svc.ac_repair.name': ("AC Repair", "ఏసీ రిపేర్", "एसी रिपेयर"),
 'svc.ac_repair.desc': ("Not cooling, not starting, leaking or noisy AC: diagnosed and fixed.", "చల్లబడకపోవడం, ఆన్ కాకపోవడం, నీరు కారడం లేదా శబ్దం: సమస్య గుర్తించి సరిచేస్తాం.", "ठंडा न करना, चालू न होना, पानी टपकना या शोर: जाँचकर ठीक करते हैं।"),
 'svc.ac_servicing.name': ("AC Servicing", "ఏసీ సర్వీసింగ్", "एसी सर्विसिंग"),
 'svc.ac_servicing.desc': ("Filter, indoor and outdoor unit cleaning for better cooling.", "మెరుగైన కూలింగ్ కోసం ఫిల్టర్, ఇండోర్ & అవుట్‌డోర్ యూనిట్ క్లీనింగ్.", "बेहतर कूलिंग के लिए फ़िल्टर, इनडोर और आउटडोर यूनिट की सफ़ाई।"),
 'svc.ac_install.name': ("AC Installation", "ఏసీ ఇన్‌స్టాలేషన్", "एसी इंस्टॉलेशन"),
 'svc.ac_install.desc': ("Neat split and window AC installation, tested before we leave.", "స్ప్లిట్ & విండో ఏసీల చక్కని ఇన్‌స్టాలేషన్, వెళ్ళే ముందు టెస్టింగ్.", "स्प्लिट और विंडो एसी की साफ़-सुथरी इंस्टॉलेशन, जाने से पहले टेस्टिंग।"),
 'svc.ac_uninstall.name': ("AC Uninstallation", "ఏసీ అన్‌ఇన్‌స్టాలేషన్", "एसी अनइंस्टॉलेशन"),
 'svc.ac_uninstall.desc': ("Safe removal of indoor and outdoor units when you shift.", "ఇల్లు మారేటప్పుడు ఇండోర్ & అవుట్‌డోర్ యూనిట్ల సురక్షిత తొలగింపు.", "घर बदलते समय इनडोर और आउटडोर यूनिट को सुरक्षित हटाना।"),
 'svc.ac_gas.name': ("AC Gas Filling", "ఏసీ గ్యాస్ ఫిల్లింగ్", "एसी गैस फिलिंग"),
 'svc.ac_gas.desc': ("Leak check first, then gas filling only if it is needed.", "ముందు లీక్ చెకింగ్, అవసరమైతేనే గ్యాస్ ఫిల్లింగ్.", "पहले लीक की जाँच, ज़रूरत होने पर ही गैस फिलिंग।"),
 'svc.ac_deepclean.name': ("AC Deep Cleaning", "ఏసీ డీప్ క్లీనింగ్", "एसी डीप क्लीनिंग"),
 'svc.fridge.name': ("Refrigerator Repair", "ఫ్రిజ్ రిపేర్", "फ्रिज रिपेयर"),
 'svc.fridge.desc': ("Cooling problems and general refrigerator repairs.", "కూలింగ్ సమస్యలు మరియు సాధారణ ఫ్రిజ్ రిపేర్లు.", "कूलिंग की समस्या और सामान्य फ्रिज रिपेयर।"),
 'svc.washer.name': ("Washing Machine Repair", "వాషింగ్ మెషిన్ రిపేర్", "वॉशिंग मशीन रिपेयर"),
 'svc.washer.desc': ("Drainage, spinning and other washing machine problems.", "డ్రైనేజ్, స్పిన్నింగ్ మరియు ఇతర వాషింగ్ మెషిన్ సమస్యలు.", "पानी निकासी, स्पिनिंग और अन्य वॉशिंग मशीन की समस्याएँ।"),
 'svc.cooler.name': ("Air Cooler Repair", "ఎయిర్ కూలర్ రిపేర్", "एयर कूलर रिपेयर"),
 'svc.cooler.desc': ("Pump, water flow and cooling performance issues.", "పంప్, నీటి ప్రవాహం మరియు కూలింగ్ సమస్యలు.", "पंप, पानी के बहाव और कूलिंग की समस्याएँ।"),
 'svc.fan.name': ("Ceiling Fan Repair", "సీలింగ్ ఫ్యాన్ రిపేర్", "सीलिंग फैन रिपेयर"),
 'svc.fan.desc': ("Slow speed, noise or a fan that will not run.", "నెమ్మదిగా తిరగడం, శబ్దం లేదా ఫ్యాన్ పనిచేయకపోవడం.", "धीमी स्पीड, शोर या पंखा न चलना।"),
})

# ---------- home ----------
add({
 'hero.eyebrow': ("Doorstep AC service in Narasaraopet", "నరసరావుపేటలో ఇంటి వద్దకే ఏసీ సర్వీస్", "नरसरावपेट में घर पर एसी सर्विस"),
 'hero.h1': ("Reliable <span class=\"hl\">AC Repair &amp; Services</span> at Your Doorstep",
             "మీ ఇంటి వద్దకే నమ్మకమైన <span class=\"hl\">ఏసీ రిపేర్ &amp; సర్వీసులు</span>",
             "आपके घर पर भरोसेमंद <span class=\"hl\">एसी रिपेयर और सर्विस</span>"),
 'hero.sub': ("Looking for dependable AC repair and servicing in Narasaraopet? BOBBY provides AC installation, uninstallation, servicing, gas filling and repair, along with home appliance repair services.",
              "నరసరావుపేటలో నమ్మకమైన ఏసీ రిపేర్ మరియు సర్వీసింగ్ కోసం చూస్తున్నారా? BOBBY ఏసీ ఇన్‌స్టాలేషన్, అన్‌ఇన్‌స్టాలేషన్, సర్వీసింగ్, గ్యాస్ ఫిల్లింగ్, రిపేర్‌తో పాటు గృహోపకరణాల రిపేర్ సేవలను అందిస్తుంది.",
              "नरसरावपेट में भरोसेमंद एसी रिपेयर और सर्विसिंग चाहिए? BOBBY एसी इंस्टॉलेशन, अनइंस्टॉलेशन, सर्विसिंग, गैस फिलिंग और रिपेयर के साथ घरेलू उपकरणों की रिपेयर सेवाएँ भी देता है।"),
 'hero.trust': ("Split &amp; window ACs · All major brands · Phone &amp; WhatsApp booking",
                "స్ప్లిట్ &amp; విండో ఏసీలు · ప్రముఖ బ్రాండ్లు అన్నీ · ఫోన్ &amp; వాట్సాప్ బుకింగ్",
                "स्प्लिट और विंडो एसी · सभी प्रमुख ब्रांड · फ़ोन और व्हाट्सऐप बुकिंग"),
 'hero.card.title': ("Cooling restored", "కూలింగ్ మళ్ళీ సిద్ధం", "कूलिंग फिर से चालू"),
 'hero.card.sub': ("Inspected · Serviced · Tested", "తనిఖీ · సర్వీస్ · టెస్ట్", "जाँच · सर्विस · टेस्ट"),
 'quick.eyebrow': ("Quick booking", "త్వరిత బుకింగ్", "क्विक बुकिंग"),
 'quick.h2': ("What Service Do You Need Today?", "ఈరోజు మీకు ఏ సర్వీస్ కావాలి?", "आज आपको कौन-सी सर्विस चाहिए?"),
 'quick.sub': ("Pick a service and book it instantly on WhatsApp. Your message is ready, just tap send.", "సర్వీస్ ఎంచుకుని వాట్సాప్‌లో వెంటనే బుక్ చేయండి. మెసేజ్ సిద్ధంగా ఉంటుంది, సెండ్ నొక్కండి చాలు.", "सर्विस चुनें और व्हाट्सऐप पर तुरंत बुक करें। मैसेज तैयार रहेगा, बस भेजें दबाएँ।"),
 'acsec.eyebrow': ("Our main focus", "మా ప్రధాన సేవ", "हमारी मुख्य सेवा"),
 'acsec.h2': ("Complete AC Services in Narasaraopet", "నరసరావుపేటలో పూర్తి ఏసీ సేవలు", "नरसरावपेट में संपूर्ण एसी सेवाएँ"),
 'acsec.sub': ("AC repair and servicing is what we do best. Every visit starts with a proper inspection, so we fix the real problem instead of guessing.",
               "ఏసీ రిపేర్ మరియు సర్వీసింగ్ మా ప్రత్యేకత. ఊహించకుండా అసలు సమస్యను సరిచేయడానికి, ప్రతి విజిట్ సరైన తనిఖీతో మొదలవుతుంది.",
               "एसी रिपेयर और सर्विसिंग हमारी ख़ासियत है। अंदाज़ा लगाने के बजाय असली समस्या ठीक करने के लिए हर विज़िट सही जाँच से शुरू होती है।"),
 'appsec.eyebrow': ("Beyond AC", "ఏసీతో పాటు", "एसी के अलावा"),
 'appsec.h2': ("Home Appliance Repair Services", "గృహోపకరణాల రిపేర్ సేవలు", "घरेलू उपकरण रिपेयर सेवाएँ"),
 'appsec.sub': ("We also repair the appliances your home depends on every day.", "మీ ఇంటికి రోజూ అవసరమైన ఉపకరణాలను కూడా మేము రిపేర్ చేస్తాము.", "हम आपके घर के रोज़मर्रा के उपकरण भी रिपेयर करते हैं।"),
 'brands.eyebrow': ("Multi-brand service", "మల్టీ-బ్రాండ్ సర్వీస్", "मल्टी-ब्रांड सर्विस"),
 'brands.h2': ("Multi-Brand AC &amp; Home Appliance Services", "మల్టీ-బ్రాండ్ ఏసీ &amp; గృహోపకరణాల సేవలు", "मल्टी-ब्रांड एसी और घरेलू उपकरण सेवाएँ"),
 'brands.sub': ("We provide independent repair and servicing support for selected products from popular appliance brands.",
                "ప్రముఖ బ్రాండ్ల ఎంపిక చేసిన ఉత్పత్తులకు మేము స్వతంత్ర రిపేర్ మరియు సర్వీసింగ్ సహాయం అందిస్తాము.",
                "हम लोकप्रिय ब्रांड्स के चुनिंदा उत्पादों के लिए स्वतंत्र रिपेयर और सर्विसिंग सहायता देते हैं।"),
 'brands.note': ("BOBBY is an independent service provider and is not an authorised service centre or official partner of these brands. Brand names are shown only to indicate the products we work on.",
                 "BOBBY ఒక స్వతంత్ర సర్వీస్ ప్రొవైడర్; ఈ బ్రాండ్ల అధీకృత సర్వీస్ సెంటర్ లేదా అధికారిక భాగస్వామి కాదు. మేము పనిచేసే ఉత్పత్తులను తెలియజేయడానికి మాత్రమే బ్రాండ్ పేర్లు చూపబడ్డాయి.",
                 "BOBBY एक स्वतंत्र सर्विस प्रोवाइडर है और इन ब्रांड्स का अधिकृत सर्विस सेंटर या आधिकारिक पार्टनर नहीं है। ब्रांड नाम सिर्फ़ यह बताने के लिए हैं कि हम किन उत्पादों पर काम करते हैं।"),
 'brands.ask': ("Don't see your brand? Ask us on WhatsApp.", "మీ బ్రాండ్ కనిపించలేదా? వాట్సాప్‌లో అడగండి.", "आपका ब्रांड नहीं दिखा? व्हाट्सऐप पर पूछें।"),
 'why.eyebrow': ("Why BOBBY", "ఎందుకు BOBBY", "क्यों BOBBY"),
 'why.h2': ("Why Choose BOBBY?", "BOBBY నే ఎందుకు ఎంచుకోవాలి?", "BOBBY को ही क्यों चुनें?"),
 'why.1.t': ("Local doorstep service", "స్థానిక ఇంటి వద్ద సేవ", "स्थानीय घर पर सेवा"),
 'why.1.d': ("We come to your home in Narasaraopet and nearby areas.", "నరసరావుపేట మరియు చుట్టుపక్కల ప్రాంతాల్లో మీ ఇంటికే వస్తాము.", "नरसरावपेट और आसपास के इलाकों में हम आपके घर आते हैं।"),
 'why.2.t': ("AC repair &amp; maintenance focus", "ఏసీ రిపేర్ &amp; మెయింటెనెన్స్‌పై దృష్టి", "एसी रिपेयर और मेंटेनेंस पर फ़ोकस"),
 'why.2.d': ("AC work is the core of what we do, every single day.", "ఏసీ పని మా రోజువారీ పనిలో ప్రధాన భాగం.", "एसी का काम हमारे रोज़ के काम का मुख्य हिस्सा है।"),
 'why.3.t': ("Many appliances, one call", "ఒకే కాల్‌తో అనేక ఉపకరణాలు", "एक कॉल, कई उपकरण"),
 'why.3.d': ("AC, refrigerator, washing machine, air cooler and ceiling fan.", "ఏసీ, ఫ్రిజ్, వాషింగ్ మెషిన్, ఎయిర్ కూలర్ మరియు సీలింగ్ ఫ్యాన్.", "एसी, फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन।"),
 'why.4.t': ("Clear communication", "స్పష్టమైన సమాచారం", "साफ़ बातचीत"),
 'why.4.d': ("We explain the problem in simple words before starting.", "పని మొదలుపెట్టే ముందు సమస్యను సులభమైన మాటల్లో వివరిస్తాము.", "काम शुरू करने से पहले समस्या आसान शब्दों में समझाते हैं।"),
 'why.5.t': ("Estimate before work begins", "పని ముందే అంచనా", "काम से पहले अनुमान"),
 'why.5.d': ("You approve the cost before any repair starts.", "ఏ రిపేర్ మొదలయ్యే ముందే ఖర్చును మీరు ఆమోదిస్తారు.", "किसी भी रिपेयर से पहले आप खर्च को मंज़ूरी देते हैं।"),
 'why.6.t': ("Phone &amp; WhatsApp booking", "ఫోన్ &amp; వాట్సాప్ బుకింగ్", "फ़ोन और व्हाट्सऐप बुकिंग"),
 'why.6.d': ("Book in a minute with a call or a WhatsApp message.", "కాల్ లేదా వాట్సాప్ మెసేజ్‌తో ఒక్క నిమిషంలో బుక్ చేయండి.", "कॉल या व्हाट्सऐप मैसेज से एक मिनट में बुक करें।"),
 'why.7.t': ("Customer-focused service", "కస్టమర్‌కే ప్రాధాన్యత", "ग्राहक सबसे पहले"),
 'why.7.d': ("Respectful, tidy work inside your home.", "మీ ఇంట్లో మర్యాదపూర్వకమైన, శుభ్రమైన పని.", "आपके घर में सम्मानजनक और साफ़-सुथरा काम।"),
 'how.eyebrow': ("Simple process", "సులభమైన విధానం", "आसान प्रक्रिया"),
 'how.h2': ("How Our Service Works", "మా సర్వీస్ ఎలా పనిచేస్తుంది", "हमारी सर्विस कैसे काम करती है"),
 'how.1.t': ("Book Your Service", "మీ సర్వీస్ బుక్ చేయండి", "अपनी सर्विस बुक करें"),
 'how.1.d': ("Call or WhatsApp BOBBY and explain your appliance issue.", "BOBBY కి కాల్ లేదా వాట్సాప్ చేసి మీ ఉపకరణ సమస్యను వివరించండి.", "BOBBY को कॉल या व्हाट्सऐप करें और अपने उपकरण की समस्या बताएँ।"),
 'how.2.t': ("Discuss the Problem", "సమస్య గురించి మాట్లాడండి", "समस्या पर बात करें"),
 'how.2.d': ("Share your appliance type, brand and service requirement.", "మీ ఉపకరణం రకం, బ్రాండ్ మరియు సర్వీస్ అవసరాన్ని తెలియజేయండి.", "उपकरण का प्रकार, ब्रांड और सर्विस की ज़रूरत बताएँ।"),
 'how.3.t': ("Technician Visit", "టెక్నీషియన్ విజిట్", "टेक्नीशियन विज़िट"),
 'how.3.d': ("We arrange a visit and inspect the appliance.", "విజిట్ ఏర్పాటు చేసి ఉపకరణాన్ని తనిఖీ చేస్తాము.", "हम विज़िट तय करते हैं और उपकरण की जाँच करते हैं।"),
 'how.4.t': ("Service Completion", "సర్వీస్ పూర్తి", "सर्विस पूरी"),
 'how.4.d': ("You confirm the estimate, we complete the agreed work and test the appliance.", "మీరు అంచనాను నిర్ధారించాక, అంగీకరించిన పని పూర్తి చేసి ఉపకరణాన్ని టెస్ట్ చేస్తాము.", "आपके अनुमान की पुष्टि के बाद हम तय काम पूरा करके उपकरण की टेस्टिंग करते हैं।"),
 'rev.eyebrow': ("Reviews", "రివ్యూలు", "रिव्यू"),
 'rev.h2': ("Customer Reviews", "కస్టమర్ రివ్యూలు", "ग्राहकों की राय"),
 'rev.sub': ("We publish only genuine feedback from real customers. Had a service from BOBBY? Tell us how it went.",
             "నిజమైన కస్టమర్ల అసలైన అభిప్రాయాలను మాత్రమే మేము ప్రచురిస్తాము. BOBBY నుండి సర్వీస్ పొందారా? మీ అనుభవం మాకు చెప్పండి.",
             "हम सिर्फ़ असली ग्राहकों की सच्ची राय प्रकाशित करते हैं। BOBBY से सर्विस ली है? अपना अनुभव हमें बताएँ।"),
 'rev.btn': ("Share Your Feedback", "మీ అభిప్రాయం పంచుకోండి", "अपनी राय भेजें"),
 'rev.empty': ("Genuine customer reviews will appear here.", "నిజమైన కస్టమర్ రివ్యూలు ఇక్కడ కనిపిస్తాయి.", "असली ग्राहकों के रिव्यू यहाँ दिखेंगे।"),
 'loc.eyebrow': ("Service area", "సర్వీస్ ప్రాంతం", "सर्विस क्षेत्र"),
 'loc.h2': ("AC Repair &amp; Services in Narasaraopet", "నరసరావుపేటలో ఏసీ రిపేర్ &amp; సర్వీసులు", "नरसरावपेट में एसी रिपेयर और सर्विस"),
 'loc.p1': ("BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES provides doorstep AC repair, installation, servicing and home appliance repair support in Narasaraopet and nearby areas within approximately 10 km.",
            "BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES నరసరావుపేట మరియు సుమారు 10 కి.మీ. పరిధిలోని సమీప ప్రాంతాల్లో ఇంటి వద్దకే ఏసీ రిపేర్, ఇన్‌స్టాలేషన్, సర్వీసింగ్ మరియు గృహోపకరణాల రిపేర్ సేవలు అందిస్తుంది.",
            "BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES नरसरावपेट और लगभग 10 किमी के दायरे में आसपास के इलाकों में घर पर एसी रिपेयर, इंस्टॉलेशन, सर्विसिंग और घरेलू उपकरण रिपेयर की सेवा देता है।"),
 'loc.p2': ("Whether your split AC has stopped cooling in peak summer, your window AC is making a strange noise, or you need an AC installed in a new home, help is a local call away. We also repair refrigerators, washing machines, air coolers and ceiling fans for homes across Narasaraopet.",
            "వేసవిలో మీ స్ప్లిట్ ఏసీ చల్లబడకపోయినా, విండో ఏసీ వింత శబ్దం చేస్తున్నా, లేదా కొత్త ఇంట్లో ఏసీ పెట్టించాలన్నా, ఒక్క లోకల్ కాల్ చాలు. నరసరావుపేటలోని ఇళ్లకు ఫ్రిజ్, వాషింగ్ మెషిన్, ఎయిర్ కూలర్ మరియు సీలింగ్ ఫ్యాన్ రిపేర్లు కూడా చేస్తాము.",
            "चाहे गर्मी में आपका स्प्लिट एसी ठंडा करना बंद कर दे, विंडो एसी अजीब आवाज़ करे, या नए घर में एसी लगवाना हो, मदद बस एक लोकल कॉल दूर है। हम नरसरावपेट के घरों के लिए फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन भी रिपेयर करते हैं।"),
 'loc.c1': ("Narasaraopet town", "నరసరావుపేట పట్టణం", "नरसरावपेट शहर"),
 'loc.c2': ("Nearby areas within about 10 km", "సుమారు 10 కి.మీ. లోపు సమీప ప్రాంతాలు", "लगभग 10 किमी के भीतर आसपास के इलाके"),
 'loc.c3': ("Call to confirm your area", "మీ ప్రాంతం కోసం కాల్ చేసి నిర్ధారించుకోండి", "अपने इलाके की पुष्टि के लिए कॉल करें"),
 'loc.map': ("Map of Narasaraopet, Andhra Pradesh", "నరసరావుపేట, ఆంధ్రప్రదేశ్ మ్యాప్", "नरसरावपेट, आंध्र प्रदेश का नक्शा"),
 'faqh.eyebrow': ("Quick answers", "త్వరిత సమాధానాలు", "तुरंत जवाब"),
 'faqh.h2': ("Frequently Asked Questions", "తరచుగా అడిగే ప్రశ్నలు", "अक्सर पूछे जाने वाले सवाल"),
 'blogh.eyebrow': ("Knowledge Centre", "నాలెడ్జ్ సెంటర్", "नॉलेज सेंटर"),
 'blogh.h2': ("AC &amp; Appliance Care Tips", "ఏసీ &amp; అప్లయెన్స్ సంరక్షణ చిట్కాలు", "एसी और अप्लायंस केयर टिप्स"),
 'blogh.sub': ("Simple guides to help you understand common problems before you call.", "కాల్ చేసే ముందు సాధారణ సమస్యలను అర్థం చేసుకోవడానికి సులభమైన గైడ్‌లు.", "कॉल करने से पहले आम समस्याएँ समझने के लिए आसान गाइड।"),
 'cta.h2': ("AC not cooling? Let's fix it today.", "ఏసీ చల్లబడట్లేదా? ఈరోజే సరిచేద్దాం.", "एसी ठंडा नहीं कर रहा? आज ही ठीक करते हैं।"),
 'cta.sub': ("Call or WhatsApp BOBBY for doorstep service in Narasaraopet.", "నరసరావుపేటలో ఇంటి వద్ద సేవ కోసం BOBBY కి కాల్ లేదా వాట్సాప్ చేయండి.", "नरसरावपेट में घर पर सर्विस के लिए BOBBY को कॉल या व्हाट्सऐप करें।"),
})

# ---------- AC detail ----------
add({
 'ac.A.t': ("AC Repair &amp; Troubleshooting", "ఏసీ రిపేర్ &amp; ట్రబుల్‌షూటింగ్", "एसी रिपेयर और ट्रबलशूटिंग"),
 'ac.A.d': ("Find the real cause and fix it properly.", "అసలు కారణం కనుగొని సరిగ్గా సరిచేస్తాం.", "असली कारण ढूँढकर सही तरीके से ठीक करते हैं।"),
 'ac.A.1': ("AC not cooling", "ఏసీ చల్లబడకపోవడం", "एसी ठंडा न करना"),
 'ac.A.2': ("AC not switching on", "ఏసీ ఆన్ కాకపోవడం", "एसी चालू न होना"),
 'ac.A.3': ("Water leakage", "నీరు కారడం", "पानी टपकना"),
 'ac.A.4': ("Unusual noise", "అసాధారణ శబ్దం", "असामान्य आवाज़"),
 'ac.A.5': ("Cooling performance problems", "కూలింగ్ సరిగా లేకపోవడం", "कूलिंग कम होना"),
 'ac.A.6': ("Electrical and component issues", "ఎలక్ట్రికల్ &amp; విడిభాగాల సమస్యలు", "इलेक्ट्रिकल और पार्ट्स की समस्याएँ"),
 'ac.B.t': ("AC Servicing &amp; Maintenance", "ఏసీ సర్వీసింగ్ &amp; మెయింటెనెన్స్", "एसी सर्विसिंग और मेंटेनेंस"),
 'ac.B.d': ("Keep your AC cooling well and running efficiently.", "మీ ఏసీ బాగా చల్లబరుస్తూ సమర్థవంతంగా నడిచేలా చూస్తాం.", "आपका एसी अच्छी ठंडक दे और कुशलता से चले।"),
 'ac.B.1': ("Regular AC servicing", "రెగ్యులర్ ఏసీ సర్వీసింగ్", "नियमित एसी सर्विसिंग"),
 'ac.B.2': ("Filter cleaning", "ఫిల్టర్ క్లీనింగ్", "फ़िल्टर की सफ़ाई"),
 'ac.B.3': ("Indoor unit cleaning", "ఇండోర్ యూనిట్ క్లీనింగ్", "इनडोर यूनिट की सफ़ाई"),
 'ac.B.4': ("Outdoor unit inspection", "అవుట్‌డోర్ యూనిట్ తనిఖీ", "आउटडोर यूनिट की जाँच"),
 'ac.B.5': ("General maintenance", "సాధారణ మెయింటెనెన్స్", "सामान्य मेंटेनेंस"),
 'ac.C.t': ("AC Installation", "ఏసీ ఇన్‌స్టాలేషన్", "एसी इंस्टॉलेशन"),
 'ac.C.d': ("Correct mounting, piping and testing for your new AC.", "మీ కొత్త ఏసీకి సరైన మౌంటింగ్, పైపింగ్ మరియు టెస్టింగ్.", "आपके नए एसी के लिए सही माउंटिंग, पाइपिंग और टेस्टिंग।"),
 'ac.C.1': ("Split AC installation", "స్ప్లిట్ ఏసీ ఇన్‌స్టాలేషన్", "स्प्लिट एसी इंस्टॉलेशन"),
 'ac.C.2': ("Window AC installation", "విండో ఏసీ ఇన్‌స్టాలేషన్", "विंडो एसी इंस्टॉलेशन"),
 'ac.C.3': ("Installation inspection", "ఇన్‌స్టాలేషన్ తనిఖీ", "इंस्टॉलेशन की जाँच"),
 'ac.C.4': ("Testing after installation", "ఇన్‌స్టాలేషన్ తర్వాత టెస్టింగ్", "इंस्टॉलेशन के बाद टेस्टिंग"),
 'ac.D.t': ("AC Uninstallation", "ఏసీ అన్‌ఇన్‌స్టాలేషన్", "एसी अनइंस्टॉलेशन"),
 'ac.D.d': ("Careful removal when you move or replace your AC.", "ఇల్లు మారేటప్పుడు లేదా ఏసీ మార్చేటప్పుడు జాగ్రత్తగా తొలగింపు.", "घर बदलने या एसी बदलने पर सावधानी से हटाना।"),
 'ac.D.1': ("Safe removal of indoor and outdoor units", "ఇండోర్ &amp; అవుట్‌డోర్ యూనిట్ల సురక్షిత తొలగింపు", "इनडोर और आउटडोर यूनिट को सुरक्षित हटाना"),
 'ac.D.2': ("AC shifting support", "ఏసీ షిఫ్టింగ్ సహాయం", "एसी शिफ्टिंग में सहायता"),
 'ac.D.3': ("Reinstallation enquiries", "రీ-ఇన్‌స్టాలేషన్ విచారణలు", "दोबारा इंस्टॉलेशन की पूछताछ"),
 'ac.E.t': ("AC Gas Filling", "ఏసీ గ్యాస్ ఫిల్లింగ్", "एसी गैस फिलिंग"),
 'ac.E.d': ("Inspection first, gas only when your AC really needs it.", "ముందు తనిఖీ, నిజంగా అవసరమైతేనే గ్యాస్.", "पहले जाँच, गैस तभी जब सच में ज़रूरत हो।"),
 'ac.E.1': ("Cooling-related inspection", "కూలింగ్ సంబంధిత తనిఖీ", "कूलिंग से जुड़ी जाँच"),
 'ac.E.2': ("Refrigerant leak inspection", "రిఫ్రిజిరెంట్ లీక్ తనిఖీ", "रेफ्रिजरेंट लीक की जाँच"),
 'ac.E.3': ("Gas filling where required", "అవసరమైన చోట గ్యాస్ ఫిల్లింగ్", "ज़रूरत होने पर गैस फिलिंग"),
 'ac.E.4': ("Cooling performance testing", "కూలింగ్ పనితీరు టెస్టింగ్", "कूलिंग परफ़ॉर्मेंस टेस्टिंग"),
 'ac.E.note': ("Not every cooling problem needs gas. Dirty filters, a blocked coil or an electrical fault can also cause poor cooling, so our technician inspects the AC first.",
               "ప్రతి కూలింగ్ సమస్యకూ గ్యాస్ అవసరం ఉండదు. మురికి ఫిల్టర్లు, బ్లాక్ అయిన కాయిల్ లేదా ఎలక్ట్రికల్ లోపం వల్ల కూడా కూలింగ్ తగ్గుతుంది. అందుకే మా టెక్నీషియన్ ముందుగా ఏసీని తనిఖీ చేస్తారు.",
               "हर कूलिंग समस्या में गैस की ज़रूरत नहीं होती। गंदे फ़िल्टर, जाम कॉइल या इलेक्ट्रिकल खराबी से भी कूलिंग कम होती है, इसलिए हमारे टेक्नीशियन पहले एसी की जाँच करते हैं।"),
 'ac.F.t': ("AC Deep Cleaning", "ఏసీ డీప్ క్లీనింగ్", "एसी डीप क्लीनिंग"),
 'ac.F.d': ("A thorough clean for fresher air and better airflow.", "తాజా గాలి, మెరుగైన గాలి ప్రవాహం కోసం పూర్తి శుభ్రత.", "ताज़ा हवा और बेहतर एयरफ़्लो के लिए पूरी सफ़ाई।"),
 'ac.F.1': ("Indoor unit cleaning", "ఇండోర్ యూనిట్ క్లీనింగ్", "इनडोर यूनिट की सफ़ाई"),
 'ac.F.2': ("Filter and coil cleaning", "ఫిల్టర్ &amp; కాయిల్ క్లీనింగ్", "फ़िल्टर और कॉइल की सफ़ाई"),
 'ac.F.3': ("General airflow maintenance", "గాలి ప్రవాహ మెయింటెనెన్స్", "एयरफ़्लो मेंटेनेंस"),
 'ac.types.h': ("We work on split and window ACs", "స్ప్లిట్ మరియు విండో ఏసీలపై పనిచేస్తాము", "हम स्प्लिट और विंडो एसी पर काम करते हैं"),
 'ac.types.p': ("Wall-mounted split ACs and window ACs are the most common in Narasaraopet homes, and both are covered by every service on this page.",
                "నరసరావుపేట ఇళ్లలో గోడకు అమర్చే స్ప్లిట్ ఏసీలు మరియు విండో ఏసీలు ఎక్కువగా ఉంటాయి; ఈ పేజీలోని ప్రతి సేవ రెండింటికీ వర్తిస్తుంది.",
                "नरसरावपेट के घरों में दीवार पर लगने वाले स्प्लिट एसी और विंडो एसी सबसे आम हैं, और इस पेज की हर सर्विस दोनों के लिए है।"),
})

# ---------- appliance detail ----------
add({
 'ap.fridge.t': ("Refrigerator Repair &amp; Service", "ఫ్రిజ్ రిపేర్ &amp; సర్వీస్", "फ्रिज रिपेयर और सर्विस"),
 'ap.fridge.1': ("Cooling issues", "కూలింగ్ సమస్యలు", "कूलिंग की समस्याएँ"),
 'ap.fridge.2': ("General refrigerator maintenance", "సాధారణ ఫ్రిజ్ మెయింటెనెన్స్", "फ्रिज का सामान्य मेंटेनेंस"),
 'ap.fridge.3': ("Common refrigerator problems", "సాధారణ ఫ్రిజ్ సమస్యలు", "फ्रिज की आम समस्याएँ"),
 'ap.washer.t': ("Washing Machine Repair &amp; Service", "వాషింగ్ మెషిన్ రిపేర్ &amp; సర్వీస్", "वॉशिंग मशीन रिपेयर और सर्विस"),
 'ap.washer.1': ("Washing machine problems", "వాషింగ్ మెషిన్ సమస్యలు", "वॉशिंग मशीन की समस्याएँ"),
 'ap.washer.2': ("Water drainage issues", "నీరు బయటకు పోకపోవడం", "पानी न निकलने की समस्या"),
 'ap.washer.3': ("General maintenance", "సాధారణ మెయింటెనెన్స్", "सामान्य मेंटेनेंस"),
 'ap.cooler.t': ("Air Cooler Repair &amp; Service", "ఎయిర్ కూలర్ రిపేర్ &amp; సర్వీస్", "एयर कूलर रिपेयर और सर्विस"),
 'ap.cooler.1': ("Cooling performance issues", "కూలింగ్ పనితీరు సమస్యలు", "कूलिंग कम होना"),
 'ap.cooler.2': ("Water circulation problems", "నీటి సర్క్యులేషన్ సమస్యలు", "पानी के सर्कुलेशन की समस्या"),
 'ap.cooler.3': ("General servicing", "సాధారణ సర్వీసింగ్", "सामान्य सर्विसिंग"),
 'ap.fan.t': ("Ceiling Fan Repair &amp; Service", "సీలింగ్ ఫ్యాన్ రిపేర్ &amp; సర్వీస్", "सीलिंग फैन रिपेयर और सर्विस"),
 'ap.fan.1': ("Fan operation problems", "ఫ్యాన్ సరిగా పనిచేయకపోవడం", "पंखा ठीक से न चलना"),
 'ap.fan.2': ("Noise-related issues", "శబ్దం సమస్యలు", "आवाज़ की समस्याएँ"),
 'ap.fan.3': ("General repair and maintenance", "సాధారణ రిపేర్ &amp; మెయింటెనెన్స్", "सामान्य रिपेयर और मेंटेनेंस"),
})

# ---------- FAQ ----------
FAQ_N = 13
add({
 'faq.1.q': ("Do you provide AC repair services in Narasaraopet?", "మీరు నరసరావుపేటలో ఏసీ రిపేర్ సేవలు అందిస్తారా?", "क्या आप नरसरावपेट में एसी रिपेयर सेवा देते हैं?"),
 'faq.1.a': ("Yes. We provide doorstep AC repair in Narasaraopet and nearby areas within about 10 km. Call or WhatsApp +91 83748 89163 to book.",
             "అవును. నరసరావుపేట మరియు సుమారు 10 కి.మీ. లోపు సమీప ప్రాంతాల్లో ఇంటి వద్దకే ఏసీ రిపేర్ చేస్తాము. బుక్ చేయడానికి +91 83748 89163 కి కాల్ లేదా వాట్సాప్ చేయండి.",
             "हाँ। हम नरसरावपेट और लगभग 10 किमी के भीतर आसपास के इलाकों में घर पर एसी रिपेयर करते हैं। बुकिंग के लिए +91 83748 89163 पर कॉल या व्हाट्सऐप करें।"),
 'faq.2.q': ("Do you repair split and window ACs?", "మీరు స్ప్లిట్ మరియు విండో ఏసీలు రిపేర్ చేస్తారా?", "क्या आप स्प्लिट और विंडो एसी रिपेयर करते हैं?"),
 'faq.2.a': ("Yes. We repair and service both split ACs and window ACs.", "అవును. స్ప్లిట్ మరియు విండో ఏసీలు రెండింటినీ రిపేర్ మరియు సర్వీస్ చేస్తాము.", "हाँ। हम स्प्लिट और विंडो दोनों तरह के एसी रिपेयर और सर्विस करते हैं।"),
 'faq.3.q': ("Do you provide AC installation and uninstallation?", "మీరు ఏసీ ఇన్‌స్టాలేషన్ మరియు అన్‌ఇన్‌స్టాలేషన్ చేస్తారా?", "क्या आप एसी इंस्टॉलेशन और अनइंस्टॉलेशन करते हैं?"),
 'faq.3.a': ("Yes. We install new split and window ACs, safely remove ACs when you move, and help with reinstallation.",
             "అవును. కొత్త స్ప్లిట్ మరియు విండో ఏసీలు ఇన్‌స్టాల్ చేస్తాము, ఇల్లు మారేటప్పుడు ఏసీని సురక్షితంగా తొలగిస్తాము, మళ్ళీ అమర్చడంలో సహాయం చేస్తాము.",
             "हाँ। हम नए स्प्लिट और विंडो एसी लगाते हैं, घर बदलते समय एसी को सुरक्षित हटाते हैं और दोबारा लगाने में मदद करते हैं।"),
 'faq.4.q': ("Do you provide AC gas filling?", "మీరు ఏసీ గ్యాస్ ఫిల్లింగ్ చేస్తారా?", "क्या आप एसी गैस फिलिंग करते हैं?"),
 'faq.4.a': ("Yes. We first check for leaks and other causes of poor cooling, then fill gas only if the AC actually needs it.",
             "అవును. ముందుగా లీక్‌లు మరియు కూలింగ్ తగ్గడానికి ఇతర కారణాలను తనిఖీ చేసి, ఏసీకి నిజంగా అవసరమైతేనే గ్యాస్ నింపుతాము.",
             "हाँ। पहले हम लीक और कम कूलिंग के दूसरे कारणों की जाँच करते हैं, फिर एसी को सच में ज़रूरत होने पर ही गैस भरते हैं।"),
 'faq.5.q': ("How do I know whether my AC needs gas filling?", "నా ఏసీకి గ్యాస్ ఫిల్లింగ్ అవసరమా అని ఎలా తెలుసుకోవాలి?", "कैसे पता करें कि मेरे एसी को गैस फिलिंग चाहिए?"),
 'faq.5.a': ("Weak cooling, ice on the copper pipes or a hissing sound can point to low gas, but dirty filters and electrical faults cause similar symptoms. A technician needs to inspect the AC to confirm.",
             "కూలింగ్ తగ్గడం, కాపర్ పైపులపై మంచు లేదా బుస్ శబ్దం గ్యాస్ తక్కువగా ఉందని సూచించవచ్చు; కానీ మురికి ఫిల్టర్లు, ఎలక్ట్రికల్ లోపాలు కూడా ఇలాంటి లక్షణాలు చూపుతాయి. నిర్ధారించడానికి టెక్నీషియన్ ఏసీని తనిఖీ చేయాలి.",
             "कम ठंडक, कॉपर पाइप पर बर्फ़ या सीटी जैसी आवाज़ गैस कम होने का संकेत हो सकते हैं, लेकिन गंदे फ़िल्टर और इलेक्ट्रिकल खराबी से भी ऐसे ही लक्षण दिखते हैं। पुष्टि के लिए टेक्नीशियन को एसी की जाँच करनी होती है।"),
 'faq.6.q': ("Do you provide AC servicing and cleaning?", "మీరు ఏసీ సర్వీసింగ్ మరియు క్లీనింగ్ చేస్తారా?", "क्या आप एसी सर्विसिंग और सफ़ाई करते हैं?"),
 'faq.6.a': ("Yes. Servicing covers filter cleaning, indoor unit cleaning and an outdoor unit check. Deep cleaning is also available.",
             "అవును. సర్వీసింగ్‌లో ఫిల్టర్ క్లీనింగ్, ఇండోర్ యూనిట్ క్లీనింగ్ మరియు అవుట్‌డోర్ యూనిట్ చెకింగ్ ఉంటాయి. డీప్ క్లీనింగ్ కూడా అందుబాటులో ఉంది.",
             "हाँ। सर्विसिंग में फ़िल्टर की सफ़ाई, इनडोर यूनिट की सफ़ाई और आउटडोर यूनिट की जाँच शामिल है। डीप क्लीनिंग भी उपलब्ध है।"),
 'faq.7.q': ("Do you repair refrigerators?", "మీరు ఫ్రిజ్‌లు రిపేర్ చేస్తారా?", "क्या आप फ्रिज रिपेयर करते हैं?"),
 'faq.7.a': ("Yes. We repair refrigerators with cooling problems and other common faults.", "అవును. కూలింగ్ సమస్యలు మరియు ఇతర సాధారణ లోపాలున్న ఫ్రిజ్‌లను రిపేర్ చేస్తాము.", "हाँ। हम कूलिंग की समस्या और दूसरी आम खराबियों वाले फ्रिज रिपेयर करते हैं।"),
 'faq.8.q': ("Do you repair washing machines?", "మీరు వాషింగ్ మెషిన్లు రిపేర్ చేస్తారా?", "क्या आप वॉशिंग मशीन रिपेयर करते हैं?"),
 'faq.8.a': ("Yes, including drainage, spinning and other common washing machine problems.", "అవును. డ్రైనేజ్, స్పిన్నింగ్ మరియు ఇతర సాధారణ వాషింగ్ మెషిన్ సమస్యలతో సహా.", "हाँ, पानी निकासी, स्पिनिंग और दूसरी आम समस्याओं समेत।"),
 'faq.9.q': ("Do you provide air cooler and ceiling fan repair?", "మీరు ఎయిర్ కూలర్ మరియు సీలింగ్ ఫ్యాన్ రిపేర్ చేస్తారా?", "क्या आप एयर कूलर और सीलिंग फैन रिपेयर करते हैं?"),
 'faq.9.a': ("Yes. We repair air coolers and ceiling fans as well.", "అవును. ఎయిర్ కూలర్లు మరియు సీలింగ్ ఫ్యాన్లను కూడా రిపేర్ చేస్తాము.", "हाँ। हम एयर कूलर और सीलिंग फैन भी रिपेयर करते हैं।"),
 'faq.10.q': ("Which AC brands do you service?", "మీరు ఏ ఏసీ బ్రాండ్లకు సర్వీస్ చేస్తారు?", "आप किन एसी ब्रांड्स की सर्विस करते हैं?"),
 'faq.10.a': ("We service popular brands such as LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier and Voltas. We are an independent service provider, not an authorised brand service centre.",
              "LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier, Voltas వంటి ప్రముఖ బ్రాండ్లకు సర్వీస్ చేస్తాము. మేము స్వతంత్ర సర్వీస్ ప్రొవైడర్; బ్రాండ్ అధీకృత సర్వీస్ సెంటర్ కాదు.",
              "हम LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier और Voltas जैसे लोकप्रिय ब्रांड्स की सर्विस करते हैं। हम स्वतंत्र सर्विस प्रोवाइडर हैं, ब्रांड के अधिकृत सर्विस सेंटर नहीं।"),
 'faq.11.q': ("How can I book an AC technician?", "ఏసీ టెక్నీషియన్‌ను ఎలా బుక్ చేయాలి?", "एसी टेक्नीशियन कैसे बुक करें?"),
 'faq.11.a': ("Call +91 83748 89163, send us a WhatsApp message, or use the booking form on our Contact page.", "+91 83748 89163 కి కాల్ చేయండి, వాట్సాప్ మెసేజ్ పంపండి, లేదా మా కాంటాక్ట్ పేజీలోని బుకింగ్ ఫారం ఉపయోగించండి.", "+91 83748 89163 पर कॉल करें, व्हाट्सऐप मैसेज भेजें, या हमारे संपर्क पेज का बुकिंग फ़ॉर्म इस्तेमाल करें।"),
 'faq.12.q': ("Which locations do you cover?", "మీరు ఏ ప్రాంతాలకు సేవలు అందిస్తారు?", "आप किन इलाकों में सेवा देते हैं?"),
 'faq.12.a': ("Narasaraopet and surrounding areas within approximately 10 km. Call us to confirm your location.", "నరసరావుపేట మరియు సుమారు 10 కి.మీ. పరిధిలోని చుట్టుపక్కల ప్రాంతాలు. మీ ప్రాంతం కోసం కాల్ చేసి నిర్ధారించుకోండి.", "नरसरावपेट और लगभग 10 किमी के दायरे के आसपास के इलाके। अपने इलाके की पुष्टि के लिए हमें कॉल करें।"),
 'faq.13.q': ("How can I get a service estimate?", "సర్వీస్ అంచనా ఎలా పొందాలి?", "सर्विस का अनुमान कैसे मिलेगा?"),
 'faq.13.a': ("Share your appliance type, brand and problem by call or WhatsApp. The technician confirms the final estimate after inspecting the appliance and before starting any work.",
              "కాల్ లేదా వాట్సాప్ ద్వారా మీ ఉపకరణం రకం, బ్రాండ్ మరియు సమస్య తెలియజేయండి. ఉపకరణాన్ని తనిఖీ చేసిన తర్వాత, పని మొదలుపెట్టే ముందు టెక్నీషియన్ తుది అంచనాను నిర్ధారిస్తారు.",
              "कॉल या व्हाट्सऐप पर उपकरण का प्रकार, ब्रांड और समस्या बताएँ। टेक्नीशियन उपकरण की जाँच के बाद और काम शुरू करने से पहले अंतिम अनुमान बताते हैं।"),
})

# ---------- page heroes / meta ----------
add({
 'p.about.h1': ("About BOBBY AC Repair &amp; Home Appliance Services", "BOBBY AC Repair &amp; Home Appliance Services గురించి", "BOBBY AC Repair &amp; Home Appliance Services के बारे में"),
 'p.about.sub': ("A local AC and home appliance service provider in Narasaraopet.", "నరసరావుపేటలోని స్థానిక ఏసీ మరియు గృహోపకరణాల సర్వీస్ ప్రొవైడర్.", "नरसरावपेट का स्थानीय एसी और घरेलू उपकरण सर्विस प्रोवाइडर।"),
 'p.ac.h1': ("AC Repair &amp; Services in Narasaraopet", "నరసరావుపేటలో ఏసీ రిపేర్ &amp; సర్వీసులు", "नरसरावपेट में एसी रिपेयर और सर्विस"),
 'p.ac.sub': ("Repair, servicing, installation, uninstallation, gas filling and deep cleaning for split and window ACs.", "స్ప్లిట్ మరియు విండో ఏసీలకు రిపేర్, సర్వీసింగ్, ఇన్‌స్టాలేషన్, అన్‌ఇన్‌స్టాలేషన్, గ్యాస్ ఫిల్లింగ్ మరియు డీప్ క్లీనింగ్.", "स्प्लिट और विंडो एसी के लिए रिपेयर, सर्विसिंग, इंस्टॉलेशन, अनइंस्टॉलेशन, गैस फिलिंग और डीप क्लीनिंग।"),
 'p.app.h1': ("Home Appliance Repair in Narasaraopet", "నరసరావుపేటలో గృహోపకరణాల రిపేర్", "नरसरावपेट में घरेलू उपकरण रिपेयर"),
 'p.app.sub': ("Refrigerator, washing machine, air cooler and ceiling fan repair at your doorstep.", "ఇంటి వద్దకే ఫ్రిజ్, వాషింగ్ మెషిన్, ఎయిర్ కూలర్ మరియు సీలింగ్ ఫ్యాన్ రిపేర్.", "घर पर फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन रिपेयर।"),
 'p.brands.h1': ("Brands We Service", "మేము సర్వీస్ చేసే బ్రాండ్లు", "हम इन ब्रांड्स की सर्विस करते हैं"),
 'p.brands.sub': ("Independent multi-brand service for ACs and home appliances.", "ఏసీలు మరియు గృహోపకరణాలకు స్వతంత్ర మల్టీ-బ్రాండ్ సర్వీస్.", "एसी और घरेलू उपकरणों के लिए स्वतंत्र मल्टी-ब्रांड सर्विस।"),
 'p.faqs.h1': ("Frequently Asked Questions", "తరచుగా అడిగే ప్రశ్నలు", "अक्सर पूछे जाने वाले सवाल"),
 'p.faqs.sub': ("Straight answers about our AC and appliance services in Narasaraopet.", "నరసరావుపేటలో మా ఏసీ మరియు అప్లయెన్స్ సేవల గురించి సూటి సమాధానాలు.", "नरसरावपेट में हमारी एसी और अप्लायंस सेवाओं के बारे में सीधे जवाब।"),
 'p.contact.h1': ("Contact &amp; Book a Service", "సంప్రదించండి &amp; సర్వీస్ బుక్ చేయండి", "संपर्क करें और सर्विस बुक करें"),
 'p.contact.sub': ("Call, WhatsApp or send your details with the form below.", "కాల్, వాట్సాప్ చేయండి లేదా కింది ఫారం ద్వారా మీ వివరాలు పంపండి.", "कॉल, व्हाट्सऐप करें या नीचे दिए फ़ॉर्म से अपनी जानकारी भेजें।"),
 'p.blog.h1': ("Knowledge Centre", "నాలెడ్జ్ సెంటర్", "नॉलेज सेंटर"),
 'p.blog.sub': ("Practical guides on AC and home appliance care.", "ఏసీ మరియు గృహోపకరణాల సంరక్షణపై ఉపయోగకరమైన గైడ్‌లు.", "एसी और घरेलू उपकरणों की देखभाल पर उपयोगी गाइड।"),
 'p.privacy.h1': ("Privacy Policy", "గోప్యతా విధానం", "गोपनीयता नीति"),
 'p.terms.h1': ("Terms &amp; Conditions", "నిబంధనలు &amp; షరతులు", "नियम और शर्तें"),
 'p.sitemap.h1': ("Sitemap", "సైట్‌మ్యాప్", "साइटमैप"),
 'p.404.h1': ("Page not found", "పేజీ కనుగొనబడలేదు", "पेज नहीं मिला"),
 'p.404.sub': ("The page you are looking for may have moved. Try the links below or call us.", "మీరు వెతుకుతున్న పేజీ మారి ఉండవచ్చు. కింది లింకులు ప్రయత్నించండి లేదా మాకు కాల్ చేయండి.", "आप जो पेज ढूँढ रहे हैं वह हट गया होगा। नीचे दिए लिंक देखें या हमें कॉल करें।"),
})

# ---------- about ----------
add({
 'about.who.h': ("Who we are", "మేము ఎవరం", "हम कौन हैं"),
 'about.who.p1': ("BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES is a local service provider based in Narasaraopet, Andhra Pradesh. Our main work is AC repair, servicing, installation, uninstallation and gas filling for split and window ACs.",
                  "BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES ఆంధ్రప్రదేశ్‌లోని నరసరావుపేటలో ఉన్న స్థానిక సర్వీస్ ప్రొవైడర్. స్ప్లిట్ మరియు విండో ఏసీలకు రిపేర్, సర్వీసింగ్, ఇన్‌స్టాలేషన్, అన్‌ఇన్‌స్టాలేషన్ మరియు గ్యాస్ ఫిల్లింగ్ మా ప్రధాన పని.",
                  "BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES आंध्र प्रदेश के नरसरावपेट में स्थित एक स्थानीय सर्विस प्रोवाइडर है। स्प्लिट और विंडो एसी की रिपेयर, सर्विसिंग, इंस्टॉलेशन, अनइंस्टॉलेशन और गैस फिलिंग हमारा मुख्य काम है।"),
 'about.who.p2': ("We also repair refrigerators, washing machines, air coolers and ceiling fans, so families can call one trusted local number for most home appliance problems.",
                  "ఫ్రిజ్‌లు, వాషింగ్ మెషిన్లు, ఎయిర్ కూలర్లు మరియు సీలింగ్ ఫ్యాన్లను కూడా రిపేర్ చేస్తాము; అందువల్ల చాలా గృహోపకరణాల సమస్యలకు కుటుంబాలు ఒకే నమ్మకమైన లోకల్ నంబర్‌కు కాల్ చేయవచ్చు.",
                  "हम फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन भी रिपेयर करते हैं, ताकि परिवार ज़्यादातर घरेलू उपकरणों की समस्या के लिए एक भरोसेमंद लोकल नंबर पर कॉल कर सकें।"),
 'about.how.h': ("How we work", "మేము ఎలా పనిచేస్తాము", "हम कैसे काम करते हैं"),
 'about.how.1': ("<b>Inspect first.</b> We find the actual cause before suggesting any repair or part.", "<b>ముందు తనిఖీ.</b> ఏ రిపేర్ లేదా విడిభాగం సూచించే ముందు అసలు కారణం కనుగొంటాము.", "<b>पहले जाँच।</b> कोई रिपेयर या पार्ट सुझाने से पहले हम असली कारण ढूँढते हैं।"),
 'about.how.2': ("<b>Explain clearly.</b> You hear what is wrong in simple words.", "<b>స్పష్టంగా వివరణ.</b> సమస్య ఏమిటో సులభమైన మాటల్లో చెబుతాము.", "<b>साफ़ जानकारी।</b> क्या ख़राब है, यह आसान शब्दों में बताते हैं।"),
 'about.how.3': ("<b>Estimate before work.</b> Nothing starts until you agree to the cost.", "<b>పనికి ముందే అంచనా.</b> మీరు ఖర్చుకు అంగీకరించే వరకు పని మొదలవదు.", "<b>काम से पहले अनुमान।</b> आपकी सहमति के बिना कोई काम शुरू नहीं होता।"),
 'about.how.4': ("<b>Test before we leave.</b> We check the appliance is working after the job.", "<b>వెళ్ళే ముందు టెస్ట్.</b> పని తర్వాత ఉపకరణం సరిగా పనిచేస్తుందో చూస్తాము.", "<b>जाने से पहले टेस्ट।</b> काम के बाद जाँचते हैं कि उपकरण ठीक चल रहा है।"),
 'about.area.h': ("Where we work", "మేము ఎక్కడ పనిచేస్తాము", "हम कहाँ काम करते हैं"),
 'about.area.p': ("We serve homes in Narasaraopet and nearby areas within approximately 10 km. If you are just outside this range, call us and we will tell you honestly whether we can reach you.",
                  "నరసరావుపేట మరియు సుమారు 10 కి.మీ. లోపు సమీప ప్రాంతాల్లోని ఇళ్లకు సేవలు అందిస్తాము. మీరు కొంచెం బయట ఉంటే, కాల్ చేయండి; మేము రాగలమో లేదో నిజాయితీగా చెబుతాము.",
                  "हम नरसरावपेट और लगभग 10 किमी के भीतर आसपास के घरों में सेवा देते हैं। अगर आप थोड़ा बाहर हैं, तो कॉल करें, हम ईमानदारी से बताएँगे कि हम पहुँच सकते हैं या नहीं।"),
})

# ---------- contact / form ----------
add({
 'c.call.h': ("Call us", "మాకు కాల్ చేయండి", "हमें कॉल करें"),
 'c.wa.h': ("WhatsApp booking", "వాట్సాప్ బుకింగ్", "व्हाट्सऐप बुकिंग"),
 'c.loc.h': ("Location", "ప్రాంతం", "लोकेशन"),
 'c.area.h': ("Service area", "సర్వీస్ ప్రాంతం", "सर्विस क्षेत्र"),
 'c.area.v': ("Narasaraopet + about 10 km", "నరసరావుపేట + సుమారు 10 కి.మీ.", "नरसरावपेट + लगभग 10 किमी"),
 'f.h': ("Service Booking Form", "సర్వీస్ బుకింగ్ ఫారం", "सर्विस बुकिंग फ़ॉर्म"),
 'f.note': ("This form does not store your details. It opens WhatsApp with your booking message ready, so you can review and send it to us.",
            "ఈ ఫారం మీ వివరాలను సేవ్ చేయదు. మీ బుకింగ్ మెసేజ్‌తో వాట్సాప్ తెరుచుకుంటుంది; చూసుకుని మాకు పంపవచ్చు.",
            "यह फ़ॉर्म आपकी जानकारी सेव नहीं करता। यह आपके बुकिंग मैसेज के साथ व्हाट्सऐप खोलता है, ताकि आप देखकर हमें भेज सकें।"),
 'f.name': ("Your name", "మీ పేరు", "आपका नाम"),
 'f.phone': ("Mobile number", "మొబైల్ నంబర్", "मोबाइल नंबर"),
 'f.appliance': ("Appliance", "ఉపకరణం", "उपकरण"),
 'f.service': ("Service needed", "అవసరమైన సర్వీస్", "ज़रूरी सर्विस"),
 'f.area': ("Area / landmark in Narasaraopet", "నరసరావుపేటలో ప్రాంతం / ల్యాండ్‌మార్క్", "नरसरावपेट में इलाका / लैंडमार्क"),
 'f.brand': ("Brand (optional)", "బ్రాండ్ (ఐచ్ఛికం)", "ब्रांड (वैकल्पिक)"),
 'f.date': ("Preferred date (optional)", "కావలసిన తేదీ (ఐచ్ఛికం)", "पसंदीदा तारीख़ (वैकल्पिक)"),
 'f.msg': ("Describe the problem (optional)", "సమస్యను వివరించండి (ఐచ్ఛికం)", "समस्या बताएँ (वैकल्पिक)"),
 'f.ph.name': ("Full name", "పూర్తి పేరు", "पूरा नाम"),
 'f.ph.phone': ("10-digit mobile number", "10 అంకెల మొబైల్ నంబర్", "10 अंकों का मोबाइल नंबर"),
 'f.ph.area': ("Colony, street or landmark", "కాలనీ, వీధి లేదా ల్యాండ్‌మార్క్", "कॉलोनी, गली या लैंडमार्क"),
 'f.ph.brand': ("e.g. your appliance brand", "ఉదా: మీ ఉపకరణ బ్రాండ్", "जैसे: आपके उपकरण का ब्रांड"),
 'f.ph.msg': ("e.g. AC not cooling since yesterday", "ఉదా: నిన్నటి నుండి ఏసీ చల్లబడట్లేదు", "जैसे: कल से एसी ठंडा नहीं कर रहा"),
 'f.select': ("Select", "ఎంచుకోండి", "चुनें"),
 'f.opt.splitac': ("Split AC", "స్ప్లిట్ ఏసీ", "स्प्लिट एसी"),
 'f.opt.windowac': ("Window AC", "విండో ఏసీ", "विंडो एसी"),
 'f.opt.fridge': ("Refrigerator", "ఫ్రిజ్", "फ्रिज"),
 'f.opt.washer': ("Washing machine", "వాషింగ్ మెషిన్", "वॉशिंग मशीन"),
 'f.opt.cooler': ("Air cooler", "ఎయిర్ కూలర్", "एयर कूलर"),
 'f.opt.fan': ("Ceiling fan", "సీలింగ్ ఫ్యాన్", "सीलिंग फैन"),
 'f.opt.repair': ("Repair", "రిపేర్", "रिपेयर"),
 'f.opt.service': ("Servicing / cleaning", "సర్వీసింగ్ / క్లీనింగ్", "सर्विसिंग / सफ़ाई"),
 'f.opt.install': ("Installation", "ఇన్‌స్టాలేషన్", "इंस्टॉलेशन"),
 'f.opt.uninstall': ("Uninstallation", "అన్‌ఇన్‌స్టాలేషన్", "अनइंस्टॉलेशन"),
 'f.opt.gas': ("Gas filling check", "గ్యాస్ ఫిల్లింగ్ చెక్", "गैस फिलिंग जाँच"),
 'f.opt.notsure': ("Not sure, need inspection", "తెలియదు, తనిఖీ కావాలి", "पता नहीं, जाँच चाहिए"),
 'f.submit': ("Send Booking on WhatsApp", "వాట్సాప్‌లో బుకింగ్ పంపండి", "व्हाट्सऐप पर बुकिंग भेजें"),
 'f.err.req': ("Please fill in this field.", "దయచేసి ఈ ఫీల్డ్ నింపండి.", "कृपया यह जानकारी भरें।"),
 'f.err.phone': ("Please enter a valid 10-digit Indian mobile number.", "దయచేసి సరైన 10 అంకెల మొబైల్ నంబర్ ఇవ్వండి.", "कृपया सही 10 अंकों का मोबाइल नंबर डालें।"),
 'f.ok': ("Opening WhatsApp… tap Send to confirm your booking.", "వాట్సాప్ తెరుచుకుంటోంది… బుకింగ్ కోసం సెండ్ నొక్కండి.", "व्हाट्सऐप खुल रहा है… बुकिंग के लिए भेजें दबाएँ।"),
 'f.wa.title': ("New service booking", "కొత్త సర్వీస్ బుకింగ్", "नई सर्विस बुकिंग"),
})

# ---------- footer ----------
add({
 'ft.about': ("Local doorstep AC repair, servicing, installation and home appliance repair in Narasaraopet, Andhra Pradesh.",
              "నరసరావుపేట, ఆంధ్రప్రదేశ్‌లో ఇంటి వద్దకే ఏసీ రిపేర్, సర్వీసింగ్, ఇన్‌స్టాలేషన్ మరియు గృహోపకరణాల రిపేర్.",
              "नरसरावपेट, आंध्र प्रदेश में घर पर एसी रिपेयर, सर्विसिंग, इंस्टॉलेशन और घरेलू उपकरण रिपेयर।"),
 'ft.quick': ("Quick Links", "త్వరిత లింకులు", "क्विक लिंक्स"),
 'ft.ac': ("AC Services", "ఏసీ సేవలు", "एसी सेवाएँ"),
 'ft.contact': ("Contact", "సంప్రదింపు", "संपर्क"),
 'ft.maint': ("AC Maintenance", "ఏసీ మెయింటెనెన్స్", "एसी मेंटेनेंस"),
 'ft.area': ("Serving Narasaraopet and nearby areas within about 10 km.", "నరసరావుపేట మరియు సుమారు 10 కి.మీ. లోపు సమీప ప్రాంతాలకు సేవలు.", "नरसरावपेट और लगभग 10 किमी के भीतर आसपास के इलाकों में सेवा।"),
 'ft.rights': ("All rights reserved.", "సర్వ హక్కులు ప్రత్యేకించబడ్డాయి.", "सर्वाधिकार सुरक्षित।"),
 'ft.privacy': ("Privacy Policy", "గోప్యతా విధానం", "गोपनीयता नीति"),
 'ft.terms': ("Terms &amp; Conditions", "నిబంధనలు &amp; షరతులు", "नियम और शर्तें"),
 'ft.sitemap': ("Sitemap", "సైట్‌మ్యాప్", "साइटमैप"),
 'ft.indep': ("Independent multi-brand service provider. Not an authorised service centre of any brand.", "స్వతంత్ర మల్టీ-బ్రాండ్ సర్వీస్ ప్రొవైడర్. ఏ బ్రాండ్‌కూ అధీకృత సర్వీస్ సెంటర్ కాదు.", "स्वतंत्र मल्टी-ब्रांड सर्विस प्रोवाइडर। किसी भी ब्रांड का अधिकृत सर्विस सेंटर नहीं।"),
})

# ---------- legal ----------
add({
 'priv.body': ("""<p>This website is run by BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES, Narasaraopet, Andhra Pradesh. We respect your privacy and collect as little information as possible.</p>
<h2>What we collect</h2><p>The website does not have user accounts and does not store your booking details on a server. When you use the booking form, your details are placed into a WhatsApp message on your own device. Nothing is sent until you choose to send it.</p>
<h2>How we use your details</h2><p>Information you send by phone or WhatsApp (such as your name, number, area and appliance problem) is used only to arrange and carry out your service. We do not sell or share it for marketing.</p>
<h2>Third-party services</h2><p>The site loads fonts from Google Fonts, and a map from Google Maps. These services may receive basic technical information such as your IP address. WhatsApp is governed by its own privacy policy.</p>
<h2>Your language choice</h2><p>We save your chosen language in your browser so the site remembers it. You can clear it at any time from your browser settings.</p>
<h2>Contact</h2><p>For any privacy question, call or WhatsApp +91 83748 89163.</p>""",
"""<p>ఈ వెబ్‌సైట్‌ను నరసరావుపేట, ఆంధ్రప్రదేశ్‌లోని BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES నిర్వహిస్తుంది. మేము మీ గోప్యతను గౌరవిస్తాము మరియు వీలైనంత తక్కువ సమాచారం మాత్రమే సేకరిస్తాము.</p>
<h2>మేము ఏమి సేకరిస్తాము</h2><p>ఈ వెబ్‌సైట్‌లో యూజర్ అకౌంట్లు లేవు; మీ బుకింగ్ వివరాలను సర్వర్‌లో సేవ్ చేయదు. బుకింగ్ ఫారం ఉపయోగించినప్పుడు, మీ వివరాలు మీ ఫోన్‌లోనే వాట్సాప్ మెసేజ్‌గా సిద్ధమవుతాయి. మీరు పంపే వరకు ఏదీ పంపబడదు.</p>
<h2>మీ వివరాలను ఎలా ఉపయోగిస్తాము</h2><p>ఫోన్ లేదా వాట్సాప్ ద్వారా మీరు ఇచ్చే సమాచారం (పేరు, నంబర్, ప్రాంతం, ఉపకరణ సమస్య) మీ సర్వీస్‌ను ఏర్పాటు చేసి పూర్తి చేయడానికి మాత్రమే ఉపయోగిస్తాము. మార్కెటింగ్ కోసం అమ్మము లేదా పంచుకోము.</p>
<h2>ఇతర సేవలు</h2><p>ఈ సైట్ Google Fonts నుండి ఫాంట్లు, Google Maps నుండి మ్యాప్‌ను లోడ్ చేస్తుంది. ఈ సేవలకు మీ IP అడ్రస్ వంటి ప్రాథమిక సాంకేతిక సమాచారం చేరవచ్చు. వాట్సాప్‌కు దాని స్వంత గోప్యతా విధానం వర్తిస్తుంది.</p>
<h2>మీ భాష ఎంపిక</h2><p>మీరు ఎంచుకున్న భాషను సైట్ గుర్తుంచుకోవడానికి మీ బ్రౌజర్‌లో సేవ్ చేస్తాము. బ్రౌజర్ సెట్టింగ్స్ నుండి ఎప్పుడైనా తొలగించవచ్చు.</p>
<h2>సంప్రదింపు</h2><p>గోప్యతకు సంబంధించిన ఏ ప్రశ్నకైనా +91 83748 89163 కి కాల్ లేదా వాట్సాప్ చేయండి.</p>""",
"""<p>यह वेबसाइट नरसरावपेट, आंध्र प्रदेश के BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES द्वारा चलाई जाती है। हम आपकी निजता का सम्मान करते हैं और जितनी कम हो सके उतनी जानकारी लेते हैं।</p>
<h2>हम क्या लेते हैं</h2><p>इस वेबसाइट पर कोई यूज़र अकाउंट नहीं है और यह आपकी बुकिंग जानकारी सर्वर पर सेव नहीं करती। बुकिंग फ़ॉर्म इस्तेमाल करने पर आपकी जानकारी आपके ही फ़ोन पर व्हाट्सऐप मैसेज में भर जाती है। जब तक आप भेजें नहीं, कुछ नहीं जाता।</p>
<h2>हम जानकारी का उपयोग कैसे करते हैं</h2><p>फ़ोन या व्हाट्सऐप पर दी गई जानकारी (नाम, नंबर, इलाका, उपकरण की समस्या) सिर्फ़ आपकी सर्विस तय करने और पूरी करने के लिए इस्तेमाल होती है। हम इसे मार्केटिंग के लिए न बेचते हैं न साझा करते हैं।</p>
<h2>तीसरे पक्ष की सेवाएँ</h2><p>साइट Google Fonts से फ़ॉन्ट, Google Maps से नक्शा लोड करती है। इन सेवाओं को आपका IP पता जैसी बुनियादी तकनीकी जानकारी मिल सकती है। व्हाट्सऐप पर उसकी अपनी गोपनीयता नीति लागू होती है।</p>
<h2>आपकी भाषा</h2><p>आपकी चुनी हुई भाषा आपके ब्राउज़र में सेव होती है ताकि साइट उसे याद रखे। आप इसे कभी भी ब्राउज़र सेटिंग्स से हटा सकते हैं।</p>
<h2>संपर्क</h2><p>गोपनीयता से जुड़े किसी भी सवाल के लिए +91 83748 89163 पर कॉल या व्हाट्सऐप करें।</p>"""),
 'terms.body': ("""<p>By using this website or booking a service with BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES, you agree to these terms.</p>
<h2>Bookings</h2><p>A booking request by phone, WhatsApp or the website form is confirmed only when we reply with a visit time. Visit times depend on availability and location.</p>
<h2>Inspection and estimates</h2><p>The technician inspects the appliance first. Any price shown on this website is a starting price; the final estimate is shared with you before work begins, and work starts only with your approval.</p>
<h2>Parts</h2><p>If a part needs replacing, we explain why and confirm the cost with you first. Availability of parts can vary by brand and model.</p>
<h2>Independent service</h2><p>BOBBY is an independent service provider and is not an authorised service centre of any brand. Repairs by an independent provider may affect a manufacturer's warranty; please check your warranty terms before booking.</p>
<h2>Payment</h2><p>Payment is due when the agreed work is completed.</p>
<h2>Website content</h2><p>Articles on this site are general guidance, not a substitute for an inspection by a technician. Please do not open electrical parts of appliances yourself.</p>
<h2>Contact</h2><p>Questions about these terms: +91 83748 89163.</p>""",
"""<p>ఈ వెబ్‌సైట్ ఉపయోగించడం లేదా BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES తో సర్వీస్ బుక్ చేయడం ద్వారా మీరు ఈ నిబంధనలకు అంగీకరిస్తున్నారు.</p>
<h2>బుకింగ్‌లు</h2><p>ఫోన్, వాట్సాప్ లేదా వెబ్‌సైట్ ఫారం ద్వారా చేసిన బుకింగ్ అభ్యర్థన, మేము విజిట్ సమయంతో సమాధానం ఇచ్చినప్పుడే నిర్ధారించబడుతుంది. విజిట్ సమయాలు లభ్యత మరియు ప్రాంతంపై ఆధారపడి ఉంటాయి.</p>
<h2>తనిఖీ మరియు అంచనాలు</h2><p>టెక్నీషియన్ ముందుగా ఉపకరణాన్ని తనిఖీ చేస్తారు. ఈ వెబ్‌సైట్‌లో చూపిన ధరలు ప్రారంభ ధరలు మాత్రమే; తుది అంచనా పని మొదలయ్యే ముందే మీకు తెలియజేయబడుతుంది, మీ ఆమోదంతోనే పని మొదలవుతుంది.</p>
<h2>విడిభాగాలు</h2><p>ఏదైనా విడిభాగం మార్చాల్సి వస్తే, ఎందుకో వివరించి ముందుగా ఖర్చు నిర్ధారిస్తాము. విడిభాగాల లభ్యత బ్రాండ్ మరియు మోడల్‌ను బట్టి మారవచ్చు.</p>
<h2>స్వతంత్ర సేవ</h2><p>BOBBY ఒక స్వతంత్ర సర్వీస్ ప్రొవైడర్; ఏ బ్రాండ్‌కూ అధీకృత సర్వీస్ సెంటర్ కాదు. స్వతంత్ర ప్రొవైడర్ చేసే రిపేర్లు తయారీదారు వారంటీపై ప్రభావం చూపవచ్చు; బుక్ చేసే ముందు మీ వారంటీ నిబంధనలు చూసుకోండి.</p>
<h2>చెల్లింపు</h2><p>అంగీకరించిన పని పూర్తయిన తర్వాత చెల్లింపు చేయాలి.</p>
<h2>వెబ్‌సైట్ విషయం</h2><p>ఈ సైట్‌లోని వ్యాసాలు సాధారణ మార్గదర్శకం మాత్రమే; టెక్నీషియన్ తనిఖీకి ప్రత్యామ్నాయం కాదు. దయచేసి ఉపకరణాల ఎలక్ట్రికల్ భాగాలను మీరే తెరవకండి.</p>
<h2>సంప్రదింపు</h2><p>ఈ నిబంధనలపై ప్రశ్నలకు: +91 83748 89163.</p>""",
"""<p>इस वेबसाइट का उपयोग करके या BOBBY AC REPAIR &amp; HOME APPLIANCE SERVICES से सर्विस बुक करके आप इन शर्तों से सहमत होते हैं।</p>
<h2>बुकिंग</h2><p>फ़ोन, व्हाट्सऐप या वेबसाइट फ़ॉर्म से भेजा गया बुकिंग अनुरोध तभी पक्का होता है जब हम विज़िट का समय बताकर जवाब देते हैं। विज़िट का समय उपलब्धता और लोकेशन पर निर्भर करता है।</p>
<h2>जाँच और अनुमान</h2><p>टेक्नीशियन पहले उपकरण की जाँच करते हैं। इस वेबसाइट पर दिखाई गई कीमतें शुरुआती कीमतें हैं; अंतिम अनुमान काम शुरू होने से पहले बताया जाता है और आपकी मंज़ूरी के बाद ही काम शुरू होता है।</p>
<h2>पार्ट्स</h2><p>अगर कोई पार्ट बदलना हो, तो हम कारण बताकर पहले खर्च की पुष्टि करते हैं। पार्ट्स की उपलब्धता ब्रांड और मॉडल के अनुसार बदल सकती है।</p>
<h2>स्वतंत्र सेवा</h2><p>BOBBY एक स्वतंत्र सर्विस प्रोवाइडर है और किसी भी ब्रांड का अधिकृत सर्विस सेंटर नहीं है। स्वतंत्र प्रोवाइडर की रिपेयर से निर्माता की वारंटी प्रभावित हो सकती है; बुकिंग से पहले अपनी वारंटी की शर्तें देख लें।</p>
<h2>भुगतान</h2><p>तय काम पूरा होने पर भुगतान करना होता है।</p>
<h2>वेबसाइट सामग्री</h2><p>इस साइट के लेख सामान्य जानकारी हैं, टेक्नीशियन की जाँच का विकल्प नहीं। कृपया उपकरणों के इलेक्ट्रिकल हिस्से ख़ुद न खोलें।</p>
<h2>संपर्क</h2><p>इन शर्तों पर सवाल के लिए: +91 83748 89163।</p>"""),
})

add({
 'addr.full': ("Door 11-28-32/5, Employees Colony, Isha Zen Enclave, Palapadu Road, Arundelpet, Narasaraopeta, Andhra Pradesh 522601",)*3,
 'hours.open': ("Open 24 hours", "24 గంటలూ అందుబాటులో", "24 घंटे खुला"),
 'c.hours.h': ("Working hours", "పని వేళలు", "काम के घंटे"),
 'btn.dir': ("Get Directions", "దారి చూపించు", "रास्ता देखें"),
 'btn.maps': ("View on Google Maps", "గూగుల్ మ్యాప్స్‌లో చూడండి", "गूगल मैप्स पर देखें"),
 'rev.google': ("Write a Google Review", "గూగుల్ రివ్యూ రాయండి", "गूगल रिव्यू लिखें"),
 'rev.first': ("Be one of our first Google reviewers. Your honest feedback helps other families in Narasaraopet choose with confidence.", "మా మొదటి గూగుల్ రివ్యూయర్లలో ఒకరు కండి. మీ నిజాయితీ అభిప్రాయం నరసరావుపేటలోని ఇతర కుటుంబాలకు నమ్మకంగా ఎంచుకోవడానికి సహాయపడుతుంది.", "हमारे पहले गूगल रिव्यूअर्स में से एक बनें। आपकी सच्ची राय नरसरावपेट के दूसरे परिवारों को भरोसे से चुनने में मदद करती है।"),
 'rev.read': ("Read all reviews on Google", "అన్ని రివ్యూలు గూగుల్‌లో చదవండి", "सभी रिव्यू गूगल पर पढ़ें"),
 'brands.banner': ("We repair and service these popular brands", "ఈ ప్రముఖ బ్రాండ్లను మేము రిపేర్ మరియు సర్వీస్ చేస్తాము", "हम इन लोकप्रिय ब्रांड्स की रिपेयर और सर्विस करते हैं"),
})

# ---------- booking: location + modal ----------
add({
 'btn.bookservice': ("Book Service", "సర్వీస్ బుక్ చేయండి", "सर्विस बुक करें"),
 'mbar.book': ("Book Service", "బుక్ చేయండి", "बुक करें"),
 'f.close': ("Close", "మూసివేయండి", "बंद करें"),
 'f.loc': ("Your location (helps the technician reach you)", "మీ లొకేషన్ (టెక్నీషియన్ మీ దగ్గరకు రావడానికి)", "आपकी लोकेशन (टेक्नीशियन को पहुँचने में मदद)"),
 'f.loc.cur': ("Use my current location", "నా ప్రస్తుత లొకేషన్", "मेरी मौजूदा लोकेशन"),
 'f.loc.map': ("Choose on map", "మ్యాప్‌లో ఎంచుకోండి", "मैप पर चुनें"),
 'f.loc.getting': ("Getting your location…", "మీ లొకేషన్ తీసుకుంటోంది…", "आपकी लोकेशन ली जा रही है…"),
 'f.loc.ok': ("Location added", "లొకేషన్ జోడించబడింది", "लोकेशन जुड़ गई"),
 'f.loc.view': ("View on map", "మ్యాప్‌లో చూడండి", "मैप पर देखें"),
 'f.loc.clear': ("Remove", "తీసివేయండి", "हटाएँ"),
 'f.loc.denied': ("Location access is blocked. Allow location for this site in your browser, or choose on the map.", "లొకేషన్ అనుమతి నిరాకరించబడింది. బ్రౌజర్‌లో ఈ సైట్‌కు లొకేషన్ అనుమతించండి, లేదా మ్యాప్‌లో ఎంచుకోండి.", "लोकेशन की अनुमति बंद है। ब्राउज़र में इस साइट के लिए लोकेशन चालू करें, या मैप पर चुनें।"),
 'f.loc.fail': ("Couldn't get your location. Please choose it on the map.", "మీ లొకేషన్ దొరకలేదు. దయచేసి మ్యాప్‌లో ఎంచుకోండి.", "आपकी लोकेशन नहीं मिल सकी। कृपया मैप पर चुनें।"),
 'f.loc.note': ("Optional. Your location is shared only when you send the WhatsApp message.", "ఐచ్ఛికం. మీరు వాట్సాప్ మెసేజ్ పంపినప్పుడు మాత్రమే మీ లొకేషన్ షేర్ అవుతుంది.", "वैकल्पिक। आपकी लोकेशन सिर्फ़ तब जाती है जब आप व्हाट्सऐप मैसेज भेजते हैं।"),
 'f.wa.loc': ("Location", "లొకేషన్", "लोकेशन"),
 'map.title': ("Choose your location", "మీ లొకేషన్ ఎంచుకోండి", "अपनी लोकेशन चुनें"),
 'map.hint': ("Tap the map to drop a pin, then drag it exactly onto your house.", "మ్యాప్‌పై నొక్కి పిన్ పెట్టండి, తర్వాత దాన్ని సరిగ్గా మీ ఇంటిపైకి లాగండి.", "मैप पर टैप करके पिन लगाएँ, फिर उसे ठीक अपने घर पर खींचें।"),
 'map.search': ("Search colony, street or landmark", "కాలనీ, వీధి లేదా ల్యాండ్‌మార్క్ వెతకండి", "कॉलोनी, गली या लैंडमार्क खोजें"),
 'map.go': ("Search", "వెతకండి", "खोजें"),
 'map.use': ("Use this location", "ఈ లొకేషన్ ఉపయోగించండి", "यह लोकेशन चुनें"),
 'map.me': ("My location", "నా లొకేషన్", "मेरी लोकेशन"),
 'map.noresult': ("No place found. Try a nearby landmark, or move the map and tap.", "ప్రదేశం దొరకలేదు. దగ్గరలోని ల్యాండ్‌మార్క్ ప్రయత్నించండి, లేదా మ్యాప్ కదిలించి నొక్కండి.", "जगह नहीं मिली। पास का लैंडमार्क आज़माएँ, या मैप खिसकाकर टैप करें।"),
})
_loc = {
 'en': '<h2>Location</h2><p>If you tap “Use my current location” or pick a point on the map, the location stays in the booking form on your device. It is added to your WhatsApp message as a map link and reaches us only if you send that message. The map is provided by OpenStreetMap.</p>\n<h2>Contact</h2>',
 'te': '<h2>లొకేషన్</h2><p>మీరు “నా ప్రస్తుత లొకేషన్” నొక్కినా లేదా మ్యాప్‌లో ఒక ప్రదేశాన్ని ఎంచుకున్నా, ఆ లొకేషన్ మీ ఫోన్‌లోని బుకింగ్ ఫారంలోనే ఉంటుంది. అది మ్యాప్ లింక్‌గా మీ వాట్సాప్ మెసేజ్‌లో జోడించబడుతుంది; మీరు ఆ మెసేజ్ పంపితేనే మాకు చేరుతుంది. మ్యాప్ OpenStreetMap ద్వారా అందించబడుతుంది.</p>\n<h2>సంప్రదింపు</h2>',
 'hi': '<h2>लोकेशन</h2><p>अगर आप “मेरी मौजूदा लोकेशन” दबाते हैं या मैप पर कोई जगह चुनते हैं, तो लोकेशन आपके ही फ़ोन पर बुकिंग फ़ॉर्म में रहती है। यह मैप लिंक के रूप में आपके व्हाट्सऐप मैसेज में जुड़ती है और हमें तभी मिलती है जब आप वह मैसेज भेजते हैं। मैप OpenStreetMap द्वारा दिया जाता है।</p>\n<h2>संपर्क</h2>',
}
_pv = list(S['priv.body'])
for i, (l, head) in enumerate([('en', '<h2>Contact</h2>'), ('te', '<h2>సంప్రదింపు</h2>'), ('hi', '<h2>संपर्क</h2>')]):
    assert head in _pv[i]
    _pv[i] = _pv[i].replace(head, _loc[l], 1)
S['priv.body'] = tuple(_pv)

add({
 'stat.cust': ("Happy Customers", "సంతోషకరమైన కస్టమర్లు", "संतुष्ट ग्राहक"),
 'stat.years': ("Years Experience", "సంవత్సరాల అనుభవం", "साल का अनुभव"),
 'stat.brands': ("Brands Serviced", "బ్రాండ్లకు సర్వీస్", "ब्रांड्स की सर्विस"),
 'stat.support': ("Emergency Support", "అత్యవసర సహాయం", "इमरजेंसी सपोर्ट"),
})
S['rev.eyebrow'] = ("Customer Reviews", "కస్టమర్ రివ్యూలు", "ग्राहक रिव्यू")
S['rev.h2'] = ("What Our Customers Say", "మా కస్టమర్లు ఏమంటున్నారు", "हमारे ग्राहक क्या कहते हैं")

# ---------- trust carousel (facts about the service, not customer quotes) ----------
add({
 'tr.eyebrow': ("Why Narasaraopet trusts BOBBY", "నరసరావుపేట BOBBY ని ఎందుకు నమ్ముతుంది", "नरसरावपेट BOBBY पर क्यों भरोसा करता है"),
 'tr.h2': ("Why Families Call BOBBY", "కుటుంబాలు BOBBY కి ఎందుకు కాల్ చేస్తాయి", "परिवार BOBBY को क्यों बुलाते हैं"),
 'tr.1.t': ("Open 24 hours", "24 గంటలూ అందుబాటులో", "24 घंटे खुला"),
 'tr.1.d': ("Breakdowns don't wait. Call us any time, day or night.", "బ్రేక్‌డౌన్ ఎప్పుడైనా రావచ్చు. పగలు రాత్రి ఎప్పుడైనా కాల్ చేయండి.", "खराबी कभी भी आ सकती है। दिन हो या रात, कभी भी कॉल करें।"),
 'tr.2.t': ("Quick doorstep response", "త్వరిత ఇంటి వద్ద సేవ", "घर पर तुरंत सेवा"),
 'tr.2.d': ("We come to your home anywhere in Narasaraopet and within about 10 km.", "నరసరావుపేట మరియు సుమారు 10 కి.మీ. లోపు ఎక్కడైనా మీ ఇంటికే వస్తాము.", "नरसरावपेट और लगभग 10 किमी के भीतर कहीं भी हम आपके घर आते हैं।"),
 'tr.3.t': ("Inspection first", "ముందు తనిఖీ", "पहले जाँच"),
 'tr.3.d': ("We find the real cause before suggesting any repair or part.", "ఏ రిపేర్ లేదా విడిభాగం సూచించే ముందు అసలు కారణం కనుగొంటాము.", "कोई रिपेयर या पार्ट सुझाने से पहले असली कारण ढूँढते हैं।"),
 'tr.4.t': ("Estimate before work", "పనికి ముందే అంచనా", "काम से पहले अनुमान"),
 'tr.4.d': ("You approve the cost before any work begins. No surprises.", "ఏ పని మొదలయ్యే ముందే ఖర్చును మీరు ఆమోదిస్తారు. ఆశ్చర్యాలు ఉండవు.", "काम शुरू होने से पहले आप खर्च को मंज़ूरी देते हैं। कोई सरप्राइज़ नहीं।"),
 'tr.5.t': ("Gas only when needed", "అవసరమైతేనే గ్యాస్", "ज़रूरत हो तभी गैस"),
 'tr.5.d': ("Leak check first. Gas filling only if your AC really needs it.", "ముందు లీక్ చెక్. నిజంగా అవసరమైతేనే గ్యాస్ ఫిల్లింగ్.", "पहले लीक की जाँच। एसी को सच में ज़रूरत हो तभी गैस फिलिंग।"),
 'tr.6.t': ("All major brands", "అన్ని ప్రముఖ బ్రాండ్లు", "सभी प्रमुख ब्रांड"),
 'tr.6.d': ("LG, Daikin, Voltas, Samsung, Blue Star, Haier and more.", "LG, Daikin, Voltas, Samsung, Blue Star, Haier మరియు మరిన్ని.", "LG, Daikin, Voltas, Samsung, Blue Star, Haier और भी।"),
 'tr.7.t': ("7+ years of experience", "7+ సంవత్సరాల అనుభవం", "7+ साल का अनुभव"),
 'tr.7.d': ("Hands-on experience with ACs and home appliances.", "ఏసీలు మరియు గృహోపకరణాలపై ప్రత్యక్ష అనుభవం.", "एसी और घरेलू उपकरणों पर हाथों-हाथ अनुभव।"),
 'tr.8.t': ("500+ happy customers", "500+ సంతోషకరమైన కస్టమర్లు", "500+ संतुष्ट ग्राहक"),
 'tr.8.d': ("Homes across Narasaraopet trust us with their appliances.", "నరసరావుపేట అంతటా ఇళ్లు తమ ఉపకరణాల కోసం మమ్మల్ని నమ్ముతాయి.", "नरसरावपेट भर के घर अपने उपकरणों के लिए हम पर भरोसा करते हैं।"),
 'tr.9.t': ("Genuine spare parts", "నాణ్యమైన విడిభాగాలు", "असली स्पेयर पार्ट्स"),
 'tr.9.d': ("Quality parts for a longer appliance life.", "ఉపకరణం ఎక్కువ కాలం పనిచేయడానికి నాణ్యమైన భాగాలు.", "उपकरण की लंबी उम्र के लिए अच्छी क्वालिटी के पार्ट्स।"),
 'tr.10.t': ("Tested before we leave", "వెళ్ళే ముందు టెస్ట్", "जाने से पहले टेस्ट"),
 'tr.10.d': ("We check everything works properly before we finish.", "పని పూర్తి చేసే ముందు అన్నీ సరిగా పనిచేస్తున్నాయో చూస్తాము.", "काम खत्म करने से पहले जाँचते हैं कि सब ठीक चल रहा है।"),
 'tr.11.t': ("Easy booking", "సులభమైన బుకింగ్", "आसान बुकिंग"),
 'tr.11.d': ("Book in a minute by call, WhatsApp or our online form.", "కాల్, వాట్సాప్ లేదా ఆన్‌లైన్ ఫారం ద్వారా ఒక్క నిమిషంలో బుక్ చేయండి.", "कॉल, व्हाट्सऐप या ऑनलाइन फ़ॉर्म से एक मिनट में बुक करें।"),
})

S['rev.sub2'] = ("Customer feedback matters to us. Explore experiences shared by customers who have used our AC repair and home appliance services in Narasaraopet and surrounding areas.",
 "కస్టమర్ల అభిప్రాయం మాకు చాలా ముఖ్యం. నరసరావుపేట మరియు చుట్టుపక్కల ప్రాంతాల్లో మా AC రిపేర్ మరియు గృహోపకరణ సేవలను ఉపయోగించిన కస్టమర్ల అనుభవాలను చూడండి.",
 "ग्राहकों की राय हमारे लिए बहुत मायने रखती है। नरसरावपेट और आसपास के इलाकों में हमारी AC रिपेयर और होम अप्लायंस सेवाएँ लेने वाले ग्राहकों के अनुभव देखें।")
S['rev.readall'] = ("Read All Google Reviews", "అన్ని గూగుల్ రివ్యూలు చదవండి", "सभी गूगल रिव्यू पढ़ें")
S['rev.write'] = ("Write a Review", "రివ్యూ రాయండి", "रिव्यू लिखें")

# ---- Home: animated service slider (2nd hero) + pre-header ----
S['pre.known'] = ("Known as", "అందరికీ", "उर्फ़")
S['bh2.eyebrow'] = ("Our Services", "మా సేవలు", "हमारी सेवाएँ")
S['bh2.trust'] = ("Trusted doorstep service in Narasaraopet", "నరసరావుపేటలో నమ్మకమైన ఇంటి వద్ద సేవ", "नरसरावपेट में भरोसेमंद डोरस्टेप सेवा")
S['bh2.h2'] = ("Reliable AC Repair &amp; Services at <em>Your Doorstep</em>", "నమ్మకమైన AC రిపేర్ &amp; సేవలు <em>మీ ఇంటి వద్దకే</em>", "भरोसेमंद AC रिपेयर और सेवाएँ <em>आपके दरवाज़े पर</em>")
S['bh2.tab.ac'] = ("AC", "AC", "AC")
S['bh2.tab.fridge'] = ("Fridge", "ఫ్రిజ్", "फ्रिज")
S['bh2.tab.washer'] = ("Washer", "వాషర్", "वॉशर")
S['bh2.tab.cooler'] = ("Cooler", "కూలర్", "कूलर")
S['bh2.tab.fan'] = ("Fan", "ఫ్యాన్", "पंखा")
S['bh2.ac.t'] = ("AC Repair &amp; Servicing", "AC రిపేర్ &amp; సర్వీసింగ్", "AC रिपेयर और सर्विसिंग")
S['bh2.ac.d'] = ("Installation · Uninstallation · Gas filling · Repair — split &amp; window ACs of all major brands.", "ఇన్‌స్టలేషన్ · అన్‌ఇన్‌స్టలేషన్ · గ్యాస్ ఫిల్లింగ్ · రిపేర్ — అన్ని ప్రధాన బ్రాండ్ల స్ప్లిట్ &amp; విండో ACలు.", "इंस्टॉलेशन · अनइंस्टॉलेशन · गैस फिलिंग · रिपेयर — सभी प्रमुख ब्रांड के स्प्लिट और विंडो AC।")
S['bh2.fridge.t'] = ("Refrigerator Repair", "రిఫ్రిజిరేటర్ రిపేర్", "रेफ्रिजरेटर रिपेयर")
S['bh2.fridge.d'] = ("Not cooling, ice build-up, noise or gas issues — single &amp; double-door models.", "కూలింగ్ లేకపోవడం, ఐస్ పేరుకుపోవడం, శబ్దం లేదా గ్యాస్ సమస్యలు — సింగిల్ &amp; డబుల్ డోర్ మోడల్స్.", "कूलिंग न होना, बर्फ जमना, आवाज़ या गैस की समस्या — सिंगल और डबल डोर मॉडल।")
S['bh2.washer.t'] = ("Washing Machine Repair", "వాషింగ్ మెషిన్ రిపేర్", "वॉशिंग मशीन रिपेयर")
S['bh2.washer.d'] = ("Drum, drain, motor and control-board faults in front &amp; top-load machines.", "ఫ్రంట్ &amp; టాప్ లోడ్ మెషిన్లలో డ్రమ్, డ్రెయిన్, మోటార్, కంట్రోల్ బోర్డ్ సమస్యలు.", "फ्रंट और टॉप लोड मशीनों में ड्रम, ड्रेन, मोटर और कंट्रोल बोर्ड की खराबी।")
S['bh2.cooler.t'] = ("Air Cooler Repair", "ఎయిర్ కూలర్ రిపేర్", "एयर कूलर रिपेयर")
S['bh2.cooler.d'] = ("Pump, motor, cooling pads and wiring — ready before the summer peak.", "పంప్, మోటార్, కూలింగ్ ప్యాడ్స్, వైరింగ్ — వేసవి ముందే సిద్ధం.", "पंप, मोटर, कूलिंग पैड और वायरिंग — गर्मी से पहले तैयार।")
S['bh2.fan.t'] = ("Ceiling Fan Repair", "సీలింగ్ ఫ్యాన్ రిపేర్", "सीलिंग फैन रिपेयर")
S['bh2.fan.d'] = ("Slow speed, noise, capacitor and regulator problems fixed at home.", "నెమ్మదిగా తిరగడం, శబ్దం, కెపాసిటర్, రెగ్యులేటర్ సమస్యలు ఇంటి వద్దే సరిచేస్తాం.", "धीमी स्पीड, आवाज़, कैपेसिटर और रेगुलेटर की समस्या घर पर ठीक।")
S['bh2.prev'] = ("Previous service", "మునుపటి సేవ", "पिछली सेवा")
S['bh2.next'] = ("Next service", "తదుపరి సేవ", "अगली सेवा")
S['bh2.mq.1'] = ("Cool Comfort. Honest Service. Right at Your Doorstep.", "చల్లని సౌకర్యం. నిజాయితీ సేవ. మీ ఇంటి వద్దకే.", "ठंडा आराम। ईमानदार सेवा। सीधे आपके दरवाज़े पर।")
S['bh2.mq.2'] = ("Inspection first", "ముందు తనిఖీ", "पहले जाँच")
S['bh2.mq.3'] = ("Estimate before work", "పని ముందే అంచనా", "काम से पहले अनुमान")
S['bh2.mq.4'] = ("Open 24 hours", "24 గంటలూ అందుబాటులో", "24 घंटे खुला")
S['bh2.mq.5'] = ("All major brands", "అన్ని ప్రధాన బ్రాండ్లు", "सभी प्रमुख ब्रांड")
S['bh2.mq.6'] = ("Genuine spare parts", "నిజమైన స్పేర్ పార్ట్స్", "असली स्पेयर पार्ट्स")
S['bh2.mq.7'] = ("500+ happy customers", "500+ సంతోషకరమైన కస్టమర్లు", "500+ खुश ग्राहक")
S['bh2.mq.8'] = ("7+ years in Narasaraopet", "నరసరావుపేటలో 7+ సంవత్సరాలు", "नरसरावपेट में 7+ साल")

S['rev.sample'] = ("SAMPLE", "నమూనా", "नमूना")
S['rev.samplenote'] = ("Sample reviews shown for preview — genuine customer reviews will replace these soon.", "ప్రివ్యూ కోసం నమూనా రివ్యూలు చూపిస్తున్నాం — త్వరలో నిజమైన కస్టమర్ రివ్యూలు వస్తాయి.", "प्रीव्यू के लिए नमूना रिव्यू दिखाए गए हैं — जल्द ही असली ग्राहक रिव्यू आएँगे।")

# ---- Booking form v2: precise location, search suggestions, validation, thank-you ----
S['f.loc.improving'] = ("Getting a precise fix… ±{m} m", "ఖచ్చితమైన లొకేషన్ తీసుకుంటున్నాం… ±{m} మీ", "सटीक लोकेशन ले रहे हैं… ±{m} मी")
S['f.loc.adjust'] = ("Adjust on map", "మ్యాప్‌లో సరిచేయండి", "मैप पर ठीक करें")
S['f.loc.weak'] = ("Location is approximate (±{m} m). Please check the pin on the map.", "లొకేషన్ సుమారుగా ఉంది (±{m} మీ). దయచేసి మ్యాప్‌లో పిన్ చూసుకోండి.", "लोकेशन अनुमानित है (±{m} मी)। कृपया मैप पर पिन देख लें।")
S['f.loc.insecure'] = ("Location needs a secure (https) page. Please use 'Choose on map'.", "లొకేషన్‌కు సురక్షిత (https) పేజీ అవసరం. 'మ్యాప్‌లో ఎంచుకోండి' ఉపయోగించండి.", "लोकेशन के लिए सुरक्षित (https) पेज चाहिए। 'मैप पर चुनें' इस्तेमाल करें।")
S['f.loc.denied'] = ("Location permission is blocked. Allow location for this site in your browser settings, or use 'Choose on map'.", "లొకేషన్ అనుమతి బ్లాక్ అయింది. బ్రౌజర్ సెట్టింగ్స్‌లో ఈ సైట్‌కు లొకేషన్ అనుమతించండి, లేదా 'మ్యాప్‌లో ఎంచుకోండి' ఉపయోగించండి.", "लोकेशन की अनुमति बंद है। ब्राउज़र सेटिंग्स में इस साइट के लिए लोकेशन चालू करें, या 'मैप पर चुनें' इस्तेमाल करें।")
S['f.loc.fail'] = ("Couldn't get your location. Turn on GPS and try again, or use 'Choose on map'.", "మీ లొకేషన్ దొరకలేదు. GPS ఆన్ చేసి మళ్లీ ప్రయత్నించండి, లేదా 'మ్యాప్‌లో ఎంచుకోండి' ఉపయోగించండి.", "आपकी लोकेशन नहीं मिली। GPS चालू करके फिर कोशिश करें, या 'मैप पर चुनें' इस्तेमाल करें।")
S['map.hint'] = ("Search your area, colony or landmark — or move the map so the pin sits on your house. You can also paste a Google Maps link.", "మీ ఏరియా, కాలనీ లేదా ల్యాండ్‌మార్క్ వెతకండి — లేదా పిన్ మీ ఇంటిపై ఉండేలా మ్యాప్‌ను కదపండి. Google Maps లింక్ కూడా పేస్ట్ చేయవచ్చు.", "अपना इलाका, कॉलोनी या लैंडमार्क खोजें — या मैप को खिसकाएँ ताकि पिन आपके घर पर हो। Google Maps लिंक भी पेस्ट कर सकते हैं।")
S['map.search'] = ("Search area, colony, landmark or paste a Maps link", "ఏరియా, కాలనీ, ల్యాండ్‌మార్క్ వెతకండి లేదా Maps లింక్ పేస్ట్ చేయండి", "इलाका, कॉलोनी, लैंडमार्क खोजें या Maps लिंक पेस्ट करें")
S['map.searching'] = ("Searching…", "వెతుకుతున్నాం…", "खोज रहे हैं…")
S['map.noresult'] = ("No match found. Try a nearby landmark (school, temple, hospital) or move the map to your house.", "సరిపోలేది దొరకలేదు. దగ్గరలోని ల్యాండ్‌మార్క్ (స్కూల్, గుడి, హాస్పిటల్) ప్రయత్నించండి లేదా మ్యాప్‌ను మీ ఇంటికి కదపండి.", "कुछ नहीं मिला। पास का लैंडमार्क (स्कूल, मंदिर, अस्पताल) आज़माएँ या मैप को अपने घर तक खिसकाएँ।")
S['map.sat'] = ("Satellite", "శాటిలైట్", "सैटेलाइट")
S['map.street'] = ("Map", "మ్యాప్", "मैप")
S['map.pinaddr'] = ("Pin location", "పిన్ లొకేషన్", "पिन लोकेशन")
S['f.err.phone'] = ("Enter a valid 10-digit mobile number (starts with 6, 7, 8 or 9).", "సరైన 10 అంకెల మొబైల్ నంబర్ ఇవ్వండి (6, 7, 8 లేదా 9తో మొదలవ్వాలి).", "सही 10 अंकों का मोबाइल नंबर डालें (6, 7, 8 या 9 से शुरू)।")
S['f.err.name'] = ("Please enter your name (at least 2 letters).", "దయచేసి మీ పేరు ఇవ్వండి (కనీసం 2 అక్షరాలు).", "कृपया अपना नाम लिखें (कम से कम 2 अक्षर)।")
S['f.err.area'] = ("Please enter your area or a landmark (at least 3 letters).", "దయచేసి మీ ఏరియా లేదా ల్యాండ్‌మార్క్ ఇవ్వండి (కనీసం 3 అక్షరాలు).", "कृपया अपना इलाका या लैंडमार्क लिखें (कम से कम 3 अक्षर)।")
S['f.err.date'] = ("Please choose today or a future date.", "దయచేసి ఈరోజు లేదా తర్వాతి తేదీ ఎంచుకోండి.", "कृपया आज या आगे की तारीख चुनें।")
S['f.phone.count'] = ("{n}/10 digits", "{n}/10 అంకెలు", "{n}/10 अंक")
S['f.thanks.h'] = ("Thanks for booking!", "బుక్ చేసినందుకు ధన్యవాదాలు!", "बुकिंग के लिए धन्यवाद!")
S['f.thanks.p'] = ("We've received your details and will catch up with you soon.", "మీ వివరాలు మాకు అందాయి, త్వరలోనే మిమ్మల్ని సంప్రదిస్తాం.", "आपकी जानकारी हमें मिल गई है, हम जल्द ही आपसे संपर्क करेंगे।")
S['f.thanks.sign'] = ("— Bobby", "— బాబీ", "— बॉबी")
S['f.thanks.tip'] = ("WhatsApp has opened with your booking — just tap Send there to confirm.", "మీ బుకింగ్‌తో WhatsApp ఓపెన్ అయింది — కన్ఫర్మ్ చేయడానికి అక్కడ Send నొక్కండి.", "आपकी बुकिंग के साथ WhatsApp खुल गया है — कन्फ़र्म करने के लिए वहाँ Send दबाएँ।")
S['f.thanks.again'] = ("Open WhatsApp again", "WhatsApp మళ్లీ ఓపెన్ చేయండి", "WhatsApp फिर से खोलें")
S['f.thanks.new'] = ("Book another service", "మరో సేవ బుక్ చేయండి", "दूसरी सेवा बुक करें")
S['f.wa.addr'] = ("Address (from map)", "చిరునామా (మ్యాప్ నుండి)", "पता (मैप से)")

# ---- Booking: accurate success wording (WhatsApp still needs Send) ----
S['f.thanks.h'] = ("Almost done — press Send in WhatsApp", "దాదాపు పూర్తైంది — WhatsAppలో Send నొక్కండి", "लगभग हो गया — WhatsApp में Send दबाएँ")
S['f.thanks.p'] = ("Your booking message is ready in WhatsApp. Please press Send to submit your service request. Our team will contact you to confirm the visit.",
 "మీ బుకింగ్ సందేశం WhatsAppలో సిద్ధంగా ఉంది. మీ సర్వీస్ అభ్యర్థనను పంపడానికి దయచేసి Send నొక్కండి. విజిట్‌ను నిర్ధారించడానికి మా టీమ్ మిమ్మల్ని సంప్రదిస్తుంది.",
 "आपका बुकिंग संदेश WhatsApp में तैयार है। अपनी सर्विस रिक्वेस्ट भेजने के लिए कृपया Send दबाएँ। विज़िट कन्फ़र्म करने के लिए हमारी टीम आपसे संपर्क करेगी।")
S['f.thanks.tip'] = ("Didn't see WhatsApp open? Use the button below.", "WhatsApp ఓపెన్ కాలేదా? కింద ఉన్న బటన్ ఉపయోగించండి.", "WhatsApp नहीं खुला? नीचे दिया बटन इस्तेमाल करें।")

# ---- Slider hero: distinct heading (no duplicate of the main H1) ----
S['bh2.h2'] = ("One Call for AC, Fridge, Washing Machine, Cooler &amp; Fan Repair", "AC, ఫ్రిజ్, వాషింగ్ మెషిన్, కూలర్ &amp; ఫ్యాన్ రిపేర్ — ఒక్క కాల్ చాలు", "AC, फ्रिज, वॉशिंग मशीन, कूलर और पंखा रिपेयर — बस एक कॉल")

S['duo.trust'] = ("Why customers choose BOBBY", "కస్టమర్లు BOBBYని ఎందుకు ఎంచుకుంటారు", "ग्राहक BOBBY को क्यों चुनते हैं")
S['ft.more'] = ("More about BOBBY", "BOBBY గురించి మరింత", "BOBBY के बारे में और जानें")
S['ft.about'] = ("Local doorstep AC repair, servicing, installation and home appliance repair in Narasaraopet, Andhra Pradesh. Run by Yalamanda Gogasani (Bobby), we service split and window ACs, refrigerators, washing machines, air coolers and ceiling fans of all major brands — with inspection first and a clear estimate before any work.",
 "నరసరావుపేట, ఆంధ్రప్రదేశ్‌లో ఇంటి వద్దకే ఏసీ రిపేర్, సర్వీసింగ్, ఇన్‌స్టాలేషన్ మరియు గృహోపకరణాల రిపేర్. యలమంద గోగసాని (బాబీ) నిర్వహణలో, అన్ని ప్రముఖ బ్రాండ్ల స్ప్లిట్ & విండో ఏసీలు, ఫ్రిజ్‌లు, వాషింగ్ మెషీన్లు, ఎయిర్ కూలర్లు, సీలింగ్ ఫ్యాన్లకు సర్వీస్ చేస్తాం — ముందుగా తనిఖీ, పని ముందు స్పష్టమైన అంచనా.",
 "नरसरावपेट, आंध्र प्रदेश में घर पर एसी रिपेयर, सर्विसिंग, इंस्टॉलेशन और घरेलू उपकरण रिपेयर। यलमंदा गोगासानी (बॉबी) द्वारा संचालित — हम सभी प्रमुख ब्रांड्स के स्प्लिट व विंडो एसी, फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन की सर्विस करते हैं — पहले जाँच, काम से पहले साफ़ अनुमान।")
S['ft.about'] = ("Your trusted AC repair, installation and maintenance specialists in Narasaraopet, Andhra Pradesh — fast, reliable and affordable. Run by Bobby, we service split and window ACs, refrigerators, washing machines, air coolers and ceiling fans of all major brands at your doorstep, with inspection first and a clear estimate before any work.",
 "నరసరావుపేట, ఆంధ్రప్రదేశ్‌లో మీకు నమ్మకమైన ఏసీ రిపేర్, ఇన్‌స్టాలేషన్ మరియు మెయింటెనెన్స్ నిపుణులు — వేగంగా, నమ్మకంగా, తక్కువ ఖర్చుతో. బాబీ నిర్వహణలో, అన్ని ప్రముఖ బ్రాండ్ల స్ప్లిట్ & విండో ఏసీలు, ఫ్రిజ్‌లు, వాషింగ్ మెషీన్లు, ఎయిర్ కూలర్లు, సీలింగ్ ఫ్యాన్లకు మీ ఇంటి వద్దకే సర్వీస్ — ముందుగా తనిఖీ, పని ముందు స్పష్టమైన అంచనా.",
 "नरसरावपेट, आंध्र प्रदेश में आपके भरोसेमंद एसी रिपेयर, इंस्टॉलेशन और मेंटेनेंस विशेषज्ञ — तेज़, भरोसेमंद और किफ़ायती। बॉबी द्वारा संचालित — हम सभी प्रमुख ब्रांड्स के स्प्लिट व विंडो एसी, फ्रिज, वॉशिंग मशीन, एयर कूलर और सीलिंग फैन की आपके घर पर सर्विस करते हैं — पहले जाँच, काम से पहले साफ़ अनुमान।")
