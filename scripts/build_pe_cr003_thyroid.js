#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-003_thyroid_disorders_in_children.json'
);

const notes = [
  {
    id: 'pe-cr-003-n1',
    subtopic: 'Congenital hypothyroidism',
    title: 'Why congenital hypothyroidism is treated urgently',
    content: 'Thyroid hormone is essential for early brain development, so delayed therapy in congenital hypothyroidism risks irreversible neurocognitive impairment.',
    keyPoints: [
      'Thyroid hormone supports neuronal migration and myelination.',
      'Neurodevelopmental injury is time sensitive.',
      'Early treatment improves IQ outcomes.'
    ],
    reference: 'Congenital hypothyroidism: delayed treatment risks irreversible neurodevelopmental injury.'
  },
  {
    id: 'pe-cr-003-n2',
    subtopic: 'Maternal thyroid hormone',
    title: 'Why maternal T4 supports fetal brain development',
    content: 'Before the fetal thyroid is fully functional, maternal T4 crosses the placenta and supports cortical development; severe maternal hypothyroxinemia can impair fetal neurodevelopment.',
    keyPoints: [
      'Maternal T4 is the main source in early gestation.',
      'Fetal brain development depends on adequate T4.',
      'Maternal hypothyroxinemia increases neurocognitive risk.'
    ],
    reference: 'Maternal T4: critical for fetal brain development before fetal thyroid maturity.'
  },
  {
    id: 'pe-cr-003-n3',
    subtopic: 'Screening physiology',
    title: 'How the neonatal TSH surge affects screening timing',
    content: 'A physiologic TSH surge occurs in the first day of life, so screening is ideally performed after 24–48 hours to reduce false positives.',
    keyPoints: [
      'TSH rises sharply after birth.',
      'Early samples can overestimate hypothyroidism.',
      'Later sampling improves specificity.'
    ],
    reference: 'Neonatal TSH surge: early samples can yield false-positive screens.'
  },
  {
    id: 'pe-cr-003-n4',
    subtopic: 'Newborn screening',
    title: 'How TSH-first and T4-backup screening strategies differ',
    content: 'TSH-first screening detects primary hypothyroidism, while T4-backup programs can also catch central hypothyroidism or delayed TSH rise.',
    keyPoints: [
      'TSH-first focuses on primary CH.',
      'T4-backup can detect central disease.',
      'Delayed TSH rise may need repeat sampling.'
    ],
    reference: 'Screening: TSH-first targets primary CH; T4-backup broadens detection.'
  },
  {
    id: 'pe-cr-003-n5',
    subtopic: 'Screening samples',
    title: 'Why cord blood thyroid tests are limited',
    content: 'Cord blood values can be influenced by perinatal stress and do not reliably capture the postnatal TSH surge, reducing their accuracy as a sole screen.',
    keyPoints: [
      'Cord samples miss the postnatal TSH rise.',
      'Perinatal factors alter cord thyroid values.',
      'Heel-stick screening remains standard.'
    ],
    reference: 'Cord blood screening: limited sensitivity because it misses the postnatal TSH surge.'
  },
  {
    id: 'pe-cr-003-n6',
    subtopic: 'Transient CH',
    title: 'How to recognize transient congenital hypothyroidism',
    content: 'Transient CH is suggested by mild TSH elevation, improving thyroid function over time, or known exposures such as iodine excess, prematurity, or maternal antibodies.',
    keyPoints: [
      'Often mild and improves over months.',
      'Prematurity or iodine exposure are clues.',
      'Re-evaluate after age 3.'
    ],
    reference: 'Transient CH: consider iodine exposure, prematurity, or maternal antibodies with improving labs.'
  },
  {
    id: 'pe-cr-003-n7',
    subtopic: 'Dyshormonogenesis',
    title: 'Why dyshormonogenesis often causes goiter',
    content: 'Defects in thyroid hormone synthesis raise TSH chronically, stimulating thyroid growth and leading to an enlarged, hyperplastic gland.',
    keyPoints: [
      'Synthesis defects increase TSH.',
      'TSH drives thyroid hyperplasia.',
      'Goiter may be present at birth or infancy.'
    ],
    reference: 'Dyshormonogenesis: chronic TSH stimulation causes goiter.'
  },
  {
    id: 'pe-cr-003-n8',
    subtopic: 'Iodine deficiency',
    title: 'Why iodine deficiency leads to endemic cretinism',
    content: 'In areas of severe iodine deficiency, maternal and fetal hypothyroidism cause irreversible neurodevelopmental impairment and growth failure in infants.',
    keyPoints: [
      'Iodine is required for thyroid hormone synthesis.',
      'Maternal and fetal deficiency co-exist.',
      'Neurocognitive injury is severe without prevention.'
    ],
    reference: 'Endemic cretinism: severe iodine deficiency causes irreversible neurodevelopmental impairment.'
  },
  {
    id: 'pe-cr-003-n9',
    subtopic: 'Iodine intake',
    title: 'How pediatric iodine requirements change with age',
    content: 'Iodine requirements increase from infancy through adolescence; both deficiency and excess can disrupt thyroid function.',
    keyPoints: [
      'Needs rise as children grow.',
      'Deficiency impairs hormone synthesis.',
      'Excess iodine can also cause hypothyroidism.'
    ],
    reference: 'Iodine intake: requirements rise with age; deficiency or excess disrupts thyroid function.'
  },
  {
    id: 'pe-cr-003-n10',
    subtopic: 'Juvenile hypothyroidism',
    title: 'How juvenile hypothyroidism typically presents',
    content: 'School-age hypothyroidism often presents with poor growth, weight gain, fatigue, cold intolerance, and delayed bone age rather than classic infant signs.',
    keyPoints: [
      'Growth deceleration is common.',
      'Weight gain may be modest relative to short stature.',
      'Bone age is delayed.'
    ],
    reference: 'Juvenile hypothyroidism: growth failure and delayed bone age are key clues.'
  },
  {
    id: 'pe-cr-003-n11',
    subtopic: 'Autoimmune thyroiditis',
    title: 'Why Hashimoto thyroiditis is the most common cause of acquired hypothyroidism',
    content: 'Autoimmune destruction of thyroid tissue is prevalent in older children and adolescents, often with goiter and thyroid autoantibodies.',
    keyPoints: [
      'Anti-TPO and anti-Tg antibodies are common.',
      'Goiter may be present.',
      'Progressive hypothyroidism can occur.'
    ],
    reference: 'Hashimoto thyroiditis: the leading cause of acquired hypothyroidism in children.'
  },
  {
    id: 'pe-cr-003-n12',
    subtopic: 'Van Wyk-Grumbach',
    title: 'How severe hypothyroidism causes precocious puberty',
    content: 'Very high TSH can stimulate FSH receptors and increase prolactin, leading to ovarian cysts, vaginal bleeding, and delayed bone age despite pubertal signs.',
    keyPoints: [
      'Precocious puberty with delayed bone age is characteristic.',
      'Ovarian enlargement or cysts may appear.',
      'TSH can cross-react with gonadotropin receptors.'
    ],
    reference: 'Van Wyk-Grumbach: severe hypothyroidism can cause precocious puberty with delayed bone age.'
  },
  {
    id: 'pe-cr-003-n13',
    subtopic: 'Ovarian findings',
    title: 'Why multicystic ovaries occur in hypothyroidism',
    content: 'Prolonged hypothyroidism increases TRH and prolactin and allows TSH cross-reactivity with FSH receptors, promoting ovarian stimulation and cyst formation.',
    keyPoints: [
      'TSH can activate FSH receptors.',
      'Hyperprolactinemia contributes to gonadal effects.',
      'Cysts regress with thyroid replacement.'
    ],
    reference: 'Multicystic ovaries: severe hypothyroidism stimulates ovaries via TSH and prolactin.'
  },
  {
    id: 'pe-cr-003-n14',
    subtopic: 'Pituitary hyperplasia',
    title: 'How thyrotroph hyperplasia mimics a pituitary tumor',
    content: 'Long-standing primary hypothyroidism can cause pituitary enlargement from thyrotroph hyperplasia, which regresses after adequate L-T4 replacement.',
    keyPoints: [
      'Pituitary enlargement is reactive, not neoplastic.',
      'Markedly elevated TSH is a clue.',
      'Size decreases after thyroid hormone therapy.'
    ],
    reference: 'Pituitary hyperplasia: chronic primary hypothyroidism can mimic pituitary mass.'
  },
  {
    id: 'pe-cr-003-n15',
    subtopic: 'Skeletal features',
    title: 'Why stippled epiphyses appear in congenital hypothyroidism',
    content: 'Thyroid hormone is required for normal endochondral ossification; deficiency leads to epiphyseal dysgenesis and stippling on imaging.',
    keyPoints: [
      'Epiphyseal maturation is delayed.',
      'Radiographs show stippled epiphyses.',
      'Improves with early hormone replacement.'
    ],
    reference: 'Stippled epiphyses: thyroid hormone deficiency disrupts ossification.'
  },
  {
    id: 'pe-cr-003-n16',
    subtopic: 'Orthopedic complications',
    title: 'How hypothyroidism predisposes to slipped capital femoral epiphysis',
    content: 'Delayed epiphyseal maturation and obesity related to hypothyroidism increase the risk of SCFE in older children.',
    keyPoints: [
      'Delayed skeletal maturation weakens the physis.',
      'Weight gain adds mechanical stress.',
      'Hip or knee pain warrants urgent evaluation.'
    ],
    reference: 'SCFE risk: delayed maturation and weight gain in hypothyroidism increase susceptibility.'
  },
  {
    id: 'pe-cr-003-n17',
    subtopic: 'Diagnostic testing',
    title: 'How the perchlorate discharge test identifies iodide organification defects',
    content: 'Perchlorate blocks iodide trapping; release of radioactive iodide after perchlorate suggests failed organification and points toward dyshormonogenesis.',
    keyPoints: [
      'Iodide organification defects show a positive discharge.',
      'Perchlorate blocks further iodide uptake.',
      'Used when dyshormonogenesis is suspected.'
    ],
    reference: 'Perchlorate discharge: iodide release after perchlorate suggests organification defect.'
  },
  {
    id: 'pe-cr-003-n18',
    subtopic: 'Central hypothyroidism',
    title: 'How secondary hypothyroidism differs from primary disease',
    content: 'Central hypothyroidism presents with low free T4 and inappropriately normal or low TSH, often accompanied by other pituitary hormone deficiencies.',
    keyPoints: [
      'TSH is not elevated despite low free T4.',
      'Look for other pituitary deficits.',
      'Pituitary imaging may be required.'
    ],
    reference: 'Secondary hypothyroidism: low free T4 with non-elevated TSH suggests central disease.'
  },
  {
    id: 'pe-cr-003-n19',
    subtopic: 'Neonatal Graves',
    title: 'Why maternal TRAb can cause neonatal thyrotoxicosis',
    content: 'TSH receptor antibodies cross the placenta and can stimulate the fetal thyroid, causing neonatal Graves disease even if the mother is euthyroid.',
    keyPoints: [
      'TRAb crosses the placenta.',
      'Neonatal disease can occur after maternal treatment.',
      'Monitoring is needed when maternal TRAb is high.'
    ],
    reference: 'Neonatal Graves: transplacental TRAb can stimulate the fetal thyroid.'
  },
  {
    id: 'pe-cr-003-n20',
    subtopic: 'Neonatal Graves',
    title: 'How neonatal Graves disease is treated',
    content: 'Treatment includes antithyroid medication (usually methimazole), beta blockade, and supportive care, with close monitoring until maternal antibodies clear.',
    keyPoints: [
      'Methimazole is the preferred antithyroid agent.',
      'Beta blockers control adrenergic symptoms.',
      'Disease is transient as antibodies decline.'
    ],
    reference: 'Neonatal Graves: methimazole and beta blockade are typical treatments until TRAb clears.'
  },
  {
    id: 'pe-cr-003-n21',
    subtopic: 'Childhood Graves',
    title: 'How to treat childhood Graves disease',
    content: 'Initial therapy uses methimazole with beta blockade when symptomatic; definitive therapy can be radioiodine or surgery when remission is unlikely.',
    keyPoints: [
      'Methimazole is first-line.',
      'Beta blockers treat tachycardia and tremor.',
      'Definitive therapy is considered for relapsing disease.'
    ],
    reference: 'Childhood Graves: methimazole first-line with beta blockers; definitive therapy for relapse.'
  },
  {
    id: 'pe-cr-003-n22',
    subtopic: 'Antithyroid drugs',
    title: 'Why methimazole is preferred over propylthiouracil in children',
    content: 'Methimazole has a safer hepatic profile, while propylthiouracil carries a higher risk of severe liver injury in children.',
    keyPoints: [
      'PTU has rare but severe hepatotoxicity.',
      'Methimazole is effective and safer.',
      'PTU is generally avoided in pediatrics.'
    ],
    reference: 'Antithyroid therapy: methimazole is preferred because PTU can cause severe liver injury.'
  },
  {
    id: 'pe-cr-003-n23',
    subtopic: 'Thyroid storm',
    title: 'How pediatric thyroid storm is recognized and managed',
    content: 'Thyroid storm presents with hyperthermia, tachycardia, CNS dysfunction, and GI symptoms; management includes beta blockade, antithyroid drugs, iodine, and supportive care.',
    keyPoints: [
      'Look for fever, tachyarrhythmia, and agitation.',
      'Use methimazole and iodine after blocking hormone synthesis.',
      'Provide aggressive supportive care.'
    ],
    reference: 'Thyroid storm: requires beta blockade, antithyroid therapy, iodine, and supportive care.'
  },
  {
    id: 'pe-cr-003-n24',
    subtopic: 'McCune-Albright',
    title: 'How McCune-Albright syndrome causes hyperthyroidism',
    content: 'Activating GNAS mutations can lead to autonomous thyroid hormone production, often with nodular goiter and suppressed TSH.',
    keyPoints: [
      'GNAS activation drives autonomous hormone production.',
      'Thyroid nodules and goiter are common.',
      'Suppressed TSH with high T4/T3 suggests autonomy.'
    ],
    reference: 'McCune-Albright: autonomous thyroid hormone production from GNAS activation.'
  },
  {
    id: 'pe-cr-003-n25',
    subtopic: 'Subclinical hypothyroidism',
    title: 'Why mild TSH elevation often warrants monitoring rather than immediate therapy',
    content: 'Subclinical hypothyroidism with normal free T4 and minimal symptoms can be observed with repeat testing, particularly when TSH is only mildly elevated.',
    keyPoints: [
      'Check for thyroid antibodies and symptoms.',
      'Repeat labs to confirm persistence.',
      'Treat if TSH rises or symptoms develop.'
    ],
    reference: 'Subclinical hypothyroidism: mild TSH elevation with normal free T4 can be monitored.'
  },
  {
    id: 'pe-cr-003-n26',
    subtopic: 'Laboratory patterns',
    title: 'How to interpret low T4 with normal TSH in children',
    content: 'Low free T4 with non-elevated TSH suggests central hypothyroidism or non-thyroidal illness, warranting broader pituitary evaluation.',
    keyPoints: [
      'Inappropriately normal TSH is abnormal.',
      'Assess other pituitary axes.',
      'Consider non-thyroidal illness in acute disease.'
    ],
    reference: 'Low free T4 with non-elevated TSH suggests central disease or non-thyroidal illness.'
  },
  {
    id: 'pe-cr-003-n27',
    subtopic: 'Replacement therapy',
    title: 'Why L-T4 titration should be gradual in long-standing hypothyroidism',
    content: 'In long-standing hypothyroidism, rapid full-dose replacement can precipitate symptoms of hyperthyroidism or cardiac stress; gradual titration is safer.',
    keyPoints: [
      'Start with lower doses in chronic disease.',
      'Increase gradually while monitoring symptoms.',
      'Avoid overtreatment and tachycardia.'
    ],
    reference: 'Long-standing hypothyroidism: gradual L-T4 titration reduces adverse effects.'
  },
  {
    id: 'pe-cr-003-n28',
    subtopic: 'Adrenal axis',
    title: 'Why adrenal function should be assessed before high-dose thyroid replacement',
    content: 'In patients with possible central hypothyroidism or pituitary disease, thyroid replacement can increase cortisol clearance and precipitate adrenal crisis if cortisol reserve is low.',
    keyPoints: [
      'Check for symptoms of cortisol deficiency.',
      'Measure morning cortisol or ACTH-stim test if needed.',
      'Treat adrenal insufficiency before full thyroid replacement.'
    ],
    reference: 'Adrenal axis: evaluate cortisol reserve before high-dose thyroid replacement in central disease.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-003-q1',
    subtopic: 'Congenital hypothyroidism',
    question: 'Which outcome is most strongly linked to delayed treatment of congenital hypothyroidism?',
    options: [
      'Permanent neurocognitive impairment',
      'Early closure of fontanelles',
      'Hyperactivity in early childhood',
      'Accelerated bone age'
    ],
    correctOption: 0,
    explanation: 'Delayed thyroid hormone replacement can cause irreversible neurodevelopmental injury.',
    reference: 'Congenital hypothyroidism: delayed treatment risks irreversible neurodevelopmental injury.'
  },
  {
    id: 'pe-cr-003-q2',
    subtopic: 'Maternal thyroid hormone',
    question: 'During early gestation, the primary source of thyroid hormone for the fetus is:',
    options: [
      'Fetal thyroid gland',
      'Maternal T4 crossing the placenta',
      'Placental T3 production',
      'Pituitary TSH secretion'
    ],
    correctOption: 1,
    explanation: 'Maternal T4 supports fetal brain development before fetal thyroid maturity.',
    reference: 'Maternal T4: critical for fetal neurodevelopment before fetal thyroid function is established.'
  },
  {
    id: 'pe-cr-003-q3',
    subtopic: 'Screening physiology',
    question: 'Why is newborn screening ideally performed after 24–48 hours of life?',
    options: [
      'To allow the neonatal TSH surge to settle',
      'Because T4 cannot be measured earlier',
      'Because maternal TSH must clear',
      'To detect only central hypothyroidism'
    ],
    correctOption: 0,
    explanation: 'Early sampling can be confounded by the physiologic postnatal TSH surge.',
    reference: 'Neonatal TSH surge: early samples can yield false-positive screens.'
  },
  {
    id: 'pe-cr-003-q4',
    subtopic: 'Newborn screening',
    question: 'A T4-backup newborn screening program is most likely to detect which condition?',
    options: [
      'Central hypothyroidism',
      'Neonatal hyperthyroidism',
      'Transient hyperthyroxinemia',
      'Thyroid hormone resistance'
    ],
    correctOption: 0,
    explanation: 'T4-backup helps identify central hypothyroidism or delayed TSH rise.',
    reference: 'Screening: T4-backup broadens detection beyond primary hypothyroidism.'
  },
  {
    id: 'pe-cr-003-q5',
    subtopic: 'Transient CH',
    question: 'Which scenario most suggests transient congenital hypothyroidism?',
    options: [
      'Mild TSH elevation that normalizes on follow-up',
      'Large goiter and permanent high TSH',
      'Absent thyroid gland on ultrasound',
      'Persistent low free T4 despite therapy'
    ],
    correctOption: 0,
    explanation: 'Transient CH often shows mild abnormalities that improve over time.',
    reference: 'Transient CH: improving labs and mild elevation suggest transient disease.'
  },
  {
    id: 'pe-cr-003-q6',
    subtopic: 'Dyshormonogenesis',
    question: 'Which finding best supports dyshormonogenesis as the cause of congenital hypothyroidism?',
    options: [
      'Goiter with elevated TSH',
      'Absent thyroid gland on imaging',
      'Low thyroglobulin levels with no goiter',
      'Suppressed TSH with high T4'
    ],
    correctOption: 0,
    explanation: 'Synthesis defects cause chronic TSH stimulation and goiter.',
    reference: 'Dyshormonogenesis: chronic TSH stimulation causes goiter.'
  },
  {
    id: 'pe-cr-003-q7',
    subtopic: 'Iodine deficiency',
    question: 'Endemic cretinism is primarily caused by:',
    options: [
      'Severe iodine deficiency during pregnancy',
      'Maternal hyperthyroidism',
      'Neonatal TSH surge',
      'Excess iodine intake'
    ],
    correctOption: 0,
    explanation: 'Severe iodine deficiency in pregnancy leads to fetal and neonatal hypothyroidism.',
    reference: 'Endemic cretinism: severe iodine deficiency causes irreversible neurodevelopmental impairment.'
  },
  {
    id: 'pe-cr-003-q8',
    subtopic: 'Juvenile hypothyroidism',
    question: 'Which presentation is most typical of juvenile hypothyroidism?',
    options: [
      'Growth deceleration with delayed bone age',
      'Accelerated height velocity',
      'Advanced bone age with tall stature',
      'Isolated hypertension'
    ],
    correctOption: 0,
    explanation: 'School-age hypothyroidism often presents with poor growth and delayed bone age.',
    reference: 'Juvenile hypothyroidism: growth failure and delayed bone age are key clues.'
  },
  {
    id: 'pe-cr-003-q9',
    subtopic: 'Van Wyk-Grumbach',
    question: 'Precocious puberty with delayed bone age in a child should raise concern for:',
    options: [
      'Severe hypothyroidism',
      'Central precocious puberty',
      'Androgen-secreting tumor',
      'Congenital adrenal hyperplasia'
    ],
    correctOption: 0,
    explanation: 'Van Wyk-Grumbach syndrome causes pubertal signs with delayed bone age.',
    reference: 'Van Wyk-Grumbach: severe hypothyroidism causes precocious puberty with delayed bone age.'
  },
  {
    id: 'pe-cr-003-q10',
    subtopic: 'Pituitary hyperplasia',
    question: 'A 14-year-old with severe hypothyroidism has a large pituitary on MRI. The most likely explanation is:',
    options: [
      'Thyrotroph hyperplasia',
      'Pituitary adenoma with hormone secretion',
      'Craniopharyngioma',
      'Pituitary apoplexy'
    ],
    correctOption: 0,
    explanation: 'Chronic primary hypothyroidism can cause pituitary enlargement that regresses with therapy.',
    reference: 'Pituitary hyperplasia: chronic hypothyroidism can mimic a pituitary mass.'
  },
  {
    id: 'pe-cr-003-q11',
    subtopic: 'Skeletal features',
    question: 'Stippled epiphyses in a neonate most strongly suggest:',
    options: [
      'Congenital hypothyroidism',
      'Congenital adrenal hyperplasia',
      'Vitamin D intoxication',
      'Hyperparathyroidism'
    ],
    correctOption: 0,
    explanation: 'Thyroid hormone deficiency disrupts ossification and causes stippled epiphyses.',
    reference: 'Stippled epiphyses: thyroid hormone deficiency disrupts ossification.'
  },
  {
    id: 'pe-cr-003-q12',
    subtopic: 'Orthopedic complications',
    question: 'Which endocrine condition increases risk for slipped capital femoral epiphysis?',
    options: [
      'Hypothyroidism',
      'Hyperthyroidism',
      'Central diabetes insipidus',
      'Hypoparathyroidism'
    ],
    correctOption: 0,
    explanation: 'Delayed maturation and weight gain in hypothyroidism predispose to SCFE.',
    reference: 'SCFE risk: delayed maturation and weight gain in hypothyroidism increase susceptibility.'
  },
  {
    id: 'pe-cr-003-q13',
    subtopic: 'Diagnostic testing',
    question: 'A positive perchlorate discharge test indicates:',
    options: [
      'An iodide organification defect',
      'Thyroid agenesis',
      'Central hypothyroidism',
      'Hyperthyroidism from Graves disease'
    ],
    correctOption: 0,
    explanation: 'Iodide release after perchlorate suggests failed organification.',
    reference: 'Perchlorate discharge: iodide release after perchlorate suggests organification defect.'
  },
  {
    id: 'pe-cr-003-q14',
    subtopic: 'Central hypothyroidism',
    question: 'Which lab pattern most supports secondary hypothyroidism?',
    options: [
      'Low free T4 with low/normal TSH',
      'High free T4 with low TSH',
      'High free T4 with high TSH',
      'Normal free T4 with high TSH'
    ],
    correctOption: 0,
    explanation: 'Central hypothyroidism shows low T4 with inappropriately non-elevated TSH.',
    reference: 'Secondary hypothyroidism: low free T4 with non-elevated TSH.'
  },
  {
    id: 'pe-cr-003-q15',
    subtopic: 'Neonatal Graves',
    question: 'Which maternal factor most predicts neonatal Graves disease?',
    options: [
      'High maternal TRAb levels',
      'Maternal hypothyroxinemia',
      'Maternal iodine deficiency',
      'Maternal thyroid surgery history alone'
    ],
    correctOption: 0,
    explanation: 'Transplacental TRAb stimulate the fetal thyroid.',
    reference: 'Neonatal Graves: transplacental TRAb can stimulate the fetal thyroid.'
  },
  {
    id: 'pe-cr-003-q16',
    subtopic: 'Neonatal Graves',
    question: 'The most appropriate initial therapy for neonatal Graves disease is:',
    options: [
      'Methimazole with beta blockade',
      'Levothyroxine replacement',
      'Radioiodine ablation',
      'Observation only'
    ],
    correctOption: 0,
    explanation: 'Methimazole and beta blockers control hormone production and symptoms.',
    reference: 'Neonatal Graves: methimazole and beta blockade are typical treatments.'
  },
  {
    id: 'pe-cr-003-q17',
    subtopic: 'Childhood Graves',
    question: 'Which medication is first-line for pediatric Graves disease?',
    options: [
      'Methimazole',
      'Propylthiouracil',
      'Radioiodine',
      'Lithium'
    ],
    correctOption: 0,
    explanation: 'Methimazole is preferred due to safety and efficacy.',
    reference: 'Childhood Graves: methimazole is first-line therapy.'
  },
  {
    id: 'pe-cr-003-q18',
    subtopic: 'Antithyroid drugs',
    question: 'Why is propylthiouracil avoided in children?',
    options: [
      'Higher risk of severe hepatotoxicity',
      'Lower efficacy in suppressing T4',
      'Causes congenital hypothyroidism',
      'Cannot be used with beta blockers'
    ],
    correctOption: 0,
    explanation: 'PTU carries a rare but serious risk of liver failure.',
    reference: 'Antithyroid therapy: PTU can cause severe liver injury.'
  },
  {
    id: 'pe-cr-003-q19',
    subtopic: 'Thyroid storm',
    question: 'A febrile child with hyperthyroidism, tachycardia, agitation, and diarrhea most likely has:',
    options: [
      'Thyroid storm',
      'Myxedema coma',
      'Transient thyrotoxicosis',
      'Adrenal crisis'
    ],
    correctOption: 0,
    explanation: 'Thyroid storm presents with hyperthermia, adrenergic symptoms, and GI/CNS dysfunction.',
    reference: 'Thyroid storm: fever, tachycardia, and CNS/GI dysfunction are classic.'
  },
  {
    id: 'pe-cr-003-q20',
    subtopic: 'McCune-Albright',
    question: 'Which thyroid feature is most typical in McCune-Albright syndrome?',
    options: [
      'Autonomous hyperthyroidism with nodular goiter',
      'Congenital thyroid agenesis',
      'Central hypothyroidism',
      'Thyroid hormone resistance'
    ],
    correctOption: 0,
    explanation: 'GNAS activation causes autonomous hormone production and nodular goiter.',
    reference: 'McCune-Albright: autonomous thyroid hormone production with nodular goiter.'
  },
  {
    id: 'pe-cr-003-q21',
    subtopic: 'Replacement therapy',
    question: 'In long-standing severe hypothyroidism, the best levothyroxine strategy is to:',
    options: [
      'Start low and titrate gradually',
      'Start at full weight-based dose',
      'Delay treatment until pubertal completion',
      'Use liothyronine monotherapy'
    ],
    correctOption: 0,
    explanation: 'Gradual titration avoids symptoms of overtreatment and cardiac stress.',
    reference: 'Long-standing hypothyroidism: gradual L-T4 titration reduces adverse effects.'
  },
  {
    id: 'pe-cr-003-q22',
    subtopic: 'Subclinical hypothyroidism',
    question: 'A child has TSH 6 mIU/L with normal free T4 and no symptoms. The best next step is:',
    options: [
      'Repeat thyroid function tests and monitor',
      'Start high-dose levothyroxine immediately',
      'Order emergent pituitary MRI',
      'Begin antithyroid medication'
    ],
    correctOption: 0,
    explanation: 'Mild subclinical hypothyroidism can be monitored with repeat labs.',
    reference: 'Subclinical hypothyroidism: mild TSH elevation with normal free T4 can be monitored.'
  },
  {
    id: 'pe-cr-003-q23',
    subtopic: 'Laboratory patterns',
    question: 'Low free T4 with a normal TSH most strongly suggests:',
    options: [
      'Central hypothyroidism',
      'Primary hypothyroidism',
      'Graves disease',
      'Thyroid hormone resistance'
    ],
    correctOption: 0,
    explanation: 'A non-elevated TSH with low T4 indicates central disease.',
    reference: 'Low free T4 with non-elevated TSH suggests central disease.'
  },
  {
    id: 'pe-cr-003-q24',
    subtopic: 'Van Wyk-Grumbach',
    question: 'A 14-year-old girl with longstanding hypothyroidism, ovarian cysts, and a pituitary mass most likely has:',
    options: [
      'Van Wyk-Grumbach phenomenon',
      'Central precocious puberty',
      'Gonadotropin-secreting adenoma',
      'Cushing disease'
    ],
    correctOption: 0,
    explanation: 'Severe hypothyroidism can cause ovarian cysts and pituitary hyperplasia.',
    reference: 'Van Wyk-Grumbach: severe hypothyroidism can cause ovarian cysts and pituitary hyperplasia.'
  },
  {
    id: 'pe-cr-003-q25',
    subtopic: 'Adrenal axis',
    question: 'Why should adrenal function be assessed before full thyroid replacement in suspected central disease?',
    options: [
      'Thyroid hormone can increase cortisol clearance and precipitate crisis',
      'Thyroid hormone suppresses aldosterone',
      'Levothyroxine reduces ACTH secretion permanently',
      'Cortisol always rises with hypothyroidism'
    ],
    correctOption: 0,
    explanation: 'Replacing thyroid hormone can unmask cortisol deficiency if adrenal reserve is low.',
    reference: 'Adrenal axis: evaluate cortisol reserve before high-dose thyroid replacement in central disease.'
  },
  {
    id: 'pe-cr-003-q26',
    subtopic: 'Screening samples',
    question: 'Which statement best describes cord blood thyroid testing?',
    options: [
      'It can miss the postnatal TSH surge and is less reliable alone',
      'It is the preferred single screening method worldwide',
      'It always detects central hypothyroidism',
      'It is unaffected by perinatal stress'
    ],
    correctOption: 0,
    explanation: 'Cord blood testing misses the postnatal TSH surge and can be less sensitive.',
    reference: 'Cord blood screening: limited sensitivity because it misses the postnatal TSH surge.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-003-tf1',
    subtopic: 'Congenital hypothyroidism',
    statement: 'Delayed treatment of congenital hypothyroidism can lead to permanent neurodevelopmental impairment.',
    correctAnswer: true,
    explanation: 'Early replacement is crucial for brain development.',
    reference: 'Congenital hypothyroidism: delayed treatment risks irreversible neurodevelopmental injury.'
  },
  {
    id: 'pe-cr-003-tf2',
    subtopic: 'Screening physiology',
    statement: 'The physiologic neonatal TSH surge can cause false-positive screens if samples are collected too early.',
    correctAnswer: true,
    explanation: 'TSH rises immediately after birth and settles later.',
    reference: 'Neonatal TSH surge: early samples can yield false-positive screens.'
  },
  {
    id: 'pe-cr-003-tf3',
    subtopic: 'Newborn screening',
    statement: 'T4-backup screening can detect central hypothyroidism that might be missed by TSH-only programs.',
    correctAnswer: true,
    explanation: 'Central disease may not show an elevated TSH.',
    reference: 'Screening: T4-backup broadens detection beyond primary hypothyroidism.'
  },
  {
    id: 'pe-cr-003-tf4',
    subtopic: 'Dyshormonogenesis',
    statement: 'Dyshormonogenesis commonly presents with goiter due to chronic TSH stimulation.',
    correctAnswer: true,
    explanation: 'Synthesis defects lead to persistent TSH elevation.',
    reference: 'Dyshormonogenesis: chronic TSH stimulation causes goiter.'
  },
  {
    id: 'pe-cr-003-tf5',
    subtopic: 'Iodine deficiency',
    statement: 'Severe iodine deficiency during pregnancy can cause irreversible neurodevelopmental injury in infants.',
    correctAnswer: true,
    explanation: 'Iodine is essential for fetal thyroid hormone production.',
    reference: 'Endemic cretinism: severe iodine deficiency causes irreversible neurodevelopmental impairment.'
  },
  {
    id: 'pe-cr-003-tf6',
    subtopic: 'Van Wyk-Grumbach',
    statement: 'Precocious puberty with delayed bone age is a classic clue to severe hypothyroidism.',
    correctAnswer: true,
    explanation: 'This pattern is typical of Van Wyk-Grumbach phenomenon.',
    reference: 'Van Wyk-Grumbach: severe hypothyroidism causes precocious puberty with delayed bone age.'
  },
  {
    id: 'pe-cr-003-tf7',
    subtopic: 'Pituitary hyperplasia',
    statement: 'Pituitary enlargement due to hypothyroidism generally regresses with levothyroxine therapy.',
    correctAnswer: true,
    explanation: 'Thyrotroph hyperplasia is reversible with hormone replacement.',
    reference: 'Pituitary hyperplasia: chronic hypothyroidism can mimic a pituitary mass.'
  },
  {
    id: 'pe-cr-003-tf8',
    subtopic: 'Central hypothyroidism',
    statement: 'Low free T4 with a non-elevated TSH suggests central hypothyroidism.',
    correctAnswer: true,
    explanation: 'TSH is inappropriately normal or low in central disease.',
    reference: 'Secondary hypothyroidism: low free T4 with non-elevated TSH suggests central disease.'
  },
  {
    id: 'pe-cr-003-tf9',
    subtopic: 'Neonatal Graves',
    statement: 'Maternal TSH receptor antibodies can cause neonatal Graves disease.',
    correctAnswer: true,
    explanation: 'TRAb cross the placenta and stimulate the fetal thyroid.',
    reference: 'Neonatal Graves: transplacental TRAb can stimulate the fetal thyroid.'
  },
  {
    id: 'pe-cr-003-tf10',
    subtopic: 'Antithyroid drugs',
    statement: 'Propylthiouracil is preferred over methimazole for children because of better safety.',
    correctAnswer: false,
    explanation: 'Methimazole is preferred due to lower risk of severe hepatotoxicity.',
    reference: 'Antithyroid therapy: methimazole is preferred because PTU can cause severe liver injury.'
  },
  {
    id: 'pe-cr-003-tf11',
    subtopic: 'Replacement therapy',
    statement: 'Rapid full-dose levothyroxine replacement is always appropriate in long-standing severe hypothyroidism.',
    correctAnswer: false,
    explanation: 'Gradual titration is safer in chronic disease.',
    reference: 'Long-standing hypothyroidism: gradual L-T4 titration reduces adverse effects.'
  },
  {
    id: 'pe-cr-003-tf12',
    subtopic: 'Adrenal axis',
    statement: 'In suspected central hypothyroidism, cortisol reserve should be assessed before high-dose thyroid replacement.',
    correctAnswer: true,
    explanation: 'Thyroid hormone can precipitate adrenal crisis if cortisol is low.',
    reference: 'Adrenal axis: evaluate cortisol reserve before high-dose thyroid replacement in central disease.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-003-ar1',
    subtopic: 'Congenital hypothyroidism',
    assertion: 'Congenital hypothyroidism must be treated promptly.',
    reason: 'Delayed therapy can lead to irreversible neurodevelopmental impairment.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Congenital hypothyroidism: delayed treatment risks irreversible neurodevelopmental injury.'
  },
  {
    id: 'pe-cr-003-ar2',
    subtopic: 'Newborn screening',
    assertion: 'TSH-first newborn screening primarily detects primary hypothyroidism.',
    reason: 'Central hypothyroidism may not show an elevated TSH.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the limitation.',
    reference: 'Screening: TSH-first targets primary CH; central disease may have non-elevated TSH.'
  },
  {
    id: 'pe-cr-003-ar3',
    subtopic: 'Dyshormonogenesis',
    assertion: 'Dyshormonogenesis often presents with goiter.',
    reason: 'Chronic TSH stimulation causes thyroid hyperplasia.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the assertion.',
    reference: 'Dyshormonogenesis: chronic TSH stimulation causes goiter.'
  },
  {
    id: 'pe-cr-003-ar4',
    subtopic: 'Van Wyk-Grumbach',
    assertion: 'Severe hypothyroidism can cause precocious puberty.',
    reason: 'High TSH can stimulate gonadotropin receptors and increase prolactin.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the mechanism.',
    reference: 'Van Wyk-Grumbach: severe hypothyroidism can cause precocious puberty with delayed bone age.'
  },
  {
    id: 'pe-cr-003-ar5',
    subtopic: 'Pituitary hyperplasia',
    assertion: 'Primary hypothyroidism can cause pituitary enlargement.',
    reason: 'Thyrotroph hyperplasia develops in response to chronically elevated TSH.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the enlargement.',
    reference: 'Pituitary hyperplasia: chronic hypothyroidism can mimic a pituitary mass.'
  },
  {
    id: 'pe-cr-003-ar6',
    subtopic: 'Diagnostic testing',
    assertion: 'A positive perchlorate discharge test supports an iodide organification defect.',
    reason: 'Perchlorate blocks iodide trapping and causes release of unorganified iodide.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the diagnostic rationale.',
    reference: 'Perchlorate discharge: iodide release after perchlorate suggests organification defect.'
  },
  {
    id: 'pe-cr-003-ar7',
    subtopic: 'Central hypothyroidism',
    assertion: 'Low free T4 with a normal TSH is abnormal.',
    reason: 'TSH should rise in primary hypothyroidism, so a normal value suggests central disease.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the interpretation.',
    reference: 'Secondary hypothyroidism: low free T4 with non-elevated TSH suggests central disease.'
  },
  {
    id: 'pe-cr-003-ar8',
    subtopic: 'Neonatal Graves',
    assertion: 'Neonatal Graves disease can occur even if the mother is euthyroid.',
    reason: 'TSH receptor antibodies can cross the placenta and stimulate the fetal thyroid.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the phenomenon.',
    reference: 'Neonatal Graves: transplacental TRAb can stimulate the fetal thyroid.'
  },
  {
    id: 'pe-cr-003-ar9',
    subtopic: 'Antithyroid drugs',
    assertion: 'Methimazole is preferred for pediatric Graves disease.',
    reason: 'Propylthiouracil carries a higher risk of severe liver injury in children.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the preference.',
    reference: 'Antithyroid therapy: methimazole is preferred because PTU can cause severe liver injury.'
  },
  {
    id: 'pe-cr-003-ar10',
    subtopic: 'McCune-Albright',
    assertion: 'McCune-Albright syndrome can cause hyperthyroidism.',
    reason: 'Activating GNAS mutations lead to autonomous thyroid hormone production.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the mechanism.',
    reference: 'McCune-Albright: autonomous thyroid hormone production from GNAS activation.'
  },
  {
    id: 'pe-cr-003-ar11',
    subtopic: 'Replacement therapy',
    assertion: 'Levothyroxine should be started at a lower dose in long-standing severe hypothyroidism.',
    reason: 'Rapid full-dose replacement can cause symptoms of thyrotoxicosis or cardiac stress.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the strategy.',
    reference: 'Long-standing hypothyroidism: gradual L-T4 titration reduces adverse effects.'
  },
  {
    id: 'pe-cr-003-ar12',
    subtopic: 'Adrenal axis',
    assertion: 'Adrenal function should be assessed before full thyroid replacement in suspected central disease.',
    reason: 'Thyroid hormone can increase cortisol clearance and precipitate adrenal crisis.',
    correctOption: 0,
    explanation: 'Both statements are true, and the reason explains the safety concern.',
    reference: 'Adrenal axis: evaluate cortisol reserve before high-dose thyroid replacement in central disease.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-003',
  book: 'clinical_rounds',
  chapterNo: '3',
  title: 'Thyroid Disorders in Children',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/003_thyroid_disorders_in_children',
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
