/* BOBBY – Quick Estimate popup: indicative service + spare-part ranges, PDF download, WhatsApp share. */
(function () {
  var modal = document.getElementById('estModal');
  if (!modal) return;
  var body = modal.querySelector('.est-body');
  var DATA = null, loading = null, sel = {}, parts = [], cats = {}, lastFocus = null;
  var JSPDF_SRC = '/assets/js/vendor/jspdf.umd.min.js';

  function lang() { var l = (document.documentElement.lang || 'en').slice(0, 2); return (l === 'te' || l === 'hi') ? l : 'en'; }
  function L(k) { var d = DATA.labels[lang()] || DATA.labels.en; return d[k] || DATA.labels.en[k] || k; }
  function inr(n) { return Number(n).toLocaleString('en-IN'); }
  function rng(a, b) { return a === b ? '₹' + inr(a) : '₹' + inr(a) + ' – ₹' + inr(b); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  function load() {
    if (DATA) return Promise.resolve(DATA);
    if (loading) return loading;
    loading = fetch(modal.getAttribute('data-src')).then(function (r) { return r.json(); }).then(function (d) { DATA = d; return d; });
    return loading;
  }

  function open(preset) {
    lastFocus = document.activeElement;
    modal.classList.add('open'); modal.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
    body.innerHTML = '<p class="est-load">…</p>';
    load().then(function () {
      var ps = preset && DATA.services.filter(function (s) { return s.id === preset; })[0];
      if (ps) { cats[ps.cat] = true; if (!sel[preset]) sel[preset] = 1; }
      render();
      var f = modal.querySelector('.est-cat'); if (f) f.focus({ preventScroll: true });
    }).catch(function () { body.innerHTML = '<p class="est-load">Could not load prices. Please call +91 83748 89163.</p>'; });
  }
  function close() {
    modal.classList.remove('open'); modal.setAttribute('aria-hidden', 'true');
    if (!document.querySelector('.modal.open')) document.body.style.overflow = '';
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }

  function totals() {
    var lo = 0, hi = 0, plus = false, lines = [];
    DATA.services.forEach(function (s) {
      var q = sel[s.id]; if (!q) return;
      lo += s.min * q; hi += s.max * q; if (s.plus) plus = true;
      lines.push({ name: s.name, en: s.name.en, q: q, min: s.min, max: s.max, plus: s.plus });
    });
    parts.forEach(function (p) {
      lo += p.min * p.q; hi += p.max * p.q;
      lines.push({ name: { en: p.name }, en: p.name, q: p.q, min: p.min, max: p.max, part: true });
    });
    return { lo: lo, hi: hi, plus: plus, lines: lines };
  }

  function stepper(id, q, kind) {
    return '<span class="est-qty" data-kind="' + kind + '" data-id="' + esc(id) + '"><button type="button" data-d="-1" aria-label="−">−</button><b>' + q + '</b><button type="button" data-d="1" aria-label="+">+</button></span>';
  }

  function svcRow(s, lg) {
    var q = sel[s.id] || 0;
    return '<li class="est-svc' + (q ? ' on' : '') + '"><label><input type="checkbox" data-svc="' + s.id + '"' + (q ? ' checked' : '') + '>' +
      '<span class="est-n">' + esc(s.name[lg] || s.name.en) + '<small>' + rng(s.min, s.max) + ' ' + esc(L('est.u.' + s.unit)) + (s.plus ? ' · ' + esc(L('est.plusparts')) : '') + '</small></span></label>' +
      (q ? stepper(s.id, q, 'svc') : '') + '</li>';
  }
  function partsBlock() {
    var groups = {}, order = [];
    DATA.parts.forEach(function (p, i) { if (!groups[p.cat]) { groups[p.cat] = []; order.push(p.cat); } groups[p.cat].push('<option value="' + i + '">' + esc(p.name) + ' (' + rng(p.min, p.max) + ')</option>'); });
    var opts = order.map(function (c) { return '<optgroup label="' + esc(c) + '">' + groups[c].join('') + '</optgroup>'; }).join('');
    var plist = parts.map(function (p, i) {
      return '<li><span class="est-n">' + esc(p.name) + '<small>' + rng(p.min, p.max) + ' ' + esc(p.unit) + '</small></span>' + stepper(i, p.q, 'part') +
        '<button type="button" class="est-rm" data-rm="' + i + '" aria-label="' + esc(L('est.remove')) + '">×</button></li>';
    }).join('');
    return '<div class="est-parts"><p class="est-parts-h">' + esc(L('est.parts')) + '</p><p class="est-mini">' + esc(L('est.parts.p')) + '</p>' +
      '<div class="est-pick"><select aria-label="' + esc(L('est.pick')) + '"><option value="">' + esc(L('est.pick')) + '</option>' + opts + '</select>' +
      '<button type="button" class="btn btn-line btn-sm est-add">' + esc(L('est.add')) + '</button></div>' +
      (plist ? '<ul class="est-list est-plist">' + plist + '</ul>' : '') + '</div>';
  }

  function render() {
    var lg = lang();
    var chips = DATA.cats.map(function (c) {
      var on = !!cats[c.id];
      return '<button type="button" class="est-cat' + (on ? ' on' : '') + '" data-cat="' + c.id + '" aria-pressed="' + on + '"><span class="est-cat-ic">' + c.svg + '</span><span>' + esc(c.name[lg] || c.name.en) + '</span><i class="est-tick" aria-hidden="true">✓</i></button>';
    }).join('');
    var groups = DATA.cats.filter(function (c) { return cats[c.id]; }).map(function (c) {
      var rows = DATA.services.filter(function (s) { return s.cat === c.id; }).map(function (s) { return svcRow(s, lg); }).join('');
      return '<div class="est-grp"><p class="est-grp-h"><span class="est-cat-ic">' + c.svg + '</span>' + esc(c.name[lg] || c.name.en) + '</p><ul class="est-list">' + rows + '</ul>' + (c.id === 'ac' ? partsBlock() : '') + '</div>';
    }).join('');
    var t = totals();
    var sum = t.lines.length ? (
      '<ul class="est-lines">' + t.lines.map(function (l) {
        return '<li><span>' + esc(l.name[lg] || l.en) + (l.q > 1 ? ' × ' + l.q : '') + '</span><b>' + rng(l.min * l.q, l.max * l.q) + '</b></li>';
      }).join('') + '</ul>' +
      '<div class="est-total"><span>' + esc(L('est.total')) + '</span><b>' + rng(t.lo, t.hi) + (t.plus ? '<small>' + esc(L('est.plusparts')) + '</small>' : '') + '</b></div>'
    ) : '<p class="est-empty">' + esc(L(groups ? 'est.empty' : 'est.pickcat')) + '</p>';
    body.innerHTML =
      '<p class="est-sub">' + esc(L('est.sub')) + '</p>' +
      '<h3 class="est-h3">' + esc(L('est.step1')) + '</h3><p class="est-mini">' + esc(L('est.step1.p')) + '</p><div class="est-cats">' + chips + '</div>' +
      (groups ? '<h3 class="est-h3">' + esc(L('est.step2')) + '</h3>' + groups : '') +
      '<div class="est-sum" aria-live="polite"><h3 class="est-h3">' + esc(L('est.sum')) + '</h3>' + sum + '</div>' +
      (t.lines.length ? '<p class="est-note">' + esc(L('est.note')) + '</p>' : '') +
      '<div class="est-actions"><button type="button" class="btn btn-orange est-pdf"' + (t.lines.length ? '' : ' disabled') + '>' + esc(L('est.pdf')) + '</button>' +
      '<button type="button" class="btn btn-wa est-wa"' + (t.lines.length ? '' : ' disabled') + '>' + esc(L('est.wa')) + '</button></div>';
  }

  body.addEventListener('change', function (e) {
    var c = e.target.closest('[data-svc]'); if (!c) return;
    var id = c.getAttribute('data-svc');
    if (c.checked) sel[id] = sel[id] || 1; else delete sel[id];
    render(); var el = body.querySelector('[data-svc="' + id + '"]'); if (el) el.focus({ preventScroll: true });
  });
  body.addEventListener('click', function (e) {
    var cb = e.target.closest('.est-cat');
    if (cb) {
      var cid = cb.getAttribute('data-cat');
      if (cats[cid]) { delete cats[cid]; DATA.services.forEach(function (s) { if (s.cat === cid) delete sel[s.id]; }); if (cid === 'ac') parts = []; }
      else cats[cid] = true;
      render(); var nb = body.querySelector('.est-cat[data-cat="' + cid + '"]'); if (nb) nb.focus({ preventScroll: true }); return;
    }
    var b = e.target.closest('.est-qty button');
    if (b) {
      var w = b.parentNode, id = w.getAttribute('data-id'), d = +b.getAttribute('data-d');
      if (w.getAttribute('data-kind') === 'svc') { sel[id] = Math.max(1, Math.min(20, (sel[id] || 1) + d)); }
      else { var p = parts[+id]; p.q = Math.max(1, Math.min(20, p.q + d)); }
      render(); return;
    }
    var rm = e.target.closest('[data-rm]'); if (rm) { parts.splice(+rm.getAttribute('data-rm'), 1); render(); return; }
    if (e.target.closest('.est-add')) {
      var s = body.querySelector('.est-pick select'), v = s && s.value; if (v === '' || v == null) { if (s) s.focus(); return; }
      var src = DATA.parts[+v], ex = parts.filter(function (x) { return x.id === src.id; })[0];
      if (ex) ex.q = Math.min(20, ex.q + 1); else parts.push({ id: src.id, name: src.name, min: src.min, max: src.max, unit: src.unit, q: 1 });
      render(); return;
    }
    if (e.target.closest('.est-pdf')) { pdf(e.target.closest('.est-pdf')); return; }
    if (e.target.closest('.est-wa')) { wa(); return; }
  });

  function stamp() {
    var d = new Date(), p = function (n) { return (n < 10 ? '0' : '') + n; };
    return { date: p(d.getDate()) + '/' + p(d.getMonth() + 1) + '/' + d.getFullYear(), file: d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()),
             no: 'EST-' + d.getFullYear() + p(d.getMonth() + 1) + p(d.getDate()) + '-' + p(d.getHours()) + p(d.getMinutes()) };
  }

  function wa() {
    var t = totals(), b = DATA.biz;
    var msg = 'Hello BOBBY, I would like a service visit. My online estimate (' + stamp().no + '):\n' +
      t.lines.map(function (l) { return '• ' + l.en + (l.q > 1 ? ' x ' + l.q : '') + ': Rs. ' + inr(l.min * l.q) + (l.max !== l.min ? ' - ' + inr(l.max * l.q) : ''); }).join('\n') +
      '\nEstimated total: Rs. ' + inr(t.lo) + ' - ' + inr(t.hi) + (t.plus ? ' (+ parts if needed)' : '') +
      '\nI understand the final price is confirmed after inspection.\nMy area: ';
    window.open('https://wa.me/' + b.wa + '?text=' + encodeURIComponent(msg), '_blank', 'noopener');
  }

  function loadJsPDF() {
    if (window.jspdf) return Promise.resolve(window.jspdf);
    return new Promise(function (ok, bad) {
      var s = document.createElement('script'); s.src = JSPDF_SRC; s.async = true;
      s.onload = function () { ok(window.jspdf); }; s.onerror = bad; document.head.appendChild(s);
    });
  }
  function imgData(src) {
    return new Promise(function (ok) {
      var i = new Image(); i.crossOrigin = 'anonymous';
      i.onload = function () { try { var c = document.createElement('canvas'); c.width = i.naturalWidth; c.height = i.naturalHeight; c.getContext('2d').drawImage(i, 0, 0); ok(c.toDataURL('image/png')); } catch (e) { ok(null); } };
      i.onerror = function () { ok(null); }; i.src = src;
    });
  }

  /* ---------- PDF: letterhead design ---------- */
  var IC = {
    phone: 'M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z',
    pin: 'M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z',
    web: 'M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zm6.93 6h-2.95c-.32-1.25-.78-2.45-1.38-3.56 1.84.63 3.37 1.91 4.33 3.56zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2H4.26zm.82 2h2.95c.32 1.25.78 2.45 1.38 3.56-1.84-.63-3.37-1.9-4.33-3.56zm2.95-8H5.08c.96-1.66 2.49-2.93 4.33-3.56C8.81 5.55 8.35 6.75 8.03 8zM12 19.96c-.83-1.2-1.48-2.53-1.91-3.96h3.82c-.43 1.43-1.08 2.76-1.91 3.96zM14.34 14H9.66c-.09-.66-.16-1.32-.16-2 0-.68.07-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95c-.96 1.65-2.49 2.93-4.33 3.56zM16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2h-3.38z',
    mail: 'M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z'
  };
  function icon(path, fg, bg) {
    var c = document.createElement('canvas'), n = 96; c.width = c.height = n; var g = c.getContext('2d');
    if (bg) { g.fillStyle = bg; g.beginPath(); if (g.roundRect) g.roundRect(0, 0, n, n, 14); else g.rect(0, 0, n, n); g.fill(); }
    var pad = bg ? 20 : 4, k = (n - pad * 2) / 24; g.translate(pad, pad); g.scale(k, k); g.fillStyle = fg; g.fill(new Path2D(path));
    return c.toDataURL('image/png');
  }
  function goldGrad(g, x0, x1) { var gr = g.createLinearGradient(x0, 0, x1, 0); gr.addColorStop(0, '#9c6b1c'); gr.addColorStop(.35, '#f3cf6a'); gr.addColorStop(.6, '#fff1b3'); gr.addColorStop(.8, '#e0a93a'); gr.addColorStop(1, '#a8741f'); return gr; }
  function blueGrad(g, x0, x1) { var gr = g.createLinearGradient(x0, 0, x1, 0); gr.addColorStop(0, '#1a8ed8'); gr.addColorStop(.5, '#1559a8'); gr.addColorStop(1, '#102c50'); return gr; }
  // header artwork: blue gradient band with gold + orange swooshes (10 px per mm)
  function headArt() {
    var c = document.createElement('canvas'), k = 10; c.width = 210 * k; c.height = 64 * k; var g = c.getContext('2d');
    g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height); g.scale(k, k);
    function edge(o) { g.moveTo(0, 47 + o); g.bezierCurveTo(55, 60 + o, 115, 55 + o, 158, 44 + o); g.bezierCurveTo(185, 37 + o, 200, 39 + o, 210, 47 + o); }
    g.beginPath(); g.moveTo(0, 0); g.lineTo(210, 0); g.lineTo(210, 47); g.bezierCurveTo(200, 39, 185, 37, 158, 44); g.bezierCurveTo(115, 55, 55, 60, 0, 47); g.closePath();
    g.fillStyle = blueGrad(g, 0, 210); g.fill();
    // soft light sheen
    var sh = g.createLinearGradient(0, 0, 0, 50); sh.addColorStop(0, 'rgba(255,255,255,.10)'); sh.addColorStop(1, 'rgba(255,255,255,0)'); g.fillStyle = sh; g.fillRect(0, 0, 210, 50);
    // gold ribbon hugging the wave (thick in the middle, tapered ends)
    g.beginPath(); edge(1.2); g.bezierCurveTo(200, 43.5, 186, 42.5, 158, 50.5); g.bezierCurveTo(112, 63.5, 50, 64, 0, 49.5); g.closePath();
    g.fillStyle = goldGrad(g, 0, 210); g.fill();
    // thin orange swoosh inside the blue band
    g.beginPath(); g.moveTo(0, 40); g.bezierCurveTo(45, 50, 95, 49, 140, 38.5); g.bezierCurveTo(98, 52, 45, 54, 0, 43); g.closePath();
    var og = g.createLinearGradient(0, 0, 140, 0); og.addColorStop(0, '#f2851f'); og.addColorStop(1, 'rgba(242,133,31,0)'); g.fillStyle = og; g.fill();
    return c.toDataURL('image/jpeg', .9);
  }
  // bottom bar: blue segment + gold segment with angled cuts
  function footArt() {
    var c = document.createElement('canvas'), k = 10; c.width = 210 * k; c.height = 7 * k; var g = c.getContext('2d');
    g.fillStyle = '#fff'; g.fillRect(0, 0, c.width, c.height); g.scale(k, k);
    g.beginPath(); g.moveTo(0, 1); g.lineTo(128, 1); g.lineTo(122, 7); g.lineTo(0, 7); g.closePath(); g.fillStyle = blueGrad(g, 0, 128); g.fill();
    g.beginPath(); g.moveTo(133, 1); g.lineTo(210, 1); g.lineTo(210, 7); g.lineTo(127, 7); g.closePath(); g.fillStyle = goldGrad(g, 127, 210); g.fill();
    return c.toDataURL('image/jpeg', .9);
  }

  function pdf(btn) {
    var label = btn.textContent; btn.disabled = true; btn.textContent = L('est.loading');
    Promise.all([loadJsPDF(), imgData(modal.getAttribute('data-logo'))]).then(function (r) {
      var J = r[0].jsPDF, logo = r[1], doc = new J({ unit: 'mm', format: 'a4', compress: true }), t = totals(), st = stamp(), b = DATA.biz;
      var W = 210, M = 16, y, navy = [16, 44, 80], blue = [21, 89, 168], orange = [242, 133, 31], grey = [85, 105, 124], ink = [23, 43, 58];
      var HEAD = headArt(), FOOT = footArt(), gold = '#f3cf6a';
      var I = { pinG: icon(IC.pin, gold), phoneG: icon(IC.phone, gold), mailG: icon(IC.mail, gold),
        phone: icon(IC.phone, '#fff', '#1a8ed8'), web: icon(IC.web, '#fff', '#102c50'), pin: icon(IC.pin, '#fff', '#1a8ed8') };
      var BOTTOM = 258;
      function header(first) {
        if (!first) { doc.addImage(HEAD, 'JPEG', 0, -34, W, 64, 'head'); y = 40; return; }
        doc.addImage(HEAD, 'JPEG', 0, 0, W, 64, 'head');
        if (logo) doc.addImage(logo, 'PNG', 12, 6.5, 32, 32, 'bobbylogo');
        var x = logo ? 50 : M;
        doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'bold'); doc.setFontSize(16.5);
        doc.text('BOBBY AC Repair & Home Appliance Services', x, 15);
        doc.setFont('helvetica', 'italic'); doc.setFontSize(9); doc.setTextColor(243, 207, 106);
        doc.text('Your trusted partner in complete appliance care at your doorstep', x, 20.5);
        doc.setFont('helvetica', 'normal'); doc.setFontSize(8.8); doc.setTextColor(255, 255, 255);
        doc.addImage(I.pinG, 'PNG', x, 23.4, 3.6, 3.6);
        doc.text(doc.splitTextToSize(b.street + ', ' + b.city, W - x - 12), x + 5, 26.2);
        doc.addImage(I.phoneG, 'PNG', x, 33.6, 3.4, 3.4); doc.text('Phone / WhatsApp: ' + b.phone, x + 5, 36.3);
        var ex = x + 5 + doc.getTextWidth('Phone / WhatsApp: ' + b.phone) + 7;
        doc.addImage(I.mailG, 'PNG', ex, 33.7, 3.4, 3.4); doc.text(b.email, ex + 5, 36.3);
        y = 70;
      }
      function footer(n, of) {
        doc.setDrawColor(40, 52, 66); doc.setLineWidth(0.9); doc.line(M, 266, W - M, 266); doc.setLineWidth(0.2);
        var cols = [[I.phone, [b.phone, 'Call / WhatsApp'], 'tel:' + b.phone.replace(/\s/g, '')], [I.web, [b.web, b.email], 'https://' + b.web],
          [I.pin, ['Arundelpet, Narasaraopet', 'Andhra Pradesh 522601'], null]];
        var BW = 34, ws = cols.map(function (c) {
          doc.setFont('helvetica', 'normal'); doc.setFontSize(8.6); var a = doc.getTextWidth(c[1][0]); doc.setFontSize(8); return 10 + Math.max(a, doc.getTextWidth(c[1][1]));
        });
        var gap = (W - M * 2 - BW - ws[0] - ws[1] - ws[2]) / 3, x = M;
        cols.forEach(function (c, i) {
          doc.addImage(c[0], 'PNG', x, 270.5, 8, 8);
          doc.setFont('helvetica', 'normal'); doc.setFontSize(8.6); doc.setTextColor.apply(doc, ink); doc.text(c[1][0], x + 10, 273.8);
          doc.setTextColor.apply(doc, grey); doc.setFontSize(8); doc.text(c[1][1], x + 10, 278);
          if (c[2]) doc.link(x, 270, ws[i], 9, { url: c[2] });
          x += ws[i] + gap;
        });
        x = W - M - BW;
        doc.setFillColor(201, 101, 10); doc.roundedRect(x + 0.4, 271.1, BW, 8, 2, 2, 'F');
        doc.setFillColor(242, 133, 31); doc.roundedRect(x, 270.5, BW, 8, 2, 2, 'F');
        doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'bold'); doc.setFontSize(9.2);
        doc.text('BOOK ONLINE  \u203A', x + BW / 2, 275.6, { align: 'center' });
        doc.link(x, 270.5, BW, 8, { url: b.book });
        if (of > 1) { doc.setFontSize(7.5); doc.setTextColor.apply(doc, grey); doc.text('Page ' + n + ' of ' + of, W / 2, 285.5, { align: 'center' }); }
        doc.addImage(FOOT, 'JPEG', 0, 290, W, 7, 'foot');
      }
      function room(h) { if (y + h > BOTTOM) { doc.addPage(); header(false); } }
      function watermark() {
        if (!logo || !doc.GState) return;
        doc.setGState(new doc.GState({ opacity: 0.06 })); doc.addImage(logo, 'PNG', 140, 150, 58, 58, 'bobbylogo'); doc.setGState(new doc.GState({ opacity: 1 }));
      }
      function inr0(n) { return inr(Math.round(n)); }

      header(true);
      doc.setTextColor.apply(doc, navy); doc.setFont('helvetica', 'bold'); doc.setFontSize(19);
      doc.text('Service Estimate / Quote', W / 2, y, { align: 'center' });
      doc.setDrawColor(242, 133, 31); doc.setLineWidth(0.8); doc.line(W / 2 - 14, y + 3, W / 2 + 14, y + 3); doc.setLineWidth(0.2);
      y += 11; doc.setFont('helvetica', 'normal'); doc.setFontSize(9.8); doc.setTextColor.apply(doc, grey);
      doc.text('Quote Date: ' + st.date, W - M, y, { align: 'right' }); doc.text('Quote No: ' + st.no, W - M, y + 5.5, { align: 'right' });
      y += 11;
      // table
      var cx = [M, 112, 128, 165, W - M];
      function thead() {
        doc.setFillColor(16, 44, 80); doc.rect(M, y, W - M * 2, 11, 'F');
        doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'bold'); doc.setFontSize(9.6);
        doc.text('Service / Part', cx[0] + 3, y + 7); doc.text('Qty', (cx[1] + cx[2]) / 2, y + 7, { align: 'center' });
        doc.text(['Range of Rate', '(Rs.)'], cx[2] + 3, y + 4.6); doc.text(['Amount average', '(Rs.)'], cx[4] - 3, y + 4.6, { align: 'right' });
        y += 11;
      }
      thead(); doc.setFontSize(9.6);
      var lo = 0, av = 0, hi = 0;
      t.lines.forEach(function (l, i) {
        var a = Math.round((l.min + l.max) / 2) * l.q; lo += l.min * l.q; hi += l.max * l.q; av += a;
        var name = l.en + (l.plus ? ' (+ parts if needed)' : '') + (l.part ? ' [spare part]' : '');
        doc.setFont('helvetica', 'normal'); var nl = doc.splitTextToSize(name, cx[1] - cx[0] - 6), h = Math.max(9, nl.length * 4.4 + 4.6);
        if (y + h > BOTTOM) { doc.addPage(); header(false); thead(); doc.setFontSize(9.6); }
        if (i % 2) { doc.setFillColor(244, 248, 252); doc.rect(M, y, W - M * 2, h, 'F'); }
        doc.setFont('helvetica', 'normal'); doc.setTextColor.apply(doc, ink);
        doc.text(nl, cx[0] + 3, y + 5.9); doc.text(String(l.q), (cx[1] + cx[2]) / 2, y + 5.9, { align: 'center' });
        doc.text(l.min === l.max ? inr(l.min) : inr(l.min) + ' - ' + inr(l.max), cx[2] + 3, y + 5.9);
        doc.text(inr0(a), cx[4] - 3, y + 5.9, { align: 'right' });
        doc.setDrawColor(220, 231, 241); doc.line(M, y + h, W - M, y + h); y += h;
      });
      // totals
      room(34); y += 3;
      var rows = [['Estimated Total – Lower side', lo, 0], ['Estimated Total – Average', av, 1], ['Estimated Total – Higher side', hi, 0]];
      rows.forEach(function (rw) {
        if (rw[2]) { doc.setFillColor(16, 44, 80); doc.roundedRect(M, y, W - M * 2, 10, 1.5, 1.5, 'F'); doc.setTextColor(255, 255, 255); }
        else { doc.setFillColor(238, 245, 252); doc.rect(M, y + 0.5, W - M * 2, 9, 'F'); doc.setTextColor.apply(doc, navy); }
        doc.setFont('helvetica', 'bold'); doc.setFontSize(rw[2] ? 11 : 10);
        doc.text(rw[0], M + 4, y + 6.6); doc.text('Rs. ' + inr0(rw[1]), W - M - 4, y + 6.6, { align: 'right' });
        y += 11;
      });
      if (t.plus) { doc.setFont('helvetica', 'bolditalic'); doc.setFontSize(9); doc.setTextColor.apply(doc, grey); doc.text('+ Parts (if needed, charged extra)', M + 4, y + 2); y += 5; }
      doc.setDrawColor(16, 44, 80); doc.setLineWidth(0.6); doc.line(M, y + 1, W - M, y + 1); doc.setLineWidth(0.2);
      // booking
      // thank you + estimate only
      var note = 'Please note: this is only an estimate, not the final price. The final price depends on the technician\'s inspection, the spare parts required and the service needed, and may vary. Spare-part prices are indicative market ranges (reviewed ' + DATA.partsReviewed + '). Work starts only after you approve the final quotation.';
      doc.setFontSize(9.2); var nl = doc.splitTextToSize(note, W - M * 2 - 10), bh = nl.length * 4.5 + 10;
      room(bh + 22); y += 12;
      doc.setFont('helvetica', 'bold'); doc.setFontSize(11); doc.setTextColor.apply(doc, navy);
      doc.text('Thank you for choosing BOBBY AC Repair & Home Appliance Services', W / 2, y, { align: 'center' });
      y += 5;
      doc.setFillColor(255, 246, 236); doc.setDrawColor(246, 217, 184); doc.roundedRect(M, y, W - M * 2, bh, 2, 2, 'FD');
      doc.setFillColor(242, 133, 31); doc.rect(M, y + 1.5, 1.3, bh - 3, 'F');
      doc.setTextColor.apply(doc, orange); doc.setFont('helvetica', 'bold'); doc.setFontSize(9.8); doc.text('ESTIMATE ONLY', M + 5, y + 6);
      doc.setTextColor.apply(doc, ink); doc.setFont('helvetica', 'normal'); doc.setFontSize(9.2); doc.text(nl, M + 5, y + 11);
      y += bh + 6;
      doc.setFont('helvetica', 'italic'); doc.setFontSize(9.5); doc.setTextColor.apply(doc, grey);
      doc.text('Your trusted partner in complete appliance care at your doorstep', W / 2, y, { align: 'center' });
      var n = doc.getNumberOfPages();
      for (var p = 1; p <= n; p++) { doc.setPage(p); footer(p, n); }
      doc.save('BOBBY-Estimate-' + st.file + '.pdf');
    }).catch(function (e) { if (window.console) console.error(e); alertMsg(); }).then(function () { btn.disabled = false; btn.textContent = label; });
  }
  function alertMsg() { var n = modal.querySelector('.est-note'); if (n) n.insertAdjacentHTML('beforebegin', '<p class="est-empty">PDF could not be created. Please try again or use WhatsApp.</p>'); }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-estimate]');
    if (a) { e.preventDefault(); var dm = document.querySelector('.drawer.open,.nav-drawer.open'); open(a.getAttribute('data-estimate')); return; }
    if (e.target.closest && e.target.closest('#estModal [data-close-est]')) close();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && modal.classList.contains('open')) { e.stopPropagation(); close(); } }, true);
  if (location.hash === '#estimate') setTimeout(function () { open(); }, 300);
})();
