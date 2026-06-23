#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-006_precocious_puberty.json'
);

const notes = [
  {
    id: 'pe-cr-006-n1',
    subtopic: 'Definition',
    title: 'Why precocious puberty is defined before age 8 in girls and 9 in boys',
    content: 'Population data show that pubertal onset clusters around 10.5 years in girls and 11.5 years in boys, so ages below those means by about 2.5 SD signal abnormal early activation.',
    keyPoints: [
      'The cutoff reflects statistical deviation from normal timing.',
      'Girls <8 years and boys <9 years warrant evaluation.',
      'Cutoffs help identify pathologic causes early.'
    ],
    reference: 'Precocious puberty is defined as secondary sexual characteristics before 8 years in girls or 9 years in boys.'
  },
  {
    id: 'pe-cr-006-n2',
    subtopic: 'Definition',
    title: 'How accelerated puberty differs from precocious puberty',
    content: 'Accelerated puberty starts at a normal age but progresses unusually fast, so it still needs evaluation even though the onset is not early.',
    keyPoints: [
      'Onset is within normal limits.',
      'Progression is rapid and may be nonsequential.',
      'Underlying lesions can drive the speed.'
    ],
    reference: 'Accelerated puberty means normal-age onset with rapid progression that still needs evaluation.'
  },
  {
    id: 'pe-cr-006-n3',
    subtopic: 'Clinical impact',
    title: 'Why early puberty needs evaluation beyond reassurance',
    content: 'Early sex steroid exposure can reduce adult height and cause psychosocial distress, and evaluation helps detect structural lesions or hormone-secreting tumors.',
    keyPoints: [
      'Advanced bone age threatens final height.',
      'Psychosocial effects can be significant.',
      'Organic causes must be excluded.'
    ],
    reference: 'Children with early puberty should be evaluated to prevent height loss, psychosocial issues, and missed lesions.'
  },
  {
    id: 'pe-cr-006-n4',
    subtopic: 'Classification',
    title: 'How GDPP differs from GIPP clinically',
    content: 'GDPP reflects early HPG-axis activation with sequential, progressive pubertal events, whereas GIPP is sex steroid excess without HPG reactivation and often shows discordant staging.',
    keyPoints: [
      'GDPP is HPG-axis driven.',
      'GIPP is independent of gonadotropins.',
      'Discordant staging suggests GIPP.'
    ],
    reference: 'GDPP is sequential and HPG-axis driven; GIPP is steroid excess with nonsequential progression.'
  },
  {
    id: 'pe-cr-006-n5',
    subtopic: 'Classification',
    title: 'Why isosexual and heterosexual precocity are separated',
    content: 'Isosexual precocity matches chromosomal sex, while heterosexual precocity reflects opposite-sex characteristics and is always gonadotropin independent.',
    keyPoints: [
      'Isosexual: puberty consistent with gonadal sex.',
      'Heterosexual: discordant traits.',
      'Heterosexual precocity implies peripheral steroids.'
    ],
    reference: 'Isosexual precocity aligns with gonadal sex, whereas heterosexual precocity is discordant and gonadotropin independent.'
  },
  {
    id: 'pe-cr-006-n6',
    subtopic: 'Normal variants',
    title: 'How premature thelarche is distinguished from true precocity',
    content: 'Isolated premature thelarche is nonprogressive, lacks other secondary sexual characteristics, and shows normal growth velocity and bone age.',
    keyPoints: [
      'Breast changes are mild and stable.',
      'No pubarche or uterine enlargement.',
      'Bone age remains appropriate.'
    ],
    reference: 'Premature thelarche is nonprogressive with normal growth and bone age.'
  },
  {
    id: 'pe-cr-006-n7',
    subtopic: 'Normal variants',
    title: 'Why premature thelarche often remains limited to B2–B3',
    content: 'Breast maturation needs both estrogen and progesterone; isolated thelarche has estrogen exposure without pubertal progesterone, so maturation stalls early.',
    keyPoints: [
      'Estrogen drives ductal growth.',
      'Progesterone is required for full maturation.',
      'Lack of progesterone limits progression.'
    ],
    reference: 'Isolated premature thelarche has estrogen exposure without pubertal progesterone, limiting breast staging.'
  },
  {
    id: 'pe-cr-006-n8',
    subtopic: 'Androgen physiology',
    title: 'How adrenarche differs from pubarche',
    content: 'Adrenarche is a biochemical rise in adrenal androgens around age 6, whereas pubarche is the clinical appearance of hair and body odor, usually closer to age 8.',
    keyPoints: [
      'Adrenarche is hormonal.',
      'Pubarche is clinical hair development.',
      'Conversion to testosterone drives hair changes.'
    ],
    reference: 'Adrenarche is biochemical adrenal androgen rise; pubarche is clinical hair development.'
  },
  {
    id: 'pe-cr-006-n9',
    subtopic: 'Premature pubarche',
    title: 'Why bone age guides evaluation of premature pubarche',
    content: 'Isolated pubarche with minimal bone age advancement suggests benign premature adrenarche, while significant advancement or virilization signals pathologic androgen excess.',
    keyPoints: [
      'Bone age >2.5 SD prompts evaluation.',
      'Virilization suggests pathologic causes.',
      'Obesity-related adrenarche is common.'
    ],
    reference: 'Bone age and androgenization determine whether premature pubarche needs full workup.'
  },
  {
    id: 'pe-cr-006-n10',
    subtopic: 'Diagnostics',
    title: 'How basal and stimulated LH identify GDPP in girls',
    content: 'Basal LH at or above 0.3 IU/L indicates HPG-axis activation, and a pubertal LH response to GnRH agonist confirms GDPP when basal values are low.',
    keyPoints: [
      'Basal LH ≥0.3 IU/L supports GDPP.',
      'Triptorelin-stimulated LH ≥8 IU/L is pubertal.',
      'Estradiol response can support diagnosis.'
    ],
    reference: 'Basal LH and stimulated LH thresholds are used to confirm GDPP in girls.'
  },
  {
    id: 'pe-cr-006-n11',
    subtopic: 'Diagnostics',
    title: 'Why LH response is preferred over FSH for diagnosing GDPP',
    content: 'FSH response to GnRH occurs across ages, while LH response reflects true reactivation of the GnRH pulse generator.',
    keyPoints: [
      'FSH rises even in prepubertal children.',
      'LH surge signifies HPG-axis activation.',
      'LH is more tightly neuroendocrine regulated.'
    ],
    reference: 'LH response to GnRH, not FSH, indicates activation of the GnRH pulse generator.'
  },
  {
    id: 'pe-cr-006-n12',
    subtopic: 'Imaging',
    title: 'How pelvic ultrasound supports puberty assessment in girls',
    content: 'Uterine length above 3.5 cm, pubertal uterine shape, and ovarian volume above 2.8 ml indicate estrogen exposure and onset of puberty.',
    keyPoints: [
      'Uterine length >3.5 cm is significant.',
      'Ovarian volume ≥2.8 ml suggests puberty.',
      'Endometrial echo supports estrogen effect.'
    ],
    reference: 'Pelvic ultrasound parameters indicate estrogen exposure and pubertal onset in girls.'
  },
  {
    id: 'pe-cr-006-n13',
    subtopic: 'Imaging',
    title: 'Why ovarian cyst patterns help separate GDPP from GIPP',
    content: 'Multiple small follicles favor GDPP, while a single large follicular cyst suggests GIPP from autonomous ovarian estrogen production.',
    keyPoints: [
      'Multiple cysts imply HPG-driven stimulation.',
      'Single large cyst points to GIPP.',
      'Cyst size >9 mm favors GIPP.'
    ],
    reference: 'Multiple small follicles suggest GDPP, whereas a large solitary cyst suggests GIPP.'
  },
  {
    id: 'pe-cr-006-n14',
    subtopic: 'Neuroimaging',
    title: 'How neuroimaging is prioritized in precocious puberty',
    content: 'MRI is recommended for all children with GDPP, especially boys, girls with onset before 6 years, neurological symptoms, or rapid progression.',
    keyPoints: [
      'Boys have higher rates of CNS lesions.',
      'Girls <6 years have higher yield.',
      'Gelastic seizures or visual symptoms demand imaging.'
    ],
    reference: 'MRI is indicated in GDPP, particularly in boys, very young girls, or those with neurologic signs.'
  },
  {
    id: 'pe-cr-006-n15',
    subtopic: 'Hypothalamic hamartoma',
    title: 'Why hypothalamic hamartomas trigger GDPP',
    content: 'Ectopic GnRH neurons within hamartomas escape normal inhibition and release GnRH pulses, prematurely activating the HPG axis.',
    keyPoints: [
      'Accessory GnRH neurons are autonomous.',
      'GnRH pulsatility reactivates early.',
      'HPG-axis becomes prematurely active.'
    ],
    reference: 'Hypothalamic hamartomas contain ectopic GnRH neurons that drive early HPG activation.'
  },
  {
    id: 'pe-cr-006-n16',
    subtopic: 'Hypothalamic hamartoma',
    title: 'How gelastic seizures point to hypothalamic hamartoma',
    content: 'Sudden episodes of laughter with autonomic features and no loss of awareness are classic for hamartoma-related gelastic seizures in young children.',
    keyPoints: [
      'Episodes are brief and stereotyped.',
      'Autonomic signs often accompany laughter.',
      'Hamartoma is the leading cause.'
    ],
    reference: 'Gelastic seizures are most commonly caused by hypothalamic hamartoma.'
  },
  {
    id: 'pe-cr-006-n17',
    subtopic: 'McCune-Albright syndrome',
    title: 'Why MAS causes gonadotropin-independent precocity',
    content: 'Constitutive GNAS activation drives autonomous ovarian cysts and estrogen production, leading to episodic vaginal bleeding and premature thelarche.',
    keyPoints: [
      'Autonomous ovarian steroidogenesis occurs.',
      'Breast changes can wax and wane.',
      'Café-au-lait spots and fibrous dysplasia are clues.'
    ],
    reference: 'MAS causes autonomous ovarian cysts and estrogen excess leading to GIPP.'
  },
  {
    id: 'pe-cr-006-n18',
    subtopic: 'Familial testotoxicosis',
    title: 'How familial testotoxicosis produces early virilization',
    content: 'Activating LH receptor mutations trigger testosterone secretion independent of LH, leading to penile growth, pubarche, and enlarged testes in boys.',
    keyPoints: [
      'LH receptor gain-of-function drives testosterone.',
      'LH is suppressed despite virilization.',
      'Testicular size increases from intratesticular testosterone.'
    ],
    reference: 'Familial testotoxicosis is LH receptor activation causing LH-independent testosterone production.'
  },
  {
    id: 'pe-cr-006-n19',
    subtopic: 'Mixed precocity',
    title: 'Why mixed precocious puberty develops in chronic GIPP',
    content: 'Long-standing sex steroid excess advances bone age and primes the HPG axis, so treatment of GIPP can unmask GDPP that needs GnRH agonist therapy.',
    keyPoints: [
      'Advanced bone age predicts HPG activation.',
      'GIPP therapy can unmask GDPP.',
      'Both conditions require treatment.'
    ],
    reference: 'Mixed precocity is GDPP superimposed on GIPP after prolonged steroid exposure.'
  },
  {
    id: 'pe-cr-006-n20',
    subtopic: 'Evaluation',
    title: 'How boys with precocious puberty are evaluated',
    content: 'Evaluation includes basal LH and testosterone, GnRH stimulation if needed, and targeted imaging such as MRI brain or abdominal imaging to find etiology.',
    keyPoints: [
      'Basal LH ≥0.3 IU/L suggests GDPP.',
      'Testosterone elevation guides etiology.',
      'Imaging identifies CNS or adrenal tumors.'
    ],
    reference: 'Boys need basal LH/testosterone, stimulation testing, and imaging to define GDPP vs GIPP.'
  },
  {
    id: 'pe-cr-006-n21',
    subtopic: 'Evaluation',
    title: 'How girls with isosexual precocity are evaluated',
    content: 'Basal LH and estradiol guide classification, GnRH agonist testing confirms GDPP, and pelvic ultrasound assesses uterine and ovarian maturation.',
    keyPoints: [
      'Basal LH and estradiol are first-line.',
      'GnRH stimulation confirms HPG activation.',
      'Pelvic ultrasound documents estrogen effect.'
    ],
    reference: 'Girls with isosexual precocity are assessed with gonadotropins, estradiol, and pelvic ultrasound.'
  },
  {
    id: 'pe-cr-006-n22',
    subtopic: 'Therapy',
    title: 'Why GnRH agonists are first-line for GDPP',
    content: 'GnRH agonists reliably suppress the HPG axis, regress pubertal changes, and help preserve adult height, especially when started early.',
    keyPoints: [
      'They provide reversible HPG suppression.',
      'Regression of secondary sex traits occurs.',
      'Best height benefit when started young.'
    ],
    reference: 'GnRH agonists are the preferred treatment for GDPP because they effectively suppress HPG-axis activity.'
  },
  {
    id: 'pe-cr-006-n23',
    subtopic: 'Therapy',
    title: 'How GnRH agonist therapy works and why flare can occur',
    content: 'Initial receptor stimulation causes a transient rise in gonadotropins and steroids, followed by receptor downregulation and sustained suppression.',
    keyPoints: [
      'Flare occurs in the first 1–2 weeks.',
      'Suppression follows within weeks.',
      'Depot formulations are used monthly or quarterly.'
    ],
    reference: 'GnRH agonists cause an initial flare then downregulate receptors and suppress the HPG axis.'
  },
  {
    id: 'pe-cr-006-n24',
    subtopic: 'Therapy monitoring',
    title: 'How to monitor response to GnRH agonist therapy',
    content: 'Monitoring includes Tanner staging, growth velocity, basal and stimulated LH with estradiol or testosterone, and annual bone age assessment.',
    keyPoints: [
      'Clinical regression should be evident by 6–12 months.',
      'Growth velocity should slow.',
      'Hormonal suppression confirms adequate dosing.'
    ],
    reference: 'Monitoring includes clinical progression, growth velocity, hormone suppression, and bone age.'
  },
  {
    id: 'pe-cr-006-n25',
    subtopic: 'Therapy discontinuation',
    title: 'Why stopping GnRH agonists is usually timed around age 11',
    content: 'Beyond about 11 years, continued suppression may reduce final height gain because pubertal growth depends on sex steroids, so therapy is usually stopped when age-appropriate.',
    keyPoints: [
      'Height gain diminishes after ~11 years.',
      'Pubertal timing should be age appropriate.',
      'Psychosocial goals also guide timing.'
    ],
    reference: 'GnRH agonists are commonly discontinued around 11 years when further height benefit is minimal.'
  },
  {
    id: 'pe-cr-006-n26',
    subtopic: 'Therapy recovery',
    title: 'How the HPG axis recovers after stopping GnRH agonists',
    content: 'Gonadotropins rise within months, pubertal progression resumes in 3–6 months, and menses typically returns within 1–1.5 years in girls.',
    keyPoints: [
      'Recovery is reversible and expected.',
      'Girls resume menses within about a year.',
      'Boys progress more slowly.'
    ],
    reference: 'HPG-axis activity typically recovers within a year after stopping GnRH agonists.'
  },
  {
    id: 'pe-cr-006-n27',
    subtopic: 'Bone health',
    title: 'Why GnRH agonists do not compromise peak bone mass',
    content: 'Long-term data show normal accrual of bone mass, but adequate calcium and vitamin D are important during therapy.',
    keyPoints: [
      'Bone density normalizes after therapy.',
      'Calcium and vitamin D support bone health.',
      'Monitoring is still prudent.'
    ],
    reference: 'GnRH agonist therapy does not impair peak bone mass, but calcium and vitamin D should be optimized.'
  },
  {
    id: 'pe-cr-006-n28',
    subtopic: 'GIPP treatment',
    title: 'How gonadotropin-independent precocity is treated',
    content: 'Management targets the underlying source of sex steroids, including surgery for tumors, glucocorticoids for CAH, or aromatase inhibitors/MDPA for MAS.',
    keyPoints: [
      'Tumors require surgical management.',
      'CAH responds to steroid replacement.',
      'MAS often needs antiestrogen therapy.'
    ],
    reference: 'GIPP treatment is etiology-specific, including tumor removal, CAH therapy, or antiestrogen strategies for MAS.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-006-q1',
    subtopic: 'Case vignette',
    question: 'A 3-year-old girl has Tanner B3 breasts, growth acceleration, bone age 7 years, uterine enlargement, basal LH 2.3 IU/L, and GnRH-agonist LH 56 IU/L. The best diagnosis is:',
    options: [
      'Idiopathic gonadotropin-dependent precocious puberty',
      'Isolated premature thelarche',
      'Gonadotropin-independent precocity from ovarian cyst',
      'Primary hypothyroidism with pseudo-precocity'
    ],
    correctOption: 0,
    explanation: 'Advanced bone age, uterine growth, and pubertal LH response indicate GDPP.',
    reference: 'Pubertal LH response with advanced bone age and uterine growth supports GDPP.'
  },
  {
    id: 'pe-cr-006-q2',
    subtopic: 'Definition',
    question: 'Which age threshold defines precocious puberty in boys?',
    options: [
      'Secondary sexual characteristics before 9 years',
      'Before 10 years',
      'Before 11 years',
      'Before 12 years'
    ],
    correctOption: 0,
    explanation: 'Cutoffs are <8 years in girls and <9 years in boys.',
    reference: 'Precocious puberty is defined as pubertal signs before 9 years in boys.'
  },
  {
    id: 'pe-cr-006-q3',
    subtopic: 'Normal variants',
    question: 'A 2-year-old girl has stable Tanner B2 breasts, no pubic hair, normal growth velocity, and normal bone age. The most likely diagnosis is:',
    options: [
      'Isolated premature thelarche',
      'GDPP',
      'GIPP from ovarian cyst',
      'Central nervous system tumor'
    ],
    correctOption: 0,
    explanation: 'Nonprogressive thelarche with normal growth and bone age suggests benign premature thelarche.',
    reference: 'Premature thelarche is nonprogressive with normal growth and bone age.'
  },
  {
    id: 'pe-cr-006-q4',
    subtopic: 'Classification',
    question: 'Which feature best distinguishes GIPP from GDPP in boys?',
    options: [
      'Penile enlargement with small testes',
      'Testicular enlargement preceding penile growth',
      'Sequential pubertal progression',
      'Pubertal LH response to GnRH'
    ],
    correctOption: 0,
    explanation: 'Discordant penile enlargement with small testes suggests peripheral steroid excess (GIPP).',
    reference: 'GIPP often shows discordant staging, such as penile growth without testicular enlargement.'
  },
  {
    id: 'pe-cr-006-q5',
    subtopic: 'Classification',
    question: 'Heterosexual precocious puberty is best described as:',
    options: [
      'Secondary sexual characteristics discordant with gonadal sex',
      'Early but sequential puberty',
      'HPG-axis reactivation with pubertal LH response',
      'Delayed puberty after normal onset'
    ],
    correctOption: 0,
    explanation: 'Heterosexual precocity is opposite-sex trait development and is gonadotropin independent.',
    reference: 'Heterosexual precocity is discordant with gonadal sex and is gonadotropin independent.'
  },
  {
    id: 'pe-cr-006-q6',
    subtopic: 'Androgen physiology',
    question: 'Adrenarche refers to:',
    options: [
      'Biochemical rise in adrenal androgens before clinical hair development',
      'Appearance of pubic hair due to ovarian estrogen',
      'Testicular enlargement from LH stimulation',
      'Onset of menarche'
    ],
    correctOption: 0,
    explanation: 'Adrenarche is the hormonal rise in DHEA/DHEAS that precedes pubarche.',
    reference: 'Adrenarche is a biochemical adrenal androgen rise; pubarche is clinical hair development.'
  },
  {
    id: 'pe-cr-006-q7',
    subtopic: 'Premature pubarche',
    question: 'A child with isolated pubic hair and bone age advanced by >2.5 SD should undergo evaluation for:',
    options: [
      'Pathologic androgen excess',
      'Normal puberty variant',
      'Constitutional delay',
      'Thyroid hormone resistance'
    ],
    correctOption: 0,
    explanation: 'Marked bone age advancement or virilization suggests pathologic causes of pubarche.',
    reference: 'Significant bone age advancement with pubarche warrants evaluation for androgen excess.'
  },
  {
    id: 'pe-cr-006-q8',
    subtopic: 'Diagnostics',
    question: 'In girls, a basal LH value most consistent with GDPP is:',
    options: [
      '≥0.3 IU/L',
      '≤0.1 IU/L',
      '0.05 IU/L',
      'Undetectable'
    ],
    correctOption: 0,
    explanation: 'Basal LH at or above 0.3 IU/L indicates HPG-axis activation.',
    reference: 'Basal LH ≥0.3 IU/L supports GDPP.'
  },
  {
    id: 'pe-cr-006-q9',
    subtopic: 'Diagnostics',
    question: 'Why is LH response to GnRH preferred over FSH response for diagnosing GDPP?',
    options: [
      'LH response reflects HPG-axis reactivation',
      'FSH response is absent in puberty',
      'LH is elevated in all children regardless of puberty',
      'FSH is only secreted by the adrenal gland'
    ],
    correctOption: 0,
    explanation: 'FSH responses occur at all ages, whereas LH rises only after HPG-axis activation.',
    reference: 'LH response indicates activation of the GnRH pulse generator.'
  },
  {
    id: 'pe-cr-006-q10',
    subtopic: 'Imaging',
    question: 'Which pelvic ultrasound finding best supports pubertal onset in a girl?',
    options: [
      'Ovarian volume ≥2.8 ml',
      'Uterine length 2.5 cm',
      'Absent endometrial echo',
      'Ovarian volume 0.5 ml'
    ],
    correctOption: 0,
    explanation: 'Ovarian volume ≥2.8 ml is a strong indicator of pubertal estrogen effect.',
    reference: 'Ovarian volume ≥2.8 ml supports pubertal onset on ultrasound.'
  },
  {
    id: 'pe-cr-006-q11',
    subtopic: 'Imaging',
    question: 'A single ovarian cyst larger than 9 mm in a girl with early breast development suggests:',
    options: [
      'GIPP from autonomous estrogen production',
      'GDPP with HPG activation',
      'Normal pubertal variant',
      'Congenital hypogonadism'
    ],
    correctOption: 0,
    explanation: 'A solitary large cyst favors GIPP, while multiple small follicles favor GDPP.',
    reference: 'A single large follicular cyst points to GIPP.'
  },
  {
    id: 'pe-cr-006-q12',
    subtopic: 'Neuroimaging',
    question: 'Which child with GDPP has the highest priority for MRI brain?',
    options: [
      'Boy with precocity at age 7',
      'Girl with onset at age 7.5 and slow progression',
      'Girl with onset at 7.8 years and normal neuro exam',
      'Girl with isolated thelarche and normal bone age'
    ],
    correctOption: 0,
    explanation: 'Boys have a higher prevalence of CNS lesions and should always be imaged.',
    reference: 'MRI is recommended for all GDPP, particularly in boys or very young girls.'
  },
  {
    id: 'pe-cr-006-q13',
    subtopic: 'Hypothalamic hamartoma',
    question: 'A 3-year-old boy has gelastic seizures and GDPP. The most likely lesion is:',
    options: [
      'Hypothalamic hamartoma',
      'Pituitary microadenoma',
      'Pineal cyst',
      'Craniopharyngioma'
    ],
    correctOption: 0,
    explanation: 'Gelastic seizures in young children strongly suggest hypothalamic hamartoma.',
    reference: 'Gelastic seizures are most commonly caused by hypothalamic hamartoma.'
  },
  {
    id: 'pe-cr-006-q14',
    subtopic: 'McCune-Albright syndrome',
    question: 'A girl with precocious vaginal bleeding, café-au-lait spots, and fibrous dysplasia likely has:',
    options: [
      'McCune-Albright syndrome',
      'Neurofibromatosis type 1',
      'Peutz-Jeghers syndrome',
      'Turner syndrome'
    ],
    correctOption: 0,
    explanation: 'The triad of café-au-lait macules, fibrous dysplasia, and endocrinopathy fits MAS.',
    reference: 'MAS causes autonomous ovarian estrogen production with café-au-lait macules and fibrous dysplasia.'
  },
  {
    id: 'pe-cr-006-q15',
    subtopic: 'Familial testotoxicosis',
    question: 'A boy with early virilization, enlarged testes, suppressed LH, and family history of early puberty likely has:',
    options: [
      'Familial testotoxicosis',
      'GDPP from a CNS lesion',
      'Primary hypothyroidism',
      'Androgen-secreting adrenal tumor'
    ],
    correctOption: 0,
    explanation: 'LH receptor activation causes gonadotropin-independent testosterone production with enlarged testes.',
    reference: 'Familial testotoxicosis is LH receptor activation causing LH-independent testosterone production.'
  },
  {
    id: 'pe-cr-006-q16',
    subtopic: 'Mixed precocity',
    question: 'Mixed precocious puberty most often occurs when:',
    options: [
      'Long-standing GIPP advances bone age and later activates HPG axis',
      'GnRH agonist therapy is started early',
      'The child has isolated premature thelarche',
      'Adrenarche is delayed'
    ],
    correctOption: 0,
    explanation: 'Chronic steroid exposure primes the HPG axis, leading to GDPP superimposed on GIPP.',
    reference: 'Mixed precocity is GDPP superimposed on GIPP after prolonged steroid exposure.'
  },
  {
    id: 'pe-cr-006-q17',
    subtopic: 'Evaluation',
    question: 'In boys, a basal LH ≥0.3 IU/L most strongly suggests:',
    options: [
      'GDPP',
      'GIPP',
      'Isolated adrenarche',
      'Delayed puberty'
    ],
    correctOption: 0,
    explanation: 'Basal LH at or above 0.3 IU/L indicates HPG-axis activation.',
    reference: 'Basal LH ≥0.3 IU/L suggests GDPP in boys.'
  },
  {
    id: 'pe-cr-006-q18',
    subtopic: 'Therapy',
    question: 'The first-line medical treatment for GDPP is:',
    options: [
      'GnRH agonist therapy',
      'High-dose estrogen',
      'Aromatase inhibitor alone',
      'Testosterone suppression with ketoconazole'
    ],
    correctOption: 0,
    explanation: 'GnRH agonists suppress the HPG axis and reverse pubertal progression.',
    reference: 'GnRH agonists are the preferred treatment for GDPP.'
  },
  {
    id: 'pe-cr-006-q19',
    subtopic: 'Therapy',
    question: 'A known effect of initiating GnRH agonist therapy is:',
    options: [
      'Transient pubertal flare in the first 1–2 weeks',
      'Immediate and permanent gonadal failure',
      'Suppressed growth velocity within 24 hours',
      'Rapid loss of bone density in all patients'
    ],
    correctOption: 0,
    explanation: 'Initial receptor stimulation causes a temporary rise in gonadotropins and sex steroids.',
    reference: 'GnRH agonists cause an initial flare before sustained suppression.'
  },
  {
    id: 'pe-cr-006-q20',
    subtopic: 'Therapy monitoring',
    question: 'Which monitoring strategy is most appropriate for children receiving GnRH agonists?',
    options: [
      'Tanner staging, growth velocity, and periodic LH/estradiol or testosterone',
      'Annual CT brain without labs',
      'Urine ketone checks only',
      'No monitoring if growth slows'
    ],
    correctOption: 0,
    explanation: 'Clinical and biochemical monitoring ensures adequate suppression.',
    reference: 'Monitoring includes pubertal staging, growth velocity, and hormone suppression.'
  },
  {
    id: 'pe-cr-006-q21',
    subtopic: 'Therapy discontinuation',
    question: 'Stopping GnRH agonist therapy is usually considered when:',
    options: [
      'Chronological age approaches 11 years and height benefit is minimal',
      'The child reaches Tanner stage 2',
      'Basal LH rises above 0.3 IU/L',
      'Bone age equals chronological age at all times'
    ],
    correctOption: 0,
    explanation: 'Height gains are limited beyond about 11 years, so therapy is often stopped then.',
    reference: 'Therapy is commonly stopped around age 11 when further height benefit is minimal.'
  },
  {
    id: 'pe-cr-006-q22',
    subtopic: 'Therapy recovery',
    question: 'After stopping GnRH agonist therapy, menses in girls typically resumes:',
    options: [
      'Within about 1 to 1.5 years',
      'Within 1 week',
      'After 5 years',
      'Never resumes'
    ],
    correctOption: 0,
    explanation: 'Gonadotropin recovery is gradual, with menses returning within about a year.',
    reference: 'Menses typically resumes within 1–1.5 years after stopping GnRH agonists.'
  },
  {
    id: 'pe-cr-006-q23',
    subtopic: 'Bone health',
    question: 'Which statement about GnRH agonist therapy and bone mass is most accurate?',
    options: [
      'Peak bone mass is generally preserved with adequate calcium and vitamin D',
      'It always causes permanent osteoporosis',
      'It prevents any bone accrual after therapy stops',
      'It increases fracture risk in all children'
    ],
    correctOption: 0,
    explanation: 'Evidence shows no long-term compromise of peak bone mass.',
    reference: 'GnRH agonist therapy does not impair peak bone mass when nutrition is optimized.'
  },
  {
    id: 'pe-cr-006-q24',
    subtopic: 'GIPP treatment',
    question: 'Best initial treatment for precocious puberty from an adrenal tumor is:',
    options: [
      'Surgical removal of the tumor',
      'GnRH agonist alone',
      'Observation only',
      'High-dose estrogen'
    ],
    correctOption: 0,
    explanation: 'Tumor-driven GIPP requires surgical removal of the source of steroids.',
    reference: 'GIPP treatment targets the underlying source, with surgery for tumors.'
  },
  {
    id: 'pe-cr-006-q25',
    subtopic: 'GIPP treatment',
    question: 'Which medication class is commonly used for precocity in McCune-Albright syndrome?',
    options: [
      'Aromatase inhibitors or MDPA',
      'Thyroid hormone only',
      'Growth hormone alone',
      'Beta blockers'
    ],
    correctOption: 0,
    explanation: 'MAS treatment often uses antiestrogen strategies such as aromatase inhibitors or MDPA.',
    reference: 'MAS-related precocity can be treated with MDPA, ketoconazole, or aromatase inhibitors.'
  },
  {
    id: 'pe-cr-006-q26',
    subtopic: 'Neuroimaging',
    question: 'A girl with GDPP, visual impairment, and rapid pubertal progression should:',
    options: [
      'Undergo MRI brain to evaluate for CNS pathology',
      'Be reassured and observed only',
      'Receive only pelvic ultrasound',
      'Start metformin therapy'
    ],
    correctOption: 0,
    explanation: 'Neurologic signs or rapid progression increase the likelihood of CNS lesions.',
    reference: 'MRI is indicated in GDPP with neurologic features or rapid progression.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-006-tf1',
    subtopic: 'Definition',
    statement: 'Precocious puberty is defined as pubertal signs before 8 years in girls or 9 years in boys.',
    correctAnswer: true,
    explanation: 'These age cutoffs are standard for clinical evaluation.',
    reference: 'Precocious puberty is defined as secondary sexual characteristics before 8 years in girls or 9 years in boys.'
  },
  {
    id: 'pe-cr-006-tf2',
    subtopic: 'Normal variants',
    statement: 'Isolated premature thelarche is typically nonprogressive with normal bone age.',
    correctAnswer: true,
    explanation: 'Stable breast development without growth acceleration is typical.',
    reference: 'Premature thelarche is nonprogressive with normal growth and bone age.'
  },
  {
    id: 'pe-cr-006-tf3',
    subtopic: 'Classification',
    statement: 'GIPP is characterized by sex steroid excess independent of HPG-axis activation.',
    correctAnswer: true,
    explanation: 'GIPP is peripheral and not driven by gonadotropins.',
    reference: 'GIPP is sex steroid excess without HPG-axis reactivation.'
  },
  {
    id: 'pe-cr-006-tf4',
    subtopic: 'Androgen physiology',
    statement: 'Adrenarche is a biochemical rise in DHEA/DHEAS that precedes pubarche.',
    correctAnswer: true,
    explanation: 'Clinical pubic hair appears later.',
    reference: 'Adrenarche is a biochemical adrenal androgen rise; pubarche is clinical hair development.'
  },
  {
    id: 'pe-cr-006-tf5',
    subtopic: 'Diagnostics',
    statement: 'Basal LH ≥0.3 IU/L in a girl suggests GDPP.',
    correctAnswer: true,
    explanation: 'This threshold indicates HPG-axis activation.',
    reference: 'Basal LH ≥0.3 IU/L supports GDPP.'
  },
  {
    id: 'pe-cr-006-tf6',
    subtopic: 'Imaging',
    statement: 'Ovarian volume ≥2.8 ml on ultrasound supports pubertal onset in girls.',
    correctAnswer: true,
    explanation: 'Ovarian volume is a sensitive marker of estrogen exposure.',
    reference: 'Ovarian volume ≥2.8 ml supports pubertal onset on ultrasound.'
  },
  {
    id: 'pe-cr-006-tf7',
    subtopic: 'Neuroimaging',
    statement: 'MRI brain is recommended for all children diagnosed with GDPP.',
    correctAnswer: true,
    explanation: 'CNS lesions are more common in boys and younger girls.',
    reference: 'MRI is indicated in GDPP, particularly in boys or very young girls.'
  },
  {
    id: 'pe-cr-006-tf8',
    subtopic: 'Hypothalamic hamartoma',
    statement: 'Gelastic seizures are strongly associated with hypothalamic hamartoma.',
    correctAnswer: true,
    explanation: 'The lesion is the most common cause of gelastic seizures.',
    reference: 'Gelastic seizures are most commonly caused by hypothalamic hamartoma.'
  },
  {
    id: 'pe-cr-006-tf9',
    subtopic: 'Therapy',
    statement: 'GnRH agonists can cause an initial flare before suppression.',
    correctAnswer: true,
    explanation: 'Early receptor stimulation temporarily raises gonadotropins.',
    reference: 'GnRH agonists cause an initial flare before sustained suppression.'
  },
  {
    id: 'pe-cr-006-tf10',
    subtopic: 'Therapy discontinuation',
    statement: 'HPG-axis recovery after stopping GnRH agonists usually occurs within a year.',
    correctAnswer: true,
    explanation: 'Gonadotropins rise within months after discontinuation.',
    reference: 'HPG-axis activity typically recovers within a year after stopping GnRH agonists.'
  },
  {
    id: 'pe-cr-006-tf11',
    subtopic: 'Bone health',
    statement: 'GnRH agonist therapy generally does not impair peak bone mass when nutrition is adequate.',
    correctAnswer: true,
    explanation: 'Long-term data support normal bone mass accrual.',
    reference: 'GnRH agonist therapy does not impair peak bone mass when nutrition is optimized.'
  },
  {
    id: 'pe-cr-006-tf12',
    subtopic: 'GIPP treatment',
    statement: 'Treatment of GIPP is tailored to the underlying source of steroid excess.',
    correctAnswer: true,
    explanation: 'Tumors, CAH, and MAS require different treatments.',
    reference: 'GIPP treatment targets the underlying source, with surgery for tumors or medical therapy for specific causes.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-006-ar1',
    subtopic: 'Definition',
    assertion: 'Precocious puberty is defined as pubertal signs before 8 years in girls.',
    reason: 'This cutoff reflects about 2.5 standard deviations below the mean age of pubertal onset.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the cutoff.',
    reference: 'Precocious puberty cutoffs are based on statistical deviation from mean pubertal onset age.'
  },
  {
    id: 'pe-cr-006-ar2',
    subtopic: 'Classification',
    assertion: 'GDPP usually shows sequential pubertal progression.',
    reason: 'It is driven by early activation of the HPG axis.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the pattern.',
    reference: 'GDPP reflects early HPG activation with sequential pubertal changes.'
  },
  {
    id: 'pe-cr-006-ar3',
    subtopic: 'Normal variants',
    assertion: 'Isolated premature thelarche is typically nonprogressive.',
    reason: 'Progesterone exposure remains prepubertal, limiting breast maturation.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the limited progression.',
    reference: 'Premature thelarche remains limited because progesterone levels are prepubertal.'
  },
  {
    id: 'pe-cr-006-ar4',
    subtopic: 'Diagnostics',
    assertion: 'Basal LH ≥0.3 IU/L supports a diagnosis of GDPP in girls.',
    reason: 'LH elevation reflects reactivation of the GnRH pulse generator.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the test.',
    reference: 'Basal LH thresholds indicate HPG-axis activation.'
  },
  {
    id: 'pe-cr-006-ar5',
    subtopic: 'Diagnostics',
    assertion: 'LH response to GnRH is preferred over FSH response to diagnose GDPP.',
    reason: 'FSH response occurs even in prepubertal children.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains test choice.',
    reference: 'LH response indicates true HPG activation, while FSH responds at all ages.'
  },
  {
    id: 'pe-cr-006-ar6',
    subtopic: 'Imaging',
    assertion: 'Ovarian volume ≥2.8 ml on ultrasound suggests pubertal onset.',
    reason: 'Ovarian enlargement reflects estrogen exposure and follicular activity.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the imaging marker.',
    reference: 'Ovarian enlargement on ultrasound reflects estrogen exposure and pubertal onset.'
  },
  {
    id: 'pe-cr-006-ar7',
    subtopic: 'Neuroimaging',
    assertion: 'MRI brain is recommended in boys with GDPP.',
    reason: 'Boys have a higher likelihood of CNS pathology.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the recommendation.',
    reference: 'Boys with GDPP have a higher prevalence of CNS lesions, so MRI is indicated.'
  },
  {
    id: 'pe-cr-006-ar8',
    subtopic: 'Hypothalamic hamartoma',
    assertion: 'Gelastic seizures suggest hypothalamic hamartoma in children with precocity.',
    reason: 'Hamartomas contain ectopic GnRH neurons that can drive early puberty.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the association.',
    reference: 'Gelastic seizures are linked to hypothalamic hamartoma and early HPG activation.'
  },
  {
    id: 'pe-cr-006-ar9',
    subtopic: 'Therapy',
    assertion: 'GnRH agonists can cause a transient flare in the first 1–2 weeks.',
    reason: 'Initial receptor stimulation increases gonadotropin secretion before downregulation.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the flare.',
    reference: 'GnRH agonists initially stimulate then suppress the HPG axis.'
  },
  {
    id: 'pe-cr-006-ar10',
    subtopic: 'Therapy monitoring',
    assertion: 'Monitoring GnRH agonist therapy includes growth velocity and hormone suppression.',
    reason: 'Clinical regression and biochemical suppression confirm adequate dosing.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains monitoring.',
    reference: 'Therapy is monitored by growth, pubertal staging, and hormone suppression.'
  },
  {
    id: 'pe-cr-006-ar11',
    subtopic: 'Therapy discontinuation',
    assertion: 'GnRH agonist therapy is often discontinued around age 11.',
    reason: 'Further height gain is limited once pubertal growth depends on sex steroids.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains timing.',
    reference: 'Stopping GnRH agonists around age 11 reflects minimal further height benefit.'
  },
  {
    id: 'pe-cr-006-ar12',
    subtopic: 'GIPP treatment',
    assertion: 'Treatment of GIPP depends on the underlying cause.',
    reason: 'Tumors require surgery while CAH and MAS need medical therapy.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the approach.',
    reference: 'GIPP management is etiology-specific, including surgery or targeted medical therapy.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-006',
  book: 'clinical_rounds',
  chapterNo: '6',
  title: 'Precocious Puberty',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/006_precocious_puberty',
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
