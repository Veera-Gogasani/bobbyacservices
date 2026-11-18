/**
 * Domain handling for BOBBY AC Repair (Cloudflare Pages middleware).
 * - bobbyacservices.com (no www)  -> 301 to https://www.bobbyacservices.com (same path)
 * - *.pages.dev                   -> 301 to the main domain ONLY when REDIRECT_PAGES_DEV is true.
 *   Leave it false until www.bobbyacservices.com is connected and working, then set it to true.
 */
const CANONICAL_HOST = 'www.bobbyacservices.com';
const REDIRECT_PAGES_DEV = false;

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const host = url.hostname;
  const isApex = host === 'bobbyacservices.com';
  const isPagesDev = host.endsWith('.pages.dev');
  if (isApex || (REDIRECT_PAGES_DEV && isPagesDev)) {
    url.hostname = CANONICAL_HOST;
    url.protocol = 'https:';
    url.port = '';
    return Response.redirect(url.toString(), 301);
  }
  return context.next();
}
