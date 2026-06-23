#!/usr/bin/env node
'use strict';

const fs = require('fs');
const path = require('path');

const OUT = path.join(
  __dirname,
  '../data/pe-cr-009_disorders_of_sex_development.json'
);

const notes = [
  {
    id: 'pe-cr-009-n1',
    subtopic: 'Definition',
    title: 'How disorders of sex development are defined',
    content: 'Disorders of sex development (DSD) are congenital conditions in which chromosomal, gonadal, or phenotypic sex are incongruent, and the label also applies to some conditions without obvious genital ambiguity.',
    keyPoints: [
      'Mismatch can involve chromosomal, gonadal, or anatomical sex.',
      'The spectrum includes cases without visible ambiguity.',
      'Older labels like intersex are no longer preferred.'
    ],
    reference: 'DSD refers to congenital discordance among chromosomal, gonadal, or phenotypic sex and can include cases without overt ambiguity.'
  },
  {
    id: 'pe-cr-009-n2',
    subtopic: 'Genetics',
    title: 'Why chromosomal DSD arises from nondisjunction or chimerism',
    content: 'Chromosomal DSD is caused by meiotic or mitotic nondisjunction leading to aneuploidy and mosaicism, or by chimerism when two genetically distinct cell lines coexist after double fertilization or early zygote fusion.',
    keyPoints: [
      'Meiotic nondisjunction yields classic sex chromosome aneuploidy.',
      'Mitotic errors cause mosaic karyotypes.',
      'Chimerism reflects two genetic origins in one individual.'
    ],
    reference: 'Chromosomal DSD results from meiotic or mitotic nondisjunction or from chimerism produced by double fertilization or early zygote fusion.'
  },
  {
    id: 'pe-cr-009-n3',
    subtopic: 'Genetics',
    title: 'How mosaicism differs from chimerism in DSD',
    content: 'Mosaicism arises from a single zygote with post-zygotic mitotic errors, whereas chimerism reflects two distinct genetic lineages in one individual due to dispermy or early fusion of zygotes.',
    keyPoints: [
      'Mosaicism: one zygote, multiple cell lines.',
      'Chimerism: two genetic origins.',
      'Ovotesticular DSD is a classic example of chimerism.'
    ],
    reference: 'Mosaicism comes from one zygote with mitotic nondisjunction, while chimerism arises from two genetically distinct cell lines.'
  },
  {
    id: 'pe-cr-009-n4',
    subtopic: 'Embryology',
    title: 'How sex determination differs from sex differentiation',
    content: 'Sex determination is the genetic decision of the bipotential gonad to become testis or ovary, while sex differentiation is the hormone-driven development of internal and external genitalia; both occur mainly during weeks 7 to 12 of gestation.',
    keyPoints: [
      'Determination sets gonadal fate.',
      'Differentiation shapes internal and external anatomy.',
      'The critical window is mid-first trimester.'
    ],
    reference: 'Sex determination establishes gonadal fate, whereas differentiation shapes internal and external genitalia during weeks 7 to 12.'
  },
  {
    id: 'pe-cr-009-n5',
    subtopic: 'Embryology',
    title: 'How key genes guide testis and ovary development',
    content: 'Testis development is driven by genes such as SRY, SOX9, SF1, WT1, and DHH, while ovarian development requires active signaling from WNT4, FOXL2, and RSPO1 rather than passive default.',
    keyPoints: [
      'SRY initiates the testis pathway via SOX9.',
      'Testis fate depends on multiple transcription factors.',
      'Ovarian fate requires WNT4, FOXL2, and RSPO1.'
    ],
    reference: 'Testis determination depends on SRY, SOX9, SF1, WT1, and DHH, while ovarian development requires WNT4, FOXL2, and RSPO1.'
  },
  {
    id: 'pe-cr-009-n6',
    subtopic: 'Genetics',
    title: 'How DAX1 dosage alters gonadal development',
    content: 'DAX1 on Xp20.3 is dose sensitive: one copy supports normal gonadal development, loss leads to hypogonadotropic hypogonadism with adrenal hypoplasia, and duplication promotes gonadal dysgenesis.',
    keyPoints: [
      'DAX1 is critical for gonads and adrenal cortex.',
      'Loss causes adrenal hypoplasia with hypogonadism.',
      'Duplication can trigger gonadal dysgenesis.'
    ],
    reference: 'DAX1 is dose dependent; loss causes hypogonadism with adrenal hypoplasia, while duplication leads to gonadal dysgenesis.'
  },
  {
    id: 'pe-cr-009-n7',
    subtopic: 'Embryology',
    title: 'How Wolffian and Mullerian ducts map to internal organs',
    content: 'Wolffian ducts form epididymis, vas deferens, seminal vesicles, and related structures in males, while Mullerian ducts form fallopian tubes, uterus, cervix, and upper vagina in females.',
    keyPoints: [
      'Wolffian ducts become male internal tract structures.',
      'Mullerian ducts become female internal tract structures.',
      'Both duct systems are present early in development.'
    ],
    reference: 'Wolffian derivatives include epididymis and vas deferens, whereas Mullerian derivatives include the uterus and fallopian tubes.'
  },
  {
    id: 'pe-cr-009-n8',
    subtopic: 'Embryology',
    title: 'How external genitalia development depends on androgens',
    content: 'The genital tubercle, urogenital folds, and labioscrotal swellings differentiate into male structures with androgen exposure; in the absence of androgens they form the clitoris, labia minora, and labia majora.',
    keyPoints: [
      'Male differentiation requires androgen exposure.',
      'Female differentiation occurs without androgen stimulation.',
      'Common primordia underlie both pathways.'
    ],
    reference: 'External genital primordia form male structures with androgens and female structures when androgens are absent.'
  },
  {
    id: 'pe-cr-009-n9',
    subtopic: 'Embryology',
    title: 'How AMH and testosterone shape male differentiation',
    content: 'Sertoli cell AMH induces Mullerian regression, Leydig cell testosterone stabilizes Wolffian ducts, and conversion to dihydrotestosterone drives external virilization because DHT has much higher androgen receptor affinity.',
    keyPoints: [
      'AMH causes Mullerian duct regression.',
      'Testosterone preserves Wolffian ducts.',
      'DHT mediates external virilization.'
    ],
    reference: 'AMH regresses Mullerian ducts, testosterone stabilizes Wolffian ducts, and DHT mediates external virilization.'
  },
  {
    id: 'pe-cr-009-n10',
    subtopic: 'Assessment',
    title: 'How Prader staging and EMS quantify genital ambiguity',
    content: 'Prader staging grades virilization in 46,XX infants, while the external masculinization score (EMS) quantifies undervirilization in 46,XY DSD, with a typical male score of 12 and female score of 0.',
    keyPoints: [
      'Prader staging is for 46,XX virilization.',
      'EMS grades undervirilization in 46,XY DSD.',
      'Normal male EMS is 12 and female EMS is 0.'
    ],
    reference: 'Prader staging grades virilization in 46,XX, while EMS grades undervirilization in 46,XY with male score 12 and female score 0.'
  },
  {
    id: 'pe-cr-009-n11',
    subtopic: 'Embryology',
    title: 'How timing of prenatal androgens drives virilization',
    content: 'Androgen exposure before 12 weeks of gestation leads to clitoromegaly, posterior labial fusion, and a single urogenital opening, whereas exposure after 12 weeks generally causes isolated clitoromegaly.',
    keyPoints: [
      'Early exposure causes fusion and single opening.',
      'Later exposure tends to cause isolated clitoromegaly.',
      'Clitoral length of 9 mm or more is concerning.'
    ],
    reference: 'Androgen exposure before 12 weeks causes clitoromegaly with posterior fusion and a single opening, while later exposure causes isolated clitoromegaly.'
  },
  {
    id: 'pe-cr-009-n12',
    subtopic: 'Embryology',
    title: 'Why a blind vaginal pouch develops in some 46,XY DSD',
    content: 'A blind vaginal pouch forms when AMH remains intact but testosterone action is impaired, leading to Mullerian regression with partial urogenital sinus differentiation; causes include CAIS, 17alpha-hydroxylase deficiency, 17beta-HSD3 deficiency, and 5alpha-reductase deficiency.',
    keyPoints: [
      'AMH regression preserves only lower vaginal segment.',
      'Defective androgen action prevents full male differentiation.',
      'Several androgen biosynthesis or action defects can cause it.'
    ],
    reference: 'Blind vaginal pouch occurs when AMH is preserved but testosterone action is impaired, as in CAIS or androgen biosynthetic defects.'
  },
  {
    id: 'pe-cr-009-n13',
    subtopic: 'Embryology',
    title: 'Why both Wolffian and Mullerian derivatives can persist',
    content: 'Persistent Mullerian duct syndrome, ovotesticular DSD, and mixed gonadal dysgenesis can yield both duct systems because AMH action is insufficient or gonadal tissue is asymmetric.',
    keyPoints: [
      'PMDS reflects impaired AMH secretion or action.',
      'OT-DSD and MGD often show asymmetric gonads.',
      'Duct derivatives follow the side-specific gonad.'
    ],
    reference: 'Both duct systems can be present in PMDS, OT-DSD, or MGD when AMH action is inadequate or gonads are asymmetric.'
  },
  {
    id: 'pe-cr-009-n14',
    subtopic: '46,XY DSD',
    title: 'How etiologies of 46,XY DSD are organized',
    content: '46,XY DSD stems from impaired testis development, androgen biosynthesis, or androgen action, and female external genitalia can be seen with complete gonadal dysgenesis, CAIS, or severe steroidogenic defects.',
    keyPoints: [
      'Major groups: testis development, biosynthesis, action.',
      'Female external genitalia suggests severe defects.',
      'Ambiguity can occur across all categories.'
    ],
    reference: '46,XY DSD includes testis development disorders, androgen biosynthetic defects, and androgen resistance; female genitalia can occur in severe forms.'
  },
  {
    id: 'pe-cr-009-n15',
    subtopic: '46,XX DSD',
    title: 'How etiologies of 46,XX DSD are organized',
    content: '46,XX DSD arises from disorders of gonadal development or androgen excess; strong androgen exposure during weeks 8 to 12 can produce an apparently male phenotype even without testes.',
    keyPoints: [
      'Gonadal development disorders include SRY translocation.',
      'Androgen excess causes virilization.',
      'Early exposure yields the most masculinized phenotype.'
    ],
    reference: '46,XX DSD results from gonadal development defects or androgen excess, and early androgen exposure can produce a male-appearing phenotype.'
  },
  {
    id: 'pe-cr-009-n16',
    subtopic: 'Clinical features',
    title: 'How micropenis is defined and what it implies',
    content: 'Micropenis is defined as stretched penile length below minus 2.5 standard deviations for age, with a term newborn cutoff near 2.5 cm, and suggests impaired androgen synthesis/action or pituitary disease.',
    keyPoints: [
      'Definition uses stretched penile length.',
      'Term newborn cutoff is about 2.5 cm.',
      'Etiologies include hypogonadism or GH deficiency.'
    ],
    reference: 'Micropenis is stretched penile length below -2.5 SD, about 2.5 cm in term newborns, and suggests androgen or pituitary disorders.'
  },
  {
    id: 'pe-cr-009-n17',
    subtopic: 'Clinical features',
    title: 'How hypospadias is classified and linked to DSD',
    content: 'Hypospadias is an ectopic urethral meatus on the ventral penis, classified as distal, mid, or proximal; proximal forms are more often associated with DSD and may coexist with chordee.',
    keyPoints: [
      'Distal is most common.',
      'Proximal hypospadias raises DSD concern.',
      'Chordee and dorsal hood are common associations.'
    ],
    reference: 'Hypospadias is a ventral meatus classified as distal, mid, or proximal, and proximal forms are more often associated with DSD.'
  },
  {
    id: 'pe-cr-009-n18',
    subtopic: 'Clinical features',
    title: 'How chordee develops in undervirilized 46,XY DSD',
    content: 'Chordee results from ventral penile tissues lagging behind dorsal corporal growth, likely due to lower androgen effect on urethral and spongiosal development.',
    keyPoints: [
      'Ventral tissues are underdeveloped.',
      'Dorsal corporal growth predominates.',
      'Androgen action is critical for urethral development.'
    ],
    reference: 'Chordee reflects underdevelopment of ventral tissues relative to dorsal corpora in undervirilized 46,XY DSD.'
  },
  {
    id: 'pe-cr-009-n19',
    subtopic: 'Clinical features',
    title: 'How cryptorchidism is defined and distributed',
    content: 'Cryptorchidism is failure of one or both testes to descend into the scrotum, usually resolving by 3 months of age, and most undescended testes are located high scrotal or inguinal.',
    keyPoints: [
      'Most spontaneous descent occurs by 3 months.',
      'Persistent undescended testes are uncommon after 6 to 9 months.',
      'High scrotal and inguinal locations are most common.'
    ],
    reference: 'Cryptorchidism is undescended testes, often descending by 3 months, and commonly located high scrotal or inguinal.'
  },
  {
    id: 'pe-cr-009-n20',
    subtopic: 'Clinical features',
    title: 'Why cryptorchidism with hypospadias raises DSD risk',
    content: 'Isolated cryptorchidism is usually idiopathic, but the combination with hypospadias increases the probability of DSD and suggests etiologies such as PAIS, androgen biosynthetic defects, mixed gonadal dysgenesis, or OT-DSD.',
    keyPoints: [
      'DSD is uncommon in isolated cryptorchidism.',
      'Hypospadias increases the likelihood of DSD.',
      'PAIS, biosynthetic defects, MGD, and OT-DSD are key causes.'
    ],
    reference: 'Cryptorchidism plus hypospadias increases DSD likelihood, with causes including PAIS, androgen biosynthetic defects, MGD, and OT-DSD.'
  },
  {
    id: 'pe-cr-009-n21',
    subtopic: 'Evaluation',
    title: 'How to distinguish anorchia from bilateral cryptorchidism',
    content: 'High gonadotropins with low testosterone suggest absent or dysgenetic testes, while low gonadotropins favor cryptorchidism due to central hypogonadism; AMH or inhibin B absence supports anorchia.',
    keyPoints: [
      'High LH/FSH with low testosterone suggests anorchia.',
      'AMH and inhibin B help confirm testis absence.',
      'hCG testing is useful in prepubertal children.'
    ],
    reference: 'Anorchia is suggested by high gonadotropins with low testosterone and undetectable AMH or inhibin B.'
  },
  {
    id: 'pe-cr-009-n22',
    subtopic: 'Evaluation',
    title: 'How hCG stimulation testing is used in DSD',
    content: 'Short-course hCG testing measures androgen response to distinguish androgen biosynthetic defects, 5alpha-reductase deficiency, and androgen resistance; T/DHT ratio above 10 suggests 5alpha-reductase deficiency, while T/A ratio below 0.8 with high androstenedione supports 17beta-HSD3 deficiency.',
    keyPoints: [
      'hCG is given for 3 days with pre and post testing.',
      'T/DHT ratio greater than 10 favors 5alpha-reductase deficiency.',
      'Low T/A ratio with high androstenedione favors 17beta-HSD3 deficiency.'
    ],
    reference: 'hCG testing differentiates androgen biosynthesis and action defects, using ratios such as T/DHT >10 or T/A <0.8 with high androstenedione.'
  },
  {
    id: 'pe-cr-009-n23',
    subtopic: 'Neonatal evaluation',
    title: 'How the newborn DSD evaluation starts with gonad palpation',
    content: 'In neonatal genital ambiguity, palpation of gonads guides the workup: palpable gonads suggest testes or ovotestes, nonpalpable gonads suggest undervirilized 46,XY or virilized 46,XX, and asymmetric findings suggest MGD or OT-DSD.',
    keyPoints: [
      'Palpable gonads imply testicular tissue.',
      'Nonpalpable gonads broaden the differential.',
      'Asymmetry raises suspicion for MGD or OT-DSD.'
    ],
    reference: 'Palpable gonads point to testes or ovotestes, nonpalpable gonads suggest 46,XY undervirilization or 46,XX virilization, and asymmetry suggests MGD or OT-DSD.'
  },
  {
    id: 'pe-cr-009-n24',
    subtopic: 'Psychosexual',
    title: 'How psychosexual development is assessed',
    content: 'Psychosexual development comprises gender identity (self-perceived gender), gender role (behavioral expression), and gender orientation (sexual partner preference).',
    keyPoints: [
      'Identity is the internal sense of gender.',
      'Role reflects social behavior and expression.',
      'Orientation refers to partner preference.'
    ],
    reference: 'Psychosexual development includes gender identity, gender role, and gender orientation.'
  },
  {
    id: 'pe-cr-009-n25',
    subtopic: 'Psychosexual',
    title: 'How gender dysphoria is defined in DSD care',
    content: 'Gender dysphoria describes significant distress from mismatch between gender identity and assigned sex of rearing, and it may occur with or without DSD.',
    keyPoints: [
      'Distress is the defining feature.',
      'Mismatch involves identity and assigned sex.',
      'It is not limited to DSD diagnoses.'
    ],
    reference: 'Gender dysphoria is distress caused by discordance between gender identity and assigned sex, and can occur with or without DSD.'
  },
  {
    id: 'pe-cr-009-n26',
    subtopic: 'Surgery',
    title: 'How timing of hypospadias repair is determined',
    content: 'Hypospadias repair is ideally performed between 6 and 12 months of age to support psychosocial development and tissue pliability, and proximal lesions with chordee often require two-stage reconstruction.',
    keyPoints: [
      'Preferred age window is 6 to 12 months.',
      'Early repair aligns with gender identity formation.',
      'Proximal hypospadias may need staged repair.'
    ],
    reference: 'Hypospadias repair is ideally done at 6 to 12 months, with proximal lesions often needing two-stage reconstruction.'
  },
  {
    id: 'pe-cr-009-n27',
    subtopic: 'Surgery',
    title: 'How gonadectomy decisions balance cancer risk and sex of rearing',
    content: 'Gonadectomy is recommended when tumor risk is high or when gonads conflict with sex of rearing, such as in 46,XY gonadal dysgenesis or MGD, while CAIS and OT-DSD require individualized timing and surveillance.',
    keyPoints: [
      'High-risk gonads merit early removal.',
      'Sex of rearing influences the decision.',
      'Lower-risk conditions may allow delayed surgery.'
    ],
    reference: 'Gonadectomy is advised for high-risk gonads or discordant sex of rearing, while lower-risk conditions may allow delayed removal with surveillance.'
  },
  {
    id: 'pe-cr-009-n28',
    subtopic: '46,XX DSD',
    title: 'How XX male syndrome presents clinically',
    content: '46,XX male syndrome results from SRY translocation to the X chromosome, leading to a male phenotype with small testes, infertility, gynecomastia, and elevated FSH from germ cell failure.',
    keyPoints: [
      'SRY translocation drives male phenotype.',
      'Testes are small with primary infertility.',
      'FSH is consistently elevated.'
    ],
    reference: 'XX male syndrome is caused by SRY translocation and presents with male phenotype, small testes, infertility, gynecomastia, and elevated FSH.'
  }
].map(note => ({ ...note, type: 'note' }));

const mcqs = [
  {
    id: 'pe-cr-009-q1',
    subtopic: 'Case vignette',
    question: 'A 20-year-old reared as female has primary amenorrhea, genital ambiguity, bilateral palpable gonads, 46,XY karyotype, high androstenedione with low testosterone, and a low T/A ratio after hCG. The most likely diagnosis is:',
    options: [
      '17beta-HSD3 deficiency',
      '5alpha-reductase type 2 deficiency',
      'Partial androgen insensitivity syndrome',
      '46,XY complete gonadal dysgenesis'
    ],
    correctOption: 0,
    explanation: 'High androstenedione with low testosterone and low T/A ratio is typical of 17beta-HSD3 deficiency.',
    reference: 'Low testosterone with high androstenedione and low T/A ratio after hCG supports 17beta-HSD3 deficiency.'
  },
  {
    id: 'pe-cr-009-q2',
    subtopic: 'Definition',
    question: 'Disorders of sex development are defined as congenital conditions with discordance between:',
    options: [
      'Chromosomal, gonadal, or phenotypic sex',
      'Age and pubertal stage only',
      'Gonadal size and body mass index',
      'Only external genital appearance'
    ],
    correctOption: 0,
    explanation: 'DSD refers to mismatch among chromosomal, gonadal, and phenotypic sex.',
    reference: 'DSD are congenital disorders with discordance between chromosomal, gonadal, or phenotypic sex.'
  },
  {
    id: 'pe-cr-009-q3',
    subtopic: 'Genetics',
    question: 'Chromosomal DSD most commonly results from:',
    options: [
      'Meiotic or mitotic nondisjunction and chimerism',
      'Somatic point mutations in the androgen receptor',
      'Environmental endocrine disruptors only',
      'Maternal diabetes during pregnancy'
    ],
    correctOption: 0,
    explanation: 'Nondisjunction and chimerism are key mechanisms.',
    reference: 'Chromosomal DSD results from nondisjunction during meiosis or mitosis or from chimerism.'
  },
  {
    id: 'pe-cr-009-q4',
    subtopic: 'Genetics',
    question: 'Which statement best distinguishes mosaicism from chimerism?',
    options: [
      'Mosaicism comes from one zygote; chimerism from two genetic origins',
      'Mosaicism requires two zygotes; chimerism requires one',
      'Mosaicism is always lethal; chimerism is always benign',
      'Mosaicism only affects males'
    ],
    correctOption: 0,
    explanation: 'Mosaicism is one zygote with multiple cell lines, while chimerism involves two genetic origins.',
    reference: 'Mosaicism originates from one zygote, whereas chimerism reflects two genetically distinct cell lines.'
  },
  {
    id: 'pe-cr-009-q5',
    subtopic: 'Embryology',
    question: 'Sex determination refers to:',
    options: [
      'Gonadal differentiation into testis or ovary',
      'Formation of external genitalia only',
      'Menarche onset',
      'Adrenarche onset'
    ],
    correctOption: 0,
    explanation: 'Determination is the decision of gonadal fate.',
    reference: 'Sex determination is the development of a bipotential gonad into testis or ovary.'
  },
  {
    id: 'pe-cr-009-q6',
    subtopic: 'Genetics',
    question: 'Duplication of DAX1 most strongly predisposes to:',
    options: [
      'Gonadal dysgenesis',
      'Complete androgen insensitivity',
      'Congenital adrenal hyperplasia',
      'SRY translocation'
    ],
    correctOption: 0,
    explanation: 'DAX1 is dose sensitive and duplication can impair gonadal development.',
    reference: 'Duplication of DAX1 is associated with gonadal dysgenesis.'
  },
  {
    id: 'pe-cr-009-q7',
    subtopic: 'Embryology',
    question: 'Which structure is a Wolffian duct derivative in males?',
    options: [
      'Epididymis',
      'Uterus',
      'Upper vagina',
      'Fallopian tube'
    ],
    correctOption: 0,
    explanation: 'Epididymis is derived from the Wolffian duct.',
    reference: 'Wolffian duct derivatives include the epididymis and vas deferens.'
  },
  {
    id: 'pe-cr-009-q8',
    subtopic: 'Embryology',
    question: 'Anti-Mullerian hormone produced by Sertoli cells causes:',
    options: [
      'Regression of Mullerian ducts',
      'Formation of the epididymis',
      'Fusion of labioscrotal folds',
      'Development of the prostate'
    ],
    correctOption: 0,
    explanation: 'AMH drives Mullerian duct regression.',
    reference: 'AMH from Sertoli cells regresses Mullerian ducts.'
  },
  {
    id: 'pe-cr-009-q9',
    subtopic: 'Embryology',
    question: 'External genital virilization in the embryo relies primarily on:',
    options: [
      'Dihydrotestosterone',
      'Estradiol',
      'Progesterone',
      'Cortisol'
    ],
    correctOption: 0,
    explanation: 'DHT has high androgen receptor affinity and drives virilization.',
    reference: 'External genital differentiation requires testosterone conversion to DHT.'
  },
  {
    id: 'pe-cr-009-q10',
    subtopic: 'Assessment',
    question: 'The external masculinization score for a typical male newborn is:',
    options: [
      '12',
      '8',
      '5',
      '0'
    ],
    correctOption: 0,
    explanation: 'EMS ranges from 0 in typical females to 12 in typical males.',
    reference: 'EMS score is 12 for a normal male external genitalia and 0 for a normal female.'
  },
  {
    id: 'pe-cr-009-q11',
    subtopic: 'Embryology',
    question: 'Androgen exposure before 12 weeks of gestation in a 46,XX fetus most likely results in:',
    options: [
      'Clitoromegaly with posterior labial fusion and a single urogenital opening',
      'Isolated clitoromegaly only',
      'Normal female genitalia',
      'Isolated labial fusion without clitoromegaly'
    ],
    correctOption: 0,
    explanation: 'Early exposure produces more extensive virilization.',
    reference: 'Androgen exposure before 12 weeks causes clitoromegaly, posterior fusion, and a single urogenital opening.'
  },
  {
    id: 'pe-cr-009-q12',
    subtopic: 'Embryology',
    question: 'A blind vaginal pouch in a 46,XY individual is most consistent with:',
    options: [
      'Defective androgen action with preserved AMH',
      'Excess fetal estrogen production',
      'Complete absence of AMH',
      'Early rupture of the genital sinus'
    ],
    correctOption: 0,
    explanation: 'AMH preserves Mullerian regression while impaired androgen action prevents full male differentiation.',
    reference: 'Blind vaginal pouch reflects preserved AMH with impaired testosterone action.'
  },
  {
    id: 'pe-cr-009-q13',
    subtopic: 'Embryology',
    question: 'Presence of both Wolffian and Mullerian derivatives suggests:',
    options: [
      'Persistent Mullerian duct syndrome',
      'Complete androgen insensitivity',
      'Turner syndrome',
      '46,XX complete gonadal dysgenesis'
    ],
    correctOption: 0,
    explanation: 'PMDS is characterized by retained Mullerian structures in a male.',
    reference: 'Both duct systems can be present in PMDS, OT-DSD, or MGD.'
  },
  {
    id: 'pe-cr-009-q14',
    subtopic: '46,XY DSD',
    question: 'Female external genitalia in a 46,XY individual is most commonly seen with:',
    options: [
      'Complete androgen insensitivity syndrome',
      'SRY translocation',
      'Congenital adrenal hyperplasia due to 21alpha-hydroxylase deficiency',
      'Ovotesticular DSD'
    ],
    correctOption: 0,
    explanation: 'CAIS causes female external genitalia with absent Mullerian structures.',
    reference: '46,XY individuals with CAIS typically have female external genitalia.'
  },
  {
    id: 'pe-cr-009-q15',
    subtopic: '46,XX DSD',
    question: 'The most common cause of ambiguous genitalia in a 46,XX newborn is:',
    options: [
      'Congenital adrenal hyperplasia due to 21alpha-hydroxylase deficiency',
      'Complete androgen insensitivity',
      '46,XY gonadal dysgenesis',
      'Vanishing testes syndrome'
    ],
    correctOption: 0,
    explanation: '21alpha-hydroxylase deficiency is the most common cause.',
    reference: 'CAH due to 21alpha-hydroxylase deficiency is the most common cause of virilization in 46,XX infants.'
  },
  {
    id: 'pe-cr-009-q16',
    subtopic: '46,XX DSD',
    question: 'A 46,XX individual with apparently male external genitalia is most likely to have:',
    options: [
      'SRY gene translocation to the X chromosome',
      'Complete androgen insensitivity',
      '5alpha-reductase deficiency',
      'Mixed gonadal dysgenesis'
    ],
    correctOption: 0,
    explanation: 'SRY translocation can produce a male phenotype in 46,XX.',
    reference: 'SRY translocation to the X chromosome can cause 46,XX testicular DSD.'
  },
  {
    id: 'pe-cr-009-q17',
    subtopic: 'Clinical features',
    question: 'Micropenis in a term newborn is typically defined as stretched penile length:',
    options: [
      'Less than 2.5 cm',
      'Less than 4.0 cm',
      'Greater than 3.5 cm',
      'Exactly 5.0 cm'
    ],
    correctOption: 0,
    explanation: 'The cutoff is about 2.5 cm in term newborns.',
    reference: 'Micropenis is stretched penile length below -2.5 SD, about 2.5 cm in term newborns.'
  },
  {
    id: 'pe-cr-009-q18',
    subtopic: 'Clinical features',
    question: 'The most common type of hypospadias is:',
    options: [
      'Distal (glandular or subcoronal)',
      'Proximal (perineal)',
      'Mid-shaft only',
      'Penoscrotal only'
    ],
    correctOption: 0,
    explanation: 'Distal hypospadias accounts for the majority of cases.',
    reference: 'Distal hypospadias is the most common form.'
  },
  {
    id: 'pe-cr-009-q19',
    subtopic: 'Clinical features',
    question: 'Chordee in undervirilized 46,XY DSD occurs because:',
    options: [
      'Ventral penile tissues are underdeveloped compared with dorsal corpora',
      'Dorsal penile tissues are absent',
      'Penile skin is fused to the scrotum only',
      'Estrogen excess shortens the urethra'
    ],
    correctOption: 0,
    explanation: 'Disproportionate growth of dorsal vs ventral tissues produces curvature.',
    reference: 'Chordee reflects underdevelopment of ventral tissues relative to dorsal corpora.'
  },
  {
    id: 'pe-cr-009-q20',
    subtopic: 'Clinical features',
    question: 'Most spontaneous testicular descent in cryptorchidism occurs by:',
    options: [
      '3 months of age',
      '12 months of age',
      '24 months of age',
      '5 years of age'
    ],
    correctOption: 0,
    explanation: 'Most descent occurs within the first 3 months.',
    reference: 'Spontaneous descent of testes usually occurs by 1 to 3 months of age.'
  },
  {
    id: 'pe-cr-009-q21',
    subtopic: 'Evaluation',
    question: 'After hCG stimulation, a testosterone to dihydrotestosterone ratio greater than 10 suggests:',
    options: [
      '5alpha-reductase type 2 deficiency',
      '17beta-HSD3 deficiency',
      'Complete androgen insensitivity',
      'Gonadal dysgenesis'
    ],
    correctOption: 0,
    explanation: 'T/DHT >10 is characteristic of 5alpha-reductase deficiency.',
    reference: 'A T/DHT ratio greater than 10 after hCG indicates 5alpha-reductase type 2 deficiency.'
  },
  {
    id: 'pe-cr-009-q22',
    subtopic: 'Evaluation',
    question: 'High androstenedione with a T/A ratio below 0.8 after hCG most strongly suggests:',
    options: [
      '17beta-HSD3 deficiency',
      'Partial androgen insensitivity',
      'Complete gonadal dysgenesis',
      'CAH due to 21alpha-hydroxylase deficiency'
    ],
    correctOption: 0,
    explanation: 'Low T/A ratio with high androstenedione supports 17beta-HSD3 deficiency.',
    reference: 'T/A ratio below 0.8 with elevated androstenedione indicates 17beta-HSD3 deficiency.'
  },
  {
    id: 'pe-cr-009-q23',
    subtopic: '46,XX DSD',
    question: 'Which CAH variant can produce genital ambiguity in both 46,XX and 46,XY individuals?',
    options: [
      'P450 oxidoreductase deficiency',
      '21alpha-hydroxylase deficiency',
      '11beta-hydroxylase deficiency',
      '17alpha-hydroxylase deficiency'
    ],
    correctOption: 0,
    explanation: 'POR deficiency is the variant associated with ambiguity in both sexes.',
    reference: 'P450 oxidoreductase deficiency is the CAH variant associated with ambiguity in both sexes.'
  },
  {
    id: 'pe-cr-009-q24',
    subtopic: '46,XX DSD',
    question: 'Placental aromatase deficiency is classically associated with:',
    options: [
      'Maternal virilization and 46,XX fetal virilization',
      'Isolated male infertility only',
      'Hypertension with low androgens',
      'Ambiguous genitalia in 46,XY infants only'
    ],
    correctOption: 0,
    explanation: 'Excess fetal androgens virilize both mother and female fetus.',
    reference: 'Placental aromatase deficiency leads to maternal virilization and virilization of 46,XX fetuses.'
  },
  {
    id: 'pe-cr-009-q25',
    subtopic: '46,XX DSD',
    question: 'The typical genetic mechanism in XX male syndrome is:',
    options: [
      'SRY translocation to the X chromosome',
      'Loss of the X chromosome',
      'Duplication of the androgen receptor gene',
      'Deletion of WNT4'
    ],
    correctOption: 0,
    explanation: 'SRY translocation produces a male phenotype in 46,XX.',
    reference: 'XX male syndrome is caused by SRY translocation to the X chromosome.'
  },
  {
    id: 'pe-cr-009-q26',
    subtopic: 'Surgery',
    question: 'Corrective surgery for hypospadias is ideally performed at:',
    options: [
      '6 to 12 months of age',
      'Birth to 1 month of age',
      '4 to 5 years of age',
      'After puberty only'
    ],
    correctOption: 0,
    explanation: 'Repair in infancy aligns with tissue pliability and psychosocial considerations.',
    reference: 'Hypospadias repair is ideally performed between 6 and 12 months.'
  }
].map(mcq => ({ ...mcq, type: 'mcq' }));

const trueFalse = [
  {
    id: 'pe-cr-009-tf1',
    subtopic: 'Definition',
    statement: 'DSD includes congenital discordance between chromosomal, gonadal, or phenotypic sex, even without overt genital ambiguity.',
    correctAnswer: true,
    explanation: 'The definition includes discordance without visible ambiguity.',
    reference: 'DSD includes discordance among chromosomal, gonadal, or phenotypic sex and can include cases without ambiguity.'
  },
  {
    id: 'pe-cr-009-tf2',
    subtopic: 'Genetics',
    statement: 'Mosaicism arises from post-zygotic mitotic errors, whereas chimerism reflects two genetic origins.',
    correctAnswer: true,
    explanation: 'Mosaicism and chimerism differ in their origin.',
    reference: 'Mosaicism comes from one zygote with mitotic nondisjunction, while chimerism reflects two genetic origins.'
  },
  {
    id: 'pe-cr-009-tf3',
    subtopic: 'Embryology',
    statement: 'Sex determination establishes gonadal fate, while sex differentiation shapes internal and external genitalia.',
    correctAnswer: true,
    explanation: 'These are distinct developmental steps.',
    reference: 'Sex determination sets gonadal fate, and differentiation shapes internal and external genitalia.'
  },
  {
    id: 'pe-cr-009-tf4',
    subtopic: 'Genetics',
    statement: 'Duplication of DAX1 can lead to gonadal dysgenesis.',
    correctAnswer: true,
    explanation: 'DAX1 is dose sensitive and duplication is pathogenic.',
    reference: 'Duplication of DAX1 results in gonadal dysgenesis.'
  },
  {
    id: 'pe-cr-009-tf5',
    subtopic: 'Assessment',
    statement: 'The EMS score is used to grade undervirilization in 46,XY DSD, with a normal male score of 12.',
    correctAnswer: true,
    explanation: 'EMS is designed for 46,XY undervirilization.',
    reference: 'EMS is used for 46,XY DSD and a normal male score is 12.'
  },
  {
    id: 'pe-cr-009-tf6',
    subtopic: 'Embryology',
    statement: 'Androgen exposure after 12 weeks of gestation tends to cause isolated clitoromegaly rather than complete labial fusion.',
    correctAnswer: true,
    explanation: 'Timing determines the degree of virilization.',
    reference: 'Exposure after 12 weeks generally causes isolated clitoromegaly.'
  },
  {
    id: 'pe-cr-009-tf7',
    subtopic: 'Embryology',
    statement: 'A blind vaginal pouch in 46,XY DSD typically reflects impaired androgen action with intact AMH.',
    correctAnswer: true,
    explanation: 'AMH regression with deficient androgen action produces the blind pouch.',
    reference: 'Blind vaginal pouch occurs when AMH is preserved but testosterone action is impaired.'
  },
  {
    id: 'pe-cr-009-tf8',
    subtopic: 'Clinical features',
    statement: 'Micropenis in a term newborn is defined by stretched penile length below about 2.5 cm.',
    correctAnswer: true,
    explanation: 'This cutoff approximates -2.5 SD for term newborns.',
    reference: 'Micropenis is defined as stretched penile length below -2.5 SD, about 2.5 cm at term.'
  },
  {
    id: 'pe-cr-009-tf9',
    subtopic: 'Neonatal evaluation',
    statement: 'Palpable gonads in a newborn with ambiguous genitalia suggest the presence of testicular tissue.',
    correctAnswer: true,
    explanation: 'Palpable gonads usually represent testes or ovotestes.',
    reference: 'Palpable gonads suggest testes or ovotestes in newborns with ambiguous genitalia.'
  },
  {
    id: 'pe-cr-009-tf10',
    subtopic: '46,XX DSD',
    statement: 'P450 oxidoreductase deficiency is a CAH variant that can cause genital ambiguity in both 46,XX and 46,XY individuals.',
    correctAnswer: true,
    explanation: 'POR deficiency is the CAH variant affecting both sexes.',
    reference: 'P450 oxidoreductase deficiency can produce ambiguity in both 46,XX and 46,XY.'
  },
  {
    id: 'pe-cr-009-tf11',
    subtopic: 'Psychosexual',
    statement: 'Psychosexual development includes gender identity, gender role, and gender orientation.',
    correctAnswer: true,
    explanation: 'These three elements define behavioral sex.',
    reference: 'Psychosexual development comprises gender identity, gender role, and gender orientation.'
  },
  {
    id: 'pe-cr-009-tf12',
    subtopic: 'Surgery',
    statement: 'Gonadectomy is recommended early for high-risk gonads such as those in mixed gonadal dysgenesis.',
    correctAnswer: true,
    explanation: 'Tumor risk drives early removal in high-risk conditions.',
    reference: 'Gonadectomy is recommended at diagnosis for high-risk conditions such as mixed gonadal dysgenesis.'
  }
].map(tf => ({ ...tf, type: 'true_false' }));

const assertionReason = [
  {
    id: 'pe-cr-009-ar1',
    subtopic: 'Definition',
    assertion: 'Disorders of sex development include cases without overt genital ambiguity.',
    reason: 'DSD is defined by discordance among chromosomal, gonadal, or phenotypic sex.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'DSD is defined by discordance among chromosomal, gonadal, or phenotypic sex and can include cases without ambiguity.'
  },
  {
    id: 'pe-cr-009-ar2',
    subtopic: 'Genetics',
    assertion: 'Mosaicism involves multiple cell lines derived from a single zygote.',
    reason: 'Mitotic nondisjunction after fertilization creates additional cell lines.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Mosaicism arises from post-zygotic mitotic nondisjunction creating multiple cell lines.'
  },
  {
    id: 'pe-cr-009-ar3',
    subtopic: 'Embryology',
    assertion: 'External genital virilization requires conversion of testosterone to DHT.',
    reason: 'DHT has higher affinity for the androgen receptor than testosterone.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'External genital virilization depends on DHT because it has stronger androgen receptor affinity.'
  },
  {
    id: 'pe-cr-009-ar4',
    subtopic: 'Assessment',
    assertion: 'Prader staging is primarily used for virilization in 46,XX infants.',
    reason: 'It grades the extent of external genital virilization in 46,XX DSD.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the assertion.',
    reference: 'Prader staging grades virilization of external genitalia in 46,XX individuals.'
  },
  {
    id: 'pe-cr-009-ar5',
    subtopic: 'Embryology',
    assertion: 'A blind vaginal pouch can occur in 46,XY DSD.',
    reason: 'AMH regression can be intact while testosterone action is impaired.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the mechanism.',
    reference: 'Blind vaginal pouch occurs when AMH is intact but androgen action is defective.'
  },
  {
    id: 'pe-cr-009-ar6',
    subtopic: '46,XY DSD',
    assertion: '5alpha-reductase type 2 deficiency often presents with undervirilized genitalia.',
    reason: 'Conversion of testosterone to DHT is impaired.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the phenotype.',
    reference: '5alpha-reductase deficiency causes undervirilization due to impaired DHT formation.'
  },
  {
    id: 'pe-cr-009-ar7',
    subtopic: 'Evaluation',
    assertion: 'A T/DHT ratio above 10 after hCG supports 5alpha-reductase deficiency.',
    reason: 'DHT fails to rise appropriately when conversion is defective.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the ratio.',
    reference: 'T/DHT ratio greater than 10 after hCG indicates impaired testosterone to DHT conversion.'
  },
  {
    id: 'pe-cr-009-ar8',
    subtopic: '46,XX DSD',
    assertion: 'P450 oxidoreductase deficiency can cause genital ambiguity in both sexes.',
    reason: 'This defect disrupts multiple steroidogenic enzymes.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the breadth of effects.',
    reference: 'P450 oxidoreductase deficiency affects steroidogenic enzymes and can cause ambiguity in both sexes.'
  },
  {
    id: 'pe-cr-009-ar9',
    subtopic: 'Psychosexual',
    assertion: 'Gender dysphoria reflects distress due to mismatch between identity and assigned sex.',
    reason: 'The distress may occur with or without a DSD diagnosis.',
    correctOption: 1,
    explanation: 'Both statements are true, but the reason does not directly explain the assertion.',
    reference: 'Gender dysphoria is distress from mismatch between identity and assigned sex, and it can occur with or without DSD.'
  },
  {
    id: 'pe-cr-009-ar10',
    subtopic: 'Surgery',
    assertion: 'Hypospadias repair is usually recommended in infancy.',
    reason: 'Early surgery benefits psychosocial development and tissue pliability.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the recommendation.',
    reference: 'Hypospadias repair is ideally performed at 6 to 12 months to support psychosocial outcomes and tissue pliability.'
  },
  {
    id: 'pe-cr-009-ar11',
    subtopic: 'Surgery',
    assertion: 'Gonadectomy is recommended at diagnosis for 46,XY gonadal dysgenesis.',
    reason: 'These gonads carry a high risk for germ cell malignancy.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the recommendation.',
    reference: 'High malignancy risk in 46,XY gonadal dysgenesis supports gonadectomy at diagnosis.'
  },
  {
    id: 'pe-cr-009-ar12',
    subtopic: '46,XX DSD',
    assertion: 'XX male syndrome presents with small testes and infertility.',
    reason: 'SRY translocation drives male phenotype but germ cell failure leads to high FSH.',
    correctOption: 0,
    explanation: 'Both statements are true and the reason explains the findings.',
    reference: 'XX male syndrome results from SRY translocation with small testes, infertility, and elevated FSH.'
  }
].map(ar => ({ ...ar, type: 'assertion_reason' }));

const output = {
  id: 'pe-cr-009',
  book: 'clinical_rounds',
  chapterNo: '9',
  title: 'Disorders of Sex Development',
  section: 'Pediatric Endo',
  sourceFile: 'pediatric_endo/clinical_rounds/009_disorders_of_sex_development',
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
