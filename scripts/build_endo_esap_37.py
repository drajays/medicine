#!/usr/bin/env python3
"""Generate remediated ESAP 2021 module e21-37 — medullary thyroid carcinoma."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT = PORTAL_DATA / "endo2021_chapter_37_Patients_With_oid_Cancer.json"


def build() -> dict:
    p = "e21-37"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Epidemiology",
                "Why early MTC diagnosis is the only curative strategy",
                "Medullary thyroid carcinoma arises from parafollicular C cells. Early intrathyroidal disease permits definitive cure; delayed diagnosis with extrathyroidal spread is rarely curable and requires lifelong surveillance and possible systemic therapy.",
                ref(
                    "Significance of the Clinical Problem",
                    "early diagnosis followed by early treatment is the only way to guarantee definitive cure.",
                ),
            ),
            note(
                f"{p}-n2",
                "Prognostic markers",
                "How serum calcitonin guides MTC prognosis",
                "Preoperative calcitonin <500 pg/mL and postoperative calcitonin <20 pg/mL portend good prognosis. Laterocervical (not central compartment) nodal metastases at diagnosis worsen persistence and survival.",
                ref(
                    "Prognostic Factors",
                    "If the calcitonin value is less than 500 pg/mL (<146 pmol/L) before surgery, there is a good probability of survival. Clinical remission is almost 100% when calcitonin decreases to less than 20 pg/mL (<5.8 pmol/L) after surgery.",
                ),
            ),
            note(
                f"{p}-n3",
                "Diagnosis",
                "Why calcitonin outperforms cytology for MTC detection",
                "MTC cytology is often nonspecific; several series report high FNA failure rates. Routine or selective serum calcitonin measurement is more sensitive than cytology for detecting MTC in thyroid nodules.",
                ref(
                    "Diagnosis",
                    "Several studies have demonstrated that routine measurement of serum calcitonin is the most accurate diagnostic tool for the detection of MTC in patients with thyroid nodules. In all series, the sensitivity of serum calcitonin was more accurate than that of cytology.",
                ),
            ),
            note(
                f"{p}-n4",
                "Grey-zone calcitonin",
                "How to evaluate basal calcitonin 20–100 pg/mL",
                "Medium-low calcitonin is not immediately diagnostic. Calcium stimulation (3–4× rise) confirms MTC secretion; FNA needle-wash calcitonin localizes the source when cytology is indeterminate.",
                ref(
                    "Diagnostic Tools When Serum Calcitonin Is In the Grey Zone",
                    "Elevated basal serum calcitonin, especially a medium-low level (ie, <100 pg/mL (<29.2 pmol/L)), should not be immediately considered to be diagnostic of MTC.",
                ),
            ),
            note(
                f"{p}-n5",
                "RET screening",
                "Why all MTC patients need germline RET testing",
                "Despite absent family history, 5–10% of apparently sporadic MTC harbor germline RET variants. Identification enables cascade screening and risk-stratified prophylactic thyroidectomy in carriers.",
                ref(
                    "Genetic Screening",
                    "RET genetic screening must be performed in all patients with MTC, even in the absence of a family history of thyroid cancer.",
                ),
            ),
            note(
                f"{p}-n6",
                "MEN2 timing",
                "How ATA risk classes guide prophylactic thyroidectomy",
                "RET variant penetrance varies (M918T most aggressive; V804M/S891A less so). Timing of prophylactic thyroidectomy depends on mutation risk class plus basal and stimulated calcitonin in carriers.",
                ref(
                    "Genetic Screening",
                    "the American Thyroid Association guidelines classify pathogenic variants into different classes of risk, and the timing of thyroidectomy in carriers should be based on several factors, including the level of risk of the pathogenic variant and the basal and stimulated value of serum calcitonin.",
                ),
            ),
            note(
                f"{p}-n7",
                "Follow-up",
                "Why CEA complements calcitonin in advanced MTC",
                "Post-thyroidectomy surveillance includes exam, neck ultrasound, thyroid function, calcitonin, and CEA. Dedifferentiated tumors may show relatively low calcitonin with rising CEA reflecting tumor burden.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "CEA measurement is relevant because it provides a better idea about the tumor burden and the degree of differentiation of the tumor since, when dedifferentiated, serum calcitonin can be relatively low and CEA rather elevated.",
                ),
            ),
            note(
                f"{p}-n8",
                "Systemic therapy",
                "When to start vandetanib or cabozantinib",
                "TKIs are indicated for RECIST-documented progression within 12 months or clinically advanced disease. Local therapy is preferred when metastases are small and slow-growing; systemic therapy when multimetastatic progressive disease is evident.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "These medications should be started if the progression of the disease, as assessed according to Response Evaluation Criteria in Solid Tumors (RECIST), has been documented in the last 12 months or according to clinical judgment in very advanced cases.",
                ),
            ),
            note(
                f"{p}-n9",
                "Drug selection",
                "How to choose between vandetanib and cabozantinib",
                "Cabozantinib may act faster but with a more demanding safety profile and can follow prior TKI; vandetanib is more manageable, slower, usable in children, and effective for ectopic ACTH/Cushing—but contraindicated if QTc prolonged.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "According to the results of the phase 3 studies, the effect of cabozantinib seems to be more rapid but with a safety profile more demanding in its management.",
                ),
            ),
            note(
                f"{p}-n10",
                "Emerging RET inhibitors",
                "Why selective RET inhibitors may supersede multikinase TKIs",
                "LOXO-292 and BLU-667 (pralsetinib) target RET specifically with efficacy similar to TKIs but less impact on quality of life—promising for resistance after vandetanib/cabozantinib.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "There are already 2 new RET-specific inhibitors, LOXO 29218 and BLUE 667, that are characterized by good efficacy similar to that of the tyrosine kinase inhibitors, with a much smaller impact on quality of life.",
                ),
            ),
            note(
                f"{p}-n11",
                "Referral",
                "Why MTC requires multidisciplinary specialized centers",
                "Rarity, cytologic difficulty, familial implications, and complex persistent disease management warrant follow-up in a multidisciplinary team at a specialized center.",
                ref(
                    "Conclusions",
                    "it is recommended that patients with MTC be followed by a multidisciplinary team in a specialized center.",
                ),
            ),
            note(
                f"{p}-n12",
                "ZETA/EXAM trials",
                "What ZETA and EXAM established for advanced MTC",
                "Phase 3 trials of vandetanib and cabozantinib demonstrated significant progression-free survival benefit versus placebo in advanced progressive MTC, leading to FDA and EMA approval.",
                ref(
                    "Significance of the Clinical Problem",
                    "Phase 3 clinical trials with these 2 drugs, the ZETA and EXAM trials, demonstrated significant prolongation of progression-free survival in patients treated with the drug compared with survival in those treated with placebo.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1",
                "A 43-year-old woman has a 2.4-cm suspicious right thyroid nodule, AUS/FLUS cytology, normal thyroid function, and serum calcitonin 45 pg/mL. Neck ultrasound shows no abnormal lymph nodes. What is the best next step?",
                [
                    "Wait-and-see with repeat testing every 6 months",
                    "Total thyroidectomy with central neck dissection",
                    "Right lobectomy for diagnosis",
                    "Repeat FNA with calcitonin immunocytochemistry and needle-wash calcitonin",
                ],
                3,
                "Calcitonin 20–100 pg/mL is a grey zone requiring localization—needle-wash calcitonin and immunocytochemistry clarify MTC before committing to extent of surgery.",
                ref(
                    "Case 1",
                    "Repeated FNA for immunocytochemistry for calcitonin and measurement of calcitonin in the needle washout",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2",
                "A 56-year-old man has MTC on FNA of a 2.9-cm nodule, calcitonin 420 pg/mL, no sonographic nodal metastases. After total thyroidectomy and central dissection, histology shows MTC with C-cell hyperplasia and no nodal metastases. He asks about prognosis and family screening. Which statement is correct?",
                [
                    "Good prognosis likely; perform RET genetic screening on the patient first",
                    "MTC prognosis is always poor; screen relatives with serum calcitonin only",
                    "Good prognosis; no relative screening without family history",
                    "Prognosis depends on sporadic vs hereditary nature before any relative testing",
                ],
                0,
                "Intra-thyroidal disease with calcitonin <500 pg/mL suggests good prognosis. All MTC patients need germline RET testing regardless of family history before cascade family screening.",
                ref(
                    "Case 2",
                    "His prognosis is good with a high probability for long survival: RET genetic screening should be first performed in the patient himself",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3",
                "A 63-year-old man with long-standing metastatic MTC has rising calcitonin (630→780 pg/mL) and CEA (68→85 ng/mL), RECIST progression of mediastinal, lung, and liver lesions, and new diarrhea. Best next step?",
                [
                    "Intravenous chemotherapy",
                    "Start a tyrosine kinase inhibitor",
                    "Continue observation only",
                    "External beam radiotherapy to mediastinal nodes",
                ],
                1,
                "Rapid biochemical and radiographic progression with symptoms meets criteria for systemic TKI therapy; vandetanib is preferred when symptomatic.",
                ref(
                    "Case 3",
                    "Start a tyrosine kinase inhibitor",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Calcitonin screening",
                "For a thyroid nodule with planned surgery for indeterminate cytology, the most appropriate additional test is:",
                [
                    "Serum thyroglobulin",
                    "Basal serum calcitonin",
                    "TSH receptor antibody",
                    "24-hour urinary iodine",
                ],
                1,
                "When routine calcitonin is not used for all nodules, it should at least be measured when surgery is planned for indeterminate cytology; elevated levels guide extent of surgery.",
                ref(
                    "Diagnosis",
                    "If the routine measurement of serum calcitonin is not adopted in the clinical workup of thyroid nodules, it could be helpful at least when surgical treatment is planned for a nodule with indeterminate cytology.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Calcium stimulation",
                "A patient has basal calcitonin 65 pg/mL with indeterminate FNA. Calcium stimulation test shows 4-fold rise in calcitonin. This pattern most strongly supports:",
                [
                    "Heterophile antibody interference only",
                    "True MTC calcitonin secretion",
                    "Ectopic calcitonin from lung NET without thyroid MTC",
                    "Exclusion of MTC",
                ],
                1,
                "True MTC calcitonin rises markedly (typically 3–4×) after calcium stimulation; other sources and artifacts do not.",
                ref(
                    "Case 1",
                    "true calcitonin secreted by MTC shows a very high increase after stimulation, while calcitonin from other origins (i.e., other neuroendocrine tumors, ectopic production, interference from heterophilic antibodies, etc) does not respond to the stimulus.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Surgery extent",
                "For confirmed unilateral MTC without nodal disease on imaging, standard initial surgery includes:",
                [
                    "Hemithyroidectomy alone",
                    "Total thyroidectomy with central compartment neck dissection",
                    "Iodine-131 ablation only",
                    "External neck irradiation",
                ],
                1,
                "Total thyroidectomy with central neck dissection is standard for MTC; lobectomy alone is insufficient for established MTC.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "When patients are not cured by the primary surgical treatment, which should include total thyroidectomy and central neck lymph node dissection",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Hereditary MTC",
                "After identifying a germline RET variant in an index MTC patient, relatives who test negative for the variant:",
                [
                    "Require lifelong annual calcitonin screening",
                    "Can avoid ongoing MTC surveillance",
                    "Need prophylactic thyroidectomy by age 5",
                    "Must undergo annual neck MRI",
                ],
                1,
                "Relatives without the familial RET variant are not at increased MTC risk and need not be monitored longitudinally for MTC.",
                ref(
                    "Genetic Screening",
                    "Relatives who do not carry the pathogenic variant can avoid being monitored over the years, as they are not at increased risk to develop MTC.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "TKI limitations",
                "Regarding vandetanib and cabozantinib in MTC, which is true?",
                [
                    "Both demonstrated overall survival benefit in phase 3 trials",
                    "They are cytotoxic and cure metastatic disease",
                    "They prolong progression-free survival but resistance eventually develops",
                    "They replace the need for initial surgery",
                ],
                2,
                "ZETA and EXAM showed PFS benefit, not proven OS advantage; TKIs are cytostatic and resistance emerges requiring continued clinical judgment.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "from the results of the 2 studies, it is clearly evident that sooner or later a sort of resistance develops",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Vandetanib contraindication",
                "Vandetanib should be avoided in which patient?",
                [
                    "Childhood MTC with MEN2B",
                    "Symptomatic metastatic MTC with diarrhea",
                    "Prolonged QTc interval >470 ms in a woman",
                    "Prior cabozantinib failure",
                ],
                2,
                "Vandetanib prolongs QTc and is contraindicated when QTc exceeds sex-specific thresholds; cabozantinib lacks this limitation.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "Vandetanib cannot be used in patients who have a prolonged QTc interval (>450 ms in men and >470 ms in women), while cabozantinib does not have this limitation.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "MEN2B clues",
                "Physical findings most suggestive of MEN2B and prompting MTC evaluation include:",
                [
                    "Graves ophthalmopathy",
                    "Mucosal neuromas and marfanoid habitus",
                    "Pretibial myxedema",
                    "Amenorrhea with hyperprolactinemia",
                ],
                1,
                "Mucosal neuromas, marfanoid habitus, and skeletal alterations suggest MEN2B and should prompt MTC evaluation.",
                ref(
                    "Diagnosis",
                    "Mucosal neuromas on the gue and/or in the conjunctiva, marfanoid itus, and/or skeletal alterations suggest the nosis of multiple endocrine neoplasia type 2B should prompt evaluation for MTC.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Indolent metastases",
                "Small slow-growing distant MTC metastases on surveillance should generally prompt:",
                [
                    "Immediate TKI therapy",
                    "Observation with local therapy when feasible; defer systemic therapy until progression",
                    "High-dose radioactive iodine",
                    "Total body irradiation",
                ],
                1,
                "Slow-growing small metastases may be compatible with long good-quality life; aggressive systemic therapy is deferred unless rapid progression is documented.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "These lesions are compatible with a long period of good quality of life. In these cases, an aggressive therapeutic approach may not be indicated, unless an evident rapidly progressive disease is demonstrated.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Sporadic RET",
                "Somatic RET testing on tumor tissue in sporadic MTC may help because it:",
                [
                    "Eliminates need for calcitonin follow-up",
                    "Confirms sporadic nature and may guide RET-targeted therapy",
                    "Replaces germline testing entirely",
                    "Predicts response to radioactive iodine",
                ],
                1,
                "Somatic RET analysis can confirm sporadic disease, inform prognosis, and identify candidates for RET-specific inhibitors.",
                ref(
                    "Genetic Screening",
                    "the discovery of a somatic pathogenic variant (usually in 45% of cases) confirms the sporadic nature of the tumor",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Post-op remission",
                "Postoperative serum calcitonin <20 pg/mL after MTC surgery is associated with:",
                [
                    "Mandatory adjuvant external beam radiation",
                    "Near 100% clinical remission probability",
                    "Need for immediate TKI",
                    "Lifetime TSH suppression to <0.1 mIU/L",
                ],
                1,
                "Calcitonin <20 pg/mL after surgery correlates with near-complete remission probability.",
                ref(
                    "Prognostic Factors",
                    "Clinical remission is almost 100% when calcitonin decreases to less than 20 pg/mL (<5.8 pmol/L) after surgery.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "MTC prognosis",
                "All patients with medullary thyroid carcinoma have uniformly poor long-term survival regardless of stage at diagnosis.",
                False,
                "Early intrathyroidal MTC has favorable prognosis; stage and calcitonin levels stratify outcomes.",
                ref(
                    "Prognostic Factors",
                    "if an early diagnosis is made, possibly when the neoplastic disease is still intrathyroidal, 90% of patients survive up to 35 years.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Cytology",
                "FNA cytology reliably diagnoses MTC in the majority of cases without need for calcitonin measurement.",
                False,
                "Several series show high FNA failure rates; calcitonin is more sensitive.",
                ref(
                    "Diagnosis",
                    "Although the cytologic pattern of MTC is generally typical, several series show a high percentage of failure in making a presurgical diagnosis by FNA cytology.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "RET testing",
                "Germline RET screening is indicated only when family history of MTC is present.",
                False,
                "5–10% of apparently sporadic cases harbor germline RET variants.",
                ref(
                    "Genetic Screening",
                    "RET genetic screening must be performed in all patients with MTC, even in the absence of a family history of thyroid cancer.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Laterocervical nodes",
                "Laterocervical lymph node metastases at MTC diagnosis are a poor prognostic factor.",
                True,
                "Laterocervical nodal metastases worsen persistence and survival unlike isolated central compartment disease in some series.",
                ref(
                    "Prognostic Factors",
                    "the presence of lymph node metastases in the laterocervical neck region, but not those in the central compartment, is considered a bad prognostic factor",
                ),
            ),
            tf(
                f"{p}-tf5",
                "TKI timing",
                "Tyrosine kinase inhibitors should be started at MTC diagnosis regardless of disease burden.",
                False,
                "TKIs are for RECIST-documented progression or advanced symptomatic disease; observation may suffice for indolent metastases.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "These medications should be started if the progression of the disease, as assessed according to Response Evaluation Criteria in Solid Tumors (RECIST), has been documented in the last 12 months",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Cabozantinib",
                "Cabozantinib can be used after prior tyrosine kinase inhibitor therapy in progressive MTC.",
                True,
                "Cabozantinib showed PFS benefit as second-line after another TKI.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "Cabozantinib has also been tested in patients who had been previously treated with another tyrosine kinase inhibitor, and the results showed that it works in terms of prolongation of progression-free survival",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Vandetanib Cushing",
                "Vandetanib can reverse ectopic ACTH secretion and paraneoplastic Cushing syndrome in advanced MTC.",
                True,
                "Reported cases show reversal of ectopic ACTH/Cushing with vandetanib.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "there are several reported cases whereby the ectopic ACTH secretion and the consequent paraneoplastic Cushing syndrome, which is frequently present when the disease is multimetastatic and advanced, is reverted and cured by the administration of vandetanib.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "CEA",
                "CEA is useless in MTC follow-up because calcitonin is always elevated when disease is active.",
                False,
                "CEA reflects tumor burden and dedifferentiation when calcitonin is discordantly low.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "when dedifferentiated, serum calcitonin can be relatively low and CEA rather elevated.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Calcitonin",
                "Basal serum calcitonin is more sensitive than FNA cytology for detecting MTC in thyroid nodules.",
                "Calcitonin is produced almost exclusively by thyroid C cells in normal physiology.",
                0,
                "Both true; calcitonin specificity and superior sensitivity to cytology support the assertion, and C-cell origin explains selective secretion.",
                ref(
                    "Diagnosis",
                    "the sensitivity of serum calcitonin was more accurate than that of cytology.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "RET",
                "All patients with MTC require germline RET testing.",
                "A negative family history excludes hereditary MTC.",
                2,
                "Assertion true (universal RET testing recommended) but reason false—5–10% sporadic-appearing cases are germline positive.",
                ref(
                    "Genetic Screening",
                    "5% to 10% of patients with apparently sporadic MTC harbor a germline RET pathogenic variant",
                ),
            ),
            ar(
                f"{p}-ar3",
                "TKI",
                "Vandetanib and cabozantinib improve progression-free survival in advanced MTC.",
                "They have demonstrated improvement in overall survival in phase 3 trials.",
                1,
                "Both true but reason is false—PFS benefit shown; OS benefit not demonstrated.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "so far neither shown an increase in overall survival.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Grey zone",
                "Calcitonin 45 pg/mL in a patient with AUS/FLUS cytology warrants further MTC-directed testing.",
                "Any calcitonin above the upper limit of normal confirms MTC without further workup.",
                2,
                "Assertion true (grey-zone workup needed); reason false because 20–100 pg/mL is not immediately diagnostic.",
                ref(
                    "Case 1",
                    "When the serum calcitonin concentration is greater than 20 pg/mL but less than 100 pg/mL (5.8-29.2 pmol/L), it is not immediately diagnostic of MTC",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Prophylactic surgery",
                "Timing of prophylactic thyroidectomy in RET carriers depends on mutation risk class.",
                "All RET carriers should undergo thyroidectomy in infancy regardless of mutation.",
                2,
                "Assertion true per ATA risk stratification; reason false—timing is individualized not uniform infancy surgery.",
                ref(
                    "Genetic Screening",
                    "the timing of thyroidectomy in carriers should be based on several factors, including the level of risk of the pathogenic variant",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Surveillance",
                "Rising calcitonin and CEA with RECIST progression indicate need for systemic therapy in metastatic MTC.",
                "Stable small metastases always require immediate TKI regardless of biomarkers.",
                0,
                "Both true and linked—biochemical and radiographic progression triggers systemic therapy; indolent disease may be observed.",
                ref(
                    "Case 3",
                    "the evidence, according to RECIST (Response Evaluation Criteria in Solid Tumors), of progressive disease involving all the lesions is sufficient to indicate that it is now time to start a systemic therapy.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Specialized care",
                "MTC should be managed in specialized multidisciplinary centers.",
                "MTC is too common for referral centers to improve outcomes.",
                2,
                "Assertion true; reason false—MTC is rare and complexity favors specialized care.",
                ref(
                    "Conclusions",
                    "Considering the rarity of the disease, the difficulty of making an early diagnosis, the possibility that MTC can be familial, and the fact that management of persistent disease can be challenging, it is recommended that patients with MTC be followed by a multidisciplinary team in a specialized center.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "RET inhibitors",
                "Selective RET inhibitors may offer efficacy with fewer off-target toxicities than multikinase TKIs.",
                "RET inhibitors have no role after vandetanib or cabozantinib failure.",
                2,
                "Assertion true; reason false—emerging agents address resistance after first-line TKIs.",
                ref(
                    "Follow-Up and Therapies for Advanced Disease",
                    "There are already 2 new RET-specific inhibitors, LOXO 29218 and BLUE 667, that are characterized by good efficacy similar to that of the tyrosine kinase inhibitors, with a much smaller impact on quality of life.",
                ),
            ),
        ]
    )

    return {
        "id": "e21-37",
        "volume": 2021,
        "chapterNo": "37",
        "title": "Patients With Thyroid Cancer",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Rossella Elisei, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_37_Patients_With_oid_Cancer.md",
        "items": items,
    }


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    shutil.copy2(OUT, MASTER_DATA / OUT.name)
    print(f"Wrote {OUT} ({len(data['items'])} items)")


if __name__ == "__main__":
    main()
