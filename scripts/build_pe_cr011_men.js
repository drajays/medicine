#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-011_multiple_endocrine_neoplasia.json'
);

const notes = [
  {
    id: 'pe-cr-011-n1',
    subtopic: 'Definition',
    title: 'How multiple endocrine neoplasia is defined',
    content: 'Multiple endocrine neoplasia (MEN) describes inherited syndromes in which tumors affect two or more endocrine organs in the same individual, either at the same time or sequentially.',
    keyPoints: [
      'Tumors involve at least two endocrine glands.',
      'Patterns can be synchronous or metachronous.',
      'Clinical manifestations depend on the hormones secreted.'
    ],
    reference: 'MEN is an inherited disorder with tumors in two or more endocrine organs that can be synchronous or metachronous.'
  },
  {
    id: 'pe-cr-011-n2',
    subtopic: 'Classification',
    title: 'How MEN syndromes are categorized into types',
    content: 'MEN is classified into MEN1 and MEN2, with MEN2 subdivided into MEN2A and MEN2B; MEN4 is a newer category, and disorders with endocrine plus non-endocrine tumors are grouped as MEON.',
    keyPoints: [
      'MEN2 includes MEN2A and MEN2B.',
      'MEN4 is a distinct phenotype beyond MEN1.',
      'MEON includes syndromes with endocrine and non-endocrine tumors.'
    ],
    reference: 'MEN is classified into MEN1, MEN2A, MEN2B, and MEN4, while mixed endocrine and non-endocrine neoplasia is grouped as MEON.'
  },
  {
    id: 'pe-cr-011-n3',
    subtopic: 'MEN1 organs',
    title: 'How MEN1 organ involvement is organized',
    content: 'MEN1 classically involves parathyroid, pituitary, and pancreatic neuroendocrine tumors, with additional involvement of adrenal and thyroid lesions and cutaneous manifestations.',
    keyPoints: [
      'Classic triad: parathyroid, pituitary, pancreas.',
      'Adrenal and thyroid lesions are also described.',
      'Cutaneous markers can accompany endocrine disease.'
    ],
    reference: 'MEN1 involves parathyroid, pituitary, and pancreatic tumors with adrenal and thyroid lesions and skin findings.'
  },
  {
    id: 'pe-cr-011-n4',
    subtopic: 'MEN1 prevalence',
    title: 'Why parathyroid disease dominates MEN1 presentations',
    content: 'Primary hyperparathyroidism is the most frequent MEN1 manifestation, occurring in about 95% of patients, while pancreatic NETs and pituitary tumors occur in smaller but substantial proportions.',
    keyPoints: [
      'Parathyroid hyperplasia or adenoma is most common.',
      'Pancreatic NETs occur in roughly 40 to 70 percent.',
      'Pituitary tumors occur in roughly 30 to 40 percent.'
    ],
    reference: 'Parathyroid involvement occurs in about 95% of MEN1, with pancreatic NETs and pituitary tumors in 40-70% and 30-40% respectively.'
  },
  {
    id: 'pe-cr-011-n5',
    subtopic: 'MEN1 screening',
    title: 'How to decide who should be screened for MEN1',
    content: 'MEN1 screening is advised for people with two MEN1-associated tumors, first-degree relatives of a known mutation carrier, or those with early or multiglandular primary hyperparathyroidism and gastrinoma or multiple pancreatic NETs.',
    keyPoints: [
      'Two MEN1-associated tumors warrant screening.',
      'First-degree relatives of mutation carriers should be screened.',
      'Early or multiglandular PHPT and gastrinoma are triggers.'
    ],
    reference: 'Screening is recommended for those with two MEN1-associated tumors, relatives of mutation carriers, or early/multiglandular PHPT and gastrinoma or multiple pancreatic NETs.'
  },
  {
    id: 'pe-cr-011-n6',
    subtopic: 'MEN1 suspicion',
    title: 'How single-gland presentations can suggest MEN1',
    content: 'Young-onset or multiglandular primary hyperparathyroidism suggests MEN1, and gastrinomas with PPI-resistant ulcers or multiple pancreatic NETs should prompt MEN1 evaluation, whereas isolated pituitary tumors rarely indicate MEN1.',
    keyPoints: [
      'PHPT before 30 years or multiglandular disease raises concern.',
      'Gastrinoma with refractory or recurrent ulcers is suggestive.',
      'Isolated pituitary tumors seldom reflect MEN1.'
    ],
    reference: 'PHPT in young patients or multiglandular disease, gastrinoma with refractory ulcers, or multiple pancreatic NETs should trigger MEN1 evaluation.'
  },
  {
    id: 'pe-cr-011-n7',
    subtopic: 'MEN1 follow-up',
    title: 'How MEN1 surveillance is structured',
    content: 'MEN1 surveillance combines annual biochemical testing for functional tumors with periodic imaging for nonfunctioning lesions, beginning in childhood for pituitary and pancreatic NET screening.',
    keyPoints: [
      'Annual labs target functional tumors.',
      'Imaging tracks nonfunctioning pancreatic NETs.',
      'Screening starts early, including pituitary MRI every few years.'
    ],
    reference: 'MEN1 follow-up uses annual biochemistry and imaging with early surveillance for pituitary and pancreatic tumors.'
  },
  {
    id: 'pe-cr-011-n8',
    subtopic: 'MEN1 pituitary',
    title: 'Why MEN1 pituitary tumors are clinically challenging',
    content: 'MEN1 pituitary tumors are often macroadenomas, more aggressive, and less responsive to medical therapy; prolactinomas are most common, followed by somatotropinomas.',
    keyPoints: [
      'Macroadenomas are common in MEN1.',
      'Prolactinoma is the most frequent subtype.',
      'Aggressive behavior and resistance are typical.'
    ],
    reference: 'MEN1 pituitary tumors are often aggressive macroadenomas, most commonly prolactinomas followed by somatotropinomas.'
  },
  {
    id: 'pe-cr-011-n9',
    subtopic: 'MEN1 insulinoma',
    title: 'How MEN1-associated insulinomas differ by age',
    content: 'MEN1 insulinomas often present earlier than sporadic insulinomas, frequently before 40 years of age, and can coexist with other pancreatic NETs.',
    keyPoints: [
      'Presentation is commonly before 40 years.',
      'Some patients have concurrent pancreatic NETs.',
      'Lesions are usually small and benign.'
    ],
    reference: 'MEN1 insulinomas present early, often before age 40, and may coexist with other pancreatic NETs.'
  },
  {
    id: 'pe-cr-011-n10',
    subtopic: 'MEN1 skin',
    title: 'How cutaneous markers point to MEN1',
    content: 'Lipomas, facial angiofibromas, and collagenomas are frequent in MEN1 and can appear before endocrine disease, serving as early clinical clues.',
    keyPoints: [
      'Lipomas occur in about one-third of patients.',
      'Angiofibromas and collagenomas are common.',
      'Skin findings may precede endocrine tumors.'
    ],
    reference: 'MEN1 includes lipomas, angiofibromas, and collagenomas that can appear before endocrine manifestations.'
  },
  {
    id: 'pe-cr-011-n11',
    subtopic: 'MEN1 gastrinoma',
    title: 'How MEN1 gastrinomas are distributed',
    content: 'MEN1 gastrinomas are often multiple and tiny, frequently located in the duodenal wall within the gastrinoma triangle, and metastasize to peripancreatic nodes.',
    keyPoints: [
      'Lesions are often small and multiple.',
      'Duodenal wall involvement is common.',
      'The gastrinoma triangle is the key region.'
    ],
    reference: 'MEN1 gastrinomas are usually small, multiple, and often located in the duodenal wall within the gastrinoma triangle.'
  },
  {
    id: 'pe-cr-011-n12',
    subtopic: 'MEN1 gastrinoma',
    title: 'Why medical therapy is preferred for MEN1 gastrinoma',
    content: 'Because duodenal gastrinomas are often multiple and small, curative surgery is difficult and management favors proton pump inhibitors and somatostatin analogues, with pancreatic resection reserved for tumors larger than 2 cm.',
    keyPoints: [
      'Multiple duodenal lesions limit surgical cure.',
      'Proton pump inhibitors control acid hypersecretion.',
      'Pancreatic tumors >2 cm merit resection.'
    ],
    reference: 'MEN1 duodenal gastrinomas are often multiple and small; medical therapy is preferred, with surgery for pancreatic tumors larger than 2 cm.'
  },
  {
    id: 'pe-cr-011-n13',
    subtopic: 'MEN1 pancreatic NET',
    title: 'How nonfunctioning pancreatic NETs are managed in MEN1',
    content: 'Nonfunctioning pancreatic NETs are common in MEN1, often malignant, and typically warrant resection when larger than 1 cm or showing rapid growth.',
    keyPoints: [
      'Nonfunctioning NETs are increasingly detected.',
      'Risk of malignancy is significant.',
      'Resection is advised for tumors >1 cm.'
    ],
    reference: 'Nonfunctioning pancreatic NETs in MEN1 are often malignant and should be resected when larger than 1 cm or rapidly growing.'
  },
  {
    id: 'pe-cr-011-n14',
    subtopic: 'MEN1 gene',
    title: 'How MEN1 gene mutations drive tumor formation',
    content: 'MEN1 is a tumor suppressor gene on chromosome 11q13 encoding menin, and germline mutation predisposes to tumorigenesis after loss of heterozygosity in affected tissue.',
    keyPoints: [
      'MEN1 is located on chromosome 11q13.',
      'Menin regulates transcription and cell division.',
      'Second-hit loss of heterozygosity promotes tumors.'
    ],
    reference: 'MEN1 is a tumor suppressor on 11q13 encoding menin, and loss of heterozygosity in tissue leads to tumor formation.'
  },
  {
    id: 'pe-cr-011-n15',
    subtopic: 'MEN2 overview',
    title: 'How MEN2 syndromes are defined',
    content: 'MEN2 is an autosomal dominant disorder of neural crest-derived endocrine organs and includes MEN2A, MEN2B, and familial medullary thyroid carcinoma.',
    keyPoints: [
      'MEN2 involves neural crest-derived tissues.',
      'MEN2A and MEN2B are the main variants.',
      'Familial medullary thyroid carcinoma is part of MEN2.'
    ],
    reference: 'MEN2 is an autosomal dominant disorder involving neural crest-derived endocrine organs and includes MEN2A, MEN2B, and familial MTC.'
  },
  {
    id: 'pe-cr-011-n16',
    subtopic: 'MEN2A',
    title: 'How MEN2A is clinically defined',
    content: 'MEN2A consists of medullary thyroid carcinoma, pheochromocytoma, and primary hyperparathyroidism, with cutaneous lichen amyloidosis and Hirschsprung disease as associated features.',
    keyPoints: [
      'MTC is nearly universal in MEN2A.',
      'Pheochromocytoma occurs in 30 to 50 percent.',
      'Cutaneous lichen amyloidosis and Hirschsprung disease can occur.'
    ],
    reference: 'MEN2A includes medullary thyroid carcinoma, pheochromocytoma, and PHPT with associations such as cutaneous lichen amyloidosis and Hirschsprung disease.'
  },
  {
    id: 'pe-cr-011-n17',
    subtopic: 'MEN2A suspicion',
    title: 'How MEN2A can be suspected clinically',
    content: 'MEN2A should be suspected in young patients with goiter and diarrhea suggestive of MTC or with early-onset pheochromocytoma that is bilateral or epinephrine secreting.',
    keyPoints: [
      'MTC presents early with goiter or diarrhea.',
      'Pheochromocytomas may be bilateral and mild.',
      'PHPT tends to be mild and late.'
    ],
    reference: 'MEN2A is suggested by early MTC with goiter/diarrhea or bilateral, epinephrine-secreting pheochromocytoma.'
  },
  {
    id: 'pe-cr-011-n18',
    subtopic: 'MTC evaluation',
    title: 'Why all MTC cases need familial evaluation',
    content: 'Because a significant minority of medullary thyroid carcinoma is hereditary, every MTC patient should undergo evaluation for MEN2 or familial MTC.',
    keyPoints: [
      'Roughly one-fifth of MTC is familial.',
      'RET mutation testing is critical.',
      'Family screening guides prophylactic care.'
    ],
    reference: 'About 20% of MTC cases are hereditary, so all patients should be evaluated for MEN2 or familial MTC.'
  },
  {
    id: 'pe-cr-011-n19',
    subtopic: 'Calcitonin',
    title: 'How elevated calcitonin can occur without MTC',
    content: 'Elevated calcitonin can be seen in renal failure, autoimmune thyroiditis, primary hyperparathyroidism, neuroendocrine tumors, certain medications, and postprandial states, so fasting interpretation is required.',
    keyPoints: [
      'Non-MTC conditions can raise calcitonin.',
      'Drug effects include DPP4 inhibitors and GLP1 agonists.',
      'Fasting testing avoids postprandial elevation.'
    ],
    reference: 'High calcitonin can occur with renal failure, thyroiditis, PHPT, NETs, and medications or food intake, so fasting testing is recommended.'
  },
  {
    id: 'pe-cr-011-n20',
    subtopic: 'Calcitonin',
    title: 'Why calcitonin can be low in MTC',
    content: 'Low calcitonin in proven MTC can result from assay hook effect or poorly differentiated tumors that produce less calcitonin and more CEA.',
    keyPoints: [
      'Hook effect is corrected with sample dilution.',
      'Poor differentiation lowers calcitonin secretion.',
      'CEA may rise as calcitonin falls.'
    ],
    reference: 'Low calcitonin in MTC may reflect hook effect or poor differentiation with higher CEA production.'
  },
  {
    id: 'pe-cr-011-n21',
    subtopic: 'C-cell hyperplasia',
    title: 'How C-cell hyperplasia is diagnosed',
    content: 'C-cell hyperplasia requires clusters of at least seven C-cells extending beyond the junction of the upper and lower thirds of the thyroid lobe, and secondary causes must be excluded.',
    keyPoints: [
      'Clusters require at least seven C-cells.',
      'Distribution extends beyond normal lobe junctions.',
      'Secondary causes like PHPT and thyroiditis must be excluded.'
    ],
    reference: 'C-cell hyperplasia is defined by clusters of seven C-cells extending beyond normal thyroid lobe junctions after excluding secondary causes.'
  },
  {
    id: 'pe-cr-011-n22',
    subtopic: 'RET gene',
    title: 'How RET proto-oncogene mutations cause MEN2',
    content: 'RET is a receptor tyrosine kinase gene on chromosome 10q11.2, and gain-of-function mutations lead to constitutive signaling and tumorigenesis in neural crest-derived tissues.',
    keyPoints: [
      'RET encodes a receptor tyrosine kinase.',
      'Gain-of-function mutations drive MEN2.',
      'Neural crest-derived tissues are most affected.'
    ],
    reference: 'RET is a receptor tyrosine kinase gene on 10q11.2; gain-of-function mutations drive MEN2 tumorigenesis.'
  },
  {
    id: 'pe-cr-011-n23',
    subtopic: 'RET testing',
    title: 'How to decide who needs RET genetic testing',
    content: 'RET testing is recommended for any patient with medullary thyroid carcinoma, those with two MEN2-related endocrine tumors, familial MTC, first-degree relatives of MEN2, MEN2B phenotypes, and those with cutaneous lichen amyloidosis or Hirschsprung disease.',
    keyPoints: [
      'Isolated MTC at any age requires testing.',
      'MEN2B phenotype warrants urgent testing.',
      'Relatives of MEN2 patients should be screened.'
    ],
    reference: 'RET testing is advised for all MTC cases, MEN2-related tumors, familial MTC, relatives, MEN2B phenotype, and CLA or Hirschsprung disease.'
  },
  {
    id: 'pe-cr-011-n24',
    subtopic: 'MEN2B',
    title: 'How MEN2B presents clinically',
    content: 'MEN2B presents in infancy or childhood with aggressive MTC, bilateral pheochromocytomas, mucosal neuromas, marfanoid habitus, and typically no primary hyperparathyroidism.',
    keyPoints: [
      'MTC is universal and aggressive.',
      'Pheochromocytomas are often bilateral.',
      'Mucosal neuromas and marfanoid habitus are hallmarks.'
    ],
    reference: 'MEN2B features early aggressive MTC, bilateral pheochromocytoma, mucosal neuromas, marfanoid habitus, and no PHPT.'
  },
  {
    id: 'pe-cr-011-n25',
    subtopic: 'Mucosal neuromas',
    title: 'How mucosal neuromas appear in MEN2B',
    content: 'Mucosal neuromas are encapsulated nerve sheath tumors on the tongue, palate, pharynx, lips, eyelids, and GI tract, producing thickened eyelids and blubbery lips with submucosal nodules.',
    keyPoints: [
      'Lesions affect oral and GI mucosa.',
      'Thickened eyelid margins and corneal nerves can occur.',
      'Blubbery lips with nodules are characteristic.'
    ],
    reference: 'MEN2B mucosal neuromas involve oral and GI mucosa, can thicken eyelids, and cause blubbery lips with submucosal nodules.'
  },
  {
    id: 'pe-cr-011-n26',
    subtopic: 'MEN4',
    title: 'How MEN4 differs from MEN1',
    content: 'MEN4 mimics MEN1 clinically but is caused by CDKN1B mutations and is associated with parathyroid and pituitary tumors plus reproductive organ neoplasia.',
    keyPoints: [
      'CDKN1B mutations replace MEN1 mutations.',
      'Parathyroid and pituitary tumors are typical.',
      'Reproductive organ tumors help distinguish MEN4.'
    ],
    reference: 'MEN4 is MEN1-like with CDKN1B mutations, parathyroid and pituitary tumors, and reproductive organ neoplasia.'
  },
  {
    id: 'pe-cr-011-n27',
    subtopic: 'MEON',
    title: 'How MEON syndromes are defined',
    content: 'MEON syndromes include disorders with both endocrine and non-endocrine tumors, such as Carney complex, von Hippel-Lindau disease, and neurofibromatosis type 1.',
    keyPoints: [
      'MEON combines endocrine and non-endocrine neoplasia.',
      'Carney complex, VHL, and NF1 are key examples.',
      'These are distinct from classic MEN categories.'
    ],
    reference: 'MEON encompasses disorders like Carney complex, VHL disease, and neurofibromatosis type 1.'
  },
  {
    id: 'pe-cr-011-n28',
    subtopic: 'Carney complex',
    title: 'How Carney complex manifests clinically',
    content: 'Carney complex is characterized by lentigines, cardiac and cutaneous myxomas, and multiple endocrine neoplasias such as PPNAD, pituitary adenoma, and nodular goiter.',
    keyPoints: [
      'Pigmented skin and mucosal lesions are common.',
      'Myxomas involve heart and skin.',
      'Endocrine tumors include PPNAD and pituitary adenoma.'
    ],
    reference: 'Carney complex features lentigines, myxomas, and endocrine tumors including PPNAD, pituitary adenoma, and nodular goiter.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-011-q1',
    subtopic: 'Case vignette',
    question: 'A 42-year-old man has a giant GH/prolactin pituitary adenoma, hyperparathyroidism, pancreatic NET with gastrinoma, and a MEN1 mutation. The most likely diagnosis is:',
    options: [
      'MEN1 syndrome',
      'MEN2A syndrome',
      'MEN2B syndrome',
      'Carney complex'
    ],
    correctOption: 0,
    explanation: 'The triad of parathyroid, pituitary, and pancreatic NET with MEN1 mutation defines MEN1.',
    reference: 'MEN1 involves parathyroid, pituitary, and pancreatic NETs and is confirmed by MEN1 mutation.'
  },
  {
    id: 'pe-cr-011-q2',
    subtopic: 'Definition',
    question: 'Multiple endocrine neoplasia is defined by tumors involving:',
    options: [
      'Two or more endocrine organs in one patient',
      'Only one endocrine organ with aggressive behavior',
      'One endocrine and one non-endocrine organ',
      'Only thyroid and parathyroid glands'
    ],
    correctOption: 0,
    explanation: 'MEN requires tumors in at least two endocrine organs.',
    reference: 'MEN is characterized by tumors in two or more endocrine organs.'
  },
  {
    id: 'pe-cr-011-q3',
    subtopic: 'Classification',
    question: 'Which grouping best reflects current MEN classification?',
    options: [
      'MEN1, MEN2A, MEN2B, MEN4, and MEON',
      'MEN1, MEN2, MEN3, MEN5 only',
      'MEN1, MEN2, and MEN3 only',
      'MENA, MENB, MENC, and MEND'
    ],
    correctOption: 0,
    explanation: 'MEN is categorized into MEN1, MEN2A, MEN2B, MEN4, and MEON.',
    reference: 'MEN includes MEN1, MEN2A, MEN2B, MEN4, and MEON.'
  },
  {
    id: 'pe-cr-011-q4',
    subtopic: 'MEN1 prevalence',
    question: 'The most common endocrine manifestation of MEN1 is:',
    options: [
      'Primary hyperparathyroidism',
      'Pituitary adenoma',
      'Pheochromocytoma',
      'Medullary thyroid carcinoma'
    ],
    correctOption: 0,
    explanation: 'Parathyroid hyperplasia or adenoma occurs in about 95% of MEN1 patients.',
    reference: 'Parathyroid involvement is present in approximately 95% of MEN1 patients.'
  },
  {
    id: 'pe-cr-011-q5',
    subtopic: 'MEN1 tumors',
    question: 'Which pancreatic NET is most common in MEN1?',
    options: [
      'Gastrinoma',
      'Glucagonoma',
      'VIPoma',
      'Somatostatinoma'
    ],
    correctOption: 0,
    explanation: 'Gastrinoma is the most frequent pancreatic NET in MEN1.',
    reference: 'Gastrinoma is the most common pancreatic NET in MEN1.'
  },
  {
    id: 'pe-cr-011-q6',
    subtopic: 'MEN1 screening',
    question: 'Which scenario mandates screening for MEN1?',
    options: [
      'Two MEN1-associated endocrine tumors in one patient',
      'Isolated papillary thyroid carcinoma',
      'Isolated pituitary tumor in an older adult',
      'Single adrenal adenoma without other tumors'
    ],
    correctOption: 0,
    explanation: 'Presence of two MEN1-associated tumors is a classic indication for screening.',
    reference: 'MEN1 screening is advised for patients with two MEN1-associated endocrine tumors.'
  },
  {
    id: 'pe-cr-011-q7',
    subtopic: 'MEN1 suspicion',
    question: 'Which presentation most strongly suggests MEN1 in a patient with primary hyperparathyroidism?',
    options: [
      'Age younger than 30 years or multiglandular disease',
      'Age older than 60 years with a single adenoma',
      'Mild hypercalcemia with normal phosphate',
      'Isolated nephrolithiasis'
    ],
    correctOption: 0,
    explanation: 'Early-onset or multiglandular PHPT should prompt MEN1 evaluation.',
    reference: 'PHPT before 30 years of age or multiglandular disease should raise suspicion for MEN1.'
  },
  {
    id: 'pe-cr-011-q8',
    subtopic: 'MEN1 pituitary',
    question: 'The most common pituitary tumor in MEN1 is:',
    options: [
      'Prolactinoma',
      'Corticotropinoma',
      'Thyrotropinoma',
      'Gonadotropinoma'
    ],
    correctOption: 0,
    explanation: 'Prolactinoma is the most common MEN1 pituitary tumor.',
    reference: 'Prolactinoma is the most common pituitary tumor in MEN1.'
  },
  {
    id: 'pe-cr-011-q9',
    subtopic: 'MEN1 insulinoma',
    question: 'MEN1-associated insulinomas typically present:',
    options: [
      'Before 40 years of age',
      'Only after age 60',
      'Only during infancy',
      'Only after age 80'
    ],
    correctOption: 0,
    explanation: 'MEN1 insulinomas commonly present before 40 years.',
    reference: 'MEN1 insulinomas often present before age 40, usually before age 20.'
  },
  {
    id: 'pe-cr-011-q10',
    subtopic: 'MEN1 skin',
    question: 'Which cutaneous finding is most typical of MEN1?',
    options: [
      'Angiofibromas',
      'Café au lait macules',
      'Mucosal neuromas',
      'Port-wine stains'
    ],
    correctOption: 0,
    explanation: 'Angiofibromas and collagenomas are common in MEN1.',
    reference: 'MEN1 cutaneous findings include angiofibromas and collagenomas.'
  },
  {
    id: 'pe-cr-011-q11',
    subtopic: 'MEN1 gastrinoma',
    question: 'MEN1-related gastrinomas are most often located in the:',
    options: [
      'Duodenal wall within the gastrinoma triangle',
      'Tail of the pancreas only',
      'Adrenal medulla',
      'Thyroid gland'
    ],
    correctOption: 0,
    explanation: 'MEN1 gastrinomas are frequently duodenal and in the gastrinoma triangle.',
    reference: 'Gastrinomas in MEN1 are often in the duodenum within the gastrinoma triangle.'
  },
  {
    id: 'pe-cr-011-q12',
    subtopic: 'MEN1 gastrinoma',
    question: 'The preferred management of multiple small duodenal gastrinomas in MEN1 is:',
    options: [
      'Medical therapy with proton pump inhibitors and somatostatin analogues',
      'Routine Whipple procedure for all patients',
      'Radioactive iodine ablation',
      'Observation without therapy'
    ],
    correctOption: 0,
    explanation: 'Multiple small duodenal lesions limit surgical cure; medical therapy is preferred.',
    reference: 'MEN1 duodenal gastrinomas are often multiple and treated medically with PPIs and somatostatin analogues.'
  },
  {
    id: 'pe-cr-011-q13',
    subtopic: 'MEN1 pancreatic NET',
    question: 'Nonfunctioning pancreatic NETs in MEN1 generally warrant resection when they are:',
    options: [
      'Larger than 1 cm or rapidly growing',
      'Smaller than 2 mm',
      'Any size without growth',
      'Only if calcified'
    ],
    correctOption: 0,
    explanation: 'Tumors greater than 1 cm or rapidly growing are resected.',
    reference: 'Nonfunctioning pancreatic NETs in MEN1 are resected when larger than 1 cm or rapidly growing.'
  },
  {
    id: 'pe-cr-011-q14',
    subtopic: 'MEN1 gene',
    question: 'The MEN1 gene is located on:',
    options: [
      'Chromosome 11q13',
      'Chromosome 10q11.2',
      'Chromosome 17q11.2',
      'Chromosome 21q21'
    ],
    correctOption: 0,
    explanation: 'MEN1 is a tumor suppressor gene on 11q13.',
    reference: 'MEN1 is located on chromosome 11q13.'
  },
  {
    id: 'pe-cr-011-q15',
    subtopic: 'MEN2 overview',
    question: 'MEN2 syndromes are characterized by involvement of:',
    options: [
      'Neural crest-derived endocrine organs',
      'Only adrenal cortex tumors',
      'Only parathyroid tumors',
      'Only pancreatic tumors'
    ],
    correctOption: 0,
    explanation: 'MEN2 affects neural crest-derived endocrine organs.',
    reference: 'MEN2 is an autosomal dominant disorder involving neural crest-derived endocrine organs.'
  },
  {
    id: 'pe-cr-011-q16',
    subtopic: 'MEN2A',
    question: 'Which triad defines MEN2A?',
    options: [
      'Medullary thyroid carcinoma, pheochromocytoma, and primary hyperparathyroidism',
      'Pituitary adenoma, gastrinoma, and insulinoma',
      'Pheochromocytoma, paraganglioma, and pituitary adenoma',
      'Thyroid lymphoma, adrenal adenoma, and hyperthyroidism'
    ],
    correctOption: 0,
    explanation: 'MEN2A classically includes MTC, pheochromocytoma, and PHPT.',
    reference: 'MEN2A consists of medullary thyroid carcinoma, pheochromocytoma, and PHPT.'
  },
  {
    id: 'pe-cr-011-q17',
    subtopic: 'MEN2A',
    question: 'Which skin finding is associated with MEN2A?',
    options: [
      'Cutaneous lichen amyloidosis',
      'Café au lait macules',
      'Angiofibromas',
      'Blaschkoid hypopigmentation'
    ],
    correctOption: 0,
    explanation: 'Cutaneous lichen amyloidosis is linked to MEN2A.',
    reference: 'Cutaneous lichen amyloidosis is associated with MEN2A.'
  },
  {
    id: 'pe-cr-011-q18',
    subtopic: 'MEN2A suspicion',
    question: 'Which presentation most suggests MEN2A-associated MTC?',
    options: [
      'Young patient with nodular goiter and recurrent diarrhea',
      'Elderly patient with painless thyroid cyst',
      'Child with short stature and delayed puberty',
      'Adult with Graves disease and tremor'
    ],
    correctOption: 0,
    explanation: 'Early MTC can present with goiter and diarrhea in a young patient.',
    reference: 'MTC in MEN2A can present early with goiter and diarrhea.'
  },
  {
    id: 'pe-cr-011-q19',
    subtopic: 'MTC evaluation',
    question: 'Approximately what proportion of medullary thyroid carcinoma is hereditary?',
    options: [
      'About 20 percent',
      'About 2 percent',
      'About 70 percent',
      'About 90 percent'
    ],
    correctOption: 0,
    explanation: 'About one-fifth of MTC cases are hereditary.',
    reference: 'Approximately 20% of MTC cases are hereditary.'
  },
  {
    id: 'pe-cr-011-q20',
    subtopic: 'Calcitonin',
    question: 'Which condition can cause elevated calcitonin without MTC?',
    options: [
      'Chronic renal failure',
      'Secondary adrenal insufficiency',
      'Hypopituitarism',
      'Type 1 diabetes'
    ],
    correctOption: 0,
    explanation: 'Renal failure is a recognized non-MTC cause of high calcitonin.',
    reference: 'Calcitonin can be elevated in chronic renal failure.'
  },
  {
    id: 'pe-cr-011-q21',
    subtopic: 'C-cell hyperplasia',
    question: 'Which histologic feature supports C-cell hyperplasia?',
    options: [
      'Clusters of seven C-cells extending beyond normal lobe junctions',
      'Single isolated C-cells only',
      'Diffuse follicular hyperplasia without C-cells',
      'Absent C-cells in the thyroid'
    ],
    correctOption: 0,
    explanation: 'Diagnostic criteria include clusters of seven C-cells beyond normal junctions.',
    reference: 'C-cell hyperplasia requires clusters of at least seven C-cells extending beyond normal lobe junctions.'
  },
  {
    id: 'pe-cr-011-q22',
    subtopic: 'RET gene',
    question: 'RET proto-oncogene is located on:',
    options: [
      'Chromosome 10q11.2',
      'Chromosome 11q13',
      'Chromosome 17q11.2',
      'Chromosome 3p25'
    ],
    correctOption: 0,
    explanation: 'RET is located on chromosome 10q11.2.',
    reference: 'RET is located on chromosome 10q11.2.'
  },
  {
    id: 'pe-cr-011-q23',
    subtopic: 'RET testing',
    question: 'Which patient should undergo RET genetic testing?',
    options: [
      'Any patient with medullary thyroid carcinoma',
      'Any patient with papillary thyroid cancer',
      'Any patient with Graves disease',
      'Any patient with Hashimoto thyroiditis'
    ],
    correctOption: 0,
    explanation: 'RET testing is recommended for all MTC patients.',
    reference: 'RET testing is advised for any patient with medullary thyroid carcinoma.'
  },
  {
    id: 'pe-cr-011-q24',
    subtopic: 'MEN2B',
    question: 'Which feature is typical of MEN2B but not MEN2A?',
    options: [
      'Mucosal neuromas with marfanoid habitus',
      'Primary hyperparathyroidism',
      'Cutaneous lichen amyloidosis',
      'Hirschsprung disease'
    ],
    correctOption: 0,
    explanation: 'MEN2B is marked by mucosal neuromas and marfanoid habitus.',
    reference: 'MEN2B is characterized by mucosal neuromas and marfanoid habitus, with little to no PHPT.'
  },
  {
    id: 'pe-cr-011-q25',
    subtopic: 'MEN4',
    question: 'MEN4 is most commonly associated with mutations in:',
    options: [
      'CDKN1B',
      'RET',
      'MEN1',
      'NF1'
    ],
    correctOption: 0,
    explanation: 'MEN4 is linked to CDKN1B mutations.',
    reference: 'MEN4 is associated with CDKN1B gene mutation.'
  },
  {
    id: 'pe-cr-011-q26',
    subtopic: 'NF1 endocrine',
    question: 'Which endocrine manifestation is associated with neurofibromatosis type 1?',
    options: [
      'Pheochromocytoma',
      'Medullary thyroid carcinoma as the dominant tumor',
      'Primary adrenal insufficiency',
      'Hyperthyroidism as the hallmark'
    ],
    correctOption: 0,
    explanation: 'NF1 can be associated with pheochromocytoma and other endocrine tumors.',
    reference: 'Endocrine neoplasias in NF1 include pheochromocytoma and other neuroendocrine tumors.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-011-tf1',
    subtopic: 'Definition',
    statement: 'MEN is characterized by tumors involving two or more endocrine organs in one patient.',
    correctAnswer: true,
    explanation: 'This is the defining feature of MEN syndromes.',
    reference: 'MEN involves tumors in two or more endocrine organs.'
  },
  {
    id: 'pe-cr-011-tf2',
    subtopic: 'Classification',
    statement: 'MEN2 is subdivided into MEN2A and MEN2B, while MEN4 is a distinct category.',
    correctAnswer: true,
    explanation: 'These are the current MEN categories.',
    reference: 'MEN2 includes MEN2A and MEN2B, and MEN4 is a separate entity.'
  },
  {
    id: 'pe-cr-011-tf3',
    subtopic: 'MEN1 prevalence',
    statement: 'Primary hyperparathyroidism is present in the vast majority of MEN1 patients.',
    correctAnswer: true,
    explanation: 'Parathyroid disease occurs in about 95% of MEN1 cases.',
    reference: 'Parathyroid hyperplasia or adenoma occurs in about 95% of MEN1 patients.'
  },
  {
    id: 'pe-cr-011-tf4',
    subtopic: 'MEN1 screening',
    statement: 'First-degree relatives of MEN1 mutation carriers should undergo screening.',
    correctAnswer: true,
    explanation: 'Relatives have a substantial inherited risk.',
    reference: 'First-degree relatives of MEN1 mutation carriers should be screened.'
  },
  {
    id: 'pe-cr-011-tf5',
    subtopic: 'MEN1 pituitary',
    statement: 'Prolactinoma is the most common pituitary tumor in MEN1.',
    correctAnswer: true,
    explanation: 'Prolactinoma leads MEN1 pituitary subtypes.',
    reference: 'Prolactinoma is the most common pituitary tumor in MEN1.'
  },
  {
    id: 'pe-cr-011-tf6',
    subtopic: 'MEN1 gastrinoma',
    statement: 'MEN1 gastrinomas are usually single, large pancreatic tumors.',
    correctAnswer: false,
    explanation: 'MEN1 gastrinomas are usually small, multiple, and often duodenal.',
    reference: 'MEN1 gastrinomas are often small, multiple, and duodenal rather than large pancreatic tumors.'
  },
  {
    id: 'pe-cr-011-tf7',
    subtopic: 'MEN2A',
    statement: 'MEN2A includes medullary thyroid carcinoma, pheochromocytoma, and primary hyperparathyroidism.',
    correctAnswer: true,
    explanation: 'This is the classic MEN2A triad.',
    reference: 'MEN2A consists of medullary thyroid carcinoma, pheochromocytoma, and PHPT.'
  },
  {
    id: 'pe-cr-011-tf8',
    subtopic: 'Calcitonin',
    statement: 'Elevated calcitonin can occur in chronic renal failure without medullary thyroid carcinoma.',
    correctAnswer: true,
    explanation: 'Renal failure is a recognized non-MTC cause of elevated calcitonin.',
    reference: 'Calcitonin can be elevated in chronic renal failure and other non-MTC conditions.'
  },
  {
    id: 'pe-cr-011-tf9',
    subtopic: 'C-cell hyperplasia',
    statement: 'C-cell hyperplasia requires clusters of at least seven C-cells in thyroid tissue.',
    correctAnswer: true,
    explanation: 'Cluster size is part of diagnostic criteria.',
    reference: 'C-cell hyperplasia is diagnosed with clusters of at least seven C-cells.'
  },
  {
    id: 'pe-cr-011-tf10',
    subtopic: 'RET gene',
    statement: 'RET proto-oncogene gain-of-function mutations cause MEN2 syndromes.',
    correctAnswer: true,
    explanation: 'Constitutive RET signaling drives MEN2 tumorigenesis.',
    reference: 'Gain-of-function RET mutations result in MEN2 tumorigenesis.'
  },
  {
    id: 'pe-cr-011-tf11',
    subtopic: 'MEN2B',
    statement: 'MEN2B typically lacks primary hyperparathyroidism.',
    correctAnswer: true,
    explanation: 'PHPT is virtually absent in MEN2B.',
    reference: 'Parathyroid adenoma or hyperplasia virtually does not occur in MEN2B.'
  },
  {
    id: 'pe-cr-011-tf12',
    subtopic: 'MEN4',
    statement: 'MEN4 is associated with CDKN1B mutations rather than MEN1 mutations.',
    correctAnswer: true,
    explanation: 'CDKN1B is the defining gene alteration.',
    reference: 'MEN4 is associated with CDKN1B mutation instead of MEN1 mutation.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-011-ar1',
    subtopic: 'Definition',
    assertion: 'MEN syndromes require tumors in at least two endocrine organs.',
    reason: 'MEN involves synchronous or metachronous tumors across multiple endocrine glands.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'MEN is defined by tumors in two or more endocrine organs that may be synchronous or metachronous.'
  },
  {
    id: 'pe-cr-011-ar2',
    subtopic: 'MEN1 prevalence',
    assertion: 'Primary hyperparathyroidism is the most frequent MEN1 manifestation.',
    reason: 'Parathyroid hyperplasia or adenoma occurs in about 95% of MEN1 patients.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Parathyroid disease occurs in about 95% of MEN1 patients, making it the most common manifestation.'
  },
  {
    id: 'pe-cr-011-ar3',
    subtopic: 'MEN1 screening',
    assertion: 'Young patients with multiglandular primary hyperparathyroidism should be evaluated for MEN1.',
    reason: 'Multiglandular disease and early onset are typical MEN1 clues.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'PHPT at young age or multiglandular disease should raise suspicion for MEN1.'
  },
  {
    id: 'pe-cr-011-ar4',
    subtopic: 'MEN1 pituitary',
    assertion: 'MEN1 pituitary tumors are often macroadenomas with aggressive behavior.',
    reason: 'MEN1 pituitary tumors are usually resistant to medical therapy.',
    correctOption: 1,
    explanation: 'Both statements are true, but resistance does not fully explain macroadenoma prevalence.',
    reference: 'MEN1 pituitary tumors are usually macroadenomas with aggressive behavior and resistance to medical therapy.'
  },
  {
    id: 'pe-cr-011-ar5',
    subtopic: 'MEN1 gastrinoma',
    assertion: 'Medical therapy is often preferred for MEN1 duodenal gastrinomas.',
    reason: 'MEN1 duodenal gastrinomas are frequently multiple and very small.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the preference for medical therapy.',
    reference: 'MEN1 duodenal gastrinomas are small and multiple, making cure by surgery difficult, so medical therapy is preferred.'
  },
  {
    id: 'pe-cr-011-ar6',
    subtopic: 'MEN1 gene',
    assertion: 'MEN1 is a tumor suppressor gene on chromosome 11q13.',
    reason: 'Loss of heterozygosity in affected tissue leads to tumor formation.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the mechanism.',
    reference: 'MEN1 is a tumor suppressor on 11q13, and loss of heterozygosity leads to tumor formation.'
  },
  {
    id: 'pe-cr-011-ar7',
    subtopic: 'MEN2A',
    assertion: 'Medullary thyroid carcinoma is the most common and earliest feature of MEN2A.',
    reason: 'MTC is present in nearly all MEN2A patients.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'MTC is present in almost all MEN2A patients and is the earliest feature.'
  },
  {
    id: 'pe-cr-011-ar8',
    subtopic: 'Calcitonin',
    assertion: 'A low calcitonin level does not exclude medullary thyroid carcinoma.',
    reason: 'Hook effect or poorly differentiated tumors can lower measured calcitonin.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Low calcitonin in MTC can result from hook effect or poor differentiation.'
  },
  {
    id: 'pe-cr-011-ar9',
    subtopic: 'C-cell hyperplasia',
    assertion: 'C-cell hyperplasia should prompt evaluation for MEN2.',
    reason: 'C-cell hyperplasia can precede development of medullary thyroid carcinoma.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the need for MEN2 evaluation.',
    reference: 'C-cell hyperplasia precedes MTC and patients should be evaluated for MEN2 after excluding secondary causes.'
  },
  {
    id: 'pe-cr-011-ar10',
    subtopic: 'RET gene',
    assertion: 'RET mutations are found in nearly all MEN2A and MEN2B patients.',
    reason: 'Gain-of-function RET mutations drive tumorigenesis in neural crest-derived tissues.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the association.',
    reference: 'RET mutations are present in almost all MEN2A and MEN2B and cause constitutive signaling in neural crest-derived tissues.'
  },
  {
    id: 'pe-cr-011-ar11',
    subtopic: 'MEN2B',
    assertion: 'Mucosal neuromas are a hallmark of MEN2B.',
    reason: 'They arise as encapsulated nerve sheath tumors on mucosal surfaces.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the phenotype.',
    reference: 'MEN2B mucosal neuromas are encapsulated nerve sheath tumors on mucosal surfaces.'
  },
  {
    id: 'pe-cr-011-ar12',
    subtopic: 'MEN4',
    assertion: 'MEN4 can mimic MEN1 despite negative MEN1 mutation testing.',
    reason: 'MEN4 is caused by CDKN1B mutations and includes parathyroid and pituitary tumors.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains why MEN4 resembles MEN1.',
    reference: 'MEN4 is due to CDKN1B mutation and includes parathyroid and pituitary tumors, mimicking MEN1.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-011',
  book: 'clinical_rounds',
  chapterNo: '11',
  title: 'Multiple Endocrine Neoplasia',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/011_multiple_endocrine_neoplasia',
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
