#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const SRC = '/Users/dr.ajayshukla/Downloads/semaglutide_deconstruction_50.md';
const OUT = path.join(__dirname, '../data/ht-001_semaglutide.json');

const md = fs.readFileSync(SRC, 'utf8');
const data = JSON.parse(fs.readFileSync(OUT, 'utf8'));

const CATS = [
  ['Category 1: The Axiomatic Questions \\(The Root\\)', 'Axiomatic — The Root'],
  ['Category 2: The Glassbox Questions \\(The Mechanism\\)', 'Glassbox — The Mechanism'],
  ['Category 3: The Invariant Questions \\(The Constants\\)', 'Invariant — The Constants'],
  ['Category 4: The Falsifiability Questions \\(The Breakpoint\\)', 'Falsifiability — The Breakpoint'],
  ['Category 5: The Counterfactual Questions \\(The Inversion\\)', 'Counterfactual — The Inversion'],
  ['Category 6: The Second-Order Questions \\(The Cascade\\)', 'Second-Order — The Cascade'],
  ['Category 7: The Boundary Questions \\(The Extremes\\)', 'Boundary — The Extremes'],
  ['Category 8: The Lineage Questions \\(The Origin\\)', 'Lineage — The Origin'],
  ['Category 9: The Equilibrium Questions \\(The End-State\\)', 'Equilibrium — The End-State'],
  ['Category 10: The Discordance Questions \\(The Anomalies\\)', 'Discordance — The Anomalies']
];

function parseQuestions() {
  const items = [];
  for (let c = 0; c < CATS.length; c++) {
    const [catRe, subtopic] = CATS[c];
    const startRe = new RegExp(`## ${catRe}`);
    const endRe = c < CATS.length - 1
      ? new RegExp(`## ${CATS[c + 1][0]}`)
      : null;

    const startIdx = md.search(startRe);
    if (startIdx < 0) continue;
    const endIdx = endRe ? md.search(endRe) : md.length;
    const section = md.slice(startIdx, endIdx);

    const qRe = /### (\d+)\. ([^\n]+)\n\* \*\*Deconstruction:\*\* ([\s\S]*?)\n\* \*\*Published Evidence & Certainty:\*\* ([^\n]+(?:\n(?!\* \*\*)[^\n]+)*)\n\* \*\*Reference:\*\* ([^\n]+)/g;
    let m;
    while ((m = qRe.exec(section)) !== null) {
      const num = parseInt(m[1], 10);
      const title = m[2].trim();
      let decon = m[3].trim();
      const evidence = m[4].trim().replace(/\s+/g, ' ');
      const ref = m[5].trim();

      // Normalize numbered list deconstructions into newline-separated steps
      decon = decon.replace(/\n\s*(\d+)\.\s+/g, '\n$1. ');

      const certaintyMatch = evidence.match(/^(Highly certain|Limited information|Moderately certain|Undeniably true|Biophysically absolute|High biological certainty[^.]*|Falsified[^.]*|Limited direct[^.]*)/i);
      const certainty = certaintyMatch ? certaintyMatch[1].replace(/\.$/, '') : 'See evidence';

      const keyPoints = [];
      const sentences = (decon + ' ' + evidence).split(/(?<=[.!?])\s+/).filter(s => s.length > 25);
      for (const s of sentences.slice(0, 4)) keyPoints.push(s.trim());

      const quote = (decon.split('\n')[0] || evidence).slice(0, 120);
      items.push({
        num,
        subtopic,
        title,
        content: `Deconstruction:\n${decon}\n\nPublished Evidence & Certainty: ${evidence}\n\nCertainty: ${certainty}`,
        keyPoints: keyPoints.length ? keyPoints : [decon.slice(0, 100)],
        reference: `DECON 50 Q${num} [${certainty}]: "${quote}${quote.length >= 120 ? '...' : ''}" (${ref})`
      });
    }
  }
  return items.sort((a, b) => a.num - b.num);
}

const parsed = parseQuestions();
if (parsed.length !== 50) {
  console.error('Expected 50 questions, parsed', parsed.length);
  process.exit(1);
}

const notes = parsed.map((d, i) => ({
  id: `ht-001-n${131 + i}`,
  type: 'note',
  subtopic: d.subtopic,
  title: d.title,
  content: d.content,
  keyPoints: d.keyPoints,
  reference: d.reference
}));

const mcqs = [
  { id: 'ht-001-q33', subtopic: 'Axiomatic — Root', question: 'SELECT trial data most directly falsifies which axiom about semaglutide cardiovascular benefit?', options: ['CV benefit requires HbA1c reduction below 7%', 'CV benefit requires weight loss above 15%', 'CV benefit is solely downstream of glycemic lowering', 'CV benefit requires concurrent SGLT2 inhibitor therapy'], correctOption: 2, explanation: 'SELECT enrolled non-diabetic patients with normal/prediabetic HbA1c who still had 20% MACE reduction, proving benefit is not solely from glucose lowering.', reference: 'DECON 50 Q3: "overweight/obese patients without type 2 diabetes... experienced a 20% reduction in MACE" (Lincoff AM, SELECT, NEJM 2023)' },
  { id: 'ht-001-q34', subtopic: 'Glassbox — Mechanism', question: 'The first step in oral semaglutide gastric absorption after tablet dissolution is:', options: ['Paracellular transport through opened tight junctions in the duodenum', 'SNAC creating a localized high-concentration microenvironment neutralizing gastric acid', 'Hepatic first-pass metabolism in portal circulation', 'Active transport via intestinal PepT1 transporters'], correctOption: 1, explanation: 'Tablet dissolves in gastric mucus; SNAC releases and creates local pH ~7-8, inactivating pepsin and enabling transcellular absorption.', reference: 'DECON 50 Q6: "SNAC molecules release and create a localized microenvironment... elevating the local pH to ~7-8" (Buckley ST, Sci Transl Med 2018)' },
  { id: 'ht-001-q35', subtopic: 'Invariant — Constants', question: 'What primarily drives GI intolerance when initiating semaglutide — absolute plasma concentration or rate of concentration change?', options: ['Steady-state Cmax only', 'Rate of change of plasma concentration (dC/dt), not absolute C', 'Albumin binding saturation', 'Renal clearance variability'], correctOption: 1, explanation: 'Rapid exposure increases cause nausea/vomiting; slow 4-week titration allows CNS adaptation to high steady-state levels.', reference: 'DECON 50 Q13: "The rate of change of plasma concentration (dC/dt), rather than the absolute concentration (C) itself" (Bækdal TA, Clin Pharmacokinet 2018)' },
  { id: 'ht-001-q36', subtopic: 'Falsifiability — Breakpoint', question: 'Post-hoc SUSTAIN 6 and SELECT analyses falsified which model of semaglutide cardioprotection?', options: ['Weight-loss-exclusive model — MACE benefit consistent even in patients losing <5% body weight', 'Direct vascular inflammation model', 'SGLT2-dependent natriuresis model', 'Beta-cell regeneration model'], correctOption: 0, explanation: 'MACE hazard ratio reduction was consistent across weight-loss subgroups including those with 0-5% loss, falsifying weight-loss-exclusive cardioprotection.', reference: 'DECON 50 Q16: "even patients who lost <5% or 0% of their body weight experienced significant cardiovascular protection" (Lincoff AM, SELECT)' },
  { id: 'ht-001-q37', subtopic: 'Counterfactual — Inversion', question: 'If the C18 fatty diacid chain is removed from semaglutide, expected half-life change is:', options: ['Unchanged at 168 hours', 'Reduced from 168 hours to less than 5 hours', 'Extended to 14 days via hepatic storage', 'Eliminated only in renal impairment'], correctOption: 1, explanation: 'Without albumin-binding C18 diacid, rapid glomerular filtration and enzymatic degradation reduce half-life to <5 hours.', reference: 'DECON 50 Q24: "reducing its half-life from 168 hours to less than 5 hours" (Sorli C, SUSTAIN 1)' },
  { id: 'ht-001-q38', subtopic: 'Discordance — Anomalies', question: 'The diabetic retinopathy paradox after starting semaglutide is best explained by:', options: ['Direct GLP-1R retinal toxicity', 'Rapid HbA1c drop causing acute metabolic shock and transient VEGF spike in fragile retinal vessels', 'SNAC accumulation in retinal pigment epithelium', 'Albumin-bound drug depositing in choroidal vessels'], correctOption: 1, explanation: 'Rapid glucose clearing in severe pre-existing retinopathy causes localized hypoxia response with transient VEGF elevation worsening edema before stabilization.', reference: 'DECON 50 Q47: "rapid drop in blood glucose... triggers a transient spike in intra-retinal VEGF expression" (Bain SC, Cardiovasc Diabetol 2019)' },
  { id: 'ht-001-q39', subtopic: 'Equilibrium — End-State', question: 'STEP trial weight plateau at weeks 60-68 represents:', options: ['Complete hypothalamic GLP-1R desensitization', 'Thermodynamic equilibrium where reduced caloric intake matches lowered TDEE/RMR', 'Development of neutralizing antibodies', 'Irreversible beta-cell exhaustion'], correctOption: 1, explanation: 'As mass decreases, TDEE and RMR drop while ghrelin rises; plateau occurs when suppressed intake equals new lower expenditure.', reference: 'DECON 50 Q41: "reduced caloric intake matches the body\'s new, lower TDEE, establishing a new energy equilibrium" (Wilding JPH, STEP 1)' },
  { id: 'ht-001-q40', subtopic: 'Lineage — Origin', question: 'Exendin-4 from Gila monster venom was critical to semaglutide lineage because it proved:', options: ['Oral peptide delivery was feasible', 'DPP-4-resistant GLP-1R agonism could be clinically viable (glycine at position 2)', 'Weekly albumin binding was possible', 'CNS penetration required for glycemic control'], correctOption: 1, explanation: 'Exendin-4 shared 53% homology with human GLP-1 but resisted DPP-4 via glycine at position 2, proving long-acting incretin concept.', reference: 'DECON 50 Q36: "completely resistant to DPP-4 because of a glycine substitution at position 2" (Eng J, J Biol Chem 1992)' }
].map(q => ({ ...q, type: 'mcq' }));

const trueFalse = [
  { id: 'ht-001-tf19', subtopic: 'Axiomatic — Root', statement: 'Semaglutide perfectly mimics native GLP-1 regarding half-life, tissue distribution, and receptor cycling dynamics.', correctAnswer: false, explanation: 'Native GLP-1 is pulsatile (2-3 min clearance); semaglutide provides continuous 168-hour receptor occupancy altering recycling dynamics.', reference: 'DECON 50 Q5: "Semaglutide provides continuous, high-concentration receptor occupancy for 168 hours per dose" (Meier JJ, Nat Rev Endocrinol 2012)' },
  { id: 'ht-001-tf20', subtopic: 'Invariant — Constants', statement: 'Gastric emptying delay remains permanently reduced throughout chronic semaglutide therapy.', correctAnswer: false, explanation: 'Gastric emptying delay undergoes tachyphylaxis by weeks 12-20; central appetite suppression remains active.', reference: 'DECON 50 Q12: "gastric motility rate returns toward baseline due to rapid tachyphylaxis" (Hjerpsted JB, Diabetes Obes Metab 2018)' },
  { id: 'ht-001-tf21', subtopic: 'Falsifiability — Breakpoint', statement: 'Human withdrawal studies falsify the hypothesis that semaglutide structurally reverses beta-cell apoptosis.', correctAnswer: true, explanation: 'After washout, insulin secretory capacity and HbA1c return to baseline within 4-12 weeks — benefit is functional, not structural.', reference: 'DECON 50 Q18: "insulin secretory capacity and HbA1c levels return to baseline within 4 to 12 weeks" (Meier JJ, Nat Rev Endocrinol 2012)' },
  { id: 'ht-001-tf22', subtopic: 'Counterfactual — Inversion', statement: 'Oral semaglutide without SNAC co-formulation achieves near-zero systemic bioavailability.', correctAnswer: true, explanation: 'Gastric pepsin hydrolyzes the peptide at pH 1.5-2.0; remaining peptide cannot cross gastric mucosa lipid bilayers.', reference: 'DECON 50 Q22: "resulting in zero systemic bioavailability" (Buckley ST, Sci Transl Med 2018)' },
  { id: 'ht-001-tf23', subtopic: 'Boundary — Extremes', statement: 'Oral semaglutide pharmacokinetics remain stable in severe renal failure including hemodialysis patients.', correctAnswer: true, explanation: 'PK studies show AUC/Cmax comparable to healthy controls; renal filtration is not primary clearance pathway.', reference: 'DECON 50 Q32: "systemic exposure (AUC and Cmax) remains highly stable and comparable to healthy controls" (Bækdal TA, J Clin Pharmacol 2018)' },
  { id: 'ht-001-tf24', subtopic: 'Discordance — Anomalies', statement: 'Semaglutide causes lean mass loss (~40% of total weight) partly due to profound satiety driving protein under-nutrition.', correctAnswer: true, explanation: 'STEP 1 DXA showed 40% lean mass loss; severe central satiety may reduce protein intake below essential amino acid needs.', reference: 'DECON 50 Q50: "profound, rapid central satiety that patients frequently experience severe, unmonitored protein under-nutrition" (Wilding JPH, STEP 1 DXA)' }
].map(q => ({ ...q, type: 'true_false' }));

const ar = [
  { id: 'ht-001-ar19', subtopic: 'Axiomatic — Root', assertion: 'Semaglutide cardiovascular benefit is not solely driven by HbA1c reduction.', reason: 'SELECT showed 20% MACE reduction in patients without type 2 diabetes.', correctOption: 0, explanation: 'Both true; SELECT in non-diabetic cohort directly proves CV benefit independent of glycemic lowering magnitude.', reference: 'DECON 50 Q3: "cardioprotection is driven by systemic anti-inflammatory, anti-atherosclerotic pathways" (Lincoff AM, SELECT)' },
  { id: 'ht-001-ar20', subtopic: 'Invariant — Constants', assertion: 'Lean mass comprises ~40% of weight lost on semaglutide 2.4 mg.', reason: 'This is an obligate consequence of rapid negative energy balance in any weight-loss modality.', correctOption: 0, explanation: 'Both true; STEP 1 DXA confirmed 40% lean loss as biological invariant of rapid caloric deficit.', reference: 'DECON 50 Q14: "lean mass loss typically comprises 20% to 40% of total weight lost" (Wilding JPH, STEP 1 DXA)' },
  { id: 'ht-001-ar21', subtopic: 'Falsifiability — Breakpoint', assertion: 'CNS GLP-1R activation is mandatory for semaglutide-induced weight loss.', reason: 'Rodent CNS GLP-1R knockout abolishes semaglutide food intake reduction.', correctOption: 0, explanation: 'Both true; Cre-lox brainstem/hypothalamus knockout studies confirm brain dependency.', reference: 'DECON 50 Q17: "peripheral administration of semaglutide fails to reduce food intake or induce weight loss" (Sisley S, J Clin Invest 2014)' },
  { id: 'ht-001-ar22', subtopic: 'Equilibrium — End-State', assertion: 'Gastric motility returns to baseline during chronic semaglutide therapy.', reason: 'Gastric emptying delay undergoes full tachyphylaxis while central metabolic benefits persist.', correctOption: 0, explanation: 'Both true; explains diminishing early nausea while weight/glycemic benefits continue.', reference: 'DECON 50 Q43: "gastric transit returns back to its baseline physiological rate" (Hjerpsted JB, Diabetes Obes Metab 2018)' },
  { id: 'ht-001-ar23', subtopic: 'Discordance — Anomalies', assertion: 'Serum lipase elevations on semaglutide are usually clinically benign.', reason: 'GLP-1R activation causes pancreatic exocrine enzyme leakage without zymogen auto-activation or necrosis.', correctOption: 0, explanation: 'Both true; explains disconnect between elevated enzymes and <0.1% pancreatitis incidence.', reference: 'DECON 50 Q49: "benign, functional stimulation of pancreatic exocrine cells, causing them to leak small amounts of enzymes" (Marso SP, SUSTAIN 6)' },
  { id: 'ht-001-ar24', subtopic: 'Lineage — Origin', assertion: 'Semaglutide\'s weekly dosing required engineering beyond liraglutide\'s C16 fatty acid design.', reason: 'Aib-8 substitution, Arg-34, and C18 diacid with hydrophilic spacer increased albumin binding five-fold.', correctOption: 0, explanation: 'Both true; molecular lineage from liraglutide (13h) to semaglutide (168h) required these specific modifications.', reference: 'DECON 50 Q37: "C18 diacid increased albumin binding affinity by five-fold" (Sorli C, SUSTAIN 1; Lau J, J Med Chem 2015)' }
].map(q => ({ ...q, type: 'assertion_reason' }));

// Remove prior 50-Q batch if re-running (idempotent)
const filtered = data.items.filter(it => {
  const n = parseInt((it.id.match(/-n(\d+)$/) || [])[1], 10);
  if (n >= 131) return false;
  if (it.id.match(/-q(3[3-9]|40)$/)) return false;
  if (it.id.match(/-tf(19|2[0-4])$/)) return false;
  if (it.id.match(/-ar(19|2[0-4])$/)) return false;
  return true;
});

data.items = [...filtered, ...notes, ...mcqs, ...trueFalse, ...ar];
const sources = new Set((data.sourceFile || '').split(/;\s*/).filter(Boolean));
sources.add('semaglutide_pubmed_qa_100.md');
sources.add('semaglutide_axiomatic_deconstruction.md');
sources.add('semaglutide_deconstruction_50.md');
data.sourceFile = [...sources].join('; ');
data.subtitle = 'GLP-1 Receptor Agonist — PubMed Trials & Structural Deconstruction (150 Q)';

fs.writeFileSync(OUT, JSON.stringify(data, null, 2) + '\n');

const counts = {};
data.items.forEach(it => { counts[it.type] = (counts[it.type] || 0) + 1; });
console.log('Parsed questions:', parsed.length);
console.log('Updated:', OUT);
console.log('Counts:', counts, 'total:', data.items.length);
