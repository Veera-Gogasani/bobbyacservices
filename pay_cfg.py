# -*- coding: utf-8 -*-
"""UPI 'Pay' + Google review settings.
UPI_ID: Bobby's real UPI ID exactly as shown in Google Pay / PhonePe (profile -> UPI ID).
Leave '' to keep the Pay button hidden everywhere (a phone number alone cannot be used in a UPI payment link)."""
import os
UPI_ID = os.environ.get('BOBBY_UPI_TEST', '8374889163@ibl')   # owner's displayed PhonePe UPI ID (KVB a/c 2961); his QR image encodes the same account as @axl
# Exact parameters decoded from the owner's own QR code. App buttons send these unchanged (no amount/note),
# because UPI apps decline website-started payments to personal accounts when extra fields are added.
UPI_QR_PARAMS = 'pn=G%20YALLAMANDA&mc=0000&mode=02&purpose=00'
UPI_NAME = 'G YALLAMANDA'                                # bank-registered name the customer's UPI app shows (from the QR)
UPI_NUMBER = '8374889163'                                # Google Pay / PhonePe number (manual fallback)
REVIEW_URL = ('https://www.google.com/maps/place//data=!4m3!3m2!1s0x3a4a8120cd16cd23:0x6713e7c4650facdb!12e1'
              '?source=g.page.m.ia._&laa=nmx-review-solicitation-ia2')

def strings(name):
    b = f'<b>{name}</b>'
    return {
 'pay.btn': ('Pay', 'చెల్లించండి', 'भुगतान'),
 'pay.btn.long': ('Pay via UPI', 'UPI ద్వారా చెల్లించండి', 'UPI से भुगतान करें'),
 'pay.h': ('Pay BOBBY via UPI', 'UPI ద్వారా BOBBYకి చెల్లించండి', 'UPI से BOBBY को भुगतान करें'),
 'pay.sub': ('Thanks for the opportunity to serve you.', 'మీకు సేవ చేసే అవకాశం ఇచ్చినందుకు ధన్యవాదాలు.', 'आपकी सेवा का अवसर देने के लिए धन्यवाद।'),
 'pay.to': ('Paying to', 'చెల్లింపు అందుకునేవారు', 'भुगतान प्राप्तकर्ता'),
 'pay.qr': ('Pay with QR code', 'QR కోడ్‌తో చెల్లించండి', 'QR कोड से भुगतान करें'),
 'pay.qr.p': ('Scan with any UPI app. On this phone: tap Save QR, then in Google Pay or PhonePe tap Scan and choose the QR from your gallery.',
              'ఏ UPI యాప్‌తోనైనా స్కాన్ చేయండి. ఈ ఫోన్‌లో: Save QR నొక్కి, ఆపై Google Pay లేదా PhonePeలో Scan నొక్కి గ్యాలరీ నుండి QRను ఎంచుకోండి.',
              'किसी भी UPI ऐप से स्कैन करें। इसी फ़ोन पर: Save QR दबाएं, फिर Google Pay या PhonePe में Scan दबाकर गैलरी से QR चुनें।'),
 'pay.qr.save': ('Save QR', 'QR సేవ్ చేయండి', 'QR सेव करें'),
 'pay.copybtn': ('Copy UPI ID', 'UPI ID కాపీ చేయండి', 'UPI ID कॉपी करें'),
 'pay.copied': ('Copied! Now open PhonePe or Google Pay and paste it.', 'కాపీ అయింది! ఇప్పుడు PhonePe లేదా Google Pay తెరిచి పేస్ట్ చేయండి.', 'कॉपी हो गया! अब PhonePe या Google Pay खोलकर पेस्ट करें।'),
 'pay.s1': ('Tap Copy UPI ID.', 'UPI ID కాపీ చేయండి నొక్కండి.', 'UPI ID कॉपी करें दबाएं।'),
 'pay.s2': ('Open PhonePe or Google Pay, tap "To UPI ID" (PhonePe) or "Pay UPI ID or number" (Google Pay) and paste.',
            'PhonePe లేదా Google Pay తెరిచి, "To UPI ID" (PhonePe) లేదా "Pay UPI ID or number" (Google Pay) నొక్కి పేస్ట్ చేయండి.',
            'PhonePe या Google Pay खोलें, "To UPI ID" (PhonePe) या "Pay UPI ID or number" (Google Pay) दबाकर पेस्ट करें।'),
 'pay.s3': ('Enter the bill amount and pay.', 'బిల్లు మొత్తం నమోదు చేసి చెల్లించండి.', 'बिल राशि डालें और भुगतान करें।'),
 'pay.check': (f'Before you enter your UPI PIN, check that your app shows the name {b}.',
               f'UPI PIN నమోదు చేసే ముందు, మీ యాప్‌లో {b} పేరు కనిపిస్తోందో చూసుకోండి.',
               f'UPI PIN डालने से पहले देख लें कि आपके ऐप में {b} नाम दिख रहा है।'),
 'pay.safe': ("Your payment goes from your UPI app straight to BOBBY's bank account. This website never sees your bank details or UPI PIN.",
              'మీ చెల్లింపు మీ UPI యాప్ నుండి నేరుగా BOBBY బ్యాంక్ ఖాతాకు వెళ్తుంది. మీ బ్యాంక్ వివరాలు లేదా UPI PIN ఈ వెబ్‌సైట్‌కు ఎప్పుడూ కనిపించవు.',
              'आपका भुगतान आपके UPI ऐप से सीधे BOBBY के बैंक खाते में जाता है। यह वेबसाइट आपकी बैंक जानकारी या UPI PIN कभी नहीं देखती।'),
 'rv.h': ('Thank you for choosing BOBBY!', 'BOBBYని ఎంచుకున్నందుకు ధన్యవాదాలు!', 'BOBBY चुनने के लिए धन्यवाद!'),
 'rv.p': ('Could you take 30 seconds to share your experience on Google? Your review helps other families in Narasaraopet find a trusted technician.',
          '30 సెకన్లు కేటాయించి Googleలో మీ అనుభవాన్ని పంచుకుంటారా? మీ రివ్యూ నరసరావుపేటలోని ఇతర కుటుంబాలకు నమ్మకమైన టెక్నీషియన్‌ను కనుగొనడంలో సహాయపడుతుంది.',
          'क्या आप 30 सेकंड में Google पर अपना अनुभव साझा करेंगे? आपका रिव्यू नरसरावपेट के दूसरे परिवारों को भरोसेमंद टेक्नीशियन ढूंढने में मदद करता है।'),
 'rv.steps': ('Tap the button, choose your stars, write a line about the service and tap Post.',
              'బటన్ నొక్కి, స్టార్లు ఎంచుకుని, సర్వీస్ గురించి ఒక లైన్ రాసి Post నొక్కండి.',
              'बटन दबाएं, स्टार चुनें, सर्विस के बारे में एक लाइन लिखें और Post दबाएं।'),
 'rv.later': ('Not now', 'ఇప్పుడు కాదు', 'अभी नहीं'),
 'pp.secure': ('Secure payment by PhonePe', 'PhonePe ద్వారా సురక్షిత చెల్లింపు', 'PhonePe द्वारा सुरक्षित भुगतान'),
 'pp.amt': ('Bill amount (₹)', 'బిల్లు మొత్తం (₹)', 'बिल राशि (₹)'),
 'pp.amt.ph': ('Amount agreed with the technician', 'టెక్నీషియన్‌తో అంగీకరించిన మొత్తం', 'टेक्नीशियन से तय राशि'),
 'pp.mob': ('Your mobile number (optional)', 'మీ మొబైల్ నంబర్ (ఐచ్ఛికం)', 'आपका मोबाइल नंबर (वैकल्पिक)'),
 'pp.mob.ph': ('10-digit mobile number', '10 అంకెల మొబైల్ నంబర్', '10 अंकों का मोबाइल नंबर'),
 'pp.btn': ('Pay with PhonePe', 'PhonePeతో చెల్లించండి', 'PhonePe से भुगतान करें'),
 'pp.wait': ('Opening PhonePe…', 'PhonePe తెరుస్తోంది…', 'PhonePe खुल रहा है…'),
 'pp.p': ("You'll go to PhonePe's secure payment page with the amount already filled in. Choose PhonePe (or any UPI app), enter your UPI PIN, and you're done.",
          'మొత్తం ముందే నింపిన PhonePe సురక్షిత చెల్లింపు పేజీకి వెళ్తారు. PhonePe (లేదా ఏ UPI యాప్ అయినా) ఎంచుకుని, UPI PIN నమోదు చేస్తే చాలు.',
          'आप PhonePe के सुरक्षित भुगतान पेज पर जाएंगे, जहां राशि पहले से भरी होगी। PhonePe (या कोई भी UPI ऐप) चुनें, UPI PIN डालें, बस हो गया।'),
 'pp.err.amt': ('Please enter an amount between ₹1 and ₹1,00,000.', 'దయచేసి ₹1 నుండి ₹1,00,000 మధ్య మొత్తం నమోదు చేయండి.', 'कृपया ₹1 से ₹1,00,000 के बीच राशि दर्ज करें।'),
 'pp.err': ('Could not start the payment. Please try again, or call +91 83748 89163.', 'చెల్లింపు ప్రారంభించలేకపోయాం. మళ్లీ ప్రయత్నించండి, లేదా +91 83748 89163కి కాల్ చేయండి.', 'भुगतान शुरू नहीं हो सका। कृपया फिर कोशिश करें, या +91 83748 89163 पर कॉल करें।'),
 'pr.title': ('Payment status', 'చెల్లింపు స్థితి', 'भुगतान स्थिति'),
 'pr.check.h': ('Checking your payment…', 'మీ చెల్లింపును తనిఖీ చేస్తున్నాం…', 'आपका भुगतान जांचा जा रहा है…'),
 'pr.check.p': ('Please wait a moment. Do not close this page.', 'దయచేసి కొద్దిసేపు వేచి ఉండండి. ఈ పేజీని మూసివేయవద్దు.', 'कृपया थोड़ा इंतज़ार करें। यह पेज बंद न करें।'),
 'pr.ok.h': ('Payment successful', 'చెల్లింపు విజయవంతమైంది', 'भुगतान सफल'),
 'pr.ok.p': ('Thank you! BOBBY has received your payment.', 'ధన్యవాదాలు! BOBBYకి మీ చెల్లింపు అందింది.', 'धन्यवाद! BOBBY को आपका भुगतान मिल गया है।'),
 'pr.amount': ('Amount', 'మొత్తం', 'राशि'),
 'pr.order': ('Payment ID', 'చెల్లింపు ID', 'भुगतान ID'),
 'pr.pend.h': ('Payment is processing', 'చెల్లింపు ప్రాసెస్ అవుతోంది', 'भुगतान प्रोसेस हो रहा है'),
 'pr.pend.p': ("This can take a minute. Please don't pay again; this page updates automatically.", 'దీనికి ఒక నిమిషం పట్టవచ్చు. దయచేసి మళ్లీ చెల్లించవద్దు; ఈ పేజీ ఆటోమేటిక్‌గా అప్‌డేట్ అవుతుంది.', 'इसमें एक मिनट लग सकता है। कृपया दोबारा भुगतान न करें; यह पेज अपने आप अपडेट होगा।'),
 'pr.fail.h': ('Payment not completed', 'చెల్లింపు పూర్తి కాలేదు', 'भुगतान पूरा नहीं हुआ'),
 'pr.fail.p': ('The payment was cancelled or failed. If any amount was debited, your bank usually refunds it automatically within a few days.', 'చెల్లింపు రద్దయింది లేదా విఫలమైంది. ఏదైనా మొత్తం కట్ అయితే, మీ బ్యాంక్ సాధారణంగా కొన్ని రోజుల్లో ఆటోమేటిక్‌గా తిరిగి ఇస్తుంది.', 'भुगतान रद्द या विफल हो गया। अगर कोई राशि कटी है, तो आपका बैंक आमतौर पर कुछ दिनों में अपने आप वापस कर देता है।'),
 'pr.err.h': ("We couldn't check the payment", 'చెల్లింపును తనిఖీ చేయలేకపోయాం', 'हम भुगतान जांच नहीं सके'),
 'pr.err.p': ('Please call or WhatsApp BOBBY on +91 83748 89163 with your Payment ID and we will confirm it.', 'మీ చెల్లింపు IDతో +91 83748 89163కి కాల్ లేదా WhatsApp చేయండి, మేము నిర్ధారిస్తాము.', 'कृपया अपनी भुगतान ID के साथ +91 83748 89163 पर कॉल या WhatsApp करें, हम पुष्टि करेंगे।'),
 'pr.retry': ('Try again', 'మళ్లీ ప్రయత్నించండి', 'फिर कोशिश करें'),
 'pr.home': ('Back to home', 'హోమ్‌కి వెళ్లండి', 'होम पर जाएं'),
 'pr.review': ('Write a Google Review', 'Google రివ్యూ రాయండి', 'Google रिव्यू लिखें'),
 'rev.btn': ('Write a Google Review', 'Google రివ్యూ రాయండి', 'Google रिव्यू लिखें'),
 'rev.short': ('Review us', 'రివ్యూ ఇవ్వండి', 'रिव्यू दें'),
}
