"""ESAP 2021 modules e21-16 (Paget disease) and e21-21 (pseudoacromegaly)."""
from __future__ import annotations

from build_endo_esap_modules import ar, mcq, note, ref, tf


def build_chapter_16() -> dict:
    p = "e21-16"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Epidemiology",
                "Why Paget disease of bone remains clinically important",
                "PDB is the second most common metabolic bone disease after osteoporosis, typically identified by elevated alkaline phosphatase or incidental radiographs. Most patients are asymptomatic, but bone pain and local complications drive therapy decisions.",
                ref(
                    "Main Conclusions",
                    "PDB is the second most common metabolic bone disease after osteoporosis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Therapy",
                "How bisphosphonates help painful Paget disease",
                "Bisphosphonates—especially intravenous zoledronic acid—are more than three times more likely than placebo to eliminate bone pain, with a number needed to treat of only 5; patients with shorter symptom duration respond better.",
                ref(
                    "Therapeutic Management",
                    "bisphosphonate treatment is more than 3 times more likely than placebo to eliminate bone pain in PDB (31% vs 9% [relative risk (RR) = 3.42; 95% confidence interval (CI), 1.31-8.90])",
                ),
            ),
            note(
                f"{p}-n3",
                "Asymptomatic PDB",
                "Why expectant management is advised for asymptomatic Paget disease",
                "There is insufficient evidence that bisphosphonates or other interventions prevent deformity, fractures, orthopedic surgery, or hearing loss in asymptomatic patients—treat pain, not isolated biochemical elevation.",
                ref(
                    "Main Conclusions",
                    "there is insufficient evidence of other disease benefit (ie, prevention of deformity, fractures, orthopedic surgery, hearing loss) with bisphosphonates or other pharmacologic/nonpharmacologic interventions, such that expectant management and treatment of patients with PDB who have been pain is currently advised.",
                ),
            ),
            note(
                f"{p}-n4",
                "Diagnosis",
                "How to stage imaging after biochemical suspicion of PDB",
                "Plain radiographs of symptomatic or high-yield sites are reasonable first steps; whole-body technetium-99m bone scintigraphy is more sensitive than plain films and is recommended to define the extent of metabolically active disease.",
                ref(
                    "Diagnosis",
                    "whole-body bone scintigraphy is recommended as well, in addition to targeted radiographs, as a means to fully and accurately define the extent of metabolically active disease in patients with PDB.",
                ),
            ),
            note(
                f"{p}-n5",
                "Biochemical relapse",
                "Pitfall: biochemical relapse does not equal clinical relapse",
                "After zoledronic acid, alkaline phosphatase may rise without return of pain—PRISM trials showed intensive treat-to-target normalization did not reduce pain, fractures, or orthopedic procedures and may increase fracture risk in older, long-standing disease.",
                ref(
                    "Barriers to Optimal Practice",
                    "Biochemical relapse (ie, increase in alkaline phosphatase above the normal range) does not necessarily predict clinical relapse (ie, recurrence of bone pain), thereby presenting a challenge in the long-term management of patients with PDB.",
                ),
            ),
            note(
                f"{p}-n6",
                "Drug choice",
                "Zoledronic acid versus oral risedronate in painful PDB",
                "Head-to-head data favor IV zoledronic acid 5 mg over oral risedronate for pain relief and lower clinical relapse rates; calcitonin is second-line when bisphosphonates are contraindicated; denosumab is not recommended.",
                ref(
                    "Therapeutic Management",
                    "zoledronic acid, 5 mg intravenously, is superior to risedronate, 30 mg orally for 2 months, in relieving bone pain (RR, 1.36; 95% CI, 1.06-1.74).",
                ),
            ),
            note(
                f"{p}-n7",
                "Underrecognition",
                "Why bone-specific alkaline phosphatase helps when total ALP is borderline",
                "Total alkaline phosphatase reflects hepatic and skeletal fractions; patients with PDB may have normal totals when hepatic contribution is low or skeletal involvement is limited—bone-specific ALP, P1NP, or CTX can confirm elevated turnover.",
                ref(
                    "Barriers to Optimal Practice",
                    "PDB may be underrecognized in patients with an alkaline phosphatase level within but at the upper limit of the normal range, in which case measurement of bone-specific alkaline phosphatase and/or other bone biomarkers (P1NP, C-telopeptide) may be helpful.",
                ),
            ),
            note(
                f"{p}-n8",
                "Skull involvement",
                "How to manage asymptomatic calvarial Paget disease",
                "Hearing impairment is significantly more common than in the general population even without subjective symptoms—audiometry is indicated; bisphosphonates have not been shown to slow or reverse hearing loss.",
                ref(
                    "Case 3",
                    "the incidence of hearing impairment in patients with PDB is significantly higher than in the general population.",
                ),
            ),
            note(
                f"{p}-n9",
                "Pathogenesis",
                "Paget disease pathobiology: lytic then sclerotic remodeling",
                "Initial osteoclastic lytic lesions recruit accelerated osteoblastic woven bone formation, yielding hypervascular, structurally inferior bone that may later \"burn out\" into sclerotic inactive lesions.",
                ref(
                    "Prevalence and Pathogenesis",
                    "The result of this process is an enlarged, hypervascular and structurally inferior skeletal site.",
                ),
            ),
            note(
                f"{p}-n10",
                "Genetics",
                "SQSTM1 variants and familial Paget disease",
                "Up to 30% of patients have a positive family history; SQSTM1 pathogenic variants account for ~21% in some cohorts and associate with earlier, more severe disease including spinal stenosis.",
                ref(
                    "Prevalence and Pathogenesis",
                    "Within the United States, studies suggest that a first-degree relative of a patient with PDB is 7 times more likely to develop the disease than someone with an unaffected relative.",
                ),
            ),
            note(
                f"{p}-n11",
                "Case 1 management",
                "How to extend staging in incidentally discovered pelvic Paget disease",
                "Asymptomatic patients with focal pelvic disease may have multifocal involvement including spine—whole-body bone scan is indicated before reassurance or therapy; bisphosphonates should not start without defining disease extent.",
                ref(
                    "Case 1",
                    "whole-body bone scanning with technetium $^{99}$Tc (Answer C) is indicated.",
                ),
            ),
            note(
                f"{p}-n12",
                "Follow-up",
                "Surveillance after successful zoledronic acid in monostotic PDB",
                "Rising alkaline phosphatase without pain warrants clinical and biochemical surveillance every 6–12 months—not automatic retreatment or repeat scintigraphy when the diagnosis and monostotic site are already established.",
                ref(
                    "Case 5",
                    "continued clinical and biochemical surveillance (Answer C) is indicated for this patient.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A 64-year-old man has pelvic CT showing iliac and pubic thickening, ALP 114 U/L (24–110), no pain, and normal hip exam. What is the best next step?",
                [
                    "Zoledronic acid 5 mg IV",
                    "Alendronate 40 mg daily for 6 months",
                    "Technetium-99m whole-body bone scintigraphy",
                    "Fasting serum C-telopeptide",
                ],
                2,
                "Asymptomatic PDB with possible multifocal disease requires bone scintigraphy to define extent before treatment or reassurance.",
                ref(
                    "Case 1",
                    "whole-body bone scanning with technetium $^{99}$Tc (Answer C) is indicated.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A 52-year-old man has active symptomatic pelvic PDB on radiograph and bone scan with ALP 114 U/L and bone-specific ALP 33 µg/L. What is the best treatment?",
                [
                    "Zoledronic acid 5 mg IV",
                    "Risedronate 30 mg daily for 2 months",
                    "Calcitonin 100 units SC three times weekly",
                    "Denosumab 60 mg SC every 6 months",
                ],
                0,
                "Symptomatic active PDB with recent pain is best treated with IV zoledronic acid, superior to oral risedronate in trials.",
                ref(
                    "Case 2",
                    "Zoledronic acid intravenously (Answer A) is superior to oral risedronate (Answer B) based on a head-to-head comparison and is the best treatment for this patient.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A 60-year-old woman has skull Paget on bone scan with mild calvarial thickening, no headaches, and denies hearing loss. Best next step?",
                [
                    "Zoledronic acid 5 mg IV",
                    "Alendronate 40 mg daily for 6 months",
                    "Audiometry testing",
                    "CT of the skull",
                ],
                2,
                "Subclinical hearing loss is common in skull PDB; audiometry guides assistive technology—bisphosphonates do not reverse hearing loss.",
                ref(
                    "Case 3",
                    "audiometry testing (Answer C) is indicated to determine whether hearing loss is present",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Therapy",
                "Which statement about bisphosphonate therapy in asymptomatic Paget disease is most accurate?",
                [
                    "IV zoledronic acid prevents hearing loss in all skull lesions",
                    "Intensive treat-to-target ALP normalization reduces fracture risk in all ages",
                    "Robust RCT evidence supports bisphosphonates only for reducing skeletal pain",
                    "Denosumab is first-line when bisphosphonates fail",
                ],
                2,
                "Cochrane data robustly support pain reduction; other outcomes lack evidence; denosumab is not recommended.",
                ref(
                    "Therapeutic Management",
                    "existing evidence for bisphosphonate use is robust only for reduction in skeletal pain.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "PRISM trials",
                "The PRISM and PRISM-EZ trials demonstrated that intensive bisphosphonate treatment in PDB:",
                [
                    "Reduced bone pain more than symptom-driven therapy over ~3 years",
                    "Did not reduce bone pain, fractures, or orthopedic surgery vs symptomatic treatment",
                    "Normalized ALP and eliminated all long-term fracture risk",
                    "Should be standard for all patients under age 50",
                ],
                1,
                "Intensive therapy did not improve pain, fractures, or surgery needs; long-term ALP normalization did not improve quality of life and may raise fracture risk in older cohorts.",
                ref(
                    "Therapeutic Management",
                    "intensive bisphosphonate treatment did not reduce bone pain, fractures, or need for orthopedic surgery compared with symptom-driven treatment in patients with PDB over an average of 3 years.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Diagnosis",
                "When plain radiographs are negative but PDB is suspected biochemically, the recommended next imaging step is:",
                [
                    "MRI of the pelvis only",
                    "Whole-body bone scintigraphy",
                    "PET-CT of the spine",
                    "No further imaging; repeat ALP in 6 months",
                ],
                1,
                "Scintigraphy is more sensitive than plain films for detecting metabolically active PDB.",
                ref(
                    "Diagnosis",
                    "In the absence of plain radiographic involvement, whole-body bone scintigraphy is recommended based on its superior sensitivity for detecting PDB compared with the sensitivity of plain x-rays",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Biomarkers",
                "In a patient with established painful PDB on imaging, fasting C-telopeptide measurement is:",
                [
                    "Required before starting zoledronic acid",
                    "Superior to ALP for diagnosis",
                    "Of limited utility for diagnosis or therapeutic management",
                    "Mandatory to predict clinical relapse after zoledronic acid",
                ],
                2,
                "Turnover markers have limited utility once diagnosis and activity are established; they do not reliably predict clinical relapse after zoledronic acid.",
                ref(
                    "Case 2",
                    "measurement of bone turnover (Answer D) has limited utility in either the diagnosis or therapeutic management of this patient.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Complications",
                "Which complication of Paget disease is correctly paired with its mechanism?",
                [
                    "High-output heart failure from hypervascular pagetic bone (rare)",
                    "Premature mortality from osteosarcoma in most patients",
                    "Hearing loss only after skull deformity is visible",
                    "Fractures occur exclusively in burned-out sclerotic lesions",
                ],
                0,
                "Hypervascular pagetic bone can rarely cause high-output failure; osteosarcoma is <1% without excess mortality; hearing loss can be subclinical.",
                ref(
                    "Clinical Presentation",
                    "Hypervascularity of affected bone may exacerbate bleeding risk with orthopedic procedures that involve pagetic sites and has been associated, rarely, with high-output cardiac failure.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Epidemiology",
                "Paget disease of bone epidemiology is best described by which statement?",
                [
                    "Equal prevalence in Asian and European ancestry",
                    "More common in females than males",
                    "Prevalence roughly doubles each decade after age 50",
                    "Incidence is rising sharply worldwide",
                ],
                2,
                    "PDB affects ~1–3% of older adults, favors Anglo-Saxon/European heritage and males (~1.4:1), and prevalence appears to be declining.",
                ref(
                    "Prevalence and Pathogenesis",
                    "it roughly doubles in incidence for each decade after age 50 years.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Surgery",
                "A patient with painful PDB inadequately controlled medically requires hip replacement. Which is true?",
                [
                    "Bisphosphonates are proven to eliminate perioperative bleeding risk",
                    "Hip or knee arthroplasty is recommended when medical therapy is inadequate",
                    "Surgery is contraindicated in all polyostotic disease",
                    "Osteotomy is never considered for deformity",
                ],
                1,
                    "Insufficient evidence supports pharmacologic benefit on orthopedic outcomes, but arthroplasty is recommended when medical therapy fails; osteotomy may be considered for deformity.",
                ref(
                    "Therapeutic Management",
                    "hip or knee arthroplasty is recommended in patients in whom medical therapy is inadequate.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Case 5",
                "A woman with prior monostotic femoral PDB treated with zoledronic acid has normalized ALP historically but now ALP 140 U/L without pain. Best management?",
                [
                    "Repeat zoledronic acid 5 mg IV",
                    "Switch to alendronate 40 mg daily",
                    "Clinical and biochemical surveillance every 6–12 months",
                    "Repeat whole-body bone scintigraphy",
                ],
                2,
                "Biochemical relapse without pain does not mandate retreatment or repeat scintigraphy in known monostotic PDB.",
                ref(
                    "Case 5",
                    "continued clinical and biochemical surveillance (Answer C) is indicated for this patient.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Pathology",
                "The initial pagetic bone lesion is best characterized as:",
                [
                    "Purely sclerotic with low osteoclast activity",
                    "Lytic with increased osteoclast number and activity",
                    "Malignant osteoblastic proliferation",
                    "Avascular necrosis of trabecular bone",
                ],
                1,
                "The initial lesion is lytic from increased osteoclast activity, followed by accelerated osteoblastic woven bone formation.",
                ref(
                    "Prevalence and Pathogenesis",
                    "The initial lesion in PDB, which may be solitary (mono-ostotic) or multicentric (polyostotic), is lytic in nature and due to increased number and activity of osteoclasts.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Screening",
                    "In a patient without localizing symptoms but elevated ALP suggesting PDB, a reasonable limited radiographic survey includes:",
                [
                    "Skull, abdomen/pelvis, and tibia",
                    "Hands and feet only",
                    "Cervical spine only",
                    "No radiographs; proceed directly to biopsy",
                ],
                0,
                "Limited survey of skull/facial bones, abdomen (pelvis/proximal femurs), and tibia is recommended given high prevalence at these sites.",
                ref(
                    "Diagnosis",
                    "a limited x-ray survey of the skull and facial bones, abdomen (which includes the pelvis and proximal femurs), and tibia is recommended given the high prevalence of involvement of these sites.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Therapy",
                "Intravenous bisphosphonates confer a greater and more sustained analgesic effect than oral bisphosphonates in painful Paget disease.",
                True,
                "Main conclusions and RCT data support superior pain relief with IV therapy.",
                ref(
                    "Main Conclusions",
                    "Painful PDB is responsive to treatment with bisphosphonates, with a greater and more sustained effect conferred by intravenous than oral therapy.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Asymptomatic disease",
                "Bisphosphonate treatment is proven to prevent hearing loss in asymptomatic skull Paget disease.",
                False,
                "There is insufficient evidence that bisphosphonates prevent hearing loss.",
                ref(
                    "Case 3",
                    "There is no evidence to date that treatment with bisphosphonates (Answers A and B) slows or reverses hearing loss in patients with PDB.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Relapse",
                "Lack of biochemical relapse after zoledronic acid reliably identifies patients at risk of clinical relapse on risedronate but not zoledronic acid.",
                False,
                "For zoledronic acid, lack of biochemical relapse was not helpful in defining clinical relapse risk.",
                ref(
                    "Therapeutic Management",
                    "lack of biochemical relapse (increase in alkaline phosphatase level) was not helpful in defining which patients were at risk of clinical relapse when treated with zoledronic acid.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Malignancy",
                "Malignant transformation to osteosarcoma occurs in more than 10% of Paget patients.",
                False,
                "Osteosarcoma transformation is very rare (<1%).",
                ref(
                    "Clinical Presentation",
                    "Very rarely, malignant transformation to osteosarcoma (<1%) or giant-cell tumor development occurs.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Denosumab",
                "Denosumab is recommended for Paget disease when bisphosphonates fail.",
                False,
                "Denosumab is not recommended because of insufficient evidence.",
                ref(
                    "Therapeutic Management",
                    "denosumab is not recommended for PDB because of insufficient evidence.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Familial disease",
                "A first-degree relative of a PDB patient is about seven times more likely to develop PDB than someone with an unaffected relative.",
                True,
                "Familial clustering is well documented in US cohorts.",
                ref(
                    "Prevalence and Pathogenesis",
                    "a first-degree relative of a patient with PDB is 7 times more likely to develop the disease than someone with an unaffected relative.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Imaging",
                "Whole-body bone scintigraphy may be negative at sites of inactive Paget disease.",
                True,
                "Inactive burned-out lesions may not uptake tracer.",
                ref(
                    "Diagnosis",
                    "whole-body bone scintigraphy may be negative at sites of inactive PDB.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "PRISM-EZ",
                "Long-term intensive ALP normalization over more than 7 years improved quality of life in PRISM-EZ.",
                False,
                "Long-term normalization did not improve pain, quality of life, or orthopedic procedures and may increase fracture risk.",
                ref(
                    "Therapeutic Management",
                    "long-term normalization of alkaline phosphatase over more than 7 years did not improve bone pain, improve quality of life, or reduce the need for orthopedic procedures, and it may actually be associated with a higher fracture risk.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Painful PDB",
                "Assertion: A patient with recent-onset Paget bone pain is an appropriate candidate for bisphosphonate therapy.",
                "Reason: Bisphosphonates are proven to prevent all orthopedic and neurologic complications of Paget disease.",
                1,
                "Both true, but R is false—evidence supports pain relief, not proven prevention of other outcomes.",
                ref(
                    "Barriers to Optimal Practice",
                    "bisphosphonate treatment of patients with PDB has not been proven to reduce the risk for orthopedic and neurologic outcomes.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Asymptomatic PDB",
                "Assertion: An asymptomatic patient with biochemical and radiographic PDB should receive zoledronic acid immediately.",
                "Reason: Without treatment, multifocal spine disease will invariably cause neurologic complications.",
                4,
                "Neither is supported—expectant management is advised absent pain; neurologic benefit unproven.",
                ref(
                    "Case 1",
                    "there is not an indication to treat him with pharmacologic therapy, including bisphosphonates.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "ALP monitoring",
                "Assertion: Rising alkaline phosphatase after prior zoledronic acid always requires retreatment.",
                "Reason: Biochemical relapse does not necessarily predict clinical relapse.",
                2,
                "A is false when pain is absent; R is true.",
                ref(
                    "Barriers to Optimal Practice",
                    "Biochemical relapse (ie, increase in alkaline phosphatase above the normal range) does not necessarily predict clinical relapse (ie, recurrence of bone pain)",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Hearing",
                "Assertion: Audiometry is indicated in patients with skull Paget disease even without subjective hearing loss.",
                "Reason: Hearing impairment prevalence is significantly higher than in the general population.",
                0,
                "Both true and causally linked.",
                ref(
                    "Case 3",
                    "the incidence of hearing impairment in patients with PDB is significantly higher than in the general population.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Zoledronic vs risedronate",
                "Assertion: Zoledronic acid is superior to risedronate for pain relief in PDB.",
                "Reason: Patients treated with zoledronic acid are less likely to experience clinical relapse than those treated with risedronate.",
                0,
                "Both true; head-to-head trial supports superiority for pain and relapse.",
                ref(
                    "Therapeutic Management",
                    "Patients treated with zoledronic acid are also less likely than those treated with risedronate to experience clinical relapse (recurrence of bone pain) (9.2% vs 25.2%)",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Bone scan",
                "Assertion: Whole-body scintigraphy is indicated in a newly diagnosed asymptomatic patient with pelvic PDB on CT.",
                "Reason: Multifocal disease including spine may exist and influence management decisions.",
                0,
                "Both true—the case vignette links extent assessment to treatment candidacy.",
                ref(
                    "Case 1",
                    "he may have multifocal disease that includes the spine, which could position him as a candidate for treatment because of concerns regarding disease progression and possible neurologic complications.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Calcitonin",
                "Assertion: Calcitonin may improve bone pain when bisphosphonates are contraindicated.",
                "Reason: Calcitonin is superior to zoledronic acid in all PDB patients.",
                1,
                "Assertion has low-level support; reason is false.",
                ref(
                    "Therapeutic Management",
                    "Low level evidence indicates that calcitonin may improve bone pain in patients with PDB, although it may be considered when bisphosphonate use is contraindicated.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Total ALP",
                "Assertion: A normal total alkaline phosphatase excludes Paget disease.",
                "Reason: Low hepatic fraction or limited skeletal involvement can yield normal total ALP despite PDB.",
                2,
                "A is false; R correctly explains why.",
                ref(
                    "Diagnosis",
                    "a low hepatic fraction may result in a normal total alkaline phosphatase value.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "16",
        "title": "Modern Management of the Patient With Paget Disease of Bone",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Thomas J. Weber, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_16_Modern_Manager_Patient_With_Pac.md",
        "items": items,
    }


def build_chapter_21() -> dict:
    p = "e21-21"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Overview",
                "Why pseudoacromegaly must be considered in acromegaloid patients",
                "Several rare genetic and metabolic conditions mimic acromegaloid facies and acral enlargement without GH/IGF-1 excess; awareness prevents years of misdirected pituitary workup.",
                ref(
                    "Main Conclusions",
                    "Awareness of these rare conditions will help the differential diagnosis in patients with acromegaloid features but no GH excess.",
                ),
            ),
            note(
                f"{p}-n2",
                "Diagnostic approach",
                "How to approach the differential diagnosis of pseudoacromegaly",
                "Organize features into acromegaloid habitus (tall, normal, or short), primarily tall stature, or biochemical GH/IGF-1 discordance; gestalt, dysmorphism, pubertal timing, and intellectual disability narrow the list.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "the main features can be assigned to 3 categories: (1) primarily acromegaloid features with tall, normal, or short stature; (2) primarily tall stature; and (3) biochemical abnormalities suggestive of high GH or IGF-1 levels.",
                ),
            ),
            note(
                f"{p}-n3",
                "Pachydermoperiostosis",
                "How urinary PGE2 helps diagnose pachydermoperiostosis",
                "Clubbing, forehead furrowing, young-onset arthralgia, and lean habitus suggest pachydermoperiostosis from SLCO2A1 or HPGD variants; elevated urinary PGE2 with low metabolites points to HPGD deficiency.",
                ref(
                    "Case 1",
                    "In patients with HPGD pathogenic variants, there is elevated urinary PGE2 (Answer D), with low/undetectable PGE2 metabolites",
                ),
            ),
            note(
                f"{p}-n4",
                "Cantú syndrome",
                "Cantú syndrome: hypertrichosis and cardiac findings",
                "Infant-onset generalized hypertrichosis with coarse facies, cardiomegaly, PDA, and pericardial effusions suggests Cantú syndrome from activating ABCC9 or KCNJ8 variants—minoxidil can phenocopy via K-ATP channel activation.",
                ref(
                    "Case 2",
                    "Hypertrichotic osteochondrodysplasia is caused by activating pathogenic variants in the ABCC9 gene (sulfonylurea receptor 2) or, rarely, its partner the KCNJ8 gene",
                ),
            ),
            note(
                f"{p}-n5",
                "Pubertal GH testing",
                "Why oral glucose suppression testing is challenging in adolescence",
                "GH nadir after OGTT is pubertal-stage and gender specific—highest in Tanner 2–3 girls (1.57 ng/mL)—and IGF-1 correlates better with pubertal stage than chronological age.",
                ref(
                    "Biochemical Alterations",
                    "GH nadir is highest in Tanner stage 2 to 3 girls (1.57 ng/mL [1.57 μg/L]) and lower in other pubetal stages (0.64 ng/mL [0.64 μg/L]) or for boys (0.5 ng/mL [0.5 μg/L]).",
                ),
            ),
            note(
                f"{p}-n6",
                "IGSF1 deficiency",
                "Why IGSF1 deficiency elevates GH and IGF-1 without acromegaly",
                "IGSF1 deficiency is the only known condition with elevated GH and IGF-1 without clinical acromegaly—central hypothyroidism and testicular enlargement are part of the syndrome.",
                ref(
                    "Biochemical Alterations",
                    "There is only one known disease condition in which both high GH and IGF-1 can be seen without the patient having clinical acromegaly: the recently described IGSF1 deficiency syndrome.",
                ),
            ),
            note(
                f"{p}-n7",
                "X-linked acrogigantism",
                "How X-linked acrogigantism presents in early childhood",
                "GPR101 duplication causes infant-onset GH/IGF-1 and prolactin excess with pituitary hyperplasia—almost 80% of patients are female; normal birth weight with rapid growth under age 1 is typical.",
                ref(
                    "Case 3",
                    "Almost 80% of patients with X-linked acrogigantism are female.",
                ),
            ),
            note(
                f"{p}-n8",
                "Overgrowth syndromes",
                "Sotos, Weaver, and related overgrowth syndromes",
                "Rapid childhood growth with acromegaloid features, typical gestalt, and intellectual disability characterize several overgrowth syndromes—clinical phenotyping precedes targeted gene panels.",
                ref(
                    "Acromegaloid Features",
                    "Acromegaloid features with rapid growth in childhood are typical of several overgrowth syndromes such as Sotos syndrome, Weaver syndrome, Beckwith-Wiedemann syndrome, and Tatton-Brown syndrome",
                ),
            ),
            note(
                f"{p}-n9",
                "Minoxidil phenocopy",
                "How minoxidil mimics Cantú syndrome",
                "Prolonged minoxidil activates ATP-sensitive potassium channels like Cantú syndrome, producing acromegaloid skin changes and hypertrichosis.",
                ref(
                    "Acromegaloid Features",
                    "Longstanding minoxidil treatment, via its stimulating activity on the ATP potassium channel, produces symptoms similar to those observed in Cantú syndrome, acromegaloid skin changes, and hypertrichosis.",
                ),
            ),
            note(
                f"{p}-n10",
                "Diagnostic delay",
                "Pitfall: decades-long misdiagnosis of pseudoacromegaly",
                "Rare conditions are often missed—reported cases were referred to endocrinology four times over 40 years before correct genetic diagnosis.",
                ref(
                    "Barriers to Optimal Practice",
                    "We have reported a case in which a patient was referred to endocrinology on 4 different occasions over 40 years, from age 10 to 50 years, by the time the correct diagnosis was made.",
                ),
            ),
            note(
                f"{p}-n11",
                "Miura type",
                "Miura-type epiphyseal chondrodysplasia and toe length",
                "Extreme tall stature in young children with extra-long halluces can indicate natriuretic peptide C pathway disorders such as Miura-type epiphyseal chondrodysplasia.",
                ref(
                    "Case 3",
                    "Extra-long halluces could be diagnostic for diseases affecting the natriuretic peptide C pathway.",
                ),
            ),
            note(
                f"{p}-n12",
                "Genetic referral",
                "When to refer pseudoacromegaly patients for genetics",
                "After excluding endocrine GH excess, most pseudoacromegaly conditions are genetic—genetic consultation is recommended.",
                ref(
                    "Main Conclusions",
                    "Most pseudoacromegaly conditions have a genetic origin, so referral for genetic consultation is recommended if endocrine causes have been ruled out.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A 26-year-old man has tall stature, clubbing, forehead furrowing, sweating since age 15, and lean habitus. Best diagnostic step?",
                [
                    "Family history only",
                    "Baseline pituitary function tests",
                    "Genetic consultation without biochemical workup",
                    "Urinary prostaglandin E2 measurement",
                ],
                3,
                "Clubbing with pachydermia suggests pachydermoperiostosis; urinary PGE2 helps distinguish HPGD from SLCO2A1 subtypes.",
                ref(
                    "Case 1",
                    "Measuring baseline pituitary hormones (Answer B) can help rule out acromegaly.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A woman has coarse facies, thickened fingers, and infant-onset generalized hypertrichosis in multiple family members with pericardial effusions. Best approach?",
                [
                    "GH and IGF-1 only",
                    "Gonadal hormone panel only",
                    "Type clinical features into a search engine to identify syndromes",
                    "Immediate pituitary MRI without biochemical testing",
                ],
                2,
                "Cantú syndrome has a broad multisystem phenotype—pattern recognition via clinical search can accelerate diagnosis before genetic confirmation.",
                ref(
                    "Case 2",
                    "Typing clinical features into Google (Answer C) may be helpful.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A 4-year-old girl has height +5 SD without family tall stature. Which diagnosis should be included in the differential?",
                [
                    "X-linked acrogigantism",
                    "Neurofibromatosis type 1",
                    "Epiphyseal chondrodysplasia, Miura type",
                    "Carney complex",
                ],
                2,
                "Extreme childhood tall stature with long toes suggests Miura-type epiphyseal chondrodysplasia; XLAG causes infant-onset acrogigantism.",
                ref(
                    "Case 3",
                    "Answer: H) Epiphyseal chondrodysplasia, Miura type",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Pachydermoperiostosis",
                "Pachydermoperiostosis is caused by pathogenic variants in:",
                [
                    "ABCC9 and KCNJ8",
                    "SLCO2A1 and HPGD",
                    "GPR101",
                    "IGSF1",
                ],
                1,
                "SLCO2A1 (PGE2 transporter) and HPGD (15-PGDH) defects raise PGE2 and produce clubbing and pachydermia.",
                ref(
                    "Case 1",
                    "biallelic pathogenic variants in the transporter SLCO2A1 gene where PGE2 is degraded, or due to defective enzymatic clearing of PGE2 caused by biallelic pathogenic variants in the HPGD gene",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Cantú syndrome",
                "Cantú syndrome is caused by activating variants in:",
                [
                    "FBN1",
                    "COL1A1",
                    "ABCC9 or KCNJ8",
                    "PROP1",
                ],
                2,
                "ABCC9 (SUR2) and rarely KCNJ8 (Kir6.1) encode ATP-sensitive K+ channel subunits.",
                ref(
                    "Case 2",
                    "activating pathogenic variants in the ABCC9 gene (sulfonylurea receptor 2) or, rarely, its partner the KCNJ8 gene",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Biochemistry",
                "Physiological states with both elevated GH and IGF-1 include:",
                [
                    "Hypothyroidism and anorexia",
                    "Pregnancy and adolescence",
                    "Cushing syndrome and obesity",
                    "Primary hypogonadism only",
                ],
                1,
                "Pregnancy and adolescence are the two physiological states with elevated GH and IGF-1.",
                ref(
                    "Table. Conditions Associated With Discrepant GH and/or IGF-1 Levels",
                    "Adolescence",
                ),
            ),
            mcq(
                f"{p}-q7",
                "XLAG",
                "X-linked acrogigantism is due to:",
                [
                    "AIP pathogenic variants",
                    "GPR101 duplication",
                    "MEN1 pathogenic variants",
                    "McCune-Albright gsp mutation",
                ],
                1,
                "GPR101 duplication on X chromosome causes infant-onset pituitary hyperplasia/tumor with GH, IGF-1, and usually prolactin excess.",
                ref(
                    "Case 3",
                    "X-linked acrogigantism is due to duplication of the orphan receptor GPR101 gene",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Marfan syndrome",
                "In evaluating tall stature, Marfan syndrome is suggested by:",
                [
                    "Intellectual disability as a universal feature",
                    "Ectopia lentis in nearly 60% of cases",
                    "Suppressed IGF-1 and GH",
                    "Generalized hypertrichosis at birth",
                ],
                1,
                "Ectopia lentis is a hallmark; cardiovascular aortic dilation and mitral prolapse are evaluated with Ghent criteria.",
                ref(
                    "Case 3",
                    "ectopia lentis is the hallmark feature seen in nearly 60% of cases.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Drug effect",
                "Which medication can produce a phenocopy of Cantú syndrome?",
                [
                    "Phenytoin",
                    "Minoxidil",
                    "Metformin",
                    "Levothyroxine",
                ],
                1,
                "Minoxidil activates the same K-ATP channels, causing hypertrichosis and acromegaloid skin changes.",
                ref(
                    "Acromegaloid Features",
                    "Longstanding minoxidil treatment, via its stimulating activity on the ATP potassium channel, produces symptoms similar to those observed in Cantú syndrome",
                ),
            ),
            mcq(
                f"{p}-q10",
                "IGSF1",
                "IGSF1 deficiency syndrome is characterized by:",
                [
                    "Low GH and IGF-1 with gigantism",
                    "High GH and IGF-1 without clinical acromegaly",
                    "Isolated prolactinoma",
                    "Normal GH axis with acromegaloid facies only",
                ],
                1,
                "IGSF1 loss-of-function is the unique high GH/IGF-1 without acromegaly syndrome.",
                ref(
                    "Biochemical Alterations",
                    "both high GH and IGF-1 can be seen without the patient having clinical acromegaly: the recently described IGSF1 deficiency syndrome.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Overgrowth",
                "Which feature favors an overgrowth syndrome over pituitary gigantism in a tall child?",
                [
                    "Acromegaloid habitus with increased appetite only",
                    "Intellectual disability and characteristic gestalt",
                    "Elevated prolactin with microadenoma",
                    "GH nadir <0.4 ng/mL on OGTT in a pubertal boy",
                ],
                1,
                "Overgrowth syndromes often show gestalt and developmental delay; pituitary gigantism shows true GH/IGF-1 excess.",
                ref(
                    "Case 3",
                    "Is there evidence of intellectual disability or central nervous system abnormalities? This would suggest overgrowth syndromes",
                ),
            ),
            mcq(
                f"{p}-q12",
                "PGE2 mechanism",
                "Clubbing in pachydermoperiostosis shares mechanism with lung disease because:",
                [
                    "Both cause GH hypersecretion",
                    "The lung is the primary site for PGE2 degradation",
                    "Both involve IGF-2 hypoglycemia",
                    "Both are treated with somatostatin analogues",
                ],
                1,
                "SLCO2A1 defects impair pulmonary PGE2 uptake/degradation—same pathway implicated in pulmonary clubbing.",
                ref(
                    "Case 1",
                    "the mechanism is probably linked, as lung is the primary site for PGE2 degradation.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Initial workup",
                "In any patient with acromegaloid features, the essential first endocrine step is:",
                [
                    "Urinary prostaglandin E2 before GH testing",
                    "Measurement of GH and IGF-1 to exclude true acromegaly",
                    "Immediate genetic panel without exam",
                    "Skull MRI before biochemistry",
                ],
                1,
                "True acromegaly must be excluded biochemically before pursuing rare pseudoacromegaly diagnoses.",
                ref(
                    "Significance of the Clinical Problem",
                    "which should lead to the prompt assessment of the GH/IGF-1 axis.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Overview",
                "Pseudoacromegaly conditions can include acromegaloid facies, prognathism, visceromegaly, and hyperhidrosis without GH excess.",
                True,
                "Overlapping features are listed in the significance section.",
                ref(
                    "Significance of the Clinical Problem",
                    "Overlapping features can include acromegaloid facies and acral enlargement, prognathism, visceromegaly, hypertension, fatigue, headaches, arthralgias, paresthesia, hyperhidrosis",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Cantú syndrome",
                "Cantú syndrome commonly presents with suppressed gonadotropins and primary amenorrhea.",
                False,
                "Cantú features hypertrichosis, coarse facies, cardiac enlargement, and joint hyperextensibility—not primary hypogonadism.",
                ref(
                    "Case 2",
                    "The most prominent manifestation is the generalized hypertrichosis, in addition to the coarse facial features, bulbous nose, thick lips",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Pregnancy",
                "IGF-1 peaks around the 37th week of pregnancy at 2–3 times nonpregnant levels.",
                True,
                "Pregnancy creates a unique GH/IGF axis with placental GH and protease effects.",
                ref(
                    "Biochemical Alterations",
                    "increased IGF-1 peaking at the 37th week of pregnancy.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Phenytoin",
                "Prolonged phenytoin use can induce some acromegaloid features.",
                True,
                "Drug adverse effects are listed among pseudoacromegaly causes.",
                ref(
                    "Acromegaloid Features",
                    "Phenytoin can induce some acromegaloid features.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "XLAG sex",
                "X-linked acrogigantism predominantly affects males.",
                False,
                "Almost 80% of XLAG patients are female.",
                ref(
                    "Case 3",
                    "Almost 80% of patients with X-linked acrogigantism are female.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "HPGD",
                "In HPGD-related pachydermoperiostosis, urinary PGE2 is elevated with low or undetectable PGE2 metabolites.",
                True,
                "This biochemical pattern distinguishes HPGD from SLCO2A1 subtypes.",
                ref(
                    "Case 1",
                    "there is elevated urinary PGE2 (Answer D), with low/undetectable PGE2 metabolites",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Sotos syndrome",
                "Distinctive forehead appearance and gestalt characterize Sotos syndrome among acromegaloid differentials.",
                True,
                "Key facial gestalt aids differentiation.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Key facial features (the overall \"gestalt\") may characterize Sotos syndrome.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "GH receptor",
                "Increased tissue responsiveness to GH (e.g., GH receptor D3 genotype) can cause normal GH with high IGF-1.",
                True,
                "Listed under normal GH and high IGF-1 conditions.",
                ref(
                    "Table. Conditions Associated With Discrepant GH and/or IGF-1 Levels",
                    "Increased tissue responsiveness to GH (eg, genotype D3 of the GH receptor)",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Pseudoacromegaly",
                "Assertion: Patients with pseudoacromegaly may be referred repeatedly before correct diagnosis.",
                "Reason: Most physicians lack experience with these rare usually genetic disorders.",
                0,
                "Both true—awareness barrier causes diagnostic delay.",
                ref(
                    "Barriers to Optimal Practice",
                    "Because pseudoacromegaly conditions are rare, most physicians have no experience with these diseases, thus hindering diagnosis.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Pachydermoperiostosis",
                "Assertion: Clubbing in a young patient with acromegaloid features suggests pachydermoperiostosis.",
                "Reason: Pachydermoperiostosis is caused by GH hypersecretion from a pituitary adenoma.",
                2,
                "Assertion true; reason false—mechanism is PGE2 metabolism, not GH excess.",
                ref(
                    "Case 1",
                    "The key clinical diagnostic clue in this case is the clubbing",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Cantú syndrome",
                "Assertion: Minoxidil can phenocopy Cantú syndrome.",
                "Reason: Minoxidil activates ATP-sensitive potassium channels like activating ABCC9 variants.",
                0,
                "Both true and mechanistically linked.",
                ref(
                    "Case 2",
                    "minoxidil activates this potassium channel and is of course used to induce hair growth.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Adolescent OGTT",
                "Assertion: GH may fail to suppress adequately on OGTT during pubertal growth spurts.",
                "Reason: GH nadir thresholds are identical for all pubertal stages and genders.",
                2,
                "Assertion true; reason false—nadir is stage and gender specific.",
                ref(
                    "Biochemical Alterations",
                    "GH levels are increased, particularly at the peak of pubertal growth, and often do not fully suppress during an oral glucose tolerance test.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Genetics",
                "Assertion: Genetic consultation is recommended when endocrine causes of acromegaly are excluded.",
                "Reason: Most pseudoacromegaly conditions have a genetic origin.",
                0,
                "Both true per main conclusions.",
                ref(
                    "Main Conclusions",
                    "Most pseudoacromegaly conditions have a genetic origin, so referral for genetic consultation is recommended if endocrine causes have been ruled out.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "XLAG",
                "Assertion: X-linked acrogigantism should be considered in extreme childhood tall stature.",
                "Reason: XLAG is due to GPR101 duplication causing GH/IGF-1 and usually prolactin excess.",
                0,
                "Both true—only endocrine cause of such extreme SD height.",
                ref(
                    "Case 3",
                    "Of the endocrine causes, the only abnormality resulting in this degree of SD in height is X-linked acrogigantism (Answer A)",
                ),
            ),
            ar(
                f"{p}-ar7",
                "IGSF1",
                "Assertion: IGSF1 deficiency can elevate both GH and IGF-1 without clinical acromegaly.",
                "Reason: IGSF1 deficiency always presents with pituitary gigantism.",
                2,
                "Assertion true; reason false—no acromegaly/gigantism phenotype.",
                ref(
                    "Biochemical Alterations",
                    "both high GH and IGF-1 can be seen without the patient having clinical acromegaly: the recently described IGSF1 deficiency syndrome.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Hyperinsulinemia",
                "Assertion: Severe insulin resistance can produce acromegaloid clinical features.",
                "Reason: Hyperinsulinemia is among the most common pseudoacromegaly presentations in endocrine clinics.",
                2,
                "Assertion true; hyperinsulinemia is rare except as noted—reason overstates frequency.",
                ref(
                    "Significance of the Clinical Problem",
                    "Apart from hyperinsulinemia, pseudoacromegaly states are rare conditions",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "21",
        "title": "Pseudoacromegaly Syndromes",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Marta Korbonits, MD, PhD; Pedro Marques, MD, PhD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_21_Pseudoacromegaly_Syndromes.md",
        "items": items,
    }
