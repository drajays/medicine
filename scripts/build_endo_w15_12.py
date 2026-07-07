#!/usr/bin/env python3
"""Generate Williams 15e module w15-12 — Nontoxic Goiter, Nodular Thyroid Disorders, and Thyroid Malignancies."""
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
OUT_NAME = "w15-12_Nontoxic_Diffuse_Goiter_Nodular_Thyroid_Disorders_and_Thyroid_Malignancies.json"


def build() -> dict:
    p = "w15-12"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Neck sonography in thyroid cancer care",
                "Neck sonography is integral to thyroid evaluation and especially useful in low-risk thyroid cancer for mapping disease and guiding follow-up.",
                ref(
                    "KEY POINTS",
                    "Neck sonography has become an integral part of the clinical evaluation of thyroid patients and a useful tool in patients with low-risk thyroid cancer.",
                ),
            ),
            note(
                f"{p}-n2",
                "Ultrasonography",
                "TIRADS and tiered sonographic risk systems",
                "ATA, ACR TIRADS, and similar systems score nodule features to estimate malignancy risk and recommend FNA versus surveillance, improving interobserver agreement.",
                ref(
                    "Ultrasonography",
                    "In 2017, the ACR published a scoring system that promotes systematic assessment of the imaging features of thyroid nodules, the Thyroid Imaging Reporting and Data System (TIRADS), which is inspired by the ACR's recommended approaches to the imaging of the breast (BIRADS) and other organs.",
                ),
            ),
            note(
                f"{p}-n3",
                "Ultrasonography",
                "Why microcalcifications and irregular margins drive FNA thresholds",
                "Features with highest specificity for cancer—microcalcifications, hypoechoic parenchyma, infiltrative margins—are most predictive in combination; high-risk nodules are generally biopsied at ≥1 cm.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Features with the highest specificity for thyroid cancer include the presence of microcalcifications, hypoechoic parenchyma, and infiltrative or irregular margins.",
                ),
            ),
            note(
                f"{p}-n4",
                "Nodular disease evaluation",
                "Why even normal-range TSH raises malignancy risk",
                "Higher serum TSH concentrations, even within the reference range, are associated with increased likelihood that a thyroid nodule is malignant.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Higher serum TSH concentrations, even within the normal reference range, may increase the risk that a thyroid nodule is cancerous.",
                ),
            ),
            note(
                f"{p}-n5",
                "Ultrasonography",
                "How preoperative neck US changes cancer surgery",
                "All patients with differentiated or medullary thyroid carcinoma should have preoperative sonography to identify suspicious regional nodes and plan nodal dissection.",
                ref(
                    "Ultrasonography",
                    "A preoperative sonogram should be obtained in all patients with differentiated thyroid carcinoma or medullary thyroid carcinoma (MTC) to preoperatively identify the anatomic locations of any sonographically suspicious regional lymph nodes and thereby permit planning of nodal dissection.",
                ),
            ),
            note(
                f"{p}-n6",
                "Thyroid scintigraphy",
                "Why autonomously functioning hot nodules are rarely malignant",
                "Functioning nodules—especially when surrounding tissue uptake is suppressed—account for fewer than 5–10% of nodules and are almost invariably benign.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "The only situation in which an iodine scan can exclude malignancy with reasonable certainty is in the case of a toxic (hot) adenoma.",
                ),
            ),
            note(
                f"{p}-n7",
                "Nontoxic goiter",
                "Epidemiology of goiter and thyroid nodules",
                "Goiter prevalence varies with iodine intake; sonographic screening shows 20–40% goiter prevalence in adults and up to 65% nodule prevalence in healthy adults screened with US.",
                ref(
                    "Epidemiology of Goiter",
                    "Using sonography as the screening method, the prevalence of goiter in an unselected adult population has been reported to be 20% to 40%.",
                ),
            ),
            note(
                f"{p}-n8",
                "Nodular disease evaluation",
                "How suppressed TSH redirects the nodule workup",
                "A low or undetectable TSH—even with normal free hormones—suggests toxic autonomous nodules and should prompt thyroid scintigraphy rather than proceeding directly to FNA of all nodules.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "A low or undetectable serum TSH, even if associated with normal free thyroid hormone levels, should suggest the possibility of toxic, autonomously functioning nodules and prompt thyroid scintigraphy.",
                ),
            ),
            note(
                f"{p}-n9",
                "Fine-needle aspiration",
                "FNA technique and Bethesda reporting",
                "US-guided FNA with on-site adequacy assessment exceeds 90% sensitivity and specificity; results are classified using the Bethesda System for Reporting Thyroid Cytopathology.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "FNA of thyroid nodules has eclipsed all other techniques for diagnosing thyroid cancer, with reported overall rates of sensitivity and specificity exceeding 90% in iodine-sufficient areas.",
                ),
            ),
            note(
                f"{p}-n10",
                "Laboratory evaluation",
                "Why serum thyroglobulin is not used in initial nodule assessment",
                "Follicular-cell carcinomas may release thyroglobulin, but overlap with benign disease makes serum Tg unhelpful in the initial workup of nodular thyroid disease.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Therefore, the measurement of serum Tg levels is not useful in the initial workup of nodular thyroid disease.",
                ),
            ),
            note(
                f"{p}-n11",
                "NIFTP",
                "Noninvasive follicular thyroid neoplasm with papillary-like nuclear features",
                "NIFTP represents encapsulated follicular-variant lesions without capsular or vascular invasion; properly diagnosed NIFTPs have outstanding prognosis and the term cancer has been removed from their definition.",
                ref(
                    "NIFTP",
                    "Because of this, the word cancer has been eliminated from the definition of these tumors to underscore their outstanding prognosis, thereby discouraging overly aggressive treatment and follow-up.",
                ),
            ),
            note(
                f"{p}-n12",
                "Fine-needle aspiration",
                "How Bethesda categories translate to management",
                "Bethesda malignant and suspicious categories warrant near-total thyroidectomy or lobectomy; benign results carry ~1–5% false-negative risk; indeterminate categories stratify malignancy risk from AUS/FLUS through suspicious for malignancy.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "Similarly, a benign result should be viewed as highly accurate because data confirmed a low risk (~1%–5%) of false-negative results and negligible mortality risk from false-negative aspirates during an 8.5-year follow-up.",
                ),
            ),
            note(
                f"{p}-n13",
                "Papillary thyroid carcinoma",
                "PTC epidemiology and prognosis",
                "PTC constitutes 50–90% of differentiated thyroid cancers worldwide; most present as AJCC stage I or II, yet 10–30% develop recurrences, often biochemical before structural.",
                ref(
                    "Papillary Thyroid Carcinoma",
                    "As the most common thyroid malignancy, PTC constitutes 50% to 90% of DTCs worldwide.",
                ),
            ),
            note(
                f"{p}-n14",
                "Molecular testing",
                "Why molecular classifiers refine indeterminate FNA cytology",
                "DNA mutational panels and RNA gene-expression classifiers improve preoperative risk assessment for Bethesda III/IV nodules, with high negative predictive values that can avoid unnecessary surgery.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "In most cases of a healthy patient with Bethesda class III or IV cytology, molecular testing is endorsed because of its ability to substantially improve preoperative cancer risk assessment and modify clinical care, especially when a negative (benign) result is obtained.",
                ),
            ),
            note(
                f"{p}-n15",
                "Follicular thyroid carcinoma",
                "FTC presentation and metastatic pattern",
                "FTC presents as a painless nodule, rarely with cervical nodes; lymph node metastases are exceptional and should prompt reconsideration of papillary variant or oncocytic carcinoma; distant lung and bone metastases occur in 15–27% at presentation.",
                ref(
                    "Presenting Features of Follicular Thyroid Carcinoma",
                    "Lymph node metastases to the neck in FTC are so exceptional that \"wherever they are observed, the alternative possibilities of follicular variant papillary carcinoma, oncocytic carcinoma, and poorly differentiated carcinoma should be considered.\"",
                ),
            ),
            note(
                f"{p}-n16",
                "Radioiodine therapy",
                "How postoperative RAI indications have narrowed",
                "Remnant ablation is no longer routinely recommended because neck US and high-sensitivity thyroglobulin on levothyroxine suffice for surveillance; adjuvant and therapeutic RAI remain for intermediate- and high-risk disease.",
                ref(
                    "131I and the Role of RAI Administration",
                    "This is no longer routinely recommended because disease surveillance may be satisfactorily accomplished without RAI ablation using neck US and high-sensitivity Tg (with Tg antibody) measurements while the patient is on thyroid hormone therapy.",
                ),
            ),
            note(
                f"{p}-n17",
                "Medullary thyroid carcinoma",
                "MTC diagnosis and calcitonin staging",
                "MTC arises from C cells; calcitonin >100 pg/mL suggests disease, and levels >500–1000 pg/mL predict extensive nodal or distant metastases requiring comprehensive imaging including liver MRI and FDOPA PET.",
                ref(
                    "Presenting Features of MTC",
                    "If the unstimulated serum calcitonin determination is greater than 100 pg/mL, MTC is likely present.",
                ),
            ),
            note(
                f"{p}-n18",
                "Surgery",
                "Why lobectomy suffices for many low-risk differentiated cancers",
                "For tumors >1 cm and <4 cm without multinodularity, invasion, irradiation history, or hypothyroidism, thyroid lobectomy alone should suffice; total thyroidectomy is warranted for tumors >4 cm or high-risk features.",
                ref(
                    "Surgical Therapy: Selecting Total or Lobectomy for Differentiated Thyroid Cancer",
                    "For a tumor >1 cm and <4 cm without any of the associated features or history, thyroid lobectomy alone should suffice.",
                ),
            ),
            note(
                f"{p}-n19",
                "Anaplastic thyroid carcinoma",
                "ATC presentation and staging",
                "ATC presents as a rapidly enlarging neck mass in older adults with hoarseness, dyspnea, or dysphagia; all cases are AJCC stage IV, PET/CT is essential, and resectability is the strongest survival predictor.",
                ref(
                    "Presenting Features of ATC",
                    "ATC typically presents in patients in the sixth or seventh decade of life as a rapidly enlarging neck mass that may be associated with hoarseness, dyspnea, dysphagia, and pain.",
                ),
            ),
            note(
                f"{p}-n20",
                "ATA risk stratification",
                "How ATA categories guide postoperative RAI",
                "ATA low-risk patients do not need remnant ablation; intermediate-risk patients may receive 30–150 mCi 131I; high-risk or metastatic disease warrants 100–200 mCi with dosimetry when diffuse pulmonary uptake is present.",
                ref(
                    "ATA Recurrence Risk Stratification to Guide Postoperative RAI Decision Making",
                    "RAI remnant ablation is not recommended for patients with ATA low-risk disease because of the long-term favorable prognosis after surgery alone.",
                ),
            ),
            note(
                f"{p}-n21",
                "Staging",
                "AJCC eighth edition thyroid cancer staging",
                "The 2017 AJCC system raises the age threshold for high-risk differentiated cancer to 55 years and attenuates prognostic weight of microscopic extrathyroidal extension and small cervical nodes.",
                ref(
                    "Classification and Staging of Thyroid Cancer",
                    "The main changes are (1) an increase in the age threshold (>55 years versus >45 years) for defining cases at high risk for thyroid cancer—related death and (2) attenuation of the previous unfavorable prognostic significance attributed to small cervical lymph node metastasis and microscopic extrathyroidal extension.",
                ),
            ),
            note(
                f"{p}-n22",
                "Long-term follow-up",
                "How thyroglobulin defines response to therapy",
                "After total thyroidectomy, excellent response requires suppressed Tg <0.2 ng/mL; rising Tg or antibodies without structural disease defines biochemical incomplete response; structural incomplete response carries highest mortality risk.",
                ref(
                    "Long-Term Follow-Up of Patients With Thyroid Cancer After Initial Therapy",
                    "However, with the development of new ultrasensitive assays, the definition of excellent response to therapy can be established with the suppressed thyroglobulin value of less than 0.2 ng/mL.",
                ),
            ),
            note(
                f"{p}-n23",
                "TSH-suppressive therapy",
                "TSH suppression targets after thyroid cancer treatment",
                "Levothyroxine suppresses TSH-driven tumor growth; goals are TSH <0.1 mU/L for high-risk, 0.1–0.5 for intermediate-risk, and 0.5–2 mU/L for low-risk patients, balanced against bone and cardiac risks.",
                ref(
                    "TSH-Suppressive Therapy",
                    "The initial goal is a serum TSH concentration that is below about 0.1 mU/L for patients with high-risk thyroid cancer or 0.1 to 0.5 mU/L for patients with intermediate risk, and the TSH may be maintained at the lower end of the reference range (0.5–2 mU/L) for low-risk patients.",
                ),
            ),
            note(
                f"{p}-n24",
                "RAI-refractory disease",
                "How to recognize RAI-refractory differentiated thyroid cancer",
                "Martinique Principles define refractoriness by absent post-therapy uptake, progression despite uptake or cumulative activity >600 mCi, or discordant avidity among metastases—clinical context still guides whether to re-treat.",
                ref(
                    "Defining RAI-Refractory Differentiated Thyroid Cancer",
                    "DTC metastasis or metastases progress despite a cumulative 131I activity of >22.2 GBq (600 mCi).",
                ),
            ),
            note(
                f"{p}-n25",
                "Hürthle cell carcinoma",
                "Oncocytic carcinoma biology and RAI responsiveness",
                "OCA (formerly Hürthle cell carcinoma) shows mitochondrial-rich cytoplasm, often presents as widely invasive disease, and demonstrates poor 131I avidity in metastases compared with other differentiated histologies.",
                ref(
                    "Risk of Recurrence and Mortality",
                    "In a series including 22 patients with metastatic OCA treated with 131I, 131I avidity was present in only 13.6% of cases, a rate that was lower compared to all other DTC histology studies.",
                ),
            ),
            note(
                f"{p}-n26",
                "Targeted therapy",
                "Why biomarker testing precedes systemic therapy",
                "RAI-refractory differentiated thyroid cancer often harbors BRAFV600E, RET, NTRK, or ALK alterations; multigene NGS is recommended before initiating systemic treatment because multiple biomarker-directed therapies are now available.",
                ref(
                    "Systemic Therapy for RAI-Refractory DTC",
                    "Thus, biomarker testing to identify potential oncogenic driver alterations is now considered essential before initiating systemic treatment in most patients with RAI-refractory DTC.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Ultrasonography",
                "A 52-year-old woman has a 1.4-cm solid hypoechoic nodule with irregular margins and punctate echogenic foci but no abnormal nodes. Best next step?",
                [
                    "US-guided FNA because high-suspicion features meet biopsy size threshold",
                    "Repeat US in 2 years because nodule is <2 cm",
                    "Therapeutic 131I ablation without cytology",
                    "Serum thyroglobulin to exclude cancer",
                ],
                0,
                "Microcalcifications, hypoechocity, and irregular margins are high-risk; ATA/TIRADS generally recommend FNA at ≥1 cm.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "For example, FNA of higher-risk nodules is generally recommended when they are equal to or larger than 1 cm.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Ultrasonography",
                "A 1.8-cm purely cystic thyroid nodule is incidentally found. No suspicious nodes. Appropriate management?",
                [
                    "Conservative surveillance without FNA for diagnosis",
                    "Immediate total thyroidectomy",
                    "131I therapy to shrink the cyst",
                    "FNA of cyst fluid alone for routine cancer screening",
                ],
                0,
                "Purely cystic nodules are so rarely malignant that FNA is not indicated for diagnostic purposes.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Importantly, purely cystic nodules are so rarely malignant that FNA is not indicated for diagnostic purposes.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Nodular disease evaluation",
                "A multinodular gland has three nodules ≥1 cm. The largest is 2.2 cm. How should malignancy risk be assessed?",
                [
                    "Evaluate each clinically relevant nodule separately—not only the dominant nodule",
                    "Biopsy only the largest nodule because cancer risk is proportional to size alone",
                    "Assume multinodularity excludes cancer and observe all",
                    "Measure serum Tg on all patients to triage biopsy",
                ],
                0,
                "With multiple nodules, cancer rate per patient equals solitary nodule risk; each nodule needs separate evaluation.",
                ref(
                    "The Approach to Thyroid Nodular Disease",
                    "Importantly, when multiple nodules are present, each must be separately evaluated because the dominant (largest) nodule is not solely representative of the thyroid cancer risk.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Nodular disease evaluation",
                "A 45-year-old man has a 1.6-cm thyroid nodule. TSH is 3.8 mU/L (upper normal). How does sex affect pretest malignancy risk?",
                [
                    "Men carry higher estimated malignancy risk (~20–30%) than women (~10–20%)",
                    "Sex does not influence thyroid cancer risk at all",
                    "Women have twice the malignancy risk of men for any nodule",
                    "Male sex excludes the need for FNA regardless of sonography",
                ],
                0,
                "Validated risk tables show higher baseline malignancy estimates in men than women for new nodules.",
                ref(
                    "The Approach to Thyroid Nodular Disease",
                    "Characteristics that are associated with a higher risk for malignancy include young age (under approximately 45 years), male sex, a history of external neck radiation during childhood or adolescence, total-body radiation for bone marrow transplant, and rapid nodule growth or persistent changes in speaking, breathing, or swallowing (Table 12.2).",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Thyroid scintigraphy",
                "A patient has a 2-cm nodule with suppressed TSH and focal 123I uptake while the remainder of the gland is cold. Next step?",
                [
                    "Treat as almost certainly benign autonomous nodule; scintigraphy can exclude malignancy here",
                    "Proceed directly to total thyroidectomy without further testing",
                    "Order FDG-PET because all cold nodules are malignant",
                    "Start high-dose levothyroxine suppression",
                ],
                0,
                "Hot nodules with suppressed extranodular uptake are rarely malignant—the classic scenario where scintigraphy excludes cancer.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "These lesions are typically associated with a suppressed serum TSH level. They account for fewer than 5% to 10% of thyroid nodules and are almost invariably benign.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Fine-needle aspiration",
                "FNA returns Bethesda II (benign) for a 1.5-cm intermediate-suspicion nodule. What counseling is most accurate?",
                [
                    "False-negative risk is low (~1–5%) with clinical and sonographic follow-up",
                    "Benign cytology proves absence of cancer forever—no follow-up needed",
                    "Benign cytology mandates completion thyroidectomy",
                    "Repeat FNA weekly until malignant",
                ],
                0,
                "Benign Bethesda results are highly accurate with low false-negative and mortality risk on long follow-up.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "Similarly, a benign result should be viewed as highly accurate because data confirmed a low risk (~1%–5%) of false-negative results and negligible mortality risk from false-negative aspirates during an 8.5-year follow-up.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Molecular testing",
                "Bethesda III cytology on an otherwise healthy 40-year-old. Molecular testing returns benign (high NPV). Best management?",
                [
                    "Observation without surgery because negative molecular result parallels benign cytology risk",
                    "Total thyroidectomy regardless of molecular result",
                    "External beam radiation to the nodule",
                    "Routine calcitonin screening replaces molecular testing",
                ],
                0,
                "Molecular tests with high negative predictive value can avoid surgery in indeterminate nodules when benign.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "In most cases of a healthy patient with Bethesda class III or IV cytology, molecular testing is endorsed because of its ability to substantially improve preoperative cancer risk assessment and modify clinical care, especially when a negative (benign) result is obtained.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Nontoxic goiter",
                "An elderly patient with compressive substernal goiter refuses surgery. Which nonoperative option has evidence for volume reduction?",
                [
                    "131I therapy with documented ~40–55% volume reduction over 1–2 years",
                    "Long-term TSH-suppressive levothyroxine—currently recommended standard",
                    "Ethanol ablation of the entire multinodular gland",
                    "Observation only—131I is contraindicated in substernal goiter",
                ],
                0,
                "131I reduces nontoxic goiter volume substantially and MRI shows improved tracheal dimensions even with substernal extension.",
                ref(
                    "Management Options for Patients With Nontoxic Diffuse Goiter and Nodular Thyroid Disease",
                    "In one study, thyroid volume (assessed by ultrasonography) was reduced by 40% after 1 year and 55% after 2 years, with no further reduction thereafter, and 60% of the total reduction occurred within the first 3 months.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "PET imaging",
                "FDG-PET performed for lung cancer shows focal thyroid uptake in a nodule without prior thyroid disease. What is the cancer risk and next step?",
                [
                    "~30–40% malignancy risk; evaluate with thyroid US and FNA if management would change",
                    "Always benign Hashimoto pattern—no further workup",
                    "Immediate total thyroidectomy without cytology",
                    "FDG avidity excludes thyroid cancer",
                ],
                0,
                "Incidental FDG-avid thyroid nodules carry 30–40% cancer risk and warrant US ± FNA when results would alter care.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Although not recommended for the routine evaluation of thyroid nodules, incidental PET-positive nodules have a cancer risk of 30% to 40%.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Papillary thyroid carcinoma",
                "A 35-year-old undergoes total thyroidectomy for 1.8-cm classic PTC confined to the thyroid with two 1-mm nodal micrometastases. ATA risk category?",
                [
                    "Low risk—intrathyroidal disease with ≤5 micrometastases <0.2 cm",
                    "High risk because any nodal disease mandates stage IV",
                    "Intermediate risk solely due to patient age <45",
                    "High risk requiring empiric 200 mCi 131I in all cases",
                ],
                0,
                "Minimal central micrometastases fit ATA low-risk criteria with excellent recurrence prognosis.",
                ref(
                    "Prediction of Papillary Thyroid Carcinoma Recurrence",
                    "Minimal lymph node involvement (i.e., less than three lymph node metastases, each <2 mm) is associated with a low risk of recurrence.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Surgery",
                "A 2.5-cm intrathyroidal PTC without nodes, no radiation history, euthyroid, solitary nodule. Preferred initial operation?",
                [
                    "Thyroid lobectomy alone",
                    "Total thyroidectomy with prophylactic bilateral lateral neck dissection",
                    "Hemithyroidectomy with routine central neck dissection for all tumors >1 cm",
                    "Active surveillance only because all PTCs are <1 cm",
                ],
                0,
                "Tumors >1 cm and <4 cm without high-risk features are appropriately treated with lobectomy.",
                ref(
                    "Surgical Therapy: Selecting Total or Lobectomy for Differentiated Thyroid Cancer",
                    "For a tumor >1 cm and <4 cm without any of the associated features or history, thyroid lobectomy alone should suffice.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Radioiodine therapy",
                "Six weeks after total thyroidectomy for intermediate-risk PTC, unstimulated Tg is 0.4 ng/mL, anti-Tg negative, no structural disease. RAI ablation?",
                [
                    "Not routinely indicated—low Tg and low-risk postoperative status favor observation",
                    "Mandatory 100 mCi 131I for all total thyroidectomy patients",
                    "131I only if CT neck was performed the same week",
                    "Defer all surveillance because Tg is unreliable after surgery",
                ],
                0,
                "Unstimulated Tg <1 ng/mL without antibodies confers favorable prognosis without routine remnant ablation.",
                ref(
                    "Postoperative Disease Status and RAI Decision Making",
                    "Although there is a lack of consensus regarding actionable Tg levels, if RAI is being considered, an unstimulated Tg of <1 ng/mL in the absence of detectable anti-Tg antibodies confers a highly favorable prognosis without RAI ablation,",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Radioiodine therapy",
                "A high-risk DTC patient needs postoperative 131I. Which TSH preparation is preferred in most guidelines?",
                [
                    "Thyroid hormone withdrawal to TSH >30 mIU/L rather than rhTSH for high-risk disease",
                    "Continue levothyroxine and use rhTSH exclusively for all risk groups",
                    "No TSH stimulation is required for therapeutic 131I",
                    "Use liothyronine alone without measuring TSH",
                ],
                0,
                "For ATA high-risk disease, thyroid hormone withdrawal remains preferred preparation for therapeutic RAI in major guidelines.",
                ref(
                    "Preparation for RAI Therapy",
                    "In patients with ATA high-risk disease, thyroid hormone withdrawal remains the preferred preparation for RAI therapy in most major thyroid cancer guidelines.",
                ),
            ),
            mcq(
                f"{p}-q14",
                "Medullary thyroid carcinoma",
                "Calcitonin 850 pg/mL with biopsy-proven MTC before surgery. Essential preoperative step?",
                [
                    "Screen for pheochromocytoma and hyperparathyroidism; test for germline RET",
                    "Start empiric levothyroxine suppression to TSH <0.1",
                    "Therapeutic 131I dosimetry",
                    "Defer genetic testing because all MTC is sporadic",
                ],
                0,
                "All MTC patients need MEN2/RET evaluation and pheochromocytoma screening before thyroidectomy.",
                ref(
                    "Surgical Approach to Medullary Thyroid Cancer",
                    "Patients who present with MTC should be biochemically screened for pheochromocytoma and hyperparathyroidism.",
                ),
            ),
            mcq(
                f"{p}-q15",
                "Medullary thyroid carcinoma",
                "Postoperative MTC: calcitonin and CEA normalize after complete resection. Long-term biochemical recurrence risk?",
                [
                    "Less than 5% biochemical recurrence; structural recurrence even lower",
                    "Nearly 100% recurrence within 1 year regardless of markers",
                    "Calcitonin is useless after thyroidectomy in MTC",
                    "Rising CEA always means medullary microcarcinoma only",
                ],
                0,
                "Biochemical complete response after total resection carries <5% long-term biochemical recurrence risk.",
                ref(
                    "Outcome Prediction for MTC",
                    "Following complete resection, if a biochemical complete response is achieved (i.e., serum calcitonin and CEA levels normalize), the long-term likelihood of biochemical recurrence is less than 5%, and the risk of structural recurrence is even lower.",
                ),
            ),
            mcq(
                f"{p}-q16",
                "Follicular thyroid carcinoma",
                "A resected 3-cm minimally invasive FTC has capsular invasion only, no vascular invasion. Expected nodal recurrence rate at 20 years?",
                [
                    "Around 2%—nodal recurrence is lowest among differentiated carcinomas",
                    "50%—FTC routinely spreads to cervical nodes like PTC",
                    "0% because FTC never recurs",
                    "90% unless prophylactic bilateral neck dissection performed",
                ],
                0,
                "Typical FTC rarely involves nodes; nodal recurrence rate at 20 years is about 2%.",
                ref(
                    "Risk of Follicular Thyroid Carcinoma Recurrence and Mortality",
                    "Nodal metastases are rare in typical FTC, and the nodal recurrence rate at 20 postoperative years is the lowest among differentiated thyroid carcinoma, being around 2%.",
                ),
            ),
            mcq(
                f"{p}-q17",
                "Anaplastic thyroid carcinoma",
                "A 68-year-old has rapidly enlarging fixed neck mass; FNA suggests ATC. PET/CT shows no distant disease but tracheal invasion. First priority?",
                [
                    "Immediate multidisciplinary evaluation including resectability assessment and molecular testing",
                    "Observation for 6 months to confirm diagnosis",
                    "131I ablation as primary therapy",
                    "Levothyroxine suppression to TSH <0.1 mU/L",
                ],
                0,
                "ATC requires urgent multidisciplinary care; PET/CT staging and assessment for R0/R1 resection are critical.",
                ref(
                    "Presenting Features of ATC",
                    "Given the frequency of distant metastasis in ATC, PET/CT imaging is considered essential in the staging workup.",
                ),
            ),
            mcq(
                f"{p}-q18",
                "Long-term follow-up",
                "After total thyroidectomy and RAI, suppressed Tg is 0.1 ng/mL, US negative. Response category and follow-up intensity?",
                [
                    "Excellent response—decrease follow-up intensity and relax TSH suppression",
                    "Structural incomplete response requiring immediate neck dissection",
                    "Biochemical incomplete response mandating empiric 200 mCi 131I",
                    "Indeterminate response requiring PET every month",
                ],
                0,
                "Suppressed Tg <0.2 ng/mL with negative imaging defines excellent response with low recurrence and mortality.",
                ref(
                    "Long-Term Follow-Up of Patients With Thyroid Cancer After Initial Therapy",
                    "However, with the development of new ultrasensitive assays, the definition of excellent response to therapy can be established with the suppressed thyroglobulin value of less than 0.2 ng/mL.",
                ),
            ),
            mcq(
                f"{p}-q19",
                "RAI-refractory disease",
                "Tg-positive DTC with negative diagnostic 131I scan and FDG-avid mediastinal nodes. Best characterization?",
                [
                    "RAI-refractory disease—FDG avidity predicts poor RAI responsiveness and guides systemic therapy",
                    "Patient remains RAI-sensitive because Tg is elevated",
                    "Benign inflammatory nodes—no further imaging",
                    "Medullary thyroid carcinoma until proven otherwise",
                ],
                0,
                "Discordant FDG-avid, non-iodine-avid metastases determine unsuitability for further RAI and inform prognosis.",
                ref(
                    "Positron Emission Tomography",
                    "The presence of discordant [18F]FDG avid/non-iodine avid metastases can also determine the suitability or otherwise for RAI therapy.",
                ),
            ),
            mcq(
                f"{p}-q20",
                "Targeted therapy",
                "Progressive RAI-refractory PTC without actionable fusion; disease progression within 12 months. First-line systemic therapy?",
                [
                    "Lenvatinib or sorafenib multikinase inhibitor therapy",
                    "Immediate total thyroidectomy",
                    "High-dose 131I regardless of uptake",
                    "Levothyroxine withdrawal alone",
                ],
                0,
                "Without biomarker-directed options, MKI therapy with lenvatinib or sorafenib is indicated for progressive RAI-refractory DTC.",
                ref(
                    "First-Line Multikinase Inhibitor Therapy for DTC",
                    "For patients with progressive RAI-refractory DTC whose tumor does not harbor an actionable biomarker linked to a regulatory-approved first-line therapy, multikinase inhibitor (MKI) therapy with either lenvatinib or sorafenib is indicated in the first-line setting.",
                ),
            ),
            mcq(
                f"{p}-q21",
                "Targeted therapy",
                "RAI-refractory DTC harbors an NTRK fusion. Preferred first-line systemic approach?",
                [
                    "TRK inhibitor (larotrectinib or entrectinib) over multikinase inhibitor",
                    "Sorafenib because NTRK fusions are RAI-sensitive",
                    "Chemotherapy with CHOP regimen",
                    "Observation only—NTRK fusions are benign",
                ],
                0,
                "NTRK-fusion-positive RAI-refractory DTC favors gene-specific TRK inhibitor therapy in the first line.",
                ref(
                    "Gene-Specific Therapy for DTC",
                    "In patients with RAI-refractory DTC harboring actionable oncogenic driver alterations involving NTRK or RET fusions, gene-specific therapy is generally favored over MKIs in the first line.",
                ),
            ),
            mcq(
                f"{p}-q22",
                "Anaplastic thyroid carcinoma",
                "Unresectable BRAF V600E-mutant ATC without distant metastases. Emerging neoadjuvant approach with best reported downstaging?",
                [
                    "Dabrafenib plus trametinib to enable surgery followed by chemoradiotherapy",
                    "131I remnant ablation",
                    "Levothyroxine suppression alone",
                    "Ethanol ablation of the primary tumor",
                ],
                0,
                "Case series show BRAF/MEK inhibition can shrink unresectable ATC sufficiently to permit surgery and chemoradiation.",
                ref(
                    "Advanced Multidisciplinary Care for ATC",
                    "An encouraging case series has been reported involving six patients presenting with unresectable ATC treated with the BRAF and MEK inhibitors, dabrafenib plus trametinib.",
                ),
            ),
            mcq(
                f"{p}-q23",
                "Imaging",
                "CT neck with iodinated contrast is planned before radioiodine therapy. Minimum interval before 131I administration?",
                [
                    "At least 4–6 weeks to avoid impaired RAI uptake",
                    "No interval required—contrast enhances RAI avidity",
                    "24 hours only",
                    "CT contrast permanently contraindicates all thyroid cancer treatment",
                ],
                0,
                "Iodinated CT contrast should precede radioiodine by at least 4–6 weeks to avoid uptake interference.",
                ref(
                    "Computed Tomography",
                    "Because of the necessity of infusing iodine-containing contrast agents for CT scanning of the neck and mediastinum, CT should be performed at least 4 to 6 weeks before any administration of radioiodine.",
                ),
            ),
            mcq(
                f"{p}-q24",
                "Calcitonin screening",
                "Routine serum calcitonin in all thyroid nodule patients is:",
                [
                    "Not cost-effective due to false positives and rarity of unsuspected MTC",
                    "Mandatory in every nodule evaluation per standard practice",
                    "Superior to FNA for all differentiated cancers",
                    "Required before any US examination",
                ],
                0,
                "Routine calcitonin screening is not recommended in initial nodular evaluation because of cost and false-positive burden.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "because of the rarity of unsuspected MTC, the high frequency of false-positive results that often prompt further workup or thyroidectomy, and the unknown clinical relevance of medullary microcarcinomas (<1 cm), it is neither cost-effective nor necessary to measure serum calcitonin levels in the initial evaluation of patients with nodular thyroid disease.",
                ),
            ),
            mcq(
                f"{p}-q25",
                "Active surveillance",
                "A 1.5-cm low-risk micropapillary carcinoma in an elderly comorbid patient. Evidence-supported option?",
                [
                    "Active surveillance with intervention only if progression—similar outcomes to immediate surgery in selected studies",
                    "Mandatory total thyroidectomy with prophylactic RAI",
                    "External beam radiation as first-line curative therapy",
                    "High-dose methimazole until TSH normalizes",
                ],
                0,
                "Active surveillance is proposed for low-risk small PTC to avoid surgical morbidity, with similar outcomes in systematic reviews for tumors <1 cm.",
                ref(
                    "Active Surveillance of Thyroid Malignancy",
                    "Given the indolent nature of many (especially small, <1 cm) PTCs, active surveillance, which involves close monitoring with intervention only if there is disease progression, has been proposed as a viable management option for low-risk PTC.",
                ),
            ),
            mcq(
                f"{p}-q26",
                "Hürthle cell carcinoma",
                "Metastatic oncocytic carcinoma treated with 131I. Expected iodine avidity compared with other DTC?",
                [
                    "Much lower—only ~14% of metastatic OCA cases showed 131I avidity",
                    "Universal avidity like classic papillary cancer",
                    "OCA never metastasizes so avidity is irrelevant",
                    "Higher avidity than medullary carcinoma on FDOPA PET",
                ],
                0,
                "Metastatic oncocytic carcinoma demonstrates poor RAI avidity relative to other differentiated histologies.",
                ref(
                    "Risk of Recurrence and Mortality",
                    "In a series including 22 patients with metastatic OCA treated with 131I, 131I avidity was present in only 13.6% of cases, a rate that was lower compared to all other DTC histology studies.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "Ultrasonography",
                "TIRADS and similar tiered ultrasound systems improve interobserver agreement in thyroid nodule risk assessment.",
                True,
                "Published research supports systematic sonographic classification to improve agreement and guide FNA decisions.",
                ref(
                    "Ultrasonography",
                    "These classification systems have been shown to improve interobserver agreement.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Nodular disease",
                "The presence of multiple thyroid nodules reduces the per-patient probability of thyroid cancer compared with a solitary nodule.",
                False,
                "Cancer rate per patient remains similar because risk per nodule decreases proportionally with nodule number.",
                ref(
                    "The Approach to Thyroid Nodular Disease",
                    "Therefore, the overall cancer rate per patient is the same in those with multiple nodules as in those with a solitary nodule.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Nodular disease",
                "Serum thyroglobulin measurement is recommended in the initial diagnostic evaluation of all thyroid nodules.",
                False,
                "Overlap between benign and malignant Tg levels limits utility in initial nodular workup.",
                ref(
                    "The Evaluation of Patients With Nodular Disease",
                    "Therefore, the measurement of serum Tg levels is not useful in the initial workup of nodular thyroid disease.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Fine-needle aspiration",
                "Bethesda malignant (VI) papillary carcinoma cytology has near-100% sensitivity and specificity when read by experienced cytopathologists.",
                True,
                "Characteristic nuclear features of PTC on FNA are reliable when interpreted by experienced pathologists.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "The diagnosis of PTC (Bethesda category: malignant) by FNA on the basis of characteristic nuclear changes is both reliable and accurate, with sensitivity and specificity both approaching 100%, provided that these changes are evaluated by an experienced cytopathologist.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Nontoxic goiter",
                "Long-term levothyroxine TSH-suppressive therapy is currently recommended to shrink sporadic nontoxic goiters.",
                False,
                "Risks to bone and heart outweigh benefits; TSH-suppressive therapy is not currently recommended.",
                ref(
                    "Management Options for Patients With Nontoxic Diffuse Goiter and Nodular Thyroid Disease",
                    "For these reasons, and in balancing risks and benefits, TSH-suppressive therapy with levothyroxine therapy is not currently recommended.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Papillary thyroid carcinoma",
                "BRAF V600E mutation alone is an independent predictor of mortality independent of tumor size and stage.",
                False,
                "BRAF V600E correlates with recurrence risk but has not proven independent mortality prediction beyond tumor features.",
                ref(
                    "Prediction of Papillary Thyroid Carcinoma Recurrence",
                    "However, despite correlating with a greater risk for mortality, thus far, studies have not found a BRAF V600E mutation alone to be predictive independent of tumor features.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Follicular thyroid carcinoma",
                "Cervical lymph node metastases are common at presentation in typical follicular thyroid carcinoma.",
                False,
                "Nodal metastases are exceptional in FTC and should prompt alternate diagnoses.",
                ref(
                    "Presenting Features of Follicular Thyroid Carcinoma",
                    "Most patients with FTC present with a painless thyroid nodule, with or without background thyroid nodularity, and they rarely (2%–8%) have clinically evident lymphadenopathy at presentation.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Radioiodine therapy",
                "131I therapy has no role in anaplastic thyroid carcinoma, medullary thyroid carcinoma, or thyroid lymphoma.",
                True,
                "Non-follicular-cell-derived malignancies do not concentrate therapeutic iodine.",
                ref(
                    "ATA Recurrence Risk Stratification to Guide Postoperative RAI Decision Making",
                    "131I ablation therapy has no role in the management of patients with ATC, MTC, or thyroid lymphoma.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Medullary thyroid carcinoma",
                "Up to 6% of apparently sporadic MTC cases may harbor unsuspected germline RET mutations.",
                True,
                "Germline RET testing is needed in every MTC patient because familial cases can be missed clinically.",
                ref(
                    "Molecular Pathogenesis",
                    "Of note, germline RET mutations have been identified in up to 6% of apparently sporadic MTCs, highlighting the need for determination of germline RET status in every patient diagnosed with MTC.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Anaplastic thyroid carcinoma",
                "Long-term survival in anaplastic thyroid carcinoma is possible only after R0 or R1 resection in selected patients.",
                True,
                "Resectability with negative or microscopically positive margins is the strongest survival predictor in ATC.",
                ref(
                    "Risk of Recurrence and Mortality",
                    "A number of studies have shown that survival is possible only when patients have undergone an R0 or R1 surgery with complete resection with negative microscopic margins, or all gross tumor is resected, but margins are microscopically positive, respectively.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Long-term follow-up",
                "Stimulated thyroglobulin testing routinely adds prognostic information beyond ultrasensitive suppressed Tg in most follow-up patients.",
                False,
                "With ultrasensitive assays, stimulated Tg usually provides no additional prognostic information.",
                ref(
                    "Long-Term Follow-Up of Patients With Thyroid Cancer After Initial Therapy",
                    "For most patients, stimulated thyroglobulin values provide no additional prognostic information.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Targeted therapy",
                "Lenvatinib is generally preferred over sorafenib as first-line MKI for progressive RAI-refractory DTC based on longer PFS and higher response rates.",
                True,
                "SELECT showed superior PFS and ORR with lenvatinib; experts generally favor it over sorafenib absent head-to-head data.",
                ref(
                    "First-Line Multikinase Inhibitor Therapy for DTC",
                    "Although there is no head-to-head comparison of sorafenib to lenvatinib in patients with progressive RAI-refractory DTC, experts generally agree that lenvatinib is the preferred first-line MKI, given the longer PFS benefit and higher ORR seen with lenvatinib.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Thyroid cancer epidemiology",
                "Mortality attributable to thyroid cancer remains very low despite rising incidence.",
                True,
                "Incidence has increased but thyroid cancer mortality remains very low.",
                ref(
                    "The Approach to Thyroid Nodular Disease",
                    "Regardless, the mortality rate attributable to thyroid cancer remains very low.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Ultrasonography",
                "Assertion: Neck ultrasonography should include regional lymph node compartments when evaluating thyroid cancer.",
                "Reason: Thyroid nodules smaller than 2 mm cannot be detected by ultrasound.",
                2,
                "Assertion is true; reason is false—US detects nodules as small as 2 mm, but nodal evaluation is still required.",
                ref(
                    "Ultrasonography",
                    "Imaging of patients with thyroid nodules and during follow-up of thyroid cancer should also include evaluation of the regional neck lymph node compartments, with the goal of identifying enlarged and pathologic nodes.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Nodular disease",
                "Assertion: A functional hot thyroid nodule on scintigraphy is rarely malignant.",
                "Reason: Almost all malignant nodules are hyperfunctioning on scintigraphy.",
                2,
                "Assertion is true; reason is false—most malignant nodules are hypofunctioning (cold), not hot.",
                ref(
                    "Nuclear Medicine Imaging",
                    "Almost all malignant nodules are hypofunctioning, but more than 80% to 85% of benign nodules are also nonfunctioning.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Fine-needle aspiration",
                "Assertion: US-guided FNA reduces nondiagnostic sampling compared with palpation alone.",
                "Reason: FNA is contraindicated for solid thyroid nodules because of high complication rates.",
                2,
                "Assertion is true; reason is false—FNA is safe, standard care, and US guidance improves adequacy.",
                ref(
                    "Ultrasonography",
                    "Sonography is also the standard modality for guiding FNAB of most thyroid nodules and cervical lymph nodes, demonstrating improved accuracy and a reduction in nondiagnostic specimens.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Molecular testing",
                "Assertion: Molecular testing can reduce unnecessary surgery for Bethesda III nodules.",
                "Reason: All indeterminate nodules must proceed directly to total thyroidectomy without further testing.",
                2,
                "Assertion is true; reason is false—molecular tests with high NPV can support observation over surgery.",
                ref(
                    "Thyroid Nodule Fine-Needle Aspiration",
                    "Historically, surgical intervention was commonly recommended for nodules with SFN/FN or AUS/FLUS cytologic findings, although the majority of patients have benign disease.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Papillary thyroid carcinoma",
                "Assertion: Most patients with PTC have excellent disease-specific survival.",
                "Reason: PTC is the least common thyroid malignancy worldwide.",
                2,
                "Assertion is true; reason is false—PTC is the most common thyroid malignancy, not the least.",
                ref(
                    "Papillary Thyroid Carcinoma",
                    "As the most common thyroid malignancy, PTC constitutes 50% to 90% of DTCs worldwide.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Surgery",
                "Assertion: Total thyroidectomy is generally indicated when differentiated thyroid cancer exceeds 4 cm.",
                "Reason: Tumors larger than 4 cm are always benign follicular adenomas.",
                2,
                "Assertion is true per surgical guidelines; reason is false—large tumors warrant more extensive surgery, not benign assumption.",
                ref(
                    "Surgical Therapy: Selecting Total or Lobectomy for Differentiated Thyroid Cancer",
                    "Evidence of multinodular disease, local invasion, metastatic disease, history of head and neck irradiation, current hypothyroidism, strong family history of thyroid cancer, or tumor >4 cm generally warrants a total thyroidectomy (Table 12.5).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Radioiodine therapy",
                "Assertion: Remnant ablation with 131I is no longer routinely recommended for all low-risk differentiated thyroid cancer patients.",
                "Reason: Neck ultrasound and high-sensitivity thyroglobulin on levothyroxine can suffice for postoperative surveillance.",
                0,
                "Both true—surveillance without ablation is acceptable for low-risk disease when Tg and US are used.",
                ref(
                    "131I and the Role of RAI Administration",
                    "This is no longer routinely recommended because disease surveillance may be satisfactorily accomplished without RAI ablation using neck US and high-sensitivity Tg (with Tg antibody) measurements while the patient is on thyroid hormone therapy.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Medullary thyroid carcinoma",
                "Assertion: Pheochromocytoma must be excluded before thyroidectomy for MTC.",
                "Reason: MTC never coexists with other endocrine neoplasia syndromes.",
                2,
                "Assertion is true; reason is false—MEN2-associated MTC frequently coexists with pheochromocytoma.",
                ref(
                    "Surgical Approach to Medullary Thyroid Cancer",
                    "Any pheochromocytoma should be surgically removed before thyroidectomy.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Anaplastic thyroid carcinoma",
                "Assertion: ATC accounts for a minority of thyroid cancers but a large share of thyroid cancer deaths.",
                "Reason: ATC has a 5-year disease-specific survival exceeding 80%.",
                2,
                "Assertion is true; reason is false—ATC 5-year survival is <15%.",
                ref(
                    "Risk of Recurrence and Mortality",
                    "Despite the rarity of ATC, accounting for less than 2% of all thyroid tumors, ATC is responsible for up to 40% of all thyroid cancer deaths.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Long-term follow-up",
                "Assertion: Excellent response to therapy permits less frequent follow-up and reduced TSH suppression.",
                "Reason: Excellent response is defined only by stimulated thyroglobulin >10 ng/mL.",
                2,
                "Assertion is true; reason is false—excellent response requires low suppressed Tg, not high stimulated Tg.",
                ref(
                    "Long-Term Follow-Up of Patients With Thyroid Cancer After Initial Therapy",
                    "An excellent response to therapy should lead to an early decrease in the intensity and frequency of follow-up and the degree of TSH suppression because these patients do exceptionally well, with essentially no mortality and very low recurrence rates.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Targeted therapy",
                "Assertion: Biomarker testing should precede systemic therapy in RAI-refractory differentiated thyroid cancer.",
                "Reason: RAI-refractory tumors never harbor actionable driver mutations.",
                2,
                "Assertion is true; reason is false—BRAF, RET, NTRK, and ALK alterations are common and targetable.",
                ref(
                    "Systemic Therapy for RAI-Refractory DTC",
                    "Oncogenic driver alterations are often present in RAI-refractory DTC and include BRAFV600E mutations and RET, NTRK1, NTRK3, and ALK fusions.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Staging",
                "Assertion: AJCC eighth edition raises the age threshold defining higher mortality risk in differentiated thyroid cancer to 55 years.",
                "Reason: Age is irrelevant to differentiated thyroid cancer staging in all editions.",
                2,
                "Assertion is true; reason is false—age dichotomy at 55 years is central to eighth edition staging.",
                ref(
                    "Classification and Staging of Thyroid Cancer",
                    "The age criterion for defining high-risk disease has been raised from 45 years to 55 years.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "12",
        "title": "Nontoxic Diffuse Goiter Nodular Thyroid Disorders and Thyroid Malignancies",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Erik K. Alexander, Megan R. Haymart, David A. Pattison, Lori J. Wirth, Martha A. Zeiger",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_12_Nontoxic_Diffuse_Goiter_Nodular_Thyroid_Disorders_and_Thyroid_Malignancies.md",
        "items": items,
    }


MODULES = {OUT_NAME: build}


def write_module(filename: str, data: dict) -> tuple[Path, Path | None]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    master_path: Path | None = None
    if MASTER_DATA.exists():
        MASTER_DATA.mkdir(parents=True, exist_ok=True)
        master_path = MASTER_DATA / filename
        shutil.copy2(portal_path, master_path)
    return portal_path, master_path


def main() -> None:
    for filename, builder in MODULES.items():
        data = builder()
        portal_path, master_path = write_module(filename, data)
        counts: dict[str, int] = {}
        for item in data["items"]:
            counts[item["type"]] = counts.get(item["type"], 0) + 1
        notes = counts.get("note", 0)
        wh = sum(
            1
            for i in data["items"]
            if i["type"] == "note" and i.get("title", "").startswith(("Why", "How"))
        )
        print(f"Wrote {portal_path} ({len(data['items'])} items, {counts}, Why/How {wh}/{notes})")
        if master_path:
            print(f"  Copied to {master_path}")
        else:
            print(f"  Skipped copy — {MASTER_DATA} not found")


if __name__ == "__main__":
    main()
