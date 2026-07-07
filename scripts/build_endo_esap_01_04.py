#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-01 through e21-04 (Obesity/lipids batch)."""
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


def build_chapter_01() -> dict:
    p = "e21-01"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Residual ASCVD risk",
                "Why standard cholesterol panels miss high-risk patients",
                "ACC/AHA risk calculators based on total and HDL cholesterol can fail to identify individuals at high ASCVD risk. Proatherogenic lipoprotein subclasses—small dense LDL and triglyceride-rich remnants—and low large HDL particles may drive risk disproportionate to measured cholesterol content.",
                ref(
                    "Main Conclusions",
                    "the algorithm can fail to identify individuals at high risk for ASCVD. Thus, candidates for lipid-lowering on the basis of plasma levels of lipoprotein particle subclasses may not be identified.",
                ),
            ),
            note(
                f"{p}-n2",
                "Advanced lipoprotein testing",
                "Components of advanced lipoprotein testing",
                "Advanced testing includes nuclear magnetic resonance or ion mobility particle quantification, total LDL particle and/or apolipoprotein B concentrations, and lipoprotein(a) measured by immunoassay. Together these refine ASCVD risk beyond standard lipid panels.",
                ref(
                    "Main Conclusions",
                    "Collectively, these measurements, as well as plasma levels of total LDL particles and/or apolipoprotein B, comprise advanced lipoprotein testing.",
                ),
            ),
            note(
                f"{p}-n3",
                "When to order",
                "How to select patients for advanced lipoprotein testing",
                "Consider advanced testing for borderline dyslipidemia or intermediate estimated risk, metabolic syndrome features, and significant family history of ASCVD. It also helps assess response to lipid-lowering therapy.",
                ref(
                    "Main Conclusions",
                    "Consideration should be given to obtaining such testing for ASCVD risk assessment in individuals with borderline dyslipidemia or estimated risk using current algorithms, features of metabolic syndrome, and/or significant family history of ASCVD.",
                ),
            ),
            note(
                f"{p}-n4",
                "LDL heterogeneity",
                "Why LDL cholesterol misestimates LDL particle burden",
                "LDL particles play a central causal role in ASCVD, but total and LDL cholesterol can over- or underestimate LDL particle concentrations because LDL exists across a spectrum of size and cholesterol content.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "measurement of total and LDL cholesterol can lead to overestimation or underestimation of LDL particle concentrations. This is because there is a spectrum of LDL",
                ),
            ),
            note(
                f"{p}-n5",
                "NMR vs ion mobility",
                "Nuclear magnetic resonance versus ion mobility for LDL subclasses",
                "NMR deconvolves a single plasma lipid signal into size components; ion mobility directly measures particle subclass concentrations in defined size intervals. Reference ranges differ, and ion mobility links both medium and small LDL to ASCVD risk.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The former is based on mathematical deconvolution of a single lipid-generated signal from plasma into multiple components of differing size, while the latter yields direct measurement of concentrations of lipoprotein particle subclasses within defined particle size intervals.",
                ),
            ),
            note(
                f"{p}-n6",
                "Small LDL",
                "Why small LDL varies independently of LDL cholesterol",
                "Small and medium LDL particle levels can vary greatly at any given LDL cholesterol or triglyceride concentration. Correlations are stronger with non-HDL cholesterol and apoB, but substantial divergence remains—advanced testing is preferred for subclass profiling.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Levels of these particles, and in particular small LDL, can vary greatly at any given plasma concentration of LDL cholesterol or triglyceride",
                ),
            ),
            note(
                f"{p}-n7",
                "Lp(a)",
                "Why lipoprotein(a) requires separate immunoassay measurement",
                "Lp(a) is not readily discriminated by NMR or ion mobility. It consists of LDL covalently linked to apolipoprotein(a), conferring prothrombotic and proatherogenic properties beyond LDL cholesterol content, including stroke, CAD, and calcific aortic stenosis risk.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Another key component of advanced lipoprotein testing is Lp(a). This particle is not readily discriminated by nuclear magnetic resonance or ion mobility techniques and thus is most commonly measured by immunoassay.",
                ),
            ),
            note(
                f"{p}-n8",
                "Lp(a) genetics",
                "How to approach elevated Lp(a) in families",
                "Lp(a) is strongly genetically determined via LPA polymorphisms and kringle-repeat variation. More than one-third of the population exceeds 75 nmol/L; cascade screening of first-degree relatives directs aggressive ASCVD prevention in affected relatives.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Due to the strong genetic basis of elevated Lp(a), cascade screening of first-degree family members for this condition has value for directing more aggressive efforts at ASCVD reduction in the 50% of such relatives who may be affected.",
                ),
            ),
            note(
                f"{p}-n9",
                "Evidence limitations",
                "Pitfall: lack of RCTs targeting particle subspecies",
                "Therapeutic decisions are limited by absence of RCTs proving particle-subspecies reduction superior to LDL-C lowering for event reduction. Nevertheless, total LDL particle and apoB concentrations predict risk in multiple analyses.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "the application of evidence-based criteria for therapeutic decision-making has been limited by the lack of randomized control trials aimed at specifically testing whether reductions in lipoprotein particle subspecies are superior to change in LDL cholesterol",
                ),
            ),
            note(
                f"{p}-n10",
                "ACC/AHA statin groups",
                "Four ACC/AHA groups warranting cholesterol-lowering therapy",
                "Candidates include clinical ASCVD; LDL-C ≥190 mg/dL; diabetes age 40–75; and adults 40–75 without ASCVD/diabetes with ≥7.5% 10-year ASCVD risk (consider 5–7.5% intermediate risk).",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "4 groups of candidates for cholesterol-lowering therapy: (1) clinical ASCVD; (2) LDL cholesterol ≥190 mg/dL (≥4.92 mmol/L); (3) diabetes mellitus (patients aged 40 to 75 years); and (4) individuals aged 40 to 75 years without ASCVD or diabetes who have a 10-year risk of ASCVD of at least 7.5%",
                ),
            ),
            note(
                f"{p}-n11",
                "Case 1 — diet for small LDL",
                "How dietary carbohydrate restriction lowers small LDL",
                "For patients with elevated small LDL and pattern B, limiting carbohydrate rather than saturated fat is most appropriate to reduce small dense LDL particles—a prominent feature of advanced panel abnormalities.",
                ref(
                    "Case 1",
                    "Limitation of carbohydrate rather than saturated fat (Answer A) is most appropriate for reducing elevated levels of small LDL particles, which is a prominent feature of this patient's lipoprotein profile.",
                ),
            ),
            note(
                f"{p}-n12",
                "Barriers to practice",
                "Why clinicians underuse advanced lipoprotein testing",
                "Without particle measurements, clinicians may miss patients needing more aggressive lipid management. Challenges include differing assay platforms and lack of standardized risk thresholds, but experience with methodology enables effective use in selected patients.",
                ref(
                    "Barriers to Optimal Practice",
                    "Without obtaining measurements of lipoprotein particles that comprise advanced lipid testing, clinicians may not recognize the advisability of more aggressive lipid management for a significant subset of their patients.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — initial therapy",
                "A 43-year-old woman has total cholesterol 206 mg/dL, LDL-C 136 mg/dL, HDL-C 49 mg/dL, and 10-year ASCVD risk 5.8%. Advanced testing shows high total/small/medium LDL particles, pattern B, and Lp(a) 173 nmol/L. What initial pharmacotherapy is recommended?",
                [
                    "Diet only with further saturated fat restriction",
                    "Nicotinic acid",
                    "A PCSK9 inhibitor",
                    "A statin",
                ],
                3,
                "Statins remain first-line for increased ASCVD risk. Carbohydrate restriction—not saturated fat alone—targets small LDL; niacin and PCSK9 inhibitors are adjunctive after maximal statin therapy or intolerance.",
                ref(
                    "Case 1",
                    "Answer: D) A statin",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — post-statin response",
                "After rosuvastatin 10 mg daily for 3 months, small LDL fell 45% and medium LDL 37%, but levels remain above optimal with persistent elevated Lp(a) and pattern B. What is the best interpretation?",
                [
                    "Statin therapy failed; stop the statin",
                    "Partial response warrants ongoing lipid management beyond initial statin",
                    "PCSK9 inhibitor is mandatory immediately",
                    "No further therapy is needed because LDL-C may be at goal",
                ],
                1,
                "Statin produced meaningful subclass reductions but residual high-risk particles and Lp(a) persist—further management is warranted.",
                ref(
                    "Case 1",
                    "the resulting levels were above optimal, and elevated Lp(a) and LDL subclass pattern B persisted. Therefore, further lipid management was felt to be warranted and is underway.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Lp(a) threshold",
                "At what Lp(a) concentration does the chapter cite increased ASCVD risk in more than one-third of the population?",
                [
                    ">30 nmol/L",
                    ">50 nmol/L",
                    ">75 nmol/L",
                    ">150 nmol/L",
                ],
                2,
                "Plasma Lp(a) >75 nmol/L exceeds risk-associated levels in more than one-third of the population, with markedly higher relative risk at the 95th percentile.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "plasma Lp(a) concentrations in more than one-third of the population are higher than those associated with increased ASCVD risk (>75 nmol/L)",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Nicotinic acid",
                "When might nicotinic acid still be considered after statin therapy in a patient with elevated Lp(a)?",
                [
                    "As first-line before any statin",
                    "Only if LDL-C is at goal on maximal statin ± ezetimibe but Lp(a) and subclasses remain high",
                    "Never—it has no Lp(a) effect",
                    "Only in patients with LDL-C <70 mg/dL and no family history",
                ],
                1,
                "Niacin may reduce Lp(a) and small LDL but failed to add clinical benefit in large trials atop maximal statin therapy; it may still be trialed if substantial residual abnormalities persist.",
                ref(
                    "Case 1",
                    "if this patient does not achieve substantial further improvement in LDL levels, nicotinic acid may be subsequently considered for a trial of adjunctive therapy.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "PCSK9 indications",
                "When are PCSK9 inhibitors appropriately indicated per this chapter?",
                [
                    "For any patient with elevated Lp(a) before statin trial",
                    "Addition to maximal statin therapy when LDL lowering is insufficient or after documented statin intolerance",
                    "As monotherapy for intermediate 10-year risk only",
                    "Only when LDL-C exceeds 190 mg/dL",
                ],
                1,
                "PCSK9 inhibitors are indicated for addition to maximal statin therapy when LDL lowering is insufficient or with intolerance to multiple statins.",
                ref(
                    "Case 1",
                    "PCSK9 inhibitors (Answer C) are currently indicated only for addition to maximal statin therapy if LDL lowering is not sufficient or if there is intolerance to multiple statins.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "ApoB and LDL-P",
                "Which advanced measures does the chapter cite as supporting ASCVD risk prediction?",
                [
                    "HDL cholesterol alone",
                    "Total LDL particle concentrations and apolipoprotein B",
                    "Triglycerides alone",
                    "Remnant cholesterol validated for routine risk assignment",
                ],
                1,
                "Analyses support total LDL particle concentrations and apoB for risk prediction; remnant particle levels are not yet established for routine risk assessment.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "a number of analyses have provided support for the power of total LDL particle concentrations, as well as apolipoprotein B in this regard.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Intermediate risk",
                "A 52-year-old man has 10-year ASCVD risk 6.2% with metabolic syndrome and strong family history of premature MI. Standard lipids are borderline. What is the best next laboratory step?",
                [
                    "No further testing; risk is below 7.5%",
                    "Advanced lipoprotein testing including Lp(a) and LDL subclasses",
                    "Coronary calcium score only—particle testing never adds value",
                    "Repeat lipids in 10 years",
                ],
                1,
                "Intermediate risk (5–7.5%) with metabolic syndrome and family history is an appropriate setting for advanced lipoprotein testing.",
                ref(
                    "Main Conclusions",
                    "Consideration should be given to obtaining such testing for ASCVD risk assessment in individuals with borderline dyslipidemia or estimated risk using current algorithms, features of metabolic syndrome, and/or significant family history of ASCVD.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Lp(a) mechanism",
                "Which pathologic property of Lp(a) is highlighted beyond its LDL component?",
                [
                    "Competitive inhibition of plasminogen-induced clot lysis",
                    "Direct HDL elevation",
                    "Insulin sensitization",
                    "Lowering of remnant cholesterol",
                ],
                0,
                "Apo(a) confers prothrombotic effects via plasminogen competition and increased oxidizability via disulfide bonds.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "These include a prothrombotic effect due to its competitive inhibition of plasminogen-induced clot lysis",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Ion mobility risk",
                "Ion mobility analysis links ASCVD risk to which LDL fractions?",
                [
                    "Large LDL only",
                    "Small and medium LDL particles",
                    "IDL remnants only—LDL size is irrelevant",
                    "VLDL cholesterol exclusively",
                ],
                1,
                "Ion mobility data associate risk with medium-sized as well as small LDL particles.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "In the case of ion mobility, ASCVD risk has been found to be associated with concentrations of medium-sized, as well as small, LDL particles.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Pattern B",
                "A patient has LDL subclass pattern B with small LDL 394 nmol/L (high) and LDL peak size 216.8 Å. Which dietary emphasis is most aligned with the case discussion?",
                [
                    "Further saturated fat restriction as sole intervention",
                    "Carbohydrate limitation to reduce small dense LDL",
                    "High carbohydrate, low fat diet",
                    "Alcohol increase for HDL",
                ],
                1,
                "Carbohydrate restriction—not saturated fat limitation alone—is preferred for elevated small LDL/pattern B.",
                ref(
                    "Case 1",
                    "Limitation of carbohydrate rather than saturated fat (Answer A) is most appropriate for reducing elevated levels of small LDL particles",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Family screening",
                "A patient has Lp(a) 173 nmol/L and premature CAD. What family-based strategy does the chapter endorse?",
                [
                    "No family testing—Lp(a) is entirely environmental",
                    "Cascade screening of first-degree relatives",
                    "Screen only children under age 10",
                    "Screen siblings only if LDL-C exceeds 190 mg/dL",
                ],
                1,
                "Cascade screening of first-degree relatives helps identify the ~50% who may share elevated Lp(a) and need intensified prevention.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "cascade screening of first-degree family members for this condition has value for directing more aggressive efforts at ASCVD reduction in the 50% of such relatives who may be affected.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Large HDL",
                "In the case table, large HDL particles were 4086 nmol/L. How does the chapter frame large HDL particles?",
                [
                    "Proatherogenic when low in number",
                    "Irrelevant to ASCVD risk",
                    "Always adequately captured by HDL cholesterol",
                    "Inversely related to triglycerides only",
                ],
                0,
                "Large HDL particles are associated with reduced ASCVD risk; advanced panels quantify them beyond standard HDL-C.",
                ref(
                    "Main Conclusions",
                    "large HDL particles, which are associated with reduced ASCVD risk.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Residual risk concept",
                "Despite LDL-lowering therapy efficacy, why does considerable residual ASCVD risk persist?",
                [
                    "All risk is explained by LDL cholesterol",
                    "Proatherogenic particles such as small dense LDL and Lp(a) impact risk disproportionate to their cholesterol content",
                    "HDL cholesterol elevation always eliminates residual risk",
                    "Triglycerides are never relevant",
                ],
                1,
                "Residual risk may not be reflected by LDL-C due to atherogenic particles whose risk exceeds their cholesterol content.",
                ref(
                    "Significance of the Clinical Problem",
                    "This may not be reflected by the plasma LDL-cholesterol concentration due to increased levels of lipoprotein particles, in particular small, dense LDL and Lp(a), that impact ASCVD to an extent disproportionate to their cholesterol content.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Risk calculators",
                "ACC/AHA risk calculators always identify every patient who would benefit from lipid-lowering therapy.",
                False,
                "The algorithm can fail to identify high-risk individuals whose risk is driven by lipoprotein subclasses.",
                ref(
                    "Main Conclusions",
                    "the algorithm can fail to identify individuals at high risk for ASCVD.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Lp(a) assay",
                "Lp(a) is most commonly measured by immunoassay rather than NMR or ion mobility.",
                True,
                "Lp(a) is not readily discriminated by NMR or ion mobility techniques.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "is most commonly measured by immunoassay.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Remnant particles",
                "Remnant lipoprotein particle levels measured by advanced assays are established for routine ASCVD risk assignment.",
                False,
                "Remnant levels are measured but not yet established for application in ASCVD risk assessment.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "their levels are not yet established for application in ASCVD risk assessment.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Statin first-line",
                "Statins remain the first-line pharmacologic intervention for patients at increased ASCVD risk.",
                True,
                "Based on well-established efficacy, statins are first-line for increased-risk patients.",
                ref(
                    "Case 1",
                    "statins remain the first-line pharmacologic intervention for all patients considered to be at increased risk of ASCVD.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Lp(a) and aortic stenosis",
                "Elevated plasma Lp(a) is associated with risk for calcific aortic stenosis.",
                True,
                "Lp(a) is linked to stroke, CAD, and calcific aortic stenosis.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "plasma Lp(a) is also associated with risk for calcific aortic stenosis.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Niacin outcomes",
                "Nicotinic acid added to maximal statin ± ezetimibe consistently improved clinical outcomes in recent large trials.",
                False,
                "Niacin failed to produce clinical benefit in recent large trials when added to maximal LDL lowering.",
                ref(
                    "Case 1",
                    "has failed to produce clinical benefit in recent large trials when added to a regimen yielding maximal LDL reduction by statins ± ezetimibe.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Intermediate risk",
                "A 10-year ASCVD risk of 5% to 7.5% may warrant consideration for cholesterol-lowering therapy per ACC/AHA guidance cited.",
                True,
                "Consideration may be given to intermediate 10-year risk of 5% to 7.5%.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Consideration may also be given to intermediate 10-year risk of 5% to 7.5%.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Small LDL changes",
                "Changes in small LDL particles are strongly correlated with changes in triglyceride-rich lipoproteins and HDL.",
                True,
                "Small LDL changes track with triglyceride-rich lipoprotein and HDL changes, complicating isolated subclass attribution.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "changes in small LDL particles in particular are strongly correlated with changes in triglyceride-rich lipoproteins and HDL.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Advanced testing",
                "Assertion: Advanced lipoprotein testing can identify ASCVD risk not revealed by standard lipid measurements.",
                "Reason: Small dense LDL and Lp(a) confer risk disproportionate to their cholesterol content.",
                0,
                "Both are true and causally linked to residual risk beyond LDL-C.",
                ref(
                    "Significance of the Clinical Problem",
                    "can identify individuals at heightened ASCVD risk that is not revealed by standard lipid measurements",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Statin therapy",
                "Assertion: A statin is the appropriate initial pharmacologic therapy for the case patient with intermediate risk and abnormal advanced panel.",
                "Reason: PCSK9 inhibitors are indicated as first-line monotherapy for intermediate-risk patients.",
                2,
                "Assertion is true; PCSK9 inhibitors require maximal statin therapy or intolerance—not first-line monotherapy here.",
                ref(
                    "Case 1",
                    "PCSK9 inhibitors (Answer C) are currently indicated only for addition to maximal statin therapy",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Lp(a) genetics",
                "Assertion: Cascade family screening is valuable when Lp(a) is elevated.",
                "Reason: Lp(a) levels are under strong genetic control with wide population variability.",
                0,
                "Both are true; genetic basis supports family screening.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Lp(a) levels are under much stronger genetic control than other plasma lipoproteins",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Diet and small LDL",
                "Assertion: Carbohydrate restriction is preferred over saturated fat restriction for elevated small LDL.",
                "Reason: Saturated fat is the primary driver of small dense LDL in all patients.",
                2,
                "Assertion matches the case; saturated fat as sole driver is false for this pattern.",
                ref(
                    "Case 1",
                    "Limitation of carbohydrate rather than saturated fat (Answer A) is most appropriate for reducing elevated levels of small LDL particles",
                ),
            ),
            ar(
                f"{p}-ar5",
                "ApoB",
                "Assertion: Apolipoprotein B concentrations support ASCVD risk assessment.",
                "Reason: ApoB measures the number of atherogenic particles.",
                0,
                "Both are true; apoB reflects particle number cited in the chapter analyses.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "provided support for the power of total LDL particle concentrations, as well as apolipoprotein B",
                ),
            ),
            ar(
                f"{p}-ar6",
                "NMR vs ion mobility",
                "Assertion: NMR and ion mobility use identical analytic principles.",
                "Reason: NMR deconvolves a lipid signal while ion mobility directly measures particle concentrations in size intervals.",
                2,
                "Assertion is false; the reason correctly describes different methodologies.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The former is based on mathematical deconvolution of a single lipid-generated signal from plasma into multiple components of differing size, while the latter yields direct measurement",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Mendelian randomization",
                "Assertion: Mendelian randomization supports causality for Lp(a) and LDL cholesterol in ASCVD.",
                "Reason: Mendelian randomization supports causality for HDL cholesterol levels in ASCVD.",
                2,
                "Lp(a) and LDL-C are supported; HDL-C causality is not supported in this discussion.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Mendelian randomization, which has been used to infer ASCVD causality for LDL-cholesterol and triglyceride levels, as well as Lp(a) (but not HDL-cholesterol) levels",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Practice barriers",
                "Assertion: Without advanced particle testing clinicians may undertreat a subset of at-risk patients.",
                "Reason: All methodological platforms for advanced lipoprotein testing are fully standardized with universal risk cutoffs.",
                2,
                "Assertion is true; lack of standardization is a barrier—the reason is false.",
                ref(
                    "Barriers to Optimal Practice",
                    "there are some challenges for implementing such testing in practice, including differing methodological platforms and the lack of standardized criteria for assigning ASCVD risk.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "1",
        "title": "When Should You Order Advanced Lipoprotein Testing?",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Ronald M. Krauss, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_01_When_Should_You_Order_Advanced_Lipoprotein_Testing.md",
        "items": items,
    }


def build_chapter_02() -> dict:
    p = "e21-02"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Energy expenditure",
                "Why providers should estimate daily energy expenditure",
                "Many patients believe only highly restrictive diets succeed, leading to frustration. Reasonable estimates of daily energy expenditure enable sustainable dietary changes rather than repeated futile very-low-calorie attempts.",
                ref(
                    "Significance of the Clinical Problem",
                    "By being more familiar with the components and how to estimate daily energy expenditure, providers can help patients avoid repeated, futile diet attempts and help them select approaches that, by being more moderate, are more sustainable.",
                ),
            ),
            note(
                f"{p}-n2",
                "Discussing obesity",
                "How to raise obesity without harming the therapeutic relationship",
                "Link lifestyle choices to adiposity-related comorbidities (diabetes, hypertension, dyslipidemia) rather than implying the patient is unhealthy because they are 'too fat.' If the patient is unwilling to change, defer the conversation.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Pointing out that lifestyle choices are leading to health problems is often less threatening to the patient than implying that they are unhealthy because they are too fat",
                ),
            ),
            note(
                f"{p}-n3",
                "Self-monitoring",
                "Why self-monitoring is central to long-term weight-loss maintenance",
                "Self-monitoring is the cognitive behavioral technique most strongly associated with successful maintenance. Food intake monitoring requires near-constant attention; dietary recall is notoriously inaccurate, especially in people with overweight/obesity.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The cognitive behavioral technique most strongly associated with long-term, successful weight-loss maintenance is self-monitoring.",
                ),
            ),
            note(
                f"{p}-n4",
                "Food diary pitfall",
                "How to use a two-week food record effectively",
                "Ask patients to record everything for 2 weeks to reveal true intake patterns. Emphasize the diary is for the patient's benefit—not to please the clinician—to reduce socially desirable reporting.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "I find it helpful to ask patients to record everything they eat for 2 weeks as a way for them to understand the value of doing so.",
                ),
            ),
            note(
                f"{p}-n5",
                "Activity expenditure",
                "Estimating walking and spontaneous activity energy cost",
                "Walking calculators using distance and body weight are accurate because human exercise efficiency is narrow (20–30% of oxygen consumption relative to work). Three miles daily walking may expend ~300 kcal; housework may add 100–700 kcal.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "This woman walks at least 3 miles per day to get to and from work, which will expend 300 kcal/day.",
                ),
            ),
            note(
                f"{p}-n6",
                "Thermic effect of food",
                "Why low TEF cannot explain failure to lose weight on perceived low intake",
                "TEF averages ~10% of ingested energy (range 2–20%). Even at the lowest TEF, the deficit is far too small to explain lack of weight loss on a perceived 1200 kcal/day intake when expenditure is higher.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "At the very lowest end of possible TEF, she would expend only 94 kcal less per day than we would predict based on the 10% TEF rule, which cannot account for her failure to lose weight on a perceived intake of 1200 kcal/day.",
                ),
            ),
            note(
                f"{p}-n7",
                "Night eating syndrome",
                "Night eating syndrome diagnostic criteria",
                "Diagnosis requires evening hyperphagia or nocturnal ingestion plus ≥3 of: morning anorexia, urge to eat after dinner/at night, insomnia, evening mood worsening, or belief that eating is needed to return to sleep. Prevalence ~1.5% in the US.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Night eating syndrome is also diagnosed if there are at least 3 of the following symptoms: (1) morning anorexia; (2) a strong urge to eat between dinner and sleep and/or during the night",
                ),
            ),
            note(
                f"{p}-n8",
                "Medication review",
                "Why medication lists must include OTC agents in weight management",
                "Many medications promote weight gain; substitution with weight-neutral alternatives is often possible. Appetite-stimulating drugs make comprehensive lifestyle programs much harder to sustain.",
                ref(
                    "Main Conclusions",
                    "When patients take medications that increase their appetite, it makes it loudly difficult to lose weight and keep it off.",
                ),
            ),
            note(
                f"{p}-n9",
                "H1 antagonists",
                "How H1-receptor blockade promotes weight gain",
                "Hypothalamic histamine suppresses feeding via H1R. H1 antagonists/inverse agonists (older antihistamines, some antipsychotics) increase food intake; H1 affinity correlates with orexigenic potency.",
                ref(
                    "Case 2",
                    "H1R antagonists/inverse agonists (older over-the-counter antiallergy medications) are associated with increased food intake and weight gain.",
                ),
            ),
            note(
                f"{p}-n10",
                "Glucocorticoid appetite",
                "Why exogenous glucocorticoids increase appetite",
                "Exogenous steroids suppress hypothalamic POMC and α-MSH production, unmasking NPY/AgRP-driven appetite stimulation—the opposite of Addison disease with extreme anorexia from POMC overproduction.",
                ref(
                    "Case 2",
                    "Exogenous corticosteroids suppress proopiomelanocortin, and thereby α-MSH production, resulting in an unopposed neuropeptide Y/agouti-related peptide effect to stimulate appetite.",
                ),
            ),
            note(
                f"{p}-n11",
                "Case 2 medications",
                "Medications contributing to iatrogenic weight gain in Case 2",
                "Amitriptyline, depot medroxyprogesterone, and diphenhydramine (Tylenol PM) are all associated with weight gain. Stopping them is not guaranteed to reverse weight gain but substitution may help.",
                ref(
                    "Case 2",
                    "Answer: A, B, and C) Tricyclic antidepressant amitriptyline she takes to treat neuralgia and depression and depot medroxyprogesterone she uses for contraception and Tylenol PM she takes 5 times per week to help fall asleep",
                ),
            ),
            note(
                f"{p}-n12",
                "Commercial programs",
                "How to counsel on commercial weight-loss programs",
                "Some commercial programs have adequate published data. Weight Watchers offers lower-cost moderate restriction; Jenny Craig, Medifast, and OPTIFAST are more expensive and may use severe restriction.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Weight Watchers provide lower cost, moderately energy-restricted options, whereas Jenny Craig, Medifast, and OPTIFAST are more expensive and may employ severe energy-restricted approaches.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — stalled weight loss",
                "A woman reports eating ~1200 kcal/day without weight loss. She walks 3 miles daily and is active with housework. She denies night eating symptoms. What best explains her plateau?",
                [
                    "Abnormally low exercise efficiency (<10%)",
                    "Deficient thermic effect of food as primary cause",
                    "Inaccurate dietary recall with underestimated intake",
                    "Night eating syndrome",
                ],
                2,
                "Dietary recall is notoriously inaccurate; overweight individuals underestimate intake more than lean adults. Self-monitoring is needed.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Dietary recall is notoriously inaccurate (thus, Answer C is correct).",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — next step",
                "The same patient has never kept a detailed food record. What intervention is most appropriate before escalating to pharmacotherapy?",
                [
                    "Immediate very-low-calorie diet",
                    "Two-week comprehensive self-monitoring of food intake",
                    "Assumption that reported intake is accurate",
                    "Nocturnal polysomnography",
                ],
                1,
                "A 2-week food record educates patients about true intake and often improves awareness and weight.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "This patient may not have tried to self-monitor food intake and thus should be provided the opportunity to do so.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — medication review",
                "A 34-year-old woman gained 40 lb over 2 years with hypertriglyceridemia and acne. She uses amitriptyline, depot medroxyprogesterone, and Tylenol PM; cortisol axis is normal. Which medications should be reconsidered?",
                [
                    "Amitriptyline only",
                    "Depot medroxyprogesterone only",
                    "Amitriptyline, depot medroxyprogesterone, and Tylenol PM",
                    "None—normal cortisol excludes iatrogenic weight gain",
                ],
                2,
                "All three agents are associated with weight gain; Cushing syndrome is excluded but iatrogenic causes remain.",
                ref(
                    "Case 2",
                    "Answer: A, B, and C) Tricyclic antidepressant amitriptyline she takes to treat neuralgia and depression and depot medroxyprogesterone she uses for contraception and Tylenol PM she takes 5 times per week to help fall asleep",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Walking expenditure",
                "A patient walks 3 miles daily commuting. According to the chapter, approximate daily energy expenditure from this walking is:",
                [
                    "50 kcal/day",
                    "300 kcal/day",
                    "1000 kcal/day",
                    "Unpredictable because exercise efficiency ranges 5–50%",
                ],
                1,
                "Online walking calculators are accurate; 3 miles/day ≈300 kcal. Human efficiency is 20–30%, not 5–50%.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "This woman walks at least 3 miles per day to get to and from work, which will expend 300 kcal/day.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "TEF magnitude",
                "The thermic effect of food typically accounts for what fraction of ingested energy?",
                [
                    "About 10% (range 2–20%)",
                    "About 40%",
                    "Less than 1% in all adults",
                    "50% in obesity",
                ],
                0,
                "TEF averages 10% with a 2–20% range—too small to explain large energy balance errors.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The thermic effect of food (TEF) (Answer D) averages only 10% of ingested energy, with a range from 2% to 20% in our hands.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Night eating",
                "Which feature is required to diagnose night eating syndrome?",
                [
                    "Unconscious sleep-related eating without recall",
                    "Evening hyperphagia or nocturnal ingestion with patient awareness and recall",
                    "Any snack after 8 PM",
                    "Binge eating once monthly",
                ],
                1,
                "Patients must be aware of and able to recall eating episodes; ≥3 additional criteria are needed.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The diagnosis requires that the patient be aware of and be able to recall the eating episodes.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Behavioral maintenance",
                "Which cognitive behavioral strategy is most strongly linked to long-term weight-loss maintenance?",
                [
                    "Avoiding all carbohydrates permanently",
                    "Self-monitoring of intake and behavior",
                    "Weekly weighing only without food records",
                    "Relying on dietary recall at annual visits",
                ],
                1,
                "Self-monitoring—especially of food—is the cornerstone of maintenance.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The cognitive behavioral technique most strongly associated with long-term, successful weight-loss maintenance is self-monitoring.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "H1 blockade",
                "Which medications are noted for greatest weight gain via H1-receptor affinity?",
                [
                    "Olanzapine and clozapine",
                    "Metformin and liraglutide",
                    "Levothyroxine and statins",
                    "ACE inhibitors",
                ],
                0,
                "Neuroleptics with highest H1R affinity (olanzapine, clozapine) cause the greatest weight gain.",
                ref(
                    "Case 2",
                    "neuroleptics with highest affinity for the H1R (olanzapine and clozapine) are associated with the greatest weight gain.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Stopping weight-gain drugs",
                "After discontinuing amitriptyline and depot medroxyprogesterone, what outcome should be anticipated?",
                [
                    "Guaranteed return to baseline weight",
                    "Weight loss is not guaranteed but substitution to weight-neutral agents may help",
                    "Immediate 40-lb loss within 1 month",
                    "Further mandatory bariatric surgery",
                ],
                1,
                "Merely stopping weight-promoting medications does not guarantee weight loss.",
                ref(
                    "Case 2",
                    "Unfortunately, merely stopping these medications is no guarantee of weight loss.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Dietitian referral",
                "Who is best suited to detailed diet history and motivational interviewing for obesity?",
                [
                    "Any staff member without training",
                    "Dietitians with obesity management and behavioral training",
                    "Surgeons only",
                    "Patients should self-manage without support",
                ],
                1,
                "Dietitians trained in motivational interviewing and obesity management are best suited when physicians lack time.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Dietitians with additional training in motivational interviewing, behavioral strategies, and obesity management are best suited for this task.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Underestimation of intake",
                "Who underestimates dietary intake to the greatest extent on recall?",
                [
                    "Normal-weight adults more than those with obesity",
                    "People with overweight or obesity more than normal-weight adults",
                    "No one underestimates intake",
                    "Only children",
                ],
                1,
                "Overweight and obese individuals underestimate intake more than normal-weight adults.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "those who are overweight or obese underestimate to a greater extent than do normal-weight adults.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Spontaneous activity",
                "Besides structured walking, which activity category may contribute 100–700 kcal/day in the case discussion?",
                [
                    "Housework/spontaneous physical activity",
                    "Sleeping",
                    "Sitting at a desk exclusively",
                    "Fasting",
                ],
                0,
                "Housework as spontaneous activity can materially affect total daily expenditure.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "her housework, which may be characterized as spontaneous physical activity, can contribute as little as 100 to as much as 700 kcal/day",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Restrictive diet counseling",
                "What should providers avoid reinforcing about weight-loss diets?",
                [
                    "That only very low-calorie diets can succeed",
                    "That moderate sustainable changes can work",
                    "That energy balance matters",
                    "That medication review is useful",
                ],
                0,
                "Providers should avoid supporting the belief that only very restrictive diets succeed.",
                ref(
                    "Significance of the Clinical Problem",
                    "Providers are encouraged to avoid supporting patient contentions that only very low-calorie diets are successful.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Exercise efficiency",
                "Human exercise efficiency typically ranges from 20% to 30% of oxygen consumption relative to work output.",
                True,
                "The narrow efficiency range makes walking expenditure calculators reliable.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Humans have a relatively narrow range of exercise efficiency, ranging from 20% to 30% of oxygen consumption relative to work output",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Dietary recall",
                "Dietary recall is accurate enough to guide weight-loss plans without self-monitoring.",
                False,
                "Dietary recall is notoriously inaccurate; real-time monitoring is needed.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Dietary recall is notoriously inaccurate (thus, Answer C is correct).",
                ),
            ),
            tf(
                f"{p}-tf3",
                "TEF explanation",
                "A very low thermic effect of food can fully explain failure to lose weight on a perceived 1200 kcal/day diet.",
                False,
                "Maximum TEF deviation is ~94 kcal/day—insufficient to explain the discrepancy.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "which cannot account for her failure to lose weight on a perceived intake of 1200 kcal/day.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Night eating prevalence",
                "Night eating syndrome affects approximately 1.5% of the US general population.",
                True,
                "Prevalence estimate is 1.5% in the general US population.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "the prevalence of night eating syndrome is 1.5% in the general population in the United States.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Amitriptyline",
                "Amitriptyline is associated with significant weight gain.",
                True,
                "Older antidepressants used for pain, including amitriptyline, promote weight gain.",
                ref(
                    "Case 2",
                    "amitriptyline (Answer A), are associated with significant weight gain.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Depot MPA",
                "Depot medroxyprogesterone is associated with fat gain.",
                True,
                "Depot medroxyprogesterone is linked to fat gain.",
                ref(
                    "Case 2",
                    "depot medroxyprogesterone (Answer B) is associated with fat gain.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Diphenhydramine",
                "Diphenhydramine in sleep aids can contribute to weight gain.",
                True,
                "Older antihistamines including diphenhydramine are associated with weight gain.",
                ref(
                    "Case 2",
                    "diphenhydramine (present in sleep aids because of its sedating properties) (Answer C) are also associated with weight gain.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Food record effect",
                "Attempting to record food intake for 2 weeks may itself increase dietary awareness and promote weight loss.",
                True,
                "The act of recording often increases awareness and can produce weight loss.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "the mere act of trying to record what they are eating causes them to become more aware of their behavior and they lose weight",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Self-monitoring",
                "Assertion: Self-monitoring is key to long-term weight-loss maintenance.",
                "Reason: Most people accurately recall their food intake without recording.",
                2,
                "Assertion is true; inaccurate recall makes the reason false.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Dietary recall is notoriously inaccurate",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Walking calculators",
                "Assertion: Online walking energy calculators are quite accurate.",
                "Reason: Human exercise efficiency varies widely from 5% to 80%.",
                2,
                "Assertion is true; efficiency is narrow (20–30%), not 5–80%.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Humans have a relatively narrow range of exercise efficiency, ranging from 20% to 30%",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Medication appetite",
                "Assertion: Appetite-stimulating medications make lifestyle weight loss harder.",
                "Reason: Medications that increase appetite oppose sustained energy deficit.",
                0,
                "Both are true and causally linked.",
                ref(
                    "Case 2",
                    "if patients are taking medications that increase appetite, it is more difficult to succeed with a comprehensive lifestyle weight-loss program.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Glucocorticoids",
                "Assertion: Exogenous glucocorticoids can increase appetite.",
                "Reason: They suppress hypothalamic POMC/α-MSH and unmask NPY/AgRP appetite drive.",
                0,
                "Both are true with described mechanism.",
                ref(
                    "Case 2",
                    "Exogenous corticosteroids suppress proopiomelanocortin, and thereby α-MSH production, resulting in an unopposed neuropeptide Y/agouti-related peptide effect to stimulate appetite.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Night eating",
                "Assertion: Night eating syndrome can be ruled out if the patient denies nocturnal eating with awareness.",
                "Reason: Night eating always occurs without patient recall.",
                2,
                "Assertion is appropriate when criteria absent; unconscious eating contradicts diagnostic requirements.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The diagnosis requires that the patient be aware of and be able to recall the eating episodes.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "H1 antagonists",
                "Assertion: H1-receptor antagonists are associated with increased food intake.",
                "Reason: Hypothalamic histamine stimulates appetite via H1R.",
                2,
                "Assertion is true; histamine inhibits appetite—the reason reverses physiology.",
                ref(
                    "Case 2",
                    "Hypothalamic histamine suppresses feeding behavior via the histamine-1 receptor (H1R)",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Stopping drugs",
                "Assertion: Stopping weight-gain medications may not produce weight loss.",
                "Reason: Weight gained on medications always reverses immediately upon discontinuation.",
                2,
                "Assertion is true; immediate guaranteed reversal is false.",
                ref(
                    "Case 2",
                    "Unfortunately, merely stopping these medications is no guarantee of weight loss.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Sustainable diets",
                "Assertion: Moderate sustainable dietary changes are preferable to repeated very-low-calorie attempts.",
                "Reason: Only very-low-calorie diets have evidence for long-term success.",
                2,
                "Assertion reflects chapter guidance; exclusive VLCD success is false.",
                ref(
                    "Significance of the Clinical Problem",
                    "Providers are encouraged to avoid supporting patient contentions that only very low-calorie diets are successful.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "2",
        "title": "Challenging Cases in Nutritional and Medical Treatment of Obesity",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Michael D. Jensen, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_02_Challenging_Cases_in_Nutritional_and_Medical_Treatment_of_Obesity.md",
        "items": items,
    }


def build_chapter_03() -> dict:
    p = "e21-03"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Polypharmacy",
                "Why medication review is foundational in obesity care",
                "Many common drug classes promote weight gain; polypharmacy can produce clinically meaningful adiposity when individually modest effects accumulate. Scan lists and substitute weight-neutral or weight-loss-promoting agents when feasible.",
                ref(
                    "Main Conclusions",
                    "A prudent approach is to scan medication lists for weight-promoting drugs and substitute weight-neutral or weight loss-promoting medications when feasible.",
                ),
            ),
            note(
                f"{p}-n2",
                "Epidemiology",
                "Obesity prevalence and comorbidity burden",
                "Obesity (BMI ≥30) affects ~40% of Americans; another third are overweight. Obesity fuels prediabetes, type 2 diabetes, NAFLD, cardiovascular disease, reproductive disorders, and several cancers.",
                ref(
                    "Significance of the Clinical Problem",
                    "Obesity (BMI ≥30 kg/m²) now affects 40% of Americans and another third are overweight (BMI 25-29.9 kg/m²).",
                ),
            ),
            note(
                f"{p}-n3",
                "Guideline approach",
                "How Endocrine Society obesity pharmacology guidance sequences care",
                "Lifestyle modification is foundational; assess weight effects of current medications and switch to weight-neutral or weight-loss agents before adding antiobesity pharmacotherapy for appropriately selected patients.",
                ref(
                    "Significance of the Clinical Problem",
                    "This includes assessment of weight effects of a patient's current medications with modification of the regimen to change weight gain-promoting medications to medications that promote weight loss or are weight neutral.",
                ),
            ),
            note(
                f"{p}-n4",
                "Glucocorticoids",
                "Why chronic glucocorticoids worsen obesity-related disease",
                "Repeated or chronic steroids cause weight gain and central adiposity; obesity can then worsen the underlying condition (e.g., asthma). Use the least steroid necessary; prefer episodic treatment when possible.",
                ref(
                    "Glucocorticoids (Oral, Topical, Inhaled, Intra-articular Injections)",
                    "Steroid use can help control asthma, but weight gain and obesity can then make asthma worse.",
                ),
            ),
            note(
                f"{p}-n5",
                "Diabetes agents",
                "How to choose diabetes medications for weight-conscious patients",
                "Insulin and secretagogues promote weight gain; metformin is mildly weight-reducing; GLP-1 receptor agonists and SGLT-2 inhibitors promote weight loss and are preferred after metformin in many guidelines.",
                ref(
                    "Diabetes Medications",
                    "most professional societies now recommend metformin as first-line treatment for type 2 diabetes followed by a GLP-1 receptor agonist or SGLT-2 inhibitor given their weight-loss effects.",
                ),
            ),
            note(
                f"{p}-n6",
                "Psychotropics",
                "Weight effects of antidepressants and antipsychotics",
                "Not all psychotropics cause weight gain. Olanzapine causes the most (~2.4 kg in 3 months in trials, far more in practice). Metformin and topiramate may mitigate antipsychotic metabolic effects.",
                ref(
                    "Antidepressants and Antipsychotic Medications",
                    "Olanzapine is associated with the most weight gain overall: 2.4 kg (5 lb) in 3 months in clinical trials, but frequently much more in clinical practice",
                ),
            ),
            note(
                f"{p}-n7",
                "Beta blockers",
                "Why beta-adrenergic blockers can promote weight gain",
                "Beta-blockers used for cardiovascular disease are among less-recognized weight-promoting classes. Propranolol for migraine prophylaxis may contribute to weight gain; topiramate is weight-losing and FDA approved for migraine.",
                ref(
                    "Significance of the Clinical Problem",
                    "other classes of medication are less well recognized such as β-adrenergic blockers used to treat heart disease, heart rhythm disorders, and hypertension",
                ),
            ),
            note(
                f"{p}-n8",
                "Antihistamines",
                "Antihistamines and appetite",
                "Long-term antihistamine use is associated with weight gain in observational studies, likely via H1-receptor affinity increasing appetite. Adequate controlled quantitative data are limited.",
                ref(
                    "Antihistamines",
                    "The weight gain-promoting effects of some antihistamines are thought to be mediated through their affinity for the H1-histamine receptor.",
                ),
            ),
            note(
                f"{p}-n9",
                "Case 1 — semaglutide",
                "How semaglutide breaks the asthma–steroid–obesity cycle",
                "In class III obesity with T2DM, hypertension, hyperlipidemia, and steroid-exacerbated asthma, semaglutide improves glycemia and produces greater weight loss than SGLT-2 inhibitors or DPP-4 inhibitors.",
                ref(
                    "Case 1",
                    "Answer: C) Semaglutide",
                ),
            ),
            note(
                f"{p}-n10",
                "Case 2 — cariprazine",
                "Why cariprazine may drive post-bariatric weight regain",
                "After RYGB, weight regain with worsening diabetes on high-dose insulin may reflect atypical antipsychotic effects. Cariprazine causes weight gain; lisdexamfetamine and buspirone are not major contributors.",
                ref(
                    "Case 2",
                    "Answer: A) Cariprazine",
                ),
            ),
            note(
                f"{p}-n11",
                "Case 3 — propranolol",
                "How to switch migraine prophylaxis to promote weight loss",
                "Rapid weight gain after starting/increasing propranolol in a euthyroid woman suggests beta-blocker effect. Topiramate is FDA approved for migraine prophylaxis, promotes weight loss, and requires reliable contraception due to teratogenicity.",
                ref(
                    "Case 3",
                    "Answer: B) Switch propranolol to topiramate",
                ),
            ),
            note(
                f"{p}-n12",
                "Reproductive hormones",
                "Weight effects of hormonal contraception and androgen therapy",
                "Progesterone-only agents (depot MPA, levonorgestrel IUD) can promote adiposity in women. Testosterone therapy in hypogonadal men improves body composition; androgen deprivation for prostate cancer increases fat mass and metabolic risk.",
                ref(
                    "Reproductive Hormones (Hormonal contraceptives, Hormone Replacement Therapy with Sex Steroids)",
                    "agents can be particularly problematic for women and include progesterone-only formulations such as medroxyprogesterone acetate injections and levonorgestrel containing intrauterine devices.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — diabetes intensification",
                "A woman with class III obesity, T2DM (HbA1c 7.4%), hypertension, hyperlipidemia, and steroid-treated asthma needs a second diabetes agent. Best choice to lower glucose and promote weight loss?",
                [
                    "Sitagliptin",
                    "Pioglitazone",
                    "Semaglutide",
                    "Empagliflozin",
                ],
                2,
                "GLP-1 RAs produce more weight loss (5–10%) than SGLT-2 inhibitors; DPP-4 inhibitors are weight neutral; pioglitazone promotes weight gain.",
                ref(
                    "Case 1",
                    "Answer: C) Semaglutide",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 2 — weight regain",
                "Two years after RYGB, a woman regained 44 lb with HbA1c 10.6% on insulin glargine/lispro, liraglutide, metformin, lisdexamfetamine, buspirone, cariprazine, and fexofenadine. Which drug most likely contributes to regain?",
                [
                    "Cariprazine",
                    "Lisdexamfetamine",
                    "Buspirone",
                    "Fexofenadine",
                ],
                0,
                "Cariprazine is an atypical antipsychotic associated with weight gain; others listed are weight neutral or weight losing.",
                ref(
                    "Case 2",
                    "Answer: A) Cariprazine",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 3 — migraine and weight",
                "A euthyroid woman gained >10% body weight after sertraline and escalating propranolol for migraines. Best next step?",
                [
                    "Switch sertraline to escitalopram",
                    "Switch propranolol to topiramate",
                    "Increase levothyroxine",
                    "Add liothyronine",
                ],
                1,
                "Propranolol (beta-blocker) promotes weight gain; topiramate treats migraine and promotes weight loss—contraception required.",
                ref(
                    "Case 3",
                    "Answer: B) Switch propranolol to topiramate",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Metformin with antipsychotics",
                "Which agent may mitigate weight gain and insulin resistance from atypical antipsychotics?",
                [
                    "Metformin",
                    "Pioglitazone",
                    "Glibenclamide",
                    "Prednisone",
                ],
                0,
                "Metformin ameliorates metabolic derangements from atypical antipsychotics and promotes mild weight loss.",
                ref(
                    "Diabetes Medications",
                    "Metformin does ameliorate the metabolic derangements associated with newer psychotropic agents, particularly atypical antipsychotics.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "T2DM first-line",
                "Per the chapter, preferred sequencing after metformin for type 2 diabetes emphasizes:",
                [
                    "Sulfonylureas first",
                    "GLP-1 receptor agonist or SGLT-2 inhibitor",
                    "Thiazolidinedione monotherapy",
                    "Insulin before any oral agent",
                ],
                1,
                "Professional societies favor GLP-1 RAs or SGLT-2 inhibitors after metformin for weight-beneficial glycemic control.",
                ref(
                    "Diabetes Medications",
                    "recommend metformin as first-line treatment for type 2 diabetes followed by a GLP-1 receptor agonist or SGLT-2 inhibitor",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Olanzapine weight gain",
                "Typical short-term trial weight gain with olanzapine cited in the chapter is approximately:",
                [
                    "0.2 kg in 3 months",
                    "2.4 kg in 3 months",
                    "10 kg in 1 week",
                    "No weight gain ever",
                ],
                1,
                "Trials show ~2.4 kg in 3 months; clinical practice weight gain can be far greater with prolonged use.",
                ref(
                    "Antidepressants and Antipsychotic Medications",
                    "Olanzapine is associated with the most weight gain overall: 2.4 kg (5 lb) in 3 months in clinical trials",
                ),
            ),
            mcq(
                f"{p}-q7",
                "SGLT-2 weight loss",
                "Average weight loss with SGLT-2 inhibitors in type 2 diabetes is approximately:",
                [
                    "0.5 lb",
                    "5 to 10 lb (2.3 to 4.5 kg)",
                    "30 to 40 lb",
                    "No change",
                ],
                1,
                "SGLT-2 inhibitors typically produce 5–10 lb weight loss—less than injectable GLP-1 RAs.",
                ref(
                    "Diabetes Medications",
                    "SGLT-2 inhibitors have also been associated with weight loss when used to lower glucose levels in type 2 diabetes, with typical weight loss of 5 to 10 lb (2.3 to 4.5 kg).",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Pioglitazone",
                "Why is pioglitazone a poor choice when weight loss is a goal?",
                [
                    "It causes hypoglycemia exclusively",
                    "It stimulates adipocytes and promotes increased fat mass",
                    "It is contraindicated in diabetes",
                    "It abolishes insulin secretion",
                ],
                1,
                "TZDs including pioglitazone increase fat mass despite improving glycemia.",
                ref(
                    "Case 1",
                    "Pioglitazone (Answer B) has been shown to improve fatty liver disease as well as glycemic control, but it promotes weight gain, not weight loss.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Low-dose steroids in RA",
                "Long-term low-dose glucocorticoids for rheumatoid arthritis were associated with what weight change in a cited RCT?",
                [
                    "4% to 8% weight gain",
                    "10% weight loss",
                    "No change",
                    "20% weight loss",
                ],
                0,
                "Even low-dose chronic oral/IV steroids can produce 4–8% weight gain.",
                ref(
                    "Glucocorticoids (Oral, Topical, Inhaled, Intra-articular Injections)",
                    "long-term use of even low-dose glucocorticoids for rheumatoid arthritis in a randomized controlled trial was associated with a 4% to 8% weight gain.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "DPP-4 vs GLP-1",
                "How do DPP-4 inhibitors compare with GLP-1 receptor agonists for weight and glycemia?",
                [
                    "Equal weight loss and glycemic effect",
                    "Less weight loss and less glycemic effect than GLP-1 RAs",
                    "Greater weight loss than GLP-1 RAs",
                    "Contraindicated with metformin",
                ],
                1,
                "DPP-4 inhibitors share the incretin pathway but lack significant weight loss and have less glycemic potency.",
                ref(
                    "Case 1",
                    "The oral DPP-4 inhibitors such as sitagliptin (Answer A) work on the same pathway as GLP-1 receptor agonists, but they are not associated with significant weight loss and have less effect on glycemic control.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Topiramate counseling",
                "Before starting topiramate for migraine in a reproductive-age woman, what is essential?",
                [
                    "Discontinue all antidepressants permanently",
                    "Reliable contraception due to teratogenicity",
                    "High-dose levothyroxine",
                    "Avoid all physical activity",
                ],
                1,
                "Topiramate is teratogenic; reliable contraception is mandatory in reproductive-age women.",
                ref(
                    "Case 3",
                    "As a reproductive-aged woman, it is important that she use reliable contraception if she were to start topiramate, as this drug can have teratogenic effects on a developing fetus.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Weight-neutral SSRIs",
                "Sertraline and escitalopram are categorized in the chapter as:",
                [
                    "Weight gain promoting",
                    "Weight neutral",
                    "Mandatory for weight loss",
                    "Contraindicated in obesity",
                ],
                1,
                "Both sertraline and escitalopram are considered weight neutral—switching between them will not aid weight loss.",
                ref(
                    "Case 3",
                    "Both sertraline and escitalopram are considered to be weight neutral",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Chronic weight-promoting drugs",
                "Which scenario poses the greatest long-term weight risk?",
                [
                    "5-day prednisone burst for asthma yearly",
                    "Years of atypical antipsychotic plus insulin for T2DM",
                    "Single dose antihistamine",
                    "One week metformin trial",
                ],
                1,
                "Chronic medications for chronic diseases produce sustained adiposity exposure; brief steroids are less cumulative.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "The most problematic weight-promoting medications are those that are used to treat chronic diseases, which means the patient is exposed to weight-promoting medications over long periods.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Polypharmacy",
                "Multiple weight-neutral medications can never combine to cause clinically significant weight gain.",
                False,
                "Polypharmacy with small individual effects can sum to greater weight gain.",
                ref(
                    "Main Conclusions",
                    "Polypharmacy can also be a problem when a patient is prescribed multiple medications, each of which may have a relatively small individual effect, but which may result in greater weight gain when used concomitantly.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Metformin",
                "Metformin is commonly associated with mild weight loss (~3%–4%) in most patients.",
                True,
                "Metformin is not FDA approved for weight loss but commonly produces mild weight reduction.",
                ref(
                    "Diabetes Medications",
                    "Although metformin is not FDA approved for weight loss, it is commonly associated with mild weight loss (3%-4%) in most patients",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Inhaled steroids",
                "Chronic inhaled glucocorticoids cannot contribute to weight gain because they lack systemic absorption.",
                False,
                "Inhaled/enteral steroids can suppress the HPA axis, implying sufficient systemic absorption to affect weight and metabolism.",
                ref(
                    "Glucocorticoids (Oral, Topical, Inhaled, Intra-articular Injections)",
                    "all have been implicated in secondary adrenal insufficiency. This suggests sufficient systemic absorption to suppress the hypothalamic-pituitary-adrenal axis and therefore sufficient absorption to contribute to weight gain",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Aripiprazole",
                "Aripiprazole is always strictly weight neutral with no weight gain in any patient.",
                False,
                "Aripiprazole is classified weight neutral but can cause ~9–10 lb gain and more in sensitive individuals.",
                ref(
                    "Case 2",
                    "Some agents are classified as weight neutral, such as aripiprazole, but these agents are associated with mild weight gain of approximately 9 to 10 lb (4-4.5 kg) in general",
                ),
            ),
            tf(
                f"{p}-tf5",
                "GLP-1 weight loss",
                "Injectable GLP-1 receptor agonists are associated with more weight loss than oral SGLT-2 inhibitors.",
                True,
                "GLP-1 RAs produce 5–10% body mass loss versus ~5–10 lb with SGLT-2 inhibitors.",
                ref(
                    "Case 1",
                    "Injectable GLP-1 receptor agonists are associated with more weight loss (5%-10% of body mass) than the oral SGLT-2 inhibitors such as empagliflozin (Answer D)",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Beta blockers",
                "Beta-adrenergic blockers are among medication classes associated with weight gain.",
                True,
                "Beta-blockers for cardiovascular indications are less recognized but important weight-promoting agents.",
                ref(
                    "Significance of the Clinical Problem",
                    "β-adrenergic blockers used to treat heart disease, heart rhythm disorders, and hypertension",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Weight loss and comorbidities",
                "Weight loss can improve asthma, type 2 diabetes, hypertension, NAFLD, and sleep apnea.",
                True,
                "Multiple obesity-related conditions improve with weight reduction.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Many other chronic conditions have been shown to improve with weight loss including type 2 diabetes, hypertension, dyslipidemia, metabolic syndrome, cardiovascular disease, osteoarthritis, nonalcoholic fatty liver disease, and sleep apnea.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Topiramate adjunct",
                "Topiramate may promote weight loss and improve glucose metabolism when used with antipsychotics.",
                True,
                "Topiramate is an option beyond metformin for antipsychotic-associated weight/metabolic effects.",
                ref(
                    "Antidepressants and Antipsychotic Medications",
                    "Topiramate, FDA approved for use in seizure disorders and migraine prophylaxis, has also been shown to promote weight loss and improve glucose metabolism when used in conjunction with antipsychotic medications.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Medication scan",
                "Assertion: Reviewing medication lists for weight-promoting drugs is a first step in obesity treatment planning.",
                "Reason: All medications have identical effects on body weight.",
                2,
                "Assertion is true; identical weight effects are false.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "One of the first steps in approaching a treatment plan for patients with overweight or obesity is to review their medication list",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Steroid–asthma cycle",
                "Assertion: Obesity can worsen asthma after glucocorticoid-induced weight gain.",
                "Reason: Weight gain never affects pulmonary disease.",
                2,
                "Assertion describes a vicious cycle; weight affecting asthma is false as stated.",
                ref(
                    "Glucocorticoids (Oral, Topical, Inhaled, Intra-articular Injections)",
                    "Steroid use can help control asthma, but weight gain and obesity can then make asthma worse.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Semaglutide",
                "Assertion: Semaglutide is preferred over sitagliptin when weight loss and glycemic improvement are both needed.",
                "Reason: DPP-4 inhibitors produce greater weight loss than GLP-1 receptor agonists.",
                2,
                "Assertion is true; the reason reverses the weight effects of the drug classes.",
                ref(
                    "Case 1",
                    "The oral DPP-4 inhibitors such as sitagliptin (Answer A) work on the same pathway as GLP-1 receptor agonists, but they are not associated with significant weight loss",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Cariprazine",
                "Assertion: Cariprazine may contribute to post-bariatric weight regain in Case 2.",
                "Reason: All atypical antipsychotics are strictly weight neutral.",
                2,
                "Assertion is true; universal weight neutrality of antipsychotics is false.",
                ref(
                    "Case 2",
                    "Cariprazine (Answer A) is known to cause weight gain",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Propranolol",
                "Assertion: Propranolol may contribute to weight gain in Case 3.",
                "Reason: Beta-adrenergic blockers are associated with weight gain.",
                0,
                "Both are true and consistent with the case timeline.",
                ref(
                    "Case 3",
                    "Propranolol, a β-adrenergic blocker, is commonly used to reduce the frequency of migraines, but this medication class is associated with weight gain.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Insulin in T2DM",
                "Assertion: High-dose insulin in type 2 diabetes can worsen insulin resistance via weight gain.",
                "Reason: Insulin is a catabolic hormone that promotes weight loss.",
                2,
                "Assertion is true; insulin is anabolic and promotes weight gain—the reason is false.",
                ref(
                    "Diabetes Medications",
                    "Insulin use in type 2 diabetes, which is strongly associated with overweight/obesity and insulin resistance, can be particularly detrimental.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Antihistamines",
                "Assertion: Long-term antihistamine use has been associated with weight gain in observational studies.",
                "Reason: Antihistamines decrease appetite via H1 receptor agonism.",
                2,
                "Assertion is true; H1 antagonism increases appetite—the reason is false.",
                ref(
                    "Antihistamines",
                    "Long-term use of antihistamines, including over-the-counter antihistamines, has been associated with weight gain in observational studies",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Testosterone",
                "Assertion: Testosterone therapy in hypogonadal men can improve body composition.",
                "Reason: Testosterone increases adipose tissue and decreases lean mass.",
                2,
                "Assertion is true; the reason describes the opposite of testosterone's effect on composition.",
                ref(
                    "Reproductive Hormones (Hormonal contraceptives, Hormone Replacement Therapy with Sex Steroids)",
                    "treatment with testosterone can improve body composition with loss of adipose tissue and gain of lean muscle mass.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "3",
        "title": "Managing Weight Effects of Medications to Optimize Health in Patients With Overweight/Obesity",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Andrea D. Coviello, MD, MSc, MMCi, FACE",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_03_Managing_Weight_Effects_of_Medications_to_Optimize_Health_in_Patients_With_OverweightObesity.md",
        "items": items,
    }


def build_chapter_04() -> dict:
    p = "e21-04"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Bariatric surgery efficacy",
                "Why bariatric surgery is the most effective obesity treatment",
                "Bariatric surgery produces 20–35% weight loss and dramatically improves weight-related comorbidities, especially type 2 diabetes. Evidence shows reduced cancer and cardiovascular mortality with modern low perioperative risk.",
                ref(
                    "Main Conclusions",
                    "Bariatric surgery is the most effective treatment currently available for weight loss, and it dramatically improves weight-related comorbidities, especially type 2 diabetes mellitus (T2DM).",
                ),
            ),
            note(
                f"{p}-n2",
                "Treatment options",
                "How lifestyle, medications, and surgery compare for obesity",
                "Lifestyle yields ~3–8% loss; antiobesity medications add ~3–10% beyond lifestyle; surgery provides 20–35% loss. Each shows wide interindividual variability.",
                ref(
                    "Significance of the Clinical Problem",
                    "Lifestyle treatment alone typically provides 3% to 8% weight loss depending on the intensity of treatment",
                ),
            ),
            note(
                f"{p}-n3",
                "Procedure trends",
                "Current bariatric procedure distribution in the United States",
                "Vertical sleeve gastrectomy accounts for ~61% of cases; RYGB ~17%; adjustable gastric banding is rarely performed; BPD/DS offers greatest weight loss but highest nutritional risk.",
                ref(
                    "Significance of the Clinical Problem",
                    "VSG is now the most common operation performed, accounting for 61% of all bariatric surgeries.",
                ),
            ),
            note(
                f"{p}-n4",
                "Surgical indications",
                "BMI thresholds for bariatric surgery consideration",
                "Consider surgery for BMI >40 kg/m², or BMI >35 kg/m² with weight-related comorbidity. Growing evidence supports benefit in T2DM with BMI 30–35 when glycemia remains uncontrolled despite aggressive medical therapy.",
                ref(
                    "Significance of the Clinical Problem",
                    "Bariatric surgery (adjustable gastric banding [AGB], vertical sleeve gastrectomy [VSG], Roux-en-Y gastric bypass [RYGB], and biliopancreatic diversion with duodenal switch [BPD/DS]) provides 20% to 35% weight loss and is appropriate to consider in patients with a BMI greater than 40 kg/m² or in those with a BMI greater than 35 kg/m² who also have a weight-related comorbidity",
                ),
            ),
            note(
                f"{p}-n5",
                "Preoperative optimization",
                "How endocrinologists optimize patients before bariatric surgery",
                "Screen vitamin deficiencies; optimize T2DM (HbA1c <8%), sleep apnea, and comorbidities; counsel on lifelong supplementation, avoiding NSAIDs/smoking, and pregnancy prevention for 12–18 months postoperatively.",
                ref(
                    "Main Conclusions",
                    "Preoperative evaluation includes screening for preexisting vitamin deficiencies; optimizing medical conditions such as T2DM and sleep apnea",
                ),
            ),
            note(
                f"{p}-n6",
                "Perioperative safety",
                "Why modern bariatric surgery perioperative risk is acceptable",
                "MBSAQIP-accredited laparoscopic programs report ~0.1% mortality—lower than laparoscopic cholecystectomy (0.7%) or hip replacement (0.93%). 30-day RYGB complication rates are comparable to common elective surgeries.",
                ref(
                    "Risks",
                    "Currently, when performed by an accredited program, bariatric surgery has a lower mortality rate than that seen with laparoscopic cholecystectomy or hip replacement (0.1%, 0.7%, and 0.93%, respectively).",
                ),
            ),
            note(
                f"{p}-n7",
                "Postoperative medications",
                "How to adjust diabetes and BP medications immediately after surgery",
                "Stop scheduled insulin and use correction doses; avoid sulfonylureas. Cut antihypertensives in half and stop diuretics to prevent hypovolemia. Use liquid/crushed meds—avoid extended-release formulations.",
                ref(
                    "Medication Management",
                    "in the immediate postoperative period it is best to stop scheduled insulin and just use correction-factor insulin for high glucose levels.",
                ),
            ),
            note(
                f"{p}-n8",
                "Wernicke encephalopathy",
                "How to recognize and treat post-bariatric thiamine deficiency",
                "Wernicke encephalopathy presents 1–3 weeks postoperatively after protracted vomiting with ataxia, nystagmus, and confusion. Treat with parenteral thiamine 250–600 mg daily; prevention requires adequate thiamine beyond standard multivitamins.",
                ref(
                    "Thiamine Deficiency",
                    "Treatment consists of parenteral thiamine administration of 250 to 600 mg daily depending on the severity of the symptoms.",
                ),
            ),
            note(
                f"{p}-n9",
                "Long-term micronutrients",
                "How to monitor vitamin and mineral status after bariatric surgery",
                "Monitor B₁₂, D, A, K, iron, copper, zinc, PTH, and bone health per procedure-specific schedules. B₁₂ deficiency may take >1 year; methylmalonic acid is more sensitive than serum B₁₂ alone.",
                ref(
                    "Vitamin B₁₂",
                    "Simply testing serum vitamin B₁₂ levels may not be sufficiently sensitive to detect deficiency. Methylmalonic acid levels are a more sensitive measure of vitamin B₁₂ deficiency.",
                ),
            ),
            note(
                f"{p}-n10",
                "Weight regain",
                "How to evaluate significant post-bariatric weight regain",
                "Significant regain (~20% of lost weight) may signal mechanical surgical problems, lifestyle relapse, or medication effects. Upper GI series/endoscopy is indicated when abrupt appetite return follows years of stability—especially after band or dilated pouch.",
                ref(
                    "Weight Regain Following Weight-Loss Surgery",
                    "The value that they determined was return of 20% of the lost weight.",
                ),
            ),
            note(
                f"{p}-n11",
                "Post-bariatric hypoglycemia",
                "Post-bariatric hypoglycemia diagnosis and first-line therapy",
                "Symptomatic hypoglycemia 1–3 hours postprandially, typically 1–4 years after RYGB. Mixed-meal testing or CGM is preferred over OGTT; first-line therapy is frequent small low-GI mixed meals emphasizing protein.",
                ref(
                    "Post-Bariatric Surgery Hypoglycemia",
                    "First-line therapy is frequent small mixed meals with low-glycemic index carbohydrates that emphasize protein.",
                ),
            ),
            note(
                f"{p}-n12",
                "T2DM outcomes",
                "Microvascular and macrovascular benefits of bariatric surgery in T2DM",
                "Meta-analyses show ~74% reduction in microvascular complications vs medical therapy and ~48% reduction in macrovascular complications with ~79% lower 5-year mortality in large observational datasets.",
                ref(
                    "Microvascular and Macrovascular Disease",
                    "bariatric surgery reduced the risk of microvascular complications by 74% compared with medical therapy.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — Wernicke",
                "Three weeks after RYGB, a man has progressive vomiting then confusion, ataxia, and abnormal eye movements. Most likely deficiency?",
                [
                    "Vitamin B₁₂",
                    "Vitamin A",
                    "Thiamine",
                    "Copper",
                ],
                2,
                "Acute Wernicke encephalopathy from thiamine deficiency is a medical emergency days to weeks postoperatively with vomiting.",
                ref(
                    "Case 1",
                    "Answer: C) Thiamine",
                ),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — treatment",
                "For Wernicke encephalopathy after bariatric surgery, initial management includes:",
                [
                    "Oral multivitamin only",
                    "Parenteral thiamine 200 mg TID for 3–5 days",
                    "High-dose vitamin A IM daily",
                    "Copper infusion routinely",
                ],
                1,
                "Parenteral thiamine is urgent treatment; oral OTC multivitamins alone are insufficient acutely.",
                ref(
                    "Case 1",
                    "the person should be treated with parenteral thiamine (200 mg 3 times daily for 3-5 days).",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — band complication",
                "A woman with prior AGB presents with weight regain, abdominal pain, nausea, and port-site erythema/tenderness. Most likely diagnosis?",
                [
                    "Bowel obstruction",
                    "Band erosion",
                    "Staple line dehiscence",
                    "Anastomotic leak",
                ],
                1,
                "Band erosion through the gastric wall with tracking along the port cannula causes port-site inflammation—classic late AGB complication.",
                ref(
                    "Case 2",
                    "Answer: B) Band erosion",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Surgery indications",
                "Bariatric surgery is appropriate to consider for:",
                [
                    "BMI >25 kg/m² without comorbidities",
                    "BMI >40 kg/m² or BMI >35 kg/m² with weight-related comorbidity",
                    "Any patient requesting cosmetic weight loss only",
                    "BMI >20 kg/m²",
                ],
                1,
                "Standard thresholds are BMI >40 or >35 with comorbidity.",
                ref(
                    "Significance of the Clinical Problem",
                    "appropriate to consider in patients with a BMI greater than 40 kg/m² or in those with a BMI greater than 35 kg/m² who also have a weight-related comorbidity",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Most common procedure",
                "Which bariatric procedure is now most commonly performed in the United States?",
                [
                    "Adjustable gastric banding",
                    "Vertical sleeve gastrectomy",
                    "Biliopancreatic diversion with duodenal switch",
                    "Open vertical banded gastroplasty",
                ],
                1,
                "VSG accounts for ~61% of bariatric operations.",
                ref(
                    "Significance of the Clinical Problem",
                    "VSG is now the most common operation performed, accounting for 61% of all bariatric surgeries.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Perioperative mortality",
                "Mortality for bariatric surgery in accredited laparoscopic programs is approximately:",
                [
                    "5%",
                    "0.1%",
                    "2%",
                    "10%",
                ],
                1,
                "Accredited bariatric surgery mortality ~0.1%, lower than cholecystectomy or hip replacement.",
                ref(
                    "Risks",
                    "bariatric surgery has a lower mortality rate than that seen with laparoscopic cholecystectomy or hip replacement (0.1%, 0.7%, and 0.93%, respectively).",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Postop insulin",
                "Immediately after bariatric surgery in a patient with T2DM, insulin management should:",
                [
                    "Double all basal insulin doses",
                    "Stop scheduled insulin and use correction insulin for hyperglycemia",
                    "Continue sulfonylureas for convenience",
                    "Start SGLT-2 inhibitor at full dose day 1",
                ],
                1,
                "Glucose improves rapidly postoperatively; scheduled insulin risks hypoglycemia—use correction doses only initially.",
                ref(
                    "Medication Management",
                    "it is best to stop scheduled insulin and just use correction-factor insulin for high glucose levels.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Pregnancy counseling",
                "How long should pregnancy be avoided after bariatric surgery?",
                [
                    "1 month",
                    "12 to 18 months",
                    "5 years mandatory",
                    "No restriction",
                ],
                1,
                "Pregnancy should be avoided for 12–18 months following the procedure.",
                ref(
                    "Main Conclusions",
                    "Pregnancy should be avoided for 12 to 18 months following the procedure.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "B₁₂ monitoring",
                "Which test is more sensitive than serum B₁₂ alone for detecting deficiency after RYGB/VSG?",
                [
                    "Methylmalonic acid",
                    "Serum folate only",
                    "TSH",
                    "HbA1c",
                ],
                0,
                "Methylmalonic acid detects B₁₂ deficiency earlier than serum B₁₂.",
                ref(
                    "Vitamin B₁₂",
                    "Methylmalonic acid levels are a more sensitive measure of vitamin B₁₂ deficiency.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Vitamin D dosing",
                "Recommended daily vitamin D intake after bariatric surgery to maintain 25-OH vitamin D >30 ng/mL is:",
                [
                    "400 IU",
                    "3000 IU",
                    "50 IU",
                    "No supplementation needed",
                ],
                1,
                "All post-bariatric patients should consume 3000 IU vitamin D daily; some need much higher doses.",
                ref(
                    "Vitamin D",
                    "All patients who have had bariatric surgery should consume 3000 IU of vitamin D daily to maintain 25-hydroxyvitamin D levels greater than 30 ng/mL",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Calcium form",
                "Preferred calcium supplement after bariatric surgery is:",
                [
                    "Calcium carbonate on empty stomach",
                    "Calcium citrate",
                    "No calcium ever needed",
                    "Intravenous calcium only",
                ],
                1,
                "Calcium citrate is preferred because carbonate requires stomach acid for absorption.",
                ref(
                    "Calcium",
                    "Because calcium carbonate is not well absorbed in the absence of stomach acid, calcium citrate is the preferred form for supplementation.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Weight regain threshold",
                "A study cited in the chapter defined clinically significant weight regain after bariatric surgery as:",
                [
                    "Any 2-lb increase",
                    "Return of 20% of weight lost",
                    "50% regain only",
                    "Regain only if BMI exceeds 50",
                ],
                1,
                "Regain of 20% of lost weight was associated with comorbidity recurrence risk.",
                ref(
                    "Weight Regain Following Weight-Loss Surgery",
                    "The value that they determined was return of 20% of the lost weight.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Hypertension remission",
                "After bariatric surgery, hypertension remission at 1 year occurs in approximately what proportion of affected patients?",
                [
                    "5%",
                    "43% to 83%",
                    "100% permanently",
                    "0%—surgery never affects blood pressure",
                ],
                1,
                "Remission occurs in 43–83% at 1 year, though recurrence can occur within 10 years.",
                ref(
                    "Hypertension",
                    "surgery results in remission of hypertension in 43% to 83% of affected individuals at 1 year.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Obesity as disease",
                "Obesity is generally accepted by professional organizations as a disease of body weight regulation.",
                True,
                "Obesity is a chronic disease, not simply a lifestyle choice.",
                ref(
                    "Significance of the Clinical Problem",
                    "obesity is now generally accepted by virtually all professional organizations to be a disease of body weight regulation.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "AGB popularity",
                "Adjustable gastric banding is now rarely performed because efficacy is lower and complications higher than initially appreciated.",
                True,
                "AGB use has declined markedly.",
                ref(
                    "Significance of the Clinical Problem",
                    "AGB procedures are rarely performed any more, as efficacy is lower and complications are higher than had initially been appreciated.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "NSAIDs postop",
                "Nonsteroidal anti-inflammatory drugs should be avoided after bariatric surgery because of anastomotic ulcer risk.",
                True,
                "NSAIDs are contraindicated postoperatively.",
                ref(
                    "Management of Associated Health Conditions",
                    "Those with degenerative joint disease should be transitioned off nonsteroidal antiinflammatory agents preoperatively, as these are contraindicated in the postoperative period.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Anastomotic leak timing",
                "Anastomotic leak typically presents 3 to 4 days after surgery with tachycardia, fever, and shoulder pain.",
                True,
                "Early postoperative leak is a surgical emergency with characteristic presentation.",
                ref(
                    "Anastomotic Leak",
                    "This problem typically presents 3 to 4 days following surgery.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Cancer risk reduction",
                "Bariatric surgery is associated with reduced risk of obesity-associated cancers in large observational datasets.",
                True,
                "Data from >630,000 patients suggest ~45% reduced risk of obesity-associated cancers.",
                ref(
                    "Cancer",
                    "bariatric surgery is associated with a 28% reduced risk for developing all types of cancer, a 45% reduced risk of obesity-associated cancers",
                ),
            ),
            tf(
                f"{p}-tf6",
                "6-month diet program",
                "Six months of mandatory preoperative supervised weight loss improves long-term bariatric outcomes.",
                False,
                "Insurance-required 6-month programs lack evidence for improving long-term outcomes.",
                ref(
                    "Nutritional Evaluation",
                    "there is no evidence that this practice improves long-term outcomes.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "GLP-1 after surgery",
                "GLP-1 receptor agonists appear effective for weight loss in patients who have had bariatric surgery.",
                True,
                "Studies suggest GLP-1 RAs work similarly post-surgery as in nonsurgical patients.",
                ref(
                    "Weight Regain Following Weight-Loss Surgery",
                    "GLP-1 receptor agonist medications work just as well in patients following bariatric surgery as they do in nonsurgically treated patients.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Sleep apnea",
                "Bariatric surgery eliminates obstructive sleep apnea in all patients.",
                False,
                "AHI improves substantially but many patients retain clinically significant apnea.",
                ref(
                    "Sleep Apnea",
                    "While bariatric surgery can help many patients with sleep apnea, many are still left with clinically significant apnea.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Surgery efficacy",
                "Assertion: Bariatric surgery provides greater sustained weight loss than lifestyle or antiobesity medications alone.",
                "Reason: Lifestyle typically achieves 3–8% weight loss while surgery achieves 20–35%.",
                0,
                "Both are true and quantitatively linked.",
                ref(
                    "Significance of the Clinical Problem",
                    "Bariatric surgery (adjustable gastric banding [AGB], vertical sleeve gastrectomy [VSG], Roux-en-Y gastric bypass [RYGB], and biliopancreatic diversion with duodenal switch [BPD/DS]) provides 20% to 35% weight loss",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Wernicke",
                "Assertion: Wernicke encephalopathy after bariatric surgery requires urgent parenteral thiamine.",
                "Reason: Thiamine stores are depleted rapidly after prolonged postoperative vomiting.",
                0,
                "Both are true; vomiting predisposes to acute thiamine deficiency.",
                ref(
                    "Thiamine Deficiency",
                    "This typically presents 1 to 3 weeks following surgery in a patient who has several days of severe nausea and vomiting",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Band erosion",
                "Assertion: Port-site erythema in a patient with AGB suggests possible band erosion.",
                "Reason: AGB has no mechanical components that can fail.",
                2,
                "Assertion matches Case 2; bands are mechanical and can erode.",
                ref(
                    "Case 2",
                    "Stomach contents then track up the inflation cannula causing skin redness in the area of the port.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "B₁₂ timing",
                "Assertion: Vitamin B₁₂ deficiency usually appears within days after bariatric surgery.",
                "Reason: Body stores of B₁₂ are large and deficiency may take a year or more to develop.",
                2,
                "Assertion is false; large stores delay deficiency—the reason is true.",
                ref(
                    "Case 1",
                    "Vitamin B₁₂ deficiency (Answer A) can cause neurologic symptoms, but because of the large storage capacity of the body, deficiency usually does not appear until a year or 2 following surgery.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "T2DM preop",
                "Assertion: HbA1c should ideally be less than 8.0% before elective bariatric surgery in patients with T2DM.",
                "Reason: Hyperglycemia has no bearing on surgical outcomes.",
                2,
                "Assertion is true per chapter; ignoring glycemia is false.",
                ref(
                    "Management of Associated Health Conditions",
                    "Ideally, hemoglobin A₁c levels should be less than 8.0% before surgery in those with T2DM.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Mortality benefit",
                "Assertion: Long-term all-cause mortality is reduced after bariatric surgery compared with matched nonsurgical controls.",
                "Reason: Short-term perioperative mortality is slightly higher because of surgical risk.",
                1,
                "Both are true: early perioperative mortality is slightly higher, but that does not explain long-term mortality reduction seen by 5–10 years.",
                ref(
                    "Overall Mortality",
                    "by 5 to 10 years following surgery, several observational studies show reduced all-cause mortality in surgically treated patients as compared with matched patients who did not have surgery.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Post-bariatric hypoglycemia",
                "Assertion: Oral glucose tolerance testing is a poor diagnostic test for post-bariatric hypoglycemia.",
                "Reason: Many postoperative patients have abnormal OGTT without true post-bariatric hypoglycemia.",
                0,
                "Both are true and causally linked.",
                ref(
                    "Post-Bariatric Surgery Hypoglycemia",
                    "An oral glucose tolerance test is not a good diagnostic test, as many postsurgical patients will have abnormal values on this test and not have post-bariatric surgery hypoglycemia.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Contraception postop",
                "Assertion: Oral contraceptives may be less effective and thrombogenic after bariatric surgery.",
                "Reason: IUDs or other nonoral options may be preferable in the postoperative period.",
                0,
                "Both are true; altered absorption and thrombosis risk support alternative contraception.",
                ref(
                    "Management of Associated Health Conditions",
                    "Oral contraceptives may be less effective and may predispose to thromboembolic disease following bariatric surgery, so other options such as an intrauterine device might be considered.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "4",
        "title": "What an Endocrinologist Should Know About the Surgical Treatment of Obesity",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Daniel H. Bessesen, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_04_What_an_Endocrinologist_Should_Know_About_the_Surgical_Treatment_of_Obesity.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_01_When_Should_You_Order_Advanced_Lipoprotein_Testing.json": build_chapter_01,
    "endo2021_chapter_02_Challenging_Cases_in_Nutritional_and_Medical_Treatment_of_Obesity.json": build_chapter_02,
    "endo2021_chapter_03_Managing_Weight_Effects_of_Medications_to_Optimize_Health_in_Patients_With_OverweightObesity.json": build_chapter_03,
    "endo2021_chapter_04_What_an_Endocrinologist_Should_Know_About_the_Surgical_Treatment_of_Obesity.json": build_chapter_04,
}


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

