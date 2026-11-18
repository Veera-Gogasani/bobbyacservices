# -*- coding: utf-8 -*-
"""Builds /ac-spare-parts/ – imported by build.py (receives its helpers via init())."""
from urllib.parse import quote
import spare_parts as D

PATH = '/ac-spare-parts/'
BRANDS = ['LG', 'Daikin', 'Samsung', 'Voltas', 'Blue Star', 'Panasonic', 'Hitachi', 'Carrier', 'Godrej', 'Haier']
WA_MSG = ('Hello BOBBY, I am enquiring about the AC spare part: {name}. '
          'Please confirm compatibility, availability and approximate replacement cost for my AC model.')


def build(B):
    tx, en, plain, esc, ic, wa_ic, book_a = B.tx, B.en, B.plain, B.esc, B.ic, B.wa_ic, B.book_a
    SITE, PHONE_TEL, WA_NUM = B.SITE, B.PHONE_TEL, B.WA_NUM

    def wa_part(name):
        return 'https://wa.me/%s?text=%s' % (WA_NUM, quote(WA_MSG.format(name=name)))

    counts = {c: sum(1 for p in D.PARTS if p['cat'] == c) for c, _ in D.CATEGORIES}
    chips = (f'<button type="button" class="sp-chip is-on" data-cat="all" aria-pressed="true">{tx("sp.all")}<span class="n">{len(D.PARTS)}</span></button>' +
             ''.join(f'<button type="button" class="sp-chip" data-cat="{c}" aria-pressed="false">{tx("sp.cat." + c)}<span class="n">{counts[c]}</span></button>' for c, _ in D.CATEGORIES))

    rows = ''
    for c, _ in D.CATEGORIES:
        rows += f'<tr class="sp-grp" data-cat="{c}"><th colspan="5" scope="colgroup">{tx("sp.cat." + c)}</th></tr>'
        for p in [x for x in D.PARTS if x['cat'] == c]:
            badge = ''
            cond = p.get('condition') or ('Repair service' if p['unit'] == 'repair' else '')
            if cond:
                badge = f'<span class="sp-cond{" refurb" if cond == "Refurbished" else ""}">{esc(cond)}</span>'
            if p['price']:
                price = f'<b class="sp-amt">{D.price_text(p)}</b><span class="sp-unit">{D.UNIT_LABEL[p["unit"]]}</span>'
            else:
                price = f'<b class="sp-amt sp-por">{tx("sp.por")}</b><span class="sp-unit">model-specific quotation</span>'
            srcs = ', '.join(D.SOURCES[s][0].split(' – ')[0] for s in p['src']) or 'No verified public price'
            price += f'<span class="sp-basis b-{p["basis"] if p["price"] else "none"}" title="{esc(p["note"])}">{D.BASIS_LABEL[p["basis"]] if p["price"] else "Quoted after model check"}</span><span class="sp-src">Source: {esc(srcs)}</span>'
            imgcell = (f'<td class="sp-img sp-photo"><img src="{esc(D.photo_url(p))}" width="120" height="120" loading="lazy" decoding="async" referrerpolicy="no-referrer" alt="{esc(p["name"])} – representative product photo" onerror="this.onerror=null;this.src=\'/assets/img/parts/{p["img"]}.webp\';this.parentNode.classList.remove(\'sp-photo\')"></td>' if D.photo_url(p) else
                       f'<td class="sp-img"><img src="/assets/img/parts/{p["img"]}.webp" width="120" height="120" loading="lazy" decoding="async" alt="Illustration of {esc(p["name"])}"></td>')
            vs = p.get('variants') or []
            var = ''
            if vs:
                lab = ('model' if len(vs) == 1 else f'{len(vs)} models') if p['cat'] == 'remote' or len(vs) == 1 else f'{len(vs)} sizes / ratings'
                var = (f'<details class="sp-var"><summary>View {lab} &amp; price{"s" if len(vs) > 1 else ""}</summary><ul>' +
                       ''.join(f'<li><span>{esc(n)}</span><b>{D.inr(pr) if isinstance(pr, int) else D.inr(pr[0]) + '–' + D.inr(pr[1])}</b></li>' for n, pr in vs) + '</ul></details>')
            search = esc((p['name'] + ' ' + p['desc'] + ' ' + p['cat'] + ' ' + ' '.join(n for n, _ in vs)).lower())
            rows += (f'<tr class="sp-row" id="{p["id"]}" data-cat="{c}" data-q="{search}">' + imgcell +
                     f'<th scope="row" class="sp-name">{esc(p["name"])}{badge}</th>'
                     f'<td class="sp-desc">{esc(p["desc"])}{var}</td>'
                     f'<td class="sp-price">{price}</td>'
                     f'<td class="sp-act"><a class="btn btn-wa btn-sm" href="{wa_part(p["name"])}" target="_blank" rel="noopener" aria-label="{esc(plain("sp.enq"))}: {esc(p["name"])}">{wa_ic()}<span data-i18n="sp.enq">{en("sp.enq")}</span></a></td></tr>')

    table = f'''<div class="sp-tools reveal">
<label class="sp-search"><span class="sr-only" data-i18n="sp.search">{en("sp.search")}</span>{ic("search") if "search" in B.ICONS else ""}<input type="search" id="spQ" autocomplete="off" placeholder="{esc(plain("sp.search"))}" data-i18n-ph="sp.search"></label>
<div class="sp-chips" role="group" aria-label="Filter by category">{chips}</div></div>
<p class="sp-count" aria-live="polite"><span data-i18n="sp.showing">{en("sp.showing")}</span> <b id="spN">{len(D.PARTS)}</b> <span data-i18n="sp.of">{en("sp.of")}</span> {len(D.PARTS)} <span data-i18n="sp.parts">{en("sp.parts")}</span></p>
<div class="sp-tablewrap"><table class="sp-table">
<caption class="sr-only">AC spare parts with indicative market prices in Indian rupees (last reviewed {D.PRICE_REVIEW})</caption>
<thead><tr><th scope="col">{tx("sp.th.img")}</th><th scope="col">{tx("sp.th.name")}</th><th scope="col">{tx("sp.th.desc")}</th><th scope="col">{tx("sp.th.price")}</th><th scope="col">{tx("sp.th.enq")}</th></tr></thead>
<tbody>{rows}</tbody></table>
<p class="sp-empty" id="spEmpty" hidden>{ic("info")}<span>{tx("sp.empty")}</span></p></div>'''

    sources = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener nofollow">{esc(n)}</a></li>' for n, u in D.SOURCES.values())
    basis = ''.join(f'<li><span class="sp-basis b-{k}">{v}</span> {d}</li>' for k, v, d in [
        ('online', D.BASIS_LABEL['online'], '– part-only selling price from an online spare-parts store.'),
        ('ratecard', D.BASIS_LABEL['ratecard'], '– price from a published service rate card or rate contract; may include fitting and/or GST.'),
        ('mixed', D.BASIS_LABEL['mixed'], '– low end from online part prices, high end from service rate cards.')])

    steps = ''.join(f'<li class="reveal d{i % 3}"><span class="sp-stepn">{i}</span><div><h3>{tx("sp.id.%d.t" % i)}</h3><p>{tx("sp.id.%d.d" % i)}</p></div></li>' for i in range(1, 6))
    share = ''.join(f'<li>{ic("check")}{tx("sp.share.%d" % i)}</li>' for i in range(1, 7))
    brands = ''.join(f'<li>{b}</li>' for b in BRANDS)
    faqs = '<div class="faq">' + ''.join(
        f'<details class="reveal"{" open" if i == 1 else ""}><summary><h3 style="font-size:inherit;color:inherit;font-weight:inherit" data-i18n="sp.faq.{i}.q">{en("sp.faq.%d.q" % i)}</h3><span class="pm">{ic("plus")}</span></summary><div class="ans"><p data-i18n="sp.faq.{i}.a">{en("sp.faq.%d.a" % i)}</p></div></details>'
        for i in range(1, 11)) + '</div>'
    wa_gen = 'https://wa.me/%s?text=%s' % (WA_NUM, quote('Hello BOBBY, I need an AC spare part replaced. My AC brand/model: '))

    item_ld = {'@context': 'https://schema.org', '@type': 'ItemList', 'name': 'Residential AC spare parts – indicative price guide',
               'numberOfItems': len(D.PARTS), 'itemListElement': [
                   {'@type': 'ListItem', 'position': i + 1, 'name': p['name'], 'url': SITE + PATH + '#' + p['id'],
                    'image': D.photo_url(p) or SITE + '/assets/img/parts/%s.webp' % p['img']} for i, p in enumerate(D.PARTS)]}
    crumbs = B.crumbs_ld([('Home', '/'), ('AC Services', '/ac-services/'), ('AC Spare Parts', PATH)])

    html_ = (B.head('AC Spare Parts Price List in India | BOBBY Narasaraopet',
                    'Check approximate prices for common residential AC spare parts in India, including capacitors, PCBs, fan motors, compressors, sensors, valves and installation accessories.',
                    PATH, 'sp.crumb', [crumbs, item_ld]) +
             B.header('ac') +
             B.phero('sp.h1', 'sp.sub', [('crumb.home', '/'), ('nav.ac', '/ac-services/'), ('sp.crumb', PATH)]) +
             f'''<section class="sec sp-intro"><div class="wrap sp-intro-grid">
<div class="reveal"><p class="lead">{tx("sp.intro")}</p>
<p class="sp-review">{ic("check")}<span data-i18n="sp.review">{en("sp.review")}</span> <b><time datetime="2026-11-18">{D.PRICE_REVIEW}</time></b></p></div>
<div class="sp-imp reveal d2" role="note"><h2>{ic("info")}{tx("sp.note.h")}</h2><p>{tx("sp.note")}</p></div></div></section>
<section class="sec sec-alt sp-list" id="price-list"><div class="wrap">
<div class="sec-head reveal"><h2>{tx("sp.list.h")}</h2></div>
<p class="note sp-disc reveal">{ic("info")}<span>{tx("sp.disc.top")}</span></p>
{table}
<p class="note sp-disc">{ic("info")}<span>{tx("sp.disc.bot")}</span></p>
<details class="sp-sources"><summary>{tx("sp.src.h")} <small>· {D.PRICE_REVIEW}</small></summary>
<p>{tx("sp.src.p")} Prices were checked on <b>{D.PRICE_REVIEW}</b>.</p><ul class="sp-srcl">{sources}</ul>
<h3>{tx("sp.basis.h")}</h3><ul class="sp-basisl">{basis}</ul>
<p class="sp-muted">Product photos courtesy of <a href="https://apnaspare.com/" target="_blank" rel="noopener">ApnaSpare</a>; parts without a matching photo are shown as BOBBY illustrations. Images are representative — your AC may need a different rating or model of the part.</p></details>
</div></section>
<section class="sec"><div class="wrap sp-two">
<div class="reveal"><h2>{tx("sp.br.h")}</h2><p class="lead" style="margin-top:10px">{tx("sp.br.p")}</p><ul class="sp-brands">{brands}</ul>
<p class="sp-muted">{tx("sp.br.disc")}</p></div>
<div class="sp-share reveal d2"><h2>{tx("sp.share.h")}</h2><ul>{share}</ul>
<a class="btn btn-wa" href="{wa_gen}" target="_blank" rel="noopener">{wa_ic()}{tx("sp.cta.wa")}</a></div></div></section>
<section class="sec sec-alt"><div class="wrap">
<div class="sec-head center reveal"><h2>{tx("sp.id.h")}</h2><p class="lead">{tx("sp.id.sub")}</p></div>
<ol class="sp-steps">{steps}</ol>
<div class="sp-safe reveal" role="note"><h3>{ic("shield")}{tx("sp.safe.h")}</h3><p>{tx("sp.safe")}</p></div></div></section>
<section class="sec"><div class="wrap" style="max-width:900px"><div class="sec-head center reveal"><h2>{tx("sp.faq.h")}</h2></div>{faqs}
<div class="cta-box reveal" id="spare-cta"><div><h2 style="color:#fff;font-size:clamp(22px,2.6vw,28px);margin-bottom:6px">{tx("sp.cta.h")}</h2><p>{tx("sp.cta.p")}</p></div>
<div class="btn-row"><a class="btn btn-orange btn-sm" href="tel:{PHONE_TEL}">{ic("phone")}{tx("btn.callnum")}</a><a class="btn btn-wa btn-sm" href="{wa_gen}" target="_blank" rel="noopener">{wa_ic()}{tx("sp.cta.wa")}</a>{book_a("ac_repair", "btn-ghost btn-sm", "sp.cta.book")}</div></div>
</div></section>
<script src="/assets/js/spare-parts.js?v=3" defer></script>''' + B.footer())
    B.page(PATH, html_)


def promo(B):
    """Card for the AC Services page linking to the guide."""
    return (f'<section class="sec sp-promo-sec"><div class="wrap"><a class="sp-promo reveal" href="{PATH}">'
            f'<img src="/assets/img/parts/cap_dual.webp" width="96" height="96" loading="lazy" alt="">'
            f'<span class="t"><b>{B.tx("sp.promo.h")}</b><span>{B.tx("sp.promo.p")}</span></span>'
            f'<span class="btn btn-line btn-sm">{B.tx("sp.promo.btn")}{B.ic("arrow")}</span></a></div></section>')
