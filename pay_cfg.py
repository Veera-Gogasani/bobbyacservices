# -*- coding: utf-8 -*-
"""UPI 'Pay' + Google review settings.
UPI_ID: Bobby's real UPI ID exactly as shown in Google Pay / PhonePe (profile -> UPI ID).
Leave '' to keep the Pay button hidden everywhere (a phone number alone cannot be used in a UPI payment link)."""
import os
UPI_ID = os.environ.get('BOBBY_UPI_TEST', '8374889163@sbi')   # TEMPORARY placeholder from owner (26 Nov 2026) - replace with the real UPI ID
UPI_NAME = 'Yalamanda Gogasani'                          # payee name shown in the UPI app
UPI_NUMBER = '8374889163'                                # Google Pay / PhonePe number (manual fallback)
REVIEW_URL = ('https://www.google.com/maps/place//data=!4m3!3m2!1s0x3a4a8120cd16cd23:0x6713e7c4650facdb!12e1'
              '?source=g.page.m.ia._&laa=nmx-review-solicitation-ia2')

def strings(name):
    b = f'<b>{name}</b>'
    return {
 'pay.btn': ('Pay', 'చెల్లించండి', 'भुगतान'),
 'pay.btn.long': ('Pay via UPI', 'UPI ద్వారా చెల్లించండి', 'UPI से भुगतान करें'),
 'pay.h': ('Pay BOBBY via UPI', 'UPI ద్వారా BOBBYకి చెల్లించండి', 'UPI से BOBBY को भुगतान करें'),
 'pay.sub': ('Pay only after your service is completed and you have agreed the final bill with the technician.',
             'సర్వీస్ పూర్తయి, టెక్నీషియన్‌తో తుది బిల్లు అంగీకరించిన తర్వాత మాత్రమే చెల్లించండి.',
             'सर्विस पूरी होने और टेक्नीशियन के साथ अंतिम बिल तय होने के बाद ही भुगतान करें।'),
 'pay.to': ('Paying to', 'చెల్లింపు అందుకునేవారు', 'भुगतान प्राप्तकर्ता'),
 'pay.amt': ('Bill amount (₹)', 'బిల్లు మొత్తం (₹)', 'बिल राशि (₹)'),
 'pay.amt.ph': ('Enter amount (optional)', 'మొత్తం నమోదు చేయండి (ఐచ్ఛికం)', 'राशि दर्ज करें (वैकल्पिक)'),
 'pay.amt.p': ('You can also enter or change the amount inside your app.', 'మొత్తాన్ని మీ యాప్‌లో కూడా నమోదు చేయవచ్చు లేదా మార్చవచ్చు.', 'आप राशि अपने ऐप में भी दर्ज या बदल सकते हैं।'),
 'pay.choose': ('Choose your payment app', 'మీ పేమెంట్ యాప్‌ను ఎంచుకోండి', 'अपना पेमेंट ऐप चुनें'),
 'pay.other': ('Other UPI apps', 'ఇతర UPI యాప్‌లు', 'अन्य UPI ऐप'),
 'pay.noapp': ("Didn't open? The app may not be installed on this phone. Try the other app, or copy the UPI ID or number below and pay inside your app.",
               'తెరుచుకోలేదా? ఆ యాప్ ఈ ఫోన్‌లో ఇన్‌స్టాల్ అయి ఉండకపోవచ్చు. మరో యాప్‌ను ప్రయత్నించండి, లేదా కింద ఉన్న UPI ID / నంబర్‌ను కాపీ చేసి మీ యాప్‌లో చెల్లించండి.',
               'नहीं खुला? हो सकता है यह ऐप इस फ़ोन में इंस्टॉल न हो। दूसरा ऐप आज़माएं, या नीचे दिया UPI ID / नंबर कॉपी करके अपने ऐप में भुगतान करें।'),
 'pay.check': (f'Before you enter your UPI PIN, check that your app shows the name {b}.',
               f'UPI PIN నమోదు చేసే ముందు, మీ యాప్‌లో {b} పేరు కనిపిస్తోందో చూసుకోండి.',
               f'UPI PIN डालने से पहले देख लें कि आपके ऐप में {b} नाम दिख रहा है।'),
 'pay.manual': ('Or pay manually', 'లేదా మాన్యువల్‌గా చెల్లించండి', 'या खुद भुगतान करें'),
 'pay.upiid': ('UPI ID', 'UPI ID', 'UPI ID'),
 'pay.num': ('Google Pay / PhonePe number', 'Google Pay / PhonePe నంబర్', 'Google Pay / PhonePe नंबर'),
 'pay.copy': ('Copy', 'కాపీ', 'कॉपी'),
 'pay.copied': ('Copied', 'కాపీ అయింది', 'कॉपी हो गया'),
 'pay.manual.p': ('Open Google Pay or PhonePe, choose "Pay phone number" or "Pay UPI ID", and paste.',
                  'Google Pay లేదా PhonePe తెరిచి, "Pay phone number" లేదా "Pay UPI ID" ఎంచుకుని పేస్ట్ చేయండి.',
                  'Google Pay या PhonePe खोलें, "Pay phone number" या "Pay UPI ID" चुनें और पेस्ट करें।'),
 'pay.safe': ("Your payment goes from your UPI app straight to BOBBY's bank account. This website never sees your bank details or UPI PIN.",
              'మీ చెల్లింపు మీ UPI యాప్ నుండి నేరుగా BOBBY బ్యాంక్ ఖాతాకు వెళ్తుంది. మీ బ్యాంక్ వివరాలు లేదా UPI PIN ఈ వెబ్‌సైట్‌కు ఎప్పుడూ కనిపించవు.',
              'आपका भुगतान आपके UPI ऐप से सीधे BOBBY के बैंक खाते में जाता है। यह वेबसाइट आपकी बैंक जानकारी या UPI PIN कभी नहीं देखती।'),
 'rv.h': ('Thank you for choosing BOBBY!', 'BOBBYని ఎంచుకున్నందుకు ధన్యవాదాలు!', 'BOBBY चुनने के लिए धन्यवाद!'),
 'rv.p': ('If your payment is complete, could you take 30 seconds to share your experience on Google? Your review helps other families in Narasaraopet find a trusted technician.',
          'మీ చెల్లింపు పూర్తయితే, 30 సెకన్లు కేటాయించి Googleలో మీ అనుభవాన్ని పంచుకుంటారా? మీ రివ్యూ నరసరావుపేటలోని ఇతర కుటుంబాలకు నమ్మకమైన టెక్నీషియన్‌ను కనుగొనడంలో సహాయపడుతుంది.',
          'अगर आपका भुगतान पूरा हो गया है, तो क्या आप 30 सेकंड में Google पर अपना अनुभव साझा करेंगे? आपका रिव्यू नरसरावपेट के दूसरे परिवारों को भरोसेमंद टेक्नीशियन ढूंढने में मदद करता है।'),
 'rv.steps': ('Tap the button, choose your stars, write a line about the service and tap Post.',
              'బటన్ నొక్కి, స్టార్లు ఎంచుకుని, సర్వీస్ గురించి ఒక లైన్ రాసి Post నొక్కండి.',
              'बटन दबाएं, स्टार चुनें, सर्विस के बारे में एक लाइन लिखें और Post दबाएं।'),
 'rv.later': ('Not now', 'ఇప్పుడు కాదు', 'अभी नहीं'),
 'rev.btn': ('Write a Google Review', 'Google రివ్యూ రాయండి', 'Google रिव्यू लिखें'),
 'rev.short': ('Review us', 'రివ్యూ ఇవ్వండి', 'रिव्यू दें'),
}
