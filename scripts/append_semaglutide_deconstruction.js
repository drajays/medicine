#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(__dirname, '../data/ht-001_semaglutide.json');
const data = JSON.parse(fs.readFileSync(OUT, 'utf8'));

const DECON = [
  { cat: 'Axiomatic — The Root', num: '1.1', certainty: 'Uncertain',
    title: 'Native vs. continuous GLP-1 receptor activation: are the foundational assumptions sound?',
    content: 'Native GLP-1 is secreted in rapid, short-lived postprandial pulses. Semaglutide enforces non-physiological, continuous receptor agonism. While it is assumed this merely scales up the native effect, continuous activation in other endocrine systems often causes receptor internalization and downregulation.\n\nThe GLP-1R seems unusually resistant to complete desensitization, but tachyphylaxis observed with gastrointestinal side effects suggests partial downregulation occurs. Whether continuous activation is fundamentally sound long-term remains debated.',
    keyPoints: ['Native GLP-1: pulsatile, minutes-long exposure', 'Semaglutide: continuous 7-day receptor agonism', 'GI tachyphylaxis suggests partial receptor downregulation', 'Long-term soundness of non-physiological activation: debated'] },
  { cat: 'Axiomatic — The Root', num: '1.2', certainty: 'Uncertain',
    title: 'Are HbA1c and body weight invariant proxies for reversed metabolic dysfunction?',
    content: 'SUSTAIN and STEP assume HbA1c and body weight are proxies for reversed metabolic dysfunction. However, trial extension data (STEP 1 extension) shows these are merely clamped states, not structural reversals.\n\nUpon cessation, cardiometabolic risk factors revert, proving the underlying disease architecture remains intact despite apparent improvement on therapy.',
    keyPoints: ['HbA1c and weight treated as metabolic health proxies in trials', 'STEP 1 extension: improvements are clamped, not structural', 'Risk factors revert after drug cessation', 'Underlying disease architecture persists'] },
  { cat: 'Axiomatic — The Root', num: '1.3', certainty: 'Mostly Known',
    title: 'Is weight loss primarily central appetite suppression or peripheral lipid partitioning?',
    content: 'Published literature heavily supports the axiom that weight loss is primarily centrally mediated (hindbrain and hypothalamus). While secondary peripheral effects exist (e.g., improved lipid partitioning in hepatocytes), animal models with vagotomy or brain lesions confirm that without central nervous system penetrance, GLP-1-mediated weight loss practically ceases.',
    keyPoints: ['Weight loss primarily centrally mediated (hindbrain/hypothalamus)', 'Peripheral effects (hepatic lipid partitioning) are secondary', 'Vagotomy/brain-lesion models abolish GLP-1 weight loss', 'Central CNS penetrance is prerequisite for durable appetite suppression'] },
  { cat: 'Glassbox — The Mechanism', num: '2.1', certainty: 'Known',
    title: 'Intracellular signaling in hypothalamic POMC/CART neurons beyond cAMP/PKA',
    content: 'Beyond cAMP/PKA, semaglutide binding to the Gs-protein coupled GLP-1 receptor in POMC/CART neurons activates Epac2 (Exchange protein directly activated by cAMP). This cascade triggers opening of TRPC (Transient Receptor Potential Canonical) channels, causing membrane depolarization, calcium influx, and subsequent exocytosis of alpha-MSH.\n\nAlpha-MSH signals downstream to the MC4 receptor to suppress appetite.',
    keyPoints: ['GLP-1R → Gs → cAMP → Epac2 activation', 'Epac2 opens TRPC channels → Ca²⁺ influx', 'POMC neuron depolarization → alpha-MSH exocytosis', 'Alpha-MSH → MC4R → appetite suppression'] },
  { cat: 'Glassbox — The Mechanism', num: '2.2', certainty: 'Known',
    title: 'Mechanical mapping of gastric smooth muscle relaxation to delayed emptying',
    content: 'Semaglutide activates GLP-1 receptors on vagal afferents in the gut, sending signals to the Nucleus Tractus Solitarius (NTS) in the brainstem. This triggers parasympathetic efferent withdrawal, reducing cholinergic drive to gastric smooth muscle.\n\nOver a 7-day dosing interval, tachyphylaxis is observed: the delay in gastric emptying is pronounced during dose escalation but largely normalizes after continuous steady-state exposure.',
    keyPoints: ['Gut GLP-1R → vagal afferents → NTS brainstem', 'Parasympathetic efferent withdrawal reduces cholinergic gastric drive', 'Pronounced delay during dose escalation', 'Partial normalization (tachyphylaxis) at steady state'] },
  { cat: 'Glassbox — The Mechanism', num: '2.3', certainty: 'Uncertain',
    title: 'Intra-islet paracrine dynamics for glucose-dependent glucagon suppression',
    content: 'The mechanism of glucagon suppression is highly debated because alpha cells express virtually zero GLP-1 receptors. The suppression is likely indirect: semaglutide stimulates beta cells to release insulin and GABA, and delta cells to release somatostatin.\n\nThese locally secreted paracrine factors physically diffuse within the islet micro-architecture to shut down alpha-cell glucagon secretion in a glucose-dependent manner.',
    keyPoints: ['Alpha cells lack GLP-1 receptors — suppression is indirect', 'Beta cells release insulin + GABA; delta cells release somatostatin', 'Paracrine diffusion within islet micro-architecture', 'Glucose-dependent mechanism remains incompletely mapped'] },
  { cat: 'Invariant — The Constants', num: '3.1', certainty: 'Known',
    title: 'Structural properties uncompromised across hepatic and renal impairment',
    content: 'The alpha-aminoisobutyric acid (Aib) substitution at position 8 creates absolute steric hindrance against the DPP-4 enzyme. The C18 fatty diacid chain grants invariant, high-affinity non-covalent binding to serum albumin.\n\nBecause semaglutide is degraded via general protein catabolism (proteolysis) rather than specific hepatic CYP450 pathways or renal filtration, these structural properties remain entirely uncompromised regardless of severe hepatic or renal impairment.',
    keyPoints: ['Aib at position 8: steric DPP-4 resistance', 'C18 diacid: invariant albumin binding', 'Clearance via proteolysis, not CYP450 or renal filtration', 'PK unchanged in severe hepatic/renal impairment'] },
  { cat: 'Invariant — The Constants', num: '3.2', certainty: 'Uncertain',
    title: 'Systemic biomarkers that remain unchanged despite weight loss and HbA1c reduction',
    content: 'While systemic markers like hsCRP and lipids reliably drop, markers that reflect deeply entrenched fibrotic architecture—such as advanced fibrosis scores in MASH/NASH (F3–F4 stages)—often remain unchanged or progress despite significant weight loss and HbA1c reduction.',
    keyPoints: ['hsCRP and lipids reliably improve', 'Advanced MASH fibrosis scores (F3–F4) may not regress', 'Deep fibrotic architecture can persist despite metabolic gains', 'Structural reversal ≠ biomarker normalization'] },
  { cat: 'Invariant — The Constants', num: '3.3', certainty: 'Known',
    title: 'Binding affinity constants under chronic high-dose saturation',
    content: 'The chemical dissociation constant (Kd) governing semaglutide\'s affinity for the GLP-1R is an invariant physical property. Chronic, high-dose saturation does not alter the drug\'s affinity; rather, it may alter the density (Bmax) of available surface receptors.\n\nClinical efficacy curves prove receptor density changes do not negate the therapeutic effect.',
    keyPoints: ['Kd is an invariant physical constant', 'Chronic saturation may reduce surface receptor density (Bmax)', 'Affinity itself does not change with duration', 'Therapeutic efficacy maintained despite potential Bmax shifts'] },
  { cat: 'Falsifiability — The Breakpoint', num: '4.1', certainty: 'Known',
    title: 'What would falsify weight-independent cardiovascular and renal protection?',
    content: 'To definitively falsify weight-independent cardioprotection, a trial must feature an active comparator arm achieving the exact same trajectory and magnitude of weight loss (e.g., via a strictly matched hypocaloric diet or specific bariatric interventions) over 5 years.\n\nIf the CV hazard ratios converge perfectly between arms, the independent protective mechanism is falsified.',
    keyPoints: ['Requires matched weight-loss comparator over 5 years', 'Bariatric surgery or enforced hypocaloric diet as active control', 'Converging hazard ratios would falsify independent protection', 'Currently no trial has definitively isolated this variable'] },
  { cat: 'Falsifiability — The Breakpoint', num: '4.2', certainty: 'Unknown',
    title: 'How to falsify beta-cell structural remodeling or accelerated senescence',
    content: 'Falsification requires serial, in vivo structural analysis of human pancreatic islets, which is currently impossible without autopsy or unethical serial biopsies. We can only track functional proxies (C-peptide, proinsulin/insulin ratio), which cannot definitively rule out microscopic architectural exhaustion.',
    keyPoints: ['Serial human islet biopsy not ethically feasible', 'Functional proxies: C-peptide, proinsulin/insulin ratio', 'Cannot rule out microscopic beta-cell exhaustion', 'Falsification currently impossible with available methods'] },
  { cat: 'Falsifiability — The Breakpoint', num: '4.3', certainty: 'Known',
    title: 'Falsifying central receptor desensitization vs. thermodynamic plateau',
    content: 'This is falsifiable via thermodynamic intervention. If a patient at a semaglutide plateau is subjected to a rigidly controlled, mechanically enforced caloric deficit (e.g., metabolic ward) and resumes losing weight, it proves the plateau is a thermodynamic equilibrium (energy intake matches lowered metabolic rate), not central receptor desensitization.',
    keyPoints: ['STEP plateau at weeks 60–68 is testable', 'Metabolic ward enforced deficit can break plateau', 'Resumed weight loss → thermodynamic, not receptor desensitization', 'Adaptive thermogenesis explains equilibrium'] },
  { cat: 'Counterfactual — The Inversion', num: '5.1', certainty: 'Uncertain',
    title: 'SELECT cardiovascular benefit if weight loss is mathematically subtracted',
    content: 'Post-hoc mediation analyses from the SELECT trial suggest that if weight loss is mathematically isolated, roughly 20–30% of the cardiovascular benefit remains, pointing toward direct anti-inflammatory pathways (hsCRP reduction) and endothelial plaque stabilization independent of adipose reduction.',
    keyPoints: ['SELECT mediation analysis: ~20–30% CV benefit independent of weight', 'Residual benefit via hsCRP reduction', 'Endothelial plaque stabilization may be weight-independent', 'Majority of benefit still weight-mediated'] },
  { cat: 'Counterfactual — The Inversion', num: '5.2', certainty: 'Known',
    title: 'If mechanism were peripheral rather than central: what would change?',
    content: 'If the mechanism were strictly peripheral, GLP-1RAs that do not cross the blood-brain barrier would cause equivalent weight loss. Literature shows peripherally restricted experimental analogs improve glycemia but fail to induce significant weight loss, disproving the peripheral-dominant hypothesis.',
    keyPoints: ['Peripherally restricted GLP-1RAs improve glycemia only', 'No significant weight loss without BBB penetration', 'Peripheral-dominant hypothesis disproved experimentally', 'Central mechanism is necessary for weight effects'] },
  { cat: 'Counterfactual — The Inversion', num: '5.3', certainty: 'Known',
    title: 'If semaglutide half-life were compressed to native GLP-1 (~2 hours)',
    content: 'If semaglutide had a 2-hour half-life, it would behave exactly like exenatide. It would successfully lower post-prandial glucose via insulin secretion, but it would completely fail to induce meaningful weight loss, as continuous central nervous system saturation is an absolute prerequisite for durable appetite suppression.',
    keyPoints: ['2-hour half-life → exenatide-like pharmacology', 'Post-prandial glucose lowering preserved', 'Meaningful weight loss would fail', 'Continuous CNS saturation required for appetite suppression'] },
  { cat: 'Second-Order — The Cascade', num: '6.1', certainty: 'Uncertain',
    title: 'Long-term gastric slowing: microbiota and oral drug absorption kinetics',
    content: 'Gastric slowing is mostly transient, but the profound, years-long reduction in total caloric intake and shift in macronutrient preference severely alters the gut microbiome (reduced diversity in some cohorts). Absorption kinetics of narrow-therapeutic-index oral drugs (e.g., levothyroxine, lithium) are delayed in Tmax, though the Area Under the Curve (AUC) usually remains stable.',
    keyPoints: ['Gastric slowing largely transient at steady state', 'Caloric restriction alters gut microbiome diversity', 'Narrow-index drugs: delayed Tmax (levothyroxine, lithium)', 'AUC usually stable despite delayed peak absorption'] },
  { cat: 'Second-Order — The Cascade', num: '6.2', certainty: 'Uncertain',
    title: 'Visceral fat loss: downstream bone marrow and bone turnover effects',
    content: 'Rapid weight loss mechanically unloads the skeleton, which triggers a known second-order increase in bone resorption markers (e.g., CTX) and a decrease in bone mineral density. The multi-year consequence of this on absolute fracture risk in semaglutide cohorts is currently under intense post-market surveillance.',
    keyPoints: ['Rapid weight loss unloads skeleton mechanically', 'Increased bone resorption markers (CTX)', 'Decreased bone mineral density observed', 'Long-term fracture risk under post-market surveillance'] },
  { cat: 'Second-Order — The Cascade', num: '6.3', certainty: 'Unknown',
    title: 'Years-long dopamine reward suppression: hedonic and neurochemical consequences',
    content: 'Semaglutide dampens dopamine release in the mesolimbic reward system (VTA to nucleus accumbens) in response to food and alcohol. The long-term compounding effect of continuous dopaminergic blunting on global hedonic tone (risk of anhedonia or mood discordance) remains a biological plausibility lacking definitive long-term psychiatric data.',
    keyPoints: ['Dampens VTA → nucleus accumbens dopamine to food/alcohol', 'Continuous hedonic suppression over years: unknown consequences', 'Theoretical risk of anhedonia or mood discordance', 'No definitive long-term psychiatric outcome data'] },
  { cat: 'Boundary — The Extremes', num: '7.1', certainty: 'Known',
    title: 'Dose threshold where metabolic efficacy transitions to exponential GI toxicity',
    content: 'The transition from linear metabolic efficacy to exponential GI toxicity occurs rapidly when dose escalations breach the natural tolerance induction window (typically escalations >0.5 mg per month, or absolute doses exceeding 2.4 mg). This is driven by peak serum concentrations (Cmax) saturating the Area Postrema (the brain\'s vomiting center), which lacks a blood-brain barrier.',
    keyPoints: ['Escalation >0.5 mg/month increases GI toxicity', 'Doses exceeding 2.4 mg saturate area postrema', 'Cmax-driven nausea/vomiting at vomiting center', 'Area postrema lacks blood-brain barrier'] },
  { cat: 'Boundary — The Extremes', num: '7.2', certainty: 'Known',
    title: 'Therapeutic breakdown at metabolic spectrum extremes',
    content: 'At the extreme of absolute insulin deficiency (Type 1 Diabetes or late-stage lipodystrophy), the glycemic efficacy of semaglutide breaks down entirely, as its mechanism requires functional beta-cell mass. On the lean extreme, it disproportionately catabolizes lean muscle mass alongside fat, breaking the therapeutic logic of metabolic health improvement.',
    keyPoints: ['Type 1 DM / lipodystrophy: no functional beta cells → no glycemic effect', 'Requires intact beta-cell mass for insulin secretion', 'Lean individuals: disproportionate lean mass catabolism', 'Therapeutic logic breaks at both metabolic extremes'] },
  { cat: 'Boundary — The Extremes', num: '7.3', certainty: 'Unknown',
    title: 'Semaglutide signaling during acute hypoxia, heart failure, or sepsis',
    content: 'In acute inflammatory states, profound sympathetic nervous system override and elevated counter-regulatory hormones (cortisol, epinephrine) generally blunt the incretin effect. The direct behavior of semaglutide at the cellular level during acute ischemic stress remains poorly mapped in humans.',
    keyPoints: ['Acute inflammation blunts incretin effect generally', 'Counter-regulatory hormones (cortisol, epinephrine) override GLP-1 signaling', 'Cellular behavior during ischemic stress unmapped in humans', 'Protective vs. aberrant signaling in sepsis/HF: unknown'] },
  { cat: 'Lineage — The Origin', num: '8.1', certainty: 'Known',
    title: 'DPP-4 constraints that dictated semaglutide\'s chemical modifications from liraglutide',
    content: 'Native GLP-1 is cleaved by DPP-4 precisely between Alanine-8 and Glutamate-9. Liraglutide retained Alanine-8, relying only on steric shielding from its C16 fatty acid, leading to a 13-hour half-life. Semaglutide\'s origin necessitated replacing Alanine-8 with Aib to mathematically guarantee zero DPP-4 cleavage, extending the half-life to 165 hours.',
    keyPoints: ['DPP-4 cleaves native GLP-1 between Ala-8 and Glu-9', 'Liraglutide: retained Ala-8 + C16 fatty acid → 13-h half-life', 'Semaglutide: Aib-8 substitution → zero DPP-4 cleavage', 'Result: 165-hour half-life enabling weekly dosing'] },
  { cat: 'Lineage — The Origin', num: '8.2', certainty: 'Known',
    title: 'How short-acting GLP-1RA CV trial failures shaped SUSTAIN/STEP design',
    content: 'Early short-acting agents (lixisenatide in the ELIXA trial) failed to show CV superiority. This proved that transient, post-prandial incretin spikes do not alter vascular biology. This failure forced the structural design of semaglutide to prioritize 24/7 steady-state exposure, directly shaping the endpoints of SUSTAIN-6.',
    keyPoints: ['ELIXA (lixisenatide): no CV superiority demonstrated', 'Transient post-prandial spikes do not alter vascular biology', 'Semaglutide designed for 24/7 steady-state exposure', 'Directly shaped SUSTAIN-6 cardiovascular endpoints'] },
  { cat: 'Lineage — The Origin', num: '8.3', certainty: 'Known',
    title: 'CVOT assumptions that repositioned semaglutide as cardioprotective agent',
    content: 'The 2008 FDA mandate assumed all new diabetes drugs harbored hidden ischemic risks (post-Rosiglitazone). CVOTs were designed purely as non-inferiority safety trials. The serendipitous finding of cardiovascular superiority forced the paradigm shift of semaglutide from a mere secretagogue to a primary preventative cardiovascular agent.',
    keyPoints: ['2008 FDA mandate: CV safety for all new diabetes drugs', 'CVOTs designed as non-inferiority safety trials', 'SUSTAIN-6 serendipitously showed CV superiority', 'Repositioned from secretagogue to primary cardioprotective agent'] },
  { cat: 'Equilibrium — The End-State', num: '9.1', certainty: 'Known',
    title: 'Thermodynamic equilibrium driving the STEP weight-loss plateau at weeks 60–68',
    content: 'The plateau at week 60–68 represents a thermodynamic equilibrium. As patients lose mass, their Basal Metabolic Rate (BMR) drops via adaptive thermogenesis. The equilibrium point is where the lowered daily caloric expenditure mathematically intersects with the artificially suppressed caloric intake.',
    keyPoints: ['Plateau = thermodynamic equilibrium, not receptor failure', 'BMR drops via adaptive thermogenesis with mass loss', 'Lowered expenditure intersects suppressed intake', 'Occurs around weeks 60–68 in STEP trials'] },
  { cat: 'Equilibrium — The End-State', num: '9.2', certainty: 'Known',
    title: 'Physiological forces driving rebound after semaglutide cessation',
    content: 'The system rebounds aggressively toward baseline because the biological "set-point" in the hypothalamus is never structurally altered by semaglutide. Upon withdrawal, plummeting GLP-1 receptor agonism coincides with elevated ghrelin levels (due to weight loss), driving hyperphagia.',
    keyPoints: ['Hypothalamic set-point never structurally altered', 'Drug withdrawal → plummeting GLP-1R agonism', 'Elevated ghrelin from weight loss drives hyperphagia', 'STEP 4: ~two-thirds weight regained within 48 weeks'] },
  { cat: 'Equilibrium — The End-State', num: '9.3', certainty: 'Known',
    title: 'Beta-cell resting state at glycemic equilibrium (HbA1c <6.0%)',
    content: 'At an HbA1c <6.0%, the long-term resting state of the beta-cell is one of profound offloading. Reduced glucotoxicity, lipotoxicity, and peripheral insulin resistance result in a marked drop in fasting insulin requirements, allowing beta-cells to rest and restoring a more physiological proinsulin-to-insulin cleavage ratio.',
    keyPoints: ['HbA1c <6.0%: beta-cells in offloaded resting state', 'Reduced glucotoxicity and lipotoxicity', 'Fasting insulin requirements markedly decrease', 'Proinsulin-to-insulin ratio normalizes (HOMA-B improves)'] },
  { cat: 'Discordance — The Anomalies', num: '10.1', certainty: 'Uncertain',
    title: 'Structural mechanism of non-responders in STEP trials',
    content: 'Roughly 10–15% of patients are non-responders. The structural mechanism is likely polygenic discordance—patients whose obesity is driven by pathways downstream of the GLP-1R/POMC axis (e.g., MC4R mutations), severe psychological eating disorders that override homeostatic satiety signals, or rare polymorphisms in the GLP-1 receptor itself.',
    keyPoints: ['~10–15% non-responder rate despite verified adherence', 'MC4R mutations bypass GLP-1R/POMC pathway', 'Psychological eating disorders override satiety signals', 'Rare GLP-1R polymorphisms possible'] },
  { cat: 'Discordance — The Anomalies', num: '10.2', certainty: 'Uncertain',
    title: 'CV sub-metric discordance: MACE reduced but MI/stroke sub-metrics often insignificant',
    content: 'While composite MACE is reduced, isolated metrics like non-fatal MI often lack statistical significance in some cohorts. This discordance likely exists because atherosclerosis takes decades to form; 3-to-5-year trials capture the stabilization of vulnerable plaques (preventing fatal ruptures/strokes) but are too short to reverse structural coronary stenosis.',
    keyPoints: ['Composite MACE significantly reduced in major trials', 'Non-fatal MI sub-metrics often lack significance', '3–5 year trials stabilize plaques, not reverse stenosis', 'Atherosclerosis reversal requires decades'] },
  { cat: 'Discordance — The Anomalies', num: '10.3', certainty: 'Known',
    title: 'Lipase/amylase elevation discordance with low clinical pancreatitis incidence',
    content: 'Semaglutide directly binds to GLP-1 receptors on pancreatic exocrine acinar cells, promoting low-grade, constitutive exocytosis of lipase and amylase into the serum. However, clinical acute pancreatitis requires intracellular auto-activation of zymogens. Semaglutide increases enzyme release but does not trigger the pathological activation cascade, explaining the benign lab elevations alongside the extremely low incidence of actual necrosis.',
    keyPoints: ['GLP-1R on pancreatic acinar cells → constitutive enzyme exocytosis', 'Serum lipase/amylase elevations are common and asymptomatic', 'Acute pancreatitis requires intracellular zymogen auto-activation', 'Incidence <0.1%; lab elevations are benign'] }
];

const notes = DECON.map((d, i) => ({
  id: `ht-001-n${101 + i}`,
  type: 'note',
  subtopic: d.cat,
  title: d.title,
  content: d.content + `\n\nCertainty: ${d.certainty}`,
  keyPoints: d.keyPoints,
  reference: `${d.cat.split(' — ')[0].toUpperCase()} ${d.num} [${d.certainty}]: "${d.content.split('\n\n')[0].slice(0, 100)}${d.content.length > 100 ? '...' : ''}"`
}));

const mcqs = [
  { id: 'ht-001-q27', subtopic: 'Glassbox — Mechanism', question: 'Beyond cAMP/PKA, which signaling pathway in hypothalamic POMC neurons is activated by semaglutide to drive appetite suppression?', options: ['mTOR → S6K phosphorylation', 'Epac2 → TRPC channel opening → alpha-MSH release → MC4R', 'JAK-STAT → SOCS3 induction', 'NF-κB → inflammatory cytokine release'], correctOption: 1, explanation: 'Semaglutide activates Epac2 downstream of cAMP, opening TRPC channels, depolarizing POMC neurons, and releasing alpha-MSH which signals via MC4R.', reference: 'GLASSBOX 2.1 [Known]: "activates Epac2... triggers the opening of TRPC channels... exocytosis of alpha-MSH"' },
  { id: 'ht-001-q28', subtopic: 'Invariant — Constants', question: 'Which semaglutide structural modification mathematically guarantees zero DPP-4 cleavage?', options: ['C16 fatty acid on lysine-26 (liraglutide design)', 'Aib substitution at position 8 replacing alanine', 'Arginine substitution at position 34 only', 'SNAC co-formulation in oral tablets'], correctOption: 1, explanation: 'DPP-4 cleaves between Ala-8 and Glu-9 in native GLP-1. Replacing Ala-8 with Aib creates absolute steric hindrance, extending half-life to 165 hours vs liraglutide\'s 13 hours.', reference: 'LINEAGE 8.1 [Known]: "replacing Alanine-8 with Aib to mathematically guarantee zero DPP-4 cleavage"' },
  { id: 'ht-001-q29', subtopic: 'Counterfactual — Inversion', question: 'If semaglutide\'s half-life were compressed to ~2 hours while maintaining receptor affinity, which therapeutic effect would be lost?', options: ['Post-prandial glucose lowering', 'Durable weight loss via central appetite suppression', 'Glucagon suppression', 'Renal protection in FLOW'], correctOption: 1, explanation: 'A 2-hour half-life would mimic exenatide — effective for post-prandial glucose but unable to sustain CNS saturation needed for meaningful weight loss.', reference: 'COUNTERFACTUAL 5.3 [Known]: "completely fail to induce meaningful weight loss, as continuous central nervous system saturation is an absolute prerequisite"' },
  { id: 'ht-001-q30', subtopic: 'Equilibrium — End-State', question: 'The STEP trial weight-loss plateau at weeks 60–68 is best explained by:', options: ['Complete GLP-1 receptor desensitization in the hypothalamus', 'Thermodynamic equilibrium between lowered BMR and suppressed caloric intake', 'Development of anti-semaglutide antibodies', 'Irreversible beta-cell exhaustion'], correctOption: 1, explanation: 'The plateau represents adaptive thermogenesis lowering BMR as mass decreases, intersecting with pharmacologically suppressed intake — a thermodynamic equilibrium, not receptor failure.', reference: 'EQUILIBRIUM 9.1 [Known]: "thermodynamic equilibrium... BMR drops via adaptive thermogenesis"' },
  { id: 'ht-001-q31', subtopic: 'Discordance — Anomalies', question: 'Asymptomatic serum lipase/amylase elevations on semaglutide occur because:', options: ['Acute zymogen auto-activation causing subclinical pancreatitis', 'GLP-1R-mediated constitutive exocytosis from acinar cells without zymogen activation', 'SNAC-induced pancreatic duct obstruction', 'Direct acinar cell necrosis from albumin binding'], correctOption: 1, explanation: 'Semaglutide binds GLP-1R on exocrine acinar cells promoting enzyme release, but does not trigger the intracellular zymogen auto-activation cascade required for clinical pancreatitis.', reference: 'DISCORDANCE 10.3 [Known]: "promoting low-grade, constitutive exocytosis of lipase and amylase... does not trigger the pathological activation cascade"' },
  { id: 'ht-001-q32', subtopic: 'Falsifiability — Breakpoint', question: 'To falsify weight-independent cardiovascular protection of semaglutide, a trial would need:', options: ['A larger sample size in SELECT', 'An active comparator achieving identical weight loss magnitude over 5 years', 'Longer follow-up in FLOW only', 'Higher semaglutide dose (3.0 mg weekly)'], correctOption: 1, explanation: 'If CV hazard ratios converge when weight loss is perfectly matched via bariatric surgery or enforced hypocaloric diet, weight-independent protection would be falsified.', reference: 'FALSIFIABILITY 4.1 [Known]: "active comparator arm achieving the exact same trajectory and magnitude of weight loss... over 5 years"' }
].map(q => ({ ...q, type: 'mcq' }));

const trueFalse = [
  { id: 'ht-001-tf13', subtopic: 'Axiomatic — Root', statement: 'STEP trial improvements in HbA1c and weight represent structural reversal of underlying metabolic disease architecture.', correctAnswer: false, explanation: 'Trial extensions show these are clamped states; risk factors revert upon cessation, proving underlying disease architecture remains intact.', reference: 'AXIOMATIC 1.2 [Uncertain]: "these are merely clamped states, not structural reversals"' },
  { id: 'ht-001-tf14', subtopic: 'Glassbox — Mechanism', statement: 'Alpha cells express high levels of GLP-1 receptors, enabling direct glucagon suppression by semaglutide.', correctAnswer: false, explanation: 'Alpha cells express virtually zero GLP-1 receptors; glucagon suppression is indirect via beta-cell insulin/GABA and delta-cell somatostatin paracrine signaling.', reference: 'GLASSBOX 2.3 [Uncertain]: "alpha cells express virtually zero GLP-1 receptors"' },
  { id: 'ht-001-tf15', subtopic: 'Counterfactual — Inversion', statement: 'Peripherally restricted GLP-1RAs that do not cross the blood-brain barrier cause equivalent weight loss to semaglutide.', correctAnswer: false, explanation: 'Experimental peripherally restricted analogs improve glycemia but fail to induce significant weight loss, disproving peripheral-dominant mechanism.', reference: 'COUNTERFACTUAL 5.2 [Known]: "peripherally restricted experimental analogs improve glycemia but fail to induce significant weight loss"' },
  { id: 'ht-001-tf16', subtopic: 'Equilibrium — End-State', statement: 'Upon semaglutide withdrawal, the hypothalamic metabolic set-point returns to a more resilient state than baseline.', correctAnswer: false, explanation: 'The set-point is never structurally altered; withdrawal causes aggressive rebound via plummeting GLP-1R agonism and elevated ghrelin-driven hyperphagia.', reference: 'EQUILIBRIUM 9.2 [Known]: "the biological set-point in the hypothalamus is never structurally altered by semaglutide"' },
  { id: 'ht-001-tf17', subtopic: 'Lineage — Origin', statement: 'The ELIXA trial failure with short-acting lixisenatide directly shaped semaglutide\'s design for 24/7 steady-state exposure.', correctAnswer: true, explanation: 'ELIXA proved transient post-prandial incretin spikes do not alter vascular biology, forcing continuous exposure design in SUSTAIN-6.', reference: 'LINEAGE 8.2 [Known]: "transient, post-prandial incretin spikes do not alter vascular biology"' },
  { id: 'ht-001-tf18', subtopic: 'Boundary — Extremes', statement: 'Semaglutide retains full glycemic efficacy in patients with absolute insulin deficiency (type 1 diabetes).', correctAnswer: false, explanation: 'Glycemic efficacy requires functional beta-cell mass; in type 1 DM or late-stage lipodystrophy the mechanism breaks down entirely.', reference: 'BOUNDARY 7.2 [Known]: "glycemic efficacy of semaglutide breaks down entirely, as its mechanism requires functional beta-cell mass"' }
].map(q => ({ ...q, type: 'true_false' }));

const ar = [
  { id: 'ht-001-ar13', subtopic: 'Axiomatic — Root', assertion: 'Semaglutide-induced weight loss is primarily centrally mediated.', reason: 'Peripherally restricted GLP-1RAs cause equivalent weight loss without CNS penetration.', correctOption: 2, explanation: 'A is true (central mediation supported); R is false (peripheral analogs fail to induce significant weight loss).', reference: 'AXIOMATIC 1.3 [Mostly Known]: "without central nervous system penetrance, GLP-1-mediated weight loss practically ceases"; COUNTERFACTUAL 5.2 [Known]: "peripherally restricted experimental analogs improve glycemia but fail to induce significant weight loss"' },
  { id: 'ht-001-ar14', subtopic: 'Equilibrium — End-State', assertion: 'The STEP weight plateau represents thermodynamic equilibrium.', reason: 'Adaptive thermogenesis lowers BMR as patients lose mass, intersecting with suppressed caloric intake.', correctOption: 0, explanation: 'Both true; lowered expenditure meets suppressed intake at equilibrium — not receptor desensitization.', reference: 'EQUILIBRIUM 9.1 [Known]: "BMR drops via adaptive thermogenesis"' },
  { id: 'ht-001-ar15', subtopic: 'Discordance — Anomalies', assertion: 'Serum lipase elevations on semaglutide are clinically benign in most patients.', reason: 'Semaglutide triggers intracellular zymogen auto-activation causing subclinical pancreatitis.', correctOption: 2, explanation: 'A is true (elevations are benign); R is false (enzyme release occurs without zymogen auto-activation cascade).', reference: 'DISCORDANCE 10.3 [Known]: "does not trigger the pathological activation cascade"' },
  { id: 'ht-001-ar16', subtopic: 'Lineage — Origin', assertion: 'Semaglutide was repositioned as a primary cardioprotective agent.', reason: 'CVOTs were designed as non-inferiority safety trials that serendipitously demonstrated CV superiority.', correctOption: 0, explanation: 'Both true; 2008 FDA mandate led to safety trials that unexpectedly showed benefit, shifting clinical positioning.', reference: 'LINEAGE 8.3 [Known]: "serendipitous finding of cardiovascular superiority forced the paradigm shift"' },
  { id: 'ht-001-ar17', subtopic: 'Second-Order — Cascade', assertion: 'Rapid semaglutide-induced weight loss may decrease bone mineral density.', reason: 'Weight loss mechanically unloads the skeleton, increasing bone resorption markers like CTX.', correctOption: 0, explanation: 'Both true; mechanical unloading from rapid weight loss triggers known bone resorption cascade.', reference: 'SECOND-ORDER 6.2 [Uncertain]: "increase in bone resorption markers (e.g., CTX) and a decrease in bone mineral density"' },
  { id: 'ht-001-ar18', subtopic: 'Falsifiability — Breakpoint', assertion: 'Weight-loss plateau on semaglutide can be broken in a metabolic ward setting.', reason: 'This would prove the plateau is thermodynamic equilibrium rather than central receptor desensitization.', correctOption: 0, explanation: 'Both true; enforced caloric deficit breaking plateau falsifies receptor desensitization hypothesis.', reference: 'FALSIFIABILITY 4.3 [Known]: "proves the plateau is a thermodynamic equilibrium... not central receptor desensitization"' }
].map(q => ({ ...q, type: 'assertion_reason' }));

// Remove any previously appended deconstruction items (idempotent re-run)
const existingIds = new Set(['ht-001-n101']);
const filtered = data.items.filter(it => {
  const n = parseInt((it.id.match(/-n(\d+)$/) || [])[1], 10);
  if (n >= 101) return false;
  if (it.id.match(/-q(2[7-9]|3[0-2])$/)) return false;
  if (it.id.match(/-tf(1[3-9]|18)$/)) return false;
  if (it.id.match(/-ar(1[3-9]|18)$/)) return false;
  return true;
});

data.items = [...filtered, ...notes, ...mcqs, ...trueFalse, ...ar];
data.subtitle = 'GLP-1 Receptor Agonist — PubMed Trials & Rigorous Mechanistic Deconstruction';
data.sourceFile = 'semaglutide_pubmed_qa_100.md; semaglutide_axiomatic_deconstruction.md';

fs.writeFileSync(OUT, JSON.stringify(data, null, 2) + '\n');

const counts = {};
data.items.forEach(it => { counts[it.type] = (counts[it.type] || 0) + 1; });
console.log('Updated:', OUT);
console.log('Counts:', counts, 'total:', data.items.length);
