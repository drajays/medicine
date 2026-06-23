#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-007_delayed_puberty.json'
);

const notes = [
  {
    id: 'pe-cr-007-n1',
    subtopic: 'Definition',
    title: 'Why delayed puberty uses age 14 in boys and 13 in girls',
    content: 'Population data place pubertal onset around 11.5 years in boys and 10.5 years in girls, so the absence of testicular enlargement by 14 or breast development by 13 marks a delay beyond normal variation.',
    keyPoints: [
      'Cutoffs reflect about +2.5 SD from mean onset.',
      'Boys: no testicular enlargement by 14 years.',
      'Girls: no breast development by 13 years.'
    ],
    reference: 'Delayed puberty is defined as no testicular enlargement by 14 years in boys or no breast development by 13 years in girls.'
  },
  {
    id: 'pe-cr-007-n2',
    subtopic: 'Definition',
    title: 'How arrested or very slow progression fits delayed puberty',
    content: 'Delayed puberty also includes pubertal onset that stalls for 2 years or takes more than about 5 years to complete key milestones, reflecting failure of normal tempo.',
    keyPoints: [
      'Arrested puberty means no progression for 2 years.',
      'Prolonged tempo exceeds 5 years between key milestones.',
      'Slow tempo is managed like delayed puberty.'
    ],
    reference: 'Lack of progression for 2 years or very slow completion of pubertal milestones is considered delayed puberty.'
  },
  {
    id: 'pe-cr-007-n3',
    subtopic: 'Pubertal timing',
    title: 'Why pubarche is not used to mark pubertal onset',
    content: 'Pubarche reflects adrenal androgen production (adrenarche) and can occur without HPG-axis activation, while true puberty begins with thelarche or testicular enlargement.',
    keyPoints: [
      'Pubarche is driven by adrenal androgens.',
      'Gonadarche marks HPG-axis reactivation.',
      'Pubarche can precede gonadarche.'
    ],
    reference: 'Pubarche is a manifestation of adrenarche and does not define onset of true puberty.'
  },
  {
    id: 'pe-cr-007-n4',
    subtopic: 'Neuroendocrine control',
    title: 'How kisspeptin neurons link to GnRH release',
    content: 'Kisspeptin from KNDy and AVPV neurons stimulates GnRH neurons via GPR54 receptors, driving pulsatile GnRH secretion that initiates puberty.',
    keyPoints: [
      'KNDy neurons co-secrete kisspeptin, neurokinin B, dynorphin.',
      'Kisspeptin acts via GPR54 on GnRH neurons.',
      'This signaling triggers GnRH pulsatility.'
    ],
    reference: 'Kisspeptin from hypothalamic nuclei activates GnRH neurons through the GPR54 receptor.'
  },
  {
    id: 'pe-cr-007-n5',
    subtopic: 'Neuroendocrine control',
    title: 'How kisspeptin initiates puberty and is regulated',
    content: 'KNDy-driven kisspeptin release is a gateway to puberty, modulated by neurokinin B and dynorphin, with inhibitory control from MKRN3 and polycomb proteins.',
    keyPoints: [
      'KNDy neurons stimulate puberty onset.',
      'Neurokinin B stimulates and dynorphin inhibits kisspeptin.',
      'MKRN3 suppresses kisspeptin expression.'
    ],
    reference: 'Kisspeptin initiates puberty and is regulated by stimulatory and inhibitory signals including MKRN3.'
  },
  {
    id: 'pe-cr-007-n6',
    subtopic: 'Neuroendocrine control',
    title: 'How kisspeptin contributes to the preovulatory LH surge',
    content: 'Kisspeptin from AVPV Kiss-1 neurons mediates estrogen-driven positive feedback in females, enabling the preovulatory LH surge; this AVPV pathway is minimal in males.',
    keyPoints: [
      'AVPV Kiss-1 neurons respond to estrogen.',
      'They drive the preovulatory LH surge.',
      'AVPV Kiss-1 neurons are sparse in males.'
    ],
    reference: 'Kisspeptin from AVPV neurons mediates estrogen-driven LH surge in females.'
  },
  {
    id: 'pe-cr-007-n7',
    subtopic: 'Metabolic signals',
    title: 'How leptin acts as a permissive puberty signal',
    content: 'Adequate body fat raises leptin, which stimulates kisspeptin neurons and permits HPG-axis activation; leptin deficiency causes hypogonadotropic hypogonadism, yet normal timing can occur despite low leptin in lipodystrophy.',
    keyPoints: [
      'Leptin signals energy sufficiency to the hypothalamus.',
      'Leptin deficiency can cause isolated IHH.',
      'Leptin is permissive, not the primary trigger.'
    ],
    reference: 'Leptin stimulates kisspeptin pathways and permits puberty, but is not the sole trigger.'
  },
  {
    id: 'pe-cr-007-n8',
    subtopic: 'Mini-puberty',
    title: 'How mini-puberty is defined and timed',
    content: 'Mini-puberty is the neonatal reactivation of the HPG axis after placental estrogen withdrawal, with gonadotropin and sex steroid surges starting in the second week of life.',
    keyPoints: [
      'Gonadotropin surges begin in early infancy.',
      'Boys peak around 3 months and decline by 6-9 months.',
      'Girls have prolonged FSH elevation into early childhood.'
    ],
    reference: 'Mini-puberty is a postnatal surge of gonadotropins and sex steroids starting in early infancy.'
  },
  {
    id: 'pe-cr-007-n9',
    subtopic: 'Mini-puberty',
    title: 'Why mini-puberty is important in boys',
    content: 'The neonatal gonadotropin and testosterone surge expands Leydig and Sertoli cells, increases testicular volume, supports penile growth, and helps testicular descent.',
    keyPoints: [
      'Promotes Leydig and Sertoli cell proliferation.',
      'Increases testicular size and penile length.',
      'Supports postnatal testicular descent.'
    ],
    reference: 'Mini-puberty in boys supports testicular growth, penile growth, and descent.'
  },
  {
    id: 'pe-cr-007-n10',
    subtopic: 'Mini-puberty',
    title: 'How absence of mini-puberty signals gonadal disorders',
    content: 'Mini-puberty is absent in congenital IHH and complete androgen insensitivity; androgen excess states can suppress gonadotropins and blunt the neonatal surge.',
    keyPoints: [
      'Absent in congenital IHH.',
      'Absent in complete androgen insensitivity.',
      'Androgen excess can suppress the surge.'
    ],
    reference: 'Mini-puberty is absent in congenital IHH and complete androgen insensitivity and may be suppressed by androgen excess.'
  },
  {
    id: 'pe-cr-007-n11',
    subtopic: 'Sex differences',
    title: 'How peripubertal feedback creates gender dimorphism',
    content: 'Estrogen-mediated positive feedback for LH develops during peripuberty in girls and enables ovulation, and higher female prolactin levels also emerge during this period.',
    keyPoints: [
      'Positive LH feedback develops only in girls.',
      'This feedback is required for ovulatory cycles.',
      'Prolactin levels diverge by sex in peripuberty.'
    ],
    reference: 'Peripubertal development brings estrogen-driven LH positive feedback and higher prolactin in girls.'
  },
  {
    id: 'pe-cr-007-n12',
    subtopic: 'Hypogonadism',
    title: 'How hypogonadism is defined clinically',
    content: 'Hypogonadism refers to impaired gonadal steroidogenesis and/or gametogenesis, but isolated germ cell dysfunction with normal steroid levels is not labeled hypogonadism.',
    keyPoints: [
      'Requires impaired steroidogenesis and/or gametogenesis.',
      'Isolated germ cell failure with normal steroids is excluded.',
      'Normal estradiol with anovulation is not hypogonadism.'
    ],
    reference: 'Hypogonadism is impaired gonadal steroid production or gametogenesis, not isolated germ cell dysfunction.'
  },
  {
    id: 'pe-cr-007-n13',
    subtopic: 'Hypogonadism',
    title: 'How hypogonadism is classified along the HPG axis',
    content: 'Low gonadotropins indicate hypothalamic or pituitary causes (hypogonadotropic), whereas elevated gonadotropins indicate primary gonadal failure (hypergonadotropic).',
    keyPoints: [
      'Hypogonadotropic: central defect, low LH/FSH.',
      'Hypergonadotropic: primary gonadal failure, high LH/FSH.',
      'Classification guides etiology and testing.'
    ],
    reference: 'Hypogonadism is categorized as hypogonadotropic or hypergonadotropic based on site of defect.'
  },
  {
    id: 'pe-cr-007-n14',
    subtopic: 'Etiology',
    title: 'Why CDGP is the most common cause of delayed puberty',
    content: 'Constitutional delay in growth and puberty is the predominant cause of delayed puberty, especially in boys, with most entering puberty spontaneously by age 18.',
    keyPoints: [
      'CDGP is the leading cause in boys.',
      'Most cases resolve spontaneously before 18.',
      'Family history of late bloomers is common.'
    ],
    reference: 'CDGP is the most common cause of delayed puberty, especially in boys.'
  },
  {
    id: 'pe-cr-007-n15',
    subtopic: 'Etiology',
    title: 'How functional hypogonadotropic hypogonadism arises',
    content: 'Chronic illness and undernutrition can suppress GnRH secretion, leading to functional hypogonadotropic hypogonadism in conditions such as celiac disease, Crohn disease, nephrotic syndrome, and anorexia nervosa.',
    keyPoints: [
      'Systemic illness suppresses GnRH and gonadotropins.',
      'Examples include celiac disease and Crohn disease.',
      'Nutritional deficiency and anorexia are common causes.'
    ],
    reference: 'Functional hypogonadotropic hypogonadism occurs with chronic systemic illness or undernutrition.'
  },
  {
    id: 'pe-cr-007-n16',
    subtopic: 'Etiology',
    title: 'How acquired hypogonadotropic hypogonadism is suspected',
    content: 'Adult-onset hypogonadotropic hypogonadism requires evaluation for sellar or suprasellar pathology and a history of head trauma, stroke, or pituitary injury.',
    keyPoints: [
      'Investigate for tumors or infiltrative disease.',
      'Ask about head injury or pituitary apoplexy.',
      'Systemic disease can also contribute.'
    ],
    reference: 'Acquired hypogonadotropic hypogonadism warrants evaluation for sellar disease or pituitary injury.'
  },
  {
    id: 'pe-cr-007-n17',
    subtopic: 'Etiology',
    title: 'How congenital isolated IHH is defined',
    content: 'Congenital isolated IHH is absent or arrested puberty due to impaired GnRH or gonadotropin secretion without structural pituitary lesions or other hormone deficiencies.',
    keyPoints: [
      'Isolated defect in GnRH or gonadotropin secretion.',
      'No structural hypothalamic-pituitary abnormality.',
      'Other pituitary hormones are normal.'
    ],
    reference: 'Congenital isolated IHH is impaired GnRH/gonadotropin secretion without structural lesions or other pituitary deficits.'
  },
  {
    id: 'pe-cr-007-n18',
    subtopic: 'Etiology',
    title: 'How early childhood clues suggest congenital IHH',
    content: 'Micropenis, cryptorchidism, midline defects, and anosmia or hyposmia in a child should raise suspicion for congenital IHH.',
    keyPoints: [
      'Micropenis and cryptorchidism are key clues.',
      'Midline or skeletal defects add suspicion.',
      'Anosmia or hyposmia points toward IHH.'
    ],
    reference: 'Micropenis, cryptorchidism, midline defects, and anosmia/hyposmia suggest congenital IHH.'
  },
  {
    id: 'pe-cr-007-n19',
    subtopic: 'Clinical clues',
    title: 'How prepubertal and postpubertal hypogonadism differ in adult men',
    content: 'Prepubertal onset causes eunuchoidal proportions, high-pitched voice, scant body hair, and very small testes, whereas postpubertal onset shows normal proportions with later regression of hair and soft testes.',
    keyPoints: [
      'Prepubertal onset leads to eunuchoidal habitus.',
      'Postpubertal onset retains normal proportions.',
      'Hair regression and soft testes suggest later onset.'
    ],
    reference: 'Prepubertal onset features include eunuchoidal habitus and very small testes, whereas postpubertal onset shows normal body proportions.'
  },
  {
    id: 'pe-cr-007-n20',
    subtopic: 'Kallmann syndrome',
    title: 'How Kallmann syndrome is defined and linked to migration',
    content: 'Kallmann syndrome is congenital IHH with anosmia due to disrupted migration of olfactory and GnRH neurons, often involving genes such as KAL1, FGFR1, and PROKR2.',
    keyPoints: [
      'IHH plus anosmia defines Kallmann syndrome.',
      'Olfactory and GnRH neurons share migratory paths.',
      'KAL1 mutations are strongly linked to anosmia.'
    ],
    reference: 'Kallmann syndrome is IHH with anosmia from defective migration of olfactory and GnRH neurons.'
  },
  {
    id: 'pe-cr-007-n21',
    subtopic: 'Kallmann syndrome',
    title: 'How to test anosmia in suspected IHH',
    content: 'Formal smell testing is recommended because patients may not recognize olfactory loss; bedside odor tests or UPSIT can be used.',
    keyPoints: [
      'History alone may miss anosmia.',
      'Bedside odors like clove or peppermint can screen.',
      'UPSIT provides objective testing.'
    ],
    reference: 'Formal testing for anosmia with bedside odors or UPSIT is recommended in IHH.'
  },
  {
    id: 'pe-cr-007-n22',
    subtopic: 'Kallmann syndrome',
    title: 'How nonreproductive findings support Kallmann syndrome',
    content: 'Synkinesia, hearing loss, cerebellar signs, skeletal defects, cleft palate, dental agenesis, and renal agenesis can accompany Kallmann syndrome.',
    keyPoints: [
      'Neurologic findings include synkinesia and ataxia.',
      'Skeletal anomalies like syndactyly can occur.',
      'Renal and craniofacial defects are reported.'
    ],
    reference: 'Kallmann syndrome can include synkinesia, hearing loss, skeletal defects, and renal agenesis.'
  },
  {
    id: 'pe-cr-007-n23',
    subtopic: 'Kallmann syndrome',
    title: 'Why synkinesia occurs in some Kallmann patients',
    content: 'Mirror movements may result from partial corticospinal decussation failure or reduced interhemispheric inhibition, reflecting a midline developmental defect.',
    keyPoints: [
      'Synkinesia is a midline developmental sign.',
      'Possible mechanism is failed corticospinal decussation.',
      'Another mechanism is reduced interhemispheric inhibition.'
    ],
    reference: 'Synkinesia in Kallmann syndrome reflects midline defects such as incomplete corticospinal decussation.'
  },
  {
    id: 'pe-cr-007-n24',
    subtopic: 'CDGP vs IHH',
    title: 'How CDGP can be distinguished from congenital IHH',
    content: 'CDGP is associated with short stature, delayed bone age that matches height age, and strong family history of late bloomers, whereas congenital IHH often has neonatal clues and persistent prepubertal gonadotropins.',
    keyPoints: [
      'CDGP often has family history of delayed puberty.',
      'Bone age is delayed and correlates with height age.',
      'Neonatal micropenis or anosmia favors IHH.'
    ],
    reference: 'Family history, delayed bone age, and neonatal clues help differentiate CDGP from congenital IHH.'
  },
  {
    id: 'pe-cr-007-n25',
    subtopic: 'Evaluation',
    title: 'How to investigate a child with delayed puberty',
    content: 'Initial workup includes basic labs and thyroid tests, followed by LH, FSH, testosterone or estradiol, and bone age; further testing includes karyotype, MRI, and dynamic testing based on results.',
    keyPoints: [
      'Start with hemogram and renal, liver, thyroid tests.',
      'Assess LH, FSH, sex steroids, and bone age.',
      'Use karyotype, MRI, and dynamic tests if needed.'
    ],
    reference: 'Evaluation starts with basic labs, gonadotropins, sex steroids, and bone age, with targeted imaging or karyotype as needed.'
  },
  {
    id: 'pe-cr-007-n26',
    subtopic: 'Evaluation',
    title: 'How to decide on MRI in hypogonadotropic hypogonadism',
    content: 'MRI is recommended when hypogonadotropic hypogonadism is associated with anosmia, multiple pituitary hormone deficiency, hyperprolactinemia, or mass effect symptoms.',
    keyPoints: [
      'Indicated with anosmia or hyposmia.',
      'Indicated with multiple pituitary hormone deficits.',
      'Consider with hyperprolactinemia or mass effect.'
    ],
    reference: 'MRI is indicated when hypogonadotropic hypogonadism is linked to anosmia, pituitary deficits, or mass effect.'
  },
  {
    id: 'pe-cr-007-n27',
    subtopic: 'Treatment',
    title: 'How to induce puberty in boys with congenital IHH',
    content: 'Puberty induction uses low-dose intramuscular testosterone (50 to 100 mg monthly) with gradual dose escalation over 2 to 3 years and eventual shift to fortnightly dosing.',
    keyPoints: [
      'Start low to avoid rapid virilization.',
      'Increase dose every 6 months over 2-3 years.',
      'Adult replacement reaches 200-250 mg every 2-3 weeks.'
    ],
    reference: 'Testosterone induction starts at 50 to 100 mg monthly and is increased gradually over several years.'
  },
  {
    id: 'pe-cr-007-n28',
    subtopic: 'Fertility induction',
    title: 'How gonadotropin therapy induces fertility in IHH',
    content: 'hCG raises intratesticular testosterone and can start spermatogenesis in some, while small testes or absent FSH activity require combined hCG and FSH over prolonged courses.',
    keyPoints: [
      'hCG alone is used when testicular volume is >4 ml.',
      'Combine hCG with FSH when testes are <4 ml or response is absent.',
      'Predictors include larger testes and no prior androgen therapy.'
    ],
    reference: 'Fertility induction relies on hCG with or without FSH depending on testicular volume and response.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-007-q1',
    subtopic: 'Case vignette',
    question: 'A 19-year-old male has absent virilization, testes 1 ml, low LH/FSH/testosterone, normal MRI, and normal smell. The most likely diagnosis is:',
    options: [
      'Congenital normosmic isolated hypogonadotropic hypogonadism',
      'Constitutional delay in growth and puberty',
      'Klinefelter syndrome',
      'Androgen insensitivity syndrome'
    ],
    correctOption: 0,
    explanation: 'Severely low gonadotropins and testosterone with normal MRI and olfaction point to normosmic congenital IHH.',
    reference: 'Low LH/FSH with normal imaging and intact smell supports normosmic congenital IHH.'
  },
  {
    id: 'pe-cr-007-q2',
    subtopic: 'Definition',
    question: 'Delayed puberty in boys is defined as absence of testicular enlargement by age:',
    options: [
      '14 years',
      '13 years',
      '15 years',
      '12 years'
    ],
    correctOption: 0,
    explanation: 'The standard cutoff is no testicular enlargement by 14 years.',
    reference: 'Delayed puberty in boys is defined as lack of testicular enlargement by 14 years.'
  },
  {
    id: 'pe-cr-007-q3',
    subtopic: 'Definition',
    question: 'Delayed puberty in girls is defined by absence of breast development by age:',
    options: [
      '13 years',
      '12 years',
      '14 years',
      '15 years'
    ],
    correctOption: 0,
    explanation: 'Lack of thelarche by 13 years meets the definition.',
    reference: 'Delayed puberty in girls is defined as lack of breast development by 13 years.'
  },
  {
    id: 'pe-cr-007-q4',
    subtopic: 'Pubertal timing',
    question: 'Why is pubarche not used to define the onset of normal puberty?',
    options: [
      'It reflects adrenal androgen activity, not HPG-axis activation',
      'It occurs only after menarche',
      'It is always pathologic',
      'It requires ovarian estrogen production'
    ],
    correctOption: 0,
    explanation: 'Pubarche reflects adrenarche, which is independent of HPG-axis reactivation.',
    reference: 'Pubarche is a manifestation of adrenarche rather than true HPG-axis activation.'
  },
  {
    id: 'pe-cr-007-q5',
    subtopic: 'Neuroendocrine control',
    question: 'Kisspeptin activates GnRH neurons through which receptor?',
    options: [
      'GPR54',
      'FSH receptor',
      'LH receptor',
      'Androgen receptor'
    ],
    correctOption: 0,
    explanation: 'Kisspeptin binds to the GPR54 receptor on GnRH neurons.',
    reference: 'Kisspeptin acts via the GPR54 receptor on GnRH neurons.'
  },
  {
    id: 'pe-cr-007-q6',
    subtopic: 'Metabolic signals',
    question: 'Which statement best describes leptin in pubertal initiation?',
    options: [
      'It provides a permissive signal of energy sufficiency',
      'It is the sole trigger of puberty',
      'It suppresses kisspeptin secretion',
      'It directly replaces GnRH therapy'
    ],
    correctOption: 0,
    explanation: 'Leptin signals adequate energy stores and permits puberty but is not the primary trigger.',
    reference: 'Leptin has a permissive role for puberty rather than being the primary trigger.'
  },
  {
    id: 'pe-cr-007-q7',
    subtopic: 'Mini-puberty',
    question: 'In boys, gonadotropins and testosterone peak during mini-puberty at approximately:',
    options: [
      '3 months of age',
      'At birth',
      '12 months of age',
      '5 years of age'
    ],
    correctOption: 0,
    explanation: 'Gonadotropins and testosterone peak around 3 months and decline by 6-9 months.',
    reference: 'In boys, gonadotropins and testosterone peak around 3 months in mini-puberty.'
  },
  {
    id: 'pe-cr-007-q8',
    subtopic: 'Mini-puberty',
    question: 'Mini-puberty is absent in which condition?',
    options: [
      'Congenital isolated hypogonadotropic hypogonadism',
      'Partial androgen insensitivity',
      'Constitutional delay',
      'Delayed adrenarche'
    ],
    correctOption: 0,
    explanation: 'Mini-puberty is absent in congenital IHH and complete androgen insensitivity.',
    reference: 'Mini-puberty is absent in congenital IHH.'
  },
  {
    id: 'pe-cr-007-q9',
    subtopic: 'Hypogonadism',
    question: 'Low LH/FSH with low testosterone indicates:',
    options: [
      'Hypogonadotropic hypogonadism',
      'Hypergonadotropic hypogonadism',
      'Androgen resistance',
      'Normal puberty'
    ],
    correctOption: 0,
    explanation: 'Low gonadotropins with low sex steroids indicate a central defect.',
    reference: 'Hypogonadotropic hypogonadism features low LH/FSH with low testosterone.'
  },
  {
    id: 'pe-cr-007-q10',
    subtopic: 'Etiology',
    question: 'The most common cause of delayed puberty is:',
    options: [
      'Constitutional delay in growth and puberty',
      'Klinefelter syndrome',
      'Pituitary tumors',
      'Turner syndrome'
    ],
    correctOption: 0,
    explanation: 'CDGP is the leading cause, especially in boys.',
    reference: 'CDGP is the most common cause of delayed puberty.'
  },
  {
    id: 'pe-cr-007-q11',
    subtopic: 'Etiology',
    question: 'Which condition is a functional cause of hypogonadotropic hypogonadism?',
    options: [
      'Celiac disease',
      'Klinefelter syndrome',
      'Turner syndrome',
      'Primary gonadal failure after chemotherapy'
    ],
    correctOption: 0,
    explanation: 'Chronic systemic illness such as celiac disease can suppress GnRH.',
    reference: 'Functional hypogonadotropic hypogonadism can result from chronic systemic illness such as celiac disease.'
  },
  {
    id: 'pe-cr-007-q12',
    subtopic: 'Kallmann syndrome',
    question: 'Which MRI finding supports Kallmann syndrome?',
    options: [
      'Hypoplastic olfactory bulbs with absent olfactory sulci',
      'Enlarged pituitary gland',
      'Normal olfactory bulbs and sulci',
      'Calcified pineal gland'
    ],
    correctOption: 0,
    explanation: 'Olfactory bulb aplasia or hypoplasia with absent sulci is characteristic.',
    reference: 'Kallmann syndrome shows hypoplastic olfactory bulbs and absent olfactory sulci.'
  },
  {
    id: 'pe-cr-007-q13',
    subtopic: 'Kallmann syndrome',
    question: 'A standardized objective test for anosmia is:',
    options: [
      'University of Pennsylvania Smell Identification Test (UPSIT)',
      'Oral glucose tolerance test',
      'Water deprivation test',
      'ACTH stimulation test'
    ],
    correctOption: 0,
    explanation: 'UPSIT is an objective smell identification test.',
    reference: 'UPSIT is used for objective assessment of anosmia.'
  },
  {
    id: 'pe-cr-007-q14',
    subtopic: 'Kallmann syndrome',
    question: 'Which nonreproductive feature is commonly associated with Kallmann syndrome?',
    options: [
      'Bimanual synkinesia',
      'Hyperpigmentation',
      'Optic neuritis',
      'Café-au-lait spots'
    ],
    correctOption: 0,
    explanation: 'Mirror movements (synkinesia) are a classic associated feature.',
    reference: 'Synkinesia is a known nonreproductive feature of Kallmann syndrome.'
  },
  {
    id: 'pe-cr-007-q15',
    subtopic: 'Evaluation',
    question: 'A 10-year-old obese boy is thought to have a small penis. The next best step is to:',
    options: [
      'Measure stretched penile length accurately',
      'Start testosterone immediately',
      'Order pituitary MRI',
      'Begin hCG injections'
    ],
    correctOption: 0,
    explanation: 'Buried penis in obesity can mimic micropenis; accurate measurement comes first.',
    reference: 'Accurate stretched penile length measurement should precede evaluation for micropenis.'
  },
  {
    id: 'pe-cr-007-q16',
    subtopic: 'Evaluation',
    question: 'When basal LH and testosterone are prepubertal, the most useful next test to distinguish CDGP from IHH is:',
    options: [
      'GnRH stimulation test',
      'Random cortisol',
      'DEXA scan',
      'Serum prolactin only'
    ],
    correctOption: 0,
    explanation: 'GnRH stimulation can help differentiate CDGP from IHH when basal gonadotropins are low.',
    reference: 'GnRH stimulation is helpful when basal gonadotropins are in the prepubertal range.'
  },
  {
    id: 'pe-cr-007-q17',
    subtopic: 'CDGP',
    question: 'Which feature most supports CDGP over congenital IHH?',
    options: [
      'Strong family history of late puberty and delayed bone age',
      'Micropenis in infancy',
      'Anosmia',
      'Severe cryptorchidism'
    ],
    correctOption: 0,
    explanation: 'Family history and delayed bone age consistent with height age favor CDGP.',
    reference: 'CDGP is associated with family history and delayed bone age correlating with height age.'
  },
  {
    id: 'pe-cr-007-q18',
    subtopic: 'Treatment',
    question: 'An appropriate initial testosterone regimen for pubertal induction in boys with congenital IHH is:',
    options: [
      'Testosterone enanthate 50 to 100 mg intramuscularly monthly',
      'Testosterone 250 mg weekly from the start',
      'Continuous high-dose oral testosterone daily',
      'Single depot injection every 6 months'
    ],
    correctOption: 0,
    explanation: 'Induction starts with low-dose monthly injections and gradual escalation.',
    reference: 'Puberty induction begins with 50 to 100 mg testosterone monthly and escalates slowly.'
  },
  {
    id: 'pe-cr-007-q19',
    subtopic: 'Treatment',
    question: 'A typical hCG regimen for induction of pubertal virilization is:',
    options: [
      '500 to 2,000 IU subcutaneously or intramuscularly three times weekly',
      '50 IU daily',
      'Single monthly injection of 10,000 IU',
      'Oral hCG weekly'
    ],
    correctOption: 0,
    explanation: 'hCG is given multiple times per week to maintain testosterone in the mid-normal range.',
    reference: 'hCG is dosed 500 to 2,000 IU three times weekly for pubertal induction.'
  },
  {
    id: 'pe-cr-007-q20',
    subtopic: 'Gynecomastia',
    question: 'Gynecomastia is more common with hCG therapy because:',
    options: [
      'hCG increases testicular aromatase and estradiol production',
      'hCG blocks estrogen receptors',
      'hCG suppresses testosterone synthesis',
      'hCG inhibits aromatase in adipose tissue'
    ],
    correctOption: 0,
    explanation: 'hCG stimulates Leydig cell aromatase and raises estradiol.',
    reference: 'hCG increases testicular aromatase activity and estradiol production.'
  },
  {
    id: 'pe-cr-007-q21',
    subtopic: 'Klinefelter syndrome',
    question: 'The most common karyotype in Klinefelter syndrome is:',
    options: [
      '47,XXY',
      '45,X',
      '46,XY',
      '47,XYY'
    ],
    correctOption: 0,
    explanation: 'Most patients have the classic 47,XXY karyotype.',
    reference: 'Klinefelter syndrome is most commonly 47,XXY.'
  },
  {
    id: 'pe-cr-007-q22',
    subtopic: 'Klinefelter syndrome',
    question: 'Overdosage of which gene contributes to tall stature in Klinefelter syndrome?',
    options: [
      'SHOX',
      'SRY',
      'AR',
      'AMH'
    ],
    correctOption: 0,
    explanation: 'SHOX overdosage in the pseudoautosomal region drives tall stature.',
    reference: 'SHOX overdosage in Klinefelter syndrome contributes to tall stature.'
  },
  {
    id: 'pe-cr-007-q23',
    subtopic: 'Klinefelter syndrome',
    question: 'Which malignancy risk is particularly increased in Klinefelter syndrome?',
    options: [
      'Mediastinal germ cell tumors',
      'Colon cancer',
      'Melanoma',
      'Thyroid carcinoma'
    ],
    correctOption: 0,
    explanation: 'Mediastinal germ cell tumors are markedly overrepresented.',
    reference: 'Klinefelter syndrome carries increased risk of mediastinal germ cell tumors.'
  },
  {
    id: 'pe-cr-007-q24',
    subtopic: 'Gynecomastia',
    question: 'Pubertal gynecomastia most commonly occurs at:',
    options: [
      'Age 13 to 14 years or pubic hair stages P3 to P4',
      'Before age 8 years',
      'After age 20 years only',
      'Only after testosterone therapy'
    ],
    correctOption: 0,
    explanation: 'Peak pubertal gynecomastia is in early to mid-puberty.',
    reference: 'Pubertal gynecomastia commonly appears at ages 13 to 14 or stages P3 to P4.'
  },
  {
    id: 'pe-cr-007-q25',
    subtopic: 'Gynecomastia',
    question: 'Which patient with gynecomastia warrants evaluation?',
    options: [
      'Painful, rapidly enlarging gynecomastia',
      'Stable, small, painless pubertal gynecomastia',
      'Gynecomastia that has already resolved',
      'Isolated lipomastia without glandular tissue'
    ],
    correctOption: 0,
    explanation: 'Recent onset, painful, or rapid enlargement warrants evaluation.',
    reference: 'Rapid or painful gynecomastia should be evaluated regardless of size.'
  },
  {
    id: 'pe-cr-007-q26',
    subtopic: 'Differential diagnosis',
    question: 'A well-virilized male with bilateral nonpalpable testes and no androgen therapy most likely has:',
    options: [
      'Idiopathic bilateral cryptorchidism',
      'Klinefelter syndrome',
      'Congenital IHH',
      'Vanishing testes syndrome on testosterone'
    ],
    correctOption: 0,
    explanation: 'Normal virilization implies intact Leydig function, consistent with cryptorchidism.',
    reference: 'Well-virilized males with bilateral nonpalpable testes often have bilateral cryptorchidism.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-007-tf1',
    subtopic: 'Definition',
    statement: 'Delayed puberty in boys is defined by absence of testicular enlargement by age 14 years.',
    correctAnswer: true,
    explanation: 'The standard cutoff uses 14 years in boys.',
    reference: 'Delayed puberty in boys is defined as lack of testicular enlargement by 14 years.'
  },
  {
    id: 'pe-cr-007-tf2',
    subtopic: 'Pubertal timing',
    statement: 'Pubarche reflects adrenal androgen activity and is not a reliable marker of pubertal onset.',
    correctAnswer: true,
    explanation: 'Pubarche can occur without HPG-axis activation.',
    reference: 'Pubarche is a manifestation of adrenarche and does not define true puberty.'
  },
  {
    id: 'pe-cr-007-tf3',
    subtopic: 'Mini-puberty',
    statement: 'In boys, mini-puberty peaks around 3 months of age and wanes by 6 to 9 months.',
    correctAnswer: true,
    explanation: 'This timing is typical for the neonatal surge.',
    reference: 'Gonadotropins and testosterone peak around 3 months and decline by 6 to 9 months.'
  },
  {
    id: 'pe-cr-007-tf4',
    subtopic: 'Hypogonadism',
    statement: 'Hypogonadotropic hypogonadism is characterized by low LH/FSH and low sex steroids.',
    correctAnswer: true,
    explanation: 'Central defects lead to low gonadotropins and low testosterone or estradiol.',
    reference: 'Hypogonadotropic hypogonadism shows low gonadotropins with low sex steroids.'
  },
  {
    id: 'pe-cr-007-tf5',
    subtopic: 'Etiology',
    statement: 'CDGP is the most common cause of delayed puberty, especially in boys.',
    correctAnswer: true,
    explanation: 'CDGP accounts for most cases of delayed puberty in boys.',
    reference: 'CDGP is the most common cause of delayed puberty.'
  },
  {
    id: 'pe-cr-007-tf6',
    subtopic: 'Kallmann syndrome',
    statement: 'Kallmann syndrome is congenital IHH associated with anosmia.',
    correctAnswer: true,
    explanation: 'Anosmia or hyposmia is the defining feature alongside IHH.',
    reference: 'Kallmann syndrome is IHH with anosmia due to defective neuron migration.'
  },
  {
    id: 'pe-cr-007-tf7',
    subtopic: 'Evaluation',
    statement: 'MRI is indicated in hypogonadotropic hypogonadism with anosmia or other pituitary hormone deficiencies.',
    correctAnswer: true,
    explanation: 'Imaging is targeted to these higher-risk scenarios.',
    reference: 'MRI is indicated when hypogonadotropic hypogonadism is linked to anosmia or pituitary deficits.'
  },
  {
    id: 'pe-cr-007-tf8',
    subtopic: 'Treatment',
    statement: 'Testosterone induction should begin with low doses and be escalated over several years.',
    correctAnswer: true,
    explanation: 'Slow escalation mimics normal pubertal tempo.',
    reference: 'Testosterone induction is started at low doses and increased gradually over 2 to 3 years.'
  },
  {
    id: 'pe-cr-007-tf9',
    subtopic: 'Treatment',
    statement: 'hCG therapy can maintain more stable testosterone levels than exogenous testosterone injections.',
    correctAnswer: true,
    explanation: 'Leydig cell stimulation leads to steadier endogenous production.',
    reference: 'hCG provides more stable testosterone levels than exogenous injections.'
  },
  {
    id: 'pe-cr-007-tf10',
    subtopic: 'Klinefelter syndrome',
    statement: 'Most patients with Klinefelter syndrome have a 47,XXY karyotype.',
    correctAnswer: true,
    explanation: 'The classic XXY pattern is most common.',
    reference: 'The most common karyotype in Klinefelter syndrome is 47,XXY.'
  },
  {
    id: 'pe-cr-007-tf11',
    subtopic: 'Gynecomastia',
    statement: 'Painful or rapidly enlarging gynecomastia should be evaluated even if small.',
    correctAnswer: true,
    explanation: 'Recent onset or rapid progression warrants evaluation.',
    reference: 'Rapid or painful gynecomastia should be evaluated irrespective of size.'
  },
  {
    id: 'pe-cr-007-tf12',
    subtopic: 'Differential diagnosis',
    statement: 'A well-virilized male with bilateral nonpalpable testes suggests bilateral cryptorchidism.',
    correctAnswer: true,
    explanation: 'Normal virilization implies intact Leydig function.',
    reference: 'Well-virilized males with bilateral nonpalpable testes often have bilateral cryptorchidism.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-007-ar1',
    subtopic: 'Definition',
    assertion: 'Delayed puberty in boys is defined by absence of testicular enlargement by 14 years.',
    reason: 'The cutoff represents about 2.5 standard deviations above the mean pubertal onset.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the cutoff.',
    reference: 'Cutoffs for delayed puberty correspond to about +2.5 SD from mean pubertal onset.'
  },
  {
    id: 'pe-cr-007-ar2',
    subtopic: 'Pubertal timing',
    assertion: 'Pubarche is not used to define pubertal onset.',
    reason: 'Pubarche reflects adrenal androgen activity independent of HPG-axis activation.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Pubarche is driven by adrenarche and does not indicate HPG-axis reactivation.'
  },
  {
    id: 'pe-cr-007-ar3',
    subtopic: 'Neuroendocrine control',
    assertion: 'Kisspeptin stimulates GnRH neurons.',
    reason: 'Kisspeptin acts via the GPR54 receptor on GnRH neurons.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the mechanism.',
    reference: 'Kisspeptin activates GnRH neurons through the GPR54 receptor.'
  },
  {
    id: 'pe-cr-007-ar4',
    subtopic: 'Mini-puberty',
    assertion: 'Mini-puberty in boys peaks around 3 months of age.',
    reason: 'Placental estrogen withdrawal triggers a neonatal surge of gonadotropins and testosterone.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the timing.',
    reference: 'Mini-puberty is a neonatal surge after placental estrogen withdrawal, peaking around 3 months in boys.'
  },
  {
    id: 'pe-cr-007-ar5',
    subtopic: 'Etiology',
    assertion: 'CDGP is the most common cause of delayed puberty.',
    reason: 'Most adolescents with CDGP spontaneously enter puberty by 18 years.',
    correctOption: 1,
    explanation: 'Both statements are true, but spontaneous entry by 18 years does not explain why CDGP is most common.',
    reference: 'CDGP is the most common cause of delayed puberty, and many enter puberty by 18 years.'
  },
  {
    id: 'pe-cr-007-ar6',
    subtopic: 'Kallmann syndrome',
    assertion: 'Kallmann syndrome includes anosmia or hyposmia.',
    reason: 'Olfactory and GnRH neurons migrate together from the olfactory placode.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the anosmia.',
    reference: 'Kallmann syndrome results from failed migration of olfactory and GnRH neurons.'
  },
  {
    id: 'pe-cr-007-ar7',
    subtopic: 'Evaluation',
    assertion: 'MRI is mandatory in every patient with hypogonadotropic hypogonadism.',
    reason: 'MRI is indicated when anosmia, pituitary hormone deficits, or mass effect are present.',
    correctOption: 3,
    explanation: 'The assertion is false; MRI is individualized based on risk features.',
    reference: 'MRI is recommended in hypogonadotropic hypogonadism when associated risk features are present.'
  },
  {
    id: 'pe-cr-007-ar8',
    subtopic: 'Treatment',
    assertion: 'Testosterone therapy alone reliably induces spermatogenesis in congenital IHH.',
    reason: 'Intratesticular testosterone levels must be high and are best achieved with hCG.',
    correctOption: 2,
    explanation: 'The assertion is false, but the reason is true.',
    reference: 'Testosterone therapy induces virilization but does not reliably induce spermatogenesis; hCG supports intratesticular testosterone.'
  },
  {
    id: 'pe-cr-007-ar9',
    subtopic: 'Klinefelter syndrome',
    assertion: 'Klinefelter syndrome typically has small, firm testes and elevated gonadotropins.',
    reason: 'Primary gonadal failure leads to high LH and FSH.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the labs.',
    reference: 'Klinefelter syndrome is hypergonadotropic with small firm testes.'
  },
  {
    id: 'pe-cr-007-ar10',
    subtopic: 'Gynecomastia',
    assertion: 'Pubertal gynecomastia is usually transient.',
    reason: 'It is due to a temporary imbalance favoring estradiol over testosterone.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the transient nature.',
    reference: 'Pubertal gynecomastia reflects a temporary estradiol to testosterone imbalance and often resolves.'
  },
  {
    id: 'pe-cr-007-ar11',
    subtopic: 'Differential diagnosis',
    assertion: 'Well-virilized males with bilateral nonpalpable testes often have cryptorchidism.',
    reason: 'Leydig cell testosterone production is preserved even when germ cells are damaged by heat.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the preserved virilization.',
    reference: 'Leydig cells are heat resistant, allowing virilization despite cryptorchidism.'
  },
  {
    id: 'pe-cr-007-ar12',
    subtopic: 'Treatment',
    assertion: 'Gynecomastia is more common with hCG therapy than with testosterone.',
    reason: 'hCG increases testicular aromatase activity and estradiol production.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the difference.',
    reference: 'hCG stimulates aromatase activity, increasing estradiol and gynecomastia risk.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-007',
  book: 'clinical_rounds',
  chapterNo: '7',
  title: 'Delayed Puberty',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/007_delayed_puberty',
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
