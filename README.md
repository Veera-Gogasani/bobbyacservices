# BOBBY AC Repair & Services — Website

Multi-page website for BOBBY AC Repair & Services, Narasaraopet (English / తెలుగు / हिन्दी).

## What is in this folder
| Path | What it is |
|---|---|
| `dist/` | **The finished website.** Upload this folder to any static host. |
| `build.py` | Generator. Business details, **prices**, reviews and brand list are in its CONFIG block. |
| `strings.py` | Every piece of text on the site, in English, Telugu and Hindi. |
| `blog.py` | The 6 Knowledge Centre articles, in all three languages. |
| `art.py`, `art-src/` | Original BOBBY artwork (vector sources), exported to `static/assets/img/art/`. |
| `static/` | CSS, JavaScript, logo, icons. |

## Updating the site
1. Edit `build.py` (prices, reviews) or `strings.py` (text).
2. Run `python3 build.py` → `dist/` is rebuilt.
3. Push to GitHub. Cloudflare Pages redeploys automatically.

### Prices
In `build.py`, set `PRICE_SRC`, for example `'ac_servicing': 499`. The site automatically shows the price + ₹100
("Starting from ₹599"). Services left as `None` show "Estimate after inspection".

### Reviews
Add genuine reviews only: `REVIEWS = [{'name': 'Customer name', 'service': 'AC Repair', 'text': '...'}]`.

## Free hosting: Cloudflare Pages
1. Put this folder in a GitHub repository (e.g. `bobbyacservices`).
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Connect to Git → choose the repo.
3. Build settings: Framework preset **None**, Build command `python3 build.py`, Build output directory **dist**.
   (Or leave the build command empty and set the output directory to `dist` if you commit the built files.)
4. Deploy. The site goes live at `bobbyacservices.pages.dev`.

## Connecting www.bobbyacservices.com (after buying it on GoDaddy)
1. Cloudflare → Add a domain → `bobbyacservices.com` (Free plan) → Cloudflare shows two nameservers.
2. GoDaddy → My Products → bobbyacservices.com → DNS → Nameservers → Change → "I'll use my own" → paste both.
3. Cloudflare Pages project → Custom domains → add `www.bobbyacservices.com` and `bobbyacservices.com`.
4. HTTPS is issued automatically (usually within an hour).
If the domain changes, edit `SITE` at the top of `build.py` and rebuild.

## After launch (recommended)
- Google Search Console: add the domain, submit `https://www.bobbyacservices.com/sitemap.xml`.
- Google Business Profile: create/verify the listing and link the website. Once you have a verified map pin,
  replace the town-level map on the site with your exact business location.

### Brand logos
Put official logo files (from each brand's press/media kit) in `static/assets/img/brands/`, named
`lg`, `daikin`, `blue-star`, `samsung`, `panasonic`, `hitachi`, `carrier`, `godrej`, `haier`, `voltas`
(`.svg`, `.webp` or `.png`), then run `python3 build.py`. Brands without a file show their name as text.
