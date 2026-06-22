#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-004_childhood_cushing_s_syndrome.json'
);

const notes = [
  {
    id: 'pe-cr-004-n1',
    subtopic: 'Etiology by age',
    title: 'Why exogenous glucocorticoids are the most common cause in children',
    content: 'Most pediatric Cushing syndrome is iatrogenic because systemic, inhaled, or topical steroids are widely used and can suppress the HPA axis.',
    keyPoints: [
      'Medication history is essential.',
      'High-dose or prolonged therapy is the usual culprit.',
      'Symptoms improve after tapering when safe.'
    ],
    reference: 'Exogenous glucocorticoids are the leading cause of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-n2',
    subtopic: 'Etiology by age',
    title: 'How endogenous causes shift with age',
    content: 'In very young children, adrenal causes are more frequent, whereas older children and adolescents more often have ACTH-dependent disease.',
    keyPoints: [
      'Adrenal tumors are typical in toddlers.',
      'Cushing disease dominates in adolescents.',
      'Age helps prioritize the differential.'
    ],
    reference: 'Endogenous etiologies vary with age, with adrenal causes earlier and pituitary causes later.'
  },
  {
    id: 'pe-cr-004-n3',
    subtopic: 'Cushing disease',
    title: 'Why Cushing disease is the most common endogenous cause in adolescents',
    content: 'Pituitary corticotroph adenomas become the predominant source of excess ACTH in later childhood, leading to ACTH-dependent hypercortisolism.',
    keyPoints: [
      'Adolescents often have pituitary microadenomas.',
      'ACTH levels are inappropriately normal or high.',
      'Cortisol loses diurnal variation.'
    ],
    reference: 'Cushing disease is the commonest endogenous cause in adolescents.'
  },
  {
    id: 'pe-cr-004-n4',
    subtopic: 'Adrenal tumors',
    title: 'Why adrenal tumors are more common in younger children',
    content: 'Adrenocortical tumors and hyperplasias present earlier in childhood and can cause ACTH-independent cortisol excess.',
    keyPoints: [
      'Often present before school age.',
      'ACTH is typically suppressed.',
      'Androgen excess may coexist.'
    ],
    reference: 'Adrenal tumors are a frequent endogenous cause in young children.'
  },
  {
    id: 'pe-cr-004-n5',
    subtopic: 'Clinical clues',
    title: 'Why growth failure is a key clue to pediatric Cushing syndrome',
    content: 'Excess cortisol impairs growth hormone secretion and bone formation, so linear growth slows despite weight gain.',
    keyPoints: [
      'Height velocity drops early.',
      'Weight gain continues or accelerates.',
      'Growth failure helps distinguish from simple obesity.'
    ],
    reference: 'Growth failure with weight gain is a hallmark of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-n6',
    subtopic: 'Clinical clues',
    title: 'How weight gain with declining height velocity narrows the differential',
    content: 'Cushing syndrome causes disproportionate weight gain with slowed linear growth, unlike most nutritional obesity.',
    keyPoints: [
      'BMI rises as height velocity falls.',
      'Central adiposity predominates.',
      'Consider endocrine causes in this pattern.'
    ],
    reference: 'Disproportionate weight gain plus slowed growth suggests hypercortisolism.'
  },
  {
    id: 'pe-cr-004-n7',
    subtopic: 'Puberty',
    title: 'How hypercortisolism affects pubertal development',
    content: 'Cortisol excess suppresses gonadotropin secretion and sex steroid production, leading to delayed or stalled puberty.',
    keyPoints: [
      'Delayed puberty is common.',
      'Menstrual irregularity may occur.',
      'Gonadal axis recovers after cure.'
    ],
    reference: 'Cortisol excess suppresses the gonadal axis and delays puberty.'
  },
  {
    id: 'pe-cr-004-n8',
    subtopic: 'Androgen excess',
    title: 'Why ACTH-independent adrenal disease can cause virilization',
    content: 'Adrenocortical tumors often co-secrete androgens, causing hirsutism, acne, or virilization along with hypercortisolism.',
    keyPoints: [
      'Androgen excess suggests adrenal source.',
      'Virilization is more typical in adrenal tumors.',
      'Check DHEAS and testosterone.'
    ],
    reference: 'Adrenal tumors can co-secrete androgens, producing virilization.'
  },
  {
    id: 'pe-cr-004-n9',
    subtopic: 'Metabolic effects',
    title: 'How cortisol excess drives hypertension and metabolic risk',
    content: 'Glucocorticoids raise vascular tone and promote insulin resistance, dyslipidemia, and hypertension.',
    keyPoints: [
      'Hypertension is common.',
      'Insulin resistance and dyslipidemia develop.',
      'Cardiometabolic risk improves after cure.'
    ],
    reference: 'Hypertension and metabolic syndrome are common in pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-n10',
    subtopic: 'Skeletal effects',
    title: 'Why bone fragility occurs in pediatric Cushing syndrome',
    content: 'Cortisol suppresses osteoblast activity and increases bone resorption, leading to osteopenia and fractures.',
    keyPoints: [
      'Vertebral compression fractures can occur.',
      'Bone age may lag despite weight gain.',
      'Recovery is gradual after treatment.'
    ],
    reference: 'Glucocorticoid excess causes osteopenia and fracture risk.'
  },
  {
    id: 'pe-cr-004-n11',
    subtopic: 'Skin findings',
    title: 'How cortisol excess causes striae and easy bruising',
    content: 'Protein catabolism thins the dermis and weakens capillaries, producing wide purple striae and bruising.',
    keyPoints: [
      'Striae are wide and violaceous.',
      'Skin is thin and fragile.',
      'Wound healing is delayed.'
    ],
    reference: 'Dermal thinning from cortisol causes violaceous striae and bruising.'
  },
  {
    id: 'pe-cr-004-n12',
    subtopic: 'Neuropsychiatric',
    title: 'Why mood and cognition change in pediatric Cushing syndrome',
    content: 'Cortisol affects hippocampal and limbic function, leading to irritability, depression, and impaired concentration.',
    keyPoints: [
      'Mood changes are common.',
      'Cognitive slowing may appear.',
      'Symptoms improve after normalization.'
    ],
    reference: 'Neuropsychiatric symptoms are frequent in pediatric hypercortisolism.'
  },
  {
    id: 'pe-cr-004-n13',
    subtopic: 'McCune-Albright',
    title: 'How McCune-Albright syndrome causes ACTH-independent Cushing syndrome',
    content: 'Activating GNAS mutations can cause autonomous adrenal cortisol production in infancy or early childhood.',
    keyPoints: [
      'ACTH is suppressed.',
      'Other endocrine hyperfunction may coexist.',
      'Symptoms can be episodic.'
    ],
    reference: 'McCune-Albright can produce ACTH-independent adrenal cortisol excess.'
  },
  {
    id: 'pe-cr-004-n14',
    subtopic: 'PPNAD',
    title: 'How primary pigmented nodular adrenocortical disease presents',
    content: 'PPNAD causes small pigmented adrenal nodules and intermittent or cyclic hypercortisolism, often with paradoxical dexamethasone response.',
    keyPoints: [
      'ACTH is low.',
      'Cortisol may fluctuate.',
      'Consider in familial syndromes.'
    ],
    reference: 'PPNAD causes nodular adrenal disease with cyclic cortisol excess.'
  },
  {
    id: 'pe-cr-004-n15',
    subtopic: 'Carney complex',
    title: 'Why Carney complex is linked to pediatric Cushing syndrome',
    content: 'Carney complex includes spotty skin pigmentation, cardiac myxomas, and endocrine tumors such as PPNAD, leading to ACTH-independent Cushing syndrome.',
    keyPoints: [
      'Look for lentigines and myxomas.',
      'PRKAR1A mutations are typical.',
      'Screen family members when suspected.'
    ],
    reference: 'Carney complex is associated with PPNAD and Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-n16',
    subtopic: 'Diagnostics',
    title: 'How to approach initial screening for pediatric Cushing syndrome',
    content: 'Confirm hypercortisolism with at least two abnormal screening tests before localization.',
    keyPoints: [
      'Use UFC, late-night salivary cortisol, or LDDST.',
      'Repeat tests to confirm.',
      'Consider stress and medications as confounders.'
    ],
    reference: 'Screening relies on multiple abnormal tests before localization.'
  },
  {
    id: 'pe-cr-004-n17',
    subtopic: 'Diagnostics',
    title: 'Why 24-hour urinary free cortisol is useful',
    content: 'UFC integrates cortisol secretion over a full day and avoids changes in binding proteins.',
    keyPoints: [
      'Reflects free cortisol production.',
      'Needs age-appropriate reference ranges.',
      'Collect at least two samples.'
    ],
    reference: 'UFC captures total daily free cortisol output.'
  },
  {
    id: 'pe-cr-004-n18',
    subtopic: 'Diagnostics',
    title: 'Why late-night salivary cortisol is sensitive',
    content: 'Normal children have a strong nocturnal cortisol nadir; loss of this nadir is an early sign of Cushing syndrome.',
    keyPoints: [
      'Detects loss of diurnal rhythm.',
      'Noninvasive collection.',
      'Useful in ambulatory testing.'
    ],
    reference: 'Loss of late-night cortisol nadir is a sensitive indicator.'
  },
  {
    id: 'pe-cr-004-n19',
    subtopic: 'Dexamethasone testing',
    title: 'How to dose pediatric overnight dexamethasone suppression',
    content: 'Overnight testing uses weight-based dexamethasone, typically 25 micrograms per kilogram (max 1 mg), with morning cortisol measurement.',
    keyPoints: [
      'Weight-based dosing is essential.',
      'Measure morning cortisol after the dose.',
      'Lack of suppression supports Cushing syndrome.'
    ],
    reference: 'Overnight dexamethasone testing uses pediatric weight-based dosing.'
  },
  {
    id: 'pe-cr-004-n20',
    subtopic: 'Dexamethasone testing',
    title: 'How to dose pediatric low-dose dexamethasone suppression',
    content: 'Low-dose testing uses about 20 to 30 micrograms per kilogram per day divided every 6 hours for 48 hours (max 2 mg/day).',
    keyPoints: [
      'Use divided dosing over 48 hours.',
      'Apply pediatric weight-based limits.',
      'Failure to suppress supports hypercortisolism.'
    ],
    reference: 'Low-dose dexamethasone testing requires pediatric weight-based dosing.'
  },
  {
    id: 'pe-cr-004-n21',
    subtopic: 'Dexamethasone testing',
    title: 'How high-dose dexamethasone helps localize ACTH-dependent disease',
    content: 'Pituitary ACTH secretion often suppresses with higher dexamethasone doses, whereas ectopic ACTH does not.',
    keyPoints: [
      'Suggests pituitary source if cortisol suppresses.',
      'Use after confirming ACTH-dependent disease.',
      'Interpret alongside clinical data.'
    ],
    reference: 'High-dose dexamethasone can distinguish pituitary from ectopic ACTH.'
  },
  {
    id: 'pe-cr-004-n22',
    subtopic: 'ACTH interpretation',
    title: 'How ACTH levels separate dependent from independent disease',
    content: 'Low ACTH implies adrenal autonomy, while normal or high ACTH suggests pituitary or ectopic sources.',
    keyPoints: [
      'Suppressed ACTH points to adrenal disease.',
      'Normal or high ACTH supports ACTH-dependent causes.',
      'Draw samples in the morning when possible.'
    ],
    reference: 'ACTH levels categorize Cushing syndrome as dependent or independent.'
  },
  {
    id: 'pe-cr-004-n23',
    subtopic: 'IPSS',
    title: 'Why inferior petrosal sinus sampling is used in pediatric Cushing disease',
    content: 'IPSS confirms a central ACTH source and helps lateralize secretion when MRI is equivocal.',
    keyPoints: [
      'Useful when MRI is negative or small lesions are seen.',
      'Central-to-peripheral ACTH gradient supports pituitary source.',
      'Requires experienced centers.'
    ],
    reference: 'IPSS confirms pituitary ACTH excess when imaging is unclear.'
  },
  {
    id: 'pe-cr-004-n24',
    subtopic: 'Imaging',
    title: 'How pituitary MRI is interpreted in pediatric Cushing syndrome',
    content: 'Microadenomas can be small or absent on MRI, so imaging is interpreted with biochemical data.',
    keyPoints: [
      'Normal MRI does not exclude Cushing disease.',
      'Dynamic contrast imaging improves detection.',
      'IPSS can clarify uncertain cases.'
    ],
    reference: 'Pituitary MRI may miss microadenomas, so biochemical confirmation is essential.'
  },
  {
    id: 'pe-cr-004-n25',
    subtopic: 'Management',
    title: 'Why transsphenoidal surgery is first-line for Cushing disease',
    content: 'Removing the pituitary adenoma offers the best chance for cure and rapid reversal of hypercortisolism.',
    keyPoints: [
      'Preferred definitive therapy for pituitary disease.',
      'Requires skilled pediatric pituitary surgeons.',
      'Remission is monitored with cortisol levels.'
    ],
    reference: 'Transsphenoidal surgery is the first-line treatment for Cushing disease.'
  },
  {
    id: 'pe-cr-004-n26',
    subtopic: 'Management',
    title: 'How radiotherapy is used after unsuccessful surgery',
    content: 'Pituitary radiotherapy is considered for persistent or recurrent disease when surgery fails or is not possible.',
    keyPoints: [
      'Delayed remission may occur.',
      'Monitor for hypopituitarism.',
      'Medical therapy can bridge to effect.'
    ],
    reference: 'Radiotherapy is a second-line option for persistent Cushing disease.'
  },
  {
    id: 'pe-cr-004-n27',
    subtopic: 'Postoperative care',
    title: 'Why postoperative hydrocortisone replacement is required',
    content: 'After curative surgery, the HPA axis is suppressed and patients need stress-dose hydrocortisone until recovery.',
    keyPoints: [
      'Low cortisol after surgery indicates remission.',
      'Provide physiologic and stress dosing.',
      'Taper based on recovery testing.'
    ],
    reference: 'Postoperative adrenal insufficiency requires hydrocortisone replacement.'
  },
  {
    id: 'pe-cr-004-n28',
    subtopic: 'Recovery',
    title: 'How growth recovers after cure of Cushing syndrome',
    content: 'Cortisol normalization allows catch-up growth, though recovery may take months and depends on age and pubertal stage.',
    keyPoints: [
      'Height velocity improves first.',
      'Puberty may resume after remission.',
      'Bone health recovery is gradual.'
    ],
    reference: 'Catch-up growth can occur after successful treatment.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-004-q1',
    subtopic: 'Etiology by age',
    question: 'What is the most common cause of Cushing syndrome in children overall?',
    options: [
      'Exogenous glucocorticoid therapy',
      'Pituitary corticotroph adenoma',
      'Adrenocortical carcinoma',
      'Ectopic ACTH secretion'
    ],
    correctOption: 0,
    explanation: 'Iatrogenic steroid exposure accounts for most pediatric cases.',
    reference: 'Exogenous glucocorticoids are the leading cause of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-q2',
    subtopic: 'Adrenal tumors',
    question: 'A 3-year-old with Cushing syndrome and virilization most likely has:',
    options: [
      'Adrenocortical tumor',
      'Pituitary microadenoma',
      'Ectopic ACTH secretion',
      'Exogenous steroid exposure'
    ],
    correctOption: 0,
    explanation: 'Young age plus virilization points to an adrenal tumor with androgen co-secretion.',
    reference: 'Adrenal tumors in young children often co-secrete androgens.'
  },
  {
    id: 'pe-cr-004-q3',
    subtopic: 'Clinical clues',
    question: 'Which growth pattern is most suggestive of pediatric Cushing syndrome?',
    options: [
      'Weight gain with falling height velocity',
      'Weight loss with increased height velocity',
      'Stable weight with accelerated growth',
      'Short stature with underweight'
    ],
    correctOption: 0,
    explanation: 'Disproportionate weight gain with slowed growth is characteristic.',
    reference: 'Growth failure with weight gain is a hallmark of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-q4',
    subtopic: 'Puberty',
    question: 'Which pubertal finding is most typical in a child with Cushing syndrome?',
    options: [
      'Delayed puberty',
      'Precocious puberty',
      'Isolated thelarche',
      'Normal puberty progression'
    ],
    correctOption: 0,
    explanation: 'Cortisol excess suppresses the gonadal axis and delays puberty.',
    reference: 'Cortisol excess suppresses the gonadal axis and delays puberty.'
  },
  {
    id: 'pe-cr-004-q5',
    subtopic: 'ACTH interpretation',
    question: 'Low morning ACTH in a child with confirmed hypercortisolism indicates:',
    options: [
      'ACTH-independent adrenal disease',
      'Pituitary Cushing disease',
      'Ectopic ACTH secretion',
      'Physiologic stress response'
    ],
    correctOption: 0,
    explanation: 'Suppressed ACTH suggests autonomous adrenal cortisol production.',
    reference: 'Low ACTH implies adrenal autonomy in Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-q6',
    subtopic: 'McCune-Albright',
    question: 'Cushing syndrome in McCune-Albright syndrome is usually due to:',
    options: [
      'Autonomous adrenal cortisol production',
      'Ectopic ACTH secretion',
      'Pituitary macroadenoma',
      'Chronic steroid therapy'
    ],
    correctOption: 0,
    explanation: 'Activating GNAS mutations cause ACTH-independent adrenal hyperfunction.',
    reference: 'McCune-Albright can produce ACTH-independent adrenal cortisol excess.'
  },
  {
    id: 'pe-cr-004-q7',
    subtopic: 'PPNAD',
    question: 'Primary pigmented nodular adrenocortical disease is best described as:',
    options: [
      'Small pigmented adrenal nodules with low ACTH',
      'Large adrenal carcinoma with high ACTH',
      'Pituitary adenoma with elevated ACTH',
      'Ectopic ACTH from a carcinoid tumor'
    ],
    correctOption: 0,
    explanation: 'PPNAD causes nodular adrenal disease and ACTH suppression.',
    reference: 'PPNAD causes nodular adrenal disease with cyclic cortisol excess.'
  },
  {
    id: 'pe-cr-004-q8',
    subtopic: 'Carney complex',
    question: 'Which clinical feature supports Carney complex in a child with Cushing syndrome?',
    options: [
      'Spotty skin pigmentation and cardiac myxoma',
      'Renal cysts and hematuria',
      'Severe scoliosis',
      'Congenital hypothyroidism'
    ],
    correctOption: 0,
    explanation: 'Carney complex involves lentigines and cardiac myxomas along with endocrine tumors.',
    reference: 'Carney complex includes spotty pigmentation, myxomas, and PPNAD.'
  },
  {
    id: 'pe-cr-004-q9',
    subtopic: 'Diagnostics',
    question: 'Which screening test best detects loss of diurnal cortisol variation?',
    options: [
      'Late-night salivary cortisol',
      'Random serum cortisol',
      'Morning ACTH level',
      'Plasma aldosterone'
    ],
    correctOption: 0,
    explanation: 'Late-night salivary cortisol detects loss of the normal nadir.',
    reference: 'Loss of late-night cortisol nadir is a sensitive indicator.'
  },
  {
    id: 'pe-cr-004-q10',
    subtopic: 'Diagnostics',
    question: '24-hour urinary free cortisol is helpful because it:',
    options: [
      'Reflects daily free cortisol secretion',
      'Measures cortisol-binding globulin levels',
      'Identifies ACTH sources',
      'Replaces all other screening tests'
    ],
    correctOption: 0,
    explanation: 'UFC integrates free cortisol over 24 hours.',
    reference: 'UFC captures total daily free cortisol output.'
  },
  {
    id: 'pe-cr-004-q11',
    subtopic: 'Dexamethasone testing',
    question: 'A typical pediatric overnight dexamethasone dose is:',
    options: [
      '25 micrograms/kg (max 1 mg)',
      '1 microgram/kg (max 0.1 mg)',
      '2 mg/kg (max 10 mg)',
      '5 mg fixed dose for all ages'
    ],
    correctOption: 0,
    explanation: 'Overnight testing uses a weight-based dose with a 1 mg maximum.',
    reference: 'Overnight dexamethasone testing uses pediatric weight-based dosing.'
  },
  {
    id: 'pe-cr-004-q12',
    subtopic: 'Dexamethasone testing',
    question: 'Low-dose dexamethasone suppression testing in children typically uses:',
    options: [
      '20 to 30 micrograms/kg/day divided every 6 hours (max 2 mg/day)',
      'Single 2 mg dose at bedtime',
      '10 micrograms/kg/day once daily (max 0.5 mg)',
      'Continuous infusion for 24 hours'
    ],
    correctOption: 0,
    explanation: 'Pediatric LDDST is weight-based and divided over 48 hours.',
    reference: 'Low-dose dexamethasone testing requires pediatric weight-based dosing.'
  },
  {
    id: 'pe-cr-004-q13',
    subtopic: 'Dexamethasone testing',
    question: 'High-dose dexamethasone suppression testing in children uses approximately:',
    options: [
      '120 micrograms/kg/day divided every 6 hours (max 8 mg/day)',
      '25 micrograms/kg once at night',
      '0.5 mg/day for 2 days',
      '2 mg/kg/day single dose'
    ],
    correctOption: 0,
    explanation: 'High-dose regimens use about 120 micrograms/kg/day divided dosing.',
    reference: 'High-dose dexamethasone can distinguish pituitary from ectopic ACTH.'
  },
  {
    id: 'pe-cr-004-q14',
    subtopic: 'ACTH interpretation',
    question: 'Which ACTH pattern supports ACTH-dependent Cushing syndrome?',
    options: [
      'Normal or high ACTH',
      'Suppressed ACTH',
      'Undetectable ACTH with high DHEAS',
      'Very low ACTH after surgery'
    ],
    correctOption: 0,
    explanation: 'ACTH-dependent disease has inappropriately normal or elevated ACTH.',
    reference: 'Normal or high ACTH supports ACTH-dependent causes.'
  },
  {
    id: 'pe-cr-004-q15',
    subtopic: 'IPSS',
    question: 'Inferior petrosal sinus sampling is most useful when:',
    options: [
      'Biochemical tests confirm Cushing syndrome but MRI is equivocal',
      'Exogenous steroid exposure is suspected',
      'Adrenal mass is clearly visible on CT',
      'ACTH is fully suppressed'
    ],
    correctOption: 0,
    explanation: 'IPSS confirms pituitary ACTH sources when imaging is unclear.',
    reference: 'IPSS confirms pituitary ACTH excess when imaging is unclear.'
  },
  {
    id: 'pe-cr-004-q16',
    subtopic: 'Imaging',
    question: 'A normal pituitary MRI in a child with ACTH-dependent Cushing syndrome means:',
    options: [
      'Cushing disease is still possible and requires further testing',
      'Pituitary disease is excluded',
      'The diagnosis is incorrect',
      'Adrenal carcinoma is certain'
    ],
    correctOption: 0,
    explanation: 'Microadenomas can be missed on MRI.',
    reference: 'Pituitary MRI may miss microadenomas, so biochemical confirmation is essential.'
  },
  {
    id: 'pe-cr-004-q17',
    subtopic: 'Management',
    question: 'First-line therapy for pediatric Cushing disease is:',
    options: [
      'Transsphenoidal pituitary surgery',
      'Pituitary radiotherapy',
      'Bilateral adrenalectomy',
      'Ketoconazole monotherapy'
    ],
    correctOption: 0,
    explanation: 'Surgical removal of the pituitary adenoma offers the best chance for cure.',
    reference: 'Transsphenoidal surgery is the first-line treatment for Cushing disease.'
  },
  {
    id: 'pe-cr-004-q18',
    subtopic: 'Management',
    question: 'Which option is appropriate for persistent hypercortisolism after pituitary surgery?',
    options: [
      'Radiotherapy with or without medical therapy',
      'Observation only',
      'Stop all cortisol-lowering therapy',
      'High-dose growth hormone'
    ],
    correctOption: 0,
    explanation: 'Radiotherapy and medical therapy are considered when surgery fails.',
    reference: 'Radiotherapy is a second-line option for persistent Cushing disease.'
  },
  {
    id: 'pe-cr-004-q19',
    subtopic: 'Postoperative care',
    question: 'After curative surgery for Cushing disease, the patient requires:',
    options: [
      'Hydrocortisone replacement until HPA recovery',
      'No steroid replacement because cortisol is normal',
      'Long-term dexamethasone therapy',
      'Immediate withdrawal of all steroids'
    ],
    correctOption: 0,
    explanation: 'The HPA axis is suppressed and needs temporary replacement.',
    reference: 'Postoperative adrenal insufficiency requires hydrocortisone replacement.'
  },
  {
    id: 'pe-cr-004-q20',
    subtopic: 'Recovery',
    question: 'Which statement best describes growth after successful treatment of Cushing syndrome?',
    options: [
      'Catch-up growth can occur over months',
      'Growth never recovers',
      'Growth immediately normalizes within days',
      'Only weight changes, not height'
    ],
    correctOption: 0,
    explanation: 'Growth velocity improves gradually after cure.',
    reference: 'Catch-up growth can occur after successful treatment.'
  },
  {
    id: 'pe-cr-004-q21',
    subtopic: 'Dexamethasone testing',
    question: 'High-dose dexamethasone is most likely to suppress cortisol in:',
    options: [
      'Pituitary Cushing disease',
      'Ectopic ACTH secretion',
      'Adrenal carcinoma',
      'Exogenous steroid exposure'
    ],
    correctOption: 0,
    explanation: 'Pituitary ACTH secretion often suppresses with high-dose dexamethasone.',
    reference: 'High-dose dexamethasone can distinguish pituitary from ectopic ACTH.'
  },
  {
    id: 'pe-cr-004-q22',
    subtopic: 'Adrenal tumors',
    question: 'Which laboratory pattern supports an adrenal tumor as the cause of Cushing syndrome?',
    options: [
      'Low ACTH with elevated adrenal androgens',
      'High ACTH with high cortisol',
      'Normal ACTH with normal androgens',
      'High ACTH with low cortisol'
    ],
    correctOption: 0,
    explanation: 'Adrenal tumors suppress ACTH and may co-secrete androgens.',
    reference: 'Adrenal tumors can co-secrete androgens, producing virilization.'
  },
  {
    id: 'pe-cr-004-q23',
    subtopic: 'Clinical clues',
    question: 'Which feature best distinguishes Cushing syndrome from simple obesity?',
    options: [
      'Growth deceleration',
      'Increased appetite',
      'Mild acanthosis nigricans',
      'Family history of obesity'
    ],
    correctOption: 0,
    explanation: 'Growth failure is atypical for nutritional obesity.',
    reference: 'Growth failure with weight gain is a hallmark of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-q24',
    subtopic: 'Skin findings',
    question: 'Which skin finding is most characteristic of pediatric Cushing syndrome?',
    options: [
      'Wide violaceous striae',
      'Cafe-au-lait macules',
      'Target lesions',
      'Punctate petechiae without bruising'
    ],
    correctOption: 0,
    explanation: 'Dermal thinning leads to broad purple striae.',
    reference: 'Dermal thinning from cortisol causes violaceous striae and bruising.'
  },
  {
    id: 'pe-cr-004-q25',
    subtopic: 'IPSS',
    question: 'During inferior petrosal sinus sampling, a central-to-peripheral ACTH gradient indicates:',
    options: [
      'Pituitary source of ACTH',
      'Ectopic ACTH secretion',
      'Adrenal cortisol excess',
      'Exogenous steroid use'
    ],
    correctOption: 0,
    explanation: 'A gradient supports a pituitary ACTH source.',
    reference: 'IPSS confirms pituitary ACTH excess when imaging is unclear.'
  },
  {
    id: 'pe-cr-004-q26',
    subtopic: 'Medical therapy',
    question: 'Which medication lowers cortisol by inhibiting adrenal steroidogenesis?',
    options: [
      'Ketoconazole',
      'Levothyroxine',
      'Hydrocortisone',
      'Desmopressin'
    ],
    correctOption: 0,
    explanation: 'Ketoconazole inhibits adrenal steroid synthesis and can be used preoperatively or for persistent disease.',
    reference: 'Steroidogenesis inhibitors can be used as medical therapy.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-004-tf1',
    subtopic: 'Etiology by age',
    statement: 'Exogenous glucocorticoid exposure is the most common cause of pediatric Cushing syndrome.',
    correctAnswer: true,
    explanation: 'Iatrogenic exposure accounts for most cases.',
    reference: 'Exogenous glucocorticoids are the leading cause of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-tf2',
    subtopic: 'Clinical clues',
    statement: 'Weight gain with slowed linear growth is a classic pattern in pediatric Cushing syndrome.',
    correctAnswer: true,
    explanation: 'Cortisol excess impairs growth while promoting weight gain.',
    reference: 'Growth failure with weight gain is a hallmark of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-tf3',
    subtopic: 'Puberty',
    statement: 'Hypercortisolism often delays pubertal progression.',
    correctAnswer: true,
    explanation: 'Cortisol suppresses gonadotropin secretion.',
    reference: 'Cortisol excess suppresses the gonadal axis and delays puberty.'
  },
  {
    id: 'pe-cr-004-tf4',
    subtopic: 'Diagnostics',
    statement: 'Loss of late-night cortisol nadir is an early sign of Cushing syndrome.',
    correctAnswer: true,
    explanation: 'Late-night salivary cortisol detects loss of circadian rhythm.',
    reference: 'Loss of late-night cortisol nadir is a sensitive indicator.'
  },
  {
    id: 'pe-cr-004-tf5',
    subtopic: 'Diagnostics',
    statement: 'A single normal screening test excludes pediatric Cushing syndrome.',
    correctAnswer: false,
    explanation: 'Multiple tests are recommended before excluding the diagnosis.',
    reference: 'Screening relies on multiple abnormal tests before localization.'
  },
  {
    id: 'pe-cr-004-tf6',
    subtopic: 'ACTH interpretation',
    statement: 'Suppressed ACTH suggests ACTH-independent adrenal disease.',
    correctAnswer: true,
    explanation: 'Low ACTH implies autonomous adrenal cortisol production.',
    reference: 'ACTH levels categorize Cushing syndrome as dependent or independent.'
  },
  {
    id: 'pe-cr-004-tf7',
    subtopic: 'IPSS',
    statement: 'Inferior petrosal sinus sampling is useful when MRI does not show a clear pituitary lesion.',
    correctAnswer: true,
    explanation: 'IPSS confirms central ACTH sources when imaging is unclear.',
    reference: 'IPSS confirms pituitary ACTH excess when imaging is unclear.'
  },
  {
    id: 'pe-cr-004-tf8',
    subtopic: 'Management',
    statement: 'Transsphenoidal surgery is the preferred initial therapy for Cushing disease.',
    correctAnswer: true,
    explanation: 'Surgery offers the best chance for cure.',
    reference: 'Transsphenoidal surgery is the first-line treatment for Cushing disease.'
  },
  {
    id: 'pe-cr-004-tf9',
    subtopic: 'Postoperative care',
    statement: 'Hydrocortisone replacement is usually needed after curative pituitary surgery.',
    correctAnswer: true,
    explanation: 'The HPA axis is suppressed after surgery.',
    reference: 'Postoperative adrenal insufficiency requires hydrocortisone replacement.'
  },
  {
    id: 'pe-cr-004-tf10',
    subtopic: 'Adrenal tumors',
    statement: 'Adrenocortical tumors may cause virilization due to androgen co-secretion.',
    correctAnswer: true,
    explanation: 'Androgen excess is common in adrenal tumors.',
    reference: 'Adrenal tumors can co-secrete androgens, producing virilization.'
  },
  {
    id: 'pe-cr-004-tf11',
    subtopic: 'Carney complex',
    statement: 'Carney complex is associated with PPNAD and Cushing syndrome.',
    correctAnswer: true,
    explanation: 'PPNAD is a classic endocrine tumor in Carney complex.',
    reference: 'Carney complex is associated with PPNAD and Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-tf12',
    subtopic: 'Recovery',
    statement: 'Catch-up growth can occur after successful treatment of pediatric Cushing syndrome.',
    correctAnswer: true,
    explanation: 'Growth velocity improves after cortisol normalization.',
    reference: 'Catch-up growth can occur after successful treatment.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-004-ar1',
    subtopic: 'Clinical clues',
    assertion: 'Growth failure is a key clue to pediatric Cushing syndrome.',
    reason: 'Excess cortisol suppresses growth hormone secretion and bone formation.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Growth failure with weight gain is a hallmark of pediatric Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-ar2',
    subtopic: 'Diagnostics',
    assertion: 'Late-night salivary cortisol is a sensitive screening test.',
    reason: 'Normal children have a nocturnal cortisol nadir that is lost in Cushing syndrome.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the sensitivity.',
    reference: 'Loss of late-night cortisol nadir is a sensitive indicator.'
  },
  {
    id: 'pe-cr-004-ar3',
    subtopic: 'Dexamethasone testing',
    assertion: 'Low-dose dexamethasone suppression testing uses weight-based dosing in children.',
    reason: 'Pediatric dosing must account for body size and has a daily maximum.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the approach.',
    reference: 'Low-dose dexamethasone testing requires pediatric weight-based dosing.'
  },
  {
    id: 'pe-cr-004-ar4',
    subtopic: 'ACTH interpretation',
    assertion: 'Suppressed ACTH suggests ACTH-independent Cushing syndrome.',
    reason: 'Autonomous adrenal cortisol production feeds back to lower ACTH.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the mechanism.',
    reference: 'ACTH levels categorize Cushing syndrome as dependent or independent.'
  },
  {
    id: 'pe-cr-004-ar5',
    subtopic: 'IPSS',
    assertion: 'Inferior petrosal sinus sampling helps confirm pituitary ACTH excess.',
    reason: 'A central-to-peripheral ACTH gradient indicates a pituitary source.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the rationale.',
    reference: 'IPSS confirms pituitary ACTH excess when imaging is unclear.'
  },
  {
    id: 'pe-cr-004-ar6',
    subtopic: 'Management',
    assertion: 'Transsphenoidal surgery is the first-line therapy for Cushing disease.',
    reason: 'Removing the pituitary adenoma offers the best chance for cure.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the choice.',
    reference: 'Transsphenoidal surgery is the first-line treatment for Cushing disease.'
  },
  {
    id: 'pe-cr-004-ar7',
    subtopic: 'Postoperative care',
    assertion: 'Hydrocortisone replacement is required after curative pituitary surgery.',
    reason: 'The HPA axis remains suppressed until it recovers.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the need.',
    reference: 'Postoperative adrenal insufficiency requires hydrocortisone replacement.'
  },
  {
    id: 'pe-cr-004-ar8',
    subtopic: 'Adrenal tumors',
    assertion: 'Adrenal tumors can cause virilization in pediatric Cushing syndrome.',
    reason: 'These tumors may co-secrete adrenal androgens.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the finding.',
    reference: 'Adrenal tumors can co-secrete androgens, producing virilization.'
  },
  {
    id: 'pe-cr-004-ar9',
    subtopic: 'Carney complex',
    assertion: 'Carney complex is associated with Cushing syndrome.',
    reason: 'PPNAD is part of the Carney complex spectrum.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the association.',
    reference: 'Carney complex is associated with PPNAD and Cushing syndrome.'
  },
  {
    id: 'pe-cr-004-ar10',
    subtopic: 'Dexamethasone testing',
    assertion: 'High-dose dexamethasone can suppress cortisol in pituitary Cushing disease.',
    reason: 'Pituitary ACTH secretion often remains partially feedback sensitive.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the response.',
    reference: 'High-dose dexamethasone can distinguish pituitary from ectopic ACTH.'
  },
  {
    id: 'pe-cr-004-ar11',
    subtopic: 'Diagnostics',
    assertion: 'Multiple screening tests are recommended before diagnosing Cushing syndrome.',
    reason: 'Individual tests can be confounded by stress or medication effects.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the approach.',
    reference: 'Screening relies on multiple abnormal tests before localization.'
  },
  {
    id: 'pe-cr-004-ar12',
    subtopic: 'Recovery',
    assertion: 'Catch-up growth can follow successful treatment of pediatric Cushing syndrome.',
    reason: 'Cortisol normalization allows recovery of growth hormone action.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the recovery.',
    reference: 'Catch-up growth can occur after successful treatment.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-004',
  book: 'clinical_rounds',
  chapterNo: '4',
  title: 'Childhood Cushing\'s Syndrome',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/004_childhood_cushing_s_syndrome',
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
