/* Split-AC explorer: tabs, component list, previous/next. Works with or without the 3D viewer.
   Talks to the 3D viewer through events: 'a2:stage' {stage} and 'a2:select' {stage, part, index}. */
(function () {
  var sec = document.getElementById('ac-assembly');
  if (!sec) return;
  var tabs = [].slice.call(sec.querySelectorAll('[role="tab"]'));
  var panels = [].slice.call(sec.querySelectorAll('.a2-panel'));
  var count = sec.querySelector('.a2-count'), bar = sec.querySelector('.a2-bar i');
  var prev = sec.querySelector('.a2-prev'), next = sec.querySelector('.a2-next');
  var N = tabs.length, stage = 0, sel = null;

  function emit(name, detail) { sec.dispatchEvent(new CustomEvent(name, { detail: detail })); }
  function items(i) { return [].slice.call(panels[i].querySelectorAll('.a2-item')); }

  function setStage(i, focusTab) {
    i = Math.max(0, Math.min(N - 1, i));
    if (i === stage && panels[i] && !panels[i].hidden) { if (focusTab) tabs[i].focus(); return; }
    if (stage >= 0) select(null, true);
    stage = i;
    tabs.forEach(function (t, k) { var on = k === i; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
    panels.forEach(function (p, k) { p.hidden = k !== i; });
    if (focusTab) tabs[i].focus();
    count.textContent = ('0' + (i + 1)).slice(-2) + ' / ' + ('0' + N).slice(-2);
    bar.style.transform = 'scaleX(' + ((i + 1) / N) + ')';
    prev.disabled = i === 0; next.disabled = i === N - 1;
    var sc = tabs[i].parentNode; if (sc.scrollWidth > sc.clientWidth) sc.scrollTo({ left: tabs[i].offsetLeft - 16, behavior: 'smooth' });
    emit('a2:stage', { stage: i, sid: panels[i].dataset.sid });
  }

  /* select a component in the current stage (index or part name); null clears */
  function select(which, silent) {
    var list = items(stage), idx = -1;
    if (which !== null && which !== undefined) {
      list.forEach(function (li, k) { if (li.dataset.part === which || k === which) idx = k; });
      if (idx === sel) idx = -1;                       /* clicking the open one closes it */
    }
    list.forEach(function (li, k) {
      var on = k === idx, b = li.querySelector('.a2-pick'), d = li.querySelector('.a2-dsc');
      li.classList.toggle('on', on); b.setAttribute('aria-expanded', on ? 'true' : 'false'); d.hidden = !on;
    });
    sel = idx < 0 ? null : idx;
    if (sel !== null) { var li = list[sel]; var box = li.closest('.a2-side');
      if (box && box.scrollHeight > box.clientHeight + 4) { var r = li.getBoundingClientRect(), br = box.getBoundingClientRect(); if (r.top < br.top || r.bottom > br.bottom) box.scrollTo({ top: box.scrollTop + r.top - br.top - 12, behavior: 'smooth' }); } }
    if (!silent) emit('a2:select', { stage: stage, index: sel, part: sel === null ? null : list[sel].dataset.part });
  }

  tabs.forEach(function (t, k) {
    t.addEventListener('click', function () { setStage(k); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (e.key === 'Home') { setStage(0, true); e.preventDefault(); } else if (e.key === 'End') { setStage(N - 1, true); e.preventDefault(); }
      else if (d) { setStage((k + d + N) % N, true); e.preventDefault(); }
    });
  });
  panels.forEach(function (p) {
    p.addEventListener('click', function (e) { var b = e.target.closest('.a2-pick'); if (!b) return; var li = b.closest('.a2-item'); select(items(stage).indexOf(li)); });
  });
  prev.addEventListener('click', function () { setStage(stage - 1); });
  next.addEventListener('click', function () { setStage(stage + 1); });
  sec.addEventListener('keydown', function (e) { if (e.key === 'Escape' && sel !== null) { select(null); } });

  window.A2UI = {
    get stage() { return stage; }, get selected() { return sel; },
    setStage: setStage, select: function (part) { select(part); },
    clear: function () { select(null); }
  };
  stage = -1; setStage(0); stage = 0;
})();
