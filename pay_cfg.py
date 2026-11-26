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
 'pay.sub': ('Pay only after your service is completed and you have agreed the final bill with the technician.',
             'సర్వీస్ పూర్తయి, టెక్నీషియన్‌తో తుది బిల్లు అంగీకరించిన తర్వాత మాత్రమే చెల్లించండి.',
             'सर्विस पूरी होने और टेक्नीशियन के साथ अंतिम बिल तय होने के बाद ही भुगतान करें।'),
 'pay.to': ('Paying to', 'చెల్లింపు అందుకునేవారు', 'भुगतान प्राप्तकर्ता'),
 'pay.open': ('Open UPI app to pay', 'చెల్లించడానికి UPI యాప్ తెరవండి', 'भुगतान के लिए UPI ऐप खोलें'),
 'pay.open.p': ('Opens Google Pay, PhonePe or any UPI app on your phone with BOBBY already selected. Enter the bill amount there and tap Pay.',
                'మీ ఫోన్‌లోని Google Pay, PhonePe లేదా ఏ UPI యాప్ అయినా BOBBY ఎంపిక చేసి తెరుచుకుంటుంది. అక్కడ బిల్లు మొత్తం నమోదు చేసి Pay నొక్కండి.',
                'आपके फ़ोन का Google Pay, PhonePe या कोई भी UPI ऐप BOBBY चुना हुआ खुलेगा। वहां बिल राशि डालें और Pay दबाएं।'),
 'pay.noapp': ('No UPI app opened? Pay with the QR code below: tap Save QR, then scan it from your gallery in any UPI app.',
               'UPI యాప్ తెరుచుకోలేదా? కింద ఉన్న QR కోడ్‌తో చెల్లించండి: Save QR నొక్కి, ఏ UPI యాప్‌లోనైనా గ్యాలరీ నుండి స్కాన్ చేయండి.',
               'UPI ऐप नहीं खुला? नीचे दिए QR कोड से भुगतान करें: Save QR दबाएं, फिर किसी भी UPI ऐप में गैलरी से स्कैन करें।'),
 'pay.qr': ('Pay with QR code', 'QR కోడ్‌తో చెల్లించండి', 'QR कोड से भुगतान करें'),
 'pay.qr.p': ('Scan with any UPI app. On this phone: tap Save QR, then in Google Pay or PhonePe tap Scan and choose the QR from your gallery.',
              'ఏ UPI యాప్‌తోనైనా స్కాన్ చేయండి. ఈ ఫోన్‌లో: Save QR నొక్కి, ఆపై Google Pay లేదా PhonePeలో Scan నొక్కి గ్యాలరీ నుండి QRను ఎంచుకోండి.',
              'किसी भी UPI ऐप से स्कैन करें। इसी फ़ोन पर: Save QR दबाएं, फिर Google Pay या PhonePe में Scan दबाकर गैलरी से QR चुनें।'),
 'pay.qr.save': ('Save QR', 'QR సేవ్ చేయండి', 'QR सेव करें'),
 'pay.check': (f'Before you enter your UPI PIN, check that your app shows the name {b}.',
               f'UPI PIN నమోదు చేసే ముందు, మీ యాప్‌లో {b} పేరు కనిపిస్తోందో చూసుకోండి.',
               f'UPI PIN डालने से पहले देख लें कि आपके ऐप में {b} नाम दिख रहा है।'),
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
