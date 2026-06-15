#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const SRC = '/Users/dr.ajayshukla/Downloads/semaglutide_pubmed_qa_100 (2).md';
const OUT = path.join(__dirname, '../data/ht-001_semaglutide.json');

const md = fs.readFileSync(SRC, 'utf8');

const SUBTOPICS = {
  why: {
    1: 'Pharmacokinetics & Structure', 2: 'Cardiovascular Outcomes', 3: 'SELECT Trial Design',
    4: 'Renal Protection — FLOW', 5: 'Oral Formulation — SNAC', 6: 'Oral Dosing Requirements',
    7: 'Diabetic Retinopathy', 8: 'Dose Selection — Weight vs Diabetes', 9: 'Appetite & Reward',
    10: 'Obesity as Chronic Disease', 11: 'HFpEF & Obesity', 12: 'MASH/NASH',
    13: 'Regulatory — CV Safety', 14: 'Titration & GI Tolerance', 15: 'Trial Comparators',
    16: 'Semaglutide vs Liraglutide', 17: 'Oral Peptide Breakthrough', 18: 'Renal Mechanisms',
    19: 'Renal Impairment Dosing', 20: 'Visceral Fat', 21: 'Alzheimer\'s Disease',
    22: 'Hypoglycemia Risk', 23: 'Flexible Oral Dosing', 24: 'Lipid Effects',
    25: 'Pediatric Obesity', 26: 'Gastric Emptying', 27: 'SGLT2 Comparators',
    28: 'Elderly Safety', 29: 'Hepatic Clearance', 30: 'Hepatic Steatosis',
    31: 'SOUL Trial', 32: 'Nausea Mechanism', 33: 'Long-term Weight Maintenance',
    34: 'Alcohol Use Disorder', 35: 'Insulin Add-on', 36: 'Blood Pressure',
    37: 'East Asian Populations', 38: 'Glucagon Suppression', 39: 'Insulin Comparators',
    40: 'Central Nervous System', 41: 'Inflammation', 42: 'SGLT2 Oral Comparators',
    43: 'Behavioral Therapy', 44: 'Thyroid Safety', 45: 'Postprandial Lipemia',
    46: 'ESSENCE Trial', 47: 'Compliance', 48: 'Glomerular Protection',
    49: 'DPP-4 Comparators', 50: 'Sleep Apnea'
  },
  how: {
    51: 'Molecular Structure', 52: 'Insulin Secretion', 53: 'SNAC Absorption',
    54: 'STEP 1 Weight Loss', 55: 'SELECT MACE Mechanism', 56: 'FLOW Kidney Outcomes',
    57: 'Metabolism & Elimination', 58: 'PIONEER 4 vs Liraglutide', 59: 'Blood-Brain Barrier',
    60: 'Hypothalamic Appetite', 61: 'Gastric Emptying Tachyphylaxis', 62: 'SUSTAIN 7 vs Dulaglutide',
    63: 'STEP 3 with IBT', 64: 'STEP-HFpEF Symptoms', 65: 'Body Composition',
    66: 'STEP 2 Diabetes Effect', 67: 'MASH Resolution', 68: 'PIONEER 5 Renal Impairment',
    69: 'SUSTAIN 6 MACE', 70: 'PIONEER 2 vs Empagliflozin', 71: 'STEP 4 Withdrawal',
    72: 'Water Volume & Absorption', 73: 'Postprandial Glucose', 74: 'SELECT Non-Diabetic CV',
    75: 'STEP-TEENS Pediatrics', 76: 'Oral Dose-Response', 77: 'Gallbladder Disease',
    78: 'Oral Bioavailability', 79: 'Arterial Stiffness', 80: 'SUSTAIN 5 Basal Insulin',
    81: 'Endothelial Adhesion', 82: 'Quality of Life', 83: 'Pancreatitis Risk',
    84: 'PIONEER 3 vs Sitagliptin', 85: 'Beta-Cell Function', 86: 'PIONEER 1 Monotherapy',
    87: 'Nephropathy Prevention', 88: 'Liver Fat MRI', 89: 'Glycemic Variability',
    90: 'East Asian Safety', 91: 'Cardiac Workload', 92: 'Post-Dose Fasting',
    93: 'Epicardial Adipose Tissue', 94: 'SUSTAIN 8 vs Canagliflozin', 95: 'FLOW Composite Renal',
    96: 'Leptin & Adiponectin', 97: 'Injection Sites', 98: 'ESSENCE Fibrosis Regression',
    99: 'Oral Compliance by Dose', 100: 'PIONEER 10 Japan'
  }
};

function parseQA(section, prefix) {
  const re = new RegExp(
    `### (\\d+)\\. (${prefix === 'why' ? 'Why' : 'How'}) ([^\\n]+)\\n\\* \\*\\*Answer:\\*\\* ([^\\n]+)\\n\\* \\*\\*Reference Hint:\\*\\* ([^\\n]+)`,
    'g'
  );
  const notes = [];
  let m;
  while ((m = re.exec(section)) !== null) {
    const num = parseInt(m[1], 10);
    const question = m[2] + ' ' + m[3].trim();
    const answer = m[4].trim();
    const refHint = m[5].trim();
    const subtopicMap = prefix === 'why' ? SUBTOPICS.why : SUBTOPICS.how;
    notes.push({
      id: `ht-001-n${num}`,
      type: 'note',
      subtopic: subtopicMap[num] || 'General',
      title: question,
      content: answer,
      keyPoints: answer.split(/(?<=[.!?])\s+/).filter(s => s.length > 20).slice(0, 4),
      reference: `${prefix === 'why' ? 'WHY' : 'HOW'} Q${num}: "${answer.slice(0, 120)}${answer.length > 120 ? '...' : ''}" (${refHint})`
    });
  }
  return notes;
}

const part2 = md.split('## Part II:')[1].split('## Part III:')[0];
const part3 = md.split('## Part III:')[1];
const whyNotes = parseQA(part2, 'why');
const howNotes = parseQA(part3, 'how');
const notes = [...whyNotes, ...howNotes];

// Ensure keyPoints has at least 2 items
notes.forEach(n => {
  if (!n.keyPoints || n.keyPoints.length < 2) {
    n.keyPoints = [n.content.slice(0, 100)];
  }
});

const mcqs = [
  { id: 'ht-001-q1', subtopic: 'Pharmacokinetics', question: 'A 58-year-old man with type 2 diabetes asks why semaglutide is injected only once weekly while native GLP-1 lasts minutes. Which structural feature best explains the extended half-life?', options: ['Substitution of alanine with Aib at position 8 only', 'C18 fatty diacid chain attached to lysine-26 via a spacer enabling albumin binding', 'Oral co-formulation with SNAC in the stomach', 'DPP-4 inhibitor co-administration'], correctOption: 1, explanation: 'Semaglutide has three key modifications including a C18 fatty diacid on lysine-26 that promotes tight reversible albumin binding, protecting the peptide from renal clearance and DPP-4 degradation and extending half-life to ~1 week.', reference: 'HOW Q51: "substitution of alanine with alpha-aminoisobutyric acid (Aib) at position 8... attachment of a C18 fatty diacid chain to lysine-26 via a spacer (promoting albumin binding)" (Paper 1, Paper 6)' },
  { id: 'ht-001-q2', subtopic: 'Cardiovascular Outcomes', question: 'In SUSTAIN 6, semaglutide 1.0 mg weekly in type 2 diabetes with high cardiovascular risk reduced the primary 3-point MACE endpoint by what relative amount over 104 weeks?', options: ['12%', '20%', '26%', '35%'], correctOption: 2, explanation: 'SUSTAIN 6 demonstrated a 26% relative risk reduction in the composite of cardiovascular death, nonfatal MI, and nonfatal stroke.', reference: 'HOW Q69: "demonstrated a highly significant 26% relative risk reduction in the primary composite 3-point MACE endpoint" (Paper 6, SUSTAIN 6)' },
  { id: 'ht-001-q3', subtopic: 'Weight Management', question: 'In STEP 1, adults with overweight or obesity receiving semaglutide 2.4 mg weekly lost what mean percentage of baseline body weight at 68 weeks?', options: ['9.6%', '12.4%', '14.9%', '16.0%'], correctOption: 2, explanation: 'STEP 1 showed mean weight loss of 14.9% with semaglutide 2.4 mg vs 2.4% with placebo over 68 weeks.', reference: 'HOW Q54: "lost an average of 14.9% of their baseline body weight over 68 weeks, compared to just 2.4% in the placebo group" (Paper 22, STEP 1)' },
  { id: 'ht-001-q4', subtopic: 'Oral Formulation', question: 'A patient is started on oral semaglutide (Rybelsus). Which administration instruction is essential to maintain bioavailability?', options: ['Take with a full glass of water and breakfast', 'Take after overnight fast with ≤120 mL plain water; fast ≥30 min post-dose', 'Take at bedtime with a high-fat snack', 'Crush tablet and mix with applesauce if swallowing difficulty'], correctOption: 1, explanation: 'Food, beverages, or excess water dilute SNAC in the stomach, preventing local pH elevation and drastically reducing oral bioavailability. Fasting before and after dosing is required.', reference: 'WHY Q6: "Any food, beverage, or excess water in the stomach dilutes the SNAC concentration, preventing the required local pH elevation" (Paper 38)' },
  { id: 'ht-001-q5', subtopic: 'Renal Protection', question: 'The FLOW trial in type 2 diabetes with CKD was stopped early because interim analysis showed semaglutide met prespecified efficacy criteria for which outcome?', options: ['Resolution of MASH with fibrosis regression', 'Slowing CKD progression and reducing renal/cardiovascular mortality', 'Primary prevention of type 2 diabetes', 'Reversal of diabetic retinopathy'], correctOption: 1, explanation: 'The independent data monitoring committee recommended stopping FLOW early due to overwhelming kidney-protective efficacy on CKD progression and renal/cardiovascular mortality.', reference: 'WHY Q4: "semaglutide reached pre-specified efficacy criteria for slowing chronic kidney disease progression and reducing renal/cardiovascular mortality" (Paper 34, FLOW)' },
  { id: 'ht-001-q6', subtopic: 'SELECT Trial', question: 'SELECT enrolled adults with obesity but WITHOUT type 2 diabetes to test whether semaglutide 2.4 mg reduces MACE primarily through which mechanisms?', options: ['Direct insulin secretion independent of weight', 'Weight loss and anti-inflammatory pathways independent of glucose lowering', 'SGLT2-mediated natriuresis', 'Thyroid hormone axis stimulation'], correctOption: 1, explanation: 'SELECT tested cardiovascular benefit via weight loss and anti-inflammatory effects, not glucose lowering, in non-diabetic obese patients.', reference: 'WHY Q3: "cardiovascular benefits (MACE reduction) purely via weight loss and anti-inflammatory pathways, independently of glucose lowering" (Paper 33, SELECT)' },
  { id: 'ht-001-q7', subtopic: 'Dose Selection', question: 'Why is semaglutide 2.4 mg used for weight management but only 1.0 mg for type 2 diabetes glycemic control?', options: ['Higher dose required for CNS satiety center penetration and sustained hypothalamic GLP-1R activation', 'Lower diabetes dose avoids all GI side effects', '2.4 mg is the only dose with renal clearance', 'FDA mandates identical doses for all indications'], correctOption: 0, explanation: 'Weight reduction requires deeper, sustained CNS penetration; dose-finding showed 2.4 mg optimizes hypothalamic receptor activation for maximal weight loss.', reference: 'WHY Q8: "Weight reduction requires deep, sustained penetration into the central nervous system satiety centers" (Paper 22, Paper 39)' },
  { id: 'ht-001-q8', subtopic: 'HFpEF', question: 'In STEP-HFpEF, semaglutide improved heart failure symptoms in obese patients with HFpEF primarily by:', options: ['Increasing left ventricular ejection fraction above 60%', 'Reducing visceral/epicardial adiposity, inflammation, and plasma volume', 'Blocking beta-adrenergic receptors', 'Inducing rapid fluid restriction diuresis'], correctOption: 1, explanation: 'Benefits arise from reduced systemic inflammation, decreased visceral and epicardial fat compressing the heart, and lower plasma volume improving cardiac filling dynamics.', reference: 'WHY Q11: "reduces systemic inflammatory load, decreases visceral and epicardial adiposity... and lowers plasma volume" (Paper 31, STEP-HFpEF)' },
  { id: 'ht-001-q9', subtopic: 'Obesity Maintenance', question: 'STEP 4 randomized patients who lost weight on semaglutide 2.4 mg to continue drug vs switch to placebo. What happened to weight in the placebo group over 48 weeks?', options: ['Weight remained stable at nadir', 'Regained approximately two-thirds of lost weight', 'Continued losing weight with behavioral therapy alone', 'Developed hypoglycemia requiring drug restart'], correctOption: 1, explanation: 'Withdrawal to placebo led to rapid regain of ~two-thirds of lost weight, demonstrating obesity requires ongoing pharmacotherapy.', reference: 'HOW Q71: "regained approximately two-thirds of their lost weight within 48 weeks" (Paper 25, STEP 4)' },
  { id: 'ht-001-q10', subtopic: 'Hypoglycemia', question: 'A 45-year-old with type 2 diabetes on semaglutide monotherapy (no insulin/sulfonylurea) develops symptomatic hypoglycemia. Which mechanism makes this unlikely with semaglutide alone?', options: ['Semaglutide blocks all insulin secretion', 'GLP-1R-mediated insulin release is strictly glucose-dependent', 'Semaglutide increases hepatic glucose output', 'Albumin binding prevents pancreatic uptake'], correctOption: 1, explanation: 'Semaglutide stimulates insulin and suppresses glucagon only when glucose is elevated above fasting levels, minimizing hypoglycemia risk as monotherapy.', reference: 'WHY Q22: "Its mechanism of action on pancreatic beta cells is strictly glucose-dependent" (Paper 1, SUSTAIN 1)' },
  { id: 'ht-001-q11', subtopic: 'Diabetic Retinopathy', question: 'In SUSTAIN 6, some patients with severe baseline diabetic retinopathy experienced transient worsening after starting semaglutide. What is the most accepted explanation?', options: ['Direct retinal toxicity of GLP-1R agonism', 'Rapid HbA1c reduction causing ischemia-driven worsening (glycemic reduction phenomenon)', 'Albumin binding depositing in retinal vessels', 'SNAC formulation retinal accumulation'], correctOption: 1, explanation: 'Rapid glycemic improvement in patients with severe pre-existing retinopathy can temporarily worsen retinopathy — a known phenomenon with intensive glucose lowering.', reference: 'WHY Q7: "rapid, pronounced reduction in blood glucose... is associated with a temporary ischemia-driven worsening" (Paper 6, Paper 43)' },
  { id: 'ht-001-q12', subtopic: 'MASH', question: 'ESSENCE Part 1 demonstrated that semaglutide 2.4 mg in MASH with moderate-to-advanced fibrosis achieved which landmark hepatic outcome beyond steatohepatitis resolution?', options: ['Complete cirrhosis reversal in all patients', 'Statistically significant regression of liver fibrosis', 'Normalization of alpha-1 antitrypsin levels', 'Elimination of hepatitis B co-infection'], correctOption: 1, explanation: 'ESSENCE was the first Phase 3 trial showing semaglutide 2.4 mg resolves MASH and significantly regresses liver fibrosis.', reference: 'WHY Q46: "significantly resolves MASH and, crucially, achieves a statistically significant regression of liver fibrosis" (Paper 36, ESSENCE)' },
  { id: 'ht-001-q13', subtopic: 'Oral PK', question: 'Oral semaglutide has average bioavailability of ~1% yet achieves therapeutic steady-state levels. What dosing strategy compensates for this?', options: ['Single monthly mega-dose', 'Daily dosing establishing stable plasma levels despite variability', 'Subcutaneous rescue injection with each oral dose', 'Continuous IV infusion'], correctOption: 1, explanation: 'Despite ~1% bioavailability with high PK variability, daily oral dosing achieves stable therapeutic steady-state concentrations.', reference: 'HOW Q78: "bioavailability averages ~1%. However, daily dosing establishes highly stable, therapeutic steady-state blood levels" (Paper 37, Paper 38)' },
  { id: 'ht-001-q14', subtopic: 'Renal Dosing', question: 'A patient with eGFR 35 mL/min/1.73m² (CKD stage 3b) requires oral semaglutide. What dose adjustment is needed?', options: ['Reduce to 3 mg daily', 'Reduce to every-other-day dosing', 'No dose adjustment; PK driven by proteolytic degradation not renal excretion', 'Contraindicated — use insulin only'], correctOption: 2, explanation: 'Semaglutide clearance is primarily via systemic proteolytic degradation, not renal excretion; PIONEER 5 confirmed safety and PK in moderate renal impairment without adjustment.', reference: 'WHY Q19: "clearance of semaglutide is primarily driven by systemic metabolic peptide degradation rather than renal excretion" (Paper 16, Paper 48)' },
  { id: 'ht-001-q15', subtopic: 'Pediatrics', question: 'In STEP-TEENS, semaglutide 2.4 mg weekly in adolescents with obesity reduced BMI by what percentage at week 68?', options: ['8.4%', '12.1%', '16.1%', '20.3%'], correctOption: 2, explanation: 'STEP-TEENS showed a 16.1% BMI reduction at week 68 with efficacy comparable or superior to adult trials.', reference: 'HOW Q75: "reduced average BMI by 16.1% at week 68" (Paper 30, STEP-TEENS)' },
  { id: 'ht-001-q16', subtopic: 'Gastric Emptying', question: 'With chronic semaglutide use, which effect on gastric emptying is observed compared to initial dosing?', options: ['Progressive acceleration beyond baseline', 'Partial tachyphylaxis (desensitization) while central weight-loss effects persist', 'Complete permanent cessation of gastric motility', 'No effect at any time point'], correctOption: 1, explanation: 'Gastric emptying delay is pronounced initially but partially attenuates with chronic use; central appetite/weight effects remain fully maintained.', reference: 'HOW Q61: "undergoes partial tachyphylaxis (desensitization) over chronic use, whereas central weight-loss effects are fully maintained" (Paper 40)' },
  { id: 'ht-001-q17', subtopic: 'SELECT Outcomes', question: 'In SELECT (obesity without diabetes), semaglutide 2.4 mg reduced 3-point MACE hazard ratio to what value over ~39 months?', options: ['0.65', '0.80', '0.90', '1.05'], correctOption: 1, explanation: 'SELECT showed HR 0.80 (20% relative risk reduction) for MACE in non-diabetic obese patients.', reference: 'HOW Q74: "reduces the hazard ratio of 3-point MACE by 20% (HR 0.80)" (Paper 33, SELECT)' },
  { id: 'ht-001-q18', subtopic: 'FLOW Renal', question: 'In FLOW, semaglutide reduced the composite renal endpoint (≥50% eGFR decline, kidney failure, or kidney-related death) by what relative amount?', options: ['12% (HR 0.88)', '24% (HR 0.76)', '35% (HR 0.65)', '50% (HR 0.50)'], correctOption: 1, explanation: 'FLOW demonstrated a 24% reduction in composite kidney disease progression events (HR 0.76).', reference: 'HOW Q95: "lowers the hazard ratio of composite renal events... by 24% (HR 0.76)" (Paper 34, FLOW)' },
  { id: 'ht-001-q19', subtopic: 'Safety', question: 'Across major semaglutide programs (SUSTAIN, STEP, SELECT), acute pancreatitis incidence is best characterized as:', options: ['>5% requiring hospitalization', 'Significantly elevated vs all comparators', 'Exceptionally low (<0.1%) without significant increase vs placebo', 'Only seen with oral formulation'], correctOption: 2, explanation: 'Pancreatitis incidence remains <0.1% across major trials with no statistically significant increase vs placebo or active comparators.', reference: 'HOW Q83: "overall incidence remains exceptionally low (<0.1% across major programs), showing no statistically significant increase" (Paper 6, Paper 33)' },
  { id: 'ht-001-q20', subtopic: 'Thyroid Safety', question: 'Medullary thyroid carcinoma (MTC) carries a class-wide GLP-1RA black box warning because:', options: ['Human registry data confirmed MTC increase', 'Rodent studies showed GLP-1–mediated thyroid C-cell hyperplasia', 'Semaglutide directly mutates RET proto-oncogene', 'SNAC accumulates in thyroid follicles'], correctOption: 1, explanation: 'Rodent toxicology showed GLP-1 activation caused thyroid C-cell hyperplasia; not observed in human registries but remains a class precautionary warning.', reference: 'WHY Q44: "In rodent toxicology studies, GLP-1 activation caused thyroid C-cell hyperplasia" (Paper 6, Paper 22)' },
  { id: 'ht-001-q21', subtopic: 'Body Composition', question: 'STEP 1 DXA substudy showed lean soft tissue accounted for approximately what fraction of total weight lost on semaglutide 2.4 mg?', options: ['20%', '40%', '60%', '80%'], correctOption: 1, explanation: 'Participants lost ~10.4 kg fat mass and ~6.9 kg lean mass; lean mass ~40% of total weight loss, fat mass ~60%.', reference: 'HOW Q65: "lean mass reduction accounts for approximately 40% of the total weight lost, with fat mass accounting for the remaining 60%" (Paper 22, Paper 26)' },
  { id: 'ht-001-q22', subtopic: 'Trial Comparisons', question: 'In SUSTAIN 7, once-weekly semaglutide was compared to once-weekly dulaglutide. The result for both HbA1c and weight was:', options: ['Non-inferior only at 0.5 mg dose', 'Statistically superior at both 0.5 mg and 1.0 mg semaglutide doses', 'Inferior for weight but superior for HbA1c', 'Equivalent at all doses'], correctOption: 1, explanation: 'Semaglutide at both 0.5 mg and 1.0 mg was statistically superior to dulaglutide 0.75 mg and 1.5 mg for HbA1c and weight.', reference: 'HOW Q62: "statistically superior to once-weekly dulaglutide... in both HbA1c lowering and weight reduction" (Paper 7, SUSTAIN 7)' },
  { id: 'ht-001-q23', subtopic: 'Adverse Effects', question: 'Rapid weight loss on semaglutide increases gallbladder disease risk through which mechanisms?', options: ['Direct cholecystokinin receptor blockade', 'Cholesterol mobilization from adipose plus GLP-1–mediated reduced gallbladder motility', 'SNAC-induced bile duct obstruction', 'Insulin-induced gallstone calcification'], correctOption: 1, explanation: 'Rapid adipose cholesterol mobilization combined with reduced gallbladder motility from GLP-1R activation promotes biliary sludge and cholelithiasis.', reference: 'HOW Q77: "Rapid mobilization of cholesterol from adipose tissue... and GLP-1-mediated reduction in gallbladder motility" (Paper 22, Paper 33)' },
  { id: 'ht-001-q24', subtopic: 'CNS Mechanism', question: 'Semaglutide reduces appetite by acting on hypothalamic neurons to:', options: ['Stimulate NPY/AgRP neurons and inhibit POMC neurons', 'Stimulate POMC neurons and inhibit NPY/AgRP neurons', 'Block melanocortin-4 receptors directly', 'Increase ghrelin secretion from the stomach'], correctOption: 1, explanation: 'Semaglutide stimulates anorexigenic POMC neurons while inhibiting orexigenic NPY/AgRP neurons in the arcuate nucleus.', reference: 'HOW Q60: "stimulates pro-opiomelanocortin (POMC) neurons... while indirectly inhibiting neuropeptide Y (NPY) and agouti-related peptide (AgRP) neurons" (Paper 39, Paper 41)' },
  { id: 'ht-001-q25', subtopic: 'Titration', question: 'When initiating semaglutide 2.4 mg for weight management, a slow 4-week dose escalation is recommended primarily to:', options: ['Maximize initial weight loss in week 1', 'Allow GI tract adaptation and minimize nausea/vomiting/diarrhea', 'Achieve steady-state albumin binding faster', 'Prevent diabetic retinopathy'], correctOption: 1, explanation: 'Gradual titration over 4 weeks allows the GI tract to adapt to GLP-1R activation, reducing severity and frequency of transient GI side effects.', reference: 'WHY Q14: "allows the gastrointestinal tract to adapt over time to GLP-1 receptor activation, minimizing... nausea, vomiting, and diarrhea" (Paper 1, Paper 22)' },
  { id: 'ht-001-q26', subtopic: 'PIONEER 4', question: 'In PIONEER 4, oral semaglutide 14 mg daily compared to subcutaneous liraglutide 1.8 mg daily showed:', options: ['Inferior HbA1c reduction and inferior weight loss', 'Non-inferior HbA1c reduction and superior weight loss', 'Superior HbA1c but inferior weight loss', 'Equivalent outcomes on all endpoints'], correctOption: 1, explanation: 'Oral semaglutide 14 mg achieved non-inferior glycemic control and statistically superior weight loss vs daily liraglutide 1.8 mg.', reference: 'HOW Q58: "achieved non-inferior HbA1c reductions and demonstrated statistically superior weight loss" (Paper 15, PIONEER 4)' }
].map(q => ({ ...q, type: 'mcq' }));

const trueFalse = [
  { id: 'ht-001-tf1', subtopic: 'Oral Dosing', statement: 'Oral semaglutide should be taken with no more than 120 mL (4 oz) of plain water after an overnight fast.', correctAnswer: true, explanation: 'Excess water or food dilutes SNAC, reducing bioavailability.', reference: 'WHY Q6: "no more than 120 mL (4 oz) of plain water" (Paper 38)' },
  { id: 'ht-001-tf2', subtopic: 'Renal Dosing', statement: 'Oral semaglutide requires dose reduction in moderate chronic kidney disease (eGFR 30–59).', correctAnswer: false, explanation: 'No dose adjustment needed; clearance is via proteolytic degradation, not renal excretion.', reference: 'WHY Q19: "no dose adjustment needed for oral semaglutide in patients with renal impairment" (Paper 16, Paper 48)' },
  { id: 'ht-001-tf3', subtopic: 'Weight Maintenance', statement: 'STEP 4 demonstrated that obesity remission persists after semaglutide withdrawal without pharmacotherapy.', correctAnswer: false, explanation: 'Patients switching to placebo rapidly regained ~two-thirds of lost weight.', reference: 'HOW Q71: "regained approximately two-thirds of their lost weight within 48 weeks" (Paper 25)' },
  { id: 'ht-001-tf4', subtopic: 'Hypoglycemia', statement: 'Semaglutide monotherapy carries a high risk of symptomatic hypoglycemia.', correctAnswer: false, explanation: 'Insulin secretion is glucose-dependent; hypoglycemia risk is low without insulin or sulfonylureas.', reference: 'WHY Q22: "low risk of hypoglycemia with semaglutide monotherapy" (Paper 1)' },
  { id: 'ht-001-tf5', subtopic: 'SELECT', statement: 'The SELECT trial enrolled patients with obesity but without type 2 diabetes.', correctAnswer: true, explanation: 'SELECT tested CV outcomes independent of glucose lowering in non-diabetic obese adults.', reference: 'WHY Q3: "individuals without type 2 diabetes" (Paper 33)' },
  { id: 'ht-001-tf6', subtopic: 'FLOW', statement: 'The FLOW trial was stopped early due to efficacy on kidney outcomes.', correctAnswer: true, explanation: 'Interim analysis showed overwhelming kidney-protective benefit meeting prespecified criteria.', reference: 'WHY Q4: "independent data monitoring committee recommended stopping the FLOW trial early" (Paper 34)' },
  { id: 'ht-001-tf7', subtopic: 'Elderly', statement: 'Semaglutide requires dose reduction in adults ≥65 years due to altered pharmacokinetics.', correctAnswer: false, explanation: 'Pooled SUSTAIN/PIONEER data show age has no clinically relevant effect on PK, efficacy, or safety.', reference: 'WHY Q28: "age has no clinically relevant effect on the pharmacokinetics" (Paper 50)' },
  { id: 'ht-001-tf8', subtopic: 'Gastric Emptying', statement: 'The gastric emptying delay from semaglutide intensifies progressively over years of therapy.', correctAnswer: false, explanation: 'Gastric emptying effect shows partial tachyphylaxis with chronic use.', reference: 'HOW Q61: "undergoes partial tachyphylaxis (desensitization) over chronic use" (Paper 40)' },
  { id: 'ht-001-tf9', subtopic: 'Thyroid', statement: 'GLP-1 receptor agonists carry a precautionary black box warning for medullary thyroid carcinoma based on rodent data.', correctAnswer: true, explanation: 'Rodent C-cell hyperplasia data drives the class-wide MTC warning despite no human registry signal.', reference: 'WHY Q44: "GLP-1 activation caused thyroid C-cell hyperplasia" (Paper 6)' },
  { id: 'ht-001-tf10', subtopic: 'Injection Sites', statement: 'Subcutaneous semaglutide pharmacokinetics differ significantly between abdominal and thigh injection sites.', correctAnswer: false, explanation: 'PK profiles are equivalent across abdomen, thigh, and upper arm injection sites.', reference: 'HOW Q97: "highly equivalent and clinically interchangeable whether injected into the abdomen, thigh, or upper arm" (Paper 1)' },
  { id: 'ht-001-tf11', subtopic: 'Pancreatitis', statement: 'Semaglutide trials showed a statistically significant increase in acute pancreatitis vs placebo.', correctAnswer: false, explanation: 'Incidence <0.1% with no significant increase over comparators.', reference: 'HOW Q83: "no statistically significant increase compared to placebo" (Paper 6, Paper 33)' },
  { id: 'ht-001-tf12', subtopic: 'HFpEF', statement: 'Semaglutide improved KCCQ symptom scores and 6-minute walk distance in obese patients with HFpEF.', correctAnswer: true, explanation: 'STEP-HFpEF demonstrated improved symptoms, exercise capacity, and reduced inflammatory biomarkers.', reference: 'HOW Q64: "improves clinical symptom scores (KCCQ-CSS), increases 6-minute walk distance" (Paper 31)' }
].map(q => ({ ...q, type: 'true_false' }));

const ar = [
  { id: 'ht-001-ar1', subtopic: 'Half-life', assertion: 'Semaglutide can be dosed once weekly.', reason: 'A C18 fatty diacid chain promotes reversible albumin binding that protects the peptide from rapid renal clearance.', correctOption: 0, explanation: 'Both true; albumin binding extends half-life to ~1 week, enabling weekly dosing.', reference: 'WHY Q1: "extend its half-life to approximately 1 week... albumin binding" (Paper 1)' },
  { id: 'ht-001-ar2', subtopic: 'Oral Bioavailability', assertion: 'Oral semaglutide has very low absolute bioavailability (~1%).', reason: 'SNAC co-formulation enables transcellular gastric absorption of the peptide.', correctOption: 1, explanation: 'Both true but independent — low bioavailability reflects gut challenges; SNAC enables absorption but does not explain the low percentage itself.', reference: 'HOW Q78: "bioavailability averages ~1%" (Paper 37); WHY Q5: "SNAC acts as an absorption enhancer" (Paper 37)' },
  { id: 'ht-001-ar3', subtopic: 'Weight Dose', assertion: 'Semaglutide 2.4 mg is used for obesity management.', reason: 'Higher doses are needed for sustained hypothalamic GLP-1 receptor activation to maximize weight loss.', correctOption: 0, explanation: 'Both true; CNS penetration for satiety requires the higher 2.4 mg dose.', reference: 'WHY Q8: "2.4 mg dose optimizes long-term hypothalamic receptor activation" (Paper 22)' },
  { id: 'ht-001-ar4', subtopic: 'Retinopathy', assertion: 'Semaglutide can transiently worsen diabetic retinopathy in some patients.', reason: 'Semaglutide directly damages retinal capillary endothelial cells.', correctOption: 2, explanation: 'A is true (transient worsening with rapid glucose lowering); R is false (mechanism is glycemic reduction phenomenon, not direct toxicity).', reference: 'WHY Q7: "rapid, pronounced reduction in blood glucose... ischemia-driven worsening" (Paper 6)' },
  { id: 'ht-001-ar5', subtopic: 'FLOW', assertion: 'Semaglutide slows chronic kidney disease progression in type 2 diabetes.', reason: 'It reduces glomerular hyperfiltration, oxidative stress, and systemic hypertension.', correctOption: 0, explanation: 'Both true; renal protection operates through hemodynamic and anti-inflammatory mechanisms.', reference: 'WHY Q18: "reduces glomerular hyperfiltration, decreases local oxidative stress" (Paper 34)' },
  { id: 'ht-001-ar6', subtopic: 'Obesity Chronicity', assertion: 'Obesity requires ongoing pharmacotherapy for sustained weight loss.', reason: 'STEP 4 showed patients regained most weight after switching to placebo.', correctOption: 0, explanation: 'Both true; STEP 4 withdrawal data directly supports chronic treatment need.', reference: 'WHY Q10: "rapidly regained weight, demonstrating that continuous therapy is essential" (Paper 25)' },
  { id: 'ht-001-ar7', subtopic: 'Nausea', assertion: 'Nausea is a common early side effect of semaglutide.', reason: 'GLP-1R activation in the area postrema and delayed gastric emptying both contribute.', correctOption: 0, explanation: 'Both true; dual peripheral and central mechanisms explain nausea.', reference: 'WHY Q32: "delayed gastric emptying, and direct pharmacological activation of GLP-1 receptors in the area postrema" (Paper 22)' },
  { id: 'ht-001-ar8', subtopic: 'SELECT', assertion: 'Semaglutide reduces MACE in obese patients without diabetes.', reason: 'Semaglutide lowers HbA1c below 6.0% in all SELECT participants.', correctOption: 2, explanation: 'A is true (SELECT showed 20% MACE reduction); R is false (SELECT enrolled non-diabetic patients — benefit is via weight loss/inflammation, not glucose lowering).', reference: 'HOW Q74: "HR 0.80" (Paper 33); WHY Q3: "without type 2 diabetes" (Paper 33)' },
  { id: 'ht-001-ar9', subtopic: 'Hepatic Impairment', assertion: 'Hepatic impairment does not require oral semaglutide dose adjustment.', reason: 'Semaglutide is cleared via ubiquitous proteolytic degradation, not hepatic extraction.', correctOption: 0, explanation: 'Both true; clearance pathways are redundant and not hepatic-dependent.', reference: 'WHY Q29: "cleared via universal proteolytic degradation and fatty acid oxidation pathways" (Paper 47)' },
  { id: 'ht-001-ar10', subtopic: 'Appetite', assertion: 'Semaglutide reduces cravings for high-fat and sweet foods.', reason: 'It modulates the mesolimbic dopamine reward system reducing hedonic wanting.', correctOption: 0, explanation: 'Both true; reward pathway modulation explains food preference changes.', reference: 'WHY Q9: "modulates the mesolimbic dopamine reward system" (Paper 41)' },
  { id: 'ht-001-ar11', subtopic: 'MTC Warning', assertion: 'Semaglutide is contraindicated in patients with personal or family history of medullary thyroid carcinoma.', reason: 'Human clinical trials confirmed increased MTC incidence with semaglutide.', correctOption: 2, explanation: 'A is true (precautionary contraindication); R is false (human MTC signal not confirmed — warning based on rodent data).', reference: 'WHY Q44: "not been observed in human clinical registries" (Paper 6)' },
  { id: 'ht-001-ar12', subtopic: 'STEP 2', assertion: 'Weight loss with semaglutide 2.4 mg is slightly less in type 2 diabetes than in non-diabetic obesity.', reason: 'Background insulin or sulfonylurea therapy promotes lipogenesis and counteracts weight loss.', correctOption: 0, explanation: 'Both true; STEP 2 showed ~9.6% vs ~15% loss, partly due to diabetes therapies and metabolic adaptations.', reference: 'HOW Q66: "Weight loss is slightly lower in diabetic patients (~9.6% vs ~15%)" (Paper 23)' }
].map(q => ({ ...q, type: 'assertion_reason' }));

const output = {
  id: 'ht-001',
  topicType: 'hot_topic',
  title: 'Semaglutide',
  subtitle: 'GLP-1 Receptor Agonist — Comprehensive PubMed-Based Review',
  section: 'Hot Topics',
  category: 'Endocrinology & Metabolism',
  authors: 'PubMed Landmark Trials (SUSTAIN, PIONEER, STEP, SELECT, FLOW)',
  sourceFile: 'semaglutide_pubmed_qa_100.md',
  items: [...notes, ...mcqs, ...trueFalse, ...ar]
};

fs.writeFileSync(OUT, JSON.stringify(output, null, 2) + '\n');

const counts = {};
output.items.forEach(it => { counts[it.type] = (counts[it.type] || 0) + 1; });
const whyHow = notes.filter(n => /^(Why|How)/.test(n.title)).length;
console.log('Written:', OUT);
console.log('Counts:', counts, 'total:', output.items.length);
console.log('Notes Why/How:', whyHow + '/' + notes.length);
