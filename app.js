'use strict';

const AR_OPTIONS = [
  "Both A and R are true, and R is the correct explanation of A",
  "Both A and R are true, but R is NOT the correct explanation of A",
  "A is true, but R is false",
  "A is false, but R is true",
  "Both A and R are false"
];

const app = document.getElementById('app');
const backBtn = document.getElementById('backBtn');
const titleEl = document.getElementById('appTitle');
const themeBtn = document.getElementById('themeBtn');

let CATALOG = null;
let currentChapter = null;
let activeTab = 'notes';

/* ---------- theme ---------- */
(function initTheme(){
  const saved = localStorage.getItem('h22_theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
})();
themeBtn.addEventListener('click', () => {
  const cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', cur);
  localStorage.setItem('h22_theme', cur);
});

backBtn.addEventListener('click', showCatalog);

/* ---------- utils ---------- */
function esc(s){ return String(s==null?'':s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function el(html){ const t=document.createElement('template'); t.innerHTML=html.trim(); return t.content.firstElementChild; }

async function loadJSON(path){
  const r = await fetch(path + '?_=' + Date.now());
  if (!r.ok) throw new Error('Failed to load ' + path);
  return r.json();
}

/* ---------- boot ---------- */
(async function boot(){
  try {
    CATALOG = await loadJSON('data/index.json');
    titleEl.textContent = CATALOG.title || "Harrison's 22e";
    showCatalog();
  } catch (e){
    app.innerHTML = '<div class="empty">Could not load catalog.<br><small>'+esc(e.message)+'</small><br><br>Serve this folder over http (e.g. <code>python3 -m http.server</code>) rather than opening the file directly.</div>';
  }
})();

/* ---------- catalog view ---------- */
async function showCatalog(){
  currentChapter = null;
  backBtn.hidden = true;
  titleEl.textContent = CATALOG.title || "Harrison's 22e";
  window.scrollTo(0,0);

  if (!CATALOG._counts){
    app.innerHTML = '<div class="loading">Loading catalog…</div>';
    CATALOG._counts = {};
    const allChapters = CATALOG.sections.flatMap(s => s.chapters);
    const ready = allChapters.filter(ch => ch.status === 'ready' && ch.file);
    await Promise.all(ready.map(async ch => {
      try {
        const data = await loadJSON('data/' + ch.file);
        const items = data.items || [];
        CATALOG._counts[ch.id] = {
          notes: items.filter(i=>i.type==='note').length,
          mcq: items.filter(i=>i.type==='mcq').length,
          tf: items.filter(i=>i.type==='true_false').length,
          ar: items.filter(i=>i.type==='assertion_reason').length,
          total: items.length
        };
      } catch(e){ CATALOG._counts[ch.id] = null; }
    }));
  }

  const allChapters = CATALOG.sections.flatMap(s => s.chapters);
  const readyChapters = allChapters.filter(ch => ch.status === 'ready' && ch.file);
  const pendingChapters = allChapters.filter(ch => !(ch.status === 'ready' && ch.file));
  const total = allChapters.length;
  const pct = total ? Math.round(100 * readyChapters.length / total) : 0;
  const nextUp = pendingChapters[0];

  const totals = readyChapters.reduce((acc, ch) => {
    const c = CATALOG._counts[ch.id];
    if (c){ acc.notes+=c.notes; acc.mcq+=c.mcq; acc.tf+=c.tf; acc.ar+=c.ar; acc.items+=c.total; }
    return acc;
  }, {notes:0, mcq:0, tf:0, ar:0, items:0});

  let html = '<div class="intro-card">Clinically-focused MCQs (diagnosis, management &amp; treatment), chapter notes, true/false and assertion–reason questions — each linked to the Harrison\'s source text. <b>Endocrinology is generated first.</b></div>';

  html += `<div class="progress-card">
    <div class="progress-stats">
      <div class="stat"><span class="stat-num">${readyChapters.length}</span><span class="stat-label">Ready</span></div>
      <div class="stat"><span class="stat-num">${pendingChapters.length}</span><span class="stat-label">Pending</span></div>
      <div class="stat"><span class="stat-num">${pct}%</span><span class="stat-label">Complete</span></div>
    </div>
    <div class="progress-bar"><div class="progress-fill" style="width:${pct}%"></div></div>
    <div class="progress-totals">${totals.items} items authored — ${totals.notes} notes · ${totals.mcq} MCQs · ${totals.tf} T/F · ${totals.ar} A-R</div>
    ${nextUp ? `<div class="next-up">Next up: <b>Ch ${esc(nextUp.no||'')} — ${esc(nextUp.title)}</b> <span class="next-id">(${esc(nextUp.id)})</span></div>` : '<div class="next-up done">All chapters ready 🎉</div>'}
  </div>`;

  for (const sec of CATALOG.sections){
    html += '<div class="section-head">'+esc(sec.name)+'</div>';
    for (const ch of sec.chapters){
      const ready = ch.status === 'ready' && ch.file;
      const isNext = nextUp && ch.id === nextUp.id;
      const pill = ready ? '<span class="pill ready">ready</span>' : (isNext ? '<span class="pill next">next up</span>' : '<span class="pill pending">pending</span>');
      const c = ready ? CATALOG._counts[ch.id] : null;
      const sub = ready
        ? (c ? `${c.total} items · ${c.notes}N / ${c.mcq}Q / ${c.tf}T / ${c.ar}A` : 'Tap to study')
        : (isNext ? 'Author next — see standing workflow' : 'Awaiting authoring');
      html += `<div class="chap-card ${ready?'':'disabled'}${isNext?' next-card':''}" data-file="${ready?esc(ch.file):''}">
        <div class="chap-no">${esc(ch.no||'')}</div>
        <div class="chap-meta">
          <div class="chap-title">${esc(ch.title)} ${pill}</div>
          <div class="chap-sub">${sub}</div>
        </div>
      </div>`;
    }
  }
  app.innerHTML = html;
  app.querySelectorAll('.chap-card:not(.disabled)').forEach(card => {
    card.addEventListener('click', () => openChapter(card.dataset.file));
  });
}

/* ---------- chapter view ---------- */
async function openChapter(file){
  app.innerHTML = '<div class="loading">Loading chapter…</div>';
  try {
    currentChapter = await loadJSON('data/' + file);
  } catch(e){
    app.innerHTML = '<div class="empty">Could not load chapter.</div>';
    return;
  }
  backBtn.hidden = false;
  activeTab = 'notes';
  renderChapter();
  window.scrollTo(0,0);
}

function counts(){
  const c = currentChapter.items;
  return {
    notes: c.filter(i=>i.type==='note').length,
    mcq: c.filter(i=>i.type==='mcq').length,
    tf: c.filter(i=>i.type==='true_false').length,
    ar: c.filter(i=>i.type==='assertion_reason').length
  };
}

function renderChapter(){
  const ch = currentChapter;
  titleEl.textContent = 'Ch ' + (ch.chapterNo||'') ;
  const n = counts();
  const tab = (id,label,cnt)=>`<button class="tab ${activeTab===id?'active':''}" data-tab="${id}">${label}<br><span class="cnt">${cnt}</span></button>`;

  let html = `<div class="chap-header">
      <h2>${esc(ch.title)}</h2>
      <div class="by">Chapter ${esc(ch.chapterNo||'')} · ${esc(ch.section||'')}${ch.authors?' · '+esc(ch.authors):''}</div>
    </div>
    <div class="tabs">
      ${tab('notes','Notes',n.notes)}
      ${tab('mcq','MCQs',n.mcq)}
      ${tab('tf','True/False',n.tf)}
      ${tab('ar','Assertion–Reason',n.ar)}
    </div>
    <div id="tabBody"></div>`;
  app.innerHTML = html;
  app.querySelectorAll('.tab').forEach(t => t.addEventListener('click', ()=>{ activeTab=t.dataset.tab; renderChapter(); }));
  renderTab();
}

function renderTab(){
  const body = document.getElementById('tabBody');
  const items = currentChapter.items;
  let list, html='';
  if (activeTab==='notes'){
    list = items.filter(i=>i.type==='note');
    html = list.map(renderNote).join('') || emptyMsg();
  } else if (activeTab==='mcq'){
    list = items.filter(i=>i.type==='mcq');
    html = list.map((q,i)=>renderMCQ(q,i+1)).join('') || emptyMsg();
  } else if (activeTab==='tf'){
    list = items.filter(i=>i.type==='true_false');
    html = list.map((q,i)=>renderTF(q,i+1)).join('') || emptyMsg();
  } else {
    list = items.filter(i=>i.type==='assertion_reason');
    html = list.map((q,i)=>renderAR(q,i+1)).join('') || emptyMsg();
  }
  body.innerHTML = html;
  wireQuestions(body);
}

function emptyMsg(){ return '<div class="empty">No items in this section yet.</div>'; }

function refBlock(ref){
  if(!ref) return '';
  return `<div class="ref"><span class="ref-h">Source</span>${esc(ref)}</div>`;
}

function renderNote(nte){
  let kp = '';
  if (nte.keyPoints && nte.keyPoints.length){
    kp = '<div class="kp"><div class="kp-h">Key clinical points</div><ul>'+
      nte.keyPoints.map(k=>'<li>'+esc(k)+'</li>').join('')+'</ul></div>';
  }
  return `<div class="note">
    <div class="sub">${esc(nte.subtopic||'')}</div>
    <h3>${esc(nte.title||'')}</h3>
    <div class="body">${esc(nte.content||'')}</div>
    ${kp}
    ${refBlock(nte.reference)}
  </div>`;
}

function renderMCQ(q, idx){
  const opts = q.options.map((o,i)=>
    `<button class="opt" data-i="${i}"><span class="key">${String.fromCharCode(65+i)}.</span>${esc(o)}</button>`).join('');
  return `<div class="q" data-correct="${q.correctOption}" data-type="mcq">
    <div class="q-top"><span class="q-type">MCQ ${idx}</span><span class="q-sub">${esc(q.subtopic||'')}</span></div>
    <div class="q-stem">${esc(q.question)}</div>
    <div class="opts">${opts}</div>
    <div class="explain"><div class="verdict"></div><div class="exp-text">${esc(q.explanation||'')}</div>${refBlock(q.reference)}</div>
  </div>`;
}

function renderTF(q, idx){
  const correctIdx = q.correctAnswer === true ? 0 : 1;
  return `<div class="q" data-correct="${correctIdx}" data-type="tf">
    <div class="q-top"><span class="q-type">True / False ${idx}</span><span class="q-sub">${esc(q.subtopic||'')}</span></div>
    <div class="q-stem">${esc(q.statement)}</div>
    <div class="tf-row">
      <button class="opt" data-i="0"><span class="key">T</span>True</button>
      <button class="opt" data-i="1"><span class="key">F</span>False</button>
    </div>
    <div class="explain"><div class="verdict"></div><div class="exp-text">${esc(q.explanation||'')}</div>${refBlock(q.reference)}</div>
  </div>`;
}

function renderAR(q, idx){
  const opts = AR_OPTIONS.map((o,i)=>
    `<button class="opt" data-i="${i}"><span class="key">${String.fromCharCode(65+i)}.</span>${esc(o)}</button>`).join('');
  return `<div class="q" data-correct="${q.correctOption}" data-type="ar">
    <div class="q-top"><span class="q-type">Assertion–Reason ${idx}</span><span class="q-sub">${esc(q.subtopic||'')}</span></div>
    <div class="ar-block">
      <div class="ar-line"><b>Assertion (A):</b> ${esc(q.assertion)}</div>
      <div class="ar-line"><b>Reason (R):</b> ${esc(q.reason)}</div>
    </div>
    <div class="opts">${opts}</div>
    <div class="explain"><div class="verdict"></div><div class="exp-text">${esc(q.explanation||'')}</div>${refBlock(q.reference)}</div>
  </div>`;
}

function wireQuestions(scope){
  scope.querySelectorAll('.q').forEach(qEl => {
    const correct = parseInt(qEl.dataset.correct, 10);
    const optEls = qEl.querySelectorAll('.opt');
    optEls.forEach(opt => {
      opt.addEventListener('click', () => {
        if (qEl.dataset.answered) return;
        qEl.dataset.answered = '1';
        const chosen = parseInt(opt.dataset.i, 10);
        optEls.forEach(o => {
          const oi = parseInt(o.dataset.i, 10);
          o.disabled = true;
          if (oi === correct) o.classList.add('correct');
          else if (oi === chosen) o.classList.add('wrong');
        });
        const exp = qEl.querySelector('.explain');
        const verdict = exp.querySelector('.verdict');
        const ok = chosen === correct;
        verdict.textContent = ok ? '✓ Correct' : '✗ Incorrect — see explanation';
        verdict.className = 'verdict ' + (ok ? 'ok' : 'no');
        exp.classList.add('show');
      });
    });
  });
}
