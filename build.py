# -*- coding: utf-8 -*-
"""Static site generator for BOBBY AC Repair & Home Appliance Services.
Run:  python3 build.py   ->  writes the finished site into ./dist
Edit business details, prices and photos in the CONFIG block below."""
import json, os, shutil, html, sys
from strings import S, SERVICES, FAQ_N
from blog import POSTS, add_strings

# ======================= CONFIG =======================
# ---- Going live on the real domain: the ONLY switch ----
# 1) Buy bobbyacservices.com and add both www.bobbyacservices.com and bobbyacservices.com as Custom Domains
#    in Cloudflare Pages (project "bobbyacservices"). 2) When https://www.bobbyacservices.com opens the site,
#    set DOMAIN_CONNECTED = True, run `python3 build.py`, commit and push. Canonical links, sitemap, robots,
#    schema, llms.txt and the pages.dev -> www redirect (functions/_middleware.js) all follow this one flag.
DOMAIN_CONNECTED = True
DOMAIN    = 'www.bobbyacservices.com'
SITE      = ('https://' + DOMAIN) if DOMAIN_CONNECTED else 'https://bobbyacservices.pages.dev'
BRAND     = 'BOBBY AC Repair & Home Appliance Services'
PHONE_TXT = '+91 83748 89163'
PHONE_TEL = '+918374889163'
WA_NUM    = '918374889163'
CITY      = 'Narasaraopet'
REGION    = 'Andhra Pradesh'
UPDATED   = '2026-11-18'
ADDRESS   = {'street': 'Door 11-28-32/5, Employees Colony, Isha Zen Enclave, Palapadu Road, Arundelpet', 'locality': 'Narasaraopeta', 'postal': '522601'}
GMAPS_CID = int('6713e7c4650facdb', 16)            # Google Business Profile listing
GMAPS_URL = 'https://maps.google.com/?cid=%d' % GMAPS_CID
DIR_URL   = 'https://www.google.com/maps/dir/?api=1&destination=16.2371462,80.0339778'
GEO = (16.2371462, 80.0339778)                     # from the Google Business Profile listing
MAP_EMBED = 'https://maps.google.com/maps?q=%s,%s&amp;z=17&amp;output=embed' % GEO

# Source prices (₹). The website automatically shows source + 100.
# None = no price published yet -> card shows "Estimate after inspection".
PRICE_SRC = {
    'ac_repair': None, 'ac_servicing': None, 'ac_install': None, 'ac_uninstall': None,
    'ac_gas': None, 'ac_deepclean': None, 'fridge': None, 'washer': None, 'cooler': None, 'fan': None,
}
PRICE_MARKUP = 100

# Images: original BOBBY artwork in static/assets/img/art (regenerate with: python3 art.py)
# Trust figures shown under the hero (as provided by the business owner). Keep these accurate.
STATS = [('500', '+', 'stat.cust', 'heart'), ('7', '+', 'stat.years', 'shield'), ('10', '+', 'stat.brands', 'layers'), ('24/7', '', 'stat.support', 'phone')]
GOOGLE_REVIEW_URL = 'https://g.page/r/CdusD2XE5xNnEBM/review'   # paste your Google Business Profile review link here once you have it
# Temporary: show clearly labelled SAMPLE reviews until genuine reviews are added to REVIEWS (then set False).
SHOW_SAMPLE_REVIEWS = True
OWNER_NAME = 'Yalamanda Gogasani'
OWNER_EMAIL = 'Yalamandagogasani@gmail.com'
REVIEWS = []   # genuine reviews only: {'name': 'Customer name', 'area': 'Narasaraopet', 'service': 'AC Repair', 'rating': 5, 'text': 'exact words', 'google': True}

# SAMPLE reviews (labelled "SAMPLE" on every card) shown on the home page while SHOW_SAMPLE_REVIEWS is True.
# Replace with genuine customer reviews in REVIEWS and set SHOW_SAMPLE_REVIEWS = False before relying on them.
DEMO_REVIEWS = [{'name': n, 'area': a, 'service': s, 'rating': r, 'text': t, 'source': 'demo'} for n, a, s, r, t in [
    ('Ravi K.', 'Prakash Nagar', 'AC Repair', 5, "AC suddenly stopped cooling on a hot afternoon. Called around 3 pm and the technician reached by evening. Found the capacitor was gone, replaced it and showed me the old one too. Back to normal in under an hour."),
    ('Lakshmi P.', 'Arundelpet', 'AC Servicing', 5, "Got both bedroom ACs serviced before summer. They covered the wall and floor properly before the jet wash, so no mess at all. Cooling is noticeably better now. Thank you BOBBY team, will call you again next year."),
    ('Srinivas R.', 'Barampet', 'AC Installation', 5, "Bought a new split AC and was worried about the installation. They fixed the outdoor unit firmly, kept the pipes neat and checked the drain before leaving. Clean work."),
    ('Anusha M.', 'Ramireddypet', 'AC Uninstallation', 4, "We were shifting houses and needed the AC removed carefully. They pumped down the gas first and packed the pipes properly. Came a little later than the time given, but the work was good."),
    ('Venkatesh B.', 'Palnadu Road', 'AC Gas Filling', 5, "Another shop just refilled gas last year and it leaked again in two months. This time they found the leak at the joint, fixed it and only then filled gas. No problem since."),
    ('Padma S.', 'Satyanarayana Puram', 'AC Cooling Problem', 5, "AC was running all day but the room never got cold. They checked and said the coil was fully blocked with dust. After cleaning, the room cools within 10 minutes. Didn't push any unnecessary parts."),
    ('Naresh G.', 'Kotappakonda Road', 'Refrigerator Repair', 5, "Fridge stopped cooling and we had milk and vegetables inside. Technician came the same day, changed the thermostat and told the price before starting. Very thankful for the quick help."),
    ('Sujatha V.', 'Islampet', 'Washing Machine Repair', 4, "Washing machine drum was not spinning. Belt was worn out, they replaced it and ran a full cycle to check. Good work, reasonable charges."),
    ('Ramesh T.', 'Chilakaluripet Road', 'Air Cooler Repair', 5, "Cooler fan was running but no water flow on the pads. Pump was gone. Replaced the same visit and cleaned the tank also. Simple and honest service."),
    ('Kavitha N.', 'Vinukonda Road', 'Ceiling Fan Repair', 5, "Hall fan was very slow and making noise. Capacitor changed and bearing oiled, now it runs quietly at full speed. Didn't expect such small work to be taken so seriously."),
    ('Mahesh Y.', 'Narasaraopet', 'AC Repair', 5, "Outdoor unit kept tripping the MCB. They traced it to a loose wire and fixed it properly. Explained everything clearly. Thanks a lot, saved me from buying a new stabiliser."),
    ('Divya L.', 'Gurazala Road', 'AC Servicing', 5, "Booked on WhatsApp in the morning, technician came on time in the afternoon. Polite, cleaned up after the work and shared photos of the filters before and after."),
]]

BRANDS = ['LG', 'Daikin', 'Blue Star', 'Samsung', 'Panasonic', 'Hitachi', 'Carrier', 'Godrej', 'Haier', 'Voltas']
# ======================================================

for k, v in add_strings.items(): S[k] = v
from sp_strings import SP
for k, v in SP.items(): S[k] = v
from asm_strings import ASM
for k, v in ASM.items(): S[k] = v
from asm2_strings import A2
for k, v in A2.items(): S[k] = v
from seo_strings import SEO, PRIV_EXTRA
from about_strings import AB
for k, v in AB.items(): S[k] = v
for k, v in SEO.items(): S[k] = v
def _priv_add(body, extra):              # add hosting / image-source disclosure after the third-party paragraph
    i = body.find('Google Fonts'); j = body.find('</p>', i) if i >= 0 else -1
    return body[:j + 4] + extra + body[j + 4:] if j >= 0 else body + extra
S['priv.body'] = tuple(_priv_add(b_, e_) for b_, e_ in zip(S['priv.body'], PRIV_EXTRA))
def fmt_date(d):
    import datetime as _d; return _d.date.fromisoformat(d).strftime('%d %b %Y').lstrip('0')
def quick_answer(k):
    return (f'<section class="sec qa-sec"><div class="wrap"><div class="qa-box reveal"><p class="qa-label">{tx("qa.label")}</p>'
            f'<h2 class="qa-q">{tx("qa.%s.q" % k)}</h2><p class="qa-a">{tx("qa.%s.a" % k)}</p></div></div></section>')
import sp_page
for p in POSTS:
    for f in ('title', 'excerpt', 'body'):
        v = p[f]
        S['post.%s.%s' % (p['slug'], f)] = v if isinstance(v, tuple) else (v, v, v)

def en(key): return S[key][0]
def plain(key): return html.unescape(strip_tags(S[key][0]))
def strip_tags(s):
    import re; return re.sub(r'<[^>]+>', '', s)
def tx(key, tag='span', cls='', attrs=''):
    c = f' class="{cls}"' if cls else ''
    a = f' {attrs}' if attrs else ''
    return f'<{tag}{c}{a} data-i18n="{key}">{en(key)}</{tag}>'
def esc(s): return html.escape(s, quote=True)
def wa_default(): return 'https://wa.me/%s?text=%s' % (WA_NUM, __import__('urllib.parse').parse.quote(html.unescape(en('wa.default'))))
def wa_service(svc):
    from urllib.parse import quote
    msg = html.unescape(en('wa.service')).replace('{service}', html.unescape(strip_tags(en('svc.%s.name' % svc))))
    return 'https://wa.me/%s?text=%s' % (WA_NUM, quote(msg))

ART_W = {'about-photo': 1536, 'why': 1200}
def art_url(key, size='lg'): return f'/assets/img/art/{key}-{size}.webp'
def img(key, w, h, alt_key, eager=False, cls='', sizes='(max-width: 640px) 100vw, (max-width: 1100px) 50vw, 600px'):
    """Original BOBBY artwork (WebP, 2 sizes)."""
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    full = ART_W.get(key, 1600)
    alt = esc(plain(alt_key))
    return (f'<img{c} src="{art_url(key)}" srcset="{art_url(key, "sm")} {full//2}w, {art_url(key)} {full}w" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{alt}" data-i18n-alt="{alt_key}" {load} decoding="async">')

def price(key, style='card'):
    v = PRICE_SRC.get(key)
    if v is None:
        if style == 'tag': return ''
        return f'<p class="price">{tx("price.onvisit")}</p>'
    amt = '₹{:,}'.format(v + PRICE_MARKUP)
    if style == 'tag':
        return f'<span class="pricetag">{tx("price.from","small")}<b>{amt}</b></span>'
    return f'<p class="price">{tx("price.from")} <b>{amt}</b></p>'
def any_price(): return any(v is not None for v in PRICE_SRC.values())

# ---------------- icons ----------------
ICONS = {
 'phone': '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z" fill="currentColor"/>',
 'chat': '<path d="M12 3C6.8 3 2.7 6.7 2.7 11.3c0 1.9.7 3.6 1.9 5L3.5 21l4.9-1.5c1.1.4 2.3.6 3.6.6 5.2 0 9.3-3.7 9.3-8.3S17.2 3 12 3z" fill="currentColor"/><circle cx="8" cy="11.4" r="1.25" fill="#fff"/><circle cx="12" cy="11.4" r="1.25" fill="#fff"/><circle cx="16" cy="11.4" r="1.25" fill="#fff"/>',
 'pin': '<path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z" fill="currentColor"/>',
 'globe': '<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z" fill="none" stroke="currentColor" stroke-width="2"/>',
 'chev': '<path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>',
 'arrow': '<path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
 'search': '<circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M16 16l4.5 4.5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
 'plus': '<path d="M12 5v14M5 12h14" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>',
 'info': '<circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 11v6M12 7.5v.5" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>',
 'check': '<path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>',
 'snow': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M12 2v20M3.3 7l17.4 10M3.3 17l17.4-10"/><path d="M9.5 4L12 6.5 14.5 4M9.5 20l2.5-2.5 2.5 2.5M4 10.3l3.4.9-.9 3.4M20 13.7l-3.4-.9.9-3.4M4.9 15.3l3.4-.9-.9-3.4M19.1 8.7l-3.4.9.9 3.4"/></g>',
 'ac': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="4.5" width="19" height="8.5" rx="2.5"/><path d="M6 10h12M7.5 16.5q-1 2 0 4M12 16.5q-1 2 0 4M16.5 16.5q-1 2 0 4"/></g>',
 'wrench': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3.6 17.2a1.6 1.6 0 0 0 2.3 2.3l5.7-5.7a4 4 0 0 0 5.2-5.4l-2.4 2.4-2.1-.6-.6-2.1z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 'install': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3.5" width="18" height="7" rx="2"/><path d="M12 13.5v7M8.5 17l3.5 3.5 3.5-3.5"/></g>',
 'uninstall': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="13.5" width="18" height="7" rx="2"/><path d="M12 10.5v-7M8.5 7L12 3.5 15.5 7"/></g>',
 'gauge': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 17a8 8 0 1 1 16 0"/><path d="M12 17l4-5"/><circle cx="12" cy="17" r="1.6" fill="currentColor"/><path d="M6.5 11l1 .8M12 7.5V9M17.5 11l-1 .8"/></g>',
 'fridge': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5.5" y="2.5" width="13" height="19" rx="2.5"/><path d="M5.5 9.5h13M8.5 5.5v2M8.5 12.5v4"/></g>',
 'washer': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="2.5" width="17" height="19" rx="2.5"/><path d="M3.5 7h17"/><circle cx="12" cy="14" r="4.5"/><circle cx="16.8" cy="4.8" r=".6" fill="currentColor"/></g>',
 'cooler': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="5.5" y="2.5" width="13" height="19" rx="3"/><path d="M8.5 6h7M8.5 9h7M8.5 12h7"/><circle cx="12" cy="17.5" r="1.4"/></g>',
 'bolt': '<path d="M13 2.5L4.5 13.5H11l-1 8 8.5-11H12z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 'eye': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></g>',
 'fan': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v5"/><circle cx="12" cy="10" r="2.2"/><path d="M10 10C6 9 3 10 2 11.5c3 1 6 .5 8 0M14 10c4-1 7 0 8 1.5-3 1-6 .5-8 0M12 12.2c-.5 3.5.5 7 1.8 8.3 1-2.6.4-5.8-.3-8.3"/></g>',
 'home': '<path d="M3 11l9-7 9 7v9a1.5 1.5 0 0 1-1.5 1.5H15v-6H9v6H4.5A1.5 1.5 0 0 1 3 20z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 'user': '<circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="2"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 7l9 6 9-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 'shield': '<path d="M12 2.5l8 3.5v6c0 5-3.4 8.6-8 10-4.6-1.4-8-5-8-10V6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M8.5 12l2.5 2.5 4.5-5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 'layers': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></g>',
 'talk': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M19 9h1a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2h-1v3l-4-3h-3"/></g>',
 'rupee': '<path d="M7 4h10M7 8.5h10M10 4c4.5 0 4.5 8 0 8H7l8 8" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>',
 'heart': '<path d="M12 20s-7.5-4.6-7.5-10.2A4.3 4.3 0 0 1 12 7a4.3 4.3 0 0 1 7.5 2.8C19.5 15.4 12 20 12 20z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 'cal': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3.5" y="5" width="17" height="15.5" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4M8.5 14.5l2.3 2.3 4.7-4.6"/></g>',
 'target': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="7"/><circle cx="12" cy="12" r="2.5" fill="currentColor"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></g>',
 'radius': '<g fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9" stroke-dasharray="3 3"/><circle cx="12" cy="12" r="2.5" fill="currentColor"/></g>',
}
def wa_ic(cls='wa-ic'):
    return f'<img class="{cls}" src="/assets/img/whatsapp.png" width="22" height="22" alt="" aria-hidden="true">'

def ic(name, cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
SVC_ICON = {'ac_repair':'wrench','ac_servicing':'ac','ac_install':'install','ac_uninstall':'uninstall','ac_gas':'gauge',
            'fridge':'fridge','washer':'washer','cooler':'cooler','fan':'fan'}

NAV = [('/', 'nav.home', 'home'), ('/about/', 'nav.about', 'about'), ('/ac-services/', 'nav.ac', 'ac'),
       ('/appliance-services/', 'nav.appliance', 'app'), ('/brands/', 'nav.brands', 'brands'),
       ('/faqs/', 'nav.faqs', 'faqs'), ('/contact/', 'nav.contact', 'contact')]


# ---------------- booking form (used on Contact page and in the pop-up opened by every Book button) ----------------
def booking_form(p, inline=False):
    def opt(v, k): return f'<option value="{v}" data-i18n="{k}">{en(k)}</option>'
    def legend(n, k): return f'<legend><span class="fnum">{n}</span><span data-i18n="{k}">{en(k)}</span></legend>'
    cls = 'form bookform reveal d2' if inline else 'form bookform'
    hid = ' id="book"' if inline else ''
    clock = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7.5V12l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
    lock = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="10.5" width="14" height="10" rx="2.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
    return f'''<form class="{cls}"{hid} novalidate data-prefix="{p}">
<div class="fhead"><div class="fhead-top"><h2 id="{p}Title">{tx('f.h')}</h2><span class="ftime">{clock}<span data-i18n="f.time">{en('f.time')}</span></span></div></div>
<div class="hp" aria-hidden="true"><label>Leave empty<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>
<fieldset class="fgrp">{legend(1, 'f.g1')}
<div class="frow"><div class="field"><label for="{p}Name">{tx('f.name')} <span class="req">*</span></label><input id="{p}Name" name="name" autocomplete="name" maxlength="60" required placeholder="{esc(plain('f.ph.name'))}" data-i18n-ph="f.ph.name"><p class="emsg"></p></div>
<div class="field"><label for="{p}Phone">{tx('f.phone')} <span class="req">*</span></label><div class="phone-wrap"><span class="cc" aria-hidden="true">+91</span><input id="{p}Phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel-national" maxlength="10" pattern="[6-9][0-9]{{9}}" required placeholder="98765 43210"><span class="pcount" aria-hidden="true"></span></div><p class="emsg"></p></div></div>
</fieldset>
<fieldset class="fgrp">{legend(2, 'f.g2')}
<div class="frow"><div class="field"><label for="{p}Appliance">{tx('f.appliance')} <span class="req">*</span></label><select id="{p}Appliance" name="appliance" required><option value="" data-i18n="f.select">{en('f.select')}</option>{opt('split','f.opt.splitac')}{opt('window','f.opt.windowac')}{opt('fridge','f.opt.fridge')}{opt('washer','f.opt.washer')}{opt('cooler','f.opt.cooler')}{opt('fan','f.opt.fan')}</select><p class="emsg"></p></div>
<div class="field"><label for="{p}Service">{tx('f.service')} <span class="req">*</span></label><select id="{p}Service" name="service" required><option value="" data-i18n="f.select">{en('f.select')}</option>{opt('repair','f.opt.repair')}{opt('service','f.opt.service')}{opt('install','f.opt.install')}{opt('uninstall','f.opt.uninstall')}{opt('gas','f.opt.gas')}{opt('notsure','f.opt.notsure')}</select><p class="emsg"></p></div></div>
<div class="field"><label for="{p}Brand">{tx('f.brand')}</label><input id="{p}Brand" name="brand" maxlength="40" placeholder="{esc(plain('f.ph.brand'))}" data-i18n-ph="f.ph.brand"><p class="emsg"></p></div>
</fieldset>
<fieldset class="fgrp">{legend(3, 'f.g3')}
<div class="field loc-field"><span class="flabel">{tx('f.loc')}</span>
<div class="loc-btns"><button type="button" class="btn btn-line btn-sm loc-cur">{ic('target')}{tx('f.loc.cur')}</button><button type="button" class="btn btn-line btn-sm loc-map">{ic('pin')}{tx('f.loc.map')}</button></div>
<div class="loc-status" role="status" aria-live="polite"></div>
<input type="hidden" name="lat"><input type="hidden" name="lng"><input type="hidden" name="addr"><p class="hint">{tx('f.loc.note')}</p></div>
<div class="frow"><div class="field"><label for="{p}Area">{tx('f.area')} <span class="req">*</span></label><input id="{p}Area" name="area" maxlength="120" required placeholder="{esc(plain('f.ph.area'))}" data-i18n-ph="f.ph.area"><p class="emsg"></p></div>
<div class="field"><label for="{p}Date">{tx('f.date')}</label><input id="{p}Date" name="date" type="date"><p class="emsg"></p></div></div>
</fieldset>
<fieldset class="fgrp">{legend(4, 'f.g4')}
<div class="field"><label for="{p}Msg">{tx('f.msg')}</label><textarea id="{p}Msg" name="msg" rows="3" maxlength="500" placeholder="{esc(plain('f.ph.msg'))}" data-i18n-ph="f.ph.msg"></textarea></div>
</fieldset>
<div class="fsubmit"><button class="btn btn-wa" type="submit">{wa_ic()}{tx('f.submit')}</button><p class="fsecure">{lock}<span data-i18n="f.secure">{en('f.secure')}</span></p><p class="fprivacy">{ic('info')}{tx('f.note')}</p></div><p class="form-msg" role="status" aria-live="polite"></p>
<div class="book-done" hidden tabindex="-1"><span class="bd-ic">{ic('check')}</span>{tx('f.thanks.h', 'h3')}{tx('f.thanks.p', 'p')}<p class="bd-sign" data-i18n="f.thanks.sign">{en('f.thanks.sign')}</p><p class="bd-tip">{tx('f.thanks.tip')}</p>
<div class="bd-btns"><a class="btn btn-wa bd-again" href="#" target="_blank" rel="noopener">{wa_ic()}{tx('f.thanks.again')}</a><button type="button" class="btn btn-line bd-new">{tx('f.thanks.new')}</button></div><p class="bd-alt">{tx('wa.alt.h', 'b')} <a class="bd-sms" href="sms:+918374889163">{tx('wa.sms')}</a><a class="bd-tel" href="tel:+918374889163">{tx('wa.call')}: +91 83748 89163</a></p></div></form>'''

def modals():
    return f'''<div class="modal" id="bookModal" aria-hidden="true"><div class="modal-bg" data-close-modal></div>
<div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="mTitle"><button type="button" class="modal-x" data-close-modal aria-label="{esc(plain('f.close'))}" data-i18n-aria="f.close">×</button>{booking_form('m')}</div></div>
<div class="modal" id="mapModal" aria-hidden="true"><div class="modal-bg" data-close-modal></div>
<div class="modal-panel map-panel" role="dialog" aria-modal="true" aria-labelledby="mapTitle"><button type="button" class="modal-x" data-close-modal aria-label="{esc(plain('f.close'))}" data-i18n-aria="f.close">×</button>
<h2 id="mapTitle">{tx('map.title')}</h2>
<div class="map-search" role="search"><input type="search" autocomplete="off" enterkeyhint="search" placeholder="{esc(plain('map.search'))}" data-i18n-ph="map.search" aria-label="{esc(plain('map.search'))}" data-i18n-aria="map.search" aria-autocomplete="list" aria-controls="mapSug"><button class="btn btn-primary btn-sm map-go" type="button">{tx('map.go')}</button><ul class="map-sug" id="mapSug" role="listbox" hidden></ul></div>
<p class="map-hint">{tx('map.hint')}</p><div class="pick-wrap"><div id="pickMap" class="pick-map"></div><span class="pick-pin" aria-hidden="true">{ic('pin')}</span><div class="map-layers"><button type="button" class="on" data-layer="street">{tx('map.street')}</button><button type="button" data-layer="sat">{tx('map.sat')}</button></div></div>
<p class="map-addr" aria-live="polite"></p><p class="map-msg" role="status" aria-live="polite"></p>
<div class="modal-foot"><button type="button" class="btn btn-line btn-sm map-me">{ic('target')}{tx('map.me')}</button><button type="button" class="btn btn-primary map-use">{ic('check')}{tx('map.use')}</button></div></div></div>'''

def book_a(svc, cls, key='btn.book', icon=None):
    return f'<a class="btn {cls}" href="/contact/#book" data-book="{svc}">{wa_ic()}{tx(key)}</a>'

# ---------------- layout ----------------
def business_ld():
    return {
        '@context': 'https://schema.org', '@type': 'HVACBusiness', '@id': SITE + '/#business',
        'name': BRAND, 'alternateName': 'Bobby AC Repair', 'url': SITE + '/',
        'telephone': PHONE_TEL, 'image': SITE + '/assets/img/og-image.jpg', 'logo': SITE + '/assets/img/bobby-logo-640.webp',
        'slogan': en('brand.tagline'),
        'address': {'@type': 'PostalAddress', 'streetAddress': ADDRESS['street'], 'addressLocality': ADDRESS['locality'], 'postalCode': ADDRESS['postal'], 'addressRegion': REGION, 'addressCountry': 'IN'},
        'openingHoursSpecification': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], 'opens': '00:00', 'closes': '23:59'},
        'hasMap': GMAPS_URL, 'geo': {'@type': 'GeoCoordinates', 'latitude': GEO[0], 'longitude': GEO[1]}, 'sameAs': [GMAPS_URL],
        'areaServed': [{'@type': 'City', 'name': CITY}, {'@type': 'GeoCircle', 'geoMidpoint': {'@type': 'GeoCoordinates', 'latitude': GEO[0], 'longitude': GEO[1]}, 'geoRadius': '20000'}],
        'email': OWNER_EMAIL,
        'founder': {'@type': 'Person', 'name': OWNER_NAME, 'alternateName': 'Bobby'},
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'AC & Home Appliance Services', 'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': n, 'url': SITE + u}} for n, u in [
                ('AC Installation', '/ac-services/#ac-installation'), ('AC Uninstallation', '/ac-services/#ac-uninstallation'), ('AC Repair', '/ac-services/#ac-repair'),
                ('AC Servicing', '/ac-services/#ac-servicing'), ('AC Gas Filling', '/ac-services/#ac-gas-filling'), ('AC Deep Cleaning', '/ac-services/#ac-deep-cleaning'),
                ('Refrigerator Repair', '/appliance-services/#refrigerator'), ('Washing Machine Repair', '/appliance-services/#washing-machine'),
                ('Air Cooler Repair', '/appliance-services/#air-cooler'), ('Ceiling Fan Repair', '/appliance-services/#ceiling-fan')]]},
        'knowsLanguage': ['en', 'te', 'hi'],
    }
def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}

import hashlib as _hl
I18N_V = _hl.md5(json.dumps(S, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:8]

def head(title, desc, path, title_key=None, ld=(), og_img=None):
    url = SITE + path
    og = og_img or SITE + '/assets/img/og-image.jpg'
    tk = f' data-title-key="{title_key}"' if title_key else ''
    lds = ''.join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in ld)
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js" data-iv="{I18N_V}"{tk}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#102C50">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(BRAND)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/img/icon-192.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&display=swap"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&display=swap" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&display=swap"></noscript>
<link rel="stylesheet" href="/assets/css/style.css?v=46">
<script>try{{var l=localStorage.getItem('bobby-lang');if(l==='te'||l==='hi')document.documentElement.lang=l}}catch(e){{}}</script>
{lds}</head>
<body>
<a class="skip" href="#main" data-i18n="skip">{en('skip')}</a>
'''

def lang_switch():
    return f'''<div class="lang">
<button class="lang-btn" type="button" aria-haspopup="true" aria-expanded="false">{ic('globe')}<span class="sr-only">Language / భాష / भाषा: </span><span class="code lang-code">EN</span>{ic('chev','chev')}</button>
<ul class="lang-menu" role="menu">
<li><button type="button" role="menuitemradio" aria-checked="true" data-lang="en">English</button></li>
<li><button type="button" role="menuitemradio" aria-checked="false" data-lang="te" class="te" lang="te">తెలుగు</button></li>
<li><button type="button" role="menuitemradio" aria-checked="false" data-lang="hi" class="hi" lang="hi">हिन्दी</button></li>
</ul></div>'''

def header(active):
    links = ''.join(f'<a href="{u}"{" aria-current=\"page\"" if a == active else ""}>{tx(k)}</a>' for u, k, a in NAV if a != 'brands')  # Brands is in the footer + home page only
    return f'''<div class="topbar"><div class="wrap">
<span class="tb-owner">{ic('user')}<b>{OWNER_NAME}</b><i class="tb-sep">|</i><span data-i18n="pre.known">{en('pre.known')}</span> <b class="tb-bobby">Bobby</b><i class="tb-sep">·</i><a class="tb-mail" href="mailto:{OWNER_EMAIL}">{ic('mail')}{OWNER_EMAIL}</a></span>
<span class="tb-right">{ic('pin')}{tx('loc.short')} · {tx('hours.open')} · {ic('phone')}<a href="tel:{PHONE_TEL}">{PHONE_TXT}</a> · <a href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{tx('btn.wa')}</a></span>
</div></div>
<header class="hdr">
<div class="wrap">
<a class="logo" href="/" aria-label="BOBBY AC Repair &amp; Home Appliance Services – Home"><img class="wm" src="/assets/img/bobby-wordmark.webp" width="142" height="56" fetchpriority="high" alt="BOBBY AC Repair &amp; Home Appliance Services"></a>
<nav class="nav" aria-label="Main">{links}</nav>
<div class="hdr-actions">
{lang_switch()}
<a class="hbtn hbtn-call" href="tel:{PHONE_TEL}" aria-label="{esc(plain('btn.call'))} {PHONE_TXT}"><span class="hb-ic">{ic('phone')}</span><span class="lbl"><small data-i18n="btn.call">{en('btn.call')}</small><b>{PHONE_TXT}</b></span></a>
<a class="hbtn hbtn-book" href="/contact/#book" data-book="" aria-label="{esc(plain('btn.bookservice'))}" data-i18n-aria="btn.bookservice"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 3v4M16 3v4M3.5 10h17M9 15l2 2 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span class="lbl" data-i18n="btn.bookservice">{en('btn.bookservice')}</span></a>
<button class="burger" type="button" aria-controls="drawer" aria-expanded="false" aria-label="{esc(plain('nav.menu'))}" data-i18n-aria="nav.menu"><span></span></button>
</div></div></header>
<div class="drawer" id="drawer" aria-hidden="true">
<div class="drawer-bg" data-close></div>
<div class="drawer-panel" role="dialog" aria-modal="true" aria-label="{esc(plain('nav.menu'))}">
<div class="drawer-top"><a class="logo" href="/"><img class="wm" src="/assets/img/bobby-wordmark.webp" width="142" height="56" alt="BOBBY AC Repair &amp; Home Appliance Services"></a><button class="drawer-x" type="button" data-close aria-label="{esc(plain('nav.close'))}" data-i18n-aria="nav.close">×</button></div>
<nav aria-label="Mobile">{links}<a href="/blog/"{" aria-current=\"page\"" if active == "blog" else ""}>{tx('nav.blog')}</a></nav>
<div class="btns"><a class="btn btn-primary" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}</a>{book_a('', 'btn-wa', 'btn.bookservice')}</div>
</div></div>
<main id="main">
'''

def footer():
    q = ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' for u, k, a in NAV if a != 'ac') + f'<li><a href="/blog/">{tx("nav.blog")}</a></li>'  # AC Services has its own column
    acl = [('/ac-services/#ac-repair','svc.ac_repair.name'),('/ac-services/#ac-servicing','svc.ac_servicing.name'),
           ('/ac-services/#ac-installation','svc.ac_install.name'),('/ac-services/#ac-uninstallation','svc.ac_uninstall.name'),
           ('/ac-services/#ac-gas-filling','svc.ac_gas.name'),('/ac-services/#ac-deep-cleaning','ft.maint'),('/ac-spare-parts/','ft.parts')]
    a = ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' for u, k in acl)
    return f'''</main>
<footer class="ftr">
<div class="wrap grid">
<div><a class="logo" href="/"><img loading="lazy" class="wm" src="/assets/img/bobby-wordmark.webp" width="142" height="56" alt="BOBBY AC Repair &amp; Home Appliance Services"></a>
<p class="desc">{tx('ft.about')}</p><p class="tag">{tx('brand.tagline')}</p></div>
<div><h3>{tx('ft.quick')}</h3><ul>{q}</ul></div>
<div><h3>{tx('ft.ac')}</h3><ul>{a}</ul></div>
<div><h3>{tx('ft.contact')}</h3><ul>
<li class="ci">{ic('phone')}<a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></li>
<li class="ci">{wa_ic()}<a href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{tx('c.wa.h')}</a></li>
<li class="ci">{ic('pin')}<a href="{GMAPS_URL}" target="_blank" rel="noopener">{tx('addr.full')}</a></li><li class="ci">{ic('star')}{tx('hours.open')}</li>
<li class="ci">{ic('radius')}{tx('ft.area')}</li></ul></div>
<div class="bottom" style="grid-column:1/-1">
<div>© <span class="yr">2026</span> BOBBY AC Repair &amp; Home Appliance Services. {tx('ft.rights')}<p class="indep">{tx('ft.indep')}</p></div>
<nav aria-label="Legal"><a href="/privacy-policy/">{tx('ft.privacy')}</a><a href="/terms/">{tx('ft.terms')}</a><a href="/sitemap/">{tx('ft.sitemap')}</a></nav>
</div></div></footer>
<div class="fab"><a class="w" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener" aria-label="{esc(plain('btn.wachat'))}" data-i18n-aria="btn.wachat">{wa_ic()}</a><a class="c" href="tel:{PHONE_TEL}" aria-label="{esc(plain('btn.call'))}" data-i18n-aria="btn.call">{ic('phone')}</a></div>
<div class="mbar"><a class="c" href="tel:{PHONE_TEL}">{ic('phone')}{tx('mbar.call')}</a><a class="w" href="/contact/#book" data-book="">{wa_ic()}{tx('mbar.book')}</a></div>
{modals()}
<script src="/assets/js/main.js?v=17" defer></script>
</body></html>
'''

def phero(h1key, subkey, trail):
    items = ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' if i < len(trail) - 1 else f'<li aria-current="page">{tx(k)}</li>'
                    for i, (k, u) in enumerate(trail))
    sub = f'<p>{tx(subkey, "span")}</p>' if subkey else ''
    return f'''<section class="phero"><div class="wrap">
<nav class="crumbs anim" aria-label="Breadcrumb"><ol>{items}</ol></nav>
<h1 class="anim d1">{tx(h1key, "span")}</h1>{sub.replace("<p>", "<p class=\"anim d2\">", 1)}
</div></section>'''

def sec_head(eb, h2, sub=None, center=True):
    s = f'<p class="lead">{tx(sub, "span")}</p>' if sub else ''
    return f'<div class="sec-head{" center" if center else ""} reveal"><p class="eyebrow">{tx(eb, "span")}</p><h2>{tx(h2, "span")}</h2>{s}</div>'

# ---------------- sections ----------------
def quick_cards():
    out = []
    for i, s in enumerate(SERVICES):
        appc = ' app' if s in ('fridge', 'washer', 'cooler', 'fan') else ''
        out.append(f'''<article class="qcard reveal d{i % 4}{appc}">
<div class="ic">{ic(SVC_ICON[s])}</div><h3>{tx("svc.%s.name" % s)}</h3><p>{tx("svc.%s.desc" % s)}</p>{price(s)}
{book_a(s, 'btn-wa btn-sm')}</article>''')
    return '<div class="quick-grid">' + ''.join(out) + '</div>'

AC_BLOCKS = [  # letter, anchor, photo key, svc key for booking, bullet count, price key
    ('A', 'ac-repair', 'ac_repair', 'ac_repair', 6, 'ac_repair'),
    ('B', 'ac-servicing', 'ac_servicing', 'ac_servicing', 5, 'ac_servicing'),
    ('C', 'ac-installation', 'ac_install', 'ac_install', 4, 'ac_install'),
    ('D', 'ac-uninstallation', 'ac_uninstall', 'ac_uninstall', 3, 'ac_uninstall'),
    ('E', 'ac-gas-filling', 'ac_gas', 'ac_gas', 4, 'ac_gas'),
    ('F', 'ac-deep-cleaning', 'ac_deepclean', 'ac_servicing', 3, 'ac_deepclean'),
]
def ac_cards(featured_first=False, eager_first=False):
    out = []
    for i, (L, anchor, pk, sk, n, prk) in enumerate(AC_BLOCKS):
        lis = ''.join(f'<li>{tx("ac.%s.%d" % (L, j))}</li>' for j in range(1, n + 1))
        note = f'<p class="note">{ic("info")}{tx("ac.E.note")}</p>' if L == 'E' else ''
        feat = ' ac-featured' if (featured_first and i == 0) else ''
        out.append(f'''<article class="scard reveal d{i % 3}{feat}" id="{anchor}">
<div class="media">{img(pk, 960 if feat else 640, 600 if feat else 400, "ac.%s.t" % L, eager=bool(feat) or (eager_first and i == 0))}<span class="tag">{tx("ac.%s.t" % L)}</span>{price(prk, "tag")}</div>
<div class="body"><h3>{tx("ac.%s.t" % L)}</h3><p>{tx("ac.%s.d" % L)}</p><ul class="ticks">{lis}</ul>{note}
<div class="actions">{book_a(sk, 'btn-primary btn-sm')}<a class="btn btn-line btn-sm" href="tel:{PHONE_TEL}">{ic('phone')}{tx("btn.call")}</a></div></div></article>''')
    pf = f'<p class="price-foot">{tx("price.note")}</p>' if any_price() else ''
    return '<div class="ac-grid">' + ''.join(out) + '</div>' + pf

AP_BLOCKS = [('fridge', 'refrigerator'), ('washer', 'washing-machine'), ('cooler', 'air-cooler'), ('fan', 'ceiling-fan')]
def app_cards(eager_first=False):
    out = []
    for i, (k, anchor) in enumerate(AP_BLOCKS):
        lis = ''.join(f'<li>{tx("ap.%s.%d" % (k, j))}</li>' for j in range(1, 4))
        out.append(f'''<article class="scard reveal d{i}" id="{anchor}">
<div class="media">{img(k, 600, 450, "ap.%s.t" % k, eager=eager_first and i == 0)}<span class="tag">{tx("svc.%s.name" % k)}</span>{price(k, "tag")}</div>
<div class="body"><h3>{tx("ap.%s.t" % k)}</h3><ul class="ticks">{lis}</ul>
<div class="actions">{book_a(k, 'btn-orange btn-sm')}</div></div></article>''')
    return '<div class="app-grid app">' + ''.join(out) + '</div>'

def brand_logo(name):
    slug = name.lower().replace(' ', '-')
    for ext in ('svg', 'webp', 'png'):
        if os.path.exists(os.path.join(os.path.dirname(__file__), 'static/assets/img/brands/%s.%s' % (slug, ext))):
            return f'<img src="/assets/img/brands/{slug}.{ext}" alt="{esc(name)}" loading="lazy" width="140" height="56">'
    return name
def brands_block(tiles_too=False):
    banner = f'''<figure class="brand-banner reveal"><img src="/assets/img/brands-banner-lg.webp" srcset="/assets/img/brands-banner-sm.webp 836w, /assets/img/brands-banner-lg.webp 1672w" sizes="(max-width: 1240px) 100vw, 1200px" width="1672" height="941" fetchpriority="high" decoding="async" alt="BOBBY AC Repair &amp; Home Appliance Services banner: we repair and service LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier and Voltas" data-i18n-alt="brands.banner"></figure>'''
    tiles = ''.join(f'<div class="brand reveal d{i % 4}">{brand_logo(b)}</div>' for i, b in enumerate(BRANDS))
    grid = f'<div class="brands" style="margin-top:22px">{tiles}</div>' if tiles_too else ''
    return f'''{banner}{grid}
<p class="brand-note reveal">{ic('info')}<span>{tx('brands.note')} <a class="link-arrow" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{tx('brands.ask')}</a></span></p>'''

WHY_ICONS = ['home', 'ac', 'layers', 'talk', 'rupee', 'chat', 'heart']
def why_cards():
    return '<div class="why-grid">' + ''.join(
        f'<div class="wcard reveal d{i % 4}"><div class="ic">{ic(WHY_ICONS[i])}</div><h3>{tx("why.%d.t" % (i + 1))}</h3><p>{tx("why.%d.d" % (i + 1))}</p></div>'
        for i in range(6)) + '</div>'

def stats_block():
    items = ''.join(f'<div class="stat reveal d{i}"><span class="s-ic">{ic(icn)}</span><b><span class="count" data-to="{n if n.isdigit() else ""}">{n}</span>{suf}</b><small>{tx(k)}</small></div>' for i, (n, suf, k, icn) in enumerate(STATS))
    return f'<section class="stats-wrap" aria-label="Why customers trust us"><div class="wrap"><div class="stats">{items}</div></div></section>'

def steps_block():
    lis = ''.join(f'<li><span class="n">{i}</span><div><h3>{tx("how.%d.t" % i)}</h3><p>{tx("how.%d.d" % i)}</p></div></li>' for i in range(1, 5))
    return f'''<section class="sec steps" id="how"><div class="wrap">{sec_head("how.eyebrow", "how.h2")}<ol class="timeline">{lis}</ol></div></section>'''

TRUST = [('star', 1), ('home', 2), ('wrench', 3), ('rupee', 4), ('gauge', 5), ('layers', 6), ('shield', 7), ('heart', 8), ('check', 9), ('ac', 10), ('cal', 11)]
# ---- Reusable review carousel component ----
# Review fields: name, area (verified service location), rating (actual), text (original words),
# service (category), source: 'google' (genuinely posted on Google) or 'direct' (feedback given to us directly).
SOURCE_LABEL = {'google': 'Google review', 'direct': 'Direct customer feedback', 'demo': 'DEMO – sample only'}

def review_card(r):
    n = max(1, min(5, int(r.get('rating', 5))))
    src = r.get('source', 'direct')
    initial = esc((r.get('initial') or r['name'][:1]).upper())
    g = (f'<span class="rc-src rc-g" title="Posted on Google">{ic("check")}Google review</span>' if src == 'google'
         else f'<span class="rc-src rc-demo" data-i18n="rev.sample">{en("rev.sample")}</span>' if src == 'demo'
         else f'<span class="rc-src">{esc(SOURCE_LABEL["direct"])}</span>')
    return f'''<li class="rc-slide"><article class="rc-card">
<span class="rc-q" aria-hidden="true">“</span><header><span class="rc-av" aria-hidden="true">{initial}</span><span class="rc-who"><b>{esc(r["name"])}</b><small>{ic("pin")}{esc(r.get("area", ""))}</small></span>{g}</header>
<p class="rc-stars" role="img" aria-label="Rated {n} out of 5">{"<i>★</i>" * n}{"<i class=off>★</i>" * (5 - n)}</p>
<blockquote>{esc(r["text"])}</blockquote>
<footer><span class="rc-svc">{esc(r.get("service", ""))}</span></footer></article></li>'''

def review_carousel(reviews, label='Customer reviews'):
    if not reviews: return ''
    return f'''<div class="rc" data-rc role="region" aria-roledescription="carousel" aria-label="{esc(label)}">
<div class="rc-viewport"><ul class="rc-track">{''.join(review_card(r) for r in reviews)}</ul></div>
<div class="rc-nav"><button type="button" class="rc-btn rc-prev" aria-label="Previous reviews">{ic("arrow")}</button>
<div class="rc-dots" role="group" aria-label="Choose slide"></div>
<button type="button" class="rc-btn rc-next" aria-label="Next reviews">{ic("arrow")}</button></div></div>'''

def review_buttons():
    return (f'<div class="btn-row rc-cta"><a class="btn btn-primary" href="{GMAPS_URL}" target="_blank" rel="noopener">{ic("star")}{tx("rev.readall")}</a>'
            f'<a class="btn btn-line" href="{GOOGLE_REVIEW_URL}" target="_blank" rel="noopener">{tx("rev.write")}{ic("arrow")}</a></div>')

def reviews_block():
    """'What Our Customers Say' carousel. Genuine reviews when available; until then clearly labelled SAMPLE reviews."""
    if REVIEWS:
        body = review_carousel(REVIEWS)
    elif SHOW_SAMPLE_REVIEWS:
        body = review_carousel(DEMO_REVIEWS, 'Sample reviews')  # each card carries a SAMPLE badge
    else:
        body = f'<div class="rc-empty reveal"><p>{tx("rev.first")}</p></div>'
    return f'''<section class="sec rc-sec" id="reviews" data-nosnippet><div class="wrap">
<div class="sec-head center reveal"><p class="eyebrow">{tx("rev.eyebrow")}</p><h2>{tx("rev.h2")}</h2><p class="lead">{tx("rev.sub2")}</p></div>
{body}{review_buttons()}</div></section>'''

def location_block(h='h2'):
    return f'''<section class="sec sec-alt" id="service-area"><div class="wrap loc-grid">
<div class="reveal"><p class="eyebrow">{tx("loc.eyebrow")}</p><{h}>{tx("loc.h2")}</{h}><p style="margin-top:14px">{tx("loc.p1")}</p><p>{tx("loc.p2")}</p>
<ul class="cover"><li><span class="ci-ic">{ic('pin')}</span>{tx("addr.full")}</li><li><span class="ci-ic">{ic('star')}</span>{tx("hours.open")}</li><li><span class="ci-ic">{ic('radius')}</span>{tx("loc.c2")}</li><li><span class="ci-ic">{ic('phone')}</span>{tx("loc.c3")}</li></ul>
<div class="btn-row"><a class="btn btn-primary" href="tel:{PHONE_TEL}">{ic('phone')}{tx("btn.callnum")}</a><a class="btn btn-line" href="{DIR_URL}" target="_blank" rel="noopener">{ic('pin')}{tx("btn.dir")}</a></div></div>
<div class="map reveal d2"><iframe title="{esc(plain('loc.map'))}" data-i18n-aria="loc.map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe></div>
</div></section>'''

def acc_widget():
    """AC electricity cost calculator (FAQ page)."""
    return f'''<section class="sec sec-alt acc-sec" id="ac-electricity-cost-calculator"><div class="wrap acc-wrap">
<div class="acc-intro reveal"><p class="eyebrow">{ic('rupee')}<span data-i18n="acc.eb">{en('acc.eb')}</span></p><h2 id="accH">{tx('acc.h2')}</h2><p class="lead">{tx('acc.sub')}</p>
<p class="acc-note">{tx('acc.note')}</p><p class="acc-note">{tx('acc.tariffnote')}</p><p class="acc-note acc-tip">{ic('check')}{tx('acc.tip')}</p></div>
<form class="acc" id="acCalc" aria-labelledby="accH" onsubmit="return false">
<div class="acc-grid">
<label><span data-i18n="acc.cap">{en('acc.cap')}</span><select name="ton"><option value="1">1 Ton</option><option value="1.5" selected>1.5 Ton</option><option value="2">2 Ton</option></select></label>
<label><span data-i18n="acc.type">{en('acc.type')}</span><select name="type"><option value="inv" data-i18n="acc.inv">{en('acc.inv')}</option><option value="non" data-i18n="acc.noninv">{en('acc.noninv')}</option></select></label>
<label><span data-i18n="acc.hours">{en('acc.hours')}</span><input name="hours" type="number" inputmode="decimal" min="0" max="24" step="0.5" value="8"></label>
<label><span data-i18n="acc.days">{en('acc.days')}</span><input name="days" type="number" inputmode="numeric" min="1" max="31" step="1" value="30"></label>
<label><span data-i18n="acc.tariff">{en('acc.tariff')}</span><input name="tariff" type="number" inputmode="decimal" min="0" max="30" step="0.05" value="8.75"></label>
<label><span data-i18n="acc.watts">{en('acc.watts')}</span><input name="watts" type="number" inputmode="numeric" min="200" max="5000" step="10" placeholder="e.g. 1450"></label>
</div>
<output class="acc-out" name="out" for="acCalc" aria-live="polite">
<span class="acc-row"><span data-i18n="acc.day">{en('acc.day')}</span><b data-acc="ud">7.6</b> <small data-i18n="acc.units">{en('acc.units')}</small></span>
<span class="acc-row"><span data-i18n="acc.month">{en('acc.month')}</span><b data-acc="um">228</b> <small data-i18n="acc.units">{en('acc.units')}</small></span>
<span class="acc-row acc-big"><span data-i18n="acc.cost">{en('acc.cost')}</span><b data-acc="cm">₹1,995</b></span>
</output>
</form>
</div></section>
<script src="/assets/js/ac-cost.js?v=2" defer></script>'''

def faq_list(nums, first_open=True, hq='h3'):
    return '<div class="faq">' + ''.join(
        f'<details class="reveal"{" open" if (first_open and i == 0) else ""}><summary>{tx("faq.%d.q" % n, hq, attrs="style=\"font-size:inherit;color:inherit;font-weight:inherit\"")}<span class="pm">{ic("plus")}</span></summary><div class="ans">{tx("faq.%d.a" % n, "p")}</div></details>'
        for i, n in enumerate(nums)) + '</div>'

def post_body(post):
    """Article body. New long-form posts (English body) get a table of contents, FAQ, sources and a local contact box."""
    import re as _re
    s = post['slug']
    if isinstance(post['body'], tuple):
        return f'<div class="prose" data-i18n="post.{s}.body">{en("post.%s.body" % s)}</div>'
    body = post['body']; toc = []
    def _id(m):
        t = _re.sub(r'<[^>]+>', '', m.group(1)); i = _re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:60]
        toc.append((i, t)); return f'<h2 id="{i}">{m.group(1)}</h2>'
    body = _re.sub(r'<h2>(.*?)</h2>', _id, body)
    out = f'<p class="lang-note">{tx("blog.lang")}</p>'
    out += ('<nav class="post-toc" aria-label="Table of contents"><p class="post-toc-h">' + tx('blog.toc') + '</p><ul>' +
            ''.join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i, t in toc) + '</ul></nav>')
    out += f'<div class="prose" lang="en">{body}</div>'
    if post.get('local'):
        out += (f'<div class="post-local reveal"><h2>{tx("blog.local.h")}</h2><p>{tx("blog.local.p")}</p>'
                f'<p class="post-local-nap"><b>{esc(BRAND)}</b><br><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a> · Door 11-28-32/5, Employees Colony, Arundelpet, Narasaraopet, Palnadu District, Andhra Pradesh – 522601</p>'
                f'<div class="btn-row"><a class="btn btn-orange btn-sm" href="tel:{PHONE_TEL}">{ic("phone")}{tx("btn.callnum")}</a>'
                f'<a class="btn btn-wa btn-sm" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{wa_ic()}{tx("btn.wachat")}</a></div></div>')
    if post.get('faq'):
        out += ('<section class="post-faq" lang="en"><h2 id="faq">' + tx('blog.faqh') + '</h2><div class="faq">' +
                ''.join(f'<details><summary><h3 style="font-size:inherit;color:inherit;font-weight:inherit;margin:0">{esc(q)}</h3><span class="pm">{ic("plus")}</span></summary><div class="ans"><p>{esc(a)}</p></div></details>' for q, a in post['faq']) +
                '</div></section>')
    if post.get('sources'):
        def _a(label, url):
            ext = url.startswith('http')
            return f'<li><a href="{url}"' + (' target="_blank" rel="noopener"' if ext else '') + f'>{esc(label)}</a></li>'
        out += '<aside class="post-src" lang="en"><h2>' + tx('blog.src') + '</h2><ul>' + ''.join(_a(l, u) for l, u in post['sources']) + '</ul></aside>'
    return out

def blog_cards(posts, hq='h3', eager_first=False):
    return '<div class="blog-grid">' + ''.join(f'''<article class="bcard reveal d{i % 3}"><a class="media" href="/blog/{p['slug']}/" tabindex="-1" aria-hidden="true">{img(p['img'], 640, 360, 'post.%s.title' % p['slug'], eager=eager_first and i == 0)}</a>
<div class="body"><{hq}><a href="/blog/{p['slug']}/">{tx('post.%s.title' % p['slug'])}</a></{hq}><p>{tx('post.%s.excerpt' % p['slug'])}</p><a class="link-arrow" href="/blog/{p['slug']}/">{tx('btn.more')}<span class="sr-only">: {esc(plain('post.%s.title' % p['slug']))}</span>{ic('arrow')}</a></div></article>''' for i, p in enumerate(posts)) + '</div>'

CAL_SVG = '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15.5" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 3v4M16 3v4M3.5 10h17M9 15l2 2 4-4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CTA_ART = {   # page -> (image, side, object-position): every page gets its own picture in the same style
    'about': ('cta-ac-bobby', 'l', '35% 18%'), 'ac': ('cta-relax', 'r', '55% 40%'), 'app': ('cta-relax-mug', 'r', '62% 55%'),
    'brands': ('cta-3d-a', 'l', '50% 25%'), 'faqs': ('cta-ac-glow', 'l', '10% 22%'), 'blog': ('cta-3d-b', 'r', '50% 25%'),
}
def cta_band(page='ac'):
    """Shared call-to-action banner (artwork from BOBBY's own banner design; text and buttons are real HTML)."""
    art, side, pos = CTA_ART.get(page, CTA_ART['ac'])
    svg = lambda d: f'<svg viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
    S_ = 'fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"'
    icons = [svg(f'<path {S_} d="M14.7 6.3a4 4 0 0 0-5.3 5.3L3.5 17.5a1.8 1.8 0 0 0 2.5 2.5l5.9-5.9a4 4 0 0 0 5.3-5.3l-2.4 2.4-2.1-.4-.4-2.1z"/><path {S_} d="M4 4l5 5M3.5 6l2.5-2.5"/>'),
             svg(f'<circle {S_} cx="12" cy="12" r="3"/><path {S_} d="M12 2.8v2.4M12 18.8v2.4M2.8 12h2.4M18.8 12h2.4M5.5 5.5l1.7 1.7M16.8 16.8l1.7 1.7M5.5 18.5l1.7-1.7M16.8 7.2l1.7-1.7"/>'),
             svg(f'<rect {S_} x="6.5" y="6.5" width="11" height="15" rx="3"/><path {S_} d="M9.5 6.5V4h5v2.5M12 10.5v7M9 12.3l6 3.4M15 12.3l-6 3.4"/>'),
             svg(f'<path {S_} d="M12 2.8l7.5 3v5.6c0 4.7-3.2 8.3-7.5 9.8-4.3-1.5-7.5-5.1-7.5-9.8V5.8z"/><path {S_} d="M8.6 12.2l2.4 2.4 4.6-4.8"/>')]
    feats = ''.join(f'<li><span class="cta3-fi">{icons[i]}</span><span>{tx("cta3.f%d" % (i + 1))}</span></li>' for i in range(4))
    cal = svg(f'<rect {S_} x="3.5" y="5" width="17" height="15.5" rx="3"/><path {S_} d="M8 3v4M16 3v4M3.5 10h17"/><path fill="currentColor" d="M7 13h2.4v2.2H7zM10.8 13h2.4v2.2h-2.4zM14.6 13H17v2.2h-2.4zM7 16.6h2.4v2.2H7zM10.8 16.6h2.4v2.2h-2.4z"/>')
    return f'''<section class="cta-band"><div class="wrap"><div class="cta3 cta3-{side} reveal">
<div class="cta3-art" aria-hidden="true"><img src="/assets/img/{art}.webp" alt="" loading="lazy" decoding="async" style="object-position:{pos}"></div>
<div class="cta3-c">
<p class="cta3-pill"><span>{tx("cta3.pill")}</span></p>
<h2>{tx("cta3.h")}</h2>
<p class="cta3-sub">{tx("cta3.sub")}</p>
<ul class="cta3-feat">{feats}</ul>
</div>
<div class="cta3-bar">
<a class="cta3-book" href="/contact/#book" data-book="">{cal}<span data-i18n="cta3.book">{en("cta3.book")}</span></a>
<div class="cta3-callwa"><a class="cta3-wa" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener" aria-label="WhatsApp {PHONE_TXT}">{wa_ic()}</a>
<a class="cta3-tel" href="tel:{PHONE_TEL}"><small data-i18n="cta3.callwa">{en("cta3.callwa")}</small><b>{PHONE_TXT}</b></a></div>
</div>
</div></div></section>'''


# ---- Home: animated service slider ("2nd hero"). Appliance drawings are inline SVG so their parts can animate. ----
H2_SVG = json.load(open(os.path.join(os.path.dirname(__file__), 'art-src', 'hero2-svgs.json'), encoding='utf-8'))
H2_SLIDES = [('ac', 'COOL', '#102C50', '#1688D4', ['flake', 'ice', 'flake', 'ice', 'flake', 'ice', 'flake']),
             ('fridge', 'FRESH', '#0E6FB3', '#56C8FF', ['ice', 'flake', 'ice', 'ice', 'ice', 'flake', 'flake']),
             ('washer', 'CLEAN', '#0B1F3A', '#1688D4', ['bubble', 'drop', 'bubble', 'bubble', 'bubble', 'drop', 'bubble']),
             ('cooler', 'CHILL', '#102C50', '#0E6FB3', ['drop', 'ice', 'drop', 'drop', 'ice', 'drop', 'drop']),
             ('fan', 'BREEZE', '#0B1F3A', '#16477A', ['swirl'] * 7)]
H2_FL = [(16, 14, 74, .5, 0), (80, 12, 56, .4, 0), (24, 64, 48, .6, 0), (74, 62, 66, .55, 0), (6, 46, 130, 1.2, 7), (88, 36, 104, 1.0, 6), (58, 6, 34, .3, 0)]
H2_EXTRA = {
    'ac': '<svg class="bh2-air" viewBox="0 0 600 260" aria-hidden="true"><defs><linearGradient id="bh2-airgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E3F6FF" stop-opacity=".95"/><stop offset="1" stop-color="#56C8FF" stop-opacity="0"/></linearGradient></defs>'
          + ''.join(f'<path class="bh2-stream" style="--s:{i}" d="M{60+i*80} 0 C{40+i*80} 70 {110+i*80} 120 {80+i*80} 190 S{90+i*80} 250 {120+i*80} 260"/>' for i in range(7)) + '</svg><span class="bh2-mist"></span>',
    'fridge': '<span class="bh2-fog"><i></i><i></i><i></i></span>', 'washer': '',
    'cooler': '<span class="bh2-spray"><i></i><i></i><i></i><i></i><i></i></span>', 'fan': '<span class="bh2-ripple"><i></i><i></i><i></i></span>'}
H2_SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<linearGradient id="bh-g-ice" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".5" stop-color="#CFF0FF" stop-opacity=".7"/><stop offset="1" stop-color="#7FD6FF" stop-opacity=".55"/></linearGradient>
<radialGradient id="bh-g-drop" cx=".35" cy=".6" r=".7"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#BDEBFF"/><stop offset="1" stop-color="#56C8FF"/></radialGradient>
<radialGradient id="bh-g-bub" cx=".5" cy=".5" r=".5"><stop offset=".7" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".8"/></radialGradient>
<symbol id="bh-ice" viewBox="0 0 100 100"><path d="M22 30 L58 14 L86 32 L80 72 L44 88 L16 70Z" fill="url(#bh-g-ice)" stroke="#fff" stroke-opacity=".9" stroke-width="2"/><path d="M22 30 L52 46 L86 32 M52 46 L44 88" stroke="#fff" stroke-opacity=".7" stroke-width="2" fill="none"/><path d="M30 34 L48 26" stroke="#fff" stroke-width="5" stroke-linecap="round"/></symbol>
<symbol id="bh-flake" viewBox="0 0 100 100"><g stroke="#fff" stroke-width="6" stroke-linecap="round" fill="none"><path d="M50 8V92M14 29L86 71M14 71L86 29"/><path d="M40 16L50 26L60 16M40 84L50 74L60 84M16 42L28 40L24 28M84 58L72 60L76 72M16 58L28 60L24 72M84 42L72 40L76 28"/></g></symbol>
<symbol id="bh-drop" viewBox="0 0 100 100"><path d="M50 6 C66 34 82 50 82 68 A32 32 0 0 1 18 68 C18 50 34 34 50 6Z" fill="url(#bh-g-drop)"/><ellipse cx="38" cy="62" rx="7" ry="12" fill="#fff" opacity=".85"/></symbol>
<symbol id="bh-bubble" viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="url(#bh-g-bub)" stroke="#fff" stroke-opacity=".7" stroke-width="2"/><path d="M28 36 A26 26 0 0 1 46 22" stroke="#fff" stroke-width="6" stroke-linecap="round" fill="none"/></symbol>
<symbol id="bh-swirl" viewBox="0 0 100 100"><g fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"><path d="M8 40 H62 A14 14 0 1 0 48 26"/><path d="M8 60 H74 A14 14 0 1 1 60 74"/><path d="M18 50 H44"/></g></symbol>
</defs></svg>'''

ASM_V = 3
A2_STAGES = [
    ('sys', 'a2.t1', 'a2.h3.sys', 'a2.i.sys', [('sys%d' % i, 'sys%d' % i) for i in range(1, 6)]),
    ('in', 'a2.t2', 'a2.h3.in', 'a2.i.in', [('asm.in12', 'front'), ('asm.in5', 'filter'), ('asm.in2', 'coil'), ('asm.in3', 'blower'), ('asm.in4', 'motor'), ('asm.in6', 'pan'),
                                            ('asm.in7', 'hose'), ('asm.in8', 'sensor'), ('asm.in9', 'pcb'), ('asm.in10', 'display'), ('asm.in11', 'louver'), ('asm.in1', 'casing')]),
    ('out', 'a2.t3', 'a2.h3.out', 'a2.i.out', [('asm.out%d' % i, p) for i, p in enumerate(['cabinet', 'compressor', 'condenser', 'fan', 'fmotor', 'mpcb', 'capacitor', 'valves', 'terminal', 'grille'], 1)]),
    ('ins', 'a2.t4', 'a2.h3.ins', 'a2.i.ins', [('asm.ins%d' % i, 'ins%d' % i) for i in range(1, 8)]),
    ('cool', 'a2.t5', 'a2.h3.cool', 'a2.i.cool', [('cool%d' % i, 'cool%d' % i) for i in range(1, 7)]),
]
def asm_section(ticker=''):
    """Home: interactive split-AC explorer (5 stages, component list, 3D viewer with hotspots)."""
    chev = '<svg class="chev" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    svg = lambda d: f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    tabs, panels = '', ''
    for si, (sid, tk, hk, ik, items) in enumerate(A2_STAGES, 1):
        on = si == 1
        tabs += (f'<button type="button" role="tab" id="a2-tab-{si}" aria-controls="a2-p-{si}" aria-selected="{"true" if on else "false"}"'
                 f'{"" if on else " tabindex=\"-1\""} data-stage="{si - 1}"><small>0{si}</small>{tx(tk)}</button>')
        lis = ''
        for n, (k, part) in enumerate(items, 1):
            did = f'a2-d-{sid}-{n}'
            lis += (f'<li class="a2-item" data-part="{part}"><button type="button" class="a2-pick" aria-expanded="false" aria-controls="{did}">'
                    f'<span class="n">{n:02d}</span><span class="nm">{tx(k)}</span>{chev}</button>'
                    f'<div class="a2-dsc" id="{did}" hidden><p>{tx(k + ".d")}</p>' +
                    (f'<p class="why"><b>{tx("a2.why")}</b> {tx(k + ".u")}</p>' if (k + '.u') in S else '') + '</div></li>')
        panels += (f'<div class="a2-panel" role="tabpanel" id="a2-p-{si}" aria-labelledby="a2-tab-{si}" data-stage="{si - 1}" data-sid="{sid}"{"" if on else " hidden"}>'
                   f'<h3>{tx(hk)}</h3><p class="a2-intro">{tx(ik)}</p><ol class="a2-list">{lis}</ol>' +
                   (f'<p class="a2-note">{tx("asm.out.note")}</p>' if sid == 'out' else '') + '</div>')
    tools = (f'<button type="button" class="a2-tool" data-act="rotate" aria-pressed="false" aria-label="{esc(plain("a2.rotate"))}" data-i18n-aria="a2.rotate">{svg("M20 12a8 8 0 1 1-2.3-5.6M20 4v5h-5")}</button>'
             f'<button type="button" class="a2-tool" data-act="zin" aria-label="{esc(plain("a2.zin"))}" data-i18n-aria="a2.zin">{svg("M12 5v14M5 12h14")}</button>'
             f'<button type="button" class="a2-tool" data-act="zout" aria-label="{esc(plain("a2.zout"))}" data-i18n-aria="a2.zout">{svg("M5 12h14")}</button>'
             f'<button type="button" class="a2-tool" data-act="reset" aria-label="{esc(plain("a2.reset"))}" data-i18n-aria="a2.reset">{svg("M3 12a9 9 0 1 0 3-6.7M3 4v5h5")}</button>')
    return f'''<section id="ac-assembly" class="a2" aria-labelledby="a2-h">
<div class="wrap">
<div class="a2-head"><h2 id="a2-h"><span class="a2-eb">{tx("a2.eb")}</span><span class="a2-hh">{tx("a2.h")}</span></h2>
<p class="a2-lead">{tx("a2.p")}</p><p class="a2-hint">{svg("M9 11V6a3 3 0 0 1 6 0v5M5 13l7 7 7-7")}{tx("a2.hint")}</p></div>
<div class="a2-tabs" role="tablist" aria-label="{esc(plain("a2.eb"))}">{tabs}</div>
<div class="a2-grid">
<div class="a2-view">
<img class="a2-poster" src="/assets/img/ac-assembly-poster.webp?v={ASM_V}" width="1508" height="1268" loading="lazy" decoding="async" alt="{esc(plain("a2.poster"))}" data-i18n-alt="a2.poster">
<div class="a2-canvas"></div><div class="a2-hot" aria-hidden="true"></div>
<div class="a2-tools" hidden>{tools}</div>
<p class="a2-drag" hidden>{tx("a2.drag")}</p>
</div>
<div class="a2-side">{panels}
<div class="a2-nav"><button type="button" class="a2-prev" aria-label="{esc(plain("a2.prev"))}" data-i18n-aria="a2.prev">{svg("M15 18l-6-6 6-6")}<span>{tx("a2.prev")}</span></button>
<div class="a2-prog"><span class="a2-count">01 / 05</span><div class="a2-bar" aria-hidden="true"><i></i></div></div>
<button type="button" class="a2-next" aria-label="{esc(plain("a2.next"))}" data-i18n-aria="a2.next"><span>{tx("a2.next")}</span>{svg("M9 18l6-6-6-6")}</button></div>
</div>
</div>
</div>
<div id="asm-end">{ticker}</div>
<script>(function(){{var s=document.getElementById('ac-assembly'),ok=false;try{{var c=document.createElement('canvas');ok=!!(window.WebGLRenderingContext&&(c.getContext('webgl2')||c.getContext('webgl')));}}catch(e){{}}
if(!ok){{s.classList.add('a2-static');return;}}
var go=function(){{var j=document.createElement('script');j.src='/assets/js/ac-assembly.js?v={ASM_V}';j.async=true;j.onerror=function(){{s.classList.add('a2-static');}};document.body.appendChild(j);}};
if('IntersectionObserver'in window){{var io=new IntersectionObserver(function(e){{if(e[0].isIntersecting){{io.disconnect();go();}}}},{{rootMargin:'120% 0px'}});io.observe(s);}}else go();}})();</script>
<script src="/assets/js/a2-ui.js?v={ASM_V}" defer></script>
</section>'''


def trust_strip():
    """Moving trust ticker (moved from the hero to just above the footer)."""
    mq = ''.join(f'{tx("bh2.mq.%d" % n)}<i aria-hidden="true">✦</i>' for n in range(1, 9))
    return (f'<section class="trust-strip" aria-label="{esc(plain("duo.trust"))}"><div class="bobby-hero-marquee">'
            f'<div class="bobby-hero-mq-track"><span class="bh2-mq">{mq}</span><span class="bh2-mq" aria-hidden="true">{mq}</span></div></div></section>')

def home_slider():
    slides, caps, tabs = '', '', ''
    for i, (k, word, bg, bg2, fl) in enumerate(H2_SLIDES):
        act = ' is-active' if i == 0 else ''
        flo = ''.join(f'<span class="bobby-hero-fl{" is-front" if bl else ""}" style="--x:{x}%;--y:{y}%;--sz:{sz}px;--dp:{d};--bl:{bl}px;--fi:{j}"><svg viewBox="0 0 100 100"><use href="#bh-{t}"/></svg></span>'
                      for j, (t, (x, y, sz, d, bl)) in enumerate(zip(fl, H2_FL)))
        letters = ''.join(f'<span style="--li:{j}">{c}</span>' for j, c in enumerate(word))
        svg = H2_SVG[k].replace('class="bh2-svg"', f'class="bh2-svg bh2-svg-{k}"')
        slides += (f'<div class="bobby-hero-slide bobby-hero-slide-{k}{act}" data-bg="{bg}" data-bg2="{bg2}" aria-hidden="{"false" if i == 0 else "true"}">'
                   f'<div class="bobby-hero-word" aria-hidden="true">{letters}</div><div class="bobby-hero-floats">{flo}</div>'
                   f'<div class="bobby-hero-product"><div class="bobby-hero-bob"><div class="bh2-tilt">{svg}{H2_EXTRA[k]}</div></div><span class="bobby-hero-pshadow"></span></div></div>')
        caps += f'<div class="bobby-hero-cap{act}"><p class="bobby-hero-cap-n">0{i + 1} — {tx("bh2.tab." + k)}</p>{tx("bh2.%s.t" % k, "h3")}{tx("bh2.%s.d" % k, "p")}</div>'
        tabs += f'<button type="button" role="tab" class="bobby-hero-tab{act}" aria-selected="{"true" if i == 0 else "false"}" data-go="{i}">{tx("bh2.tab." + k)}</button>'
    mq = ''.join(f'{tx("bh2.mq.%d" % n)}<i aria-hidden="true">✦</i>' for n in range(1, 9))
    return f'''<section class="bh2s bobby-hero" id="services-showcase" aria-roledescription="carousel" aria-labelledby="bh2-h2">{H2_SYMBOLS}
<div class="bobby-hero-bg" aria-hidden="true"><span class="bobby-hero-grid"></span><span class="bobby-hero-beam"></span><span class="bobby-hero-glow"></span><span class="bh2-spot"></span><span class="bh2-frost"></span></div>
<div class="bobby-hero-stage">{slides}</div>
<div class="bobby-hero-bottom">
<div class="bobby-hero-copy"><p class="bobby-hero-trust">{ic('shield')}{tx('bh2.trust')}</p><h2 id="bh2-h2" class="bobby-hero-h1" data-i18n="bh2.h2">{en('bh2.h2')}</h2><div class="bobby-hero-caps" aria-live="polite">{caps}</div></div>
<div class="bobby-hero-mid"><div class="bobby-hero-tabs" role="tablist">{tabs}</div>
<div class="bobby-hero-ctas"><a class="bobby-hero-btn bobby-hero-btn-orange bh2-magnet" href="/contact/#book" data-book="">{tx('btn.bookservice')}{ic('arrow')}</a><a class="bobby-hero-btn bobby-hero-btn-glass bh2-magnet" href="tel:{PHONE_TEL}">{ic('phone')}<span class="bh2-call-lg">{PHONE_TXT}</span><span class="bh2-call-sm" aria-hidden="true" data-i18n="btn.call">{en('btn.call')}</span></a><a class="bobby-hero-btn bobby-hero-btn-wa bh2-magnet" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{wa_ic()}{tx('btn.wa')}</a></div></div>
<div class="bobby-hero-ctrl"><p class="bobby-hero-count"><b class="bobby-hero-cur">01</b> / 0{len(H2_SLIDES)}</p><div class="bobby-hero-progress"><span></span></div>
<div class="bobby-hero-arrows"><button type="button" class="bobby-hero-arrow bobby-hero-prev" aria-label="{esc(plain('bh2.prev'))}" data-i18n-aria="bh2.prev">{ic('arrow')}</button><button type="button" class="bobby-hero-arrow bobby-hero-next" aria-label="{esc(plain('bh2.next'))}" data-i18n-aria="bh2.next">{ic('arrow')}</button></div></div>
</div>

</section>'''

# ---------------- pages ----------------
PAGES = {}
_LM_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'lastmod.json')
try: _LM = json.load(open(_LM_FILE))
except Exception: _LM = {}
_LM_SEEN = {}
def _lm_record(path, html_):
    import hashlib, datetime, re as _re
    body = _re.sub(r'\?v=[0-9a-f]+|data-iv="[^"]*"', '', html_)       # ignore asset version bumps
    h = hashlib.md5(body.encode('utf-8')).hexdigest()
    old = _LM.get(path)
    _LM_SEEN[path] = old if (old and old['h'] == h) else {'h': h, 'd': datetime.date.today().isoformat()}
def lastmod(u):
    return (_LM_SEEN.get(u) or _LM_SEEN.get(u + 'index.html') or {'d': UPDATED})['d']
def save_lastmod():
    json.dump(_LM_SEEN, open(_LM_FILE, 'w'), indent=0, sort_keys=True)

def page(path, html_):
    _lm_record(path, html_)
    PAGES[path] = html_

def build_home():
    ld = [business_ld(),
          {'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'BOBBY AC Services', 'alternateName': ['BOBBY AC Repair & Home Appliance Services', 'bobbyacservices.com', 'BOBBY AC Narasaraopet'], 'inLanguage': ['en', 'te', 'hi'], 'publisher': {'@id': SITE + '/#business'}},
          {'@context': 'https://schema.org', '@type': 'Organization', '@id': SITE + '/#org', 'name': BRAND, 'url': SITE + '/', 'logo': SITE + '/assets/img/bobby-logo-640.webp', 'telephone': PHONE_TEL}]
    chips = [('c1', 'install', 'svc.ac_install.name'), ('c2', 'wrench', 'svc.ac_repair.name'), ('c3', 'ac', 'svc.ac_servicing.name'), ('c4', 'gauge', 'chip.gas')]
    S['chip.gas'] = ("Gas Filling", "గ్యాస్ ఫిల్లింగ్", "गैस फिलिंग")
    chips_html = ''.join(f'<span class="chip-float {c}"><i>{ic(icn)}</i>{tx(k)}</span>' for c, icn, k in chips)
    hero = f'''<section class="hero" aria-labelledby="h1"><span class="blob b1"></span><span class="blob b2"></span>
<div class="wrap">
<div>
<p class="eyebrow anim">{tx('hero.eyebrow')}</p>
<h1 id="h1" class="anim d1" data-i18n="hero.h1">{en('hero.h1')}</h1>
<p class="sub anim d2">{tx('hero.sub')}</p>
<div class="ctas anim d3">
{book_a('ac_servicing', 'btn-orange', 'btn.bookac', 'snow')}
<a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}<span class="cta-short" data-i18n="btn.call">{en('btn.call')}</span></a>
<a class="btn btn-wa" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{wa_ic()}<span class="cta-long">{tx('btn.wachat')}</span><span class="cta-short" data-i18n="btn.wa">{en('btn.wa')}</span></a>
</div>
<p class="trust anim d4">{ic('check')}{tx('hero.trust')}</p>
</div>
<div class="hero-visual anim d2">
<svg class="airflow" viewBox="0 0 300 200" fill="none" stroke="#9FE6FF" stroke-width="5" stroke-linecap="round" aria-hidden="true"><path d="M10 40 C80 10 140 70 220 40 S290 20 300 30"/><path d="M0 80 C70 50 150 110 230 80 S290 60 300 70"/><path d="M20 120 C90 90 160 150 240 120"/><path d="M10 160 C80 130 140 190 220 160"/></svg>
<div class="hero-photo hero-photo-real">{img('about-photo', 640, 690, 'about.photo.alt', eager=True)}</div>
{chips_html}
<div class="hero-card"><span class="temp">24°C</span><span><b data-i18n="hero.card.title">{en('hero.card.title')}</b><small data-i18n="hero.card.sub">{en('hero.card.sub')}</small></span></div>
</div></div></section>'''
    duo = ('<div class="hero-duo" id="hero-duo" aria-roledescription="carousel" aria-label="Featured">'
           + hero.replace('<section class="hero"', '<section class="hero hero-duo-panel is-on"', 1)
           + home_slider().replace('<section class="bh2s bobby-hero"', '<section class="bh2s bobby-hero hero-duo-panel" aria-hidden="true" inert', 1)
           + '<div class="hero-duo-pager" role="tablist" aria-label="Choose hero">'
           + '<button type="button" role="tab" class="is-on" aria-selected="true" data-duo="0" aria-label="AC repair at your doorstep"></button>'
           + '<button type="button" role="tab" aria-selected="false" data-duo="1" aria-label="Services showcase"></button></div></div>'
           + '<script>(function(){var d=document.getElementById("hero-duo"),r=document.documentElement;'
           + 'function s(k,v){var c=parseFloat(getComputedStyle(r).getPropertyValue(k));if(isNaN(c)||Math.abs(c-v)>1)r.style.setProperty(k,v+"px")}'
           + 'function f(){var m=document.querySelector(".mbar");s("--hero-top",Math.round(d.getBoundingClientRect().top+scrollY));'
           + 'if(m)s("--hero-bar",getComputedStyle(m).display!=="none"?m.offsetHeight:0)}'
           + 'f();addEventListener("DOMContentLoaded",f);addEventListener("load",f);addEventListener("resize",f);'
           + 'if(document.fonts)document.fonts.ready.then(f)})();</script>')
    body = (duo + stats_block() + reviews_block() +
        f'<section class="sec sec-alt" id="ac-services"><div class="wrap">{sec_head("acsec.eyebrow", "acsec.h2", "acsec.sub")}{ac_cards()}<p class="center reveal" style="text-align:center;margin-top:28px"><a class="btn btn-line" href="/ac-services/">{tx("btn.allac")}{ic("arrow")}</a></p></div></section>' +
        f'<section class="sec app-sec" id="appliances"><div class="wrap">{sec_head("appsec.eyebrow", "appsec.h2", "appsec.sub")}{app_cards()}</div></section>' +
        f'<section class="sec sec-alt" id="brands"><div class="wrap">{sec_head("brands.eyebrow", "brands.h2", "brands.sub")}{brands_block()}</div></section>' +
        f'''<section class="sec" id="why"><div class="wrap why-split"><div class="why-photo reveal">{img('why', 1200, 1440, 'why.h2')}</div>
<div>{sec_head("why.eyebrow", "why.h2", None, center=False)}{why_cards()}</div></div></section>''' +
        steps_block() +
        f'<section class="sec sec-alt" id="blog"><div class="wrap">{sec_head("blogh.eyebrow", "blogh.h2", "blogh.sub")}{blog_cards(POSTS[:3])}<p style="text-align:center;margin-top:28px" class="reveal"><a class="btn btn-line" href="/blog/">{tx("btn.allblog")}{ic("arrow")}</a></p></div></section>' +
        asm_section(trust_strip()))
    page('/', head('BOBBY AC, Washing Machine Repair & Home Appliance Services - Narasaraopet',
                 'Doorstep AC repair, AC servicing & installation, washing machine, refrigerator, air cooler and fan repair in Narasaraopet + 20 km. Call or WhatsApp +91 83748 89163.',
                   '/', None, ld).replace('</head>', '<link rel="stylesheet" href="/assets/css/hero2.css?v=19">\n<link rel="stylesheet" href="/assets/css/asm.css?v=%d">\n</head>' % ASM_V) + header('home') + body + footer().replace('</body>', '<script src="/assets/js/hero2.js?v=7" defer></script>\n</body>'))

def service_ld(name, desc, path):
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'description': desc, 'serviceType': name,
            'provider': {'@id': SITE + '/#business'}, 'areaServed': {'@type': 'City', 'name': CITY}, 'url': SITE + path}

def about_body():
    tags = ''.join(f'<li>{ic(i)}{tx(k)}</li>' for i, k in (('home', 'ab.tag1'), ('layers', 'ab.tag2'), ('heart', 'ab.tag3')))
    who = f"""<section class="sec ab-who"><div class="wrap about-grid"><div class="reveal">
<p class="eyebrow">{tx('ab.who.eb', 'span')}</p><h2>{tx('ab.who.h')}</h2>
<p class="lead ab-lead">{tx('ab.who.p1')}</p>
<ul class="ab-bul">{''.join(f'<li>{ic("check")}{tx(k)}</li>' for k in ('ab.who.p2', 'ab.who.p3'))}</ul>
<p class="ab-p">{tx('ab.who.p4')}</p>
<ul class="ab-tags">{tags}</ul></div>
<div class="ph-frame reveal d2"><div class="ph ph-full">{img('about-photo', 1536, 1024, 'about.photo.alt')}</div></div></div></section>"""
    phil = f"""<section class="sec ab-phil"><div class="wrap"><div class="ab-phil-card reveal">
<span class="ab-q" aria-hidden="true">“</span>
<p class="eyebrow">{tx('ab.phil.eb', 'span')}</p><h2>{tx('ab.phil.h')}</h2>
<div class="ab-phil-steps">{''.join(f'<span>{ic(i)}{tx(k)}</span>' for i, k in (('search', 'ab.phil.s1'), ('wrench', 'ab.phil.s2'), ('shield', 'ab.phil.s3')))}</div>
<p>{tx('ab.phil.p')}</p></div></div></section>"""
    svc_ic = ['ac', 'fridge', 'washer', 'cooler', 'fan', 'bolt']
    svc = f"""<section class="sec sec-alt"><div class="wrap">{sec_head('ab.svc.eb', 'ab.svc.h')}<div class="ab-svc">""" + ''.join(
        f'<article class="ab-svc-c reveal d{i % 3}"><span class="ab-ic">{ic(svc_ic[i])}</span><div><h3>{tx("ab.svc.%d.t" % (i + 1))}</h3><p>{tx("ab.svc.%d.d" % (i + 1))}</p></div></article>'
        for i in range(6)) + '</div></div></section>'
    tp_ic = ['search', 'talk', 'rupee', 'target', 'wrench', 'gauge', 'home']
    tp = f"""<section class="sec"><div class="wrap">{sec_head('ab.tp.eb', 'ab.tp.h')}<ol class="ab-tp">""" + ''.join(
        f'<li class="reveal d{i % 4}"><span class="ab-n">{i + 1:02d}</span><span class="ab-tp-ic">{ic(tp_ic[i])}</span><h3>{tx("ab.tp.%d.t" % (i + 1))}</h3><p>{tx("ab.tp.%d.d" % (i + 1))}</p></li>'
        for i in range(7)) + '</ol></div></section>'
    why = f"""<section class="sec sec-alt"><div class="wrap ab-why"><div class="reveal">{sec_head('ab.why.eb', 'ab.why.h', center=False)}</div>
<ul class="ab-checks reveal d1">{''.join(f'<li>{ic("check")}{tx("ab.why.%d" % i)}</li>' for i in range(1, 8))}</ul></div></section>"""
    return who + phil + svc + tp + why

def build_inner():
    # about
    p = '/about/'
    page(p, head('About Us | BOBBY AC & Home Appliance Services Narasaraopet',
                 'Learn about BOBBY AC Repair & Home Appliance Services in Narasaraopet: our services, inspection-first process and doorstep service coverage.', p, 'nav.about',
                 [business_ld(), crumbs_ld([('Home', '/'), ('About Us', p)])]) + header('about') +
         phero('p.about.h1', 'p.about.sub', [('crumb.home', '/'), ('nav.about', p)]) +
         about_body() +
         '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band('about') + footer())

    # AC services
    p = '/ac-services/'
    sl = [service_ld(plain('ac.%s.t' % L), plain('ac.%s.d' % L), p + '#' + a) for L, a, *_ in AC_BLOCKS]
    page(p, head('AC Services - Repair, Servicing & Installation | BOBBY Narasaraopet',
                 'Book AC repair, installation, uninstallation, servicing and gas filling checks in Narasaraopet. Split and window AC service. Call BOBBY today.',
                 p, 'nav.ac', [business_ld(), crumbs_ld([('Home', '/'), ('AC Services', p)])] + sl) + header('ac') +
         phero('p.ac.h1', 'p.ac.sub', [('crumb.home', '/'), ('nav.ac', p)]) + quick_answer('ac') +
         f'''<section class="sec"><div class="wrap">{sec_head("acsec.eyebrow", "acsec.h2", "acsec.sub")}{ac_cards(eager_first=True)}</div></section>
<section class="sec sec-alt"><div class="wrap loc-grid"><div class="reveal"><h2>{tx('ac.types.h')}</h2><p class="lead" style="margin-top:12px">{tx('ac.types.p')}</p><p class="note" style="margin-top:18px">{ic('info')}{tx('ac.E.note')}</p></div>
<div class="reveal d2">{faq_list([2, 4, 5, 6], first_open=False)}</div></div></section>''' +
         steps_block() + '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band('ac') + footer())

    # Appliance
    p = '/appliance-services/'
    sl = [service_ld(plain('ap.%s.t' % k), plain('svc.%s.desc' % k), p + '#' + a) for k, a in AP_BLOCKS]
    page(p, head('Washing Machine & Refrigerator Repair | BOBBY Narasaraopet',
                 'Need refrigerator, washing machine, air cooler or ceiling fan repair in Narasaraopet? Contact BOBBY for doorstep appliance service.',
                 p, 'nav.appliance', [business_ld(), crumbs_ld([('Home', '/'), ('Appliance Services', p)])] + sl) + header('app') +
         phero('p.app.h1', 'p.app.sub', [('crumb.home', '/'), ('nav.appliance', p)]) + quick_answer('ap') +
         f'''<section class="sec app-sec"><div class="wrap">{sec_head("appsec.eyebrow", "appsec.h2", "appsec.sub")}{app_cards(eager_first=True)}</div></section>
<section class="sec sec-alt"><div class="wrap">{sec_head("faqh.eyebrow", "faqh.h2")}{faq_list([7, 8, 9, 13])}</div></section>''' +
         '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band('app') + footer())

    # Brands
    p = '/brands/'
    page(p, head('Brands We Service - LG, Samsung, Daikin, Voltas | BOBBY Narasaraopet',
                 'BOBBY provides independent multi-brand AC and appliance repair for LG, Daikin, Samsung, Voltas, Blue Star, Panasonic and other brands.',
                 p, 'nav.brands', [business_ld(), crumbs_ld([('Home', '/'), ('Brands We Service', p)])]) + header('brands') +
         phero('p.brands.h1', 'p.brands.sub', [('crumb.home', '/'), ('nav.brands', p)]) +
         f'''<section class="sec"><div class="wrap">{sec_head("brands.eyebrow", "brands.h2", "brands.sub")}{brands_block(True)}</div></section>
<section class="sec sec-alt"><div class="wrap">{faq_list([10], hq='h2')}</div></section>''' +
         '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band('brands') + footer())

    # FAQs (FAQPage schema: every Q&A here is visible on this page)
    p = '/faqs/'
    fld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': plain('faq.%d.q' % n), 'acceptedAnswer': {'@type': 'Answer', 'text': plain('faq.%d.a' % n)}} for n in range(1, FAQ_N + 1)]}
    page(p, head('FAQs - AC & Appliance Repair Questions | BOBBY Narasaraopet',
                 'Answers about AC repair, servicing, installation, gas filling, spare parts, appliance repairs and service areas in Narasaraopet, plus an AC electricity cost calculator.',
                 p, 'nav.faqs', [business_ld(), crumbs_ld([('Home', '/'), ('FAQs', p)]), fld]) + header('faqs') +
         phero('p.faqs.h1', 'p.faqs.sub', [('crumb.home', '/'), ('nav.faqs', p)]) +
         f'<section class="sec"><div class="wrap">{faq_list(range(1, FAQ_N + 1), hq='h2')}</div></section>' + acc_widget() + cta_band('faqs') + footer())

    # Contact
    p = '/contact/'
    form = booking_form('c', inline=True)
    arrow = ic('arrow')
    quick = f'''<div class="ct-quick">
<a class="ctq ctq-call reveal" href="tel:{PHONE_TEL}"><span class="ctq-ic">{ic('phone')}</span><span class="ctq-tx"><small>{tx('c.call.h')}</small><b>{PHONE_TXT}</b><em>{tx('c.quick.call.p')}</em></span><span class="ctq-go">{arrow}</span></a>
<a class="ctq ctq-wa reveal d1" href="#book" data-goto-form><span class="ctq-ic">{wa_ic()}</span><span class="ctq-tx"><small>{tx('c.wa.h')}</small><b>{PHONE_TXT}</b><em>{tx('c.quick.wa.p')}</em></span><span class="ctq-go">{arrow}</span></a>
<a class="ctq ctq-dir reveal d2" href="{GMAPS_URL}" target="_blank" rel="noopener"><span class="ctq-ic">{ic('pin')}</span><span class="ctq-tx"><small>{tx('c.loc.h')}</small><b>{tx('c.quick.dir.h')}</b><em>{tx('c.quick.dir.p')}</em></span><span class="ctq-go">{arrow}</span></a>
</div>'''
    steps = ''.join(f'<li><span class="n">{i}</span><span>{tx("c.how.%d" % i)}</span></li>' for i in (1, 2, 3))
    chips = ''.join(f'<li>{ic("check")}{tx(k)}</li>' for k in ('tr.3.t', 'tr.4.t', 'tr.1.t'))
    cards = f'''<aside class="ct-side">
<div class="ct-card ct-info reveal"><h2 class="ct-h">{tx('c.info.h')}</h2>
<ul class="ct-list"><li><span class="ct-li-ic">{ic('pin')}</span><a href="{GMAPS_URL}" target="_blank" rel="noopener">{tx('addr.full')}</a></li>
<li><span class="ct-li-ic">{ic('star')}</span><span><small>{tx('c.hours.h')}</small><b>{tx('hours.open')}</b></span></li>
<li><span class="ct-li-ic">{ic('radius')}</span><span><small>{tx('c.area.h')}</small><b>{tx('c.area.v')}</b></span></li></ul>
<div class="map ct-map"><iframe title="{esc(plain('loc.map'))}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe></div></div>
<div class="ct-card ct-how reveal d1"><h2 class="ct-h">{tx('c.how.h')}</h2><ol class="ct-steps">{steps}</ol><ul class="ct-chips">{chips}</ul></div>
</aside>'''
    page(p, head('Contact & Book Service | BOBBY AC Services Narasaraopet',
                 'Contact BOBBY in Narasaraopet for AC repair and home appliance service. Call, WhatsApp or request a technician visit using our booking form.',
                 p, 'nav.contact', [business_ld(), crumbs_ld([('Home', '/'), ('Contact Us', p)])]) + header('contact') +
         phero('p.contact.h1', 'p.contact.sub', [('crumb.home', '/'), ('nav.contact', p)]) +
         f'<section class="sec ct-sec"><div class="wrap">{quick}<div class="ct-grid">{form}{cards}</div></div></section>' + footer())

    # Blog index + posts
    p = '/blog/'
    page(p, head('Blog - AC & Appliance Care Tips | BOBBY Narasaraopet',
                 'AC repair and servicing guides from BOBBY, Narasaraopet: AC not cooling, electricity saving, best AC brands, gas filling, water leakage and more.',
                 p, 'nav.blog', [business_ld(), crumbs_ld([('Home', '/'), ('Blog', p)])]) + header('blog') +
         phero('p.blog.h1', 'p.blog.sub', [('crumb.home', '/'), ('nav.blog', p)]) +
         f'<section class="sec"><div class="wrap">{blog_cards(POSTS, hq='h2', eager_first=True)}</div></section>' + cta_band('blog') + footer())
    for post in POSTS:
        s = post['slug']; pp = '/blog/%s/' % s
        title_en = plain('post.%s.title' % s)
        art = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': title_en, 'description': plain('post.%s.excerpt' % s),
               'datePublished': post['date'], 'dateModified': post.get('updated', post['date']), 'inLanguage': 'en', 'mainEntityOfPage': SITE + pp,
               'image': SITE + art_url(post['img']), 'author': {'@id': SITE + '/#business'}, 'publisher': {'@id': SITE + '/#business'}}
        others = [x for x in POSTS if x['slug'] != s][:3]
        lds = [business_ld(), crumbs_ld([('Home', '/'), ('Blog', '/blog/'), (title_en, pp)]), art]
        if post.get('faq'):
            lds.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
                {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in post['faq']]})
        page(pp, head(post.get('seo', title_en + ' | BOBBY'), post.get('desc', plain('post.%s.excerpt' % s)), pp, 'post.%s.title' % s,
                      lds,
                      og_img=SITE + art_url(post['img'])) + header('blog') +
             f'''<section class="phero"><div class="wrap"><nav class="crumbs anim" aria-label="Breadcrumb"><ol><li><a href="/">{tx('crumb.home')}</a></li><li><a href="/blog/">{tx('nav.blog')}</a></li><li aria-current="page">{tx('post.%s.title' % s)}</li></ol></nav>
<h1 class="anim d1">{tx('post.%s.title' % s)}</h1><p class="anim d2">{tx('post.%s.excerpt' % s)}</p>
<p class="post-meta anim d2"><span>{tx('blog.by')} <b>{esc(BRAND)}</b></span><span>{tx('blog.pub')} <time datetime="{post['date']}">{fmt_date(post['date'])}</time></span><span>{tx('blog.upd')} <time datetime="{post.get('updated', post['date'])}">{fmt_date(post.get('updated', post['date']))}</time></span></p></div></section>
<section class="sec"><article class="wrap article"><div class="cover-img reveal">{img(post['img'], 1200, 600, 'post.%s.title' % s, eager=True)}</div>
{post_body(post)}
<p class="disc">{tx('blog.disclaimer')}</p>
<div class="cta-box reveal"><div><h3>{tx('blog.related')}</h3><p>{tx('blog.relatedp')}</p></div><div class="btn-row">{book_a(post['svc'], 'btn-orange btn-sm')}<a class="btn btn-ghost btn-sm" href="{post['link']}">{tx('blog.viewsvc')}</a></div></div>
</article></section>
<section class="sec sec-alt"><div class="wrap"><div class="sec-head reveal"><h2>{tx('blog.more')}</h2></div>{blog_cards(others)}</div></section>''' + footer())

    # legal + sitemap + 404
    for path, hk, bk, ttl, act in [('/privacy-policy/', 'p.privacy.h1', 'priv.body', 'Privacy Policy', 'privacy'), ('/terms/', 'p.terms.h1', 'terms.body', 'Terms & Conditions', 'terms')]:
        page(path, head(ttl + ' | BOBBY AC Repair', ttl + ' for the BOBBY AC Repair & Home Appliance Services website, Narasaraopet.', path, hk,
                        [crumbs_ld([('Home', '/'), (ttl, path)])]) + header(act) +
             phero(hk, None, [('crumb.home', '/'), (hk, path)]) +
             f'<section class="sec"><div class="wrap legal prose" data-i18n="{bk}">{en(bk)}</div><p class="wrap legal disc">Last updated: {UPDATED}</p></section>' + footer())
    groups = [('nav.home', [('/', 'nav.home'), ('/about/', 'nav.about'), ('/contact/', 'nav.contact'), ('/faqs/', 'nav.faqs')]),
              ('nav.ac', [('/ac-services/', 'nav.ac')] + [('/ac-services/#' + a, 'ac.%s.t' % L) for L, a, *_ in AC_BLOCKS]),
              ('nav.appliance', [('/appliance-services/', 'nav.appliance')] + [('/appliance-services/#' + a, 'ap.%s.t' % k) for k, a in AP_BLOCKS] + [('/brands/', 'nav.brands')]),
              ('nav.blog', [('/blog/', 'nav.blog')] + [('/blog/%s/' % x['slug'], 'post.%s.title' % x['slug']) for x in POSTS]),
              ('ft.privacy', [('/privacy-policy/', 'ft.privacy'), ('/terms/', 'ft.terms')])]
    sm = ''.join(f'<div><h2>{tx(g)}</h2><ul>' + ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' for u, k in items) + '</ul></div>' for g, items in groups)
    page('/sitemap/', head('Sitemap | BOBBY AC Repair', 'All pages on the BOBBY AC Repair & Home Appliance Services website.', '/sitemap/', 'p.sitemap.h1',
                           [crumbs_ld([('Home', '/'), ('Sitemap', '/sitemap/')])]) + header('sitemap') +
         phero('p.sitemap.h1', None, [('crumb.home', '/'), ('p.sitemap.h1', '/sitemap/')]) +
         f'<section class="sec"><div class="wrap smap">{sm}</div></section>' + footer())
    page('/404.html', head('Page not found | BOBBY AC Repair', 'Page not found.', '/404.html', 'p.404.h1').replace('index, follow', 'noindex').replace('<link rel="canonical" href="%s/404.html">\n' % SITE, '') + header('') +
         f'''<section class="phero" style="text-align:center"><div class="wrap"><h1>{tx('p.404.h1')}</h1><p style="margin:0 auto 24px">{tx('p.404.sub')}</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-orange" href="/">{tx('btn.home')}</a><a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}</a></div></div></section>
<section class="sec"><div class="wrap">{quick_cards()}</div></section>''' + footer())

    sp_page.build(sys.modules[__name__])

# ---------------- write ----------------
def fingerprint(out):
    """Give every /assets/... reference a ?v=<content hash>, so browsers always get the newest file
    (no manual version bumps) while assets can be cached for a year."""
    import hashlib, re
    def h(fp): return hashlib.md5(open(fp, 'rb').read()).hexdigest()[:8]
    ref = re.compile(r'/assets/([A-Za-z0-9_./-]+\.(?:webp|png|jpg|jpeg|svg|ico|css|js|woff2?))(?:\?v=[A-Za-z0-9.]*)?')
    def rewrite(fp):
        s = open(fp, encoding='utf-8').read()
        def sub(m):
            p = os.path.join(out, 'assets', m.group(1))
            return m.group(0) if not os.path.isfile(p) else '/assets/%s?v=%s' % (m.group(1), h(p))
        n = ref.sub(sub, s)
        if n != s: open(fp, 'w', encoding='utf-8').write(n)
    # images first (css/js point at them), then css/js (html points at them), then pages
    for sub_ in ('assets/css', 'assets/js'):
        for f in os.listdir(os.path.join(out, sub_)):
            if f.endswith(('.css', '.js')) and f != 'ac-assembly.js': rewrite(os.path.join(out, sub_, f))
    for root, _, files in os.walk(out):
        for f in files:
            if f.endswith(('.html', '.xml', '.webmanifest')): rewrite(os.path.join(root, f))

def write_middleware():
    """functions/_middleware.js: apex -> www always; the production pages.dev address -> www only once
    DOMAIN_CONNECTED is True. Branch previews (<branch>.bobbyacservices.pages.dev) are never redirected."""
    js = f"""/**
 * GENERATED by build.py - edit DOMAIN_CONNECTED in build.py, not this file.
 * - bobbyacservices.com (no www)  -> 301 to https://{DOMAIN} (same path)
 * - bobbyacservices.pages.dev     -> 301 to https://{DOMAIN} only when the domain is connected
 * - branch previews (*.bobbyacservices.pages.dev) are left alone.
 */
const CANONICAL_HOST = '{DOMAIN}';
const REDIRECT_PAGES_DEV = {'true' if DOMAIN_CONNECTED else 'false'};

export async function onRequest(context) {{
  const url = new URL(context.request.url);
  const host = url.hostname;
  if (host === 'bobbyacservices.com' || (REDIRECT_PAGES_DEV && host === 'bobbyacservices.pages.dev')) {{
    url.hostname = CANONICAL_HOST;
    url.protocol = 'https:';
    url.port = '';
    return Response.redirect(url.toString(), 301);
  }}
  return context.next();
}}
"""
    open(os.path.join(os.path.dirname(__file__), 'functions', '_middleware.js'), 'w').write(js)


def write():
    out = os.path.join(os.path.dirname(__file__), 'dist')
    if os.path.exists(out): shutil.rmtree(out)
    shutil.copytree(os.path.join(os.path.dirname(__file__), 'static'), out)
    import rcssmin, rjsmin
    for sub, fn in (('assets/css', rcssmin.cssmin), ('assets/js', rjsmin.jsmin)):
        for f in os.listdir(os.path.join(out, sub)):
            fp = os.path.join(out, sub, f)
            if os.path.isfile(fp) and f.endswith(('.css', '.js')) and f != 'ac-assembly.js':  # bundle is pre-minified by esbuild
                src = open(fp, encoding='utf-8').read()
                mini = fn(src)
                assert len(mini) > len(src) * 0.3, fp
                open(fp, 'w', encoding='utf-8').write(mini)
    for path, content in PAGES.items():
        fp = os.path.join(out, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(out, path.strip('/'))
        if path == '/': fp = os.path.join(out, 'index.html')
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, 'w', encoding='utf-8').write(content)
    os.makedirs(os.path.join(out, 'assets/i18n'), exist_ok=True)
    for i, l in enumerate(['en', 'te', 'hi']):
        json.dump({k: v[i] for k, v in S.items()}, open(os.path.join(out, 'assets/i18n/%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    urls = [p for p in PAGES if p.endswith('/')]
    pri = lambda p: '1.0' if p == '/' else ('0.9' if p in ('/ac-services/', '/contact/') else ('0.6' if p.startswith('/blog/') or p in ('/privacy-policy/', '/terms/', '/sitemap/') else '0.8'))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'<url><loc>{SITE}{u}</loc><lastmod>{lastmod(u)}</lastmod><priority>{pri(u)}</priority></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(out, 'sitemap.xml'), 'w').write(sm); save_lastmod()
    llms = f"""# BOBBY AC Repair & Home Appliance Services

> Doorstep AC repair, servicing, installation and home appliance repair in {CITY} (Palnadu district, Andhra Pradesh, India) and nearby areas within about 20 km. Run by Yalamanda Gogasani ("Bobby").

- Phone / WhatsApp: {PHONE_TXT}
- Address: {ADDRESS['street']}, {ADDRESS['locality']}, Andhra Pradesh {ADDRESS['postal']}, India
- Google Maps: https://maps.google.com/?cid=7427535041159212251
- Languages: English, Telugu, Hindi
- Booking: call, WhatsApp, or the booking form at {SITE}/contact/

## Services
- Split AC and window AC repair: not cooling, water leakage, noise, electrical faults, PCB issues
- AC servicing (wet/foam service), installation, uninstallation and relocation
- Refrigerant leak check and gas filling
- Home appliance repair: refrigerators, washing machines, air coolers and ceiling fans
- AC spare parts (genuine or compatible, depending on model and stock)
- The technician inspects first and gives a clear estimate before starting work

## Pages
- [Home]({SITE}/): overview, how a split AC works, booking
- [AC services]({SITE}/ac-services/): AC repair, servicing, installation and gas filling
- [Appliance services]({SITE}/appliance-services/): home appliance repair
- [AC spare parts]({SITE}/ac-spare-parts/): spare parts
- [Brands]({SITE}/brands/): AC and appliance brands serviced
- [FAQs]({SITE}/faqs/): common questions on repair, servicing, area and booking
- [Blog]({SITE}/blog/): AC guides: AC repair in Narasaraopet, AC servicing in Narasaraopet, reducing AC electricity bills, best AC brands in India, top 10 AC brands in India, finding an AC technician, AC not cooling, water leakage, gas filling
- [About]({SITE}/about/): about BOBBY and the service area
- [Contact]({SITE}/contact/): phone, WhatsApp, map and booking form
"""
    open(os.path.join(out, 'llms.txt'), 'w').write(llms)
    open(os.path.join(out, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    open(os.path.join(out, 'site.webmanifest'), 'w').write(json.dumps({'name': BRAND, 'short_name': 'BOBBY AC', 'start_url': '/', 'display': 'standalone',
        'background_color': '#102C50', 'theme_color': '#102C50', 'icons': [{'src': '/assets/img/icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/assets/img/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}))
    fingerprint(out)
    write_middleware()
    open(os.path.join(out, '_headers'), 'w').write('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=(self)\n/assets/img/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/vendor/*\n  Cache-Control: public, max-age=2592000\n/assets/css/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/js/*\n  Cache-Control: public, max-age=31536000, immutable\n/assets/i18n/*\n  Cache-Control: public, max-age=31536000, immutable\n')
    print('Built %d pages -> %s' % (len(PAGES), out))

if __name__ == '__main__':
    build_home(); build_inner(); write()
