#!/usr/bin/env node
'use strict';

/**
 * NEJM trials build pipeline:
 *   node scripts/build_nejm_trials.js split          — TOC → _manifest.json + per-paper paper.md
 *   node scripts/build_nejm_trials.js refs [slug]    — ref-map → _build/<slug>.refs.json
 *   node scripts/build_nejm_trials.js build [slug]   — refs → data/tr-nejm-NNN_*.json
 *   node scripts/build_nejm_trials.js all            — split + refs + build for every paper
 *   node scripts/build_nejm_trials.js index          — refresh data/index.json NEJM entries
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const NEJM_DIR = path.join(ROOT, 'noupload', 'NEJM');
const MONO_MD = path.join(NEJM_DIR, 'nejm.pdf_by_PaddleOCR-VL-1.6.md');
const MANIFEST_PATH = path.join(NEJM_DIR, '_manifest.json');
const BUILD_DIR = path.join(NEJM_DIR, '_build');
const DATA_DIR = path.join(ROOT, 'data');
const INDEX_PATH = path.join(DATA_DIR, 'index.json');

const TOC_META = [
  { slug: 'burch2019', sourceKey: 'burch2019', title: 'Drug Effects on the Thyroid', paperType: 'review', category: 'Endocrinology' },
  { slug: 'nejmoa2502081', sourceKey: 'Coadministered-cagrilintide-and-semaglutide', title: 'REDEFINE 1 — CagriSema in Overweight/Obesity', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejm199309303291401', sourceKey: 'NEJM199309303291401', title: 'DCCT — Intensive Treatment in Type 1 Diabetes', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa011161', sourceKey: 'NEJMoa011161', title: 'RENAAL — Losartan in Diabetic Nephropathy', paperType: 'rct', category: 'Nephrology' },
  { slug: 'nejmoa011303', sourceKey: 'NEJMoa011303', title: 'IDNT — Irbesartan in Diabetic Nephropathy', paperType: 'rct', category: 'Nephrology' },
  { slug: 'nejmoa012512', sourceKey: 'NEJMoa012512', title: 'DPP — Lifestyle vs Metformin for T2DM Prevention', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa0802743', sourceKey: 'NEJMoa0802743', title: 'ACCORD — Intensive Glucose Lowering in T2DM', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa0806470', sourceKey: 'NEJMoa0806470', title: 'ADVANCE — 10-Year Follow-up of Intensive Glucose Control', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa1200225', sourceKey: 'NEJMoa1200225', title: 'STAMPEDE — Bariatric Surgery vs Medical Therapy in T2DM', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa1411892', sourceKey: 'NEJMoa1411892', title: 'SCALE — Liraglutide 3.0 mg for Weight Management', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa1501352', sourceKey: 'NEJMoa1501352', title: 'TECOS — Sitagliptin Cardiovascular Outcomes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa1504720', sourceKey: 'NEJMoa1504720', title: 'EMPA-REG OUTCOME — Empagliflozin in T2DM', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa1600869', sourceKey: 'NEJMoa1600869', title: 'STAMPEDE 5-Year — Bariatric Surgery vs Medical Therapy', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa1603827', sourceKey: 'NEJMoa1603827', title: 'LEADER — Liraglutide Cardiovascular Outcomes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa1607141', sourceKey: 'NEJMoa1607141', title: 'SUSTAIN-6 — Semaglutide Cardiovascular Outcomes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa1611925', sourceKey: 'NEJMoa1611925', title: 'CANVAS — Canagliflozin CV and Renal Events', paperType: 'rct', category: 'Cardiology & Nephrology' },
  { slug: 'nejmoa1804988', sourceKey: 'NEJMoa1804988', title: 'ASCEND — Aspirin Primary Prevention in Diabetes', paperType: 'rct', category: 'Cardiology' },
  { slug: 'nejmoa1812389', sourceKey: 'NEJMoa1812389', title: 'DECLARE-TIMI 58 — Dapagliflozin CV Outcomes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa2004967', sourceKey: 'NEJMoa2004967', title: 'VERTIS CV — Ertugliflozin Cardiovascular Outcomes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa2024816', sourceKey: 'NEJMoa2024816', title: 'DAPA-CKD — Dapagliflozin in Chronic Kidney Disease', paperType: 'rct', category: 'Nephrology' },
  { slug: 'nejmoa2032183', sourceKey: 'NEJMoa2032183', title: 'STEP 1 — Once-Weekly Semaglutide for Obesity', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa2107519', sourceKey: 'NEJMoa2107519', title: 'SURPASS-2 — Tirzepatide vs Semaglutide in T2DM', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa2206038', sourceKey: 'NEJMoa2206038', title: 'SURMOUNT-1 — Tirzepatide for Obesity', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa2208601', sourceKey: 'NEJMoa2208601', title: 'STEP TEENS — Semaglutide in Adolescents with Obesity', paperType: 'rct', category: 'Pediatrics & Endocrinology' },
  { slug: 'nejmoa2301972', sourceKey: 'NEJMoa2301972', title: 'Retatrutide — Triple-Hormone Agonist Phase 2 Obesity', paperType: 'rct', category: 'Endocrinology & Metabolism' },
  { slug: 'nejmoa2306963', sourceKey: 'NEJMoa2306963', title: 'STEP-HFpEF — Semaglutide in HFpEF and Obesity', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'nejmoa2307563', sourceKey: 'NEJMoa2307563', title: 'SELECT — Semaglutide CV Outcomes in Obesity without Diabetes', paperType: 'rct', category: 'Cardiology & Endocrinology' },
  { slug: 'step-9-oa-2024', sourceKey: 'ts-semaglutide-for-OA-STEP-9-2024', title: 'STEP 9 — Semaglutide in Obesity with Knee Osteoarthritis', paperType: 'rct', category: 'Rheumatology & Endocrinology' },
  { slug: 'ukpds-34-wiki', sourceKey: 'UKPDS 34', title: 'UKPDS 34 — Metformin in Overweight T2DM (Wiki Summary)', paperType: 'summary', category: 'Endocrinology & Metabolism' },
];

function trialId(n) { return `tr-nejm-${String(n).padStart(3, '0')}`; }
function fileSlug(slug) { return slug.replace(/[^a-z0-9-]/gi, '_').toLowerCase(); }

function parseTocPages(md) {
  const lines = md.split('\n').slice(0, 35);
  const pages = [];
  for (const line of lines) {
    const m = line.match(/^(.+?)\s+(\d+)\s*$/);
    if (m) pages.push({ raw: m[1].trim(), page: parseInt(m[2], 10) });
  }
  return pages;
}

const PAPER_START_LINES = [
  32, 389, 715, 1060, 1355, 1635, 1930, 2258, 2615, 2895,
  3191, 3436, 3726, 4001, 4293, 4557, 4828, 5105, 5386, 5676,
  5967, 6301, 6591, 6901, 7221, 7538, 7880, 8197, 8391,
];

function splitMonolith() {
  if (!fs.existsSync(MONO_MD)) throw new Error('Missing ' + MONO_MD);
  const md = fs.readFileSync(MONO_MD, 'utf8');
  const lines = md.split('\n');
  const tocPages = parseTocPages(md);

  const manifest = TOC_META.map((meta, i) => ({
    ...meta,
    trialId: trialId(i + 1),
    tocPage: tocPages[i]?.page || null,
    tocRaw: tocPages[i]?.raw || meta.sourceKey,
    dataFile: `${trialId(i + 1)}_${fileSlug(meta.slug)}.json`,
  }));

  for (let i = 0; i < manifest.length; i++) {
    const start = PAPER_START_LINES[i] - 1;
    const end = i + 1 < PAPER_START_LINES.length ? PAPER_START_LINES[i + 1] - 1 : lines.length;
    const paperMd = lines.slice(start, end).join('\n').trim();
    const dir = path.join(NEJM_DIR, manifest[i].slug);
    fs.mkdirSync(dir, { recursive: true });
    fs.writeFileSync(path.join(dir, 'paper.md'), paperMd + '\n');
  }

  fs.writeFileSync(MANIFEST_PATH, JSON.stringify({ generated: new Date().toISOString(), papers: manifest }, null, 2));
  console.log(`Split ${manifest.length} papers → ${NEJM_DIR}`);
  return manifest;
}

function loadManifest() {
  if (!fs.existsSync(MANIFEST_PATH)) return splitMonolith();
  return JSON.parse(fs.readFileSync(MANIFEST_PATH, 'utf8')).papers;
}

const CITE_RE = /\$\s*\^\{?\[?([^}\]]+)\]?\}?\s*\$/g;

function expandRefNums(raw) {
  const nums = new Set();
  for (const part of raw.split(',')) {
    const p = part.trim().replace(/\*$/, '').replace(/†/g, '').replace(/^\[|\]$/g, '');
    const range = p.match(/^(\d+)\s*[-–]\s*(\d+)$/);
    if (range) {
      for (let n = parseInt(range[1], 10); n <= parseInt(range[2], 10); n++) nums.add(n);
    } else {
      const n = parseInt(p, 10);
      if (!isNaN(n)) nums.add(n);
    }
  }
  return [...nums];
}

function cleanText(s) {
  return s
    .replace(CITE_RE, '')
    .replace(/\$\s*\\?[^$]+\$\s*/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function parseBibliography(md) {
  const bib = {};
  const refSection = md.split(/\n##?\s*REFERENCES\b/i).pop();
  const lines = (refSection === md ? md.slice(Math.floor(md.length * 0.75)) : refSection).split('\n');
  let cur = null;
  let buf = [];
  for (const line of lines) {
    const m = line.match(/^(\d+)\.\s+(.+)/);
    if (m) {
      if (cur != null) bib[cur] = buf.join(' ').trim();
      cur = parseInt(m[1], 10);
      buf = [m[2]];
    } else if (cur != null && line.trim() && !line.startsWith('<') && !line.startsWith('N ENGL')) {
      buf.push(line.trim());
    }
  }
  if (cur != null) bib[cur] = buf.join(' ').trim();
  return bib;
}

function collectCitingSpans(md) {
  const refMap = {};
  const paragraphs = md.split(/\n\n+/);
  for (const para of paragraphs) {
    if (para.startsWith('#') || para.includes('<table') || para.includes('<img')) continue;
    const cites = [...para.matchAll(CITE_RE)];
    if (!cites.length) continue;
    const nums = new Set();
    for (const c of cites) expandRefNums(c[1]).forEach(n => nums.add(n));
    const text = cleanText(para);
    if (text.length < 40) continue;
    for (const n of nums) {
      if (!refMap[n]) refMap[n] = [];
      if (!refMap[n].includes(text)) refMap[n].push(text);
    }
  }
  return refMap;
}

function pickBestSpan(spans) {
  const scored = spans.map(s => {
    let score = Math.min(s.length, 400);
    if (/\d+(\.\d+)?%/.test(s)) score += 30;
    if (/hazard ratio|HR|P\s*[<>=]|confidence interval|CI/i.test(s)) score += 25;
    if (/because|due to|mechanism|results from|occurs through/i.test(s)) score += 20;
    if (/randomized|trial|patients|compared/i.test(s)) score += 10;
    return { s, score };
  });
  scored.sort((a, b) => b.score - a.score);
  return scored[0]?.s || spans[0];
}

function suggestQuestionType(text) {
  if (/hazard ratio|HR\s*[,=]|%\s*\(|P\s*[<>=]|odds ratio|relative risk/i.test(text)) return 'shortanswer';
  if (/because|due to|mechanism|results from|occurs through|believed to|explained by/i.test(text)) return 'why';
  if (/how|inhibits|stimulates|converted|transported|administered|randomly assigned/i.test(text)) return 'how';
  if (/more likely|less likely|higher|lower|increased|decreased|versus|compared with/i.test(text)) return 'mcq';
  if (/not significant|no difference|false|did not|never/i.test(text)) return 'true_false';
  return 'why';
}

function extractNumbersForMcq(text) {
  const pcts = [...text.matchAll(/(-?\d+(?:\.\d+)?)\s*%/g)].map(m => m[1] + '%');
  const hrs = [...text.matchAll(/hazard ratio[,\s]+(\d+\.\d+)/gi)].map(m => 'HR ' + m[1]);
  return [...pcts, ...hrs].slice(0, 4);
}

function buildDraftQuestion(refNum, span, bibEntry, paper) {
  const type = suggestQuestionType(span);
  const refStr = `Ref ${refNum}: "${span.slice(0, 160)}${span.length > 160 ? '...' : ''}"${bibEntry ? ' — ' + bibEntry.slice(0, 120) : ''}`;
  const subtopic = paper.title.split('—')[0].trim().slice(0, 40);

  if (type === 'why') {
    const fact = span.replace(/\.$/, '');
    return {
      type: 'why',
      subtopic,
      question: `Why is the following clinically relevant in ${paper.title.split('—')[0].trim()}? Context: ${fact.slice(0, 120)}…`,
      answer: fact,
      reference: refStr,
    };
  }
  if (type === 'how') {
    return {
      type: 'how',
      subtopic,
      question: `How does the process described in reference ${refNum} relate to ${paper.title.split('—')[0].trim()}?`,
      answer: span,
      reference: refStr,
    };
  }
  if (type === 'shortanswer') {
    const qMatch = span.match(/(.{20,120}?)(?:\(|,|;|\.)\s*(?:hazard ratio|HR|P\s*[<>=]|-?\d)/i);
    return {
      type: 'shortanswer',
      subtopic: 'Key Outcome',
      question: `From ${paper.title.split('—')[0].trim()}, what is the key numeric finding cited in reference ${refNum}?`,
      modelAnswer: span.length > 300 ? span.slice(0, 300) : span,
      reference: refStr,
    };
  }
  if (type === 'true_false') {
    const stmt = span.length > 200 ? span.slice(0, 200) : span;
    const neg = /not |no significant|did not|without/i.test(span);
    return {
      type: 'true_false',
      subtopic,
      statement: stmt.endsWith('.') ? stmt : stmt + '.',
      correctAnswer: !neg,
      explanation: span,
      reference: refStr,
    };
  }
  const nums = extractNumbersForMcq(span);
  const correct = nums[0] || 'See reference text';
  const distractors = ['Placebo response only', 'Not reported in this trial', 'Opposite direction of effect', correct];
  const unique = [...new Set(distractors)].slice(0, 4);
  while (unique.length < 4) unique.push('Not applicable');
  const correctIdx = unique.indexOf(correct);
  return {
    type: 'mcq',
    subtopic,
    question: `Which finding is supported by reference ${refNum} in ${paper.title.split('—')[0].trim()}?`,
    options: unique,
    correctOption: correctIdx >= 0 ? correctIdx : 0,
    explanation: span,
    reference: refStr,
  };
}

function extractSection(md, name) {
  const re = new RegExp(`##?\\s*${name}\\s*\\n([\\s\\S]*?)(?=\\n##?\\s|$)`, 'i');
  const m = md.match(re);
  return m ? cleanText(m[1]).slice(0, 2000) : '';
}

function extractTrialSummary(md, paper) {
  const background = extractSection(md, 'BACKGROUND') || extractSection(md, 'INTRODUCTION');
  const methods = extractSection(md, 'METHODS');
  const results = extractSection(md, 'RESULTS');
  const conclusions = extractSection(md, 'CONCLUSIONS') || extractSection(md, 'DISCUSSION');

  const doiM = md.match(/DOI:\s*([\d./\w-]+)/i);
  const nctM = md.match(/NCT\d{5,}/);
  const fundingM = md.match(/Funded by ([^;.]+)/i);

  const headings = {
    background: background.slice(0, 800) || undefined,
    objective: background.slice(0, 400) || undefined,
    design: methods.match(/randomized[^.]{10,200}\./i)?.[0] || methods.slice(0, 300) || undefined,
    population: methods.match(/(?:enrolled|eligible|patients)[^.]{20,300}\./i)?.[0] || undefined,
    intervention: methods.match(/(?:assigned to receive|intervention)[^.]{20,300}\./i)?.[0] || undefined,
    comparator: methods.match(/placebo|usual care|control[^.]{10,200}\./i)?.[0] || undefined,
    followUp: results.match(/median follow-up[^.]+\./i)?.[0] || results.match(/week \d+/i)?.[0] || undefined,
    funding: fundingM ? fundingM[1].trim() : undefined,
    nct: nctM ? nctM[0] : undefined,
    doi: doiM ? doiM[1] : undefined,
  };
  Object.keys(headings).forEach(k => { if (!headings[k]) delete headings[k]; });

  const outcomes = [];
  const primaryM = results.match(/primary[^.]{20,400}\./i);
  if (primaryM) {
    const hrM = results.match(/hazard ratio[,\s]+(\d+\.\d+)[^;]*?(?:95%[^;]+)?/i);
    outcomes.push({
      label: 'Primary outcome (extracted)',
      type: 'primary',
      definition: primaryM[0].slice(0, 200),
      interpretation: conclusions.slice(0, 300) || primaryM[0],
      effect: hrM ? { measure: 'HR', value: parseFloat(hrM[1]), ci95: hrM[0].match(/0\.\d+\s*to\s*0\.\d+/)?.[0] } : undefined,
    });
  }

  const safetyM = results.match(/adverse event[^.]{20,300}\./i);
  const safetyHighlights = safetyM ? [safetyM[0]] : [];

  return {
    headings,
    outcomes,
    safetyHighlights: safetyHighlights.length ? safetyHighlights : undefined,
    conclusion: conclusions.slice(0, 600) || undefined,
    clinicalBottomLine: conclusions.slice(0, 250) || undefined,
  };
}

function extractCriteria(md) {
  const inclusion = [];
  const exclusion = [];
  const pop = extractSection(md, 'STUDY POPULATION') || extractSection(md, 'METHODS');
  const elig = pop.match(/Eligible patients[^.]+\./gi) || [];
  elig.forEach(e => inclusion.push(cleanText(e)));
  const excl = pop.match(/(?:excluded|Patients were excluded)[^.]+\./gi) || [];
  excl.forEach(e => exclusion.push(cleanText(e)));
  return { inclusion: inclusion.slice(0, 8), exclusion: exclusion.slice(0, 8) };
}

function buildRefsForPaper(paper) {
  const paperPath = path.join(NEJM_DIR, paper.slug, 'paper.md');
  if (!fs.existsSync(paperPath)) throw new Error('Missing ' + paperPath);
  const md = fs.readFileSync(paperPath, 'utf8');
  const bib = parseBibliography(md);
  const refMap = collectCitingSpans(md);

  const allNums = new Set([...Object.keys(bib).map(Number), ...Object.keys(refMap).map(Number)]);
  const refs = [...allNums].filter(n => !isNaN(n)).sort((a, b) => a - b).map(refNum => {
    const spans = refMap[refNum] || [];
    const best = spans.length ? pickBestSpan(spans) : (bib[refNum] || `Reference ${refNum}`);
    const draftQuestion = buildDraftQuestion(refNum, best, bib[refNum], paper);
    return {
      refNumber: refNum,
      citingSpans: spans.slice(0, 5),
      bibliographyEntry: bib[refNum] || null,
      suggestedType: draftQuestion.type,
      draftQuestion,
    };
  }).filter(r => r.citingSpans.length || r.bibliographyEntry);

  fs.mkdirSync(BUILD_DIR, { recursive: true });
  const outPath = path.join(BUILD_DIR, `${paper.slug}.refs.json`);
  fs.writeFileSync(outPath, JSON.stringify({ paper: paper.trialId, slug: paper.slug, refs }, null, 2));
  console.log(`  refs: ${paper.slug} → ${refs.length} references`);
  return refs;
}

function buildTrialJson(paper) {
  const refsPath = path.join(BUILD_DIR, `${paper.slug}.refs.json`);
  if (!fs.existsSync(refsPath)) buildRefsForPaper(paper);
  const { refs } = JSON.parse(fs.readFileSync(refsPath, 'utf8'));
  const md = fs.readFileSync(path.join(NEJM_DIR, paper.slug, 'paper.md'), 'utf8');
  const trialSummary = extractTrialSummary(md, paper);
  const { inclusion, exclusion } = extractCriteria(md);
  const bib = parseBibliography(md);

  const items = [];
  let nWhy = 0, nHow = 0, nMcq = 0, nTf = 0, nSa = 0;
  for (const r of refs) {
    const dq = r.draftQuestion;
    const prefix = paper.trialId;
    const idSuffix = `${dq.type === 'shortanswer' ? 'sa' : dq.type === 'true_false' ? 'tf' : dq.type === 'mcq' ? 'q' : dq.type}${r.refNumber}`;
    const item = { id: `${prefix}-${idSuffix}`, referenceNumber: r.refNumber, ...dq };
    if (dq.type === 'why') nWhy++;
    else if (dq.type === 'how') nHow++;
    else if (dq.type === 'mcq') nMcq++;
    else if (dq.type === 'true_false') nTf++;
    else if (dq.type === 'shortanswer') nSa++;
    items.push(item);
  }

  const abstract = extractSection(md, 'ABSTRACT') || extractSection(md, 'CONCLUSIONS');
  const keyTakeaways = [];
  if (trialSummary.clinicalBottomLine) keyTakeaways.push(trialSummary.clinicalBottomLine);
  if (trialSummary.conclusion && trialSummary.conclusion !== trialSummary.clinicalBottomLine) {
    keyTakeaways.push(trialSummary.conclusion.slice(0, 300));
  }
  if (!keyTakeaways.length && abstract) keyTakeaways.push(abstract.slice(0, 300));

  const h1 = md.match(/^# (.+)/m);
  const displayTitle = h1 ? h1[1].replace(/\$\s*\^[^$]+\$\s*/g, '').trim() : paper.title;

  const out = {
    id: paper.trialId,
    trialType: 'clinical_trial',
    subsection: 'nejm',
    sourceKey: paper.sourceKey,
    paperType: paper.paperType,
    title: displayTitle.length > 100 ? paper.title.split('—')[0].trim() : displayTitle,
    subtitle: paper.title,
    section: 'Trials',
    category: paper.category,
    authors: bib[1] ? bib[1].slice(0, 80) : 'NEJM',
    sourceFile: `noupload/NEJM/${paper.slug}/paper.md`,
    bibliography: Object.entries(bib).map(([n, entry]) => ({ number: parseInt(n, 10), entry })),
    trialDesign: {
      fullName: displayTitle,
      overview: abstract.slice(0, 500) || paper.title,
      design: trialSummary.headings?.design,
      population: trialSummary.headings?.population,
      intervention: trialSummary.headings?.intervention,
      comparator: trialSummary.headings?.comparator,
      primaryEndpoint: trialSummary.outcomes?.[0]?.definition,
      duration: trialSummary.headings?.followUp,
    },
    trialSummary,
    inclusionCriteria: inclusion,
    exclusionCriteria: exclusion,
    keyTakeaways: keyTakeaways.slice(0, 5),
    items,
    _buildMeta: { refQuestions: refs.length, types: { why: nWhy, how: nHow, mcq: nMcq, tf: nTf, shortanswer: nSa } },
  };
  delete out._buildMeta;

  const outFile = path.join(DATA_DIR, paper.dataFile);
  fs.writeFileSync(outFile, JSON.stringify(out, null, 2) + '\n');
  console.log(`  built: ${paper.dataFile} (${items.length} ref-questions)`);
  return outFile;
}

function updateIndex(manifest) {
  const index = JSON.parse(fs.readFileSync(INDEX_PATH, 'utf8'));
  index.trials = index.trials || {};
  index.trials.subsections = [
    { id: 'nejm', title: 'NEJM', description: 'Landmark NEJM papers — one reference-linked question per bibliography number' },
    { id: 'general', title: 'General', description: 'Other landmark trials' },
  ];
  index.trials.description = 'Landmark clinical trials with structured summaries, inclusion/exclusion, reference-linked Q&A (MCQ, T/F, why/how, short answer).';

  const general = (index.trials.entries || []).filter(e => e.subsection === 'general' || e.id === 'tr-001');
  if (!general.find(e => e.id === 'tr-001')) {
    general.unshift({
      id: 'tr-001',
      subsection: 'general',
      title: 'UKPDS 33',
      subtitle: 'The UKPDS 33 Landmark Trial — Intensive vs Conventional Glucose Control',
      category: 'Endocrinology & Metabolism',
      file: 'tr-001_ukpds_33.json',
      status: 'ready',
    });
  } else {
    general.forEach(e => { if (e.id === 'tr-001') e.subsection = 'general'; });
  }

  const nejmEntries = manifest.map(p => {
    const built = fs.existsSync(path.join(DATA_DIR, p.dataFile));
    return {
      id: p.trialId,
      subsection: 'nejm',
      sourceKey: p.sourceKey,
      title: p.title.split('—')[0].trim(),
      subtitle: p.title,
      category: p.category,
      paperType: p.paperType,
      file: built ? p.dataFile : null,
      status: built ? 'ready' : 'pending',
    };
  });

  index.trials.entries = [...general, ...nejmEntries];
  fs.writeFileSync(INDEX_PATH, JSON.stringify(index, null, 2) + '\n');
  console.log(`Updated index: ${nejmEntries.filter(e => e.status === 'ready').length}/${nejmEntries.length} NEJM ready`);
}

function main() {
  const cmd = process.argv[2] || 'all';
  const slugArg = process.argv[3];

  if (cmd === 'split') {
    splitMonolith();
    return;
  }

  if (cmd === 'all') splitMonolith();

  let manifest = loadManifest();

  if (cmd === 'index') {
    updateIndex(manifest);
    return;
  }

  const papers = slugArg ? manifest.filter(p => p.slug === slugArg || p.trialId === slugArg) : manifest;
  if (slugArg && !papers.length) {
    console.error('Unknown slug:', slugArg);
    process.exit(1);
  }

  if (cmd === 'refs' || cmd === 'all') {
    console.log('Building reference maps…');
    for (const p of papers) buildRefsForPaper(p);
  }

  if (cmd === 'build' || cmd === 'all') {
    console.log('Building trial JSON…');
    for (const p of papers) buildTrialJson(p);
    updateIndex(manifest);
  }

  if (cmd === 'all') {
    console.log('Done.');
  }
}

main();
