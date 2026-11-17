# -*- coding: utf-8 -*-
"""Static site generator for BOBBY AC Repair & Home Appliance Services.
Run:  python3 build.py   ->  writes the finished site into ./dist
Edit business details, prices and photos in the CONFIG block below."""
import json, os, shutil, html
from strings import S, SERVICES, FAQ_N
from blog import POSTS, add_strings

# ======================= CONFIG =======================
SITE      = 'https://www.bobbyacservices.com'      # change here if the domain changes
BRAND     = 'BOBBY AC Repair & Home Appliance Services'
PHONE_TXT = '+91 83748 89163'
PHONE_TEL = '+918374889163'
WA_NUM    = '918374889163'
CITY      = 'Narasaraopet'
REGION    = 'Andhra Pradesh'
UPDATED   = '2026-11-17'
ADDRESS   = {'street': 'Door 11, Employees Colony, Isha Zen Enclave, 28-32/5, Palapadu Road, Arundelpet', 'locality': 'Narasaraopeta', 'postal': '522601'}
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
REVIEWS = []   # genuine reviews only: {'name': 'Customer name', 'area': 'Narasaraopet', 'service': 'AC Repair', 'rating': 5, 'text': 'exact words', 'google': True}

# DEMO data — sample names & text for layout testing ONLY. Rendered only on the noindex /reviews-preview/ page.
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
for p in POSTS:
    for f in ('title', 'excerpt', 'body'):
        S['post.%s.%s' % (p['slug'], f)] = p[f]

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

ART_W = {'hero': 1200, 'about': 1600, 'technician': 1536}
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
 'fan': '<g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v5"/><circle cx="12" cy="10" r="2.2"/><path d="M10 10C6 9 3 10 2 11.5c3 1 6 .5 8 0M14 10c4-1 7 0 8 1.5-3 1-6 .5-8 0M12 12.2c-.5 3.5.5 7 1.8 8.3 1-2.6.4-5.8-.3-8.3"/></g>',
 'home': '<path d="M3 11l9-7 9 7v9a1.5 1.5 0 0 1-1.5 1.5H15v-6H9v6H4.5A1.5 1.5 0 0 1 3 20z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
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
    cls = 'form bookform reveal d2' if inline else 'form bookform'
    hid = ' id="book"' if inline else ''
    return f'''<form class="{cls}"{hid} novalidate data-prefix="{p}">
<h2 id="{p}Title">{tx('f.h')}</h2><p class="fnote">{ic('info')}{tx('f.note')}</p>
<div class="hp" aria-hidden="true"><label>Leave empty<input type="text" name="company" tabindex="-1" autocomplete="off"></label></div>
<div class="frow"><div class="field"><label for="{p}Name">{tx('f.name')} <span class="req">*</span></label><input id="{p}Name" name="name" autocomplete="name" maxlength="60" required placeholder="{esc(plain('f.ph.name'))}" data-i18n-ph="f.ph.name"><p class="emsg"></p></div>
<div class="field"><label for="{p}Phone">{tx('f.phone')} <span class="req">*</span></label><input id="{p}Phone" name="phone" type="tel" inputmode="numeric" autocomplete="tel" maxlength="14" required placeholder="{esc(plain('f.ph.phone'))}" data-i18n-ph="f.ph.phone"><p class="emsg"></p></div></div>
<div class="frow"><div class="field"><label for="{p}Appliance">{tx('f.appliance')} <span class="req">*</span></label><select id="{p}Appliance" name="appliance" required><option value="" data-i18n="f.select">{en('f.select')}</option>{opt('split','f.opt.splitac')}{opt('window','f.opt.windowac')}{opt('fridge','f.opt.fridge')}{opt('washer','f.opt.washer')}{opt('cooler','f.opt.cooler')}{opt('fan','f.opt.fan')}</select><p class="emsg"></p></div>
<div class="field"><label for="{p}Service">{tx('f.service')} <span class="req">*</span></label><select id="{p}Service" name="service" required><option value="" data-i18n="f.select">{en('f.select')}</option>{opt('repair','f.opt.repair')}{opt('service','f.opt.service')}{opt('install','f.opt.install')}{opt('uninstall','f.opt.uninstall')}{opt('gas','f.opt.gas')}{opt('notsure','f.opt.notsure')}</select><p class="emsg"></p></div></div>
<div class="field loc-field"><span class="flabel">{tx('f.loc')}</span>
<div class="loc-btns"><button type="button" class="btn btn-line btn-sm loc-cur">{ic('target')}{tx('f.loc.cur')}</button><button type="button" class="btn btn-line btn-sm loc-map">{ic('pin')}{tx('f.loc.map')}</button></div>
<div class="loc-status" role="status" aria-live="polite"></div>
<input type="hidden" name="lat"><input type="hidden" name="lng"><p class="hint">{tx('f.loc.note')}</p></div>
<div class="field"><label for="{p}Area">{tx('f.area')} <span class="req">*</span></label><input id="{p}Area" name="area" maxlength="120" required placeholder="{esc(plain('f.ph.area'))}" data-i18n-ph="f.ph.area"><p class="emsg"></p></div>
<div class="frow"><div class="field"><label for="{p}Brand">{tx('f.brand')}</label><input id="{p}Brand" name="brand" maxlength="40" placeholder="{esc(plain('f.ph.brand'))}" data-i18n-ph="f.ph.brand"><p class="emsg"></p></div>
<div class="field"><label for="{p}Date">{tx('f.date')}</label><input id="{p}Date" name="date" type="date"><p class="emsg"></p></div></div>
<div class="field"><label for="{p}Msg">{tx('f.msg')}</label><textarea id="{p}Msg" name="msg" rows="3" maxlength="500" placeholder="{esc(plain('f.ph.msg'))}" data-i18n-ph="f.ph.msg"></textarea></div>
<button class="btn btn-wa" type="submit">{wa_ic()}{tx('f.submit')}</button><p class="form-msg" role="status" aria-live="polite"></p></form>'''

def modals():
    return f'''<div class="modal" id="bookModal" aria-hidden="true"><div class="modal-bg" data-close-modal></div>
<div class="modal-panel" role="dialog" aria-modal="true" aria-labelledby="mTitle"><button type="button" class="modal-x" data-close-modal aria-label="{esc(plain('f.close'))}" data-i18n-aria="f.close">×</button>{booking_form('m')}</div></div>
<div class="modal" id="mapModal" aria-hidden="true"><div class="modal-bg" data-close-modal></div>
<div class="modal-panel map-panel" role="dialog" aria-modal="true" aria-labelledby="mapTitle"><button type="button" class="modal-x" data-close-modal aria-label="{esc(plain('f.close'))}" data-i18n-aria="f.close">×</button>
<h2 id="mapTitle">{tx('map.title')}</h2>
<form class="map-search"><input type="search" placeholder="{esc(plain('map.search'))}" data-i18n-ph="map.search" aria-label="{esc(plain('map.search'))}" data-i18n-aria="map.search"><button class="btn btn-primary btn-sm" type="submit">{tx('map.go')}</button></form>
<p class="map-hint">{tx('map.hint')}</p><div id="pickMap" class="pick-map"></div><p class="map-msg" role="status" aria-live="polite"></p>
<div class="modal-foot"><button type="button" class="btn btn-line btn-sm map-me">{ic('target')}{tx('map.me')}</button><button type="button" class="btn btn-primary map-use" disabled>{ic('check')}{tx('map.use')}</button></div></div></div>'''

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
        'areaServed': {'@type': 'City', 'name': CITY},
        'knowsLanguage': ['en', 'te', 'hi'],
    }
def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + u} for i, (n, u) in enumerate(items)]}

def head(title, desc, path, title_key=None, ld=(), og_img=None):
    url = SITE + path
    og = og_img or SITE + '/assets/img/og-image.jpg'
    tk = f' data-title-key="{title_key}"' if title_key else ''
    lds = ''.join('<script type="application/ld+json">%s</script>\n' % json.dumps(x, ensure_ascii=False) for x in ld)
    return f'''<!DOCTYPE html>
<html lang="en" class="no-js"{tk}>
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&display=swap">
<link rel="stylesheet" href="/assets/css/style.css?v=13">
<script>try{{var l=localStorage.getItem('bobby-lang');if(l==='te'||l==='hi')document.documentElement.lang=l}}catch(e){{}}</script>
{lds}</head>
<body>
<a class="skip" href="#main" data-i18n="skip">{en('skip')}</a>
'''

def lang_switch():
    return f'''<div class="lang">
<button class="lang-btn" type="button" aria-haspopup="true" aria-expanded="false" aria-label="Language / భాష / भाषा">{ic('globe')}<span class="code lang-code">EN</span>{ic('chev','chev')}</button>
<ul class="lang-menu" role="menu">
<li><button type="button" role="menuitemradio" aria-checked="true" data-lang="en">English</button></li>
<li><button type="button" role="menuitemradio" aria-checked="false" data-lang="te" class="te" lang="te">తెలుగు</button></li>
<li><button type="button" role="menuitemradio" aria-checked="false" data-lang="hi" class="hi" lang="hi">हिन्दी</button></li>
</ul></div>'''

def header(active):
    links = ''.join(f'<a href="{u}"{" aria-current=\"page\"" if a == active else ""}>{tx(k)}</a>' for u, k, a in NAV)
    return f'''<div class="topbar"><div class="wrap">
<span>{ic('pin')}{tx('loc.short')} · {tx('hours.open')}</span>
<span>{ic('phone')}<a href="tel:{PHONE_TEL}">{PHONE_TXT}</a> · <a href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{tx('btn.wa')}</a></span>
</div></div>
<header class="hdr">
<div class="wrap">
<a class="logo" href="/" aria-label="BOBBY AC Repair &amp; Home Appliance Services – Home"><img class="wm" src="/assets/img/bobby-wordmark.webp" width="142" height="56" alt="BOBBY AC Repair &amp; Home Appliance Services"></a>
<nav class="nav" aria-label="Main">{links}</nav>
<div class="hdr-actions">
{lang_switch()}
<a class="btn btn-primary btn-sm btn-call" href="tel:{PHONE_TEL}">{ic('phone')}<span class="lbl" data-i18n="btn.call">{en('btn.call')}</span></a>
<a class="btn btn-wa btn-sm" href="/contact/#book" data-book="" aria-label="{esc(plain('btn.bookservice'))}" data-i18n-aria="btn.bookservice">{wa_ic()}<span class="lbl" data-i18n="btn.bookservice">{en('btn.bookservice')}</span></a>
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
    q = ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' for u, k, a in NAV) + f'<li><a href="/blog/">{tx("nav.blog")}</a></li>'
    acl = [('/ac-services/#ac-repair','svc.ac_repair.name'),('/ac-services/#ac-servicing','svc.ac_servicing.name'),
           ('/ac-services/#ac-installation','svc.ac_install.name'),('/ac-services/#ac-uninstallation','svc.ac_uninstall.name'),
           ('/ac-services/#ac-gas-filling','svc.ac_gas.name'),('/ac-services/#ac-deep-cleaning','ft.maint')]
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
<script src="/assets/js/main.js?v=11" defer></script>
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
def ac_cards(featured_first=False):
    out = []
    for i, (L, anchor, pk, sk, n, prk) in enumerate(AC_BLOCKS):
        lis = ''.join(f'<li>{tx("ac.%s.%d" % (L, j))}</li>' for j in range(1, n + 1))
        note = f'<p class="note">{ic("info")}{tx("ac.E.note")}</p>' if L == 'E' else ''
        feat = ' ac-featured' if (featured_first and i == 0) else ''
        out.append(f'''<article class="scard reveal d{i % 3}{feat}" id="{anchor}">
<div class="media">{img(pk, 960 if feat else 640, 600 if feat else 400, "ac.%s.t" % L)}<span class="tag">{tx("ac.%s.t" % L)}</span>{price(prk, "tag")}</div>
<div class="body"><h3>{tx("ac.%s.t" % L)}</h3><p>{tx("ac.%s.d" % L)}</p><ul class="ticks">{lis}</ul>{note}
<div class="actions">{book_a(sk, 'btn-primary btn-sm')}<a class="btn btn-line btn-sm" href="tel:{PHONE_TEL}">{ic('phone')}{tx("btn.call")}</a></div></div></article>''')
    pf = f'<p class="price-foot">{tx("price.note")}</p>' if any_price() else ''
    return '<div class="ac-grid">' + ''.join(out) + '</div>' + pf

AP_BLOCKS = [('fridge', 'refrigerator'), ('washer', 'washing-machine'), ('cooler', 'air-cooler'), ('fan', 'ceiling-fan')]
def app_cards():
    out = []
    for i, (k, anchor) in enumerate(AP_BLOCKS):
        lis = ''.join(f'<li>{tx("ap.%s.%d" % (k, j))}</li>' for j in range(1, 4))
        out.append(f'''<article class="scard reveal d{i}" id="{anchor}">
<div class="media">{img(k, 600, 450, "ap.%s.t" % k)}<span class="tag">{tx("svc.%s.name" % k)}</span>{price(k, "tag")}</div>
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
    banner = f'''<figure class="brand-banner reveal"><img src="/assets/img/brands-banner-lg.webp" srcset="/assets/img/brands-banner-sm.webp 836w, /assets/img/brands-banner-lg.webp 1672w" sizes="(max-width: 1240px) 100vw, 1200px" width="1672" height="941" loading="lazy" decoding="async" alt="BOBBY AC Repair &amp; Home Appliance Services banner: we repair and service LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier and Voltas" data-i18n-alt="brands.banner"></figure>'''
    tiles = ''.join(f'<div class="brand reveal d{i % 4}">{brand_logo(b)}</div>' for i, b in enumerate(BRANDS))
    grid = f'<div class="brands" style="margin-top:22px">{tiles}</div>' if tiles_too else ''
    return f'''{banner}{grid}
<p class="brand-note reveal">{ic('info')}<span>{tx('brands.note')} <a class="link-arrow" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{tx('brands.ask')}</a></span></p>'''

WHY_ICONS = ['home', 'ac', 'layers', 'talk', 'rupee', 'chat', 'heart']
def why_cards():
    return '<div class="why-grid">' + ''.join(
        f'<div class="wcard reveal d{i % 4}"><div class="ic">{ic(WHY_ICONS[i])}</div><h3>{tx("why.%d.t" % (i + 1))}</h3><p>{tx("why.%d.d" % (i + 1))}</p></div>'
        for i in range(7)) + '</div>'

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
         else f'<span class="rc-src rc-demo">DEMO</span>' if src == 'demo'
         else f'<span class="rc-src">{esc(SOURCE_LABEL["direct"])}</span>')
    return f'''<li class="rc-slide"><article class="rc-card{' is-demo' if src == 'demo' else ''}">
<header><span class="rc-av" aria-hidden="true">{initial}</span><span class="rc-who"><b>{esc(r["name"])}</b><small>{ic("pin")}{esc(r.get("area", ""))}</small></span>{g}</header>
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
    """Trust facts marquee + 'What Our Customers Say' carousel (genuine reviews only)."""
    cards = ''.join(f'<figure class="tr-card"><span class="tr-ic">{ic(icn)}</span><figcaption><b>{tx("tr.%d.t" % n)}</b><span>{tx("tr.%d.d" % n)}</span></figcaption></figure>' for icn, n in TRUST)
    body = review_carousel(REVIEWS) if REVIEWS else f'<div class="rc-empty reveal"><div class="rev-stars" aria-hidden="true">' + ''.join(f'<span style="--i:{i}">★</span>' for i in range(5)) + f'</div><p>{tx("rev.first")}</p></div>'
    return f'''<section class="sec rev-sec" id="trust"><div class="wrap">
<div class="sec-head center reveal"><p class="eyebrow">{tx("tr.eyebrow")}</p><h2>{tx("tr.h2")}</h2></div></div>
<div class="rev-marquee reveal" aria-label="Why customers choose BOBBY"><div class="rev-belt">{cards}<div class="rev-dup" aria-hidden="true">{cards}</div></div></div></section>
<section class="sec rc-sec" id="reviews"><div class="wrap">
<div class="sec-head center reveal"><p class="eyebrow">{tx("rev.eyebrow")}</p><h2>{tx("rev.h2")}</h2><p class="lead">{tx("rev.sub2")}</p></div>
{body}{review_buttons()}</div></section>'''

def location_block(h='h2'):
    return f'''<section class="sec sec-alt" id="service-area"><div class="wrap loc-grid">
<div class="reveal"><p class="eyebrow">{tx("loc.eyebrow")}</p><{h}>{tx("loc.h2")}</{h}><p style="margin-top:14px">{tx("loc.p1")}</p><p>{tx("loc.p2")}</p>
<ul class="cover"><li><span class="ci-ic">{ic('pin')}</span>{tx("addr.full")}</li><li><span class="ci-ic">{ic('star')}</span>{tx("hours.open")}</li><li><span class="ci-ic">{ic('radius')}</span>{tx("loc.c2")}</li><li><span class="ci-ic">{ic('phone')}</span>{tx("loc.c3")}</li></ul>
<div class="btn-row"><a class="btn btn-primary" href="tel:{PHONE_TEL}">{ic('phone')}{tx("btn.callnum")}</a><a class="btn btn-line" href="{DIR_URL}" target="_blank" rel="noopener">{ic('pin')}{tx("btn.dir")}</a></div></div>
<div class="map reveal d2"><iframe title="{esc(plain('loc.map'))}" data-i18n-aria="loc.map" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe></div>
</div></section>'''

def faq_list(nums, first_open=True):
    return '<div class="faq">' + ''.join(
        f'<details class="reveal"{" open" if (first_open and i == 0) else ""}><summary>{tx("faq.%d.q" % n, "h3", attrs="style=\"font-size:inherit;color:inherit;font-weight:inherit\"")}<span class="pm">{ic("plus")}</span></summary><div class="ans">{tx("faq.%d.a" % n, "p")}</div></details>'
        for i, n in enumerate(nums)) + '</div>'

def blog_cards(posts):
    return '<div class="blog-grid">' + ''.join(f'''<article class="bcard reveal d{i % 3}"><a class="media" href="/blog/{p['slug']}/" tabindex="-1" aria-hidden="true">{img(p['img'], 640, 360, 'post.%s.title' % p['slug'])}</a>
<div class="body"><h3><a href="/blog/{p['slug']}/">{tx('post.%s.title' % p['slug'])}</a></h3><p>{tx('post.%s.excerpt' % p['slug'])}</p><a class="link-arrow" href="/blog/{p['slug']}/">{tx('btn.more')}{ic('arrow')}</a></div></article>''' for i, p in enumerate(posts)) + '</div>'

def cta_band():
    return f'''<section class="cta-band"><div class="wrap"><div class="cta-inner reveal">
<div><h2>{tx("cta.h2")}</h2><p>{tx("cta.sub")}</p></div>
<div class="btn-row"><a class="btn btn-orange" href="tel:{PHONE_TEL}">{ic('phone')}{tx("btn.callnum")}</a>{book_a('', 'btn-ghost', 'btn.bookservice')}</div>
</div></div></section>'''

# ---------------- pages ----------------
PAGES = {}
def page(path, html_):
    PAGES[path] = html_

def build_home():
    ld = [business_ld(),
          {'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': BRAND, 'inLanguage': ['en', 'te', 'hi'], 'publisher': {'@id': SITE + '/#business'}},
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
<a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}</a>
<a class="btn btn-wa" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener">{wa_ic()}{tx('btn.wachat')}</a>
</div>
<p class="trust anim d4">{ic('check')}{tx('hero.trust')}</p>
</div>
<div class="hero-visual anim d2">
<svg class="airflow" viewBox="0 0 300 200" fill="none" stroke="#9FE6FF" stroke-width="5" stroke-linecap="round" aria-hidden="true"><path d="M10 40 C80 10 140 70 220 40 S290 20 300 30"/><path d="M0 80 C70 50 150 110 230 80 S290 60 300 70"/><path d="M20 120 C90 90 160 150 240 120"/><path d="M10 160 C80 130 140 190 220 160"/></svg>
<div class="hero-photo">{img('hero', 640, 690, 'svc.ac_repair.name', eager=True)}</div>
{chips_html}
<div class="hero-card"><span class="temp">24°C</span><span><b data-i18n="hero.card.title">{en('hero.card.title')}</b><small data-i18n="hero.card.sub">{en('hero.card.sub')}</small></span></div>
</div></div></section>'''
    body = (hero + stats_block() + reviews_block() +
        f'<section class="sec sec-alt" id="ac-services"><div class="wrap">{sec_head("acsec.eyebrow", "acsec.h2", "acsec.sub")}{ac_cards()}<p class="center reveal" style="text-align:center;margin-top:28px"><a class="btn btn-line" href="/ac-services/">{tx("btn.allac")}{ic("arrow")}</a></p></div></section>' +
        f'<section class="sec app-sec" id="appliances"><div class="wrap">{sec_head("appsec.eyebrow", "appsec.h2", "appsec.sub")}{app_cards()}</div></section>' +
        f'<section class="sec sec-alt" id="brands"><div class="wrap">{sec_head("brands.eyebrow", "brands.h2", "brands.sub")}{brands_block()}</div></section>' +
        f'''<section class="sec" id="why"><div class="wrap why-split"><div class="why-photo tech reveal">{img('technician', 768, 512, 'why.h2')}<div class="badge"><img src="/assets/img/bobby-logo-160.webp" width="44" height="44" alt="" loading="lazy">{tx('brand.tagline')}</div></div>
<div>{sec_head("why.eyebrow", "why.h2", None, center=False)}{why_cards()}</div></div></section>''' +
        steps_block() +
        f'<section class="sec" id="faq"><div class="wrap">{sec_head("faqh.eyebrow", "faqh.h2")}{faq_list([1, 4, 5, 10, 11, 12])}<p style="text-align:center;margin-top:20px" class="reveal"><a class="btn btn-line" href="/faqs/">{tx("btn.allfaq")}{ic("arrow")}</a></p></div></section>' +
        f'<section class="sec sec-alt" id="blog"><div class="wrap">{sec_head("blogh.eyebrow", "blogh.h2", "blogh.sub")}{blog_cards(POSTS[:3])}<p style="text-align:center;margin-top:28px" class="reveal"><a class="btn btn-line" href="/blog/">{tx("btn.allblog")}{ic("arrow")}</a></p></div></section>' +
        '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band())
    page('/', head('BOBBY AC Repair & Home Appliance Services in Narasaraopet | AC Installation & Repair',
                   'Looking for AC repair in Narasaraopet? BOBBY provides AC servicing, installation, uninstallation, gas filling and home appliance repair. Call or WhatsApp +91 83748 89163.',
                   '/', None, ld) + header('home') + body + footer())

def service_ld(name, desc, path):
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'description': desc, 'serviceType': name,
            'provider': {'@id': SITE + '/#business'}, 'areaServed': {'@type': 'City', 'name': CITY}, 'url': SITE + path}

def build_inner():
    # about
    p = '/about/'
    page(p, head('About BOBBY AC Repair & Home Appliance Services | Narasaraopet', 'BOBBY AC Repair & Home Appliance Services is a local AC and home appliance service provider in Narasaraopet, Andhra Pradesh. Learn how we work.', p, 'nav.about',
                 [business_ld(), crumbs_ld([('Home', '/'), ('About Us', p)])]) + header('about') +
         phero('p.about.h1', 'p.about.sub', [('crumb.home', '/'), ('nav.about', p)]) +
         f'''<section class="sec"><div class="wrap about-grid"><div class="reveal"><h2>{tx('about.who.h')}</h2><p class="lead" style="margin-top:12px">{tx('about.who.p1')}</p><p class="lead" style="margin-top:12px">{tx('about.who.p2')}</p>
<h2 style="margin-top:34px">{tx('about.how.h')}</h2><ul class="points">{''.join(f'<li>{tx("about.how.%d" % i)}</li>' for i in range(1,5))}</ul></div>
<div class="ph reveal d2">{img('about', 640, 540, 'about.who.h')}</div></div></section>
<section class="sec sec-alt"><div class="wrap">{sec_head("why.eyebrow", "why.h2")}{why_cards()}</div></section>
<section class="sec"><div class="wrap" style="max-width:860px;text-align:center"><div class="reveal"><h2>{tx('about.area.h')}</h2><p class="lead" style="margin:12px auto 22px">{tx('about.area.p')}</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-primary" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}</a>{book_a('', 'btn-wa', 'btn.bookservice')}</div></div></div></section>''' +
         steps_block() + '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band() + footer())

    # AC services
    p = '/ac-services/'
    sl = [service_ld(plain('ac.%s.t' % L), plain('ac.%s.d' % L), p + '#' + a) for L, a, *_ in AC_BLOCKS]
    page(p, head('AC Repair, Servicing, Installation & Gas Filling in Narasaraopet | BOBBY',
                 'AC repair, servicing, installation, uninstallation, gas filling and deep cleaning for split and window ACs in Narasaraopet. Book BOBBY on call or WhatsApp: +91 83748 89163.',
                 p, 'nav.ac', [business_ld(), crumbs_ld([('Home', '/'), ('AC Services', p)])] + sl) + header('ac') +
         phero('p.ac.h1', 'p.ac.sub', [('crumb.home', '/'), ('nav.ac', p)]) +
         f'''<section class="sec"><div class="wrap">{sec_head("acsec.eyebrow", "acsec.h2", "acsec.sub")}{ac_cards()}</div></section>
<section class="sec sec-alt"><div class="wrap loc-grid"><div class="reveal"><h2>{tx('ac.types.h')}</h2><p class="lead" style="margin-top:12px">{tx('ac.types.p')}</p><p class="note" style="margin-top:18px">{ic('info')}{tx('ac.E.note')}</p></div>
<div class="reveal d2">{faq_list([2, 4, 5, 6], first_open=False)}</div></div></section>''' +
         steps_block() + '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band() + footer())

    # Appliance
    p = '/appliance-services/'
    sl = [service_ld(plain('ap.%s.t' % k), plain('svc.%s.desc' % k), p + '#' + a) for k, a in AP_BLOCKS]
    page(p, head('Refrigerator, Washing Machine, Air Cooler & Fan Repair in Narasaraopet | BOBBY',
                 'Doorstep refrigerator, washing machine, air cooler and ceiling fan repair in Narasaraopet. Call or WhatsApp BOBBY AC Repair & Home Appliance Services: +91 83748 89163.',
                 p, 'nav.appliance', [business_ld(), crumbs_ld([('Home', '/'), ('Appliance Services', p)])] + sl) + header('app') +
         phero('p.app.h1', 'p.app.sub', [('crumb.home', '/'), ('nav.appliance', p)]) +
         f'''<section class="sec app-sec"><div class="wrap">{sec_head("appsec.eyebrow", "appsec.h2", "appsec.sub")}{app_cards()}</div></section>
<section class="sec sec-alt"><div class="wrap">{sec_head("faqh.eyebrow", "faqh.h2")}{faq_list([7, 8, 9, 13])}</div></section>''' +
         '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band() + footer())

    # Brands
    p = '/brands/'
    page(p, head('Brands We Service | Multi-Brand AC & Appliance Repair in Narasaraopet',
                 'Independent multi-brand AC and home appliance service in Narasaraopet for LG, Daikin, Blue Star, Samsung, Panasonic, Hitachi, Carrier, Godrej, Haier and Voltas products.',
                 p, 'nav.brands', [business_ld(), crumbs_ld([('Home', '/'), ('Brands We Service', p)])]) + header('brands') +
         phero('p.brands.h1', 'p.brands.sub', [('crumb.home', '/'), ('nav.brands', p)]) +
         f'''<section class="sec"><div class="wrap">{sec_head("brands.eyebrow", "brands.h2", "brands.sub")}{brands_block(True)}</div></section>
<section class="sec sec-alt"><div class="wrap">{faq_list([10])}</div></section>''' +
         '<div style="height:clamp(64px,8vw,100px)"></div>' + cta_band() + footer())

    # FAQs (FAQPage schema: every Q&A here is visible on this page)
    p = '/faqs/'
    fld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': plain('faq.%d.q' % n), 'acceptedAnswer': {'@type': 'Answer', 'text': plain('faq.%d.a' % n)}} for n in range(1, FAQ_N + 1)]}
    page(p, head('AC Repair FAQs Narasaraopet | Gas Filling, Servicing, Installation | BOBBY',
                 'Answers to common questions about AC repair, gas filling, servicing, installation and appliance repair in Narasaraopet from BOBBY AC Repair & Home Appliance Services.',
                 p, 'nav.faqs', [business_ld(), crumbs_ld([('Home', '/'), ('FAQs', p)]), fld]) + header('faqs') +
         phero('p.faqs.h1', 'p.faqs.sub', [('crumb.home', '/'), ('nav.faqs', p)]) +
         f'<section class="sec"><div class="wrap">{faq_list(range(1, FAQ_N + 1))}</div></section>' + cta_band() + footer())

    # Contact
    p = '/contact/'
    form = booking_form('c', inline=True)
    cards = f'''<div class="ccards reveal">
<a class="ccard" href="tel:{PHONE_TEL}"><span class="ic" style="background:linear-gradient(135deg,var(--blue),#0E6FB3)">{ic('phone')}</span><span><small>{tx('c.call.h')}</small><b>{PHONE_TXT}</b></span></a>
<a class="ccard" href="{wa_default()}" data-wa="default" target="_blank" rel="noopener"><span class="ic" style="background:#fff;border:1px solid var(--line)">{wa_ic()}</span><span><small>{tx('c.wa.h')}</small><b>{PHONE_TXT}</b></span></a>
<a class="ccard" href="{DIR_URL}" target="_blank" rel="noopener"><span class="ic" style="background:var(--navy)">{ic('pin')}</span><span><small>{tx('c.loc.h')} · {tx('btn.dir')}</small><b style="font-size:14.5px;font-weight:600">{tx('addr.full')}</b></span></a>
<div class="ccard"><span class="ic" style="background:#1FA855">{ic('star')}</span><span><small>{tx('c.hours.h')}</small><b>{tx('hours.open')}</b></span></div>
<div class="ccard"><span class="ic" style="background:linear-gradient(135deg,#FFB061,var(--orange-d))">{ic('radius')}</span><span><small>{tx('c.area.h')}</small><b>{tx('c.area.v')}</b></span></div>
<div class="map" style="margin-top:6px"><iframe title="{esc(plain('loc.map'))}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{MAP_EMBED}"></iframe></div></div>'''
    page(p, head('Contact BOBBY AC Repair & Home Appliance Services | Book AC Service in Narasaraopet',
                 'Book AC repair or appliance service in Narasaraopet. Call or WhatsApp BOBBY AC Repair & Home Appliance Services on +91 83748 89163 or use the online booking form.',
                 p, 'nav.contact', [business_ld(), crumbs_ld([('Home', '/'), ('Contact Us', p)])]) + header('contact') +
         phero('p.contact.h1', 'p.contact.sub', [('crumb.home', '/'), ('nav.contact', p)]) +
         f'<section class="sec"><div class="wrap contact-grid">{cards}{form}</div></section>' + footer())

    # Blog index + posts
    p = '/blog/'
    page(p, head('AC & Appliance Care Tips | Knowledge Centre | BOBBY Narasaraopet',
                 'Simple guides on AC cooling problems, servicing, gas filling, water leakage, split vs window AC and refrigerator care from BOBBY AC Repair & Home Appliance Services, Narasaraopet.',
                 p, 'nav.blog', [business_ld(), crumbs_ld([('Home', '/'), ('Blog', p)])]) + header('blog') +
         phero('p.blog.h1', 'p.blog.sub', [('crumb.home', '/'), ('nav.blog', p)]) +
         f'<section class="sec"><div class="wrap">{blog_cards(POSTS)}</div></section>' + cta_band() + footer())
    for post in POSTS:
        s = post['slug']; pp = '/blog/%s/' % s
        title_en = plain('post.%s.title' % s)
        art = {'@context': 'https://schema.org', '@type': 'BlogPosting', 'headline': title_en, 'description': plain('post.%s.excerpt' % s),
               'datePublished': post['date'], 'dateModified': post['date'], 'inLanguage': 'en', 'mainEntityOfPage': SITE + pp,
               'image': SITE + art_url(post['img']), 'author': {'@id': SITE + '/#business'}, 'publisher': {'@id': SITE + '/#business'}}
        others = [x for x in POSTS if x['slug'] != s][:3]
        page(pp, head(title_en + ' | BOBBY AC Repair Narasaraopet', plain('post.%s.excerpt' % s), pp, 'post.%s.title' % s,
                      [business_ld(), crumbs_ld([('Home', '/'), ('Blog', '/blog/'), (title_en, pp)]), art],
                      og_img=SITE + art_url(post['img'])) + header('blog') +
             f'''<section class="phero"><div class="wrap"><nav class="crumbs anim" aria-label="Breadcrumb"><ol><li><a href="/">{tx('crumb.home')}</a></li><li><a href="/blog/">{tx('nav.blog')}</a></li><li aria-current="page">{tx('post.%s.title' % s)}</li></ol></nav>
<h1 class="anim d1">{tx('post.%s.title' % s)}</h1><p class="anim d2">{tx('post.%s.excerpt' % s)}</p></div></section>
<section class="sec"><article class="wrap article"><div class="cover-img reveal">{img(post['img'], 1200, 600, 'post.%s.title' % s, eager=True)}</div>
<div class="prose" data-i18n="post.{s}.body">{en('post.%s.body' % s)}</div>
<p class="disc">{tx('blog.disclaimer')}</p>
<div class="cta-box reveal"><div><h3>{tx('blog.related')}</h3><p>{tx('blog.relatedp')}</p></div><div class="btn-row">{book_a(post['svc'], 'btn-orange btn-sm')}<a class="btn btn-ghost btn-sm" href="{post['link']}">{tx('blog.viewsvc')}</a></div></div>
</article></section>
<section class="sec sec-alt"><div class="wrap"><div class="sec-head reveal"><h2>{tx('blog.more')}</h2></div>{blog_cards(others)}</div></section>''' + footer())

    # legal + sitemap + 404
    for path, hk, bk, ttl, act in [('/privacy-policy/', 'p.privacy.h1', 'priv.body', 'Privacy Policy', 'privacy'), ('/terms/', 'p.terms.h1', 'terms.body', 'Terms & Conditions', 'terms')]:
        page(path, head(ttl + ' | BOBBY AC Repair & Home Appliance Services', ttl + ' for the BOBBY AC Repair & Home Appliance Services website, Narasaraopet.', path, hk,
                        [crumbs_ld([('Home', '/'), (ttl, path)])]) + header(act) +
             phero(hk, None, [('crumb.home', '/'), (hk, path)]) +
             f'<section class="sec"><div class="wrap legal prose" data-i18n="{bk}">{en(bk)}</div><p class="wrap legal disc">Last updated: {UPDATED}</p></section>' + footer())
    groups = [('nav.home', [('/', 'nav.home'), ('/about/', 'nav.about'), ('/contact/', 'nav.contact'), ('/faqs/', 'nav.faqs')]),
              ('nav.ac', [('/ac-services/', 'nav.ac')] + [('/ac-services/#' + a, 'ac.%s.t' % L) for L, a, *_ in AC_BLOCKS]),
              ('nav.appliance', [('/appliance-services/', 'nav.appliance')] + [('/appliance-services/#' + a, 'ap.%s.t' % k) for k, a in AP_BLOCKS] + [('/brands/', 'nav.brands')]),
              ('nav.blog', [('/blog/', 'nav.blog')] + [('/blog/%s/' % x['slug'], 'post.%s.title' % x['slug']) for x in POSTS]),
              ('ft.privacy', [('/privacy-policy/', 'ft.privacy'), ('/terms/', 'ft.terms')])]
    sm = ''.join(f'<div><h2>{tx(g)}</h2><ul>' + ''.join(f'<li><a href="{u}">{tx(k)}</a></li>' for u, k in items) + '</ul></div>' for g, items in groups)
    page('/sitemap/', head('Sitemap | BOBBY AC Repair & Home Appliance Services', 'All pages on the BOBBY AC Repair & Home Appliance Services website.', '/sitemap/', 'p.sitemap.h1',
                           [crumbs_ld([('Home', '/'), ('Sitemap', '/sitemap/')])]) + header('sitemap') +
         phero('p.sitemap.h1', None, [('crumb.home', '/'), ('p.sitemap.h1', '/sitemap/')]) +
         f'<section class="sec"><div class="wrap smap">{sm}</div></section>' + footer())
    page('/404.html', head('Page not found | BOBBY AC Repair & Home Appliance Services', 'Page not found.', '/404.html', 'p.404.h1').replace('index, follow', 'noindex') + header('') +
         f'''<section class="phero" style="text-align:center"><div class="wrap"><h1>{tx('p.404.h1')}</h1><p style="margin:0 auto 24px">{tx('p.404.sub')}</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn-orange" href="/">{tx('btn.home')}</a><a class="btn btn-ghost" href="tel:{PHONE_TEL}">{ic('phone')}{tx('btn.callnum')}</a></div></div></section>
<section class="sec"><div class="wrap">{quick_cards()}</div></section>''' + footer())

    # DEMO preview of the review carousel (noindex, not in sitemap, not linked). Replace with genuine reviews before use.
    page('/reviews-preview/', head('Review carousel preview (DEMO) | BOBBY', 'Internal preview of the review carousel with sample data.', '/reviews-preview/', None).replace('index, follow', 'noindex, nofollow') + header('') +
         f'''<div class="demo-banner" role="note"><b>DEMO PREVIEW</b> — sample layout only. These are NOT real customers or real reviews. Not shown on the live site and hidden from search engines.</div>
<section class="sec rc-sec"><div class="wrap"><div class="sec-head center"><p class="eyebrow">{tx("rev.eyebrow")}</p><h2>{tx("rev.h2")}</h2><p class="lead">{tx("rev.sub2")}</p></div>
{review_carousel(DEMO_REVIEWS, 'Demo sample reviews')}{review_buttons()}</div></section>''' + footer())

# ---------------- write ----------------
def write():
    out = os.path.join(os.path.dirname(__file__), 'dist')
    if os.path.exists(out): shutil.rmtree(out)
    shutil.copytree(os.path.join(os.path.dirname(__file__), 'static'), out)
    for path, content in PAGES.items():
        fp = os.path.join(out, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(out, path.strip('/'))
        if path == '/': fp = os.path.join(out, 'index.html')
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, 'w', encoding='utf-8').write(content)
    os.makedirs(os.path.join(out, 'assets/i18n'), exist_ok=True)
    for i, l in enumerate(['en', 'te', 'hi']):
        json.dump({k: v[i] for k, v in S.items()}, open(os.path.join(out, 'assets/i18n/%s.json' % l), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    urls = [p for p in PAGES if p.endswith('/') and p != '/reviews-preview/']
    pri = lambda p: '1.0' if p == '/' else ('0.9' if p in ('/ac-services/', '/contact/') else ('0.6' if p.startswith('/blog/') or p in ('/privacy-policy/', '/terms/', '/sitemap/') else '0.8'))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'<url><loc>{SITE}{u}</loc><lastmod>{UPDATED}</lastmod><priority>{pri(u)}</priority></url>\n' for u in urls) + '</urlset>\n'
    open(os.path.join(out, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(out, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    open(os.path.join(out, 'site.webmanifest'), 'w').write(json.dumps({'name': BRAND, 'short_name': 'BOBBY AC', 'start_url': '/', 'display': 'standalone',
        'background_color': '#102C50', 'theme_color': '#102C50', 'icons': [{'src': '/assets/img/icon-192.png', 'sizes': '192x192', 'type': 'image/png'}, {'src': '/assets/img/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}))
    open(os.path.join(out, '_headers'), 'w').write('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=(self)\n/assets/*\n  Cache-Control: public, max-age=604800\n')
    print('Built %d pages -> %s' % (len(PAGES), out))

if __name__ == '__main__':
    build_home(); build_inner(); write()
