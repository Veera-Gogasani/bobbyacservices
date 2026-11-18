/* AC spare parts: category filter + search (works without JS: all rows visible) */
(function () {
  var q = document.getElementById('spQ'), n = document.getElementById('spN'), empty = document.getElementById('spEmpty');
  if (!q) return;
  var rows = [].slice.call(document.querySelectorAll('.sp-row')), groups = [].slice.call(document.querySelectorAll('.sp-grp'));
  var chips = [].slice.call(document.querySelectorAll('.sp-chip')), cat = 'all';
  function norm(s) { return (s || '').toLowerCase().replace(/\s+/g, ' ').trim(); }
  function has(text, terms) { text = text.toLowerCase(); return terms.every(function (t) { return text.indexOf(t) > -1; }); }
  function apply() {
    var terms = norm(q.value).split(' ').filter(Boolean), shown = 0, perCat = {};
    rows.forEach(function (r) {
      var ok = (cat === 'all' || r.dataset.cat === cat) && has(r.dataset.q, terms);
      r.hidden = !ok;
      if (ok) { shown++; perCat[r.dataset.cat] = 1; }
      var d = r.querySelector('.sp-var');
      if (!d) return;
      var any = false;
      [].forEach.call(d.querySelectorAll('li'), function (li) {
        var hit = ok && terms.length > 0 && has(li.textContent, terms);
        li.classList.toggle('hit', hit);
        if (hit) any = true;
      });
      d.open = any;
    });
    groups.forEach(function (g) { g.hidden = !perCat[g.dataset.cat]; });
    n.textContent = shown; empty.hidden = shown > 0;
  }
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      cat = c.dataset.cat;
      chips.forEach(function (x) { var on = x === c; x.classList.toggle('is-on', on); x.setAttribute('aria-pressed', on ? 'true' : 'false'); });
      apply();
    });
  });
  q.addEventListener('input', apply);
})();
