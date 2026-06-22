#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-002_disorders_of_growth_and_development_diagnosis_and_treatment.json'
);

const notes = [
  {
    id: 'pe-cr-002-n1',
    subtopic: 'Definitions',
    title: 'Why severe short stature (< -3 SDS) demands urgent evaluation',
    content: 'Height below -2 SDS defines short stature, but values below -3 SDS or rapid crossing of percentiles suggest a higher likelihood of pathology and warrant prompt, comprehensive evaluation.',
    keyPoints: [
      'Short stature is < -2 SDS.',
      'Severe short stature is < -3 SDS.',
      'Lower SDS increases the likelihood of disease.'
    ],
    reference: 'Definition: < -2 SDS is short stature, while < -3 SDS signals higher-risk pathology.'
  },
  {
    id: 'pe-cr-002-n2',
    subtopic: 'Growth velocity',
    title: 'How growth velocity identifies pathologic short stature',
    content: 'A declining growth velocity over 6–12 months is often the earliest marker of endocrine or systemic disease, even when height percentile is still within a normal range.',
    keyPoints: [
      'Velocity decline precedes percentile crossing.',
      'Measure over at least 6 months.',
      'Compare with age- and sex-specific norms.'
    ],
    reference: 'Growth velocity: a sustained slowdown is an early signal of pathology.'
  },
  {
    id: 'pe-cr-002-n3',
    subtopic: 'Urgent GHD',
    title: 'Why red flags require urgent GHD assessment',
    content: 'Neonatal hypoglycemia, micropenis, midline defects, or symptoms of raised intracranial pressure raise concern for congenital or acquired GHD/MPHD and require expedited evaluation.',
    keyPoints: [
      'Neonatal hypoglycemia and micropenis are classic clues.',
      'Midline defects increase risk of pituitary disease.',
      'Headache or visual symptoms require urgent assessment.'
    ],
    reference: 'Urgent GHD clues: neonatal hypoglycemia, micropenis, midline defects, or ICP symptoms warrant rapid workup.'
  },
  {
    id: 'pe-cr-002-n4',
    subtopic: 'Baseline labs',
    title: 'How baseline labs screen systemic causes of short stature',
    content: 'Initial testing typically includes CBC, ESR/CRP, CMP, thyroid studies, and celiac screening, with additional tests guided by history and exam to rule out chronic disease.',
    keyPoints: [
      'Screen for anemia, inflammation, renal or liver disease.',
      'Check thyroid function early.',
      'Target further tests to symptoms.'
    ],
    reference: 'Baseline labs: CBC, inflammatory markers, CMP, thyroid, and celiac screening help exclude systemic causes.'
  },
  {
    id: 'pe-cr-002-n5',
    subtopic: 'Genetics',
    title: 'Why a karyotype is required in short girls',
    content: 'Short stature in girls can be the only presenting feature of Turner syndrome; karyotyping is essential even without dysmorphic features or pubertal delay.',
    keyPoints: [
      'Turner syndrome may present with isolated short stature.',
      'Karyotype is mandatory in girls with unexplained short stature.',
      'Early detection guides growth and cardiac care.'
    ],
    reference: 'Karyotype: all girls with unexplained short stature should be screened for Turner syndrome.'
  },
  {
    id: 'pe-cr-002-n6',
    subtopic: 'Bone age',
    title: 'How bone age refines diagnosis and timing',
    content: 'Bone age assesses skeletal maturity and remaining growth potential. Delayed bone age suggests endocrine delay or constitutional delay, while advanced bone age suggests early puberty or androgen excess.',
    keyPoints: [
      'Delayed bone age implies more growth potential.',
      'Advanced bone age suggests early maturation.',
      'Compare bone age to chronological and height age.'
    ],
    reference: 'Bone age: delayed in endocrine delay, advanced in precocious puberty or androgen excess.'
  },
  {
    id: 'pe-cr-002-n7',
    subtopic: 'IGF axis',
    title: 'Why the IGF-1–IGFBP-3–ALS ternary complex matters',
    content: 'Most circulating IGF-1 is bound in a ternary complex with IGFBP-3 and acid-labile subunit (ALS), which prolongs IGF-1 half-life and reflects integrated GH action.',
    keyPoints: [
      'IGF-1 circulates bound to IGFBP-3 and ALS.',
      'The ternary complex stabilizes IGF-1.',
      'Low IGF-1 can reflect reduced GH effect.'
    ],
    reference: 'IGF axis: IGF-1 bound to IGFBP-3 and ALS reflects overall GH activity.'
  },
  {
    id: 'pe-cr-002-n8',
    subtopic: 'IGF screening',
    title: 'How IGF-1 and IGFBP-3 are used in screening',
    content: 'Low IGF-1 and/or IGFBP-3 support GH deficiency but are influenced by nutrition, chronic disease, and age; normal values do not exclude GHD.',
    keyPoints: [
      'Low values support but do not confirm GHD.',
      'Nutrition and chronic illness suppress IGF-1.',
      'Interpret with auxology and GH testing.'
    ],
    reference: 'IGF-1/IGFBP-3: supportive screening markers that require clinical correlation.'
  },
  {
    id: 'pe-cr-002-n9',
    subtopic: 'Random GH',
    title: 'Why random GH levels are not diagnostic',
    content: 'GH secretion is pulsatile, so random levels can be low even in healthy children. Diagnosis relies on stimulation testing and clinical growth patterns.',
    keyPoints: [
      'GH pulses make random levels unreliable.',
      'Low random GH does not confirm GHD.',
      'Use stimulation tests for diagnosis.'
    ],
    reference: 'Random GH: pulsatile secretion makes single measurements unreliable.'
  },
  {
    id: 'pe-cr-002-n10',
    subtopic: 'Neurosecretory dwarfism',
    title: 'How neurosecretory dwarfism differs from classic GHD',
    content: 'Neurosecretory dwarfism features poor spontaneous GH secretion with normal stimulation tests, leading to low IGF-1 and growth failure despite preserved peak GH.',
    keyPoints: [
      'Overnight GH secretion is reduced.',
      'Stimulation tests may be normal.',
      'Growth failure and low IGF-1 persist.'
    ],
    reference: 'Neurosecretory dwarfism: low spontaneous GH with normal stimulation peaks.'
  },
  {
    id: 'pe-cr-002-n11',
    subtopic: 'GH testing',
    title: 'How to choose GH stimulation tests',
    content: 'Common stimulation tests include insulin-induced hypoglycemia, clonidine, glucagon, and arginine with or without GHRH, chosen based on safety, age, and local protocols.',
    keyPoints: [
      'IIH is the gold standard but needs close monitoring.',
      'Clonidine and glucagon are commonly used alternatives.',
      'Arginine-GHRH improves diagnostic yield.'
    ],
    reference: 'GH testing: IIH, clonidine, glucagon, and arginine-based protocols are standard options.'
  },
  {
    id: 'pe-cr-002-n12',
    subtopic: 'Priming',
    title: 'Why sex-steroid priming is used before GH testing',
    content: 'Priming with short-course sex steroids in prepubertal children reduces false-positive GHD by mimicking pubertal GH responsiveness.',
    keyPoints: [
      'Priming boosts GH response in prepubertal children.',
      'Reduces false-positive GHD diagnoses.',
      'Used when delayed puberty is expected.'
    ],
    reference: 'Priming: short-course sex steroids reduce false-positive GH testing in prepubertal children.'
  },
  {
    id: 'pe-cr-002-n13',
    subtopic: 'Two-test rule',
    title: 'Why two stimulation tests are recommended for GHD',
    content: 'Because GH testing has variability and false positives, most protocols require two abnormal stimulation tests in the appropriate clinical context before confirming GHD.',
    keyPoints: [
      'GH testing is variable and assay dependent.',
      'Two abnormal tests increase diagnostic confidence.',
      'Clinical auxology must support the diagnosis.'
    ],
    reference: 'Two-test rule: confirm GHD with two abnormal stimulation tests plus compatible growth data.'
  },
  {
    id: 'pe-cr-002-n14',
    subtopic: 'Cutoffs',
    title: 'How to interpret GH peak cutoffs in children',
    content: 'Peak GH cutoffs vary by assay; many centers use <10 ng/mL as abnormal, while some use <7 ng/mL for more stringent definitions.',
    keyPoints: [
      'Cutoffs are assay specific.',
      'Common thresholds are <10 or <7 ng/mL.',
      'Interpret with clinical context.'
    ],
    reference: 'GH cutoffs: <10 ng/mL (or <7 ng/mL with stringent assays) suggests GHD.'
  },
  {
    id: 'pe-cr-002-n15',
    subtopic: 'Cutoffs',
    title: 'How GHRH-arginine testing uses a higher cutoff',
    content: 'GHRH-arginine provokes higher GH peaks, so a lower diagnostic threshold is inappropriate; a peak ≤19 ng/mL is often used to define abnormality.',
    keyPoints: [
      'GHRH-arginine generates higher peaks.',
      'Use a higher cutoff to avoid misclassification.',
      'A peak ≤19 ng/mL is commonly applied.'
    ],
    reference: 'GHRH-arginine: a peak ≤19 ng/mL is a typical abnormal cutoff.'
  },
  {
    id: 'pe-cr-002-n16',
    subtopic: 'Imaging',
    title: 'How the MRI tetrad suggests congenital GHD',
    content: 'A classic tetrad includes hypoplastic anterior pituitary, ectopic posterior pituitary, thin or absent stalk, and midline brain defects, supporting congenital hypopituitarism.',
    keyPoints: [
      'Anterior pituitary hypoplasia is common.',
      'Posterior pituitary may be ectopic.',
      'Stalk interruption and midline defects are key clues.'
    ],
    reference: 'MRI tetrad: hypoplastic anterior pituitary, ectopic posterior lobe, absent stalk, and midline defects.'
  },
  {
    id: 'pe-cr-002-n17',
    subtopic: 'Septo-optic dysplasia',
    title: 'Why septo-optic dysplasia needs pituitary surveillance',
    content: 'Septo-optic dysplasia is associated with optic nerve hypoplasia and midline brain defects, and many patients develop evolving pituitary hormone deficiencies over time.',
    keyPoints: [
      'Optic nerve hypoplasia is a hallmark.',
      'Pituitary deficiencies may appear later.',
      'Longitudinal endocrine follow-up is required.'
    ],
    reference: 'Septo-optic dysplasia: optic nerve hypoplasia with evolving pituitary deficits needs ongoing monitoring.'
  },
  {
    id: 'pe-cr-002-n18',
    subtopic: 'rhGH therapy',
    title: 'How to dose rhGH and monitor IGF-1',
    content: 'rhGH dosing is weight based and adjusted to maintain IGF-1 within the age-appropriate range (often up to +2 SDS) while tracking growth velocity and adverse effects.',
    keyPoints: [
      'Dose rhGH by weight and adjust over time.',
      'Target IGF-1 in the normal to mildly high range.',
      'Monitor growth velocity and side effects.'
    ],
    reference: 'rhGH dosing: titrate by weight and keep IGF-1 within an acceptable SDS range.'
  },
  {
    id: 'pe-cr-002-n19',
    subtopic: 'rhGH response',
    title: 'How expected first-year response guides rhGH success',
    content: 'A strong response is typically seen in the first year of rhGH, with a marked rise in growth velocity; poor response suggests adherence, diagnosis, or dose issues.',
    keyPoints: [
      'Largest growth acceleration occurs in year one.',
      'Expect a clear velocity increase above baseline.',
      'Poor response requires reassessment.'
    ],
    reference: 'rhGH response: first-year growth acceleration is the key early marker of efficacy.'
  },
  {
    id: 'pe-cr-002-n20',
    subtopic: 'rhGH response',
    title: 'How to evaluate a suboptimal response to rhGH',
    content: 'Suboptimal growth requires review of adherence, injection technique, dosing, diagnosis, and comorbidities such as hypothyroidism or chronic disease.',
    keyPoints: [
      'Confirm adherence and injection technique.',
      'Recheck diagnosis and GH dosing.',
      'Screen for thyroid or systemic illness.'
    ],
    reference: 'Suboptimal rhGH response: assess adherence, dosing, diagnosis, and comorbid conditions.'
  },
  {
    id: 'pe-cr-002-n21',
    subtopic: 'Thyroid monitoring',
    title: 'Why free T4 must be monitored on rhGH',
    content: 'rhGH can increase peripheral conversion of T4 to T3 and unmask central hypothyroidism, so thyroid function should be checked before and after therapy initiation.',
    keyPoints: [
      'rhGH may lower free T4 levels.',
      'Central hypothyroidism can be unmasked.',
      'Treat hypothyroidism to optimize growth.'
    ],
    reference: 'Thyroid monitoring: rhGH can lower free T4 and unmask central hypothyroidism.'
  },
  {
    id: 'pe-cr-002-n22',
    subtopic: 'Puberty induction',
    title: 'How to induce puberty in MPHD',
    content: 'Puberty induction uses low-dose sex steroids with gradual escalation to mimic normal pubertal progression, while continuing GH and monitoring bone age.',
    keyPoints: [
      'Start with low-dose estrogen or testosterone.',
      'Escalate slowly over 2–3 years.',
      'Monitor growth and bone age.'
    ],
    reference: 'Puberty induction: low-dose sex steroids with gradual escalation in MPHD.'
  },
  {
    id: 'pe-cr-002-n23',
    subtopic: 'GnRH agonist',
    title: 'Why combine GnRH agonist with rhGH in early puberty',
    content: 'In children entering puberty with poor predicted height, GnRH agonists can slow epiphyseal fusion and, when combined with rhGH, preserve growth potential.',
    keyPoints: [
      'GnRH agonists delay pubertal progression.',
      'Combination therapy can preserve height potential.',
      'Best for early puberty with short predicted height.'
    ],
    reference: 'GnRH agonist + rhGH: delays epiphyseal fusion and can improve predicted adult height.'
  },
  {
    id: 'pe-cr-002-n24',
    subtopic: 'Discontinuation',
    title: 'When to discontinue rhGH therapy',
    content: 'rhGH is usually stopped when near-adult height is reached, growth velocity falls below ~2 cm/year, and bone age indicates epiphyseal fusion.',
    keyPoints: [
      'Stop near adult height or minimal velocity.',
      'Confirm epiphyseal fusion with bone age.',
      'Transition to adult evaluation if needed.'
    ],
    reference: 'Discontinuation: stop rhGH when growth velocity is minimal and bone age shows fusion.'
  },
  {
    id: 'pe-cr-002-n25',
    subtopic: 'Transition',
    title: 'How to transition adolescents and reassess the GH axis',
    content: 'After linear growth ends, GH is paused for a washout period and then retested to determine if adult GHD persists, guiding ongoing therapy.',
    keyPoints: [
      'Pause rhGH for a washout period.',
      'Retest the GH axis before adult dosing.',
      'Coordinate endocrine follow-up during transition.'
    ],
    reference: 'Transition: stop rhGH, allow washout, and retest to confirm adult GHD.'
  },
  {
    id: 'pe-cr-002-n26',
    subtopic: 'Adult GHD testing',
    title: 'How adult GHD testing is performed after transition',
    content: 'Adult GHD diagnosis relies on dynamic testing (insulin tolerance or glucagon tests, or macimorelin where available) rather than IGF-1 alone.',
    keyPoints: [
      'Dynamic tests are required for confirmation.',
      'IGF-1 alone is insufficient.',
      'Choose tests based on safety and availability.'
    ],
    reference: 'Adult GHD: dynamic testing is required; IGF-1 alone is not diagnostic.'
  },
  {
    id: 'pe-cr-002-n27',
    subtopic: 'GH insensitivity',
    title: 'Why Laron syndrome does not respond to GH',
    content: 'Laron syndrome is caused by GH receptor defects leading to high GH but very low IGF-1, so treatment requires recombinant IGF-1 rather than GH.',
    keyPoints: [
      'GH receptor defects cause GH resistance.',
      'IGF-1 levels are very low despite high GH.',
      'Treat with recombinant IGF-1.'
    ],
    reference: 'Laron syndrome: GH resistance with low IGF-1 requires IGF-1 replacement, not GH.'
  },
  {
    id: 'pe-cr-002-n28',
    subtopic: 'Tall stature',
    title: 'How to assess tall stature and familial tall variants',
    content: 'Tall stature evaluation includes growth velocity, pubertal timing, bone age, and screening for syndromic features; familial tall stature usually needs reassurance, with height-limiting therapy reserved for selected cases.',
    keyPoints: [
      'Assess growth pattern and bone age.',
      'Screen for Marfan, Sotos, or endocrine causes.',
      'Familial tall stature is typically benign.'
    ],
    reference: 'Tall stature: evaluate growth pattern and syndromic features; familial tall stature is usually benign.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-002-q1',
    subtopic: 'Definitions',
    question: 'Which height SDS most strongly indicates severe short stature requiring urgent evaluation?',
    options: [
      'Above -1 SDS',
      'Below -2 SDS',
      'Below -3 SDS',
      'Between -1 and -2 SDS'
    ],
    correctOption: 2,
    explanation: 'Height below -3 SDS is considered severe and increases the likelihood of pathology.',
    reference: 'Severe short stature: height < -3 SDS warrants urgent evaluation.'
  },
  {
    id: 'pe-cr-002-q2',
    subtopic: 'Growth velocity',
    question: 'A child’s height percentile is stable, but growth velocity drops to 3 cm/year. What is the best interpretation?',
    options: [
      'Normal variant, no evaluation needed',
      'Early sign of pathologic growth failure',
      'Expected pubertal growth spurt',
      'Measurement error only'
    ],
    correctOption: 1,
    explanation: 'A sustained decline in growth velocity is an early marker of pathology.',
    reference: 'Growth velocity: persistent slowing suggests disease even before percentile shift.'
  },
  {
    id: 'pe-cr-002-q3',
    subtopic: 'Urgent GHD',
    question: 'Which presentation most strongly warrants urgent evaluation for congenital GHD/MPHD?',
    options: [
      'Isolated delayed tooth eruption',
      'Neonatal hypoglycemia and micropenis',
      'Mild short stature with normal velocity',
      'Overweight with normal height'
    ],
    correctOption: 1,
    explanation: 'Neonatal hypoglycemia and micropenis are classic red flags for pituitary deficiency.',
    reference: 'Urgent GHD clues: neonatal hypoglycemia and micropenis require prompt workup.'
  },
  {
    id: 'pe-cr-002-q4',
    subtopic: 'Baseline labs',
    question: 'Which initial lab bundle best screens systemic causes of short stature?',
    options: [
      'CBC, ESR/CRP, CMP, thyroid studies, celiac screening',
      'Serum cortisol only',
      'Random GH only',
      'Serum calcium and phosphorus only'
    ],
    correctOption: 0,
    explanation: 'Broad screening labs help identify chronic systemic disease and endocrine causes.',
    reference: 'Baseline labs: CBC, inflammatory markers, CMP, thyroid, and celiac screening are typical.'
  },
  {
    id: 'pe-cr-002-q5',
    subtopic: 'Genetics',
    question: 'A 9-year-old girl with unexplained short stature has no dysmorphic features. What is the most important next test?',
    options: [
      'Bone density scan',
      'Karyotype for Turner syndrome',
      'Fasting insulin level',
      'Random GH level'
    ],
    correctOption: 1,
    explanation: 'Turner syndrome can present with isolated short stature; karyotype is mandatory.',
    reference: 'Karyotype: all girls with unexplained short stature should be screened for Turner syndrome.'
  },
  {
    id: 'pe-cr-002-q6',
    subtopic: 'Bone age',
    question: 'Delayed bone age compared with chronological age suggests:',
    options: [
      'Reduced growth potential',
      'Preserved growth potential with delayed maturation',
      'Completed epiphyseal fusion',
      'Skeletal dysplasia in all cases'
    ],
    correctOption: 1,
    explanation: 'Delayed bone age indicates remaining growth potential and delayed maturation.',
    reference: 'Bone age: delay implies additional growth potential and delayed maturation.'
  },
  {
    id: 'pe-cr-002-q7',
    subtopic: 'IGF axis',
    question: 'The main physiologic role of the IGF-1–IGFBP-3–ALS ternary complex is to:',
    options: [
      'Stimulate TSH secretion',
      'Prolong IGF-1 half-life in circulation',
      'Reduce GH secretion',
      'Increase cortisol production'
    ],
    correctOption: 1,
    explanation: 'The ternary complex stabilizes IGF-1 and prolongs its half-life.',
    reference: 'IGF axis: IGF-1 bound to IGFBP-3 and ALS is stabilized in circulation.'
  },
  {
    id: 'pe-cr-002-q8',
    subtopic: 'IGF screening',
    question: 'Which statement about IGF-1 and IGFBP-3 in short stature is most accurate?',
    options: [
      'Normal IGF-1 excludes GHD',
      'Low IGF-1 is diagnostic of GHD',
      'Low IGF-1 supports GHD but is nonspecific',
      'IGF-1 is unaffected by nutrition'
    ],
    correctOption: 2,
    explanation: 'Low IGF-1 supports GHD but is influenced by nutrition and chronic disease.',
    reference: 'IGF-1/IGFBP-3: supportive but nonspecific screening tests.'
  },
  {
    id: 'pe-cr-002-q9',
    subtopic: 'Random GH',
    question: 'Why is a random GH level not diagnostic of GHD?',
    options: [
      'GH is secreted in pulses',
      'GH cannot be measured in children',
      'GH levels are always high in GHD',
      'IGF-1 replaces GH testing'
    ],
    correctOption: 0,
    explanation: 'Pulsatile GH secretion makes single measurements unreliable.',
    reference: 'Random GH: pulsatile secretion makes single measurements unreliable.'
  },
  {
    id: 'pe-cr-002-q10',
    subtopic: 'Neurosecretory dwarfism',
    question: 'Which finding is most consistent with neurosecretory dwarfism?',
    options: [
      'Low spontaneous GH secretion with normal stimulation tests',
      'High IGF-1 with low GH',
      'Advanced bone age with tall stature',
      'Normal growth velocity'
    ],
    correctOption: 0,
    explanation: 'Neurosecretory dwarfism features low spontaneous GH but normal stimulated peaks.',
    reference: 'Neurosecretory dwarfism: low spontaneous GH with normal stimulation peaks.'
  },
  {
    id: 'pe-cr-002-q11',
    subtopic: 'GH testing',
    question: 'Which GH stimulation test is considered the gold standard in many centers?',
    options: [
      'Insulin-induced hypoglycemia',
      'Oral glucose tolerance test',
      'Dexamethasone suppression test',
      'ACTH stimulation test'
    ],
    correctOption: 0,
    explanation: 'Insulin-induced hypoglycemia is a classic gold standard test for GH reserve.',
    reference: 'GH testing: insulin-induced hypoglycemia is a gold standard test.'
  },
  {
    id: 'pe-cr-002-q12',
    subtopic: 'Priming',
    question: 'Sex-steroid priming before GH testing is mainly used to:',
    options: [
      'Increase false-positive diagnoses',
      'Improve GH response in prepubertal children',
      'Replace GH therapy',
      'Induce final adult height'
    ],
    correctOption: 1,
    explanation: 'Priming boosts GH responses in prepubertal children and reduces false positives.',
    reference: 'Priming: short-course sex steroids increase GH responsiveness before testing.'
  },
  {
    id: 'pe-cr-002-q13',
    subtopic: 'Two-test rule',
    question: 'Most protocols require two GH stimulation tests because:',
    options: [
      'GH assays are standardized worldwide',
      'Single tests are variable and can be falsely low',
      'Stimulation tests never cause side effects',
      'Two tests are cheaper than one'
    ],
    correctOption: 1,
    explanation: 'GH testing has variability; two abnormal tests improve diagnostic confidence.',
    reference: 'Two-test rule: confirms GHD by reducing false-positive results.'
  },
  {
    id: 'pe-cr-002-q14',
    subtopic: 'Cutoffs',
    question: 'Which peak GH result most often meets a diagnostic cutoff for GHD?',
    options: [
      '15 ng/mL',
      '12 ng/mL',
      '8 ng/mL',
      '20 ng/mL'
    ],
    correctOption: 2,
    explanation: 'Many centers use <10 ng/mL (and some <7 ng/mL) as abnormal.',
    reference: 'GH cutoffs: peaks below 10 ng/mL (or 7 ng/mL) are commonly abnormal.'
  },
  {
    id: 'pe-cr-002-q15',
    subtopic: 'Cutoffs',
    question: 'A GHRH-arginine test shows a peak GH of 17 ng/mL. How should this be interpreted?',
    options: [
      'Normal response',
      'Abnormal because the cutoff is ≤19 ng/mL',
      'Invalid because GHRH-arginine is not used',
      'Indicates acromegaly'
    ],
    correctOption: 1,
    explanation: 'GHRH-arginine produces higher peaks; a cutoff of ≤19 ng/mL is commonly used.',
    reference: 'GHRH-arginine: a peak ≤19 ng/mL is considered abnormal.'
  },
  {
    id: 'pe-cr-002-q16',
    subtopic: 'Imaging',
    question: 'Which MRI combination most supports congenital GHD?',
    options: [
      'Normal pituitary with empty sella',
      'Pituitary stalk interruption and ectopic posterior pituitary',
      'Pituitary hemorrhage only',
      'Macroadenoma with cavernous invasion'
    ],
    correctOption: 1,
    explanation: 'Stalk interruption with ectopic posterior pituitary is classic for congenital hypopituitarism.',
    reference: 'MRI tetrad: stalk interruption and ectopic posterior pituitary support congenital GHD.'
  },
  {
    id: 'pe-cr-002-q17',
    subtopic: 'Septo-optic dysplasia',
    question: 'A child with optic nerve hypoplasia and absent septum pellucidum is at highest risk for:',
    options: [
      'Isolated hyperthyroidism',
      'Evolving pituitary hormone deficiencies',
      'Renal tubular acidosis',
      'Primary adrenal insufficiency only'
    ],
    correctOption: 1,
    explanation: 'Septo-optic dysplasia is associated with evolving pituitary hormone deficits.',
    reference: 'Septo-optic dysplasia: optic nerve hypoplasia with evolving pituitary deficiencies.'
  },
  {
    id: 'pe-cr-002-q18',
    subtopic: 'rhGH therapy',
    question: 'Which monitoring target is most appropriate during rhGH therapy?',
    options: [
      'IGF-1 well above +3 SDS',
      'IGF-1 within the normal to mildly elevated range',
      'No IGF-1 monitoring is needed',
      'TSH suppression to zero'
    ],
    correctOption: 1,
    explanation: 'IGF-1 is monitored to stay within an acceptable age-adjusted range.',
    reference: 'rhGH monitoring: keep IGF-1 within a normal to mildly high SDS range.'
  },
  {
    id: 'pe-cr-002-q19',
    subtopic: 'rhGH response',
    question: 'Which observation best indicates a good first-year response to rhGH?',
    options: [
      'Growth velocity decreases compared with baseline',
      'Height velocity rises substantially above baseline',
      'No change in growth velocity',
      'Declining IGF-1 with therapy'
    ],
    correctOption: 1,
    explanation: 'The first year should show a marked increase in growth velocity.',
    reference: 'rhGH response: first-year growth acceleration is expected.'
  },
  {
    id: 'pe-cr-002-q20',
    subtopic: 'rhGH response',
    question: 'A child on rhGH has minimal growth response. What should be checked first?',
    options: [
      'Bone age only',
      'Adherence and injection technique',
      'Stop therapy immediately',
      'Start GnRH agonist'
    ],
    correctOption: 1,
    explanation: 'Nonadherence and technique issues are common causes of poor response.',
    reference: 'Suboptimal rhGH response: confirm adherence and injection technique early.'
  },
  {
    id: 'pe-cr-002-q21',
    subtopic: 'Thyroid monitoring',
    question: 'A child on rhGH has low free T4 with normal TSH. What is the best interpretation?',
    options: [
      'Laboratory error only',
      'Unmasking of central hypothyroidism',
      'Excess thyroid hormone replacement',
      'GH does not affect thyroid function'
    ],
    correctOption: 1,
    explanation: 'rhGH can unmask central hypothyroidism by lowering free T4.',
    reference: 'Thyroid monitoring: rhGH can lower free T4 and reveal central hypothyroidism.'
  },
  {
    id: 'pe-cr-002-q22',
    subtopic: 'Puberty induction',
    question: 'Puberty induction in MPHD is best achieved by:',
    options: [
      'Abrupt high-dose sex steroids',
      'Low-dose sex steroids with gradual escalation',
      'Stopping GH before puberty induction',
      'GnRH antagonists only'
    ],
    correctOption: 1,
    explanation: 'Gradual low-dose replacement mimics normal pubertal progression.',
    reference: 'Puberty induction: start low-dose sex steroids and increase gradually.'
  },
  {
    id: 'pe-cr-002-q23',
    subtopic: 'GnRH agonist',
    question: 'Which patient is most likely to benefit from GnRH agonist plus rhGH therapy?',
    options: [
      'A late pubertal child with tall predicted height',
      'Early pubertal child with short predicted adult height',
      'Adult with GH deficiency',
      'Prepubertal child with normal predicted height'
    ],
    correctOption: 1,
    explanation: 'Combination therapy is considered when early puberty threatens short adult height.',
    reference: 'GnRH agonist + rhGH: used in early puberty with short predicted height.'
  },
  {
    id: 'pe-cr-002-q24',
    subtopic: 'Discontinuation',
    question: 'Which criterion most supports stopping rhGH therapy?',
    options: [
      'Growth velocity <2 cm/year with bone age showing fusion',
      'IGF-1 within normal range',
      'Weight gain only',
      'Child reaches midparental height at age 8'
    ],
    correctOption: 0,
    explanation: 'rhGH is typically stopped when growth velocity is minimal and epiphyses are fused.',
    reference: 'Discontinuation: stop rhGH with minimal velocity and epiphyseal fusion.'
  },
  {
    id: 'pe-cr-002-q25',
    subtopic: 'Transition',
    question: 'After linear growth is complete, the GH axis should be reassessed by:',
    options: [
      'Continuing the pediatric GH dose indefinitely',
      'Stopping rhGH for a washout period and retesting',
      'Relying solely on IGF-1 levels',
      'Never retesting if childhood GHD was proven'
    ],
    correctOption: 1,
    explanation: 'A washout period followed by retesting determines whether adult GHD persists.',
    reference: 'Transition: stop rhGH for washout, then retest the GH axis.'
  },
  {
    id: 'pe-cr-002-q26',
    subtopic: 'GH insensitivity',
    question: 'Which treatment is most appropriate for Laron syndrome?',
    options: [
      'High-dose rhGH',
      'Recombinant IGF-1 therapy',
      'No treatment needed',
      'GnRH agonist therapy'
    ],
    correctOption: 1,
    explanation: 'Laron syndrome is GH receptor resistance, so IGF-1 replacement is required.',
    reference: 'Laron syndrome: treat GH insensitivity with recombinant IGF-1.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-002-tf1',
    subtopic: 'Definitions',
    statement: 'Height below -3 SDS is considered severe short stature and increases the likelihood of pathology.',
    correctAnswer: true,
    explanation: 'Severe short stature is a higher-risk category.',
    reference: 'Severe short stature: height < -3 SDS is high risk.'
  },
  {
    id: 'pe-cr-002-tf2',
    subtopic: 'Growth velocity',
    statement: 'A sustained decline in growth velocity can signal disease before height percentiles change.',
    correctAnswer: true,
    explanation: 'Velocity decline often precedes percentile crossing.',
    reference: 'Growth velocity: persistent slowing is an early warning sign.'
  },
  {
    id: 'pe-cr-002-tf3',
    subtopic: 'IGF screening',
    statement: 'Normal IGF-1 and IGFBP-3 completely exclude growth hormone deficiency.',
    correctAnswer: false,
    explanation: 'Normal values do not rule out GHD.',
    reference: 'IGF-1/IGFBP-3: normal levels do not exclude GHD.'
  },
  {
    id: 'pe-cr-002-tf4',
    subtopic: 'Priming',
    statement: 'Sex-steroid priming can reduce false-positive GH stimulation tests in prepubertal children.',
    correctAnswer: true,
    explanation: 'Priming enhances GH responsiveness.',
    reference: 'Priming: short-course sex steroids reduce false-positive GH tests.'
  },
  {
    id: 'pe-cr-002-tf5',
    subtopic: 'Two-test rule',
    statement: 'Most protocols require two abnormal GH stimulation tests to diagnose GHD.',
    correctAnswer: true,
    explanation: 'Two tests increase diagnostic confidence.',
    reference: 'Two-test rule: two abnormal tests plus clinical data are required.'
  },
  {
    id: 'pe-cr-002-tf6',
    subtopic: 'Cutoffs',
    statement: 'GHRH-arginine testing uses a higher cutoff because it provokes higher GH peaks.',
    correctAnswer: true,
    explanation: 'Higher peaks require a higher threshold.',
    reference: 'GHRH-arginine: higher cutoff is needed due to higher peaks.'
  },
  {
    id: 'pe-cr-002-tf7',
    subtopic: 'Imaging',
    statement: 'A waxing-and-waning pituitary size on MRI can occur with inflammatory hypophysitis and warrants follow-up.',
    correctAnswer: true,
    explanation: 'Fluctuating size suggests inflammatory or evolving lesions.',
    reference: 'Waxing-waning pituitary: fluctuating size suggests hypophysitis and needs follow-up imaging.'
  },
  {
    id: 'pe-cr-002-tf8',
    subtopic: 'GH insensitivity',
    statement: 'Laron syndrome is characterized by high GH levels and very low IGF-1.',
    correctAnswer: true,
    explanation: 'GH receptor defects lead to GH resistance and low IGF-1.',
    reference: 'Laron syndrome: high GH with low IGF-1 reflects GH receptor resistance.'
  },
  {
    id: 'pe-cr-002-tf9',
    subtopic: 'Pygmies',
    statement: 'Pygmy populations often have normal GH secretion but relative IGF-1 insensitivity or low IGF-1 levels.',
    correctAnswer: true,
    explanation: 'Many pygmy populations show GH-IGF axis variation with reduced IGF-1 effect.',
    reference: 'Pygmies: GH secretion can be normal with low IGF-1 activity.'
  },
  {
    id: 'pe-cr-002-tf10',
    subtopic: 'Tall stature',
    statement: 'Familial tall stature typically requires no treatment unless predicted height is extreme or psychosocial issues are significant.',
    correctAnswer: true,
    explanation: 'Most familial tall stature is benign and needs reassurance.',
    reference: 'Familial tall stature: usually benign, with treatment reserved for selected cases.'
  },
  {
    id: 'pe-cr-002-tf11',
    subtopic: 'FDA indications',
    statement: 'FDA indications for rhGH include conditions beyond classic GHD, such as Turner syndrome and SGA without catch-up.',
    correctAnswer: true,
    explanation: 'rhGH is approved for multiple non-GHD indications.',
    reference: 'FDA indications: rhGH is approved for several non-GHD conditions including Turner syndrome and SGA.'
  },
  {
    id: 'pe-cr-002-tf12',
    subtopic: 'Transition',
    statement: 'IGF-1 alone is sufficient to confirm adult GHD after transition.',
    correctAnswer: false,
    explanation: 'Dynamic testing is required to confirm adult GHD.',
    reference: 'Adult GHD: dynamic testing is required; IGF-1 alone is insufficient.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-002-ar1',
    subtopic: 'Definitions',
    assertion: 'Height below -3 SDS raises concern for underlying pathology.',
    reason: 'The probability of disease increases as SDS falls farther below the mean.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Severe short stature: lower SDS increases likelihood of pathology.'
  },
  {
    id: 'pe-cr-002-ar2',
    subtopic: 'Growth velocity',
    assertion: 'A decline in growth velocity can precede a fall in height percentile.',
    reason: 'Velocity is a sensitive early marker of growth disturbance.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Growth velocity: slowing is an early signal before percentile crossing.'
  },
  {
    id: 'pe-cr-002-ar3',
    subtopic: 'IGF screening',
    assertion: 'Low IGF-1 supports the diagnosis of GHD.',
    reason: 'IGF-1 levels are also reduced by malnutrition and chronic disease.',
    correctOption: 1,
    explanation: 'Both statements are true, but the reason shows why low IGF-1 is not specific.',
    reference: 'IGF-1: supportive for GHD but nonspecific due to nutritional and chronic disease effects.'
  },
  {
    id: 'pe-cr-002-ar4',
    subtopic: 'Priming',
    assertion: 'Sex-steroid priming before GH testing is recommended in prepubertal children.',
    reason: 'Priming increases GH responsiveness and reduces false-positive results.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Priming: sex steroids increase GH response and lower false positives.'
  },
  {
    id: 'pe-cr-002-ar5',
    subtopic: 'Two-test rule',
    assertion: 'Two abnormal GH stimulation tests are typically needed to confirm GHD.',
    reason: 'GH testing is variable and assay dependent.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Two-test rule: variability in GH testing requires two abnormal results.'
  },
  {
    id: 'pe-cr-002-ar6',
    subtopic: 'Cutoffs',
    assertion: 'A peak GH <10 ng/mL is often considered abnormal.',
    reason: 'Cutoffs vary by assay and clinical context.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason supports interpretation flexibility.',
    reference: 'GH cutoffs: <10 ng/mL is common, but assay and context matter.'
  },
  {
    id: 'pe-cr-002-ar7',
    subtopic: 'Septo-optic dysplasia',
    assertion: 'Septo-optic dysplasia requires long-term endocrine follow-up.',
    reason: 'Pituitary hormone deficiencies can evolve over time in this condition.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Septo-optic dysplasia: evolving pituitary deficits necessitate ongoing monitoring.'
  },
  {
    id: 'pe-cr-002-ar8',
    subtopic: 'rhGH response',
    assertion: 'Poor first-year growth response to rhGH should trigger reassessment.',
    reason: 'Adherence, dosing, diagnosis, or comorbidities may be limiting response.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Suboptimal response: reassess adherence, dosing, diagnosis, and comorbidities.'
  },
  {
    id: 'pe-cr-002-ar9',
    subtopic: 'Thyroid monitoring',
    assertion: 'Thyroid function should be monitored after starting rhGH.',
    reason: 'rhGH can lower free T4 and unmask central hypothyroidism.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Thyroid monitoring: rhGH can reduce free T4 and reveal central hypothyroidism.'
  },
  {
    id: 'pe-cr-002-ar10',
    subtopic: 'Transition',
    assertion: 'Adolescents completing growth should be retested for adult GHD.',
    reason: 'Some childhood GHD resolves, while persistent deficiency needs adult dosing.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Transition: retesting distinguishes persistent adult GHD from resolved childhood GHD.'
  },
  {
    id: 'pe-cr-002-ar11',
    subtopic: 'GH insensitivity',
    assertion: 'Laron syndrome is characterized by low IGF-1 despite high GH.',
    reason: 'GH receptor defects cause GH resistance.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Laron syndrome: GH receptor resistance leads to high GH and low IGF-1.'
  },
  {
    id: 'pe-cr-002-ar12',
    subtopic: 'FDA indications',
    assertion: 'rhGH is approved for several non-GHD conditions.',
    reason: 'Indications include Turner syndrome, CKD, Prader-Willi syndrome, and SGA without catch-up.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'FDA indications: rhGH is approved for Turner syndrome, CKD, Prader-Willi, and SGA without catch-up.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-002',
  book: 'clinical_rounds',
  chapterNo: '2',
  title: 'Disorders of Growth and Development: Diagnosis and Treatment',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/002_disorders_of_growth_and_development_diagnosis_and_treatment',
  items: [...notes, ...mcqs, ...trueFalse, ...assertionReason]
};

fs.writeFileSync(OUT, JSON.stringify(output, null, 2) + '\n');

const counts = output.items.reduce((acc, item) => {
  acc[item.type] = (acc[item.type] || 0) + 1;
  return acc;
}, {});
const whyHow = notes.filter(note => /^(Why|How)/.test(note.title)).length;
console.log('Written:', OUT);
console.log('Counts:', counts);
console.log('Notes Why/How:', `${whyHow}/${notes.length}`);
