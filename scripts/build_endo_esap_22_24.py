"""ESAP 2021 modules e21-22 (carcinoid crisis), e21-23 (acromegaly complications), e21-24 (dopamine agonists)."""
from __future__ import annotations

from build_endo_esap_modules import ar, mcq, note, ref, tf


def build_chapter_22() -> dict:
    p = "e21-22"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Carcinoid syndrome",
                "Why classic carcinoid syndrome requires hepatic metastases",
                "Midgut tumors must metastasize to liver or lung before secreted amines reach the central circulation in concentrations causing flushing, diarrhea, and carcinoid heart disease—gastric and bronchial variants bypass this via direct venous drainage.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Classic carcinoid syndrome does not develop until a tumor has metastasized to the liver and/or lung, and the hormonal products released by the tumor reach the central venous circulation in substantial concentrations.",
                ),
            ),
            note(
                f"{p}-n2",
                "Carcinoid crisis",
                "How carcinoid crisis presents and why it kills",
                "Crisis is a severe episode of flushing, hypotension, tachyarrhythmia, confusion, and respiratory distress that can progress to cardiovascular collapse—early recognition and treatment are essential.",
                ref(
                    "Main Conclusions",
                    "Carcinoid crisis is defined as a severe episode of flushing, hypotension, tachyarrhythmia, confusion, and respiratory distress.",
                ),
            ),
            note(
                f"{p}-n3",
                "Risk factors",
                "Precipitants of carcinoid crisis ranked by frequency",
                "Most to least common: carcinoid heart disease, anesthesia/surgery, interventional therapy, radionuclide therapy, examination, serotonergic drugs (e.g., clomipramine, amitriptyline), biopsy—crisis can also occur spontaneously.",
                ref(
                    "Main Conclusions",
                    "Risk factors for or precipitating events for carcinoid crisis include, most common to least common, the presence of carcinoid heart disease, anesthesia or surgery, interventional therapy, radionuclide therapy, examination, medication (eg, serotonin drugs such as clomipramine and amitriptyline), and biopsy.",
                ),
            ),
            note(
                f"{p}-n4",
                "Crisis treatment",
                "How to treat carcinoid crisis acutely",
                "Somatostatin analogues are cornerstone therapy; add histamine blockers when histamine secretion is possible, vasopressin or phenylephrine for hypotension, and selective α/β blockers for hypertension—not β-blockers alone in hypotensive crisis.",
                ref(
                    "Main Conclusions",
                    "The treatment for carcinoid crisis and syndrome includes somatostatin analogues, histamine-receptor blockers, vasopressin or phenylephrine for significant hypotension, and α-adrenergic and β-adrenergic receptor blockers for hypertension.",
                ),
            ),
            note(
                f"{p}-n5",
                "Gastric variant",
                "Gastric carcinoid variant: histamine-driven flushing",
                "Gastric carcinoids often lack aromatic L-amino acid decarboxylase and thus secrete less serotonin—diarrhea and cardiac lesions are unusual; histamine causes patchy, pruritic, serpiginous red flushes.",
                ref(
                    "Gastric Variant Syndrome",
                    "gastric carcinoids can produce large amounts of histamine, which has been shown to have primary role in the atypical flushing and pruritus associated with these tumors.",
                ),
            ),
            note(
                f"{p}-n6",
                "Bronchial variant",
                "Bronchial carcinoid syndrome features",
                "Bronchial tumors produce less serotonin than midgut lesions; prolonged severe flushing, disorientation, lacrimation, hypotension, diarrhea, and asthma can occur—~1–2% secrete ACTH causing Cushing syndrome.",
                ref(
                    "Bronchial Carcinoid Variant Syndrome",
                    "The symptoms of bronchial carcinoid syndrome may be atypical, with episodes of severe and prolonged flushing, lasting hours to days.",
                ),
            ),
            note(
                f"{p}-n7",
                "Tumor localization",
                "Why hindgut tumors are usually hormonally silent",
                "Up to 90% of carcinoid syndrome arises from metastatic midgut tumors; bronchial tumors cause syndrome in ~10%; nearly all hindgut tumors are hormonally silent.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "nearly all hindgut tumors are hormonally silent.",
                ),
            ),
            note(
                f"{p}-n8",
                "Diagnosis",
                "Why carcinoid syndrome diagnosis is clinical",
                "As many as 40 substances may be secreted; relative contributions to each syndrome component are unknown—diagnosis rests on symptoms and signs, not a single biomarker.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Thus, the diagnosis of carcinoid syndrome and crisis is clinical based on the symptoms and signs.",
                ),
            ),
            note(
                f"{p}-n9",
                "Prophylaxis",
                "Pitfall: unclear role of prophylactic somatostatin analogues",
                "Heterogeneous definitions of crisis and limited evidence leave the role of prophylactic octreotide before procedures debated—identify at-risk patients and ensure rapid treatment capability.",
                ref(
                    "Barriers to Optimal Practice",
                    "The role of prophylactic somatostatin analogues in the treatment of carcinoid crisis is unclear.",
                ),
            ),
            note(
                f"{p}-n10",
                "Case 2 crisis",
                "How to manage intra-procedural carcinoid crisis during liver ablation",
                "Octreotide bolus plus continuous infusion with antihistamine and vasopressin for hypotension—β-blockers worsen hypotension; antihistamine alone is insufficient.",
                ref(
                    "Case 2",
                    "This patient has classic signs of carcinoid crisis that is best managed with octreotide bolus and drip, vasopressin for hypotension, and antihistamine (Answer B)",
                ),
            ),
            note(
                f"{p}-n11",
                "Epidemiology",
                "Why more clinicians will encounter NETs",
                "Neuroendocrine tumor incidence is increasing; most carcinoids arise in the gastrointestinal tract with indolent course but potential liver and lung metastases.",
                ref(
                    "Significance of the Clinical Problem",
                    "The incidence of neuroendocrine tumors (commonly referred to carcinoid) is increasing, so many health care providers will encounter patients with neuroendocrine tumors.",
                ),
            ),
            note(
                f"{p}-n12",
                "Prevention",
                "How to avoid carcinoid crisis in high-risk patients",
                "The cornerstone is identifying at-risk patients (functioning tumors, carcinoid heart disease) and ensuring rapid, effective treatment is available before anesthesia, surgery, or radionuclide therapy.",
                ref(
                    "Significance of the Clinical Problem",
                    "The cornerstone of avoiding carcinoid crisis is identifying at-risk patients and ensuring rapid and effective treatment.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 2",
                "During cryoablation of liver NET metastases, a patient develops flushing, BP 70/30, and bronchospasm. Best management?",
                [
                    "β-adrenergic blockers",
                    "Octreotide bolus and infusion, antihistamine, and vasopressin",
                    "Antihistamine alone",
                    "Phentolamine",
                ],
                1,
                "Carcinoid crisis requires somatostatin analogue plus vasopressor support; β-blockers and phentolamine worsen hypotension.",
                ref(
                    "Case 2",
                    "octreotide bolus and drip, vasopressin for hypotension, and antihistamine (Answer B)",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Classic syndrome",
                "Classic midgut carcinoid syndrome most commonly includes:",
                [
                    "Isolated hypertension without flushing",
                    "Episodic flushing, diarrhea, and carcinoid heart disease",
                    "Hyperglycemia and Cushingoid features only",
                    "Pellagra as the sole manifestation",
                ],
                1,
                "Hallmarks are flushing, diarrhea, valvular heart disease, and less often bronchospasm.",
                ref(
                    "Main Conclusions",
                    "The clinical hallmarks of classic carcinoid syndrome include episodic flushing, diarrhea, cardiac valvular disease, and, less frequently, bronchospasm.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Gastric variant",
                "Gastric carcinoid syndrome flushes are typically:",
                [
                    "Diffuse cyanotic and painless",
                    "Patchy, serpiginous, intensely pruritic, and cherry red",
                    "Identical to midgut serotonin flushes",
                    "Absent because all gastric carcinoids are nonsecretory",
                ],
                1,
                "Histamine-mediated atypical flushes differ from classic midgut syndrome.",
                ref(
                    "Gastric Variant Syndrome",
                    "the flushes may be patchy, sharply demarcated, serpiginous, and cherry red; they are also intensely pruritic.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Localization",
                "Which tumor location most often causes classic carcinoid syndrome?",
                [
                    "Appendix (hindgut) without metastases",
                    "Metastatic midgut small bowel NET",
                    "Nonfunctioning pancreatic NET without liver spread",
                    "Adrenal pheochromocytoma",
                ],
                1,
                "Up to 90% of syndrome cases involve metastatic midgut primaries.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "In up to 90% of patients, the development of carcinoid syndrome is associated with metastatic tumors originating in the midgut.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Risk factors",
                "The most common risk factor for carcinoid crisis is:",
                [
                    "Incidental appendectomy",
                    "Carcinoid heart disease",
                    "Vitamin B12 deficiency",
                    "Primary hypothyroidism",
                ],
                1,
                "Carcinoid heart disease ranks first among listed precipitants.",
                ref(
                    "Main Conclusions",
                    "Risk factors for or precipitating events for carcinoid crisis include, most common to least common, the presence of carcinoid heart disease",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Medications",
                "Which medication class can precipitate carcinoid crisis?",
                [
                    "Serotonergic antidepressants (e.g., clomipramine)",
                    "ACE inhibitors",
                    "Statins",
                    "Thiazide diuretics",
                ],
                0,
                "Serotonin-active drugs are listed precipitants.",
                ref(
                    "Main Conclusions",
                    "medication (eg, serotonin drugs such as clomipramine and amitriptyline)",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Bronchial NET",
                "Bronchial carcinoids causing carcinoid syndrome most often have:",
                [
                    "Localized typical carcinoids without metastases",
                    "Liver metastases with functioning tumor",
                    "Isolated hindgut physiology",
                    "Exclusive ACTH secretion without flushing",
                ],
                1,
                "Syndrome is rare in localized bronchial tumors but present in >80% with liver metastases.",
                ref(
                    "Bronchial Carcinoid Variant Syndrome",
                    "it can be present in more than 80% of patients with liver metastases.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Crisis treatment",
                "In carcinoid crisis with hypotension, which agent should be avoided?",
                [
                    "Octreotide",
                    "Vasopressin",
                    "β-adrenergic blockers",
                    "Histamine-receptor blockers",
                ],
                2,
                "β-blockers worsen hypotension in crisis.",
                ref(
                    "Case 2",
                    "The patient has hypotension, and β-adrenergic blockers (Answer A) would make it worse.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Serotonin",
                "Why gastric carcinoids rarely cause diarrhea or carcinoid heart disease:",
                [
                    "They secrete only calcitonin",
                    "They are frequently deficient in aromatic L-amino acid decarboxylase",
                    "They always metastasize to bone first",
                    "They are uniformly benign and nonsecretory",
                ],
                1,
                "Failure to convert tryptophan to serotonin reduces classic syndrome features.",
                ref(
                    "Gastric Variant Syndrome",
                    "gastric carcinoids are usually unable to convert the dietary tryptophan into serotonin, because they are frequently deficient in the enzyme aromatic L-amino acid decarboxylase.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Presentation delay",
                "Early symptoms of carcinoid tumors often include:",
                [
                    "Isolated hypercalcemia",
                    "Nonspecific abdominal pain, diarrhea, and intermittent obstruction",
                    "Acute Cushing syndrome in all patients",
                    "Thyrotoxicosis from TSH secretion",
                ],
                1,
                "Vague GI symptoms delay diagnosis in many patients.",
                ref(
                    "Significance of the Clinical Problem",
                    "The early symptoms of carcinoid tumor are nonspecific and may include abdominal pain, diarrhea, intermittent intestinal obstruction",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Hypertension in crisis",
                "Hypertension during carcinoid crisis may be treated with:",
                [
                    "β-blockers as monotherapy regardless of BP",
                    "α-adrenergic and β-adrenergic receptor blockers",
                    "High-dose serotonin reuptake inhibitors",
                    "No treatment; hypertension is benign",
                ],
                1,
                "Main conclusions list α- and β-blockers for hypertension in crisis/syndrome.",
                ref(
                    "Main Conclusions",
                    "α-adrenergic and β-adrenergic receptor blockers for hypertension.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Extraintestinal NET",
                "Extraintestinal carcinoids can cause syndrome without metastatic disease because:",
                [
                    "They never secrete bioactive amines",
                    "Secreted substances gain direct access to central venous circulation",
                    "They only secrete inactive prohormones",
                    "The liver inactivates all their products completely",
                ],
                1,
                "Direct venous drainage bypasses first-pass hepatic metabolism.",
                ref(
                    "Main Conclusions",
                    "Extraintestinal carcinoids can cause the syndrome in the absence of metastatic disease, because the substances that they secrete gain direct access to the central venous circulation.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Pellagra",
                "Pellagra in carcinoid syndrome results from:",
                [
                    "Excess niacin supplementation",
                    "Excess tryptophan metabolism by the tumor",
                    "Somatostatin analogue deficiency",
                    "Primary adrenal insufficiency",
                ],
                1,
                "Tryptophan shunting to serotonin synthesis depletes niacin pathways.",
                ref(
                    "Significance of the Clinical Problem",
                    "The effects of these chemicals, collectively referred to as the carcinoid syndrome, are diverse and include cutaneous flushing, diarrhea, carcinoid heart disease, bronchoconstriction, hypotension, hypertension, and pellagra.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Diagnosis",
                "Carcinoid syndrome and crisis symptoms may be nonspecific, contributing to delayed diagnosis.",
                True,
                "Listed as a barrier to optimal practice.",
                ref(
                    "Barriers to Optimal Practice",
                    "Carcinoid syndrome and crisis symptoms may be nonspecific.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Hindgut",
                "Nearly all hindgut carcinoid tumors cause classic carcinoid syndrome.",
                False,
                "Hindgut tumors are usually hormonally silent.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "nearly all hindgut tumors are hormonally silent.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Crisis",
                "Carcinoid crisis can occur spontaneously without a procedural trigger.",
                True,
                "Spontaneous crisis is acknowledged in main conclusions.",
                ref(
                    "Main Conclusions",
                    "Carcinoid crisis can also occur spontaneously.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Bronchial ACTH",
                "Approximately 1–2% of bronchial carcinoids are associated with Cushing syndrome from ectopic ACTH.",
                True,
                "Both typical and atypical bronchial carcinoids may secrete ACTH.",
                ref(
                    "Bronchial Carcinoid Variant Syndrome",
                    "Approximately 1% to 2% of bronchial carcinoids (both typical and atypical) are associated with Cushing syndrome due to ectopic production of ACTH.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Blood transfusion",
                "Blood transfusion is appropriate first-line therapy for carcinoid crisis hypotension.",
                False,
                "Case 2 explicitly rejects transfusion—patient is not bleeding.",
                ref(
                    "Case 2",
                    "A blood transfusion (Answer D) is incorrect, as the patient is not having active bleeding.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "PRRT",
                "Peptide receptor radionuclide therapy is a listed precipitant of carcinoid crisis.",
                True,
                "Radionuclide therapy is among risk factors.",
                ref(
                    "Main Conclusions",
                    "radionuclide therapy",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Gastric serotonin",
                "Gastric carcinoids typically produce large amounts of serotonin causing classic diarrhea.",
                False,
                "ALAD deficiency limits serotonin production; histamine drives atypical flushing.",
                ref(
                    "Gastric Variant Syndrome",
                    "the diarrhea and cardiac lesions, which are common features of classic midgut carcinoid syndrome, are unusual in the gastric variant of the syndrome.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Clinical link",
                "Understanding the biochemical link between tumor and syndrome prevents misattributing isolated symptoms to non-neoplastic causes.",
                True,
                "Main conclusions emphasize avoiding isolated functional misdiagnosis.",
                ref(
                    "Main Conclusions",
                    "It is very important to understand the biochemical and pathophysiological link between the carcinoid tumor and the carcinoid syndrome, because the physician may be easily misled into thinking the patient has isolated functional problems rather than a syndrome caused by a tumor.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Midgut syndrome",
                "Assertion: Classic carcinoid syndrome usually requires liver metastases from midgut primaries.",
                "Reason: Hepatic first-pass metabolism otherwise degrades secreted amines before they reach systemic circulation.",
                0,
                "Both true—standard pathophysiology of midgut NET syndrome.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Classic carcinoid syndrome does not develop until a tumor has metastasized to the liver and/or lung",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Crisis management",
                "Assertion: Octreotide is central to carcinoid crisis management.",
                "Reason: β-adrenergic blockers alone are safe first-line therapy in hypotensive crisis.",
                1,
                "Assertion true; β-blockers alone are contraindicated in hypotension.",
                ref(
                    "Case 2",
                    "β-adrenergic blockers (Answer A) would make it worse.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Gastric flushing",
                "Assertion: Gastric carcinoid flushes are often histamine-mediated and pruritic.",
                "Reason: Gastric carcinoids convert abundant dietary tryptophan to serotonin causing classic flushes.",
                2,
                "Assertion true; reason false—ALAD deficiency limits serotonin.",
                ref(
                    "Gastric Variant Syndrome",
                    "gastric carcinoids can produce large amounts of histamine, which has been shown to have primary role in the atypical flushing and pruritus",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Heart disease",
                "Assertion: Carcinoid heart disease is the most common risk factor for crisis.",
                "Reason: Carcinoid heart disease is more common than anesthesia as a precipitant.",
                0,
                "Both true per ordered risk-factor list.",
                ref(
                    "Main Conclusions",
                    "most common to least common, the presence of carcinoid heart disease, anesthesia or surgery",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Antihistamine",
                "Assertion: Antihistamine alone is insufficient for carcinoid crisis with hypotension.",
                "Reason: Antihistamine only blocks histamine effects and does not treat hypotension.",
                0,
                "Both true per case 2 explanation.",
                ref(
                    "Case 2",
                    "An antihistamine (Answer C) would only block the effect of histamine and would not treat the hypotension.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Bronchial NET",
                "Assertion: Bronchial carcinoids can cause atypical prolonged flushing.",
                "Reason: Bronchial carcinoids produce more serotonin than midgut carcinoids.",
                2,
                "Assertion true; reason false—bronchial tumors produce less serotonin.",
                ref(
                    "Bronchial Carcinoid Variant Syndrome",
                    "Bronchial carcinoids produce less serotonin than do midgut carcinoids",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Biopsy",
                "Assertion: Tumor biopsy can precipitate carcinoid crisis.",
                "Reason: Biopsy is among listed precipitating events for crisis.",
                0,
                "Both true.",
                ref(
                    "Main Conclusions",
                    "biopsy. Carcinoid crisis can also occur spontaneously.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "NET incidence",
                "Assertion: Clinicians will increasingly encounter patients with neuroendocrine tumors.",
                "Reason: NET incidence is decreasing worldwide.",
                2,
                "Assertion true; incidence is increasing, not decreasing.",
                ref(
                    "Significance of the Clinical Problem",
                    "The incidence of neuroendocrine tumors (commonly referred to carcinoid) is increasing",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "22",
        "title": "Prevention and Management of Carcinoid Crisis",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Electron Kebebew, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_22_Prevention_and_Management_of_Carcinoid_Crisis.md",
        "items": items,
    }


def build_chapter_23() -> dict:
    p = "e21-23"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Remission rates",
                "Why acromegaly often requires multimodality therapy",
                "Microadenoma postoperative remission approaches 90% at expert centers, but macroadenomas—especially with cavernous invasion—remit <50%; combined surgery and somatostatin analogues achieve ~70% biochemical control overall.",
                ref(
                    "Significance of the Clinical Problem",
                    "combined use of surgery and somatostatin analogue therapy leads to overall biochemical remission rates of around 70%.",
                ),
            ),
            note(
                f"{p}-n2",
                "Mortality",
                "Why biochemical control of GH/IGF-1 matters for survival",
                "Acromegaly increases mortality, which can normalize when GH and IGF-1 are controlled—yet long-term morbidity from hypopituitarism, cardiometabolic disease, sleep apnea, arthropathy, fractures, and malignancy persists.",
                ref(
                    "Significance of the Clinical Problem",
                    "Acromegaly is associated with increased mortality, which can be normalized by control of GH and IGF-1 secretion.",
                ),
            ),
            note(
                f"{p}-n3",
                "Surveillance",
                "How to structure long-term acromegaly complication surveillance",
                "Personalize screening for hypopituitarism, blood pressure, lipids/glucose, sleep apnea, echocardiography, colonoscopy, bone densitometry, spinal and joint imaging, thyroid ultrasound, and quality of life—not all tests repeat at fixed intervals.",
                ref(
                    "Significance of the Clinical Problem",
                    "A structured surveillance program must be personalized and should consider: Hypopituitarism Blood pressure Vascular risk factors (lipid profile and glucose intolerance) Obstructive sleep apnea Echocardiography Colonoscopy",
                ),
            ),
            note(
                f"{p}-n4",
                "Exceptions",
                "Why arthropathy, sleep apnea, and quality of life may not improve with biochemical control",
                "GH/IGF-1 control reduces most complications, but soft-tissue changes and irreversible joint damage often persist—arthropathy correlates with presenting hormone levels.",
                ref(
                    "Significance of the Clinical Problem",
                    "Exceptions to this rule may be sleep apnea, arthropathy, and quality of life.",
                ),
            ),
            note(
                f"{p}-n5",
                "Diabetes improvement",
                "How acromegaly remission affects glucose metabolism",
                "GH antagonizes insulin action; with biochemical control, insulin resistance improves in almost all patients and diabetes resolves in many after successful surgery.",
                ref(
                    "Case 1",
                    "With the fall in GH levels, insulin resistance and glucose tolerance improve in almost all patients, with resolution of diabetes in a number of individuals",
                ),
            ),
            note(
                f"{p}-n6",
                "Pasireotide diabetes",
                "How to treat pasireotide-induced hyperglycemia",
                "Pasireotide suppresses insulin and incretin secretion—GLP-1 receptor agonists and DPP-4 inhibitors are most appropriate; sulfonylureas are less ideal.",
                ref(
                    "Case 2",
                    "GLP-1 receptor agonists (Answer C) and DPP-4 inhibitors appear to be the most appropriate treatment modality for pasireotide-induced diabetes.",
                ),
            ),
            note(
                f"{p}-n7",
                "Arthropathy phases",
                "Two phases of acromegalic arthropathy",
                "Early phase shows joint space widening from cartilage hypertrophy and ligamentous laxity with some reversibility; later instability leads to narrowing, osteophytes, and cartilage fissuring.",
                ref(
                    "Case 3",
                    "The initial phase is characterized by an increase in joint space (Answer A) resulting from hypertrophy of the cartilage and ligamentous laxity.",
                ),
            ),
            note(
                f"{p}-n8",
                "Colonoscopy",
                "When to screen for colonic neoplasia in acromegaly",
                "Screen at diagnosis and every 5 years until GH/IGF-1 controlled—do not wait until age 50; risk abrogates with biochemical control.",
                ref(
                    "Case 4",
                    "At diagnosis and then every 5 years until GH and IGF-1 levels are controlled",
                ),
            ),
            note(
                f"{p}-n9",
                "Treatment sequelae",
                "Complications of acromegaly therapies over time",
                "Surgery causes early complications; radiation causes hypopituitarism, second malignancies, and vascular disease years later; medical adverse effects add monitoring complexity.",
                ref(
                    "Significance of the Clinical Problem",
                    "Complications of surgery generally occur early, whereas those associated with radiation therapy (hypopituitarism, second malignancies, vascular disease) usually take a number of years to be realized.",
                ),
            ),
            note(
                f"{p}-n10",
                "Multidisciplinary care",
                "Why endocrinologists coordinate acromegaly comorbidity management",
                "After biochemical control, most complications are managed like general-population counterparts, but multidisciplinary care is frequently required.",
                ref(
                    "Significance of the Clinical Problem",
                    "Management of many of the complications requires multidisciplinary care, frequently coordinated by the endocrinologist.",
                ),
            ),
            note(
                f"{p}-n11",
                "Sleep apnea",
                "Pitfall: expecting sleep apnea to resolve after biochemical remission",
                "Most studies fail to show resolution of OSA after GH/IGF-1 control—soft-tissue changes often persist.",
                ref(
                    "Case 1",
                    "most studies fail to show resolution of sleep apnea with biochemical control of acromegaly.",
                ),
            ),
            note(
                f"{p}-n12",
                "Vertebral fractures",
                "Vertebral fracture risk after biochemical control",
                "Fracture incidence slows with control but remains greater than expected in the general population.",
                ref(
                    "Case 1",
                    "The incidence of vertebral fractures (Answer C) does appear to slow with biochemical control; however, the incidence remains greater than expected.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "After transsphenoidal remission of acromegaly, which complication is most likely to improve?",
                [
                    "Diabetes mellitus",
                    "Arthropathy",
                    "Vertebral fractures (to normal population risk)",
                    "Sleep apnea",
                ],
                0,
                "Diabetes improves with falling GH; arthropathy, fractures, and sleep apnea often persist or improve incompletely.",
                ref(
                    "Case 1",
                    "thus, Answer A is correct",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "Best medication class for pasireotide-induced diabetes?",
                [
                    "Sulfonylurea",
                    "Metformin alone as sole preferred class",
                    "GLP-1 receptor agonist",
                    "Insulin only—no other agents help",
                ],
                2,
                "GLP-1 RAs and DPP-4 inhibitors address pasireotide's incretin suppression.",
                ref(
                    "Case 2",
                    "GLP-1 receptor agonists (Answer C) and DPP-4 inhibitors appear to be the most appropriate treatment modality",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "Features of acromegalic arthropathy include:",
                [
                    "Joint space widening only",
                    "Joint space narrowing only",
                    "Hyperosteophytes only",
                    "All of: widening, narrowing, hyperosteophytes, and cartilage fissuring",
                ],
                3,
                "All listed features occur at different disease stages.",
                ref(
                    "Case 3",
                    "All of these are features of acromegal arthropathy at different stages of the process (Answer E).",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Colonoscopy",
                "Recommended colorectal screening in active acromegaly:",
                [
                    "No screening unless symptomatic",
                    "Begin at age 50 only",
                    "At diagnosis then every 5 years until GH/IGF-1 controlled",
                    "Annual colonoscopy lifelong regardless of control",
                ],
                2,
                "Polyps and cancers are present at presentation; interval depends on control and prior findings.",
                ref(
                    "Case 4",
                    "At diagnosis and then every 5 years until GH and IGF-1 levels are controlled",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Remission",
                "Postoperative remission rate for acromegaly microadenomas at specialist centers is approximately:",
                [
                    "30%",
                    "50%",
                    "90%",
                    "100%",
                ],
                2,
                "Microadenoma remission approaches 90%; macroadenomas fare much worse.",
                ref(
                    "Significance of the Clinical Problem",
                    "Postoperative remission rates for microadenomas in specialist centers approach 90%.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "SSA therapy",
                "Long-acting somatostatin analogues control GH/IGF-1 in what fraction of postoperative nonremitters?",
                [
                    "5–10%",
                    "30–40%",
                    "70–80%",
                    "95–100%",
                ],
                1,
                "SSAs control axis in 30–40% of surgical failures.",
                ref(
                    "Significance of the Clinical Problem",
                    "Long-acting somatostatin analogue therapy leads to control of both GH and IGF-in 30% to 40% of patients not in remission following surgery.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Arthropathy",
                "Acromegalic arthropathy progression correlates most closely with:",
                [
                    "Post-treatment IGF-1 only",
                    "GH and IGF-1 levels at presentation",
                    "Patient age at diagnosis only",
                    "Radiation dose only",
                ],
                1,
                "Arthropathy fails to reverse and correlates with presenting hormone levels.",
                ref(
                    "Case 1",
                    "premature degenerative arthropathy (Answer B), which correlates most closely to GH and IGF-1 levels at presentation.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Malignancy",
                "Regarding malignancy risk in acromegaly:",
                [
                    "No evidence for any increased colonic polyp prevalence",
                    "Increased colonic hyperplastic polyps and malignancies are suggested",
                    "Thyroid cancer risk is proven absent",
                    "Screening is never recommended",
                ],
                1,
                "Colonic and thyroid malignancies are most studied; increased polyp/cancer prevalence is suggested.",
                ref(
                    "Case 4",
                    "the data suggest there is an increased prevalence of both colonic hyperplastic polyps and malignancies.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "QoL",
                "Quality of life in treated acromegaly:",
                [
                    "Always normalizes with biochemical control",
                    "May remain impaired despite long-term biochemical stability",
                    "Is unrelated to disease activity",
                    "Improves only after radiation",
                ],
                1,
                "QoL is among outcomes with less impact from biochemical control.",
                ref(
                    "Significance of the Clinical Problem",
                    "Biochemical control has less impact, however, on impaired quality of life and arthropathy",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Incidence",
                "Approximate annual incidence of acromegaly is:",
                [
                    "3–4 cases per million",
                    "30–40 cases per million",
                    "300–400 cases per million",
                    "3–4 cases per 100,000",
                ],
                0,
                "Low incidence and nonspecific early features delay diagnosis.",
                ref(
                    "Significance of the Clinical Problem",
                    "low incidence (3 to 4 cases/10^6 per year)",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Persistent disease",
                "Approximately what fraction of acromegaly patients still need further therapy after surgery plus SSA?",
                [
                    "5%",
                    "15%",
                    "30%",
                    "60%",
                ],
                2,
                "~30% require additional therapy beyond surgery + SSA to reach optimal control.",
                ref(
                    "Significance of the Clinical Problem",
                    "Approximately 30% of patients still require further therapy to achieve optimal disease control.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Sleep apnea mechanism",
                "Sleep apnea often persists after biochemical control because:",
                [
                    "GH rises again covertly",
                    "Soft-tissue changes from acromegaly frequently remain",
                    "SSAs cause permanent airway obstruction",
                    "Patients develop central apnea only",
                ],
                1,
                "Persistent soft-tissue changes explain lack of OSA resolution.",
                ref(
                    "Case 1",
                    "the soft-tissue changes observed in patients with acromegaly frequently remain after achieving biochemical control.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Aggressive control",
                "Biochemical control of GH/IGF-1 should be pursued rapidly because:",
                [
                    "It eliminates all need for surveillance",
                    "It reduces severity or prevalence of most complications",
                    "It reverses all joint damage within 1 year",
                    "It replaces multidisciplinary follow-up",
                ],
                1,
                "Control reduces most complications; exceptions remain for arthropathy, OSA, QoL.",
                ref(
                    "Significance of the Clinical Problem",
                    "Control of GH and IGF-1 reduces the severity, or prevalence, of most complications observed, and therefore biochemical control should be pursued rapidly and aggressively.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Diabetes",
                "Resolution of diabetes occurs in some patients after biochemical control of acromegaly.",
                True,
                "Case 1 states diabetes resolves in a number of individuals.",
                ref(
                    "Case 1",
                    "with resolution of diabetes in a number of individuals",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Arthropathy",
                "Biochemical control reliably reverses established acromegalic arthropathy.",
                False,
                "Arthropathy progresses despite control and correlates with presenting levels.",
                ref(
                    "Case 1",
                    "Biochemical control of acromegaly fails to prevent progression of premature degenerative arthropathy",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Colonoscopy timing",
                "Colorectal screening in acromegaly should wait until age 50 as in the general population.",
                False,
                "Abnormalities are present at presentation—screen at diagnosis.",
                ref(
                    "Case 4",
                    "screening should not wait until age 50 years (Answer B), when screening is typically recommended for the general population.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Pasireotide",
                "Pasireotide inhibits incretin secretion contributing to hyperglycemia.",
                True,
                "Mechanism explained in case 2.",
                ref(
                    "Case 2",
                    "Pasireotide inhibits not only insulin secretion, but also gut hormones including the incretins.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Macroadenoma surgery",
                "Cavernous sinus invasion lowers postoperative remission rates below 50% even at expert centers.",
                True,
                "Significance section states this explicitly.",
                ref(
                    "Significance of the Clinical Problem",
                    "remission rates even in specialist centers are less than 50%.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Vertebral fractures",
                "Vertebral fracture incidence after biochemical control returns to general-population levels.",
                False,
                "Incidence slows but remains greater than expected.",
                ref(
                    "Case 1",
                    "the incidence remains greater than expected.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Radiation",
                "Radiation-related hypopituitarism and vascular complications typically manifest years after treatment.",
                True,
                "Late sequelae of radiation are emphasized.",
                ref(
                    "Significance of the Clinical Problem",
                    "those associated with radiation therapy (hypopituitarism, second malignancies, vascular disease) usually take a number of years to be realized.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Colonoscopy control",
                "Control of GH and IGF-1 significantly reduces future colonic polyp risk.",
                True,
                "Case 4 states risk is abrogated by biochemical control.",
                ref(
                    "Case 4",
                    "Risk also appears to be significantly abrogated by control of GH and IGF-1 secretion",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Diabetes",
                "Assertion: Diabetes mellitus is the complication most likely to improve after acromegaly remission.",
                "Reason: GH excess antagonizes insulin action and its reduction improves glucose tolerance.",
                0,
                "Both true and mechanistically linked.",
                ref(
                    "Case 1",
                    "The excess GH secretion that defines acromegaly antagonizes insulin action, leading to glucose intolerance and diabetes.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Sleep apnea",
                "Assertion: Sleep apnea often persists after biochemical control of acromegaly.",
                "Reason: Most studies show complete resolution of OSA once IGF-1 normalizes.",
                2,
                "Assertion true; reason false—resolution is not shown in most studies.",
                ref(
                    "Case 1",
                    "most studies fail to show resolution of sleep apnea with biochemical control of acromegaly.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Pasireotide",
                "Assertion: GLP-1 receptor agonists are preferred for pasireotide-induced diabetes.",
                "Reason: Pasireotide stimulates incretin secretion causing hyperglycemia.",
                2,
                "Assertion true; pasireotide inhibits, not stimulates, incretins.",
                ref(
                    "Case 2",
                    "Pasireotide inhibits not only insulin secretion, but also gut hormones including the incretins.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Arthropathy",
                "Assertion: Early acromegalic arthropathy may show joint space widening.",
                "Reason: Widening results from cartilage hypertrophy and ligamentous laxity.",
                0,
                "Both true—early reversible phase.",
                ref(
                    "Case 3",
                    "an increase in joint space (Answer A) resulting from hypertrophy of the cartilage and ligamentous laxity.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Multimodality",
                "Assertion: Many acromegaly patients require multimodality therapy over time.",
                "Reason: Overall postoperative remission rates are 42–65% with most tumors being macroadenomas.",
                0,
                "Both true—explains need for combined modalities.",
                ref(
                    "Significance of the Clinical Problem",
                    "overall remission rates postoperatively are in the range of 42% to 65%.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Colon cancer",
                "Assertion: Colonic screening should begin at acromegaly diagnosis.",
                "Reason: Colonic abnormalities are absent until age 50.",
                2,
                "Assertion true; abnormalities present at presentation—reason false.",
                ref(
                    "Case 4",
                    "These abnormalities are present at presentation",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Surveillance",
                "Assertion: Surveillance regimens in acromegaly should be individualized.",
                "Reason: All patients require identical annual testing regardless of remission status.",
                2,
                "Assertion true; testing is personalized—not uniform annual repetition.",
                ref(
                    "Significance of the Clinical Problem",
                    "Individualization of screening is essential",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Mortality",
                "Assertion: Increased acromegaly mortality can normalize with GH/IGF-1 control.",
                "Reason: Mortality remains elevated regardless of any treatment.",
                2,
                "Assertion true per source; reason contradicts the text.",
                ref(
                    "Significance of the Clinical Problem",
                    "increased mortality, which can be normalized by control of GH and IGF-1 secretion.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "23",
        "title": "Management of Complications of Acromegaly",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Robert D. Murray, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_23_Management_complications.md",
        "items": items,
    }


def build_chapter_24() -> dict:
    p = "e21-24"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Efficacy",
                "Why cabergoline is preferred over bromocriptine for prolactinomas",
                "Cabergoline normalizes prolactin and shrinks tumors in >90% of patients with better tolerability than bromocriptine (80–90% normalization, ~50% >50% shrinkage).",
                ref(
                    "Significance of the Clinical Problem",
                    "Cabergoline, in use since the mid-1990s, can achieve these goals in more than 90% of patients.",
                ),
            ),
            note(
                f"{p}-n2",
                "Impulse control",
                "How dopamine agonists cause impulse control disorders",
                "Interaction with mesolimbic D3 receptors drives gambling, hypersexuality, compulsive eating/shopping, and punding—seen in 15–20% of treated patients, somewhat dose dependent.",
                ref(
                    "Case 1",
                    "Several studies have shown that both cabergoline and bromocriptine can cause compulsive behavior in 15% to 20% of treated patients.",
                ),
            ),
            note(
                f"{p}-n3",
                "CSF leak",
                "CSF rhinorrhea after macroadenoma shrinkage on dopamine agonists",
                "Large skull-base invasive macroadenomas can develop CSF fistula as tumor shrinks—diagnose with β2-transferrin in nasal fluid and repair to prevent meningitis.",
                ref(
                    "Main Conclusions",
                    "shrinkage of a large skull-based macroadenoma that invades the sellar floor can result in the leakage of cerebrospinal fluid around the now smaller tumor.",
                ),
            ),
            note(
                f"{p}-n4",
                "High-dose cabergoline",
                "Cardiac valve risk with high-dose cabergoline",
                "15–20% of prolactinoma patients need >standard dosing; Parkinson doses (3–5 mg daily) associate with valve disease via 5-HT2B receptors—echocardiography when crossing >2 mg/week is recommended.",
                ref(
                    "Main Conclusions",
                    "About 15% to 20% of patients require larger than standard dosages of cabergoline to normalize prolactin levels, and large dosages may cause cardiac valve abnormalities.",
                ),
            ),
            note(
                f"{p}-n5",
                "Pregnancy",
                "How to manage dopamine agonists in pregnancy",
                "Both drugs appear safe for the fetus, but stop cabergoline when pregnancy is confirmed—microadenoma enlargement risk ~2% (symptoms only) vs macroadenoma ~18% (visual fields each trimester).",
                ref(
                    "Significance of the Clinical Problem",
                    "visual field testing each trimester in addition to symptomatic monitoring is necessary for those with macroadenomas, as their risk for tumor enlargement is 18%.",
                ),
            ),
            note(
                f"{p}-n6",
                "Resistant prolactinoma",
                "How to manage cabergoline-resistant prolactinoma",
                "Increase cabergoline stepwise documenting prolactin response—~50% of bromocriptine failures respond to cabergoline; surgery or radiosurgery are alternatives.",
                ref(
                    "Case 2",
                    "most patients who have some response to cabergoline will have a further response if the dosage is increased.",
                ),
            ),
            note(
                f"{p}-n7",
                "Gonadotroph adenomas",
                "Silent gonadotroph adenomas among \"nonfunctioning\" tumors",
                "40–75% of clinically nonfunctioning adenomas are gonadotroph adenomas secreting subunits or intact gonadotropins without clinical syndrome.",
                ref(
                    "Case 5",
                    "Between 40% and 75% of clinically nonfunctioning adenomas are actually gonadotroph adenomas",
                ),
            ),
            note(
                f"{p}-n8",
                "Hypersexuality",
                "Why a spouse may ask to reduce cabergoline dose",
                "Hypersexuality is more common in men (6.5% isolated in one prolactinoma cohort)—impulse control disorders may be hidden; ask patient and partner at follow-up.",
                ref(
                    "Case 1",
                    "Hypersexuality was more common in men, and compulsive eating was more common in women.",
                ),
            ),
            note(
                f"{p}-n9",
                "Valve monitoring",
                "Echocardiography threshold for hyperprolactinemic cabergoline patients",
                "No increased valve abnormalities vs controls when doses stay ≤2 mg/week in most studies—but perform echo when exceeding 2 mg/week then annually.",
                ref(
                    "Case 2",
                    "hyperprolactinemic patients receiving greater than 2 mg weekly of cabergoline have echocardiography performed when that dosage threshold is crossed with then annually thereafter.",
                ),
            ),
            note(
                f"{p}-n10",
                "Pregnancy stop",
                "Why cabergoline is stopped when pregnancy is confirmed",
                "Despite fetal safety data, standard practice is to discontinue dopamine agonists in pregnancy and monitor for symptomatic tumor growth.",
                ref(
                    "Case 3",
                    "Answer: C) Stop cabergoline",
                ),
            ),
            note(
                f"{p}-n11",
                "β2-transferrin",
                "How to confirm CSF rhinorrhea",
                "β2-transferrin measurement in nasal fluid confirms CSF fistula—leak must be surgically repaired.",
                ref(
                    "Main Conclusions",
                    "Cerebrospinal fluid rhinorrhea can be diagnosed by measuring β2-transferrin in the nasal fluid, and the leak must be repaired to prevent meningitis.",
                ),
            ),
            note(
                f"{p}-n12",
                "Silent lactotroph",
                "Pitfall: \"nonfunctioning\" macroadenoma with mild hyperprolactinemia",
                "Immunostaining may reveal silent lactotroph adenoma—this patient's tumor stained for prolactin and stabilized on long-term cabergoline despite minimal prolactin elevation preoperatively.",
                ref(
                    "Case 5",
                    "the patient's tumor stained positively not for gonadotropins but for prolactin, so he had a \"silent\" lactotroph adenoma.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A man's wife asks about reducing cabergoline after prolactin normalization and tumor shrinkage. She is most concerned about:",
                [
                    "Difficulty urinating",
                    "Hypersexuality",
                    "Sleep apnea",
                    "Restless legs",
                ],
                1,
                "Impulse control disorders including hypersexuality are recognized cabergoline adverse effects.",
                ref(
                    "Case 1",
                    "Answer: B) Hypersexuality",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A woman on cabergoline has prolactin 68 ng/mL (partial shrinkage, no menses). Best next step?",
                [
                    "Transsphenoidal debulking",
                    "Switch to bromocriptine",
                    "Increase cabergoline dosage",
                    "Stereotactic radiosurgery",
                ],
                2,
                "Stepwise cabergoline escalation is appropriate when partial response exists.",
                ref(
                    "Case 2",
                    "Answer: C) Increase the cabergoline dosage",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A woman 20 weeks pregnant on long-term cabergoline for macroprolactinoma. Best management?",
                [
                    "Switch to bromocriptine and continue throughout pregnancy",
                    "Continue cabergoline throughout pregnancy",
                    "Stop cabergoline now",
                    "Stop now but restart if symptomatic",
                ],
                2,
                "Stop dopamine agonist when pregnancy is confirmed; monitor macroadenoma with visual fields.",
                ref(
                    "Case 3",
                    "Answer: C) Stop cabergoline",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 5",
                "After incomplete resection of a \"nonfunctioning\" macroadenoma with minimal prolactin elevation, immunostaining is most likely positive for:",
                [
                    "α subunit",
                    "Prolactin",
                    "ACTH",
                    "Negative for all hormones",
                ],
                0,
                "Most clinically NFPA are gonadotroph adenomas staining for α subunit; this case was silent lactotroph.",
                ref(
                    "Case 5",
                    "Answer: A) Positive stain for a subunit",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Valve disease",
                "Cabergoline-associated valve disease is thought to involve:",
                [
                    "D2 receptor blockade in myocardium only",
                    "5-HT2B receptor activation causing mitogenic leaflet changes",
                    "Direct calcification of mitral annulus",
                    "IgG4-related disease",
                ],
                1,
                "Serotonin 5-HT2B pathway on valves resembles carcinoid-like plaque.",
                ref(
                    "Case 2",
                    "cabergoline has action at the serotonin (5-HT) 2B receptors, which are present in valves",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Pregnancy risk",
                "Risk of symptomatic prolactinoma enlargement during pregnancy is approximately:",
                [
                    "2% microadenoma, 18% macroadenoma",
                    "18% microadenoma, 2% macroadenoma",
                    "50% for all tumors",
                    "Negligible for all tumors",
                ],
                0,
                "Microadenomas need symptomatic monitoring; macroadenomas need trimester visual fields.",
                ref(
                    "Significance of the Clinical Problem",
                    "their risk for tumor enlargement is only about 2%, visual field testing each trimester in addition to symptomatic monitoring is necessary for those with macroadenomas, as their risk for tumor enlargement is 18%.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Resistance",
                "Approximately what fraction of prolactinoma patients require more than standard cabergoline dosing?",
                [
                    "1–2%",
                    "15–20%",
                    "50%",
                    "80%",
                ],
                1,
                "15–20% are resistant to conventional ≤2 mg/week dosing.",
                ref(
                    "Main Conclusions",
                    "About 15% to 20% of patients require larger than standard dosages of cabergoline to normalize prolactin levels",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Bromocriptine switch",
                "In bromocriptine nonresponders, approximately what fraction respond to cabergoline?",
                [
                    "10%",
                    "50%",
                    "90%",
                    "100%",
                ],
                1,
                "About half of bromocriptine failures respond to cabergoline.",
                ref(
                    "Case 2",
                    "about 50% of patients who do not respond to bromocriptine do respond to cabergoline.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "CSF leak",
                "CSF rhinorrhea after DA-induced tumor shrinkage is confirmed by:",
                [
                    "Serum prolactin measurement",
                    "β2-transferrin in nasal fluid",
                    "24-hour urine cortisol",
                    "IGF-1 level",
                ],
                1,
                "β2-transferrin is diagnostic for CSF fistula.",
                ref(
                    "Main Conclusions",
                    "Cerebrospinal fluid rhinorrhea can be diagnosed by measuring β2-transferrin in the nasal fluid",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Impulse disorders prevalence",
                "In a Turkish prolactinoma cohort, overall impulse control disorder prevalence was:",
                [
                    "2%",
                    "7%",
                    "17%",
                    "50%",
                ],
                2,
                "17% had ICDs including hypersexuality, gambling, eating, shopping.",
                ref(
                    "Case 1",
                    "17% were found to have impulse control disorders",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Valve regression",
                "If valve abnormalities develop on high-dose cabergoline in Parkinson disease:",
                [
                    "All progress despite stopping drug",
                    "About one-third regress if drug stopped",
                    "Valves always normalize within 1 week",
                    "Bromocriptine worsens valve disease equally",
                ],
                1,
                "Limited data: one-third regress, half stable off drug; bromocriptine lacks this association.",
                ref(
                    "Case 2",
                    "if valve abnormalities develop, one-third have regression and half have lack of further progression of valve disease if the drug is stopped.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Fetal safety",
                "Regarding dopamine agonists in pregnancy:",
                [
                    "Both increase major fetal malformation rates significantly",
                    "Neither has been shown to increase fetal malformation risk",
                    "Only bromocriptine is safe; cabergoline is contraindicated",
                    "Both must be continued through delivery",
                ],
                1,
                "Main conclusions state neither increases malformation risk.",
                ref(
                    "Main Conclusions",
                    "Neither drug has been shown to increase the risk of fetal malformations.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Nausea",
                "Common dopamine agonist nausea is best managed by:",
                [
                    "Immediate maximum dose cabergoline",
                    "Low starting dose with gradual escalation over weeks to months",
                    "Permanent drug discontinuation at first nausea",
                    "Adding a β-blocker only",
                ],
                1,
                "Gradual titration while monitoring prolactin is standard.",
                ref(
                    "Significance of the Clinical Problem",
                    "The common adverse effect of nausea can be lessened by starting with low dosages and gradually increasing over weeks to months, monitoring the prolactin response.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Efficacy",
                "Cabergoline achieves prolactin normalization in more than 90% of prolactinoma patients.",
                True,
                "Stated in significance section.",
                ref(
                    "Significance of the Clinical Problem",
                    "Cabergoline, in use since the mid-1990s, can achieve these goals in more than 90% of patients.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Valves at standard dose",
                "Most echocardiographic studies show increased valve disease in hyperprolactinemic patients on ≤2 mg/week cabergoline versus controls.",
                False,
                "Almost all studies show no increase at ≤2 mg/week.",
                ref(
                    "Case 2",
                    "Almost all echocardiographic studies have not shown an increase in valve abnormalities in hyperprolactinemic patients taking cabergoline compared with control patients when dosages are kept to a maximum of 2 mg weekly.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Hypersexuality",
                "Hypersexuality is more commonly reported in women than men on dopamine agonists.",
                False,
                "Hypersexuality more common in men in cited study.",
                ref(
                    "Case 1",
                    "Hypersexuality was more common in men",
                ),
            ),
            tf(
                f"{p}-tf4",
                "CSF leak",
                "Untreated CSF rhinorrhea after prolactinoma shrinkage risks meningitis.",
                True,
                "Leak must be repaired to prevent meningitis.",
                ref(
                    "Main Conclusions",
                    "the leak must be repaired to prevent meningitis.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Pregnancy DA",
                "Bromocriptine and cabergoline are considered safe for the developing fetus.",
                True,
                "Significance section affirms fetal safety.",
                ref(
                    "Significance of the Clinical Problem",
                    "Both bromocriptine and cabergoline are safe for the developing fetus when given to women who wish to become pregnant.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Macroadenoma pregnancy",
                "Pregnant women with macroprolactinomas require visual field testing each trimester.",
                True,
                "18% enlargement risk mandates formal perimetry.",
                ref(
                    "Significance of the Clinical Problem",
                    "visual field testing each trimester in addition to symptomatic monitoring is necessary for those with macroadenomas",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Negative immunostain",
                "A completely hormone-negative pituitary adenoma immunostain is the most common result in clinically nonfunctioning tumors.",
                False,
                "Negative stain for all hormones is uncommon; gonadotroph adenomas predominate.",
                ref(
                    "Case 5",
                    "A negative stain for all pituitary hormones (Answer D) is uncommon.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Gambling",
                "Impulse control disorders may be hidden from family and require direct questioning.",
                True,
                "Clinicians should warn patients and ask spouses at visits.",
                ref(
                    "Case 1",
                    "It is important to also ask the spouse, as some impulse control disorders, such as gambling and compulsive shopping, may be hidden from the family.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Cabergoline valves",
                "Assertion: High-dose cabergoline may cause cardiac valve abnormalities.",
                "Reason: Cabergoline activates 5-HT2B receptors on valves triggering mitogenic changes.",
                0,
                "Both true—Parkinson data inform prolactinoma high-dose risk.",
                ref(
                    "Case 2",
                    "cabergoline has action at the serotonin (5-HT) 2B receptors, which are present in valves",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Pregnancy",
                "Assertion: Cabergoline should be stopped when pregnancy is confirmed.",
                "Reason: Cabergoline is proven teratogenic and must be switched to bromocriptine.",
                2,
                "Assertion true per case 3; fetal malformation risk not shown—reason false.",
                ref(
                    "Main Conclusions",
                    "Neither drug has been shown to increase the risk of fetal malformations.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Dose escalation",
                "Assertion: Increasing cabergoline may normalize prolactin in partial responders.",
                "Reason: Patients with no response to cabergoline never benefit from higher doses.",
                2,
                "Assertion true for partial responders; reason false.",
                ref(
                    "Case 2",
                    "most patients who have some response to cabergoline will have a further response if the dosage is increased.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "CSF leak",
                "Assertion: Dopamine agonist-induced tumor shrinkage can cause CSF rhinorrhea.",
                "Reason: Shrinkage of invasive macroadenomas can leave a CSF leak around the smaller tumor.",
                0,
                "Both true per main conclusions.",
                ref(
                    "Main Conclusions",
                    "shrinkage of a large skull-based macroadenoma that invades the sellar floor can result in the leakage of cerebrospinal fluid",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Impulse control",
                "Assertion: Dopamine agonists can cause pathologic gambling and hypersexuality.",
                "Reason: These behaviors result from D3 receptor interaction in the mesolimbic system.",
                0,
                "Both true—mechanism and prevalence cited.",
                ref(
                    "Case 1",
                    "The mechanism of action behind impulse control disorders seems to be an interaction between the dopamine agonists and the D_{3} receptors in the mesolimbic system",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Gonadotroph adenoma",
                "Assertion: Most clinically nonfunctioning adenomas are gonadotroph adenomas.",
                "Reason: They always secrete clinically evident FSH excess causing OHSS.",
                2,
                "Assertion true; functioning OHSS is very rare—reason false.",
                ref(
                    "Case 5",
                    "Between 40% and 75% of clinically nonfunctioning adenomas are actually gonadotroph adenomas",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Echo monitoring",
                "Assertion: Echocardiography is recommended when cabergoline exceeds 2 mg weekly.",
                "Reason: All patients on any cabergoline dose have 34% tricuspid regurgitation.",
                2,
                "Assertion true per guidelines; 34% is Parkinson high-dose data—not all prolactinoma doses.",
                ref(
                    "Case 2",
                    "hyperprolactinemic patients receiving greater than 2 mg weekly of cabergoline have echocardiography performed when that dosage threshold is crossed",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Bromocriptine",
                "Assertion: Bromocriptine is associated with cardiac valve abnormalities like high-dose cabergoline.",
                "Reason: Valve abnormalities are not seen with bromocriptine.",
                2,
                "Assertion false; reason true.",
                ref(
                    "Case 2",
                    "Valve abnormalities are not seen with bromocriptine.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "24",
        "title": "Dopamine Agonists: Risks, Adverse Effects, Surveillance, and Intervention",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Mark E. Molitch, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_24_Risks_Adverse_Effects_Surveillance_and_Intervention.md",
        "items": items,
    }
