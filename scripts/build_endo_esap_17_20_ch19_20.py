#!/usr/bin/env python3
"""ESAP 2021 modules e21-19 and e21-20 builder functions."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402


def build_chapter_19() -> dict:
    p = "e21-19"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Main conclusions",
                "Why GLP-1 receptor agonists and SGLT-2 inhibitors are preferentially used in high-risk T2DM",
                "Numerous agents in both classes reduce important cardiovascular and renal complications when added to usual care in patients with established ASCVD or multiple risk factors; they should be used preferentially irrespective of whether additional glucose lowering is needed.",
                ref(
                    "Main Conclusions",
                    "These newer agents should be preferentially used in patients at high risk for cardio-renal complications, including those with established major comorbidities, likely irrespective of the need for additional glucose lowering or preexisting antihyperglycemic therapy.",
                ),
            ),
            note(
                f"{p}-n2",
                "Regimen integration",
                "How to incorporate SGLT-2 inhibitors into already complex diabetes regimens",
                "When glycemic control is already at goal, background antihyperglycemic therapy may need adjustment to limit hypoglycemia and cost. Before starting an SGLT-2 inhibitor, assess blood pressure and volume status and anticipate diuretic or antihypertensive changes.",
                ref(
                    "Main Conclusions",
                    "anticipatory modification of diuretic or other antihypertensive therapy may be needed to avoid significant volume depletion or hypotension with the addition of an SGLT-2 inhibitor.",
                ),
            ),
            note(
                f"{p}-n3",
                "Residual risk",
                "Excess cardiovascular risk persists in diabetes despite improved population outcomes",
                "Individuals with diabetes still have approximately 2-fold excess cardiovascular risk; only 14% meet combined targets for glycemia, blood pressure, lipids, and nonsmoking status—leaving substantial residual risk addressable by proven drug classes.",
                ref(
                    "Significance of the Clinical Problem",
                    "only 14% meet targets for glycemic and blood pressure control and lipid management and do not smoke cigarettes.",
                ),
            ),
            note(
                f"{p}-n4",
                "CVOT paradigm",
                "How FDA cardiovascular outcomes trials reshaped T2DM therapy selection",
                "Since 2008 FDA guidance, large placebo-added-to-usual-care trials in patients with established ASCVD or high MACE risk have defined which newer antihyperglycemic classes reduce MACE, heart failure hospitalization, or renal endpoints.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "In 2008, the US FDA issued a guidance recommending thorough evaluation of all new diabetes therapies for cardiovascular safety.",
                ),
            ),
            note(
                f"{p}-n5",
                "DPP-4 inhibitors",
                "DPP-4 inhibitors: neutral MACE with a saxagliptin heart-failure signal",
                "DPP-4 inhibitor CVOTs are consistently neutral for MACE; saxagliptin in SAVOR-TIMI-53 unexpectedly increased heart failure hospitalization—a finding not reproduced elsewhere but relevant when treating patients with existing heart failure.",
                ref(
                    "DPP-4 Inhibitors",
                    "the SAVOR TIMI-53 trial of saxagliptin therapy unexpectedly found an increase in hospitalization for heart failure in patients assigned to that medication when compared with placebo.",
                ),
            ),
            note(
                f"{p}-n6",
                "GLP-1 receptor agonists",
                "GLP-1 receptor agonist cardiovascular outcomes: class heterogeneity",
                "Liraglutide, semaglutide, and dulaglutide reduce MACE in high-risk T2DM; lixisenatide and once-weekly exenatide were neutral. REWIND showed MACE benefit even when most patients lacked prior cardiovascular events. GLP-1 RAs have neutral effects on heart failure hospitalization.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "These trials have shown that liraglutide, semaglutide, and dulaglutide all reduce the risk of MACE when compared with placebo in patients with T2DM at high risk for such events.",
                ),
            ),
            note(
                f"{p}-n7",
                "SGLT-2 inhibitors",
                "SGLT-2 inhibitors: consistent heart failure benefit across CVOTs",
                "Empagliflozin and canagliflozin reduce MACE; dapagliflozin did not reduce MACE in DECLARE but did reduce a co-primary heart failure endpoint. All completed SGLT-2 inhibitor CVOTs show significant heart failure outcome reduction; DAPA-HF extended benefit to HFrEF with or without diabetes.",
                ref(
                    "SGLT-2 Inhibitors",
                    "All of the completed cardiovascular outcomes trials of SGLT-2 inhibitors have shown a significant reduction in heart failure outcomes with use of those agents.",
                ),
            ),
            note(
                f"{p}-n8",
                "Renal outcomes",
                "Why renal benefits differ between GLP-1 RAs and SGLT-2 inhibitors",
                "Meta-analyses suggest GLP-1 RA renal benefit is driven mainly by reduced macroalbuminuria, whereas SGLT-2 inhibitors reduce worsening eGFR, end-stage kidney disease, and renal death; CREDENCE established canagliflozin benefit in albuminuric CKD.",
                ref(
                    "Renal Effects of GLP-1 Receptor Agonists and SGLT-2 Inhibitors",
                    "the renal outcomes benefit noted in the trials of GLP-1 receptor agonists were primarily attributable to a reduction in macroalbuminuria, while SGLT-2 inhibitors were found to reduce the risks of worsening estimated glomerular filtration rate, end-stage kidney disease, or death due to renal causes.",
                ),
            ),
            note(
                f"{p}-n9",
                "Mechanisms",
                "Why cardiovascular trial benefits are not explained by glucose lowering alone",
                "GLP-1 RA benefit may reflect antiatherogenic effects via weight and blood pressure improvement; SGLT-2 inhibitor benefit likely involves hemodynamic effects of glycosuria and natriuresis—these mechanisms operate independently of A1c reduction.",
                ref(
                    "GLP-1 Receptor Agonists and SGLT-2 Inhibitors Outcomes Summary",
                    "The cardiovascular benefits identified in the cardiovascular outcomes trials do not appear attributable to or dependent on glucose lowering.",
                ),
            ),
            note(
                f"{p}-n10",
                "Clinical application",
                "How to choose between proven GLP-1 RA and SGLT-2 inhibitor agents",
                "Guidelines favor drugs with proven outcomes benefit; some suggest GLP-1 RA first in ASCVD with SGLT-2 inhibitor as second choice, but without head-to-head data either proven class is reasonable based on comorbidities, eGFR, heart failure phenotype, and patient preference.",
                ref(
                    "GLP-1 Receptor Agonists and SGLT-2 Inhibitors Outcomes Summary",
                    "there are no head-to-head trials comparing the effects of the 2 drug classes in this patient population; thus, choice of a proven agent from either class is reasonable, based on individual patient characteristics and preferences.",
                ),
            ),
            note(
                f"{p}-n11",
                "US indications",
                "FDA-labeled cardiovascular indications for SGLT-2 inhibitors in T2DM",
                "Empagliflozin reduces cardiovascular death in T2DM with established ASCVD; canagliflozin reduces MACE in that population; dapagliflozin reduces heart failure hospitalization in T2DM with established ASCVD or multiple cardiovascular risk factors.",
                ref(
                    "SGLT-2 Inhibitors",
                    "empagliflozin is indicated to reduce the risk of cardiovascular death in adult patients with T2DM and established ASCVD; canagliflozin is indicated to reduce the risk of MACE in the same population; and dapagliflozin is indicated to reduce the risk of hospitalization for heart failure in adults with T2DM and established ASCVD or multiple cardiovascular risk factors.",
                ),
            ),
            note(
                f"{p}-n12",
                "Implementation barriers",
                "Barriers limiting uptake of cardioprotective diabetes therapies",
                "Despite guideline recommendations, implementation remains limited in the highest-benefit populations because of unfamiliarity with rapidly emerging CVOT data, concern about adverse effects, and difficulty fitting new agents into complex regimens.",
                ref(
                    "Significance of the Clinical Problem",
                    "implementation of these therapies has thus far been quite limited, particularly in the populations of patients most likely to derive an outcome benefit.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — ASCVD without diabetes therapy",
                "A 76-year-old woman with T2DM, ASCVD (prior stent), BMI 33, BP 124/80 on lisinopril and hydrochlorothiazide, A1c 7.2%, eGFR 56, takes no glucose-lowering drugs. Best regimen change?",
                [
                    "No change",
                    "Start metformin",
                    "Start empagliflozin and discontinue hydrochlorothiazide",
                    "Start empagliflozin only without changing diuretic",
                ],
                2,
                "Established ASCVD warrants a proven cardioprotective agent; empagliflozin is appropriate and HCTZ should be stopped when starting SGLT-2 inhibitor in a normotensive older patient to avoid volume depletion.",
                ref(
                    "Case 1",
                    "Answer: C and D) Start empagliflozin and discontinue hydrochlorothiazide",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — metformin trap",
                "The same patient asks why metformin is not started first. What is the best explanation?",
                [
                    "Metformin is contraindicated when A1c is below 8%",
                    "CV benefits of SGLT-2 inhibitors require background metformin",
                    "Metformin has no demonstrated efficacy for cardiovascular risk reduction in established ASCVD",
                    "Empagliflozin cannot be used without metformin",
                ],
                2,
                "Outcomes trial benefits are not restricted to metformin users; metformin lacks proven CV risk reduction in patients with established ASCVD.",
                ref(
                    "Case 1",
                    "metformin has no demonstrated efficacy in the reduction of cardiovascular risk in patients with established ASCVD.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — low eGFR",
                "A 57-year-old man with T2DM, peripheral and coronary artery disease, CKD (eGFR 28), A1c 8.4%, on sitagliptin and basal insulin without hypoglycemia. Best change?",
                [
                    "No change",
                    "Add empagliflozin",
                    "Add lixisenatide",
                    "Substitute liraglutide for sitagliptin",
                ],
                3,
                "eGFR is below empagliflozin and canagliflozin thresholds; liraglutide (MACE-beneficial GLP-1 RA) should replace sitagliptin—combined GLP-1 RA plus DPP-4 inhibitor is not recommended.",
                ref(
                    "Case 2",
                    "Answer: E) Substitute liraglutide for sitagliptin",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 3 — CKD and HFpEF",
                "A 67-year-old woman with insulin-treated T2DM, CKD, HFpEF, A1c 8.2%, no recent hypoglycemia. Best next step?",
                [
                    "No change",
                    "Add linagliptin",
                    "Add low-dose metformin",
                    "Add canagliflozin 100 mg daily",
                ],
                3,
                "CREDENCE supports canagliflozin 100 mg in T2DM with albuminuric diabetic nephropathy and eGFR ≥30; it reduces kidney failure, CV death, and heart failure hospitalization.",
                ref(
                    "Case 3",
                    "Answer: D) Add canagliflozin, 100 mg daily",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 4 — HFrEF with prediabetes",
                "A 56-year-old man with obesity, multivessel CAD, HFrEF, prediabetes (A1c 5.9%), eGFR 46, elevated BNP. Preferred intervention?",
                [
                    "Intensive lifestyle modification alone",
                    "Begin dapagliflozin 10 mg daily",
                    "Begin liraglutide titrated to 3 mg daily for weight loss",
                    "Begin metformin 500 mg twice daily",
                ],
                1,
                "DAPA-HF showed dapagliflozin reduced worsening heart failure or cardiovascular death in HFrEF with or without diabetes—preferred over lifestyle or metformin alone in this phenotype.",
                ref(
                    "Case 4",
                    "Answer: B) Begin dapagliflozin, 10 mg daily",
                ),
            ),
            mcq(
                f"{p}-q6",
                "GLP-1 RA trials",
                "Which GLP-1 receptor agonist cardiovascular outcomes trial demonstrated MACE reduction in patients mostly without prior cardiovascular events?",
                [
                    "ELIXA (lixisenatide)",
                    "EXSCEL (exenatide once weekly)",
                    "REWIND (dulaglutide)",
                    "SUSTAIN-6 (semaglutide injection)",
                ],
                2,
                "REWIND enrolled high-risk patients but most lacked prior CV events yet still showed MACE benefit with dulaglutide.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "the REWIND trial of dulaglutide also enrolled patients at high risk, but in contrast to the other cardiovascular outcomes trials, most of the patients included had not had a prior cardiovascular event.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "SGLT-2 DECLARE",
                "In the DECLARE trial, dapagliflozin compared with placebo showed which outcome pattern?",
                [
                    "Reduced MACE but not heart failure",
                    "Neutral MACE with reduced heart failure endpoint",
                    "Increased heart failure hospitalization",
                    "Reduced MACE and renal death only",
                ],
                1,
                "DECLARE did not show MACE reduction but did significantly reduce a co-primary heart failure outcome.",
                ref(
                    "SGLT-2 Inhibitors",
                    "The DECLARE trial did not find a reduction in MACE risk with dapagliflozin; however, a second primary heart failure outcome in that trial was significantly reduced with active therapy compared with placebo.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "DPP-4 inhibitors",
                "Regarding DPP-4 inhibitors and cardiovascular risk in T2DM, which statement is correct?",
                [
                    "They reduce MACE and should replace GLP-1 RAs",
                    "They are neutral for MACE and should not be used solely to reduce cardiovascular risk",
                    "They consistently reduce heart failure hospitalization",
                    "Saxagliptin is preferred in patients with established heart failure",
                ],
                1,
                "DPP-4 inhibitors are CV-safe but neutral; saxagliptin may increase HF hospitalization.",
                ref(
                    "DPP-4 Inhibitors",
                    "DPP-4 inhibitors, although largely found to be safe from a cardiovascular perspective, should not be used to reduce cardiovascular risk in patients with T2DM.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "CREDENCE",
                "Canagliflozin 100 mg daily in CREDENCE reduced which composite in T2DM with albuminuric CKD?",
                [
                    "MACE only",
                    "Kidney failure and cardiovascular events",
                    "Retinopathy progression only",
                    "Hypoglycemia requiring assistance",
                ],
                1,
                "CREDENCE showed significant reduction in kidney failure and cardiovascular events at 2.62 years.",
                ref(
                    "Renal Effects of GLP-1 Receptor Agonists and SGLT-2 Inhibitors",
                    "canagliflozin, 100 mg daily, significantly reduced the risk of kidney failure and cardiovascular events at 2.62 years compared with placebo.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Heart failure phenotypes",
                "Across GLP-1 RA cardiovascular outcomes trials, hospitalization for heart failure was generally:",
                [
                    "Significantly reduced",
                    "Neutral",
                    "Significantly increased",
                    "Reduced only with liraglutide",
                ],
                1,
                "GLP-1 RA trials show neutral effects on heart failure hospitalization unlike SGLT-2 inhibitors.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "the trials of GLP-1 receptor agonists have found a neutral effect of these agents on rates of heart failure hospitalization.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Glycemic thresholds",
                "A patient with ASCVD has A1c at individualized goal on basal insulin without hypoglycemia. Regarding addition of a cardioprotective agent:",
                [
                    "Wait until A1c exceeds 8% before adding GLP-1 RA or SGLT-2 inhibitor",
                    "Cardioprotective agents require metformin co-therapy",
                    "Proven agents should be considered even when glycemic control is adequate",
                    "SGLT-2 inhibitors are only indicated when A1c is above 9%",
                ],
                2,
                "High-risk patients should receive proven cardio-renal agents irrespective of need for additional glucose lowering.",
                ref(
                    "Main Conclusions",
                    "likely irrespective of the need for additional glucose lowering or preexisting antihyperglycemic therapy.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Volume management",
                "Before starting empagliflozin in a patient on hydrochlorothiazide who appears euovolemic with BP 124/80, what adjustment is most appropriate?",
                [
                    "Double hydrochlorothiazide dose",
                    "Discontinue hydrochlorothiazide and reassess volume status at follow-up",
                    "Add spironolactone prophylactically",
                    "No antihypertensive changes are ever needed with SGLT-2 inhibitors",
                ],
                1,
                "Anticipatory diuretic reduction prevents volume depletion and hypotension when initiating SGLT-2 inhibitor therapy.",
                ref(
                    "Case 1",
                    "that medication should be discontinued (Answer D) when empagliflozin is started, and the patient's volume status and blood pressure should be reassessed at follow-up.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Liraglutide indication",
                "In the United States, which GLP-1 receptor agonist is indicated to reduce MACE in adults with T2DM and established ASCVD?",
                [
                    "Lixisenatide",
                    "Exenatide once weekly",
                    "Liraglutide",
                    "Dulaglutide",
                ],
                2,
                "Among GLP-1 RAs with trial benefit, liraglutide carries a US indication to reduce MACE in T2DM with established ASCVD.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "thus far in the United States liraglutide is indicated to reduce the risk of MACE in adults with T2DM and established ASCVD.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Diabetes cardiovascular risk",
                "Individuals with diabetes have approximately 2-fold excess risk of cardiovascular outcomes compared with persons without diabetes.",
                True,
                "Excess vascular risk remains substantial despite population improvements in diabetes care.",
                ref(
                    "Significance of the Clinical Problem",
                    "individuals with diabetes still have an approximately 2-fold excess risk of cardiovascular outcomes (including coronary heart disease, stroke, and vascular death) compared with outcomes of persons without diabetes.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "DPP-4 MACE",
                "Completed DPP-4 inhibitor cardiovascular outcomes trials have consistently shown neutral effects on MACE.",
                True,
                "All four listed DPP-4 inhibitor CVOTs were neutral for MACE.",
                ref(
                    "DPP-4 Inhibitors",
                    "Trials of the DPP-4 inhibitor medications completed thus far have consistently demonstrated a neutral effect of these drugs on rates of MACE.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Saxagliptin heart failure",
                "SAVOR-TIMI-53 found increased hospitalization for heart failure with saxagliptin versus placebo.",
                True,
                "This signal has not been reproduced in other trials but warrants caution in patients with heart failure.",
                ref(
                    "DPP-4 Inhibitors",
                    "the SAVOR TIMI-53 trial of saxagliptin therapy unexpectedly found an increase in hospitalization for heart failure in patients assigned to that medication when compared with placebo.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "GLP-1 RA heart failure",
                "GLP-1 receptor agonists consistently reduce hospitalization for heart failure in cardiovascular outcomes trials.",
                False,
                "GLP-1 RA trials show neutral effects on heart failure hospitalization; SGLT-2 inhibitors reduce HF outcomes.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "the trials of GLP-1 receptor agonists have found a neutral effect of these agents on rates of heart failure hospitalization.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "CV benefit and A1c",
                "Cardiovascular benefits of GLP-1 RAs and SGLT-2 inhibitors in outcomes trials appear dependent on glucose lowering.",
                False,
                "Trial benefits operate through weight, BP, hemodynamic, and other mechanisms not explained by A1c change alone.",
                ref(
                    "GLP-1 Receptor Agonists and SGLT-2 Inhibitors Outcomes Summary",
                    "The cardiovascular benefits identified in the cardiovascular outcomes trials do not appear attributable to or dependent on glucose lowering.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Lixisenatide MACE",
                "The ELIXA trial demonstrated MACE reduction with lixisenatide.",
                False,
                "Lixisenatide was neutral for cardiovascular risk in ELIXA.",
                ref(
                    "Case 2",
                    "Lixisenatide (Answer C) was not found to reduce cardiovascular risk in the ELIXA trial",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Empagliflozin eGFR",
                "Empagliflozin is indicated for use when eGFR is 45 mL/min/1.73 m² or higher.",
                True,
                "At eGFR 28, empagliflozin is not the correct choice per labeling discussed in Case 2.",
                ref(
                    "Case 2",
                    "Empagliflozin (Answer B) is not currently the correct choice for this patient given his low estimated glomerular filtration rate, as this medication is at present only indicated for use in patients with an estimated glomerular filtration rate of 45 mL/min per 1.73 m² or higher.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "DAPA-HF",
                "Dapagliflozin in DAPA-HF reduced worsening heart failure or cardiovascular death in patients with HFrEF with or without diabetes.",
                True,
                "DAPA-HF extended SGLT-2 inhibitor heart failure benefit beyond the diabetes CVOT population.",
                ref(
                    "SGLT-2 Inhibitors",
                    "dapagliflozin therapy significantly reduced the risk of worsening heart failure or death from cardiovascular causes compared with placebo.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "SGLT-2 inhibitors",
                "Assertion: SGLT-2 inhibitors reduce hospitalization for heart failure in high-risk patients with T2DM.",
                "Reason: All completed SGLT-2 inhibitor cardiovascular outcomes trials have shown significant reduction in heart failure outcomes.",
                0,
                "Both are true and the trial consistency supports the assertion.",
                ref(
                    "SGLT-2 Inhibitors",
                    "All of the completed cardiovascular outcomes trials of SGLT-2 inhibitors have shown a significant reduction in heart failure outcomes with use of those agents.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "GLP-1 RA renal effect",
                "Assertion: GLP-1 receptor agonists primarily reduce macroalbuminuria as their renal outcome benefit.",
                "Reason: GLP-1 receptor agonists reduce end-stage kidney disease more than SGLT-2 inhibitors in meta-analyses.",
                2,
                "Assertion is true per meta-analyses; the reason reverses the predominant SGLT-2 inhibitor renal endpoint benefit.",
                ref(
                    "Renal Effects of GLP-1 Receptor Agonists and SGLT-2 Inhibitors",
                    "the renal outcomes benefit noted in the trials of GLP-1 receptor agonists were primarily attributable to a reduction in macroalbuminuria, while SGLT-2 inhibitors were found to reduce the risks of worsening estimated glomerular filtration rate, end-stage kidney disease, or death due to renal causes.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Metformin in ASCVD",
                "Assertion: Metformin should not be the preferred initial step solely to reduce cardiovascular risk in a patient with established ASCVD.",
                "Reason: Metformin has no demonstrated efficacy in reducing cardiovascular risk in patients with established ASCVD.",
                0,
                "Both are true; proven GLP-1 RA or SGLT-2 inhibitor therapy addresses residual risk.",
                ref(
                    "Case 1",
                    "metformin has no demonstrated efficacy in the reduction of cardiovascular risk in patients with established ASCVD.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "DPP-4 plus GLP-1 RA",
                "Assertion: Sitagliptin should be discontinued when liraglutide is started.",
                "Reason: Combined GLP-1 receptor agonist and DPP-4 inhibitor therapy is not recommended.",
                0,
                "Both are true; substitution avoids redundant cost and unsupported combination use.",
                ref(
                    "Case 2",
                    "This patient's sitagliptin should be discontinued when liraglutide is started, as combined use of a GLP-1 receptor agonist and a DPP-4 inhibitor is not recommended",
                ),
            ),
            ar(
                f"{p}-ar5",
                "REWIND",
                "Assertion: Dulaglutide reduced MACE in REWIND despite most patients lacking prior cardiovascular events.",
                "Reason: REWIND only enrolled patients with prior myocardial infarction or stroke.",
                3,
                "Assertion is true; REWIND uniquely included mostly patients without prior CV events—the reason is false.",
                ref(
                    "GLP-1 Receptor Agonists",
                    "the REWIND trial of dulaglutide also enrolled patients at high risk, but in contrast to the other cardiovascular outcomes trials, most of the patients included had not had a prior cardiovascular event.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Canagliflozin CKD",
                "Assertion: Canagliflozin 100 mg daily is appropriate in T2DM with albuminuric nephropathy and eGFR ≥30 mL/min/1.73 m².",
                "Reason: CREDENCE demonstrated reduced kidney failure and cardiovascular events with canagliflozin versus placebo.",
                0,
                "Both are true; CREDENCE underpins the labeled renal-cardiovascular indication.",
                ref(
                    "Renal Effects of GLP-1 Receptor Agonists and SGLT-2 Inhibitors",
                    "canagliflozin, 100 mg daily, significantly reduced the risk of kidney failure and cardiovascular events at 2.62 years compared with placebo.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Low eGFR metformin",
                "Assertion: Low-dose metformin should not be added in a patient with eGFR 30–44 mL/min/1.73 m² for cardio-renal protection.",
                "Reason: Metformin reduces progression to end-stage kidney disease in albuminuric diabetic nephropathy.",
                2,
                "Assertion is true per Case 3; metformin is not recommended at this eGFR and lacks the renal outcomes shown for canagliflozin.",
                ref(
                    "Case 3",
                    "the addition of even low-dosage metformin is not recommended in patients such as this with an estimated glomerular filtration rate between 30 and 44 mL/min per 1.73 m².",
                ),
            ),
            ar(
                f"{p}-ar8",
                "HFrEF prediabetes",
                "Assertion: Dapagliflozin is the preferred next step in a patient with HFrEF and prediabetes.",
                "Reason: DAPA-HF showed dapagliflozin reduced worsening heart failure or cardiovascular death with or without diabetes.",
                0,
                "Both are true; heart failure phenotype drives SGLT-2 inhibitor priority over lifestyle or metformin alone.",
                ref(
                    "Case 4",
                    "the DAPA-HF trial found that in patients with heart failure with reduced ejection fraction with or without diabetes, dapagliflozin significantly reduced the risk of worsening heart failure or death of cardiovascular causes.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "19",
        "title": "Cardiovascular Outcomes in Patients With Type 2 Diabetes Mellitus Treated With GLP-1 Receptor Agonists and SGLT-2 Inhibitors",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Jennifer B. Green, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_19_Cardiovascular_Outcomes_in_Patients_With_Type_2_Diabetes_Mellitus_Treated_With_GLP1_Receptor_Agonists_and_SGLT2_Inhibitors.md",
        "items": items,
    }


def build_chapter_20() -> dict:
    p = "e21-20"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Screening",
                "Why patients with T2DM should be screened for NAFLD even with normal transaminases",
                "Diabetes is a high-risk population for NAFLD/NASH; up to 50% with normal ALT may have NAFLD, and unrecognized disease progresses to fibrosis, cirrhosis, and excess cardiovascular mortality.",
                ref(
                    "Main Conclusions",
                    "Patients with diabetes are considered a high-risk population for this condition and should be screened for the presence of NAFLD and NASH even if concentrations of plasma aminotransferases are normal.",
                ),
            ),
            note(
                f"{p}-n2",
                "Diagnosis",
                "How to diagnose NAFLD in clinical practice",
                "NAFLD requires hepatic steatosis on imaging or ¹H-MRS (>5.56% liver fat), exclusion of significant alcohol use (>21 units/week men, >14 women), and exclusion of other liver diseases.",
                ref(
                    "Diagnosis of NAFLD and NASH",
                    "The diagnosis of NAFLD is based on the following: (1) presence of hepatic steatosis in addition to (2) lack of significant alcohol consumption (defined as ongoing or recent alcohol consumption of >21 units/week for men and >14 units/week for women), and (3) exclusion of other liver diseases.",
                ),
            ),
            note(
                f"{p}-n3",
                "NASH diagnosis",
                "Why liver biopsy remains the reference standard for NASH",
                "Current guidelines advise liver biopsy is the only way to diagnose NASH; noninvasive tools estimate fibrosis risk but are not fully validated for NASH diagnosis before treatment initiation.",
                ref(
                    "Diagnosis of NAFLD and NASH",
                    "current guidelines advise that liver biopsy is the only way to diagnose NASH and that noninvasive techniques have not yet been fully validated for the diagnosis of this condition.",
                ),
            ),
            note(
                f"{p}-n4",
                "First-line therapy",
                "First-line pharmacotherapy for biopsy-proven NASH in patients with diabetes",
                "No FDA-approved NASH-specific agents exist, but GLP-1 receptor agonists and pioglitazone should be considered first-line in biopsy-proven NASH and in patients with diabetes and NAFLD/NASH alongside lifestyle intervention.",
                ref(
                    "Main Conclusions",
                    "GLP-1 receptor agonists and pioglitazone should be considered first-line therapy in patients with NASH confirmed on liver biopsy and in patients with diabetes and NAFLD/NASH.",
                ),
            ),
            note(
                f"{p}-n5",
                "Foundation therapy",
                "Mainstay of NAFLD/NASH management beyond drugs",
                "Weight loss and aggressive cardiovascular risk factor control—dyslipidemia, hypertension, and glycemia—remain the foundation; NAFLD increases cardiovascular risk through lipotoxicity and glucotoxicity.",
                ref(
                    "Main Conclusions",
                    "Mainstay of NAFLD treatment is weight loss and aggressive cardiovascular risk factor management (ie, dyslipidemia, hypertension, and glycemic control).",
                ),
            ),
            note(
                f"{p}-n6",
                "Pioglitazone",
                "Pioglitazone histologic efficacy in NASH with prediabetes or T2DM",
                "Long-term pioglitazone achieved NASH resolution in 51% versus 19% placebo (32% treatment difference); 58% achieved ≥2-point NAS improvement without fibrosis worsening versus 17% placebo.",
                ref(
                    "Pioglitazone",
                    "Resolution of NASH, a secondary outcome in this trial, occurred in 51% of patients in the pioglitazone arm vs 19% in the placebo group, with a placebo-subtracted treatment difference of 32% points",
                ),
            ),
            note(
                f"{p}-n7",
                "Vitamin E",
                "How vitamin E efficacy differs between patients with and without T2DM",
                "Vitamin E 800 IU daily showed benefit in PIVENS (non-diabetic NASH) but provides only marginal benefit in NASH with T2DM; AASLD guidance does not recommend vitamin E for NASH in patients with diabetes.",
                ref(
                    "Main Conclusions",
                    "Vitamin E demonstrated efficacy in patients without diabetes, and is only of marginal benefit in patients with NASH and T2DM.",
                ),
            ),
            note(
                f"{p}-n8",
                "Metformin",
                "Why metformin is not effective for steatohepatitis despite first-line diabetes use",
                "Metformin may reduce liver fat but does not significantly impact NASH resolution or fibrosis and is considered neutral for steatohepatitis treatment per current guidelines.",
                ref(
                    "Other Antidiabetes Drugs",
                    "Although metformin remains first-line therapy for the management of hyperglycemia in T2DM and may reduce liver fat, it is not effective for the treatment of steatohepatitis, as it does not significantly impact resolution of NASH or fibrosis.",
                ),
            ),
            note(
                f"{p}-n9",
                "SGLT-2 inhibitors",
                "SGLT-2 inhibitors in NAFLD: steatosis without histology trials",
                "Empagliflozin, dapagliflozin, and other SGLT-2 inhibitors reduce hepatic steatosis on imaging, but no randomized trials have assessed effects on liver histology—making them attractive second- or third-line agents, often combined with pioglitazone.",
                ref(
                    "Other Antidiabetes Drugs",
                    "Of note, there are no randomized controlled trials assessing the effect of SGLT-2 inhibitors on liver histology.",
                ),
            ),
            note(
                f"{p}-n10",
                "Liraglutide LEAN",
                "Liraglutide LEAN trial outcomes in biopsy-proven NASH",
                "Liraglutide 1.8 mg daily for 48 weeks achieved NASH resolution in 39% versus 9% placebo with less fibrosis progression—placebo-subtracted treatment difference approximately 30%.",
                ref(
                    "Strategies for Therapy and Management of NAFLD and NASH",
                    "Resolution of NASH occurred in 39% of patients with liraglutide compared with 9% of patients in the placebo group",
                ),
            ),
            note(
                f"{p}-n11",
                "Statins",
                "Statins in NAFLD/NASH: safety without histologic efficacy",
                "Statins are safe with elevated liver enzymes and remain first-line for dyslipidemia given high cardiovascular risk; prospective histology studies have not shown significant inflammation or fibrosis improvement versus placebo.",
                ref(
                    "Strategies for Therapy and Management of NAFLD and NASH",
                    "Statins are safe to use in patients with NAFLD/NASH even if liver enzymes are elevated, and should be used as first-line therapy for lipid lowering.",
                ),
            ),
            note(
                f"{p}-n12",
                "Weight loss threshold",
                "How much weight loss improves steatohepatitis",
                "An 8% to 10% body weight reduction is expected to improve steatohepatitis; histologic improvement with orlistat was proportional to weight loss, with benefit when loss exceeded 9%.",
                ref(
                    "Antiobesity Medications Other Than GLP-1 Receptor Agonists",
                    "A positive effect in improving steatohepatitis would be expected with any of these agents when inducing an 8% to 10% reduction in body weight",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — evaluation",
                "A 69-year-old man with T2DM, hepatic steatosis on ultrasound, and elevated ALT needs further evaluation of transaminitis. Which assessments are indicated?",
                [
                    "CAGE questionnaire only",
                    "Viral and autoimmune serologies only",
                    "Medication and supplement review only",
                    "All of the above (alcohol, serologies, medications, supplements)",
                ],
                3,
                "NAFLD diagnosis requires excluding alcohol, viral hepatitis, autoimmune disease, and steatogenic medications or supplements.",
                ref(
                    "Case 1",
                    "Answer: E) All of the above",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — FIB-4",
                "A patient with T2DM has FIB-4 of 2.87. What is the appropriate conclusion?",
                [
                    "FIB-4 cannot be calculated",
                    "Very low fibrosis risk—no further workup",
                    "Low to moderate risk—no further workup",
                    "Moderate to high fibrosis risk—additional workup and hepatology referral",
                ],
                3,
                "FIB-4 >2.67 indicates moderate to high advanced fibrosis risk warranting further evaluation and hepatology referral.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: D) He has a moderate to high risk of liver fibrosis, so additional workup and referral to hepatology are needed",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 1 — NASH resolution",
                "After metformin, which second-line diabetes agents have shown significant NASH resolution versus placebo on liver biopsy?",
                [
                    "Liraglutide and pioglitazone",
                    "Dulaglutide and empagliflozin",
                    "Empagliflozin and sitagliptin",
                    "Sitagliptin only",
                ],
                0,
                "LEAN (liraglutide) and pioglitazone RCTs demonstrate NASH resolution; SGLT-2 inhibitors reduce steatosis on imaging without histology trials.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A and E) Liraglutide and pioglitazone",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 1 — statins",
                "The patient asks about continuing atorvastatin with elevated liver enzymes. Best recommendation?",
                [
                    "Continue atorvastatin for cardiovascular risk from T2DM and NAFLD",
                    "Stop atorvastatin before starting pioglitazone due to interaction",
                    "Continue because statins improve NASH fibrosis in trials",
                    "Stop atorvastatin because enzymes are elevated and statins lack histologic benefit",
                ],
                0,
                "Statins are safe in NAFLD/NASH and indicated for cardiovascular risk despite limited histologic efficacy.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A) He should continue atorvastatin because of increased cardiovascular disease risk from T2DM and NAFLD",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 1 — vitamin E",
                "Which statement about vitamin E in T2DM with NASH is INCORRECT?",
                [
                    "Vitamin E 800 IU daily should be recommended based on PIVENS for this diabetic patient",
                    "Current guidelines do not recommend vitamin E for NASH in T2DM",
                    "Guidelines recommend vitamin E for NASH without T2DM",
                    "Vitamin E may increase mortality and prostate cancer risk in men",
                ],
                0,
                "PIVENS benefit was in non-diabetic NASH; vitamin E is not recommended for NASH in patients with T2DM.",
                ref(
                    "Case 1 (Continued)",
                    "Answer: A) Vitamin E at a dosage of 800 IU daily should be recommended given the known benefit of vitamin E in NASH reported in the PIVENS trial",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Case 2 — antiobesity therapy",
                "A postmenopausal woman with prediabetes and NAFLD needs 8%–11% weight loss to improve steatohepatitis. Which agents are most likely to achieve this?",
                [
                    "Orlistat alone",
                    "Phentermine/topiramate ER or liraglutide 3.0 mg",
                    "Naltrexone/bupropion only",
                    "Metformin dose escalation",
                ],
                1,
                "Phentermine/topiramate induces 8%–11% weight loss in 30%–40%; liraglutide 3.0 mg achieves similar magnitude and has NASH histology data at 1.8 mg.",
                ref(
                    "Case 2",
                    "Answer: B or D) Phentermine/topiramate ER or liraglutide",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Case 3 — fibrosis risk factors",
                "A man with longstanding uncontrolled T2DM has biopsy-proven NASH with stage 3 fibrosis despite normal ALT. Which is NOT a risk factor for advanced fibrosis?",
                [
                    "Poor glycemic control",
                    "High BMI",
                    "Normal liver enzymes",
                    "Modest red wine consumption",
                ],
                3,
                "Poor glycemic control, obesity, high triglycerides, and even 'normal' ALT do not exclude advanced fibrosis; modest red wine is not established as a fibrosis risk factor in this vignette.",
                ref(
                    "Case 3",
                    "Answer: E) Modest red wine consumption",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Case 3 — fibrosis improvement",
                "Which agent has NOT shown significant 1-point fibrosis improvement without worsening steatohepatitis versus placebo?",
                [
                    "Liraglutide",
                    "Semaglutide",
                    "Pioglitazone",
                    "Obeticholic acid",
                ],
                1,
                "Semaglutide improved NASH resolution but did not significantly improve fibrosis versus placebo in the large 72-week trial (~43% vs ~33%).",
                ref(
                    "Case 3 (Continued)",
                    "Answer: B) Semaglutide",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Epidemiology",
                "What is the approximate global prevalence of NAFLD in the general population per recent meta-analysis?",
                [
                    "5%",
                    "15%",
                    "25%",
                    "50%",
                ],
                2,
                "Global NAFLD prevalence is estimated at 25% in the general population, higher in T2DM.",
                ref(
                    "Significance of the Clinical Problem",
                    "the global prevalence of NAFLD was estimated to be 25% in the general population",
                ),
            ),
            mcq(
                f"{p}-q10",
                "NAFLD in T2DM",
                "Using sensitive imaging, NAFLD prevalence in overweight or obese adults with T2DM may reach approximately:",
                [
                    "25%",
                    "40%",
                    "56%",
                    "70%",
                ],
                3,
                "¹H-MRS-based studies report up to 70% NAFLD prevalence in overweight/obese adults with T2DM.",
                ref(
                    "Significance of the Clinical Problem",
                    "up to 70% in overweight or obese adults with T2DM.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Pioglitazone barriers",
                "A common barrier to pioglitazone use in NASH is:",
                [
                    "Lack of histologic efficacy data",
                    "Unawareness that more than 50% achieve NASH resolution",
                    "Contraindication in all patients with T2DM",
                    "Mandatory liver biopsy before every dose titration",
                ],
                1,
                "Providers often underuse pioglitazone despite >50% NASH resolution rates in trials due to unfamiliarity and concerns about weight gain.",
                ref(
                    "Barriers to Optimal Practice",
                    "unawareness about its efficacy (>50% have NASH resolution with pioglitazone)",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Semaglutide NASH trial",
                "In the semaglutide NASH trial, approximate NASH resolution rates with 0.4 mg daily versus placebo were:",
                [
                    "17% vs 59%",
                    "36% vs 51%",
                    "59% vs 17%",
                    "51% vs 19%",
                ],
                2,
                "Semaglutide 0.4 mg achieved ~59% NASH resolution without fibrosis worsening versus 17% placebo (dose-response trial).",
                ref(
                    "Strategies for Therapy and Management of NAFLD and NASH",
                    "59% in the 0.4-mg group, and 17% in the placebo group (P < .001 for semaglutide 0.4 mg vs placebo).",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Obeticholic acid REGENERATE",
                "In the REGENERATE phase 3 trial, obeticholic acid 25 mg met which primary endpoint?",
                [
                    "NASH resolution at 18 months",
                    "Fibrosis improvement ≥1 stage with no worsening of NASH",
                    "30% reduction in liver fat by MRI-PDFF only",
                    "Normalization of ALT at 12 weeks",
                ],
                1,
                "REGENERATE met fibrosis improvement without NASH worsening (23% vs 12% placebo) but not the NASH resolution primary endpoint at interim analysis.",
                ref(
                    "Investigational Drugs",
                    "met the primary endpoint of fibrosis improvement (≥1 stage) with no worsening of NASH in 23% of patients compared with 12% of patients in the placebo group",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "FDA approval",
                "There are currently FDA-approved pharmacologic therapies specifically indicated for NAFLD or NASH.",
                False,
                "No agent has a specific FDA indication for NAFLD/NASH despite multiple agents showing histologic benefit in trials.",
                ref(
                    "Significance of the Clinical Problem",
                    "currently there are no pharmacologic agents approved specifically for this condition.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Normal ALT",
                "Up to 50% of patients with normal ALT (<40 U/L) may have NAFLD.",
                True,
                "Relying on aminotransferases alone misses substantial NAFLD burden in diabetes.",
                ref(
                    "Diagnosis of NAFLD and NASH",
                    "up to 50% of patients with normal ALT levels (<40 U/L [<0.67 μkat/L]) may have NAFLD.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Pioglitazone NASH resolution",
                "Pioglitazone achieved NASH resolution in approximately 51% of patients versus 19% with placebo in a long-term RCT.",
                True,
                "This 32-percentage-point treatment difference underpins first-line recommendation in biopsy-proven NASH.",
                ref(
                    "Pioglitazone",
                    "51% of patients in the pioglitazone arm had NASH resolution (a secondary outcome) vs 19% in the placebo group",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Metformin steatohepatitis",
                "Metformin significantly improves NASH resolution and fibrosis on liver biopsy.",
                False,
                "Metformin may lower liver fat but is neutral for steatohepatitis histologic endpoints.",
                ref(
                    "Other Antidiabetes Drugs",
                    "it is not effective for the treatment of steatohepatitis, as it does not significantly impact resolution of NASH or fibrosis.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "SGLT-2 histology",
                "Randomized controlled trials have demonstrated SGLT-2 inhibitors improve liver histology in NASH.",
                False,
                "SGLT-2 inhibitors reduce steatosis on imaging; no RCTs assess histologic endpoints.",
                ref(
                    "Other Antidiabetes Drugs",
                    "there are no randomized controlled trials assessing the effect of SGLT-2 inhibitors on liver histology.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Statins safety",
                "Statins should be avoided when liver enzymes are elevated in NAFLD/NASH.",
                False,
                "Statins are safe and recommended for cardiovascular risk reduction despite elevated transaminases.",
                ref(
                    "Strategies for Therapy and Management of NAFLD and NASH",
                    "Statins are safe to use in patients with NAFLD/NASH even if liver enzymes are elevated",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Vitamin E in T2DM",
                "Current AASLD guidance recommends vitamin E for treatment of NASH in patients with T2DM.",
                False,
                "Vitamin E is recommended for non-diabetic NASH; benefit in T2DM is marginal and not guideline-endorsed.",
                ref(
                    "Case 1 (Continued)",
                    "Current guidelines do not recommend vitamin E for treatment of NASH in patients with T2DM",
                ),
            ),
            tf(
                f"{p}-tf8",
                "NAFLD NAS definition",
                "Definite NASH on biopsy requires at least grade 1 in steatosis, lobular inflammation, and hepatocellular ballooning.",
                True,
                "NASH is defined histologically by steatosis, inflammation, and ballooning each ≥grade 1.",
                ref(
                    "Diagnosis of NAFLD and NASH",
                    "Definite NASH is determined on low- to medium-power microscopy based on the presence of at least grade 1 in each of the following 3 components",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Pioglitazone first-line",
                "Assertion: Pioglitazone should be first-line pharmacotherapy in biopsy-proven NASH with T2DM.",
                "Reason: Pioglitazone achieved NASH resolution in more than 50% of patients in randomized trials.",
                0,
                "Both are true; efficacy, cardiovascular benefit, and cost support first-line use.",
                ref(
                    "Pioglitazone",
                    "pioglitazone leads to resolution of NASH (>50%) in patients with and without T2DM",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Vitamin E",
                "Assertion: Vitamin E 800 IU daily is recommended for all patients with NASH including those with T2DM.",
                "Reason: PIVENS demonstrated vitamin E benefit only in adults with NASH without diabetes.",
                2,
                "Assertion is false; PIVENS enrolled non-diabetic patients and guidelines limit vitamin E recommendation accordingly.",
                ref(
                    "Vitamin E",
                    "adults with biopsy-proven NASH without diabetes received vitamin E at a dosage of 800 IU daily vs placebo for 96 weeks.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Liraglutide LEAN",
                "Assertion: Liraglutide 1.8 mg daily improves NASH histology in biopsy-proven disease.",
                "Reason: NASH resolution occurred in 39% with liraglutide versus 9% with placebo in the LEAN trial.",
                0,
                "Both are true; LEAN supports GLP-1 RA use in NASH with diabetes.",
                ref(
                    "Case 1 (Continued)",
                    "Resolution of NASH occurred in 39% of patients with liraglutide compared with 9% of patients in the placebo group",
                ),
            ),
            ar(
                f"{p}-ar4",
                "SGLT-2 inhibitors",
                "Assertion: SGLT-2 inhibitors are attractive second- or third-line agents for NAFLD/NASH.",
                "Reason: SGLT-2 inhibitors have proven histologic NASH resolution in large randomized trials.",
                1,
                "Both statements about steatosis/weight are directionally true, but the reason is false—no histology RCTs exist.",
                ref(
                    "Other Antidiabetes Drugs",
                    "there are no randomized controlled trials assessing the effect of SGLT-2 inhibitors on liver histology.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Insulin resistance",
                "Assertion: Individuals with NAFLD are more insulin resistant at muscle, liver, and adipose tissue than those without NAFLD.",
                "Reason: In NAFLD, insulin resistance is present in liver and adipose tissue but not in muscle.",
                2,
                "Assertion is true per Gastaldelli review; insulin resistance involves all three tissues—the reason is false.",
                ref(
                    "Case 1 (Continued)",
                    "individuals with NAFLD are more insulin resistant than those without NAFLD, even if they are lean and without diabetes (Answer A).",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Weight loss",
                "Assertion: An 8% to 10% body weight reduction is expected to improve steatohepatitis.",
                "Reason: Orlistat improves NASH histology independent of weight loss magnitude.",
                2,
                "Assertion is true; orlistat histology benefit was proportional to weight loss >9%, not drug-specific.",
                ref(
                    "Antiobesity Medications Other Than GLP-1 Receptor Agonists",
                    "improvement in insulin sensitivity and liver histology is proportional to the magnitude of weight loss.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Semaglutide fibrosis",
                "Assertion: Semaglutide did not significantly improve liver fibrosis versus placebo in a large NASH trial.",
                "Reason: Most participants had advanced fibrosis which may require longer follow-up to improve.",
                1,
                "Both are true; lack of significant fibrosis improvement may reflect advanced disease stage and trial limitations.",
                ref(
                    "Case 3 (Continued)",
                    "semaglutide (Answer B) failed to show significant difference in fibrosis improvement when compared with placebo",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Endocrinology role",
                "Assertion: Endocrinologists should become more involved in NAFLD/NASH management.",
                "Reason: NASH overlaps extensively with obesity and diabetes with major clinical implications.",
                0,
                "Both are true; the chapter emphasizes endocrine leadership in this epidemic.",
                ref(
                    "Main Conclusions",
                    "endocrinologists should become more involved in the management of NAFLD/NASH given the significant overlap of NASH with obesity and diabetes",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "20",
        "title": "Pharmacologic Approaches to the Patient With Nonalcoholic Fatty Liver Disease",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Diana Barb, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_20_Pharmacologic_Approaches_to_the_Patient_With_Nonalcoholic_Fatty_Liver_Disease.md",
        "items": items,
    }
