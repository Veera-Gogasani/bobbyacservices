/* AC spare parts: category filter + search (works without JS: all rows visible) */
(function () {
  var q = document.getElementById('spQ'), n = document.getElementById('spN'), empty = document.getElementById('spEmpty');
  if (!q) return;
  var rows = [].slice.call(document.querySelectorAll('.sp-row')), groups = [].slice.call(document.querySelectorAll('.sp-grp'));
  var chips = [].slice.call(document.querySelectorAll('.sp-chip')), cat = 'all';
  function norm(s) { return (s || '').toLowerCase().replace(/\s+/g, ' ').trim(); }
  function apply() {
    var terms = norm(q.value).split(' ').filter(Boolean), shown = 0, perCat = {};
    rows.forEach(function (r) {
      var ok = (cat === 'all' || r.dataset.cat === cat) && terms.every(function (t) { return r.dataset.q.indexOf(t) > -1; });
      r.hidden = !ok; if (ok) { shown++; perCat[r.dataset.cat] = 1; }
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
  if (location.hash) { var t = document.getElementById(location.hash.slice(1)); if (t && t.classList.contains('sp-row')) t.classList.add('is-target'); }
})();
