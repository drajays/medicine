#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-008_turner_syndrome.json'
);

const notes = [
  {
    id: 'pe-cr-008-n1',
    subtopic: 'Definition',
    title: 'How Turner syndrome is defined clinically and genetically',
    content: 'Turner syndrome is a chromosomal disorder in a phenotypic female with short stature, gonadal failure, and typical physical features due to complete or partial loss of the X chromosome, especially loss of the short arm.',
    keyPoints: [
      'Phenotypic female with short stature and gonadal failure.',
      'Loss of entire X chromosome or short-arm material.',
      'Typical physical features are required for diagnosis.'
    ],
    reference: 'Turner syndrome is characterized by short stature, gonadal failure, and typical physical features in a phenotypic female with loss of the X chromosome or its short arm.'
  },
  {
    id: 'pe-cr-008-n2',
    subtopic: 'Definition',
    title: 'Why some X deletions are not labeled Turner syndrome',
    content: 'Distal Xq24 deletions cause gonadal failure without classic Turner features, and small distal Xp deletions with intact Xp22.3 show skeletal features but little gonadal failure, so these do not meet Turner syndrome criteria.',
    keyPoints: [
      'Distal Xq24 loss causes gonadal failure without the phenotype.',
      'Small distal Xp deletions spare Xp22.3 and have low gonadal failure risk.',
      'Phenotypic male individuals are excluded.'
    ],
    reference: 'Distal Xq24 deletions or small distal Xp deletions may not show the classic phenotype and are not considered Turner syndrome.'
  },
  {
    id: 'pe-cr-008-n3',
    subtopic: 'Definition',
    title: 'Why karyotype alone does not confirm Turner syndrome',
    content: 'A Turner diagnosis requires characteristic features in a phenotypic female plus a karyotypic abnormality; isolated karyotype changes without features do not qualify.',
    keyPoints: [
      'Phenotypic features are required.',
      'Karyotypic abnormality alone is insufficient.',
      'Diagnosis combines phenotype and cytogenetics.'
    ],
    reference: 'Diagnosis requires characteristic features in a phenotypic female along with karyotypic abnormalities.'
  },
  {
    id: 'pe-cr-008-n4',
    subtopic: 'Genetics',
    title: 'How SHOX contributes to growth and development',
    content: 'SHOX is a homeobox gene in the pseudoautosomal region of X and Y chromosomes, expressed early in fetal life in bones and pharyngeal arches to regulate chondrocyte growth and skeletal development.',
    keyPoints: [
      'Located in the pseudoautosomal region of X and Y.',
      'Expressed early in fetal life in long bones.',
      'Regulates chondrocyte growth and differentiation.'
    ],
    reference: 'SHOX is a pseudoautosomal homeobox gene expressed early in fetal life that regulates growth of skeletal tissues.'
  },
  {
    id: 'pe-cr-008-n5',
    subtopic: 'Genetics',
    title: 'How pseudoautosomal genes escape lyonization',
    content: 'Pseudoautosomal genes require expression from both X and Y chromosomes and do not undergo lyonization, so loss of one copy leads to haploinsufficiency.',
    keyPoints: [
      'Behave like autosomal genes.',
      'Require two copies for optimal expression.',
      'Do not undergo lyonization.'
    ],
    reference: 'Pseudoautosomal genes require both copies and do not undergo lyonization.'
  },
  {
    id: 'pe-cr-008-n6',
    subtopic: 'Genetics',
    title: 'How SHOX haploinsufficiency shapes skeletal features',
    content: 'Loss of one SHOX copy causes short stature, mesomelia, cubitus valgus, short metacarpals and metatarsals, Madelung deformity, and craniofacial changes such as high-arched palate.',
    keyPoints: [
      'Short stature and mesomelia are common.',
      'Madelung deformity can develop in adolescence.',
      'Craniofacial and limb anomalies reflect skeletal dysplasia.'
    ],
    reference: 'SHOX haploinsufficiency causes short stature, mesomelia, cubitus valgus, short metacarpals, and Madelung deformity.'
  },
  {
    id: 'pe-cr-008-n7',
    subtopic: 'Genetics',
    title: 'How Madelung deformity presents clinically',
    content: 'Madelung deformity is shortening and bowing of the radius with dorsal subluxation of the distal ulna, often becoming apparent in adolescence in SHOX-related conditions.',
    keyPoints: [
      'Shortened bowed radius.',
      'Dorsal subluxation of distal ulna.',
      'Often appears in adolescence.'
    ],
    reference: 'Madelung deformity involves shortening and bowing of the radius with dorsal subluxation of the distal ulna.'
  },
  {
    id: 'pe-cr-008-n8',
    subtopic: 'Genetics',
    title: 'How lyonization achieves dosage balance',
    content: 'Lyonization is random inactivation of one X chromosome in female embryos during early cell stages, mediated by XIST, to balance gene dosage between sexes.',
    keyPoints: [
      'Occurs early in embryogenesis.',
      'Randomly inactivates one X chromosome.',
      'XIST mediates silencing.'
    ],
    reference: 'Lyonization is random X inactivation early in embryogenesis mediated by XIST.'
  },
  {
    id: 'pe-cr-008-n9',
    subtopic: 'Genetics',
    title: 'Why Turner features occur despite X inactivation',
    content: 'Some genes escape lyonization, including pseudoautosomal genes like SHOX and other loci; loss of these escapee genes in Turner syndrome drives the phenotype.',
    keyPoints: [
      'Not all X-linked genes are silenced.',
      'Escapee genes are essential for normal development.',
      'Loss of the second X removes these genes.'
    ],
    reference: 'Genes that escape lyonization, such as SHOX, are absent in Turner syndrome and cause phenotypic abnormalities.'
  },
  {
    id: 'pe-cr-008-n10',
    subtopic: 'Genetics',
    title: 'Why 45,XO can be compatible with life',
    content: 'Most 45,XO conceptuses miscarry, but rare survivors likely have occult 45,XO/46,XX mosaicism that provides essential gene dosage.',
    keyPoints: [
      'Most 45,XO conceptuses abort.',
      'Survival is rare without mosaicism.',
      'Occult mosaicism explains viability.'
    ],
    reference: 'Survival of 45,XO is rare and likely explained by occult 45,XO/46,XX mosaicism.'
  },
  {
    id: 'pe-cr-008-n11',
    subtopic: 'Genetics',
    title: 'How common karyotypes distribute in Turner syndrome',
    content: 'About half of patients have 45,XO, mosaic 45,XO/46,XX accounts for roughly one-quarter, and the remainder have structural X abnormalities such as deletions, rings, or isochromosomes.',
    keyPoints: [
      '45,XO is most common.',
      'Mosaicism contributes about 20-30%.',
      'Structural X abnormalities comprise the rest.'
    ],
    reference: 'Approximately 45-60% have 45,XO, 20-30% have mosaicism, and the rest have structural X abnormalities.'
  },
  {
    id: 'pe-cr-008-n12',
    subtopic: 'Genetics',
    title: 'How ring chromosome affects phenotype',
    content: 'Ring X chromosome forms after distal breakage and fusion, accounts for about 10% of Turner cases, and is linked to higher mental retardation risk but fewer congenital malformations.',
    keyPoints: [
      'Ring X occurs after distal breaks and fusion.',
      'Associated with higher intellectual disability risk.',
      'Lower congenital malformation incidence.'
    ],
    reference: 'Ring X accounts for about 10% of Turner cases and is linked to higher mental retardation and fewer congenital malformations.'
  },
  {
    id: 'pe-cr-008-n13',
    subtopic: 'Genetics',
    title: 'How isochromosome Xq changes risk profile',
    content: 'Isochromosome Xq results from loss of one arm and duplication of the other, contributes to Turner syndrome in around 8%, and is associated with increased autoimmune disease and deafness.',
    keyPoints: [
      'Formed by loss of one arm with duplication of the other.',
      'Accounts for about 8% of cases.',
      'Linked to autoimmune disease and deafness.'
    ],
    reference: 'Isochromosome Xq causes about 8% of Turner cases and is linked to autoimmune disorders and deafness.'
  },
  {
    id: 'pe-cr-008-n14',
    subtopic: 'Prenatal',
    title: 'How prenatal ultrasound raises suspicion for Turner syndrome',
    content: 'Ultrasound findings such as increased nuchal translucency, cystic hygroma, left-sided cardiac defects, renal anomalies, and growth restriction warrant karyotyping for Turner syndrome.',
    keyPoints: [
      'Cystic hygroma and increased nuchal translucency are key.',
      'Left-sided cardiac and renal anomalies are clues.',
      'Karyotype is needed for confirmation.'
    ],
    reference: 'Prenatal clues include increased nuchal translucency, cystic hygroma, left-sided cardiac defects, renal anomalies, and growth retardation.'
  },
  {
    id: 'pe-cr-008-n15',
    subtopic: 'Neonatal',
    title: 'How Turner syndrome presents at birth or infancy',
    content: 'Lymphedema, webbed neck, low posterior hairline, abnormal auricles, left-sided cardiac anomalies, and horseshoe kidney are common early clues, while skeletal changes evolve later.',
    keyPoints: [
      'Lymphedema and webbed neck are early signs.',
      'Left-sided heart defects are common.',
      'Skeletal anomalies appear with growth.'
    ],
    reference: 'Early clues include lymphedema, webbed neck, low hairline, abnormal auricles, left-sided heart defects, and renal anomalies.'
  },
  {
    id: 'pe-cr-008-n16',
    subtopic: 'Lymphatic',
    title: 'How webbed neck develops in Turner syndrome',
    content: 'Lymphatic hypoplasia causes cystic hygroma in utero; resolution leaves redundant cervical skin that appears as a webbed neck.',
    keyPoints: [
      'Lymphatic hypoplasia leads to cystic hygroma.',
      'Resolution leaves redundant skin.',
      'Webbed neck is an early diagnostic clue.'
    ],
    reference: 'Cystic hygroma from lymphatic hypoplasia resolves into redundant neck skin, producing a webbed neck.'
  },
  {
    id: 'pe-cr-008-n17',
    subtopic: 'Lymphatic',
    title: 'How lymphedema evolves over time in Turner syndrome',
    content: 'Lymphedema appears in infancy in many patients, typically resolves by age 2, but can recur later, especially after starting growth hormone or estrogen therapy.',
    keyPoints: [
      'Often presents at birth.',
      'Usually resolves by age 2 years.',
      'May recur with GH or estrogen therapy.'
    ],
    reference: 'Lymphedema usually resolves by 2 years but can recur later, especially after rhGH or estrogen therapy.'
  },
  {
    id: 'pe-cr-008-n18',
    subtopic: 'Cardiac',
    title: 'Why webbed neck signals higher cardiac risk',
    content: 'Patients with webbed neck have a markedly higher prevalence of cardiac anomalies, making early cardiovascular screening especially important.',
    keyPoints: [
      'Webbed neck increases cardiac anomaly risk.',
      'Association is about threefold higher.',
      'Supports early imaging and monitoring.'
    ],
    reference: 'Webbed neck is associated with about three times higher risk of cardiac anomalies.'
  },
  {
    id: 'pe-cr-008-n19',
    subtopic: 'Cardiac',
    title: 'How cardiovascular anomalies present in Turner syndrome',
    content: 'Cardiac defects occur in roughly one-quarter to nearly half of patients, most commonly bicuspid aortic valve and coarctation, with additional risks of aortic dilation and anomalous venous connections.',
    keyPoints: [
      'Bicuspid aortic valve and coarctation are most common.',
      'Aortic dilation and aneurysm can occur.',
      'Other defects include PAPVC and left SVC.'
    ],
    reference: 'Bicuspid aortic valve and coarctation are the commonest defects, with other anomalies such as aortic dilatation and PAPVC.'
  },
  {
    id: 'pe-cr-008-n20',
    subtopic: 'Cardiac',
    title: 'How aortic dissection risk is determined',
    content: 'Risk increases with bicuspid valve, coarctation, elongated transverse arch, aortic dilatation, hypertension, and sinus tachycardia, and is tracked using the aortic size index.',
    keyPoints: [
      'Multiple anatomic and hemodynamic risk factors.',
      'Aortic size index accounts for small body size.',
      'Higher ASI requires closer surveillance.'
    ],
    reference: 'Risk factors include bicuspid valve, coarctation, elongated arch, aortic dilatation, hypertension, and sinus tachycardia.'
  },
  {
    id: 'pe-cr-008-n21',
    subtopic: 'Cardiac',
    title: 'How cardiac imaging is scheduled in Turner syndrome',
    content: 'Baseline ECG, echocardiography, and cardiac MRI are recommended at diagnosis; if normal, imaging is repeated every 5 to 10 years, with closer follow-up when risk factors exist or before pregnancy.',
    keyPoints: [
      'Baseline ECG, echo, and MRI at diagnosis.',
      'Repeat every 5-10 years if normal.',
      'More frequent with hypertension or aortic issues.'
    ],
    reference: 'Baseline ECG, echocardiography, and cardiac MRI are recommended, with repeat imaging every 5-10 years if normal.'
  },
  {
    id: 'pe-cr-008-n22',
    subtopic: 'Growth',
    title: 'How growth pattern evolves in Turner syndrome',
    content: 'Growth failure begins in utero, continues through childhood, and lacks a pubertal growth spurt, producing an untreated adult height about 20 cm below peers.',
    keyPoints: [
      'Intrauterine growth restriction is common.',
      'Slow childhood growth with no pubertal spurt.',
      'Average adult height deficit around 20 cm.'
    ],
    reference: 'Growth failure begins in utero and absence of pubertal growth spurt results in about 20 cm shorter adult height.'
  },
  {
    id: 'pe-cr-008-n23',
    subtopic: 'Growth',
    title: 'Why short stature has multiple drivers in Turner syndrome',
    content: 'SHOX haploinsufficiency explains most of the height deficit, while lack of prepubertal estrogen and comorbid disorders such as celiac or autoimmune thyroid disease contribute to additional growth loss.',
    keyPoints: [
      'SHOX loss accounts for most of the deficit.',
      'Prepubertal estrogen contributes to growth.',
      'Comorbidities can worsen stature.'
    ],
    reference: 'SHOX haploinsufficiency is the major driver, with estrogen deficiency and comorbid disease contributing to short stature.'
  },
  {
    id: 'pe-cr-008-n24',
    subtopic: 'Growth',
    title: 'How GH dynamics differ across puberty in Turner syndrome',
    content: 'Integrated GH secretion is typically normal prepubertally but reduced peripubertally because the estrogen-driven GH surge is absent; IGF-1 levels may be low due to GH resistance.',
    keyPoints: [
      'Prepubertal GH secretion is often normal.',
      'Peripubertal GH surge is blunted without estrogen.',
      'IGF-1 can be low from GH resistance.'
    ],
    reference: 'GH secretion is normal prepubertally but low peripubertally due to lack of estrogen-driven GH surge.'
  },
  {
    id: 'pe-cr-008-n25',
    subtopic: 'Otology',
    title: 'How ear disease contributes to hearing loss in Turner syndrome',
    content: 'External and middle ear anomalies predispose to recurrent otitis media and conductive loss in childhood, while inner ear defects cause progressive sensorineural loss in adulthood.',
    keyPoints: [
      'Recurrent otitis media leads to conductive loss.',
      'Inner ear defects cause progressive sensorineural loss.',
      'SHOX expression in pharyngeal arches links ear anomalies.'
    ],
    reference: 'Middle ear disease causes conductive loss in childhood, while inner ear defects lead to progressive sensorineural loss.'
  },
  {
    id: 'pe-cr-008-n26',
    subtopic: 'Autoimmunity',
    title: 'How autoimmune disease burden shapes follow-up',
    content: 'Autoimmune disorders are about twice as common in Turner syndrome, especially with isochromosome Xq, with Hashimoto thyroiditis most frequent, prompting annual screening.',
    keyPoints: [
      'Autoimmune disorders are doubled in frequency.',
      'Hashimoto thyroiditis is most common.',
      'Annual thyroid screening is recommended.'
    ],
    reference: 'Autoimmune disorders are about twofold higher, especially with isochromosome Xq, and Hashimoto thyroiditis is the most common.'
  },
  {
    id: 'pe-cr-008-n27',
    subtopic: 'Puberty',
    title: 'Why pubarche can be absent despite adrenarche',
    content: 'Pubarche requires ovarian conversion of adrenal androgens and synergy with estrogen, so ovarian failure in Turner syndrome delays or prevents pubic hair development.',
    keyPoints: [
      'Adrenal androgens alone may be insufficient.',
      'Ovarian conversion boosts potent androgens.',
      'Estrogen supports pilosebaceous response.'
    ],
    reference: 'Pubarche is delayed because ovarian failure reduces conversion of adrenal androgens and estrogen synergy.'
  },
  {
    id: 'pe-cr-008-n28',
    subtopic: 'Gonadal failure',
    title: 'How gonadal failure develops in Turner syndrome',
    content: 'Loss of key genes on both Xp and Xq disrupts ovarian development and triggers early follicular atresia, causing streak gonads and primary ovarian failure in most patients.',
    keyPoints: [
      'Genes on both Xp and Xq are required for ovarian development.',
      'Loss of one copy leads to streak gonads.',
      'Follicular atresia begins in fetal life.'
    ],
    reference: 'Loss of genes on Xp and Xq causes streak gonads and early follicular atresia, leading to ovarian failure.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-008-q1',
    subtopic: 'Case vignette',
    question: 'A 15-year-old girl has short stature, delayed puberty, high FSH/LH, and a karyotype 46,Xi(X)(q10). The most likely diagnosis is:',
    options: [
      'Turner syndrome with isochromosome Xq',
      'Noonan syndrome',
      'Constitutional delay of puberty',
      'Kallmann syndrome'
    ],
    correctOption: 0,
    explanation: 'Isochromosome Xq with hypergonadotropic hypogonadism in a phenotypic female fits Turner syndrome.',
    reference: 'Isochromosome Xq is a Turner karyotype associated with ovarian failure and typical phenotype.'
  },
  {
    id: 'pe-cr-008-q2',
    subtopic: 'Genetics',
    question: 'The most common karyotype in Turner syndrome is:',
    options: [
      '45,XO',
      '45,XO/46,XX',
      '46,Xi(Xq)',
      '46,Xr(X)'
    ],
    correctOption: 0,
    explanation: 'About half of patients have 45,XO.',
    reference: 'Approximately 45-60% of patients have 45,XO.'
  },
  {
    id: 'pe-cr-008-q3',
    subtopic: 'Genetics',
    question: 'SHOX is located on which chromosomal region?',
    options: [
      'Pseudoautosomal region of X and Y',
      'Long arm of chromosome 21',
      'Autosomal region of chromosome 15',
      'Mitochondrial DNA'
    ],
    correctOption: 0,
    explanation: 'SHOX resides in the pseudoautosomal region of both X and Y.',
    reference: 'SHOX is located in the pseudoautosomal region on the short arm of X and Y chromosomes.'
  },
  {
    id: 'pe-cr-008-q4',
    subtopic: 'Genetics',
    question: 'A key property of pseudoautosomal genes is that they:',
    options: [
      'Do not undergo lyonization and require two copies for expression',
      'Are silenced on the Y chromosome',
      'Are only expressed in males',
      'Undergo imprinting in all tissues'
    ],
    correctOption: 0,
    explanation: 'Pseudoautosomal genes escape lyonization and require two copies.',
    reference: 'Pseudoautosomal genes require both copies for optimal expression and do not undergo lyonization.'
  },
  {
    id: 'pe-cr-008-q5',
    subtopic: 'Genetics',
    question: 'Madelung deformity is best described as:',
    options: [
      'Shortening and bowing of the radius with dorsal subluxation of the distal ulna',
      'A proximal femoral slip',
      'Fusion of carpal bones',
      'Overgrowth of the ulna with radial hypoplasia'
    ],
    correctOption: 0,
    explanation: 'The deformity involves a bowed radius and dorsal ulna subluxation.',
    reference: 'Madelung deformity is shortening and bowing of the radius with dorsal subluxation of distal ulna.'
  },
  {
    id: 'pe-cr-008-q6',
    subtopic: 'Genetics',
    question: 'Turner phenotype persists despite lyonization because:',
    options: [
      'Some genes escape lyonization and are lost with the second X',
      'Lyonization never occurs in females',
      'Y chromosome genes are overexpressed',
      'The X chromosome lacks essential genes'
    ],
    correctOption: 0,
    explanation: 'Escapee genes such as SHOX require two copies.',
    reference: 'Genes that escape lyonization, including pseudoautosomal genes, are absent in Turner syndrome.'
  },
  {
    id: 'pe-cr-008-q7',
    subtopic: 'Prenatal',
    question: 'Which prenatal ultrasound finding most strongly suggests Turner syndrome?',
    options: [
      'Cystic hygroma with increased nuchal translucency',
      'Isolated omphalocele',
      'Neural tube defect',
      'Polyhydramnios alone'
    ],
    correctOption: 0,
    explanation: 'Cystic hygroma and increased nuchal translucency are classic prenatal clues.',
    reference: 'Increased nuchal translucency and cystic hygroma are key prenatal clues to Turner syndrome.'
  },
  {
    id: 'pe-cr-008-q8',
    subtopic: 'Lymphatic',
    question: 'Webbed neck in Turner syndrome is primarily due to:',
    options: [
      'Resolution of cystic hygroma from lymphatic hypoplasia',
      'Excessive cervical muscle growth',
      'Hyperthyroidism-related skin changes',
      'Reduced neck length from vertebral fusion'
    ],
    correctOption: 0,
    explanation: 'Lymphatic hypoplasia causes cystic hygroma that resolves into redundant skin.',
    reference: 'Cystic hygroma from lymphatic hypoplasia resolves into redundant neck skin causing webbing.'
  },
  {
    id: 'pe-cr-008-q9',
    subtopic: 'Lymphatic',
    question: 'Which statement about lymphedema in Turner syndrome is correct?',
    options: [
      'It often resolves by age 2 years but can recur later',
      'It is always progressive and permanent',
      'It appears only after puberty',
      'It is unrelated to lymphatic abnormalities'
    ],
    correctOption: 0,
    explanation: 'Lymphedema typically resolves early but may recur.',
    reference: 'Lymphedema usually resolves by 2 years but can recur later, especially after rhGH or estrogen.'
  },
  {
    id: 'pe-cr-008-q10',
    subtopic: 'Cardiac',
    question: 'The two most common cardiac defects in Turner syndrome are:',
    options: [
      'Bicuspid aortic valve and coarctation of aorta',
      'Pulmonary stenosis and Tetralogy of Fallot',
      'Atrial septal defect and Ebstein anomaly',
      'Transposition of great arteries and VSD'
    ],
    correctOption: 0,
    explanation: 'Bicuspid aortic valve and coarctation are most frequent.',
    reference: 'Bicuspid aortic valve and coarctation of aorta are the most common cardiovascular defects.'
  },
  {
    id: 'pe-cr-008-q11',
    subtopic: 'Cardiac',
    question: 'Which factor increases the risk of aortic dissection in Turner syndrome?',
    options: [
      'Aortic dilatation with systemic hypertension',
      'Normal blood pressure and normal aortic size',
      'Isolated short stature alone',
      'Mild anemia'
    ],
    correctOption: 0,
    explanation: 'Aortic dilatation and hypertension are major risk factors.',
    reference: 'Aortic dilatation and systemic hypertension are risk factors for aortic dissection in Turner syndrome.'
  },
  {
    id: 'pe-cr-008-q12',
    subtopic: 'Cardiac',
    question: 'An aortic size index (ASI) that requires urgent referral is:',
    options: [
      'Greater than 2.5 cm/m2',
      'Less than 1.5 cm/m2',
      'Exactly 1.0 cm/m2',
      'Any value below 2.0 cm/m2'
    ],
    correctOption: 0,
    explanation: 'An ASI above 2.5 cm/m2 warrants urgent evaluation.',
    reference: 'An ASI greater than 2.5 cm/m2 warrants urgent referral.'
  },
  {
    id: 'pe-cr-008-q13',
    subtopic: 'Cardiac',
    question: 'Cardiac MRI is preferred over echocardiography in Turner syndrome because it:',
    options: [
      'Detects coarctation, PAPVC, and elongated transverse arch more reliably',
      'Is cheaper and faster than echocardiography',
      'Eliminates need for blood pressure monitoring',
      'Provides direct hormonal evaluation'
    ],
    correctOption: 0,
    explanation: 'MRI is more sensitive for aortic and venous anomalies.',
    reference: 'Cardiac MRI is more sensitive for coarctation and can detect PAPVC and elongated transverse arch.'
  },
  {
    id: 'pe-cr-008-q14',
    subtopic: 'Growth',
    question: 'The typical growth pattern in Turner syndrome includes:',
    options: [
      'Absence of pubertal growth spurt and adult height about 20 cm shorter',
      'Excessive pubertal growth spurt and tall stature',
      'Normal pubertal growth spurt with delayed epiphyseal closure',
      'Short stature only after puberty'
    ],
    correctOption: 0,
    explanation: 'Lack of pubertal spurt drives the typical adult height deficit.',
    reference: 'Patients lack a pubertal growth spurt and average adult height is about 20 cm shorter.'
  },
  {
    id: 'pe-cr-008-q15',
    subtopic: 'Growth',
    question: 'The principal genetic contributor to short stature in Turner syndrome is:',
    options: [
      'SHOX haploinsufficiency',
      'SRY duplication',
      'Mutations in GH1',
      'Inactivation of IGF2'
    ],
    correctOption: 0,
    explanation: 'Loss of one SHOX copy accounts for most of the height deficit.',
    reference: 'Two copies of SHOX are required for normal growth and haploinsufficiency drives short stature.'
  },
  {
    id: 'pe-cr-008-q16',
    subtopic: 'Growth',
    question: 'Growth monitoring in girls with Turner syndrome should use:',
    options: [
      'Both standard growth charts and Turner-specific charts',
      'Only Turner-specific charts',
      'Only standard growth charts',
      'Only weight-for-age charts'
    ],
    correctOption: 0,
    explanation: 'Standard charts detect early faltering and Turner charts assess disease-specific trends.',
    reference: 'Girls with Turner syndrome should be monitored on both standard and Turner-specific growth charts.'
  },
  {
    id: 'pe-cr-008-q17',
    subtopic: 'Growth',
    question: 'When should rhGH therapy be started in Turner syndrome?',
    options: [
      'When height begins to falter on standard growth charts',
      'Only after GH stimulation tests show deficiency',
      'Only after puberty begins',
      'At 18 years of age'
    ],
    correctOption: 0,
    explanation: 'GH tests are not required; therapy is started once growth falters.',
    reference: 'Therapy with rhGH should be started once the child starts faltering on standard growth charts.'
  },
  {
    id: 'pe-cr-008-q18',
    subtopic: 'Growth',
    question: 'The recommended rhGH dose range for Turner syndrome is approximately:',
    options: [
      '0.36 to 0.46 mg/kg/week given daily',
      '0.1 mg/kg/week given weekly',
      '0.05 mg/kg/week given monthly',
      '2 mg/kg/week given every other day'
    ],
    correctOption: 0,
    explanation: 'Higher doses are needed due to GH resistance.',
    reference: 'Recommended rhGH dose is 0.36-0.46 mg/kg/week given daily.'
  },
  {
    id: 'pe-cr-008-q19',
    subtopic: 'Growth',
    question: 'A standard oxandrolone dose for growth promotion in Turner syndrome is:',
    options: [
      '0.05 mg/kg/day (maximum 2.5 mg/day)',
      '0.5 mg/kg/day',
      '5 mg/kg/day',
      '10 mg/kg/day'
    ],
    correctOption: 0,
    explanation: 'Low-dose oxandrolone is used to limit virilization risk.',
    reference: 'Oxandrolone is used at 0.05 mg/kg/day with a maximum of 2.5 mg/day.'
  },
  {
    id: 'pe-cr-008-q20',
    subtopic: 'Puberty',
    question: 'The recommended age to initiate puberty induction in Turner syndrome is:',
    options: [
      '12 years',
      '8 years',
      '15 years',
      '18 years'
    ],
    correctOption: 0,
    explanation: 'Initiation at 12 years balances growth with psychosocial health.',
    reference: 'The recommended age for puberty induction in Turner syndrome is 12 years.'
  },
  {
    id: 'pe-cr-008-q21',
    subtopic: 'Puberty',
    question: 'Which estrogen route is preferred for puberty induction in Turner syndrome?',
    options: [
      'Transdermal estradiol',
      'High-dose oral contraceptive pills',
      'Single monthly depot injection only',
      'No estrogen until adulthood'
    ],
    correctOption: 0,
    explanation: 'Transdermal estradiol has a more favorable metabolic profile.',
    reference: 'Transdermal estrogen is preferred due to favorable effects on IGF-1 and lower thromboembolic risk.'
  },
  {
    id: 'pe-cr-008-q22',
    subtopic: 'Puberty',
    question: 'Why are oral contraceptive pills discouraged for puberty induction?',
    options: [
      'They deliver excessive estrogen leading to rapid, suboptimal breast and uterine development',
      'They contain no estrogen',
      'They prevent all bone maturation',
      'They are ineffective in any adolescent'
    ],
    correctOption: 0,
    explanation: 'High-dose estrogen causes nonphysiologic, suboptimal development.',
    reference: 'High-dose estrogen in oral contraceptives causes rapid but suboptimal breast and uterine development.'
  },
  {
    id: 'pe-cr-008-q23',
    subtopic: 'Screening',
    question: 'Why is a 30-cell karyotype recommended in suspected Turner syndrome?',
    options: [
      'It detects 10% mosaicism with about 95% confidence',
      'It avoids the need for imaging',
      'It replaces prenatal testing',
      'It identifies GH deficiency'
    ],
    correctOption: 0,
    explanation: 'Thirty cells provide adequate sensitivity for mosaicism.',
    reference: 'At least 30 cells are required to detect 10% mosaicism with 95% confidence.'
  },
  {
    id: 'pe-cr-008-q24',
    subtopic: 'Screening',
    question: 'Detection of Y chromosome material in Turner syndrome implies:',
    options: [
      'Risk of gonadoblastoma and need for prophylactic gonadectomy',
      'No change in management',
      'Immediate estrogen cessation',
      'Guaranteed fertility'
    ],
    correctOption: 0,
    explanation: 'Y material increases gonadoblastoma risk and warrants gonadectomy.',
    reference: 'Y chromosome material carries increased gonadoblastoma risk and prophylactic gonadectomy is recommended.'
  },
  {
    id: 'pe-cr-008-q25',
    subtopic: 'Fertility',
    question: 'The most realistic fertility option for most women with classical Turner syndrome is:',
    options: [
      'Donor oocyte with IVF and embryo transfer',
      'Expectant management with spontaneous conception',
      'Oral ovulation induction alone',
      'Testosterone suppression therapy'
    ],
    correctOption: 0,
    explanation: 'Most women with classical Turner syndrome require donor oocytes.',
    reference: 'Donor oocyte with IVF is the main fertility option for most women with classical Turner syndrome.'
  },
  {
    id: 'pe-cr-008-q26',
    subtopic: 'Pregnancy',
    question: 'Which cardiac finding is an absolute contraindication to pregnancy in Turner syndrome?',
    options: [
      'Aortic size index greater than 2.0 cm/m2',
      'Normal echocardiography',
      'Isolated sinus tachycardia',
      'Mild mitral regurgitation'
    ],
    correctOption: 0,
    explanation: 'ASI above 2.0 cm/m2 is an absolute contraindication.',
    reference: 'An ASI greater than 2.0 cm/m2 is an absolute contraindication to pregnancy.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-008-tf1',
    subtopic: 'Definition',
    statement: 'Turner syndrome requires both characteristic phenotype and karyotypic abnormality in a phenotypic female.',
    correctAnswer: true,
    explanation: 'Phenotypic features plus karyotype define the diagnosis.',
    reference: 'Diagnosis requires characteristic features in a phenotypic female along with karyotypic abnormalities.'
  },
  {
    id: 'pe-cr-008-tf2',
    subtopic: 'Genetics',
    statement: 'Pseudoautosomal genes like SHOX escape lyonization and require two copies for optimal expression.',
    correctAnswer: true,
    explanation: 'These genes behave like autosomal genes.',
    reference: 'Pseudoautosomal genes require both copies and do not undergo lyonization.'
  },
  {
    id: 'pe-cr-008-tf3',
    subtopic: 'Lymphatic',
    statement: 'Webbed neck results from resolution of fetal cystic hygroma.',
    correctAnswer: true,
    explanation: 'Lymphatic hypoplasia leads to cystic hygroma that resolves into redundant skin.',
    reference: 'Resolution of cystic hygroma leads to webbed neck.'
  },
  {
    id: 'pe-cr-008-tf4',
    subtopic: 'Cardiac',
    statement: 'Bicuspid aortic valve and coarctation of aorta are the most common cardiac defects in Turner syndrome.',
    correctAnswer: true,
    explanation: 'These are the most frequent lesions reported.',
    reference: 'Bicuspid aortic valve and coarctation are the commonest cardiovascular defects.'
  },
  {
    id: 'pe-cr-008-tf5',
    subtopic: 'Cardiac',
    statement: 'Cardiac MRI is more sensitive than echocardiography for detecting coarctation and PAPVC.',
    correctAnswer: true,
    explanation: 'MRI can visualize the aortic arch and pulmonary veins better.',
    reference: 'Cardiac MRI detects coarctation and PAPVC not easily seen on echocardiography.'
  },
  {
    id: 'pe-cr-008-tf6',
    subtopic: 'Growth',
    statement: 'Girls with Turner syndrome typically lack a pubertal growth spurt.',
    correctAnswer: true,
    explanation: 'Estrogen deficiency blunts the pubertal GH surge.',
    reference: 'They lack pubertal growth spurt and remain about 20 cm shorter as adults.'
  },
  {
    id: 'pe-cr-008-tf7',
    subtopic: 'Growth',
    statement: 'GH stimulation tests are mandatory before starting rhGH in Turner syndrome.',
    correctAnswer: false,
    explanation: 'rhGH is indicated regardless of GH test results once growth falters.',
    reference: 'GH dynamic tests are not required before initiation of rhGH therapy.'
  },
  {
    id: 'pe-cr-008-tf8',
    subtopic: 'Puberty',
    statement: 'Transdermal estrogen is preferred over oral estrogen for puberty induction.',
    correctAnswer: true,
    explanation: 'It avoids hepatic first-pass effects and has favorable metabolic effects.',
    reference: 'Transdermal estrogen is preferred because of favorable metabolic effects and lower thromboembolism risk.'
  },
  {
    id: 'pe-cr-008-tf9',
    subtopic: 'Puberty',
    statement: 'Delaying puberty induction to 14-15 years is recommended to maximize height.',
    correctAnswer: false,
    explanation: 'Delay harms psychosocial and bone health and is no longer recommended.',
    reference: 'Delaying puberty induction beyond 12 years is not recommended.'
  },
  {
    id: 'pe-cr-008-tf10',
    subtopic: 'Screening',
    statement: 'A 30-cell karyotype is recommended to detect low-level mosaicism.',
    correctAnswer: true,
    explanation: 'Thirty cells detect 10% mosaicism with high confidence.',
    reference: 'At least 30 cells are required to detect 10% mosaicism with 95% confidence.'
  },
  {
    id: 'pe-cr-008-tf11',
    subtopic: 'Screening',
    statement: 'Presence of Y chromosome material in Turner syndrome increases gonadoblastoma risk.',
    correctAnswer: true,
    explanation: 'Y fragments raise gonadoblastoma risk and warrant gonadectomy.',
    reference: 'Y chromosome material is associated with increased gonadoblastoma risk.'
  },
  {
    id: 'pe-cr-008-tf12',
    subtopic: 'Mortality',
    statement: 'Cardiovascular disease is the leading contributor to excess mortality in Turner syndrome.',
    correctAnswer: true,
    explanation: 'Cardiovascular causes account for the largest share of excess mortality.',
    reference: 'Cardiovascular disorders contribute to the largest proportion of excess mortality.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-008-ar1',
    subtopic: 'Definition',
    assertion: 'Turner syndrome requires phenotypic features in a female along with karyotypic abnormalities.',
    reason: 'Karyotypic abnormalities without characteristic features do not qualify for the diagnosis.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Diagnosis requires characteristic features in a phenotypic female; karyotypic abnormalities alone do not qualify.'
  },
  {
    id: 'pe-cr-008-ar2',
    subtopic: 'Genetics',
    assertion: 'Pseudoautosomal genes do not undergo lyonization.',
    reason: 'They require expression from both X and Y chromosomes for optimal function.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Pseudoautosomal genes require both copies and do not undergo lyonization.'
  },
  {
    id: 'pe-cr-008-ar3',
    subtopic: 'Genetics',
    assertion: 'SHOX haploinsufficiency contributes to short stature in Turner syndrome.',
    reason: 'SHOX regulates chondrocyte growth and skeletal development.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the short stature.',
    reference: 'SHOX regulates chondrocyte growth, and haploinsufficiency leads to short stature.'
  },
  {
    id: 'pe-cr-008-ar4',
    subtopic: 'Lymphatic',
    assertion: 'Webbed neck is a helpful early diagnostic clue in Turner syndrome.',
    reason: 'It can be present at birth because it results from fetal lymphatic abnormalities.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains early detection.',
    reference: 'Webbed neck can be present at birth due to lymphatic abnormalities.'
  },
  {
    id: 'pe-cr-008-ar5',
    subtopic: 'Cardiac',
    assertion: 'Cardiac MRI is recommended at diagnosis in Turner syndrome.',
    reason: 'MRI detects coarctation, PAPVC, and elongated transverse arch better than echocardiography.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the preference.',
    reference: 'Cardiac MRI is more sensitive than echocardiography for coarctation and PAPVC.'
  },
  {
    id: 'pe-cr-008-ar6',
    subtopic: 'Cardiac',
    assertion: 'Sinus tachycardia is common in Turner syndrome.',
    reason: 'It reflects dysautonomia and may increase aortic dissection risk when aortic dilation is present.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the risk link.',
    reference: 'Sinus tachycardia is common and increases dissection risk when aortic dilatation is present.'
  },
  {
    id: 'pe-cr-008-ar7',
    subtopic: 'Growth',
    assertion: 'Growth hormone stimulation tests are required before initiating rhGH in Turner syndrome.',
    reason: 'Most patients with Turner syndrome have normal GH responses.',
    correctOption: 2,
    explanation: 'The assertion is false, but the reason is true.',
    reference: 'Most patients have normal GH responses and GH tests are not required before starting rhGH.'
  },
  {
    id: 'pe-cr-008-ar8',
    subtopic: 'Growth',
    assertion: 'RhGH doses are higher in Turner syndrome than in isolated GH deficiency.',
    reason: 'Turner syndrome is a GH-resistant state due to SHOX-related chondrocyte defects.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the dose requirement.',
    reference: 'Higher rhGH doses are needed because Turner syndrome is a GH-resistant state.'
  },
  {
    id: 'pe-cr-008-ar9',
    subtopic: 'Puberty',
    assertion: 'Puberty induction at 12 years is recommended in Turner syndrome.',
    reason: 'Low-dose estrogen started at this age allows pubertal development without compromising adult height.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the recommendation.',
    reference: 'Low-dose estrogen at 12 years supports pubertal development without affecting adult height.'
  },
  {
    id: 'pe-cr-008-ar10',
    subtopic: 'Puberty',
    assertion: 'Transdermal estrogen is preferred over oral estrogen for puberty induction.',
    reason: 'Oral estrogen has hepatic first-pass effects that reduce IGF-1 and increase procoagulant factors.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the preference.',
    reference: 'Oral estrogen increases hepatic procoagulant factors and reduces IGF-1; transdermal avoids this.'
  },
  {
    id: 'pe-cr-008-ar11',
    subtopic: 'Screening',
    assertion: 'A 30-cell karyotype is recommended when Turner syndrome is suspected.',
    reason: 'Thirty cells detect about 10% mosaicism with 95% confidence.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the recommendation.',
    reference: 'At least 30 cells are required to detect 10% mosaicism with 95% confidence.'
  },
  {
    id: 'pe-cr-008-ar12',
    subtopic: 'Pregnancy',
    assertion: 'An aortic size index greater than 2.0 cm/m2 is an absolute contraindication to pregnancy in Turner syndrome.',
    reason: 'Aortic dilatation increases the risk of dissection during pregnancy.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the contraindication.',
    reference: 'ASI greater than 2.0 cm/m2 is an absolute pregnancy contraindication because of dissection risk.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-008',
  book: 'clinical_rounds',
  chapterNo: '8',
  title: 'Turner Syndrome',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/008_turner_syndrome',
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
