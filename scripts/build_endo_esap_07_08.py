#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-07 and e21-08."""
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


def build_chapter_07() -> dict:
    p = "e21-07"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Pheochromocytoma screening",
                "Why elevated plasma normetanephrine often misleads clinicians",
                "Clinicians frequently test for pheochromocytoma, but because of assay false positives and disease rarity, 97% of patients with elevated plasma normetanephrine do not have a tumor—driving costly downstream workup and occasional surgical misadventures.",
                ref(
                    "Significance of the Clinical Problem",
                    "because of the false-positive rate of plasma normetanephrine and the rarity of pheochromocytoma, 97% of patients with elevated plasma normetanephrine do not have a pheochromocytoma.",
                ),
            ),
            note(
                f"{p}-n2",
                "CT attenuation",
                "How unenhanced CT attenuation can rule out pheochromocytoma before biochemistry",
                "Among 376 histologically confirmed pheochromocytomas with unenhanced CT data, 374 had attenuation >10 HU (99.5%). An incidentaloma at 1.2 HU cannot be pheochromocytoma—skip biochemical testing and avoid false-positive metanephrine cascades.",
                ref(
                    "Case 1",
                    "among the 376 pheochromocytomas for which unenhanced CT attenuation data were available, 374 had an attenuation value greater than 10 HU (99.5%).",
                ),
            ),
            note(
                f"{p}-n3",
                "Primary aldosteronism",
                "Why primary aldosteronism is systematically underdiagnosed",
                "Despite affecting 5%–10% of hypertensive adults, primary aldosteronism is rarely considered or tested. Delayed diagnosis drives suboptimal quality of life and preventable cardiac and renal morbidity.",
                ref(
                    "Significance of the Clinical Problem",
                    "Even though primary aldosteronism affects 5% to 10% of all persons with hypertension, clinicians do not think about it very much and do not test for it.",
                ),
            ),
            note(
                f"{p}-n4",
                "Primary aldosteronism screening",
                "How to perform case-detection testing for primary aldosteronism",
                "Use a morning venipuncture for plasma aldosterone concentration and plasma renin activity or plasma renin concentration. Testing can be done without stopping most antihypertensive medications.",
                ref(
                    "Primary Aldosteronism",
                    "Case-detection testing is performed with a morning venipuncture for the measurement of plasma aldosterone concentration and plasma renin activity or plasma renin concentration.",
                ),
            ),
            note(
                f"{p}-n5",
                "Hypokalemia trap",
                "Why normal serum potassium does not exclude primary aldosteronism",
                "Hypokalemia is present in only 28% of patients with primary aldosteronism; absence of hypokalemia is meaningless for case detection. All hypertensive patients are potential candidates.",
                ref(
                    "Primary Aldosteronism",
                    "Because hypokalemia is present in only 28% of patients with primary aldosteronism, all patients with hypertension are potential candidates for this disorder.",
                ),
            ),
            note(
                f"{p}-n6",
                "Aldosterone toxicity",
                "Why cardiovascular harm in primary aldosteronism exceeds blood pressure alone",
                "Meta-analysis shows increased stroke, coronary disease, atrial fibrillation, heart failure, diabetes, metabolic syndrome, and LVH versus essential hypertension—aldosterone-specific toxicity beyond hypertension.",
                ref(
                    "Primary Aldosteronism",
                    "Thus, the cardiovascular toxicity in primary aldosteronism extends beyond hypertension; there is an aldosterone-specific toxicity.",
                ),
            ),
            note(
                f"{p}-n7",
                "Pheochromocytoma genetics",
                "How to approach germline testing in pheochromocytoma",
                "Genetic testing should be considered in all patients, especially with paraganglioma, bilateral disease, positive family history, age <60 years, or syndromic features. Counseling is recommended because results affect relatives.",
                ref(
                    "Pheochromocytoma",
                    "Genetic testing should be considered in all patients with pheochromocytoma, especially if a patient has 1 or more of the following: paraganglioma; bilateral adrenal pheochromocytoma",
                ),
            ),
            note(
                f"{p}-n8",
                "Familial PA",
                "When to consider genetic testing for familial primary aldosteronism",
                "Consider familial forms when PA is diagnosed before age 20 or in multiple family members. Nearly all familial cases have bilateral adrenal disease and would not be cured by unilateral adrenalectomy.",
                ref(
                    "Primary Aldosteronism",
                    "Familial primary aldosteronism should be considered when primary aldosteronism is diagnosed before age 20 years or when primary aldosteronism is diagnosed in more than one family member.",
                ),
            ),
            note(
                f"{p}-n9",
                "Detection modes",
                "Changing patterns of pheochromocytoma discovery",
                "In a recent Mayo series (2005–2016), 61% were adrenal incidentalomas and 12% detected via genetic/family testing—contrasting with older series where paroxysmal symptoms drove 90% of diagnoses.",
                ref(
                    "Pheochromocytoma",
                    "In the most recent series of patients with pheochromocytoma reported from Mayo Clinic (271 patients from 2005 to 2016), 61% were detected as adrenal incidentalomas and 12% were detected because of genetic or family testing.",
                ),
            ),
            note(
                f"{p}-n10",
                "Biochemical interference",
                "How medications interfere with catecholamine testing",
                "Tricyclic antidepressants (including cyclobenzaprine) and many psychoactive agents interfere most with urinary fractionated catecholamines/metanephrines—taper ≥4 weeks when possible. Antihypertensives and acetaminophen do not interfere with modern assays.",
                ref(
                    "Pheochromocytoma",
                    "Tricyclic antidepressants (TCAs) interfere most frequently with the interpretation of 24-hour urinary fractionated catecholamines and metanephrines.",
                ),
            ),
            note(
                f"{p}-n11",
                "PA medication myths",
                "Why antihypertensives need not be stopped before primary aldosteronism screening",
                "Patients can remain on any blood pressure medication—including spironolactone and eplerenone—during case-detection testing. Endocrinologists have created an unnecessary barrier by overemphasizing medication washout.",
                ref(
                    "Case 5",
                    "Patients can be on any sodium diet and any blood pressure medication, including spironolactone and eplerenone, when performing case-detection testing for primary aldosteronism.",
                ),
            ),
            note(
                f"{p}-n12",
                "Synonymous VHL variant",
                "Why a synonymous VHL variant caused familial pheochromocytoma",
                "A heterozygous synonymous VHL c.414A>G (p.Pro138Pro) promoted exon 2 skipping despite no amino-acid change—illustrating that 'silent' variants are not always neutral and can require research-grade sequencing.",
                ref(
                    "The Genetic Mystery Solved",
                    "the c.414A>G VHL variant was found to promote exon 2 skipping.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — CT attenuation",
                "Two 50-year-old women have nearly identical 2.8-cm right adrenal incidentalomas. Patient 1 has unenhanced attenuation 1.2 HU; Patient 2 has attenuation consistent with >10 HU. Who should be screened biochemically for pheochromocytoma?",
                [
                    "Patient 1 only",
                    "Patient 2 only",
                    "Both patients",
                    "Neither patient",
                ],
                1,
                "Attenuation <10 HU effectively excludes pheochromocytoma; biochemical testing is unnecessary for Patient 1 and indicated for Patient 2.",
                ref(
                    "Case 1",
                    "Answer: B) Patient 2",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — prebiochemical pheochromocytoma",
                "A 49-year-old man has a lipid-poor, vascular 1.6-cm left adrenal mass (40.5 HU) with normal plasma and 24-hour urine metanephrines/catecholamines. Do normal biochemistry results exclude pheochromocytoma?",
                [
                    "Yes — normal metanephrines exclude the diagnosis",
                    "No — small tumors may be prebiochemical",
                    "Only if repeat testing is normal in 6 months",
                    "Yes if patient is normotensive",
                ],
                1,
                "Laparoscopic resection proved pheochromocytoma; small lipid-poor vascular masses can secrete below detection until they exceed ~1.5 cm.",
                ref(
                    "Case 2",
                    "Answer: B) No",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — pheochromocytoma genetics",
                "A 49-year-old man (Case 2) undergoes adrenalectomy for pheochromocytoma without syndromic stigmata. Best next step for germline evaluation?",
                [
                    "RET gene testing only",
                    "NF1 gene testing only",
                    "Next-generation sequencing panel for pheochromocytoma/paraganglioma susceptibility genes",
                    "No genetic testing — sporadic unilateral disease",
                ],
                2,
                "Guidelines recommend genetic testing in all pheochromocytoma patients; a multigene NGS panel is the contemporary first-line approach in unselected cases.",
                ref(
                    "Pheochromocytoma",
                    "Genetic testing should be considered in all patients with pheochromocytoma, especially if a patient has 1 or more of the following",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 4 — young hypertension",
                "A 23-year-old woman has new-onset hypertension without hypokalemia. A 35-year-old man has resistant hypertension on three agents, also normokalemic. Who should undergo primary aldosteronism case-detection testing?",
                [
                    "Only the man with resistant hypertension",
                    "Only the woman because of young age",
                    "Both patients",
                    "Neither without hypokalemia",
                ],
                2,
                "70% of primary aldosteronism patients are normokalemic; missing PA in a 23-year-old with new hypertension would be a major diagnostic error.",
                ref(
                    "Case 4",
                    "The lack of hypokalemia is meaningless—70% of patients with primary aldosteronism have a normal serum potassium concentration. Thus, both patients should be tested (Answer C).",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 5 — medications before PA screen",
                "A 56-year-old man on lisinopril, spironolactone, HCTZ, metoprolol, and amlodipine (BP 165/110 mm Hg) is screened for primary aldosteronism. Which medication(s) must be stopped first?",
                [
                    "Spironolactone and ACE inhibitor only",
                    "All antihypertensives — switch to doxazosin and verapamil",
                    "Beta-blocker and thiazide only",
                    "None — testing can proceed on current medications",
                ],
                3,
                "Case-detection can be performed on any antihypertensive regimen including mineralocorticoid receptor antagonists; stopping drugs creates an artificial barrier.",
                ref(
                    "Case 5",
                    "Answer: F) None of the above",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Case 6 — familial PA genetics",
                "A 56-year-old man with primary aldosteronism due to a unilateral aldosterone-producing adenoma is cured by adrenalectomy. Should he have genetic testing for familial hyperaldosteronism?",
                [
                    "Yes — all PA patients need genetic testing",
                    "No — sporadic unilateral APA cured by surgery",
                    "Only if he has hypokalemia",
                    "Only if hypertension persists postoperatively",
                ],
                1,
                "Familial PA is rare and should be considered when diagnosed before age 20 or in multiple family members; bilateral disease is typical and unilateral adrenalectomy would not cure familial forms.",
                ref(
                    "Case 6",
                    "Answer: B) No",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Pheochromocytoma suspicion",
                "Which clinical scenario should raise suspicion for pheochromocytoma?",
                [
                    "Stable essential hypertension in a 65-year-old",
                    "Pressor crisis during anesthesia in a patient with adrenal incidentaloma",
                    "Isolated systolic hypertension with wide pulse pressure",
                    "Mild orthostatic hypotension in an elderly patient",
                ],
                1,
                "Pressor response to anesthesia, surgery, angiography, high-dose corticosteroid, or beta-blocker is a classic pheochromocytoma trigger alongside incidentaloma and familial syndromes.",
                ref(
                    "Pheochromocytoma",
                    "A pressor response to anesthesia, surgery, angiography, high-dose corticosteroid, or β-adrenergic blocker",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Case-detection biochemistry",
                "At Mayo Clinic, the preferred initial case-detection strategy for pheochromocytoma is:",
                [
                    "Plasma fractionated metanephrines alone in all patients",
                    "24-hour urine fractionated metanephrines and catecholamines",
                    "Random serum catecholamines",
                    "MIBG scan before any biochemistry",
                ],
                1,
                "24-hour urine fractionated metanephrines and catecholamines is the most reliable case-detection strategy; plasma metanephrines are added when clinical suspicion is high.",
                ref(
                    "Pheochromocytoma",
                    "At Mayo Clinic, the most reliable case-detection strategy is measuring fractionated metanephrines and catecholamines in a 24-hour urine collection.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Young normotensive PA",
                "A 32-year-old has marked hypokalemia but BP 132/82 mm Hg (baseline ~100/60). What is the best interpretation?",
                [
                    "Hypokalemia cannot be primary aldosteronism without hypertension",
                    "Clinically significant BP rise from baseline may represent early primary aldosteronism",
                    "This pattern excludes adrenal disease",
                    "Only renovascular hypertension explains this",
                ],
                1,
                "Young patients may not meet formal hypertension criteria early in disease because counter-regulatory mechanisms and low baseline pressures mask the aldosterone effect.",
                ref(
                    "Primary Aldosteronism",
                    "Thus, although they do not meet the criteria for hypertension, there is a clinically significant change from baseline",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Genetic counseling",
                "An asymptomatic adult with family history of pheochromocytoma asks for predictive genetic testing. When is testing appropriate?",
                [
                    "Whenever the patient requests it",
                    "Only if an affected relative has a known pathogenic variant",
                    "After a positive plasma metanephrine test",
                    "Only after bilateral adrenalectomy",
                ],
                1,
                "Predictive testing in at-risk relatives requires a known familial pathogenic variant from an affected proband; counseling coordinates cascade testing.",
                ref(
                    "Pheochromocytoma",
                    "An asymptomatic person at risk for disease on the basis of family history of pheochromocytoma or paraganglioma should have genetic testing only if an affected family member has a known pathogenic variant.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Postpartum pheochromocytoma",
                "A postpartum woman develops Takotsubo-pattern cardiomyopathy, elevated troponin, and markedly elevated urinary normetanephrine with a 4.5-cm right adrenal mass. Family history reveals multiple pheochromocytomas. Initial management priority?",
                [
                    "Immediate coronary angioplasty",
                    "Alpha-blockade before beta-blockade and planned adrenalectomy",
                    "Observation until biochemistry normalizes",
                    "Empiric primary aldosteronism workup first",
                ],
                1,
                "Pheochromocytoma can mimic acute coronary syndromes; alpha-blockade (phenoxybenzamine) precedes beta-blockade, with definitive resection after biochemical control.",
                ref(
                    "Case 7",
                    "Treatment with phenoxybenzamine is initiated, and CT of the abdomen detects a 4.5-cm right adrenal mass.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "PA target-organ damage",
                "Compared with essential hypertension, primary aldosteronism is associated with which outcome?",
                [
                    "Lower stroke risk due to younger diagnosis",
                    "Increased atrial fibrillation risk (OR ~3.5 in meta-analysis)",
                    "Reduced LVH due to earlier mineralocorticoid antagonism",
                    "Lower diabetes risk",
                ],
                1,
                "Meta-analysis of 31 studies showed higher stroke, CAD, AF, heart failure, diabetes, metabolic syndrome, and LVH versus essential hypertension.",
                ref(
                    "Primary Aldosteronism",
                    "patients with aldosterone-producing adenomas and bilateral hyperplasia had an increased risk of stroke (odds ratio [OR], 2.58), coronary artery disease (OR, 1.77), atrial fibrillation (OR, 3.52), and heart failure (OR, 2.05).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Secondary hypertension epidemiology",
                "In adults under 40 years with hypertension, approximately what proportion has secondary hypertension?",
                [
                    "About 5%",
                    "About 15%",
                    "About 30%",
                    "More than 50%",
                ],
                2,
                "Secondary hypertension affects >50% of children and ~30% of young adults (<40 years), making targeted endocrine screening especially important in this age group.",
                ref(
                    "Main Conclusions",
                    "More than 50% of children and 30% of young adults (<40 years) have secondary hypertension.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Pheochromocytoma",
                "An adrenal incidentaloma with unenhanced CT attenuation less than 10 HU can still be a pheochromocytoma.",
                False,
                "99.5% of confirmed pheochromocytomas have attenuation >10 HU; values below this threshold effectively exclude the diagnosis.",
                ref(
                    "Case 1",
                    "An adrenal incidentaloma with an unenhanced CT attenuation of 1.2 HU simply cannot be a pheochromocytoma.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Pheochromocytoma",
                "Normal plasma and urine metanephrines always exclude a small pheochromocytoma.",
                False,
                "Small lipid-poor vascular adrenal masses can be prebiochemical until they exceed roughly 1.5 cm in diameter.",
                ref(
                    "Case 2",
                    "all pheochromocytomas are “prebiochemical” when small.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Primary aldosteronism",
                "Hypokalemia is present in most patients with primary aldosteronism.",
                False,
                "Only 28% have hypokalemia; normokalemia does not exclude the diagnosis.",
                ref(
                    "Primary Aldosteronism",
                    "Because hypokalemia is present in only 28% of patients with primary aldosteronism",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Primary aldosteronism",
                "Spironolactone must be discontinued before primary aldosteronism case-detection testing.",
                False,
                "Patients can be tested while on spironolactone, eplerenone, or any antihypertensive regimen.",
                ref(
                    "Case 5",
                    "Patients can be on any sodium diet and any blood pressure medication, including spironolactone and eplerenone, when performing case-detection testing for primary aldosteronism.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Genetics",
                "Genetic testing should be considered in all patients diagnosed with pheochromocytoma.",
                True,
                "Especially with paraganglioma, bilateral disease, family history, age <60, or syndromic features—but consideration applies broadly.",
                ref(
                    "Pheochromocytoma",
                    "Genetic testing should be considered in all patients with pheochromocytoma",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Familial PA",
                "A patient cured of primary aldosteronism by unilateral adrenalectomy at age 56 should routinely receive familial hyperaldosteronism genetic testing.",
                False,
                "Familial PA testing is indicated when diagnosed before age 20 or in multiple family members; sporadic unilateral APA does not warrant routine genetic testing.",
                ref(
                    "Case 6",
                    "Thus, there is no role for genetic testing in the patient described this clinical vignette.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Biochemical testing",
                "With modern HPLC/tandem mass spectrometry assays, antihypertensive medications interfere with plasma metanephrine testing.",
                False,
                "Antihypertensive medications and acetaminophen do not interfere with current assay methodology.",
                ref(
                    "Pheochromocytoma",
                    "with current assay methodology (tandem mass spectrometry, high-performance liquid chromatography), antihypertensive medications and acetaminophen do not interfere with testing.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Epidemiology",
                "Primary aldosteronism affects approximately 5% to 10% of all patients with hypertension.",
                True,
                "Current prevalence estimates support screening a broad hypertensive population, not only hypokalemic or resistant cases.",
                ref(
                    "Primary Aldosteronism",
                    "Current prevalence estimates for primary aldosteronism are 5% to 10% of all patients with hypertension.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "CT screening",
                "Assertion: Adrenal incidentalomas with unenhanced attenuation below 10 HU do not require biochemical pheochromocytoma screening.",
                "Reason: More than 99% of histologically confirmed pheochromocytomas have unenhanced attenuation greater than 10 HU.",
                0,
                "Both statements are true and causally linked—low HU reliably excludes pheochromocytoma.",
                ref(
                    "Case 1",
                    "374 had an attenuation value greater than 10 HU (99.5%).",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Prebiochemical tumors",
                "Assertion: A lipid-poor vascular adrenal mass can harbor pheochromocytoma despite normal metanephrines.",
                "Reason: Pheochromocytomas may be prebiochemical until they reach approximately 1.5 cm diameter.",
                0,
                "Both are true; small tumors secrete below biochemical detection thresholds.",
                ref(
                    "Case 2",
                    "Pheochromocytomas need a “big factory” (typically >1.5 cm in diameter) to be biochemically detectable.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "PA underdiagnosis",
                "Assertion: Primary aldosteronism is frequently missed in clinical practice.",
                "Reason: Clinicians rarely test for a disorder they perceive as uncommon despite 5%–10% prevalence.",
                0,
                "Both true; low testing rates despite substantial population prevalence drive underdiagnosis.",
                ref(
                    "Significance of the Clinical Problem",
                    "clinicians do not think about it very much and do not test for it.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Hypokalemia",
                "Assertion: Normokalemia excludes primary aldosteronism.",
                "Reason: Most patients with primary aldosteronism have hypokalemia at presentation.",
                2,
                "A is false (only 28% are hypokalemic); R is false (most are normokalemic).",
                ref(
                    "Primary Aldosteronism",
                    "Because hypokalemia is present in only 28% of patients with primary aldosteronism",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Aldosterone toxicity",
                "Assertion: Primary aldosteronism confers cardiovascular risk beyond that of blood pressure elevation alone.",
                "Reason: Aldosterone has direct target-organ toxicity independent of hypertension.",
                0,
                "Both true; meta-analysis demonstrates aldosterone-specific toxicity.",
                ref(
                    "Primary Aldosteronism",
                    "there is an aldosterone-specific toxicity.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Familial PA surgery",
                "Assertion: Familial primary aldosteronism is usually cured by unilateral adrenalectomy.",
                "Reason: Nearly all familial cases have bilateral adrenal disease.",
                4,
                "Both false—familial PA is typically bilateral and not cured by unilateral surgery.",
                ref(
                    "Primary Aldosteronism",
                    "In nearly all cases, patients with familial primary aldosteronism have bilateral adrenal disease and would not be cured with unilateral adrenalectomy.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Medication interference",
                "Assertion: Tricyclic antidepressants can cause false-positive urinary catecholamine testing.",
                "Reason: TCAs should be tapered and discontinued at least 4 weeks before testing when clinically feasible.",
                0,
                "Both true; TCAs are the most common biochemical interferent.",
                ref(
                    "Pheochromocytoma",
                    "Treatment with TCAs and antipsychotic agents should be tapered and discontinued at least 4 weeks before testing.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Predictive genetics",
                "Assertion: Asymptomatic relatives should undergo genetic testing for pheochromocytoma predisposition.",
                "Reason: Testing should proceed only when an affected family member has a known pathogenic variant.",
                1,
                "Both true but R does not explain A—predictive testing requires a known familial variant first.",
                ref(
                    "Pheochromocytoma",
                    "should have genetic testing only if an affected family member has a known pathogenic variant.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "7",
        "title": "Diagnosis and Management of Endocrine Hypertension: Deciding Who to Screen for Genetic Causes",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "William F. Young, Jr., MD, MSc.",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_07_Deciding_Who_to_Screen_for_Genetic_Causes.md",
        "items": items,
    }


def build_chapter_08() -> dict:
    p = "e21-08"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "CIRCI physiology",
                "Why serum cortisol may not reflect tissue glucocorticoid sufficiency in critical illness",
                "Tissue resistance to cortisol and reduced CBG/albumin alter total versus free cortisol; serum measurements may not reflect end-organ glucocorticoid status during sepsis and other critical illnesses.",
                ref(
                    "Main Conclusions",
                    "Routine measurements of serum cortisol may not reflect end-organ glucocorticoid sufficiency due to tissue resistance to cortisol and reduced concentrations of the principal carrier proteins for cortisol, corticosteroid-binding globulin (CBG) and albumin.",
                ),
            ),
            note(
                f"{p}-n2",
                "CIRCI definition",
                "How critical illness-related corticosteroid insufficiency is operationally defined",
                "CIRCI is defined as a serum cortisol increment <9 μg/dL (<248 nmol/L) 60 minutes after 250 mcg cosyntropin—though this threshold remains controversial and does not measure tissue glucocorticoid sufficiency.",
                ref(
                    "Definitions",
                    "CIRCI is operationally defined as a serum cortisol increment of less than 9 μg/dL (<248 nmol/L) 60 minutes after administration of 250 mcg cosyntropin.",
                ),
            ),
            note(
                f"{p}-n3",
                "Adrenal insufficiency definition",
                "Conventional adrenal insufficiency versus CIRCI",
                "True adrenal insufficiency shows suboptimal peak cortisol after cosyntropin (e.g., <18 μg/dL at 30 minutes, assay dependent) with ACTH distinguishing primary from secondary forms. CIRCI is a critical-care concept of impaired stress response without classic deficiency.",
                ref(
                    "Definitions",
                    "Adrenal insufficiency is defined as the inability to produce sufficient glucocorticoids and mineralocorticoids for tissue requirements.",
                ),
            ),
            note(
                f"{p}-n4",
                "HPA stress response",
                "How critical illness remodels HPA axis physiology",
                "Sepsis activates the HPA axis via cytokines, reduces cortisol metabolism enzymes, lowers CBG, redirects steroidogenesis toward cortisol, induces tissue glucocorticoid resistance (GR pathway changes), and is worsened by opioids, benzodiazepines, and etomidate.",
                ref(
                    "Critical Illness Stress Response",
                    "Given the complexity of these influences on the HPA axis, especially the variable degree of tissue resistance that accompanies systemic inflammation and the fall in serum binding proteins that alter the relationship between total and free cortisol, serum cortisol concentrations may not reflect tissue glucocorticoid status.",
                ),
            ),
            note(
                f"{p}-n5",
                "Relative adrenal insufficiency",
                "Why a cosyntropin increment below 9 μg/dL defined relative adrenal insufficiency",
                "In Rothwell's septic shock cohort, none of 13 patients with <9 μg/dL ACTH response survived versus 13/19 survivors with higher responses—empirically defining relative adrenal insufficiency.",
                ref(
                    "Critical Illness Stress Response",
                    "Hence, a total plasma cortisol response to cosyntropin, 250 mcg, of less than 9 μg/dL (<248 nmol/L) empirically defines relative adrenal insufficiency.",
                ),
            ),
            note(
                f"{p}-n6",
                "Hydrocortisone dosing",
                "How low-dose hydrocortisone helps septic shock",
                "Seven days of hydrocortisone approximating stress output (200–300 mg daily) shortens vasopressor support; pressor sensitivity to norepinephrine can be restored even when mortality benefit is inconsistent across trials.",
                ref(
                    "Critical Illness Stress Response",
                    "Longer treatment (7 days) with lower-dosage hydrocortisone approximating the normal adrenocortical cortisol output in severe stress (200-300 mg daily) shortens the need for vasopressor support.",
                ),
            ),
            note(
                f"{p}-n7",
                "Annane 2002 trial",
                "Why the Annane 2002 septic shock trial fueled hydrocortisone use",
                "Hydrocortisone plus fludrocortisone improved 28-day mortality in cosyntropin nonresponders (<9 μg/dL increment) but not responders; high etomidate use (72/99 patients) later criticized the generalizability.",
                ref(
                    "Clinical trials",
                    "A 2002 randomized controlled trial of hydrocortisone, 50 mg every 6 hours, and fludrocortisone, 0.05 mg daily, vs placebo revealed a 28-day mortality benefit for treatment in the nonresponders to cosyntropin, 250 mcg",
                ),
            ),
            note(
                f"{p}-n8",
                "CORTICUS trial",
                "How CORTICUS tempered enthusiasm for mortality benefit",
                "CORTICUS (499 patients) showed no 28-day mortality benefit from hydrocortisone 50 mg q6h versus placebo, though shock resolved faster; the trial was under-enrolled and criticized for enrolling less-sick patients.",
                ref(
                    "Clinical trials",
                    "The CORTICUS trial, however, did not reveal any 28-day mortality benefit from hydrocortisone, 50 mg every 6 hours in 499 patients with septic shock",
                ),
            ),
            note(
                f"{p}-n9",
                "Large modern trials",
                "How Venkatesh and Annane 2018 trials inform current practice",
                "Venkatesh (ADRENAL): no 28-day mortality difference but faster shock resolution and shorter ventilation. Annane (APROCCHSS): lower 90-day mortality with hydrocortisone plus fludrocortisone. Both support pressor-sparing benefit.",
                ref(
                    "Clinical trials",
                    "No difference in 28-day mortality was observed, but a 1-day reduction in time to shock resolution (3 vs 4 days) and a 1-day reduction in initial time of mechanical ventilation (5 vs 7 days) was noted",
                ),
            ),
            note(
                f"{p}-n10",
                "Checkpoint inhibitors",
                "Why checkpoint inhibitor hypophysitis requires immediate glucocorticoids",
                "Ipilimumab (CTLA-4 inhibitor) causes hypophysitis in up to 20% of patients. Baseline cortisol and clinical features can be diagnostic; HPA recovery is rare and high-dose steroids do not restore axis function.",
                ref(
                    "Case 1",
                    "Ipilimumab (CTLA-4 inhibitor) produces hypophysitis in up to 20% of patients. HPA axis recovery is rare, and there is no recovery benefit from high-dosage glucocorticoid.",
                ),
            ),
            note(
                f"{p}-n11",
                "Community-acquired pneumonia",
                "How hydrocortisone fits hospitalized community-acquired pneumonia",
                "Hydrocortisone <400 mg daily for 5–7 days is suggested for hospitalized CAP based on 13 trials (12 showing mortality reduction), with hyperglycemia as the principal adverse effect—independent of cosyntropin results during acute illness.",
                ref(
                    "Case 4",
                    "Hydrocortisone at a dosage less than 400 mg daily or the equivalent for 5 to 7 days is suggested for community-acquired pneumonia based on results from 13 trials, 12 of which showed reduced mortality.",
                ),
            ),
            note(
                f"{p}-n12",
                "Free cortisol",
                "Why free cortisol may better reflect illness severity than total cortisol",
                "In sepsis, TNF-α and IL-6 reduce hepatic CBG synthesis and neutrophil elastase cleaves CBG at inflammatory sites; free cortisol increments correlate more closely with illness severity than total cortisol.",
                ref(
                    "Potential for Plasma Free Cortisol and CBG Measurements",
                    "When comparing control patients with patients who have sepsis and septic shock, free cortisol increments correspond to illness severity more closely than total cortisol.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — checkpoint inhibitor",
                "A 58-year-old man on ipilimumab for metastatic melanoma presents with hypotension, postural symptoms, fatigue, and serum cortisol 4 μg/dL. Which statement is true?",
                [
                    "Cosyntropin testing must be completed before any glucocorticoid therapy",
                    "Checkpoint inhibitor-related adrenal insufficiency is likely; give parenteral glucocorticoids without delay",
                    "Most patients recover HPA axis function with high-dose oral steroids",
                    "Current exogenous glucocorticoid therapy explains the presentation",
                ],
                1,
                "Clinical and biochemical features are sufficient for treatment; CTLA-4 inhibitor hypophysitis rarely recovers and high-dose steroids do not restore the axis.",
                ref(
                    "Case 1",
                    "Answer: D) Checkpoint inhibitor-related adrenal insufficiency is the likely cause of the presentation, and parenteral glucocorticoids should be administered without delay",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — septic shock",
                "A 75-year-old man has septic shock refractory to fluids and norepinephrine 2.0 mcg/kg/min. Random cortisol 18 μg/dL; cosyntropin rise from 14 to 17 μg/dL at 60 minutes. Best statement?",
                [
                    "Hydrocortisone is contraindicated because mortality benefit is unproven",
                    "Cosyntropin nonresponse must be documented before hydrocortisone",
                    "CBG measurement is required to guide therapy",
                    "Low-dose IV hydrocortisone (~200 mg daily for 7 days) is warranted on clinical grounds",
                ],
                3,
                "Septic shock unresponsive to resuscitation and vasopressors warrants hydrocortisone regardless of cosyntropin increment; pressor-sparing benefit outweighs risks of a 7-day course.",
                ref(
                    "Case 2",
                    "Answer: E) The clinical circumstances warrant the use of low-dosage hydrocortisone such as intravenous 200 mg daily for 7 days without taper",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 4 — trauma and CAP",
                "Six months after head trauma treated with dexamethasone, a 24-year-old man presents with lobar pneumonia, hypotension, cortisol 16 μg/dL, and low TSH/free T3. Best approach?",
                [
                    "Serum cortisol is adequate — no glucocorticoid indicated",
                    "Start levothyroxine immediately for low TSH/T3",
                    "Prior dexamethasone explains current cortisol — withhold steroids",
                    "Hydrocortisone may be indicated for hospitalized CAP; reassess HPA axis after recovery",
                ],
                3,
                "CAP requiring hospitalization is an indication for short-course low-dose hydrocortisone; thyroid and gonadal abnormalities may reflect acute illness and remote dexamethasone is not the driver.",
                ref(
                    "Case 4",
                    "Answer: E) Hydrocortisone administration may be indicated for the community-acquired pneumonia on clinical grounds alone",
                ),
            ),
            mcq(
                f"{p}-q4",
                "CIRCI definition",
                "A cosyntropin stimulation test in septic shock shows a 60-minute cortisol rise of 7 μg/dL from baseline. How is this classified operationally?",
                [
                    "Normal adrenal reserve",
                    "Primary adrenal insufficiency",
                    "Critical illness-related corticosteroid insufficiency (relative adrenal insufficiency)",
                    "Pituitary Cushing syndrome",
                ],
                2,
                "An increment <9 μg/dL at 60 minutes after 250 mcg cosyntropin operationally defines CIRCI/relative adrenal insufficiency.",
                ref(
                    "Definitions",
                    "CIRCI is operationally defined as a serum cortisol increment of less than 9 μg/dL (<248 nmol/L) 60 minutes after administration of 250 mcg cosyntropin.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Annane 2002",
                "In the 2002 Annane septic shock trial, 28-day mortality benefit with hydrocortisone plus fludrocortisone was seen in which group?",
                [
                    "All patients regardless of cosyntropin response",
                    "Cosyntropin responders only",
                    "Cosyntropin nonresponders (<9 μg/dL increment) only",
                    "Only patients not exposed to etomidate",
                ],
                2,
                "Mortality benefit was confined to nonresponders; responders showed no mortality advantage.",
                ref(
                    "Clinical trials",
                    "revealed a 28-day mortality benefit for treatment in the nonresponders to cosyntropin, 250 mcg (cortisol response at 30 and 60 minutes less than 9 μg/dL [<248 nmol/L]",
                ),
            ),
            mcq(
                f"{p}-q6",
                "CORTICUS",
                "The CORTICUS trial of hydrocortisone in septic shock found:",
                [
                    "Significant 28-day mortality reduction in all patients",
                    "No 28-day mortality benefit but more rapid shock resolution",
                    "Increased 90-day survival with fludrocortisone alone",
                    "Mandatory cosyntropin testing before enrollment improved outcomes",
                ],
                1,
                "CORTICUS showed faster shock resolution without 28-day mortality improvement; it was underpowered and enrolled less-sick patients than planned.",
                ref(
                    "Clinical trials",
                    "did not reveal any 28-day mortality benefit from hydrocortisone, 50 mg every 6 hours in 499 patients with septic shock",
                ),
            ),
            mcq(
                f"{p}-q7",
                "ADRENAL trial",
                "The Venkatesh ADRENAL trial (2018) of continuous hydrocortisone 200 mg/day for 7 days in ventilated septic shock found:",
                [
                    "Lower 28-day mortality versus placebo",
                    "No 28-day mortality difference but shorter shock duration and ventilation time",
                    "Increased bacteremia and fungemia",
                    "Benefit only in cosyntropin nonresponders",
                ],
                1,
                "No mortality difference at 28 days, but 1-day reductions in shock resolution and initial mechanical ventilation without increased infection rates.",
                ref(
                    "Clinical trials",
                    "No difference in 28-day mortality was observed, but a 1-day reduction in time to shock resolution (3 vs 4 days) and a 1-day reduction in initial time of mechanical ventilation (5 vs 7 days) was noted, with no increase in rates of bacteremia or fungemia.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "APROCCHSS trial",
                "The Annane 2018 APROCCHSS trial differed from ADRENAL primarily in that it showed:",
                [
                    "Lower 90-day mortality with hydrocortisone plus fludrocortisone",
                    "Higher infection rates with combination therapy",
                    "No pressor-sparing effect",
                    "Benefit only with cosyntropin screening",
                ],
                0,
                "APROCCHSS used hydrocortisone 50 mg q6h plus fludrocortisone and demonstrated lower 90-day (not 28-day) mortality with fewer vasopressor days.",
                ref(
                    "Clinical trials",
                    "achieved a lower 90-day (but not 28-day) mortality in the treatment group (43% vs 49.1%), as well as fewer days requiring vasopressor support.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Guidelines — sepsis without shock",
                "Current SCCM/ESICM-derived recommendations for corticosteroids in sepsis state:",
                [
                    "Recommend corticosteroids for all adults with sepsis",
                    "Suggest against corticosteroids for adults with sepsis without shock",
                    "Mandate fludrocortisone in all septic patients",
                    "Require cosyntropin testing before any steroid use",
                ],
                1,
                "Guidelines suggest against corticosteroids in sepsis without shock; septic shock refractory to fluids and vasopressors is the key treatment scenario.",
                ref(
                    "Guidelines",
                    "Suggest against use of corticosteroids for adults with sepsis without shock",
                ),
            ),
            mcq(
                f"{p}-q10",
                "ARDS and meningitis",
                "According to the chapter's guideline summary, corticosteroids are recommended for:",
                [
                    "Major trauma (strong recommendation)",
                    "Early moderate-to-severe ARDS and bacterial meningitis",
                    "All patients with sepsis regardless of shock",
                    "Routine post-cardiac arrest care (strong recommendation)",
                ],
                1,
                "ARDS (conditional, moderate evidence) and bacterial meningitis (strong, low-quality evidence) are among recommended indications; major trauma is suggested against.",
                ref(
                    "Guidelines",
                    "Recommendations were made for the use of corticosteroids in hospitalized patients with early moderate to severe acute respiratory distress syndrome",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Etomidate confounding",
                "Why was the 2002 Annane trial criticized regarding cosyntropin nonresponse rates?",
                [
                    "Cosyntropin dose was subtherapeutic",
                    "Most patients received etomidate, which inhibits cortisol synthesis",
                    "Fludrocortisone was omitted in all patients",
                    "Patients were not ventilated",
                ],
                1,
                "72 of 99 patients received etomidate (11-hydroxylase inhibitor), potentially inflating nonresponder rates and mortality benefit in that subgroup.",
                ref(
                    "Clinical trials",
                    "This study was criticized, as 72 of 99 patients received etomidate, an adrenal 11-hydroxylase inhibitor that reduces cortisol synthesis",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Mortality predictors",
                "In septic shock, basal (random) cortisol is a useful mortality predictor when:",
                [
                    "It is mildly elevated (20–25 μg/dL)",
                    "It is extremely high (>45 μg/dL)",
                    "It is below 5 μg/dL only",
                    "It is always predictive regardless of level",
                ],
                1,
                "Basal cortisol is not generally predictive except at extremely high levels (>45 μg/dL), which portend worse outcomes.",
                ref(
                    "Critical Illness Stress Response",
                    "Basal cortisol values in sepsis/septic shock are not useful predictors of mortality except at extremely high cortisol levels (>45 μg/dL [>1242 nmol/L]).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Worst prognosis subgroup",
                "In Annane's 3-level prognostic classification, which septic shock patients had the lowest survival?",
                [
                    "Low basal cortisol and robust cosyntropin response",
                    "High basal cortisol (>34 μg/dL) with cosyntropin increment <9 μg/dL",
                    "Normal basal cortisol and normal cosyntropin response",
                    "Low basal cortisol and low cosyntropin response",
                ],
                1,
                "The combination of elevated basal cortisol with blunted ACTH response identified the subgroup with lowest survival.",
                ref(
                    "Critical Illness Stress Response",
                    "the lowest survival rate seen in those with a basal cortisol concentration greater than 34 μg/dL (>935 nmol/L) and a cortisol response to cosyntropin at 60 minutes less than 9 μg/dL (<248 nmol/L).",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "CIRCI",
                "Serum cortisol concentrations always reflect tissue glucocorticoid status in critical illness.",
                False,
                "Tissue resistance, altered binding proteins, and cytokine effects decouple serum levels from end-organ sufficiency.",
                ref(
                    "Critical Illness Stress Response",
                    "serum cortisol concentrations may not reflect tissue glucocorticoid status.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Cosyntropin testing",
                "Cosyntropin stimulation must be performed before starting hydrocortisone in septic shock refractory to vasopressors.",
                False,
                "Current practice supports hydrocortisone on clinical grounds; CIRCI operational definition is not mandatory for treatment.",
                ref(
                    "Case 2",
                    "The CIRCI operational definition is not required for hydrocortisone treatment.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Checkpoint inhibitors",
                "Most patients with checkpoint inhibitor-related adrenal insufficiency recover HPA axis function with high-dose glucocorticoids.",
                False,
                "HPA axis recovery is rare; high-dose glucocorticoid does not restore function.",
                ref(
                    "Case 1",
                    "HPA axis recovery is rare, and there is no recovery benefit from high-dosage glucocorticoid.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Hydrocortisone in CAP",
                "Hydrocortisone is suggested for hospitalized community-acquired pneumonia at doses below 400 mg daily for 5–7 days.",
                True,
                "13 trials, 12 showing mortality reduction, support conditional recommendation for hospitalized CAP.",
                ref(
                    "Case 4",
                    "Hydrocortisone at a dosage less than 400 mg daily or the equivalent for 5 to 7 days is suggested for community-acquired pneumonia",
                ),
            ),
            tf(
                f"{p}-tf5",
                "CORTICUS",
                "The CORTICUS trial demonstrated a 28-day mortality benefit from hydrocortisone in septic shock.",
                False,
                "No 28-day mortality benefit was seen, though shock resolved more quickly.",
                ref(
                    "Clinical trials",
                    "did not reveal any 28-day mortality benefit from hydrocortisone, 50 mg every 6 hours in 499 patients with septic shock",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Trauma",
                "Hydrocortisone has an established mortality benefit in severe trauma.",
                False,
                "A place for hydrocortisone in severe trauma is not established; guidelines suggest against use in major trauma.",
                ref(
                    "Main Conclusions",
                    "A place for hydrocortisone in severe trauma is not established.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Free cortisol",
                "Free cortisol increments correlate more closely with illness severity in sepsis than total cortisol.",
                True,
                "Reduced CBG and cleavage at inflammatory sites increase free fraction; free cortisol tracks severity better.",
                ref(
                    "Potential for Plasma Free Cortisol and CBG Measurements",
                    "free cortisol increments correspond to illness severity more closely than total cortisol.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "ADRENAL trial",
                "The ADRENAL trial showed increased rates of bacteremia and fungemia with hydrocortisone.",
                False,
                "Venkatesh et al reported no increase in bacteremia or fungemia despite faster shock resolution.",
                ref(
                    "Clinical trials",
                    "with no increase in rates of bacteremia or fungemia.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Serum cortisol limits",
                "Assertion: Random serum cortisol is unreliable for assessing glucocorticoid sufficiency in sepsis.",
                "Reason: Tissue resistance and reduced CBG/albumin alter the relationship between total and free cortisol.",
                0,
                "Both true and causally linked—binding protein changes and tissue resistance decouple serum from tissue status.",
                ref(
                    "Main Conclusions",
                    "Routine measurements of serum cortisol may not reflect end-organ glucocorticoid sufficiency due to tissue resistance to cortisol and reduced concentrations of the principal carrier proteins for cortisol, corticosteroid-binding globulin (CBG) and albumin.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Septic shock treatment",
                "Assertion: Hydrocortisone is indicated in septic shock refractory to fluids and vasopressors.",
                "Reason: Low-dose hydrocortisone for 7 days shortens vasopressor requirement.",
                0,
                "Both true; pressor-sparing benefit supports treatment even when mortality trials are discordant.",
                ref(
                    "Case 2",
                    "Hydrocortisone use is recommended in septic shock unresponsive to fluid resuscitation and inotropes.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "CIRCI testing",
                "Assertion: Cosyntropin testing is mandatory before hydrocortisone in septic shock.",
                "Reason: CIRCI is defined as a cosyntropin increment less than 9 μg/dL at 60 minutes.",
                1,
                "Both true but R does not justify A—definition exists but is not required for treatment decisions.",
                ref(
                    "Case 2",
                    "The CIRCI operational definition is not required for hydrocortisone treatment.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Checkpoint inhibitors",
                "Assertion: A patient on ipilimumab with cortisol 4 μg/dL and shock should receive immediate parenteral glucocorticoids.",
                "Reason: Cosyntropin stimulation is needed to distinguish adrenal insufficiency from CIRCI.",
                2,
                "A is true; R is false—clinical presentation is sufficient without delaying for cosyntropin.",
                ref(
                    "Case 1",
                    "Baseline cortisol and clinical features are sufficiently diagnostic of adrenal insufficiency.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Annane 2002",
                "Assertion: The Annane 2002 trial proved mortality benefit of hydrocortisone in all septic shock patients.",
                "Reason: Benefit was limited to cosyntropin nonresponders.",
                2,
                "A is false (benefit only in nonresponders); R is true.",
                ref(
                    "Clinical trials",
                    "revealed a 28-day mortality benefit for treatment in the nonresponders to cosyntropin, 250 mcg",
                ),
            ),
            ar(
                f"{p}-ar6",
                "CORTICUS",
                "Assertion: CORTICUS showed no mortality benefit from hydrocortisone in septic shock.",
                "Reason: Hydrocortisone accelerated shock resolution in that trial.",
                0,
                "Both true; lack of mortality benefit coexisted with faster shock resolution.",
                ref(
                    "Clinical trials",
                    "Hydrocortisone, however, was associated with more rapid resolution of shock.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "CAP steroids",
                "Assertion: Hydrocortisone may be given for hospitalized community-acquired pneumonia without proven primary adrenal insufficiency.",
                "Reason: Multiple randomized trials show mortality reduction with short-course low-dose steroids.",
                0,
                "Both true; CAP indication is evidence-based and independent of formal AI diagnosis.",
                ref(
                    "Case 4",
                    "Hydrocortisone at a dosage less than 400 mg daily or the equivalent for 5 to 7 days is suggested for community-acquired pneumonia based on results from 13 trials, 12 of which showed reduced mortality.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Trauma",
                "Assertion: Hydrocortisone should be routinely used in major trauma.",
                "Reason: Severe trauma causes profound HPA axis activation requiring supplementation.",
                4,
                "Both false—trauma HPA activation does not establish benefit; guidelines suggest against routine use.",
                ref(
                    "Guidelines",
                    "Suggest against use of corticosteroids in major trauma (low-quality of evidence)",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "8",
        "title": "Difficulties in Diagnosis and Management of Adrenal Insufficiency in the Critically Ill",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "David J. Torpy, MBBS, PhD, FRACP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_08_Difficulties_in_Dia_and_Managemen_Adrenal_Insuffici_the_Critically_III_F.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_07_Deciding_Who_to_Screen_for_Genetic_Causes.json": build_chapter_07,
    "endo2021_chapter_08_Difficulties_in_Dia_and_Managemen_Adrenal_Insuffici_the_Critically_III_F.json": build_chapter_08,
}


def write_module(filename: str, data: dict) -> tuple[Path, Path]:
    PORTAL_DATA.mkdir(parents=True, exist_ok=True)
    portal_path = PORTAL_DATA / filename
    portal_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
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
        print(f"  Copied to {master_path}")


if __name__ == "__main__":
    main()
