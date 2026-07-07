#!/usr/bin/env python3
"""Generate remediated ESAP 2021 modules e21-09 through e21-15."""
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


def build_chapter_09() -> dict:
    """Bone and mineral metabolism overview — sourced from ch11 intro (ch09 MD is title-only)."""
    p = "e21-09"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Clinical approach",
                "Why bone and mineral disorders need both protocol and individualization",
                "Common pathologies such as osteoporosis may follow formulaic fracture-risk assessment, but rarer diseases and rare events in common conditions demand individualized evaluation—relying on a limited investigation set with correct interpretation.",
                ref(
                    "Main Conclusions",
                    "Pathologies in bone and mineral metabolism are common and may require a formulaic approach, such as protocolized assessment of fracture risk in osteoporosis.",
                ),
            ),
            note(
                f"{p}-n2",
                "Mineral workup",
                "How to begin evaluation of mineral metabolism disorders",
                "Serum calcium (albumin-adjusted), phosphate, alkaline phosphatase, PTH, and 25-hydroxyvitamin D usually identify the underlying disorder; plasma magnesium and urinary calcium excretion add useful discrimination.",
                ref(
                    "Mineral Disease",
                    "Serum calcium adjusted for albumin phosphate, alkaline phosphatase, PTH, and 25-hydroxyvitamin D usually provide pointers to underlying disorders of mineral homeostasis.",
                ),
            ),
            note(
                f"{p}-n3",
                "FHH vs PHPT",
                "Why genetic testing now complements the calcium/creatinine clearance ratio",
                "Fasting renal calcium-to-creatinine clearance ratio traditionally distinguished FHH from primary hyperparathyroidism, but readily available genetic panel testing for FHH can now aid the differential.",
                ref(
                    "Mineral Disease",
                    "Traditionally, estimating the ratio of renal clearance of calcium to that of creatinine in the fasting state has been central to distinguishing familial hypocalciuric hypercalcemia (FHH) from primary hyperparathyroidism.",
                ),
            ),
            note(
                f"{p}-n4",
                "Active vitamin D",
                "When measurement of 1,25-dihydroxyvitamin D is occasionally justified",
                "Routine active vitamin D measurement is rarely indicated but can help in extrarenal 1,25-dihydroxyvitamin D synthesis disorders such as sarcoidosis.",
                ref(
                    "Mineral Disease",
                    "Measurement of the active form of vitamin D, is very rarely indicated but it occasionally can be useful in rare conditions of extrarenal synthesis of 1,25-dihydroxyvitamin D, such as sarcoidosis.",
                ),
            ),
            note(
                f"{p}-n5",
                "Calcitonin",
                "Why calcitonin has no role in routine calcium metabolism workup",
                "Calcitonin measurement is confined to medullary thyroid carcinoma diagnosis and monitoring—there is no role in routine investigation of calcium and bone metabolism.",
                ref(
                    "Mineral Disease",
                    "The utility of calcitonin measurement is confined to the diagnosis and monitoring of medullary carcinoma of the thyroid.",
                ),
            ),
            note(
                f"{p}-n6",
                "Bone turnover markers",
                "How biochemical markers of bone turnover support osteoporosis care",
                "Resorption markers (CTX, NTX) and formation markers (P1NP, osteocalcin) may assess fracture risk, accelerated bone loss, treatment response, and poor adherence—though routine clinical utility remains unsettled.",
                ref(
                    "Bone Disease",
                    "Biochemical markers of bone turnover (resorption markers such as CTX and NTX and formation markers such as P1NP and osteocalcin) may be useful in assessing overall risk of osteoporotic fracture and accelerated bone loss and in judging response to treatments for osteoporosis and hence poor adherence to therapy.",
                ),
            ),
            note(
                f"{p}-n7",
                "DXA interpretation",
                "Why T-scores must never be used as isolated treatment thresholds",
                "DXA reliably predicts fracture risk, but T-scores should always be contextualized within the patient's full fracture-risk profile—not used as standalone treatment triggers.",
                ref(
                    "Bone Disease",
                    "It is important not to consider T-score values in isolation and use them as isolated thresholds for treatment; DXA-determined data should always be contextualized to the full fracture risk profile of the patient.",
                ),
            ),
            note(
                f"{p}-n8",
                "Skeletal imaging",
                "How plain radiographs and isotope scans complement biochemistry",
                "Plain films detect fractures, Paget disease, and dysplasias but not bone density; isotope scans survey the skeleton for localized disease but require clinical and biochemical triangulation for specific diagnosis.",
                ref(
                    "Bone Disease",
                    "Basic x-rays are not useful for assessing bone density, but the appearance of \"osteopenia\" on a plain film is an indication for a DXA scan.",
                ),
            ),
            note(
                f"{p}-n9",
                "Bone biopsy",
                "When transiliac bone biopsy is appropriate",
                "Bone biopsy is not routine but helps in complex metabolic bone disease—especially unexplained osteomalacia or detailed renal osteodystrophy assessment—and must be done only in specialized centers.",
                ref(
                    "Bone Disease",
                    "Bone biopsy is not a routine test, but it can be helpful in patients with complex metabolic bone diseases, particularly when there is unexplained osteomalacia or a need for detailed assessment of renal osteodystrophy.",
                ),
            ),
            note(
                f"{p}-n10",
                "Diagnostic odyssey",
                "Why genomic techniques may arrive late in challenging cases",
                "Lack of robust discriminatory investigations can hinder diagnosis—as in FHH versus PHPT or tumor-induced osteomalacia localization—delaying genomic engagement beyond the ideal point.",
                ref(
                    "Main Conclusions",
                    "Lack of robust discriminatory investigations may hinder diagnosis or management such as in the case of familial hypocalciuric hypercalcemia and tumor-induced osteomalacia (localization), respectively.",
                ),
            ),
            note(
                f"{p}-n11",
                "Drug harms",
                "Bisphosphonate atypical femoral fractures and denosumab rebound",
                "Awareness of intervention thresholds and rare adverse effects of common drugs is easily overlooked—bisphosphonate-associated atypical femoral fractures and rebound vertebral fractures after denosumab cessation can cause preventable harm.",
                ref(
                    "Main Conclusions",
                    "Awareness of thresholds of intervention for treatment and rare adverse effects of commonly used drugs may be overlooked, potentially causing patient harm, such as bisphosphonate-associated atypical femoral fractures and rebound vertebral fractures with denosumab.",
                ),
            ),
            note(
                f"{p}-n12",
                "CKD-MBD",
                "Why bisphosphonates may be inappropriate in CKD-MBD with low turnover",
                "Unawareness of comorbidity complexity can promote inappropriate prescribing—bisphosphonates in chronic kidney disease-mineral and bone disorder with low bone turnover is a key example.",
                ref(
                    "Main Conclusions",
                    "Lack of awareness of complexities in cases with multiple comorbidities may promote less appropriate prescribing such as inappropriate use of bisphosphonates in the setting of chronic kidney disease-mineral and bone disorder due to low bone turnover.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Initial assessment",
                "A 55-year-old woman has recurrent low-trauma wrist fractures. Before ordering DXA, which initial laboratory panel best screens mineral and bone metabolism disorders?",
                [
                    "Serum calcium, phosphate, ALP, PTH, and 25-hydroxyvitamin D",
                    "Serum calcitonin and PTHrP",
                    "Urinary NTX alone",
                    "1,25-dihydroxyvitamin D and FGF-23 only",
                ],
                0,
                "The standard mineral panel (calcium, phosphate, ALP, PTH, 25-OHD) provides the first-line biochemical pointers; calcitonin and PTHrP are rarely indicated.",
                ref(
                    "Mineral Disease",
                    "Serum calcium adjusted for albumin phosphate, alkaline phosphatase, PTH, and 25-hydroxyvitamin D usually provide pointers to underlying disorders of mineral homeostasis.",
                ),
            ),
            mcq(
                f"{p}-q2",
                "FHH workup",
                "A mildly hypercalcemic patient has low urinary calcium excretion. Fasting calcium/creatinine clearance ratio is borderline. Best next step to distinguish FHH from primary hyperparathyroidism?",
                [
                    "Repeat PTH in 6 months",
                    "Genetic panel testing for FHH",
                    "Emergent parathyroidectomy",
                    "Empiric cinacalcet",
                ],
                1,
                "Genetic panel testing for FHH is now readily accessible and complements the traditional clearance-ratio approach.",
                ref(
                    "Mineral Disease",
                    "with genetic panel testing for FHH being more readily accessible, this approach can also be used to help distinguish the condition from primary hyperparathyroidism.",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Sarcoidosis",
                "A patient with hypercalcemia and granulomatous lung disease has normal 25-hydroxyvitamin D and suppressed PTH. Which test is occasionally useful here?",
                [
                    "Serum calcitonin",
                    "1,25-dihydroxyvitamin D",
                    "Urinary CTX",
                    "Serum PTHrP as first-line in all hypercalcemia",
                ],
                1,
                "Extrarenal 1α-hydroxylation in sarcoidosis makes active vitamin D measurement occasionally useful—unlike routine calcitonin or PTHrP screening.",
                ref(
                    "Mineral Disease",
                    "Measurement of the active form of vitamin D, is very rarely indicated but it occasionally can be useful in rare conditions of extrarenal synthesis of 1,25-dihydroxyvitamin D, such as sarcoidosis.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Plain film",
                "A lumbar spine radiograph report notes 'osteopenia' without fracture. What is the appropriate next imaging step?",
                [
                    "No further imaging — osteopenia on x-ray is diagnostic",
                    "DXA scan",
                    "Isotope bone scan only",
                    "Bone biopsy",
                ],
                1,
                "Plain-film osteopenia is an indication for DXA; x-rays cannot quantify bone density.",
                ref(
                    "Bone Disease",
                    "Basic x-rays are not useful for assessing bone density, but the appearance of \"osteopenia\" on a plain film is an indication for a DXA scan.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "DXA decision",
                "A 68-year-old woman's hip T-score is -2.3. She has no prior fracture and FRAX is below intervention threshold. Best management principle?",
                [
                    "Start bisphosphonate solely because T-score < -2.5",
                    "Contextualize DXA within full fracture-risk profile before treating",
                    "Order bone biopsy to confirm osteoporosis",
                    "Measure calcitonin before any decision",
                ],
                1,
                "T-scores must not be isolated treatment thresholds; full fracture-risk context is required.",
                ref(
                    "Bone Disease",
                    "It is important not to consider T-score values in isolation and use them as isolated thresholds for treatment; DXA-determined data should always be contextualized to the full fracture risk profile of the patient.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "BTM utility",
                "A patient on alendronate has unchanged BMD at 1 year. Which use of bone turnover markers is most supported?",
                [
                    "Screen all adults for osteoporosis",
                    "Assess treatment response and possible nonadherence",
                    "Replace DXA for diagnosis",
                    "Routine annual monitoring in every patient regardless of therapy",
                ],
                1,
                "BTMs may judge treatment response and adherence; routine population screening is not established.",
                ref(
                    "Bone Disease",
                    "Biochemical markers of bone turnover (resorption markers such as CTX and NTX and formation markers such as P1NP and osteocalcin) may be useful in assessing overall risk of osteoporotic fracture and accelerated bone loss and in judging response to treatments for osteoporosis and hence poor adherence to therapy.",
                ),
            ),
            mcq(
                f"{p}-q7",
                "Bone scan",
                "An isotope bone scan shows focal uptake in the pelvis. Next step?",
                [
                    "Diagnose Paget disease and start bisphosphonate immediately",
                    "Triangulate with clinical, biochemical, and anatomic imaging data",
                    "No further workup — scan is diagnostic",
                    "Start teriparatide for focal uptake",
                ],
                1,
                "Isotope uptake is nonspecific; diagnosis requires additional clinical, biochemical, and imaging correlation.",
                ref(
                    "Bone Disease",
                    "Uptake on such imaging is not selective, however, and is not diagnostic of specific bone diseases. Therefore, further triangulation with additional clinical, biochemical, and imaging information is required to reach a diagnosis.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Bone biopsy",
                "A patient has persistent hypophosphatemia, elevated ALP, and fractures despite vitamin D repletion; osteomalacia is suspected but the cause is unclear. Best indication for bone biopsy?",
                [
                    "Routine screening in all postmenopausal women",
                    "Unexplained osteomalacia at a specialized center",
                    "Every patient before starting bisphosphonates",
                    "Isolated low BMD T-score",
                ],
                1,
                "Bone biopsy is reserved for complex metabolic bone disease such as unexplained osteomalacia, performed only in expert centers.",
                ref(
                    "Bone Disease",
                    "Bone biopsy is not a routine test, but it can be helpful in patients with complex metabolic bone diseases, particularly when there is unexplained osteomalacia or a need for detailed assessment of renal osteodystrophy.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "History taking",
                "When evaluating a possible metabolic bone disorder, which history element is especially important?",
                [
                    "Only current medications",
                    "Early-life milestones, skeletal/dental features, and family history",
                    "Travel history exclusively",
                    "Dietary sodium intake only",
                ],
                1,
                "Initial assessment should include developmental milestones, skeletal/dental/systemic features, and family history.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Initial assessment of patients with potential bone and mineral disorders should include a detailed history that incorporates early-life developmental milestones and clinical events.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "TIO localization",
                "A patient has FGF-23-mediated hypophosphatemia but no tumor is found on initial imaging. Key barrier to optimal care?",
                [
                    "Overuse of DXA",
                    "Lack of robust localization investigations delaying definitive therapy",
                    "Excess calcitonin testing",
                    "Routine bone biopsy in all cases",
                ],
                1,
                "Tumor-induced osteomalacia localization is a paradigmatic example where limited discriminatory investigations hinder management.",
                ref(
                    "Main Conclusions",
                    "Lack of robust discriminatory investigations may hinder diagnosis or management such as in the case of familial hypocalciuric hypercalcemia and tumor-induced osteomalacia (localization), respectively.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Atypical femur fracture",
                "A woman on long-term bisphosphonate reports prodromal thigh pain. Plain films show incomplete subtrochanteric fracture. Most important prescribing principle?",
                [
                    "Continue bisphosphonate to complete fracture healing",
                    "Recognize rare adverse effects and reassess risks/benefits individually",
                    "Switch to another antiresorptive without stopping",
                    "Ignore thigh pain if DXA improved",
                ],
                1,
                "Awareness of rare drug adverse effects such as atypical femoral fractures is essential to prevent harm.",
                ref(
                    "Main Conclusions",
                    "Awareness of thresholds of intervention for treatment and rare adverse effects of commonly used drugs may be overlooked, potentially causing patient harm, such as bisphosphonate-associated atypical femoral fractures and rebound vertebral fractures with denosumab.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Denosumab cessation",
                "A patient stops denosumab without follow-on therapy and develops multiple new vertebral fractures. What principle was violated?",
                [
                    "DXA should be repeated weekly",
                    "Anticipating drug offset and planning transition therapy",
                    "Calcitonin should have been measured",
                    "Bone biopsy was mandatory before denosumab",
                ],
                1,
                "Rebound vertebral fractures after denosumab cessation exemplify harm from overlooking drug offset.",
                ref(
                    "Main Conclusions",
                    "rebound vertebral fractures with denosumab.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "CKD-MBD",
                "A dialysis patient with adynamic bone disease and low turnover is referred for 'osteoporosis treatment.' Best response?",
                [
                    "Start high-dose bisphosphonate immediately",
                    "Avoid inappropriate bisphosphonate use in low-turnover CKD-MBD",
                    "Give teriparatide without monitoring",
                    "Measure calcitonin to guide therapy",
                ],
                1,
                "Bisphosphonates may be inappropriate when CKD-MBD features low bone turnover.",
                ref(
                    "Main Conclusions",
                    "inappropriate use of bisphosphonates in the setting of chronic kidney disease-mineral and bone disorder due to low bone turnover.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "DXA",
                "DXA T-scores should be used as isolated thresholds to initiate osteoporosis treatment.",
                False,
                "T-scores must be contextualized within the full fracture-risk profile, not used alone.",
                ref(
                    "Bone Disease",
                    "It is important not to consider T-score values in isolation and use them as isolated thresholds for treatment",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Calcitonin",
                "Calcitonin measurement is part of the routine investigation of disorders of calcium and bone metabolism.",
                False,
                "Calcitonin is confined to medullary thyroid carcinoma diagnosis and monitoring.",
                ref(
                    "Mineral Disease",
                    "There is no role for calcitonin measurement in the routine investigation of calcium and bone metabolism.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Plain radiographs",
                "Plain skeletal radiographs are reliable for quantifying bone mineral density.",
                False,
                "Basic x-rays are not useful for assessing bone density.",
                ref(
                    "Bone Disease",
                    "Basic x-rays are not useful for assessing bone density",
                ),
            ),
            tf(
                f"{p}-tf4",
                "BTMs",
                "Bone turnover markers may help identify poor adherence to osteoporosis therapy.",
                True,
                "BTMs can reflect treatment response and poor adherence, though routine clinical utility is not fully established.",
                ref(
                    "Bone Disease",
                    "in judging response to treatments for osteoporosis and hence poor adherence to therapy.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Active vitamin D",
                "Measurement of 1,25-dihydroxyvitamin D is routinely indicated in all patients with hypercalcemia.",
                False,
                "Active vitamin D measurement is very rarely indicated except in select conditions such as sarcoidosis.",
                ref(
                    "Mineral Disease",
                    "Measurement of the active form of vitamin D, is very rarely indicated",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Isotope scans",
                "Increased uptake on an isotope bone scan is diagnostic of a specific bone disease without further workup.",
                False,
                "Uptake is not selective; triangulation with other data is required.",
                ref(
                    "Bone Disease",
                    "Uptake on such imaging is not selective, however, and is not diagnostic of specific bone diseases.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Genomics",
                "Genetic techniques may be engaged later than ideal in some diagnostic odysseys.",
                True,
                "Limited discriminatory tools can delay genomic diagnosis in challenging cases.",
                ref(
                    "Main Conclusions",
                    "Use of genomic techniques may be engaged later than ideal in the diagnostic odyssey.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Individualized care",
                "Individualized care in rare bone and mineral diseases can be highly variable and opinion based.",
                True,
                "Rare diseases require individualized approaches beyond formulaic protocols.",
                ref(
                    "Main Conclusions",
                    "Individualized care can be highly variable and opinion based.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "DXA",
                "Assertion: A hip T-score of -2.6 alone mandates pharmacologic osteoporosis therapy.",
                "Reason: DXA is a reliable measure of bone strength that predicts fracture risk.",
                1,
                "Both may be true in isolation, but R does not justify treating on T-score alone—full risk context is required.",
                ref(
                    "Bone Disease",
                    "DXA-determined data should always be contextualized to the full fracture risk profile of the patient.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Calcitonin",
                "Assertion: Calcitonin should be measured in every patient with hypercalcemia.",
                "Reason: Calcitonin is useful for monitoring medullary thyroid carcinoma.",
                2,
                "R is true in its limited context, but A is false—calcitonin has no routine role in calcium metabolism workup.",
                ref(
                    "Mineral Disease",
                    "There is no role for calcitonin measurement in the routine investigation of calcium and bone metabolism.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Osteopenia on x-ray",
                "Assertion: Osteopenia reported on plain radiographs warrants DXA scanning.",
                "Reason: Plain radiographs cannot reliably assess bone density.",
                0,
                "Both true and causally linked—radiographic osteopenia prompts DXA because x-rays do not quantify density.",
                ref(
                    "Bone Disease",
                    "the appearance of \"osteopenia\" on a plain film is an indication for a DXA scan.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "FHH",
                "Assertion: Genetic testing can help distinguish FHH from primary hyperparathyroidism.",
                "Reason: Fasting urinary calcium/creatinine clearance ratio has traditionally been used for this distinction.",
                1,
                "Both true, but the clearance ratio is not the correct explanation for why genetic testing helps—each is an independent tool.",
                ref(
                    "Mineral Disease",
                    "with genetic panel testing for FHH being more readily accessible, this approach can also be used to help distinguish the condition from primary hyperparathyroidism.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Bone biopsy",
                "Assertion: Bone biopsy should be performed in any patient with low BMD.",
                "Reason: Biopsy can clarify unexplained osteomalacia in expert centers.",
                2,
                "A is false—biopsy is not routine; R correctly states a valid indication.",
                ref(
                    "Bone Disease",
                    "Bone biopsy is not a routine test, but it can be helpful in patients with complex metabolic bone diseases",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Denosumab",
                "Assertion: Stopping denosumab without transition therapy can cause rebound vertebral fractures.",
                "Reason: Denosumab suppresses bone resorption while it remains on board.",
                0,
                "Both true—rapid offset after antibody clearance drives rebound bone loss and vertebral fracture risk.",
                ref(
                    "Main Conclusions",
                    "rebound vertebral fractures with denosumab.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "BTMs",
                "Assertion: Bone turnover markers have established routine clinical utility in every osteoporosis patient.",
                "Reason: BTMs may reflect treatment response and adherence.",
                2,
                "A overstates evidence—routine utility is not established; R is true but does not make A universally correct.",
                ref(
                    "Bone Disease",
                    "However, the clinical utility of routine measurements of bone turnover markers is yet to be established.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "CKD-MBD",
                "Assertion: Bisphosphonates are always appropriate in patients with CKD and low bone density.",
                "Reason: Bisphosphonates reduce fracture risk in postmenopausal osteoporosis.",
                2,
                "A is false in low-turnover CKD-MBD; R is true in primary osteoporosis but does not justify A in CKD-MBD.",
                ref(
                    "Main Conclusions",
                    "inappropriate use of bisphosphonates in the setting of chronic kidney disease-mineral and bone disorder due to low bone turnover.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "9",
        "title": "Bone and Mineral Metabolism",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Neil J. L. Gittoes, BSc, PhD, FRCP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_09_BONE_AND_MINERAL_METABOLISM.md",
        "items": items,
    }


def build_chapter_10() -> dict:
    p = "e21-10"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Screening",
                "Why serum phosphate is often overlooked in musculoskeletal complaints",
                "Chronic hypophosphatemia causes rickets or osteomalacia; serum phosphorus is frequently omitted from the evaluation of musculoskeletal symptoms, delaying diagnosis for years.",
                ref(
                    "Significance of the Clinical Problem",
                    "Serum phosphorus is an important mineral that is frequently overlooked in the evaluation of patients with musculoskeletal complaints, which can lead to significant delays in diagnosis and treatment.",
                ),
            ),
            note(
                f"{p}-n2",
                "Pediatric ranges",
                "How age-appropriate phosphate reference ranges prevent missed diagnosis",
                "Infants and children have significantly higher serum phosphate than adults; applying adult reference intervals to children can mask hypophosphatemia.",
                ref(
                    "Barriers to Optimal Practice",
                    "Serum phosphate concentrations are significantly higher in infants and younger children than in adults. As a result, hypophosphatemia may be overlooked if the adult reference range is applied to the pediatric population.",
                ),
            ),
            note(
                f"{p}-n3",
                "Classification",
                "How to categorize hypophosphatemia for evaluation",
                "Three categories guide workup: decreased intake/malabsorption, redistribution, and renal phosphate wasting (FGF-23-mediated vs non-FGF-23-mediated).",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Hypophosphatemia can be divided into 3 main categories (Table): 1. Decreased intake and/or malabsorption 2. Redistribution within the body 3. Renal phosphate wasting",
                ),
            ),
            note(
                f"{p}-n4",
                "Malabsorption labs",
                "How low fractional excretion of phosphate identifies intake/malabsorption",
                "Low urine phosphate with fractional excretion of phosphate <5% is characteristic of inadequate intake or malabsorption; elevated 1,25-dihydroxyvitamin D is also expected.",
                ref(
                    "Laboratory Assessment",
                    "Low urine phosphate with a low fractional excretion of phosphate (less than 5%) is a hallmark of hypophosphatemia caused by inadequate intake or malabsorption.",
                ),
            ),
            note(
                f"{p}-n5",
                "Redistribution",
                "Why acute respiratory alkalosis causes transient hypophosphatemia",
                "Acute alkalosis shifts phosphate intracellularly; it is self-limited and does not require phosphate replacement once the underlying cause resolves.",
                ref(
                    "Redistribution",
                    "Acute respiratory alkalosis can cause transient hypophosphatemia due to transcellular shifts, is self-limited, and does not require phosphate replacement therapy.",
                ),
            ),
            note(
                f"{p}-n6",
                "FGF-23 pattern",
                "How FGF-23-mediated renal wasting differs biochemically",
                "FGF-23-mediated disease shows normal calcium, normal or low urinary calcium, and low or inappropriately normal 1,25-dihydroxyvitamin D.",
                ref(
                    "Laboratory Assessment",
                    "FGF-23 mediated: Normal serum calcium Normal or low urinary calcium Low or inappropriately normal 1α,25(OH)2D3",
                ),
            ),
            note(
                f"{p}-n7",
                "XLH therapy",
                "How burosumab changes XLH management",
                "Anti-FGF-23 antibody (burosumab) reduces renal phosphate wasting, raises 1,25-dihydroxyvitamin D, and is given every 2 weeks in children and every 4 weeks in adults.",
                ref(
                    "FGF-23-Mediated Disease",
                    "Burosumab treatment results in reduced renal phosphate wasting and increased 1α,25(OH)2D3 concentrations.",
                ),
            ),
            note(
                f"{p}-n8",
                "Conventional XLH",
                "Why calcitriol plus phosphate requires vigilant monitoring",
                "Conventional XLH therapy risks secondary/tertiary hyperparathyroidism, hypercalciuria, nephrocalcinosis, and nephrolithiasis—tertiary hyperparathyroidism may require parathyroid surgery.",
                ref(
                    "FGF-23-Mediated Disease",
                    "Treatment with calcitriol and phosphate supplementation requires vigilant monitoring to avoid complications such as secondary/tertiary hyperparathyroidism, hypercalciuria, nephrocalcinosis, and nephrolithiasis.",
                ),
            ),
            note(
                f"{p}-n9",
                "TIO management",
                "How to manage tumor-induced osteomalacia",
                "Optimal treatment is tumor localization and surgical removal; when elusive or unresectable, calcitriol and phosphate are required—burosumab is not approved for TIO.",
                ref(
                    "FGF-23-Mediated Disease",
                    "Optimal treatment for patients with tumor-induced osteomalacia includes identification of the offending tumor and surgical removal.",
                ),
            ),
            note(
                f"{p}-n10",
                "TIO follow-up",
                "Why periodic phosphate monitoring is mandatory after TIO surgery",
                "Recurrent hypophosphatemia can occur years after apparent cure; phosphate often falls before symptoms or osteomalacia recur.",
                ref(
                    "Case 2 (Continued)",
                    "Patients with tumor-induced osteomalacia should be monitored proactively after apparent surgical cure. The best recommendation is periodic serum phosphate measurement (Answer B).",
                ),
            ),
            note(
                f"{p}-n11",
                "Hungry bone",
                "How hungry bone syndrome differs from TIO postoperative course",
                "Hungry bone follows parathyroidectomy; serum phosphate typically normalizes within days after TIO tumor resection, though pain and fractures may take months to heal.",
                ref(
                    "Case 4 (Continued)",
                    "Hungry bone syndrome may occur after parathyroidectomy for hyperparathyroidism; however, serum phosphate typically returns to normal within days after surgical cure of tumor-induced osteomalacia",
                ),
            ),
            note(
                f"{p}-n12",
                "DKA phosphate",
                "Why phosphate replacement does not improve outcomes in DKA",
                "Despite sometimes severe hypophosphatemia during DKA treatment, phosphate replacement has not been shown to improve outcomes.",
                ref(
                    "Treatment",
                    "Although hypophosphatemia occurring treatment of DKA can be severe, it is not replacement improves outcomes.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — XLH tertiary HPT",
                "A 21-year-old woman with XLH on calcitriol and phosphorus presents with calcium 13.2 mg/dL and PTH 244 pg/mL one month after stopping supplements. Best initial management?",
                [
                    "Restart phosphorus to lower calcium",
                    "Continue furosemide long-term",
                    "Order MEN1 genetic testing",
                    "Consult a parathyroid surgeon",
                ],
                3,
                "Tertiary hyperparathyroidism from overzealous phosphate therapy requires parathyroid surgery before resuming XLH treatment.",
                ref("Case 1", "Answer: D) Consult a parathyroid surgeon"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — burosumab expectations",
                "The same XLH patient restarts burosumab after pseudofractures and dental abscesses. What is a reasonable treatment expectation?",
                [
                    "Healing of pseudofractures and reduced osteomalacia-related bone pain",
                    "Improvement in osteoarthritis pain",
                    "Improvement in enthesopathy pain",
                    "Reduced frequency of dental abscess",
                ],
                0,
                "Burosumab heals pseudofractures and reduces osteomalacia bone pain; it does not treat osteoarthritis, enthesopathy, or dental abscess frequency.",
                ref("Case 1 (Continued)", "Answer: A) Reduced bone pain and healing of her pseudofractures"),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — TIO workup",
                "A 40-year-old man has fractures, low phosphate (1.8 mg/dL), elevated ALP, and a firm neck lesion. Best next step?",
                [
                    "Start alendronate for low BMD",
                    "Refer to medical genetics for heritable hypophosphatemia",
                    "Obtain urine studies to assess tubular reabsorption of phosphorus",
                    "Schedule tetracycline-labeled bone biopsy",
                ],
                2,
                "Osteomalacia with hypophosphatemia requires urinary phosphate assessment to identify renal wasting etiology.",
                ref("Case 2", "Answer: C) Obtain urine studies to assess tubular reabsorption of phosphorus"),
            ),
            mcq(
                f"{p}-q4",
                "Case 2 — FGF-23 biochemistry",
                "Fractional excretion of phosphorus is elevated. Which lab pattern is most consistent with elevated FGF-23?",
                [
                    "Elevated 1,25-dihydroxyvitamin D",
                    "High urinary calcium",
                    "Low 1,25-dihydroxyvitamin D",
                    "Elevated serum creatinine with hyperphosphatemia",
                ],
                2,
                "FGF-23 inhibits 1α-hydroxylase, producing low or inappropriately normal 1,25-dihydroxyvitamin D.",
                ref("Case 2 (Continued)", "Answer: C) Low 1,25-dihydroxyvitamin D"),
            ),
            mcq(
                f"{p}-q5",
                "Case 2 — TIO localization",
                "TIO is suspected and a 2.5×3-cm firm lesion is at the neck base. Best next step?",
                [
                    "Start calcitriol and phosphorus only",
                    "Start burosumab",
                    "Whole-body FDG-PET or 68Ga DOTATATE PET",
                    "Biopsy the neck skin lesion",
                ],
                3,
                "Cutaneous phosphaturic mesenchymal tumors occur; biopsy of the accessible neck lesion is diagnostic and therapeutic.",
                ref("Case 2 (Continued)", "Answer: D) Perform biopsy of skin lesion at the base of his neck"),
            ),
            mcq(
                f"{p}-q6",
                "Case 2 — TIO surveillance",
                "After curative TIO resection, best long-term follow-up?",
                [
                    "Return only if symptoms recur",
                    "Periodic serum phosphate measurement",
                    "Annual whole-body PET regardless of symptoms",
                    "No follow-up needed after surgical cure",
                ],
                1,
                "Proactive phosphate monitoring detects recurrence before symptomatic osteomalacia returns.",
                ref("Case 2 (Continued)", "Answer: B) Periodic serum phosphate measurement"),
            ),
            mcq(
                f"{p}-q7",
                "Case 3 — acute hypophosphatemia",
                "A 27-year-old woman has acute dyspnea, tachypnea, phosphate 1.4 mg/dL, and anxiety. Best next evaluation step?",
                [
                    "68Ga DOTATATE PET scan",
                    "Measure 1,25-dihydroxyvitamin D",
                    "Obtain arterial or venous blood gas",
                    "Urine fractional excretion of phosphate",
                ],
                2,
                "Acute anxiety with tachypnea suggests respiratory alkalosis causing transcellular hypophosphatemia—confirm with blood gas.",
                ref("Case 3", "Answer: C) Obtain arterial or venous gas"),
            ),
            mcq(
                f"{p}-q8",
                "Case 3 — management",
                "Venous blood gas confirms respiratory alkalosis from acute anxiety. Best management?",
                [
                    "Administer a benzodiazepine",
                    "Vitamin D 50,000 IU weekly for 6 weeks",
                    "Switch fluoxetine to another SSRI",
                    "Intravenous phosphate",
                ],
                0,
                "Treating anxiety reverses alkalosis and restores phosphate rapidly; IV phosphate is unnecessary for transcellular shift.",
                ref("Case 3 (Continued)", "Answer: A) Administer a benzodiazepine"),
            ),
            mcq(
                f"{p}-q9",
                "Case 3 — chronicity clues",
                "After treatment, phosphate normalizes. Which features were inconsistent with chronic hypophosphatemia?",
                [
                    "Acute-onset symptoms only",
                    "Normal childhood growth only",
                    "Normal alkaline phosphatase only",
                    "All of the above",
                ],
                3,
                "Acute onset, normal ALP, lack of bone pain/fractures, and normal childhood growth all favor acute rather than chronic hypophosphatemia.",
                ref("Case 3 (Continued)", "Answer: E) All of the above"),
            ),
            mcq(
                f"{p}-q10",
                "Case 4 — unresectable TIO",
                "A 70-year-old man has 7 years of TIO symptoms, elevated FGF-23, FEPhos 38%, and unresectable tumor. Best treatment?",
                [
                    "Physical therapy and pain clinic only",
                    "Calcitriol and phosphate or anti-FGF-23 antibody therapy",
                    "Bisphosphonate",
                    "Teriparatide",
                ],
                1,
                "Unresectable TIO requires medical therapy with calcitriol/phosphate; osteomalacia is not osteoporosis and antiresorptives/anabolics are inappropriate.",
                ref("Case 4", "Answer: B) Initiate medical therapy with calcitriol and phosphate or anti-FGF-23 antibody therapy"),
            ),
            mcq(
                f"{p}-q11",
                "Case 4 — tumor localization",
                "Six months of medical therapy leaves unhealed fractures. Best next step?",
                [
                    "Genetic testing for inherited hypophosphatemia",
                    "Additional functional whole-body imaging (e.g., 68Ga DOTATATE PET)",
                    "Arterial blood gas for respiratory alkalosis",
                    "Bone-specific alkaline phosphatase only",
                ],
                1,
                "After TIO diagnosis, whole-body functional imaging should be pursued even if prior scans were negative.",
                ref("Case 4 (Continued)", "Answer: B) Obtain functional whole-body imaging (eg, 68Ga DOTATATE PET)"),
            ),
            mcq(
                f"{p}-q12",
                "Case 4 — postoperative expectations",
                "After complete TIO tumor resection, which outcome is expected?",
                [
                    "Fractures and bone pain may take several months to resolve",
                    "Serum phosphate stays low for weeks due to hungry bone syndrome",
                    "Medical therapy required for weeks because of long FGF-23 half-life",
                    "Muscle weakness is irreversible",
                ],
                0,
                "Surgical cure is achieved but prolonged osteomalacia means pain and fractures may resolve over weeks to months.",
                ref("Case 4 (Continued)", "Answer: A) Fractures and bone pain may take several months to resolve after surgical cure"),
            ),
            mcq(
                f"{p}-q13",
                "Fanconi syndrome",
                "A patient with renal Fanconi syndrome and hypophosphatemia requires phosphate supplementation. Is calcitriol indicated?",
                [
                    "Yes — always combine calcitriol with phosphate",
                    "No — calcitriol would worsen hypercalciuria",
                    "Only if FGF-23 is elevated",
                    "Only in children under age 10",
                ],
                1,
                "Non-FGF-23 renal wasting without calcitriol deficiency should not receive calcitriol—it worsens hypercalciuria and stone risk.",
                ref(
                    "Other",
                    "Because these are not FGF-23-mediated conditions, calcitriol is not indicated as it would worsen the hypercalciuria and lead to nephrocalcinosis and nephrolithiasis.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Acute hypophosphatemia",
                "Severe acute hypophosphatemia can cause rhabdomyolysis and hemolysis.",
                True,
                "Cardiac, respiratory, rhabdomyolysis, and hemolysis may occur with severe acute hypophosphatemia.",
                ref(
                    "Significance of the Clinical Problem",
                    "Cardiac and respiratory dysfunction, as well as rhabdomyolysis and hemolysis, may occur with severe, acute hypophosphatemia.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "XLH adults",
                "All adults with XLH require ongoing pharmacologic therapy after linear growth is complete.",
                False,
                "Not all adults with XLH are symptomatic; therapy is individualized after growth completion.",
                ref("Case 1 (Continued)", "Not all adults with XLH are symptomatic and therefore not all require pharmacologic intervention."),
            ),
            tf(
                f"{p}-tf3",
                "Respiratory alkalosis",
                "Acute respiratory alkalosis requires phosphate replacement to prevent complications.",
                False,
                "Transcellular hypophosphatemia from acute alkalosis is self-limited and does not require replacement.",
                ref(
                    "Redistribution",
                    "Acute respiratory alkalosis can cause transient hypophosphatemia due to transcellular shifts, is self-limited, and does not require phosphate replacement therapy.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Burosumab TIO",
                "Burosumab is approved for treatment of tumor-induced osteomalacia.",
                False,
                "Anti-FGF-23 antibody is approved for XLH but not other FGF-23-mediated conditions such as TIO.",
                ref(
                    "FGF-23-Mediated Disease",
                    "Burosumab has not been approved for treatment of other FGF-23-mediated conditions.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Phosphate binders",
                "Calcium-based phosphate binders can cause hypophosphatemia.",
                True,
                "Phosphate binders reduce intestinal phosphate availability and can cause hypophosphatemia.",
                ref(
                    "Decreased Intake and/or Malabsorption",
                    "patients receiving phosphate binders such as calcium, sevelamer, or lanthanum carbonate can develop hypophosphatemia due to reduced intestinal phosphate availability.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "TIO recurrence",
                "After surgical cure of TIO, no further monitoring is needed.",
                False,
                "Recurrent hypophosphatemia can occur years later, including with malignant transformation.",
                ref(
                    "Case 2 (Continued)",
                    "Several years after his initial surgery, this patient developed recurrence of hypophosphatemia with sarcomatous transformation and metastases.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Hungry bone",
                "Larger parathyroid adenoma volume and higher alkaline phosphatase increase hungry bone risk after parathyroidectomy.",
                True,
                "Adenoma volume, elevated ALP, and older age are risk factors for hungry bone syndrome.",
                ref(
                    "Redistribution",
                    "larger parathyroid adenoma volume, higher alkaline phosphatase, and older age are risk factors for this condition.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Osteomalacia vs osteoporosis",
                "Low BMD in osteomalacia should be treated with bisphosphonates like osteoporosis.",
                False,
                "Osteomalacia requires correcting phosphate/vitamin D deficiency; bisphosphonates may worsen disease.",
                ref(
                    "Case 4",
                    "He has osteomalacia and therefore a bisphosphonate (Answer C) is not appropriate and may worsen his disease.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "XLH hyperparathyroidism",
                "Assertion: Restarting phosphorus before treating hyperparathyroidism in XLH will lower serum calcium.",
                "Reason: Hyperparathyroidism worsens renal phosphate wasting.",
                4,
                "Both false—phosphorus restarts worsen hyperparathyroidism; hyperparathyroidism does worsen phosphaturia but does not make A true.",
                ref(
                    "Case 1",
                    "Restarting phosphorus supplementation before addressing her hyperparathyroidism (Answer A) would only exacerbate the hyperparathyroidism.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "TIO biochemistry",
                "Assertion: FGF-23-mediated hypophosphatemia is associated with low 1,25-dihydroxyvitamin D.",
                "Reason: FGF-23 inhibits 1α-hydroxylase activity.",
                0,
                "Both true and causally linked—FGF-23 suppresses active vitamin D synthesis.",
                ref(
                    "Case 2 (Continued)",
                    "FGF-23 not only reduces renal phosphate reabsorption but also inhibits 1α-hydroxylase activity.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Acute alkalosis",
                "Assertion: A benzodiazepine can correct hypophosphatemia in acute respiratory alkalosis.",
                "Reason: Treating anxiety reverses alkalosis and transcellular phosphate shift.",
                0,
                "Both true—resolving alkalosis restores serum phosphate without phosphate supplementation.",
                ref(
                    "Case 3 (Continued)",
                    "Treatment of this patient's anxiety (Answer A) will reverse her acute respiratory alkalosis and quickly restore serum phosphate to a normal range.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "TIO surgery",
                "Assertion: Serum phosphate normalizes within days after complete TIO tumor resection.",
                "Reason: FGF-23 has a short half-life.",
                0,
                "Both true—rapid FGF-23 clearance restores phosphate quickly, unlike hungry bone after parathyroidectomy.",
                ref(
                    "Case 4 (Continued)",
                    "FGF-23 has a short, not long, half-life, and medical therapy after complete resection is not required",
                ),
            ),
            ar(
                f"{p}-ar5",
                "DKA",
                "Assertion: Phosphate should be routinely replaced during DKA treatment to improve outcomes.",
                "Reason: DKA treatment commonly causes severe hypophosphatemia.",
                2,
                "R is true but A is false—severe hypophosphatemia occurs yet replacement does not improve outcomes.",
                ref(
                    "Treatment",
                    "Although hypophosphatemia occurring treatment of DKA can be severe, it is not replacement improves outcomes.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Burosumab dental",
                "Assertion: Burosumab reduces the frequency of dental abscess in XLH.",
                "Reason: Burosumab improves healing of pseudofractures.",
                4,
                "Both false—burosumab may increase dental abscess vs conventional therapy; pseudofracture healing is a separate outcome.",
                ref(
                    "Case 1 (Continued)",
                    "there is no evidence that anti-FGF-23 antibody therapy improves pain associated with osteoarthritis (Answer B) or enthesopathy (Answer C) or reduces the frequency of dental abscess (Answer D).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Malabsorption FEPhos",
                "Assertion: Fractional excretion of phosphate <5% suggests inadequate intake or malabsorption.",
                "Reason: Renal phosphate wasting elevates fractional excretion.",
                0,
                "Both true—low FEPhos indicates non-renal cause; the reason correctly contrasts with renal wasting.",
                ref(
                    "Laboratory Assessment",
                    "Low urine phosphate with a low fractional excretion of phosphate (less than 5%) is a hallmark of hypophosphatemia caused by inadequate intake or malabsorption.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "TIO bisphosphonate",
                "Assertion: Alendronate is appropriate first-line therapy for TIO with fractures.",
                "Reason: The patient has low bone density on DXA.",
                4,
                "Both false—osteomalacia not osteoporosis; low BMD reflects defective mineralization, not an indication for bisphosphonates.",
                ref(
                    "Case 2",
                    "His low bone density is related to osteomalacia and not osteoporosis.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "10",
        "title": "Evaluation of the Patient With Hypophosphatemia",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Peter J. Tebben, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_10_Evaluation_of_the_Patient_With_Hypophosphatemia.md",
        "items": items,
    }


def build_chapter_11() -> dict:
    p = "e21-11"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Challenging cases",
                "Why challenging bone and mineral cases need individualized attention",
                "Rarer diseases and rare events in common conditions require considered individualized approaches beyond formulaic fracture-risk protocols.",
                ref(
                    "Main Conclusions",
                    "Assessment and management of rarer bone and mineral diseases, or rare events in common conditions, require a considered and individualized approach.",
                ),
            ),
            note(
                f"{p}-n2",
                "Hypocalcemia neuropsychiatric",
                "How hypocalcemia can mimic primary psychiatric disease",
                "Neuropsychiatric features including mood disturbance are recognized in hypocalcemia; papilledema is a rare association—classic Chvostek/Trousseau signs may be absent despite profound hypocalcemia.",
                ref(
                    "Case 1",
                    "Neuropsychiatric presentations, including mood disturbance, are recognized features of hypocalcemia. There is also a rare but recognized association between hypocalcemia and papilledema.",
                ),
            ),
            note(
                f"{p}-n3",
                "Atypical femur fracture",
                "Why bisphosphonates can cause subtrochanteric fractures in osteogenesis imperfecta",
                "Even in high fracture-risk OI, bisphosphonate suppression of turnover is linked to bilateral incomplete subtrochanteric fractures—requiring close sequential risk/benefit reassessment.",
                ref(
                    "Case 2",
                    "Paradoxically, in this case, such treatment is linked to the evolution of bilateral incomplete subtrochanteric fractures.",
                ),
            ),
            note(
                f"{p}-n4",
                "AFF management",
                "How to manage impending atypical femoral fracture on bisphosphonate",
                "Withhold further antiresorptives; teriparatide is the most appropriate listed option to promote healing despite unlicensed indication—romosozumab lacks data here.",
                ref(
                    "Case 2",
                    "Teriparatide (Answer E), a bone anabolic agent, was commenced to promote fracture healing (no licensed indication).",
                ),
            ),
            note(
                f"{p}-n5",
                "TIO presentation",
                "Why TIO can masquerade as neuromuscular disease",
                "Progressive pain, myopathy, and weakness with elevated ALP and hypophosphatemia may evade diagnosis for years until phosphate is measured and an ethmoid sinus mass is found.",
                ref(
                    "Case 3",
                    "This patient had little symptomatic benefit from treatment with phosphate and activated vitamin D. MRI showed a right ethmoid sinus mass",
                ),
            ),
            note(
                f"{p}-n6",
                "Brown tumor",
                "How brown tumors differ from primary bone neoplasms",
                "Brown tumors are rare pseudotumoral hyperparathyroidism manifestations—microscopically similar to giant-cell tumors but diagnosed by biochemical context of severe secondary hyperparathyroidism.",
                ref(
                    "Case 4",
                    "Brown tumors are very rare pseudotumoral manifestations of hyperparathyroidism.",
                ),
            ),
            note(
                f"{p}-n7",
                "Celiac osteomalacia",
                "Why celiac disease and pregnancy can unmask severe osteomalacia",
                "Celiac malabsorption with pregnancy increased demands can produce osteomalacia, secondary hyperparathyroidism, and brown tumors despite prior partial treatment.",
                ref(
                    "Case 4",
                    "Celiac disease and pregnancy had contributed to the severe expression of osteomalacia.",
                ),
            ),
            note(
                f"{p}-n8",
                "Hungry bone risk",
                "Which factors predict hungry bone syndrome after parathyroidectomy",
                "Elevated ALP, radiographic parathyroid bone disease, large adenoma, and untreated vitamin D deficiency increase risk—older, not younger, age is associated.",
                ref(
                    "Case 5",
                    "Older, rather than younger age, is more often associated with hungry bone syndrome (thus, Answer B is correct).",
                ),
            ),
            note(
                f"{p}-n9",
                "Pregnancy osteoporosis",
                "How pregnancy and lactation-associated osteoporosis presents",
                "Very rare condition with symptomatic postpartum vertebral fractures, no identified cause, and ~20–30% fracture risk in subsequent pregnancies.",
                ref(
                    "Case 6",
                    "Fractures in subsequent pregnancies occur in approximately 20% to 30% of cases, and it is prudent to warn patients about this risk",
                ),
            ),
            note(
                f"{p}-n10",
                "PLAO treatment",
                "Why bisphosphonates are avoided in childbearing years with PLAO",
                "Teriparatide may be used for severe progressive vertebral fractures; bisphosphonates are not ideal in women of childbearing age due to potential teratogenicity.",
                ref(
                    "Case 6",
                    "Bisphosphonates are not ideal in women during their childbearing years due to potential teratogenicity (thus, Answer C is correct)",
                ),
            ),
            note(
                f"{p}-n11",
                "Investigation set",
                "How a limited investigation panel diagnoses most mineral disorders",
                "With clear understanding of calcium, phosphate, ALP, PTH, 25-OHD, magnesium, and urinary calcium, most conditions can be reliably diagnosed.",
                ref(
                    "Main Conclusions",
                    "Evaluation of bone and mineral metabolism disorders relies on a limited set of investigations; with clear understanding and appropriate interpretation of these, most conditions can be reliably diagnosed and managed.",
                ),
            ),
            note(
                f"{p}-n12",
                "Drug harms",
                "Why awareness of rare drug effects prevents harm",
                "Overlooking bisphosphonate atypical femoral fractures and denosumab rebound vertebral fractures can cause preventable patient harm.",
                ref(
                    "Main Conclusions",
                    "Awareness of thresholds of intervention for treatment and rare adverse effects of commonly used drugs may be overlooked, potentially causing patient harm",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — hypocalcemia",
                "A 42-year-old man has panic attacks, bilateral visual field constriction, papilledema, and personality change. MRI and LP are normal. Most likely unifying diagnosis?",
                [
                    "Anterior ischemic optic neuropathy",
                    "Hypocalcemia",
                    "Primary affective disorder",
                    "Pheochromocytoma",
                ],
                1,
                "Labs showed calcium 5.3 mg/dL and PTH 2.0 pg/mL (idiopathic hypoparathyroidism); vision and personality improved with calcium and alfacalcidol.",
                ref("Case 1", "Answer: B) Hypocalcemia"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — signs",
                "In Case 1, Chvostek and Trousseau signs were absent despite calcium 5.3 mg/dL. Best interpretation?",
                [
                    "Rules out hypocalcemia",
                    "Classic signs may be absent despite significant hypocalcemia",
                    "Indicates pseudohypoparathyroidism only",
                    "Means vitamin D deficiency is the cause",
                ],
                1,
                "Classic eponymous signs are insensitive—profound hypocalcemia can exist without them.",
                ref("Case 1", "Classic signs of hypocalcemia (eg, Chvostek sign) may be absent despite significant hypocalcemia."),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — OI AFF",
                "A 64-year-old woman with OI type 4 on pamidronate then zoledronic acid has bilateral incomplete subtrochanteric femur fractures. Best pharmacologic step?",
                [
                    "Continue zoledronic acid",
                    "Calcium and vitamin D only",
                    "Switch to denosumab",
                    "Switch to teriparatide",
                ],
                3,
                "Further antiresorptives worsen suppressed turnover; teriparatide promotes healing in this setting.",
                ref("Case 2", "Answer: E) Switch to teriparatide"),
            ),
            mcq(
                f"{p}-q4",
                "Case 2 — antiresorptive trap",
                "Why is continuing zoledronic acid incorrect in Case 2?",
                [
                    "It has no effect on BMD in OI",
                    "Antiresorptives exacerbate suppressed turnover linked to atypical femoral fractures",
                    "Teriparatide is contraindicated in OI",
                    "OI never requires pharmacotherapy",
                ],
                1,
                "Persisting with antiresorptives exacerbates turnover suppression causally linked to AFF.",
                ref(
                    "Case 2",
                    "Persisting with an antiresorptive agent such as zoledronic acid (Answer A) or denosumab (Answer C) is incorrect, as such treatments exacerbate suppression of bone turnover",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 3 — TIO",
                "A 42-year-old man has 3 years of foot/ankle pain, severe myopathy, phosphate 1.6 mg/dL, low 1,25-D, and FGF-23 251 U/L. Most likely diagnosis?",
                [
                    "Secondary hyperparathyroidism",
                    "Tumor-induced osteomalacia",
                    "Vitamin D deficiency alone",
                    "X-linked hypophosphatemic rickets",
                ],
                1,
                "FGF-23 elevation with hypophosphatemia and adult onset point to TIO; ethmoid sinus mass was ultimately identified.",
                ref("Case 3", "Answer: B) Tumor-induced osteomalacia"),
            ),
            mcq(
                f"{p}-q6",
                "Case 4 — brown tumor",
                "A 21-week pregnant woman with celiac disease has a destructive tibial lesion with giant cells on biopsy. Calcium 7.8 mg/dL, PTH 482 pg/mL, 25-OHD <6 ng/mL. Most likely cause?",
                [
                    "Brown tumor",
                    "Aneurysmal bone cyst",
                    "Fibrous dysplasia",
                    "Simple bone cyst",
                ],
                0,
                "Severe osteomalacia with secondary hyperparathyroidism produced brown tumors; biochemistry distinguishes metabolic from primary bone neoplasms.",
                ref("Case 4", "Answer: A) Brown tumor"),
            ),
            mcq(
                f"{p}-q7",
                "Case 4 — differential",
                "Why is giant-cell tumor less likely than brown tumor in Case 4?",
                [
                    "Giant-cell tumors never occur in pregnancy",
                    "The degree of biochemical abnormality points to metabolic hyperparathyroidism",
                    "Brown tumors never occur in celiac disease",
                    "PTH is always normal in brown tumors",
                ],
                1,
                "Marked hypocalcemia, extreme ALP, and very high PTH provide metabolic context favoring brown tumor.",
                ref(
                    "Case 4",
                    "a diagnosis of brown tumor of hyperparathyroidism is based on abnormal biochemistry.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Case 5 — hungry bone",
                "A 25-year-old woman with large parathyroid adenoma, ALP >900 U/L, and orbital brown tumor undergoes parathyroidectomy. Which is NOT a hungry bone risk factor?",
                [
                    "Elevated alkaline phosphatase",
                    "Younger age",
                    "Radiographic parathyroid bone disease",
                    "Large parathyroid adenoma",
                ],
                1,
                "Older age—not younger—increases hungry bone risk after parathyroidectomy.",
                ref("Case 5", "Answer: B) Younger age"),
            ),
            mcq(
                f"{p}-q9",
                "Case 6 — PLAO",
                "A 28-year-old woman has multiple postpartum vertebral fractures, Z-score -4.3 at spine, and active edema on MRI. Best true statement?",
                [
                    "Subsequent pregnancy fracture risk is not increased",
                    "Bone-active drugs must be continued lifelong",
                    "Bisphosphonates should be avoided if possible due to teratogenicity concerns",
                    "Fractures typically appear in the second trimester",
                ],
                2,
                "PLAO fractures occur postpartum; bisphosphonates are avoided in childbearing years when possible; subsequent pregnancy carries 20–30% recurrence risk.",
                ref("Case 6", "Answer: C) Bisphosphonates should be avoided if possible to avoid later potential teratogenicity"),
            ),
            mcq(
                f"{p}-q10",
                "Case 6 — management",
                "For severe progressive PLAO vertebral fractures, which therapy was used successfully?",
                [
                    "Observation only",
                    "Teriparatide",
                    "High-dose oral bisphosphonate",
                    "Denosumab without follow-on therapy",
                ],
                1,
                "Due to severity and active progression, teriparatide was used with improved Z-score and pain resolution over 2 years.",
                ref(
                    "Case 6",
                    "due to the severity and active progression of the vertebral fractures, she is treated with teriparatide.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "FHH workup",
                "A patient has mild hypercalcemia and low urinary calcium. Besides clearance ratio, what now aids FHH vs PHPT distinction?",
                [
                    "Serum calcitonin",
                    "Genetic panel testing for FHH",
                    "Bone biopsy",
                    "Urinary NTX alone",
                ],
                1,
                "Genetic panel testing for FHH is increasingly accessible to distinguish from PHPT.",
                ref(
                    "Mineral Disease",
                    "with genetic panel testing for FHH being more readily accessible, this approach can also be used to help distinguish the condition from primary hyperparathyroidism.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "DXA context",
                "A patient's hip T-score is -2.4 but FRAX is low with no prior fracture. Best principle?",
                [
                    "Treat based on T-score alone",
                    "Contextualize DXA within full fracture-risk profile",
                    "Bone biopsy before any decision",
                    "Start denosumab indefinitely",
                ],
                1,
                "T-scores must not be isolated treatment thresholds.",
                ref(
                    "Bone Disease",
                    "DXA-determined data should always be contextualized to the full fracture risk profile of the patient.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Denosumab harm",
                "A patient stops denosumab without bridging therapy and develops multiple vertebral fractures. What was overlooked?",
                [
                    "Need for weekly DXA",
                    "Awareness of denosumab rebound and need for transition therapy",
                    "Routine calcitonin monitoring",
                    "Mandatory bone biopsy at initiation",
                ],
                1,
                "Rebound vertebral fractures after denosumab cessation are a recognized rare adverse effect requiring anticipatory planning.",
                ref(
                    "Main Conclusions",
                    "rebound vertebral fractures with denosumab.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Hypocalcemia",
                "Papilledema can occur as a rare manifestation of hypocalcemia.",
                True,
                "A recognized though rare association exists between hypocalcemia and papilledema.",
                ref("Case 1", "There is also a rare but recognized association between hypocalcemia and papilledema."),
            ),
            tf(
                f"{p}-tf2",
                "AFF",
                "Continuing bisphosphonates is appropriate when incomplete atypical femoral fractures are present.",
                False,
                "Further antiresorptive therapy exacerbates turnover suppression linked to AFF.",
                ref(
                    "Case 2",
                    "Persisting with an antiresorptive agent such as zoledronic acid (Answer A) or denosumab (Answer C) is incorrect",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Brown tumor",
                "Brown tumors are histologically indistinguishable from giant-cell tumors.",
                True,
                "Microscopically brown tumors resemble giant-cell tumors; diagnosis relies on biochemistry.",
                ref(
                    "Case 4",
                    "Microscopically, these lesions are indistinguishable from giant-cell tumors or aneurysmal bone cysts",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Hungry bone",
                "Younger age is a recognized risk factor for hungry bone syndrome.",
                False,
                "Older rather than younger age is more often associated with hungry bone syndrome.",
                ref("Case 5", "Older, rather than younger age, is more often associated with hungry bone syndrome"),
            ),
            tf(
                f"{p}-tf5",
                "PLAO timing",
                "Pregnancy and lactation-associated osteoporosis fractures typically occur in the postpartum period.",
                True,
                "Fractures typically occur postpartum, not during the second trimester.",
                ref("Case 6", "Fractures typically occur in the postpartum period (thus, Answer E is incorrect)"),
            ),
            tf(
                f"{p}-tf6",
                "PLAO recurrence",
                "Patients with PLAO should be warned about fracture risk in subsequent pregnancies.",
                True,
                "Approximately 20–30% have fractures in subsequent pregnancies.",
                ref("Case 6", "Fractures in subsequent pregnancies occur in approximately 20% to 30% of cases"),
            ),
            tf(
                f"{p}-tf7",
                "TIO",
                "Tumor-induced osteomalacia may present with progressive weakness mimicking neuromuscular disease.",
                True,
                "Years of misdiagnosis occurred before phosphate measurement and tumor localization.",
                ref(
                    "Case 3",
                    "The progressive neurogenic or myogenic weakness has affected all 4 limbs to the extent that he stopped working.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Calcitonin",
                "Calcitonin measurement is routinely indicated in calcium metabolism disorders.",
                False,
                "Calcitonin is confined to medullary thyroid carcinoma monitoring.",
                ref(
                    "Mineral Disease",
                    "There is no role for calcitonin measurement in the routine investigation of calcium and bone metabolism.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Hypocalcemia mimic",
                "Assertion: Hypocalcemia can present with papilledema and personality change mimicking psychiatric disease.",
                "Reason: Neuropsychiatric features are recognized manifestations of hypocalcemia.",
                0,
                "Both true and causally linked—profound hypocalcemia explains the neuro-ophthalmic and behavioral presentation.",
                ref(
                    "Case 1",
                    "Neuropsychiatric presentations, including mood disturbance, are recognized features of hypocalcemia.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "AFF",
                "Assertion: Teriparatide is preferred over continuing zoledronic acid for incomplete AFF in OI.",
                "Reason: Antiresorptives suppress bone turnover linked to atypical femoral fractures.",
                0,
                "Both true—anabolic therapy promotes healing while further antiresorption worsens the causal pathway.",
                ref(
                    "Case 2",
                    "such treatments exacerbate suppression of bone turnover, thought to be causally linked to atypical femoral fractures.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Brown tumor",
                "Assertion: A destructive bone lesion with giant cells in severe secondary hyperparathyroidism is most likely a brown tumor.",
                "Reason: Brown tumors are diagnosed based on abnormal biochemistry rather than histology alone.",
                0,
                "Both true—biochemical hyperparathyroidism/osteomalacia context distinguishes brown tumor from primary neoplasm.",
                ref(
                    "Case 4",
                    "a diagnosis of brown tumor of hyperparathyroidism is based on abnormal biochemistry.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Hungry bone",
                "Assertion: Younger age protects against hungry bone syndrome after parathyroidectomy.",
                "Reason: Elevated alkaline phosphatase indicates increased bone remodeling.",
                4,
                "Both false—older age is associated with hungry bone; elevated ALP is a risk factor, not a reason younger age protects.",
                ref("Case 5", "Older, rather than younger age, is more often associated with hungry bone syndrome"),
            ),
            ar(
                f"{p}-ar5",
                "PLAO",
                "Assertion: Bisphosphonates are first-line therapy for PLAO in women of childbearing age.",
                "Reason: Bisphosphonates reduce vertebral fracture risk in postmenopausal osteoporosis.",
                2,
                "A is false due to teratogenicity concerns; R is true in postmenopausal osteoporosis but irrelevant to PLAO first-line use.",
                ref(
                    "Case 6",
                    "Bisphosphonates are not ideal in women during their childbearing years due to potential teratogenicity",
                ),
            ),
            ar(
                f"{p}-ar6",
                "TIO",
                "Assertion: Elevated FGF-23 with hypophosphatemia in an adult suggests tumor-induced osteomalacia until proven otherwise.",
                "Reason: FGF-23 mediates renal phosphate wasting in TIO.",
                0,
                "Both true—adult-onset FGF-23-mediated hypophosphatemia warrants tumor search.",
                ref("Case 3", "Answer: B) Tumor-induced osteomalacia"),
            ),
            ar(
                f"{p}-ar7",
                "Denosumab",
                "Assertion: Stopping denosumab without transition therapy can cause multiple vertebral fractures.",
                "Reason: Denosumab has a long skeletal half-life like bisphosphonates.",
                2,
                "A is true but R is false—denosumab offset is rapid with rebound, unlike long bisphosphonate binding.",
                ref(
                    "Main Conclusions",
                    "rebound vertebral fractures with denosumab.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Chvostek sign",
                "Assertion: Absent Chvostek sign excludes significant hypocalcemia.",
                "Reason: Chvostek sign is a classic manifestation of hypocalcemia.",
                4,
                "Both false—classic signs may be absent despite profound hypocalcemia.",
                ref("Case 1", "Classic signs of hypocalcemia (eg, Chvostek sign) may be absent despite significant hypocalcemia."),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "11",
        "title": "Challenging Case and Mineral Disease",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Neil J. L. Gittoes, BSc, PhD, FRCP",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_11_Challenging_Case_and_Mineral_Disease.md",
        "items": items,
    }


def build_chapter_12() -> dict:
    p = "e21-12"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "BTM adherence",
                "Why bone turnover markers help identify poor bisphosphonate adherence",
                "Up to half of patients stop oral bisphosphonates within a year; measuring BTMs at baseline and 3 months can identify poor response likely from nonadherence.",
                ref(
                    "Significance of the Clinical Problem",
                    "the measurement of BTMs before and then 3 months after starting treatment could be a successful strategy to identify poor drug response, most likely caused by poor adherence.",
                ),
            ),
            note(
                f"{p}-n2",
                "Reference markers",
                "How CTX and PINP became the reference bone turnover markers",
                "IOF and IFCC recommend serum CTX and PINP as reference markers for research and clinical practice; automated immunoassays are preferred worldwide.",
                ref(
                    "Bone Turnover Markers",
                    "The International Osteoporosis Foundation and the International Federation of Clinical Chemistry have proposed using CTX and PINP as the reference markers.",
                ),
            ),
            note(
                f"{p}-n3",
                "Pre-analytical variability",
                "Why fasting morning samples are required for CTX",
                "CTX is twice as high in the morning as afternoon; draw fasting blood first thing in the morning to minimize diurnal variability.",
                ref(
                    "Sources of Variability in BTMs",
                    "CTX is twice as high in the morning as in the afternoon, so it is recommended to draw the patient's blood in the fasting state, first thing in the morning.",
                ),
            ),
            note(
                f"{p}-n4",
                "TRIO targets",
                "How TRIO defined treatment response targets for BTMs",
                "Two targets: least significant change (~10 μg/L PINP, 120 ng/L CTX) and premenopausal median (35 μg/L PINP, 280 ng/L CTX); ~90% respond at 12 weeks in research settings.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Response",
                    "The least significant change. This is the least change that can be considered to be significant (at P<.05) based on 2 measurements in an individual patient. This was estimated to be around 10 μg/L for PINP and 120 ng/L for CTX.",
                ),
            ),
            note(
                f"{p}-n5",
                "Drug holiday",
                "When to consider a bisphosphonate drug holiday using BTMs",
                "After 5 years of oral bisphosphonate, consider stopping if hip T-score > -2.5 and no spine fracture; BTMs rising above LSC or premenopausal median signal offset and need to restart.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Offset of Effect",
                    "Patients taking oral bisphosphonates are recommended to stop treatment after 5 years if they are at relatively low fracture risk (BMD T-score above -2.5 at the hip and no recent fracture) to reduce the risk of atypical femur fractures.",
                ),
            ),
            note(
                f"{p}-n6",
                "Denosumab BTMs",
                "How BTMs behave with denosumab start and stop",
                "Denosumab produces very high response rates—monitoring efficacy may be unnecessary—but rebound BTM increases after stopping may guide bisphosphonate bridging timing.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "after stopping denosumab, there is a rebound increase in BTMs and the timing of the rebound might help dictate the optimal time to give a bisphosphonate to prevent accelerated bone loss.",
                ),
            ),
            note(
                f"{p}-n7",
                "Anabolic BTMs",
                "How PINP monitors anabolic osteoporosis therapy",
                "Teriparatide, abaloparatide, and romosozumab cause early large PINP increases; rise >10 μg/L above LSC to >65 μg/L indicates good response—no offset monitoring needed.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "An increase above the least significant change (>10 μg/L) to above the upper limit of the reference range (>65 μg/L) indicates good response. There is no role for monitoring offset of effect",
                ),
            ),
            note(
                f"{p}-n8",
                "Glucocorticoid effect",
                "Why glucocorticoids confound BTM interpretation",
                "Recent glucocorticoid dose increases suppress BTMs especially formation markers—BTMs are only helpful in glucocorticoid-induced osteoporosis if steroid dose is unchanged.",
                ref(
                    "Sources of Variability in BTMs",
                    "if the dose has been increased in the last few days BTMs would be reduced. Thus, BTMs are only helpful in patients with glucocorticoid-induced osteoporosis if the glucocorticoid dosage remains unchanged.",
                ),
            ),
            note(
                f"{p}-n9",
                "Recent fracture",
                "How recent fracture elevates BTMs for months",
                "A recent fracture causes large BTM increases peaking at 3 months and not returning to normal for a year—particularly formation markers.",
                ref(
                    "Sources of Variability in BTMs",
                    "A recent fracture results in a large increase in BTMs with a peak after 3 months and levels not returning to normal for a year.",
                ),
            ),
            note(
                f"{p}-n10",
                "Treatment failure",
                "How IOF defines pharmacologic treatment failure on denosumab",
                "One new vertebral fracture over 8 years with suppressed PINP is not treatment failure; IOF defines failure as two fractures while on treatment.",
                ref(
                    "Case 3",
                    "According to the International Osteoporosis Foundation, treatment failure is defined as having 2 fractures while on treatment.",
                ),
            ),
            note(
                f"{p}-n11",
                "BMD vs BTM",
                "Why BTMs outperform BMD for detecting treatment offset",
                "After stopping bisphosphonates, bone loss is very slow because drug persists in bone—BTMs reflect mechanism of action and detect offset earlier than BMD.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Offset of Effect",
                    "BTMs are more useful than BMD, as they reflect the way in which these drugs work.",
                ),
            ),
            note(
                f"{p}-n12",
                "US PINP",
                "FDA status of automated PINP assays in the United States",
                "Automated immunoassays are recommended worldwide except in the US where FDA has not approved automated PINP assays.",
                ref(
                    "Bone Turnover Markers",
                    "The only exception is that in the United States the automated assays for PINP have not been approved by the FDA.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — response and offset",
                "A woman on alendronate 5 years has CTX 500→120 ng/L at 6 months, then 120 at 60 months, then 400 ng/L at 72 months off drug. Interpretation?",
                [
                    "Responded to treatment and effect has worn off",
                    "Did not respond and effect has not worn off",
                    "Responded and effect has not worn off",
                    "Cannot interpret due to variability",
                ],
                0,
                "She met LSC and premenopausal median targets on treatment; offset is shown by reciprocal rise after stopping.",
                ref("Case 1", "Answer: A) She responded to treatment and the effect has worn off"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — PINP",
                "In Case 1, PINP fell from 60 to 20 μg/L at 6 months. Does this indicate treatment response?",
                [
                    "No — change is within assay noise",
                    "Yes — exceeds LSC (>10 μg/L decrease) and falls below premenopausal median (35 μg/L)",
                    "Only if BMD also increased",
                    "Cannot assess until 12 months",
                ],
                1,
                "PINP decrease >10 μg/L to 20 μg/L meets both TRIO response criteria.",
                ref(
                    "Case 1",
                    "For PINP, she responded, as she exceeded the least significant change (decrease by more than 10) and the value fell below the median for premenopausal women (35 μg/L).",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — high turnover",
                "An 87-year-old woman stopped alendronate 2 years ago after 10 years and now has a new L2 fracture; PINP is 140 μg/L. Best treatment?",
                [
                    "Watch and wait",
                    "Teriparatide",
                    "Restart alendronate at half dose",
                    "Zoledronate or denosumab",
                ],
                3,
                "High turnover after bisphosphonate offset warrants potent antiresorptive therapy—zoledronate or denosumab.",
                ref("Case 2", "Answer: D) Initiate zoledronate or denosumab"),
            ),
            mcq(
                f"{p}-q4",
                "Case 2 — half-dose alendronate",
                "Why is half-dose alendronate unlikely to suffice in Case 2?",
                [
                    "Alendronate is contraindicated after age 80",
                    "Low-dose treatment is unlikely to reach BTM target with such high turnover",
                    "PINP cannot be measured after alendronate",
                    "Teriparatide is mandatory after any vertebral fracture",
                ],
                1,
                "With PINP 140 μg/L, low-dose alendronate is unlikely to achieve adequate turnover suppression.",
                ref(
                    "Case 2",
                    "low-dosage treatment (Answer C) for such high bone turnover is unlikely to help this patient reach the BTM target.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 3 — denosumab continuation",
                "A 78-year-old on denosumab 8 years has new L3 fracture; PINP 10 μg/L; BMD T-scores -0.7 spine, -1.5 hip. Best action?",
                [
                    "Continue denosumab",
                    "Change to teriparatide",
                    "Change to zoledronate",
                    "Stop treatment",
                ],
                0,
                "PINP <35 μg/L shows effective suppression; one fracture in 8 years is not IOF-defined treatment failure.",
                ref("Case 3", "Answer: A) Continue treatment with denosumab"),
            ),
            mcq(
                f"{p}-q6",
                "Case 3 — zoledronate switch",
                "Why is switching to zoledronate not preferred in Case 3?",
                [
                    "Zoledronate is contraindicated after age 75",
                    "Zoledronate is rarely effective if denosumab is not effective",
                    "PINP must be >200 μg/L before switching",
                    "Denosumab cannot be stopped once started",
                ],
                1,
                "Denosumab is working; zoledronate is rarely effective when denosumab has failed—and denosumab has not failed here.",
                ref("Case 3", "Zoledronate (Answer C) is rarely effective if denosumab is not effective."),
            ),
            mcq(
                f"{p}-q7",
                "Case 4 — zoledronate restart",
                "A 73-year-old had 6 annual zoledronate doses, stopped 3 years ago, lost 5% hip BMD, PINP 50 μg/L. Best treatment?",
                [
                    "Watch and wait",
                    "Anabolic therapy",
                    "Single zoledronate dose",
                    "Denosumab",
                ],
                2,
                "Accelerated bone loss and elevated PINP after 3-year gap warrant zoledronate restart; 3-year gap reduces AFF concern.",
                ref("Case 4", "Answer: C) Restart zoledronate with a single dose"),
            ),
            mcq(
                f"{p}-q8",
                "TRIO LSC",
                "Per TRIO, what is the least significant change for serum CTX in an individual patient?",
                [
                    "10 ng/L",
                    "35 ng/L",
                    "120 ng/L",
                    "280 ng/L",
                ],
                2,
                "TRIO estimated LSC around 120 ng/L for CTX and 10 μg/L for PINP.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Response",
                    "This was estimated to be around 10 μg/L for PINP and 120 ng/L for CTX.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Sampling time",
                "A patient's CTX is drawn at 4 PM without fasting. Best advice?",
                [
                    "Result is valid regardless of time",
                    "Repeat fasting morning sample — CTX has marked diurnal variation",
                    "Switch to calcitonin measurement",
                    "Only urinary NTX is valid in afternoon",
                ],
                1,
                "CTX is twice as high in morning; fasting morning sampling is recommended.",
                ref(
                    "Sources of Variability in BTMs",
                    "CTX is twice as high in the morning as in the afternoon, so it is recommended to draw the patient's blood in the fasting state, first thing in the morning.",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Drug holiday indication",
                "After 5 years of alendronate, a drug holiday may be considered if:",
                [
                    "Hip T-score is above -2.5 and no recent spine fracture",
                    "Any osteopenia on spine radiograph",
                    "CTX is below premenopausal median",
                    "Patient requests holiday regardless of risk",
                ],
                0,
                "Low fracture risk (hip T > -2.5, no spine fracture) after 5 years prompts holiday consideration to reduce AFF risk.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Offset of Effect",
                    "stop treatment after 5 years if they are at relatively low fracture risk (BMD T-score above -2.5 at the hip and no recent fracture)",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Denosumab monitoring",
                "Regarding denosumab treatment response monitoring with BTMs:",
                [
                    "Everyone responds so monitoring is never useful",
                    "Rebound BTM increase after stopping may guide bisphosphonate bridging",
                    "CTX must be measured weekly",
                    "BTMs cannot change on denosumab",
                ],
                1,
                "Near-universal denosumab response limits efficacy monitoring, but offset/rebound BTMs guide transition timing.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "after stopping denosumab, there is a rebound increase in BTMs and the timing of the rebound might help dictate the optimal time to give a bisphosphonate",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Anabolic PINP",
                "One month after starting teriparatide, PINP rises from 40 to 75 μg/L. Interpretation?",
                [
                    "Treatment failure",
                    "Good anabolic response",
                    "Need to stop teriparatide immediately",
                    "Indicates osteomalacia",
                ],
                1,
                "Anabolic agents should increase PINP above LSC to above upper reference (~65 μg/L) within weeks.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "An increase above the least significant change (>10 μg/L) to above the upper limit of the reference range (>65 μg/L) indicates good response.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Recent fracture",
                "A patient had a wrist fracture 2 months ago. How does this affect BTM interpretation?",
                [
                    "No effect on BTMs",
                    "BTMs may be falsely elevated for months",
                    "BTMs are permanently suppressed",
                    "Only urinary calcium is affected",
                ],
                1,
                "Recent fractures elevate BTMs with peak at 3 months and normalization taking up to a year.",
                ref(
                    "Sources of Variability in BTMs",
                    "A recent fracture results in a large increase in BTMs with a peak after 3 months and levels not returning to normal for a year.",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Adherence",
                "BTMs measured at baseline and 3 months can help identify poor bisphosphonate adherence.",
                True,
                "IOF/ECTS working group proposed this strategy for oral bisphosphonates.",
                ref(
                    "Significance of the Clinical Problem",
                    "the measurement of BTMs before and then 3 months after starting treatment could be a successful strategy to identify poor drug response, most likely caused by poor adherence.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "TRIO response",
                "In TRIO, approximately 90% of patients met CTX response criteria at 12 weeks on oral bisphosphonates.",
                True,
                "Research-setting response rates were ~90% for CTX and ~85% for PINP using LSC.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Response",
                    "the percentage of responders using least significant change in this research study at 12 weeks of treatment was around 90% for CTX and 85% for PINP.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Offset detection",
                "BMD changes are faster and more useful than BTMs for detecting bisphosphonate offset.",
                False,
                "BTMs are more useful than BMD for detecting offset because they reflect drug mechanism.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Offset of Effect",
                    "BTMs are more useful than BMD, as they reflect the way in which these drugs work.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Denosumab failure",
                "One vertebral fracture on denosumab over 8 years constitutes treatment failure.",
                False,
                "IOF defines failure as two fractures while on treatment.",
                ref("Case 3", "treatment failure is defined as having 2 fractures while on treatment."),
            ),
            tf(
                f"{p}-tf5",
                "Anabolic offset",
                "BTMs should be monitored for offset effect after stopping teriparatide.",
                False,
                "There is no role for monitoring offset after anabolic agents—all require follow-on antiresorptive therapy.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "There is no role for monitoring offset of effect, as all these agents should be followed by treatment with antiresorptive drugs.",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Glucocorticoids",
                "Recent glucocorticoid dose increases can falsely lower bone formation markers.",
                True,
                "Glucocorticoids suppress BTMs especially formation markers within days of dose increase.",
                ref(
                    "Sources of Variability in BTMs",
                    "if the dose has been increased in the last few days BTMs would be reduced.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Case 4 watchful waiting",
                "Watchful waiting is appropriate when hip BMD has fallen 5% and PINP is 50 μg/L after stopping zoledronate.",
                False,
                "Accelerated bone loss with high turnover requires restarting therapy—not observation.",
                ref(
                    "Case 4",
                    "Watching and waiting (Answer A) would be inappropriate, as she has both accelerated bone loss and an unacceptably high bone turnover.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "US PINP",
                "Automated PINP assays are FDA-approved and widely used in the United States.",
                False,
                "Automated PINP assays have not been FDA-approved in the US.",
                ref(
                    "Bone Turnover Markers",
                    "in the United States the automated assays for PINP have not been approved by the FDA.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Treatment response",
                "Assertion: A >120 ng/L decrease in CTX after starting alendronate indicates treatment response.",
                "Reason: TRIO defined least significant change for CTX at approximately 120 ng/L.",
                0,
                "Both true—exceeding LSC signifies biologically meaningful antiresorptive effect.",
                ref(
                    "Case 1",
                    "she exceeded the least significant change (decrease by more than 120)",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Offset",
                "Assertion: Rising CTX above premenopausal median after stopping alendronate signals need to restart therapy.",
                "Reason: Bisphosphonates continue preventing bone loss for years after stopping.",
                2,
                "A is true when offset occurs; R is true about residual effect but does not negate BTM-guided restart when turnover rebounds.",
                ref(
                    "Clinical Uses of BTMs—Identification of Treatment Offset of Effect",
                    "An increase in BTM above the least significant change or a BTM level (off treatment) above the premenopausal median signify offset of response and therefore treatment would be recommended to restart.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Denosumab",
                "Assertion: PINP 10 μg/L on denosumab indicates effective treatment.",
                "Reason: Premenopausal median PINP is 35 μg/L.",
                0,
                "Both true—PINP well below median confirms strong antiresorptive effect.",
                ref(
                    "Case 3",
                    "The PINP concentration is well below the geometric mean for young women (<35 μg/L).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "High turnover restart",
                "Assertion: Zoledronate is preferred over watchful waiting when PINP is elevated after bisphosphonate discontinuation.",
                "Reason: Elevated BTMs predict greater BMD response to antiresorptives.",
                0,
                "Both true—high turnover indicates active bone loss warranting restart.",
                ref(
                    "Case 2",
                    "She is no longer having suppression of bone turnover from the prior alendronate therapy. She has high bone turnover",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Diurnal variation",
                "Assertion: Afternoon CTX values are unreliable without fasting morning sampling.",
                "Reason: CTX is twice as high in the morning as in the afternoon.",
                0,
                "Both true—diurnal variation mandates standardized morning fasting draws.",
                ref(
                    "Sources of Variability in BTMs",
                    "CTX is twice as high in the morning as in the afternoon",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Teriparatide after denosumab",
                "Assertion: Teriparatide is the best switch for one new fracture on effective denosumab.",
                "Reason: Teriparatide is more expensive than zoledronate.",
                4,
                "Both false—denosumab has not failed; cost alone does not make teriparatide the best switch.",
                ref("Case 3", "Teriparatide (Answer B) could be effective, but she has not failed to respond to denosumab."),
            ),
            ar(
                f"{p}-ar7",
                "Anabolic monitoring",
                "Assertion: PINP should rise within a month of starting teriparatide.",
                "Reason: Anabolic agents cause early large increases in formation markers.",
                0,
                "Both true—early PINP rise confirms anabolic activity.",
                ref(
                    "Clinical Uses of BTMs—Monitoring Drugs Other Than Bisphosphonates",
                    "This marker can be measured as early as a month after treatment initiation to identify response and it should increase.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Fracture confounder",
                "Assertion: Recent fracture invalidates BTM monitoring for treatment response for up to a year.",
                "Reason: Fractures increase BTMs peaking at 3 months.",
                0,
                "Both true—recent fracture elevates BTMs and confounds treatment-response interpretation for months.",
                ref(
                    "Sources of Variability in BTMs",
                    "levels not returning to normal for a year.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "12",
        "title": "Bone Turnover Markers in the Management of Osteoporosis",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Richard Eastell, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_12_Bone_Turnover_Markers_in_the_Management_of_Osteoporosis.md",
        "items": items,
    }


def build_chapter_13() -> dict:
    p = "e21-13"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Guideline variability",
                "Why osteoporosis guidelines often fail individual patients",
                "Guidelines derived from large RCTs are rigorous but restrictive; most clinic patients would not qualify for those trials, limiting direct applicability.",
                ref(
                    "Main Conclusions",
                    "Many or most patients seen in clinical practice would not qualify for participation in the clinical trials supporting the approval of the medications used to treat them",
                ),
            ),
            note(
                f"{p}-n2",
                "Treatment gap",
                "How the global osteoporosis treatment gap arose",
                "Despite excellent fracture-risk tools and approved drugs, most at-risk patients are untreated—now recognized as a global crisis.",
                ref(
                    "Significance of the Clinical Problem",
                    "most patients at risk for fractures are not being treated. The large treatment gap is now recognized as a global crisis in the care of patients with osteoporosis.",
                ),
            ),
            note(
                f"{p}-n3",
                "Personalization",
                "How to personalize osteoporosis care beyond guidelines",
                "Clinical judgment, comorbidities, prior experiences, and patient preferences must supplement guidelines—sometimes requiring multiple visits and varied educational materials.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "Clinical judgment, patient preference, and other factors are key aspects of managing complex cases of osteoporosis.",
                ),
            ),
            note(
                f"{p}-n4",
                "GIOP",
                "Why teriparatide is favored over alendronate in high-risk glucocorticoid osteoporosis",
                "An 18-month head-to-head trial showed teriparatide produced greater spine BMD gain (7.2% vs 3.4%) and lower vertebral fracture rate (0.6% vs 6.1%) than alendronate in GIOP.",
                ref(
                    "Case 1",
                    "an 18-month randomized head-to-head trial in 414 patients comparing teriparatide with alendronate in patients with glucocorticoid-induced osteoporosis showed larger gains in spine BMD (7.2% vs 3.4%), as well as lower rates of vertebral compression fracture (0.6% vs 6.1%) in the teriparatide-treated group.",
                ),
            ),
            note(
                f"{p}-n5",
                "Vertebral augmentation",
                "How ASBMR views routine vertebral augmentation",
                "ASBMR task force advises against routine vertebral augmentation for osteoporotic fractures based on 1-year pain/disability trials—though VAPOUR showed benefit for acute severe pain <6 weeks.",
                ref(
                    "Case 1",
                    "A recent American Society for Bone and Mineral Research task force advocated against routine use of vertebral augmentation for vertebral fractures based on a review of multiple trials focusing on 1-year outcomes that showed no differences in pain and disability.",
                ),
            ),
            note(
                f"{p}-n6",
                "Denosumab stopping",
                "How to stop denosumab without rebound bone loss",
                "No drug holiday exists for denosumab—when stopping, start oral alendronate at the next scheduled injection to bridge and prevent rapid bone loss and vertebral fractures.",
                ref(
                    "Case 2",
                    "Answer: C) Start oral alendronate when his next injection is due",
                ),
            ),
            note(
                f"{p}-n7",
                "Denosumab holiday myth",
                "Why denosumab does not provide lasting protection after stopping",
                "After stopping denosumab, treatment effect is rapidly lost unless another agent is started—there is no role for a drug holiday.",
                ref(
                    "Case 2",
                    "there is no role for a drug holiday with denosumab (thus, Answer A is incorrect). After stopping denosumab, the treatment effect will be rapidly lost if another agent is not started.",
                ),
            ),
            note(
                f"{p}-n8",
                "Romosozumab mechanism",
                "How romosozumab dual-action differs from pure antiresorptives",
                "Romosozumab inhibits sclerostin, stimulating bone formation via Wnt signaling while reducing resorption through RANKL up-regulation—given monthly ×12 months then followed by antiresorptive therapy.",
                ref(
                    "Case 3",
                    "by inhibiting sclerostin, it has a dual action of stimulating bone formation and reducing bone resorption.",
                ),
            ),
            note(
                f"{p}-n9",
                "Romosozumab warning",
                "Why romosozumab carries a cardiovascular boxed warning",
                "ARCH trial showed numerically more cardiovascular events with romosozumab vs alendronate in year 1—FDA boxed warning against use within 12 months of MI or stroke.",
                ref(
                    "Case 3",
                    "there is a boxed warning that romosozumab may increase the risk of myocardial infarction, stroke, and cardiovascular death and should not be initiated in patients who have had a myocardial infarction or stroke within the preceding year (Answer B).",
                ),
            ),
            note(
                f"{p}-n10",
                "Romosozumab safety",
                "ONJ and AFF with romosozumab",
                "Atypical femoral fractures and osteonecrosis of the jaw occurred in FRAME and ARCH trials—likely related to antiresorptive component, not absent.",
                ref(
                    "Case 3",
                    "Atypical femoral fractures and osteonecrosis of the jaw were reported during both the FRAME and ARCH studies, thought to be related to the antiresorptive action (thus, Answer A is incorrect).",
                ),
            ),
            note(
                f"{p}-n11",
                "Osteoporosis diagnosis",
                "Why osteopenia on DXA does not exclude treatment in vertebral fracture",
                "A low-trauma vertebral fracture establishes osteoporosis diagnosis regardless of T-score—pharmacotherapy is indicated in high-risk patients.",
                ref(
                    "Case 1",
                    "This patient has the diagnosis of osteoporosis based on a low-trauma fracture and has a very high risk for future fracture; thus, pharmacologic therapy is indicated (thus, Answer A is incorrect).",
                ),
            ),
            note(
                f"{p}-n12",
                "TeleECHO",
                "How Bone Health TeleECHO addresses the treatment gap",
                "Technology-enabled collaborative learning such as Bone Health TeleECHO is one proposed strategy to reduce the osteoporosis treatment gap.",
                ref(
                    "Strategies for Diagnosis, Therapy, and/or Management",
                    "many strategies to reduce the treatment gap have been proposed, including technology-enabled collaborative learning, the prototype of which is Bone Health TeleECHO.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — GIOP",
                "A 62-year-old woman with COPD, chronic oral steroids, and painful vertebral fracture has osteopenia on DXA. Best therapy to reduce future vertebral fractures?",
                [
                    "Calcium and vitamin D only",
                    "Kyphoplasty alone",
                    "Teriparatide 18–24 months then antiresorptive",
                    "Oral alendronate 5 years then drug holiday",
                ],
                2,
                "Vertebral fracture defines osteoporosis; teriparatide showed superior BMD and vertebral fracture prevention vs alendronate in GIOP trial.",
                ref("Case 1", "Answer: C) Teriparatide for 18 to 24 months followed by antiresorptive therapy"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — calcium/vitamin D",
                "Why is calcium and vitamin D alone insufficient in Case 1?",
                [
                    "She has osteoporosis by fracture history with very high future fracture risk",
                    "Steroids block calcium absorption completely",
                    "DXA osteopenia rules out treatment",
                    "Teriparatide is contraindicated with COPD",
                ],
                0,
                "Low-trauma vertebral fracture establishes osteoporosis and mandates pharmacotherapy beyond supplements.",
                ref(
                    "Case 1",
                    "This patient has the diagnosis of osteoporosis based on a low-trauma fracture and has a very high risk for future fracture; thus, pharmacologic therapy is indicated",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 1 — kyphoplasty",
                "Regarding kyphoplasty for this patient's vertebral fracture:",
                [
                    "Routine use reduces adjacent-level fracture risk",
                    "It would not be expected to reduce adjacent fracture rate",
                    "ASBMR recommends routine augmentation for all vertebral fractures",
                    "It replaces need for pharmacotherapy",
                ],
                1,
                "Vertebral augmentation does not reduce adjacent-level fracture risk; ASBMR advises against routine use.",
                ref(
                    "Case 1",
                    "vertebral augmentation would not be expected to reduce the rate of adjacent level fracture.",
                ),
            ),
            mcq(
                f"{p}-q4",
                "Case 1 — alendronate",
                "When might oral alendronate still be chosen over teriparatide in GIOP?",
                [
                    "Never — alendronate is contraindicated with steroids",
                    "If teriparatide is not financially viable, contraindicated, or not desired",
                    "Only if DXA shows osteoporosis not osteopenia",
                    "Only in men under age 50",
                ],
                1,
                "Alendronate remains reasonable when teriparatide is unavailable or declined, though teriparatide has stronger GIOP data.",
                ref(
                    "Case 1",
                    "oral alendronate (Answer D) is a reasonable choice if teriparatide is not financially viable, is contraindicated, or is otherwise not desired by the patient",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 2 — denosumab stop",
                "A 70-year-old man on denosumab 8 years (eGFR 60, osteopenia on DXA) wants to stop. Best advice?",
                [
                    "Stop denosumab for a drug holiday",
                    "IV zoledronic acid 6 months after last dose",
                    "Start oral alendronate when next injection is due",
                    "Remain on denosumab for life — no alternatives studied",
                ],
                2,
                "Bridge with oral alendronate at the scheduled next injection—no denosumab drug holiday exists.",
                ref("Case 2", "Answer: C) Start oral alendronate"),
            ),
            mcq(
                f"{p}-q6",
                "Case 2 — zoledronate bridge",
                "Why is single-dose zoledronate at next injection date not the preferred answer in Case 2?",
                [
                    "Zoledronate is contraindicated with eGFR 60",
                    "Oral alendronate at next injection is the specified best advice in this vignette",
                    "Denosumab can never be stopped",
                    "Zoledronate causes rebound fractures",
                ],
                1,
                "The vignette answer is oral alendronate at next scheduled dose; zoledronate bridging is discussed elsewhere but answer C is preferred here.",
                ref("Case 2", "Answer: C) Start oral alendronate when his next injection is due"),
            ),
            mcq(
                f"{p}-q7",
                "Case 3 — romosozumab warning",
                "Which statement about romosozumab is true?",
                [
                    "No ONJ or AFF occurred in any romosozumab trial",
                    "Boxed warning against use within 12 months of MI or stroke",
                    "Contraindicated in all patients at osteosarcoma risk",
                    "Sclerostin inhibition reduces bone formation via Wnt pathway",
                ],
                1,
                "FDA boxed warning prohibits initiation within 12 months of MI or stroke; ONJ/AFF did occur; sclerostin inhibits (not stimulates) Wnt signaling.",
                ref("Case 3", "Answer: B) There is a boxed warning against using romosozumab in anyone who has had a myocardial infarction in the preceding 12 months"),
            ),
            mcq(
                f"{p}-q8",
                "Case 3 — sclerostin",
                "Romosozumab's mechanism of action is best described as:",
                [
                    "Pure antiresorptive like bisphosphonates",
                    "Dual anabolic and antiresorptive via sclerostin inhibition",
                    "RANKL antibody",
                    "PTH analog",
                ],
                1,
                "Anti-sclerostin antibody stimulates formation and reduces resorption—a novel dual mechanism.",
                ref(
                    "Case 3",
                    "by inhibiting sclerostin, it has a dual action of stimulating bone formation and reducing bone resorption.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Case 3 — osteosarcoma",
                "Is romosozumab contraindicated in patients at high osteosarcoma risk?",
                [
                    "Yes — same restriction as teriparatide",
                    "No — no evidence of increased osteosarcoma risk with sclerostin inhibition",
                    "Yes — due to ONJ risk",
                    "Only in patients over age 80",
                ],
                1,
                "No osteosarcoma warning exists for romosozumab unlike teriparatide's rodent data concerns.",
                ref(
                    "Case 3",
                    "Since there is no evidence of increased risk of osteosarcoma with sclerostin inhibition in rats or humans, there is no warning against its use in patients previously receiving radiation therapy or otherwise at high risk of osteosarcoma",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Guideline trials",
                "Why may strict RCT-based guidelines not fit many clinic patients?",
                [
                    "RCTs never include osteoporosis patients",
                    "Most treated patients would not have qualified for pivotal trials",
                    "All guidelines ignore fracture risk",
                    "DXA is never used in trials",
                ],
                1,
                "Trial eligibility criteria exclude many real-world patients, limiting guideline applicability.",
                ref(
                    "Main Conclusions",
                    "Many or most patients seen in clinical practice would not qualify for participation in the clinical trials supporting the approval of the medications used to treat them",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Treatment barriers",
                "Which factor contributes to the osteoporosis treatment gap?",
                [
                    "Excessive DXA reimbursement",
                    "Fear of medication adverse effects",
                    "Lack of any approved therapies",
                    "Universal overtreatment",
                ],
                1,
                "Fear of adverse effects, poor risk communication, and conflicting guidelines among factors widening the gap.",
                ref(
                    "Barriers to Optimal Practice",
                    "Many factors contribute to the treatment gap, including fear of medication adverse effects",
                ),
            ),
            mcq(
                f"{p}-q12",
                "FRAME trial",
                "In FRAME, romosozumab for 12 months followed by denosumab showed:",
                [
                    "73% reduction in vertebral fracture incidence in year 1 vs placebo",
                    "No vertebral fracture benefit",
                    "Increased hip fractures in year 1",
                    "Mandatory lifelong romosozumab",
                ],
                0,
                "FRAME demonstrated 73% vertebral fracture reduction in first year of romosozumab vs placebo before denosumab continuation.",
                ref(
                    "Case 3",
                    "In the first year, the romosozumab group had a 73% reduction in vertebral fracture incidence",
                ),
            ),
            mcq(
                f"{p}-q13",
                "ARCH cardiovascular",
                "ARCH trial cardiovascular findings led to:",
                [
                    "Withdrawal of romosozumab from all markets",
                    "Boxed warning and avoidance after recent MI/stroke",
                    "Mandatory daily ECG monitoring",
                    "Contraindication in all diabetics",
                ],
                1,
                "Numerically increased CV events in year 1 prompted boxed warning against recent MI/stroke.",
                ref(
                    "Case 3",
                    "there is a boxed warning that romosozumab may increase the risk of myocardial infarction, stroke, and cardiovascular death",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "GIOP teriparatide",
                "Teriparatide reduced vertebral fractures more than alendronate in glucocorticoid-induced osteoporosis.",
                True,
                "Vertebral fracture rate was 0.6% vs 6.1% favoring teriparatide in the head-to-head trial.",
                ref(
                    "Case 1",
                    "lower rates of vertebral compression fracture (0.6% vs 6.1%) in the teriparatide-treated group.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Denosumab holiday",
                "A drug holiday is appropriate after 8 years of denosumab if BMD is in the osteopenia range.",
                False,
                "There is no role for a denosumab drug holiday—rapid offset causes bone loss without bridging therapy.",
                ref("Case 2", "there is no role for a drug holiday with denosumab"),
            ),
            tf(
                f"{p}-tf3",
                "Romosozumab ONJ",
                "No cases of osteonecrosis of the jaw occurred in romosozumab trials.",
                False,
                "ONJ was reported in FRAME and ARCH, attributed to antiresorptive action.",
                ref(
                    "Case 3",
                    "osteonecrosis of the jaw were reported during both the FRAME and ARCH studies",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Sclerostin",
                "Sclerostin acts to increase bone formation via the Wnt pathway.",
                False,
                "Sclerostin inhibits Wnt signaling and reduces osteoblastic bone formation.",
                ref(
                    "Case 3",
                    "Sclerostin reduces osteoblastic bone formation by binding to LRP5/6, inhibiting Wnt signaling",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Vertebral fracture diagnosis",
                "A low-trauma vertebral fracture establishes an osteoporosis diagnosis regardless of DXA T-score.",
                True,
                "Fracture-based diagnosis applies even when DXA shows osteopenia.",
                ref(
                    "Case 1",
                    "This patient has the diagnosis of osteoporosis based on a low-trauma fracture",
                ),
            ),
            tf(
                f"{p}-tf6",
                "Denosumab bridge",
                "Oral alendronate should be started when the next denosumab injection is due if denosumab is stopped.",
                True,
                "Bridging at the next scheduled dose prevents rapid loss of treatment effect.",
                ref("Case 2", "Answer: C) Start oral alendronate when his next injection is due"),
            ),
            tf(
                f"{p}-tf7",
                "Guidelines",
                "Expert-based guidelines are never criticized for subjectivity.",
                False,
                "Expert guidelines may be simpler but are criticized for lower evidence levels and subjectivity.",
                ref(
                    "Main Conclusions",
                    "Guidelines developed by experts interpreting the best available medical evidence may be simpler, more intuitive, and easier to apply in clinical practice, but are open to criticism that they are overly subjective",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Romosozumab duration",
                "Romosozumab is given monthly for 12 months and should be followed by additional osteoporosis therapy.",
                True,
                "Monthly ×12 months then antiresorptive follow-on to maintain/enhance effects.",
                ref(
                    "Case 3",
                    "Romosozumab is given subcutaneously by a health care professional once monthly for 12 months and should be followed up with an additional osteoporosis treatment to maintain or enhance its effects.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "GIOP",
                "Assertion: Teriparatide is preferred over alendronate for high-risk glucocorticoid-induced osteoporosis with vertebral fracture.",
                "Reason: Teriparatide produced greater spine BMD gain and lower vertebral fracture rate than alendronate in a head-to-head trial.",
                0,
                "Both true and causally linked—trial data support teriparatide for secondary vertebral fracture prevention in GIOP.",
                ref(
                    "Case 1",
                    "the strongest data for secondary fracture prevention in this scenario would be for teriparatide (Answer C).",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Denosumab stop",
                "Assertion: Stopping denosumab without bridging causes rapid loss of treatment effect.",
                "Reason: Denosumab is a monoclonal antibody with no lasting skeletal effect after clearance.",
                0,
                "Both true—antibody clearance produces rapid rebound bone turnover unlike bisphosphonate persistence.",
                ref(
                    "Case 2",
                    "After stopping denosumab, the treatment effect will be rapidly lost if another agent is not started.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Romosozumab CV",
                "Assertion: Romosozumab should not be started within 12 months of myocardial infarction.",
                "Reason: ARCH showed numerically more cardiovascular events with romosozumab than alendronate in year 1.",
                0,
                "Both true—ARCH data underpin the FDA boxed warning.",
                ref(
                    "Case 3",
                    "should not be initiated in patients who have had a myocardial infarction or stroke within the preceding year (Answer B).",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Kyphoplasty",
                "Assertion: Kyphoplasty prevents adjacent vertebral fractures after osteoporotic compression fracture.",
                "Reason: Kyphoplasty reduces acute pain in selected patients.",
                2,
                "A is false—adjacent fracture prevention is not shown; R true for pain in VAPOUR subset but doesn't explain A.",
                ref(
                    "Case 1",
                    "vertebral augmentation would not be expected to reduce the rate of adjacent level fracture.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Osteopenia treatment",
                "Assertion: Calcium and vitamin D alone suffice after vertebral fracture if DXA shows osteopenia.",
                "Reason: Osteopenia indicates low bone density.",
                2,
                "A is false—fracture defines osteoporosis regardless of T-score; R is true but irrelevant to withholding pharmacotherapy.",
                ref(
                    "Case 1",
                    "pharmacologic therapy is indicated (thus, Answer A is incorrect).",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Sclerostin",
                "Assertion: Romosozumab increases bone formation by inhibiting sclerostin.",
                "Reason: Sclerostin normally inhibits Wnt-mediated osteoblastic bone formation.",
                0,
                "Both true—inhibiting the inhibitor stimulates formation.",
                ref(
                    "Case 3",
                    "Bone formation is increased when sclerostin is inhibited (thus, Answer D is incorrect).",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Trial eligibility",
                "Assertion: Strict RCT-based guidelines may not apply to many real-world osteoporosis patients.",
                "Reason: Most clinic patients would not have met trial inclusion criteria.",
                0,
                "Both true—external validity of trials limits one-size-fits-all guideline application.",
                ref(
                    "Main Conclusions",
                    "Many or most patients seen in clinical practice would not qualify for participation in the clinical trials",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Denosumab alendronate",
                "Assertion: Oral alendronate at the next scheduled injection is the best bridge when stopping denosumab in Case 2.",
                "Reason: Zoledronate has never been studied after denosumab.",
                2,
                "A is true per vignette answer; R is false—zoledronate bridging has been studied though alendronate is preferred here.",
                ref("Case 2", "Answer: C) Start oral alendronate when his next injection is due"),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "13",
        "title": "Using the Best Available Evidence to Personalize Osteoporosis Treatment",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "E. Michael Lewiecki, MD; Micol S. Rothman, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_13_Using_the_Best_Available_Evidence_to_Personalize_Osteoporosis_Treatment.md",
        "items": items,
    }


def build_chapter_14() -> dict:
    p = "e21-14"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Rickets prevention",
                "Why 400 IU daily vitamin D prevents infantile rickets",
                "Vitamin D at 400 IU daily prevents rickets in infants—universal supplementation largely eliminated nutritional rickets in Europe and North America.",
                ref(
                    "Main Conclusions",
                    "Vitamin D, at dosages of 400 IU daily, prevents rickets in infants.",
                ),
            ),
            note(
                f"{p}-n2",
                "Desirable level debate",
                "How IOM and Endocrine Society differ on desirable 25-OHD",
                "IOM sets desirable 25-OHD at 20 ng/mL (50 nmol/L) for the general public; Endocrine Society targets 30 ng/mL (75 nmol/L) for at-risk individuals with higher supplementation doses.",
                ref(
                    "Management Strategies/Vitamin D Guidelines",
                    "reach differing conclusions in terms of the desirable 25-OHD level, set at 30 ng/mL (75 nmol/L) by the Endocrine Society and 20 ng/mL (50 nmol/L) by the Institute of Medicine.",
                ),
            ),
            note(
                f"{p}-n3",
                "Assay variability",
                "Why 25-OHD assay variation exceeds guideline threshold differences",
                "Parallel assays can differ by -38 to +19 ng/mL independent of true level—bias exceeding the IOM vs Endocrine Society target gap mandates laboratory standardization.",
                ref(
                    "Impact of Assay Variation on Management Strategies",
                    "serum values measured in parallel with 2 assays could vary between -38 to +19 ng/mL, a bias that was independent of the serum 25-OHD level.",
                ),
            ),
            note(
                f"{p}-n4",
                "Screening",
                "Why population 25-OHD screening is not recommended",
                "All major guidelines concur screening is not for the general population—reserved for high-risk individuals; it does not meet WHO screening test criteria.",
                ref(
                    "Should We Screen by Measuring Serum 25-OHD Levels?",
                    "All guidelines concur that screening for vitamin D deficiency is not recommended for the general population and should be reserved for high-risk individuals.",
                ),
            ),
            note(
                f"{p}-n5",
                "Osteomalacia treatment",
                "How to treat nutritional osteomalacia with vitamin D",
                "A widely used regimen is 50,000 IU weekly for 6–8 weeks followed by 800 IU daily maintenance; PTH and ALP may take months to normalize.",
                ref(
                    "Treatment of Osteomalacia",
                    "A widely used regimen consists of giving 50,000 IU weekly for 6 to 8 weeks followed by 800 IU daily maintenance therapy.",
                ),
            ),
            note(
                f"{p}-n6",
                "Osteomalacia vs osteoporosis",
                "Why osteomalacia is not osteoporosis on DXA",
                "DXA cannot distinguish osteomalacia from osteoporosis; healing osteomalacia produces substantial BMD gains reflecting mineralization recovery, not antiresorptive treatment of osteoporosis.",
                ref(
                    "Case 1",
                    "DXA does not distinguish osteomalacia from osteoporosis. She experienced substantial increments in bone mineral density within 4 months",
                ),
            ),
            note(
                f"{p}-n7",
                "Pregnancy vitamin D",
                "How vitamin D in pregnancy affects maternal-fetal outcomes",
                "Vitamin D probably reduces preeclampsia (±calcium), gestational diabetes, low birth weight <2500 g, and severe postpartum bleeding—though high-quality data in high-risk groups are still needed.",
                ref(
                    "Main Conclusions",
                    "Vitamin D given in pregnancy probably reduces the risk of preeclampsia (± calcium), gestational diabetes, low neonatal birth weight (<2500 g), and severe postpartum bleeding.",
                ),
            ),
            note(
                f"{p}-n8",
                "Fracture prevention young adults",
                "Why vitamin D alone does not prevent fractures in adults <65",
                "No benefit of vitamin D supplementation alone on fractures or falls in ambulatory adults younger than 65 years; calcium co-administration is needed for hip/any fracture reduction in elderly.",
                ref(
                    "Main Conclusions",
                    "There is no benefit of vitamin D supplementation alone on fractures or falls in ambulatory adults younger than 65 years.",
                ),
            ),
            note(
                f"{p}-n9",
                "Safety ceiling",
                "What daily vitamin D doses are considered safe",
                "Hypercalcemia/hypercalciuria are unlikely up to 2000 IU daily; upper tolerable intake is 4000 IU—VITAL trial showed increased kidney stones at that dose.",
                ref(
                    "Main Conclusions",
                    "Hypercalcemia and hypercalciuria are unlikely to occur at dosages of up to 2000 IU daily. The upper tolerable level is 4000 IU daily, and the VITAL trial demonstrated an increased risk of kidney stones at such dosages.",
                ),
            ),
            note(
                f"{p}-n10",
                "D2 vs D3",
                "How vitamin D3 compares to D2 for efficacy",
                "Vitamin D3-based supplements are superior to D2 in terms of efficacy for raising and maintaining 25-OHD.",
                ref("Case 2", "Answer: A) Yes"),
            ),
            note(
                f"{p}-n11",
                "COVID-19",
                "Why high-dose vitamin D for COVID-19 is not evidence-based",
                "Systematic review shows no association between vitamin D deficiency and COVID-19 outcomes—high doses are unwarranted pending trial results; stay below 4000 IU daily.",
                ref(
                    "Case 4",
                    "The overwhelming evidence to date, based on these studies, mostly of low quality, reveals no association between vitamin D deficiency and COVID-19-related health outcomes.",
                ),
            ),
            note(
                f"{p}-n12",
                "Obesity dosing",
                "Why obese patients need higher vitamin D doses",
                "Obesity lowers CYP2R1 expression and serum 25-OHD; patients with obesity require higher supplementation doses to achieve target levels.",
                ref(
                    "Management Strategies/Vitamin D Guidelines",
                    "Patients with obesity require higher dosages.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — diagnosis",
                "A 51-year-old woman has calcium 6.9 mg/dL, phosphate 2.2, ALP 820, 25-OHD <2 ng/mL, PTH 250, and pelvic Looser zones. Most likely diagnosis?",
                [
                    "Obesity",
                    "Malabsorption",
                    "Nutritional osteomalacia",
                    "X-linked hypophosphatemic rickets",
                ],
                2,
                "Severe vitamin D deficiency with hypocalcemia, elevated ALP/PTH, and Looser zones is classic nutritional osteomalacia.",
                ref("Case 1", "Answer: C) Nutritional osteomalacia"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — osteoporosis",
                "She has spine T-score -2.6 and hip -2.4. Does she have osteoporosis?",
                [
                    "Yes — T-score below -2.5",
                    "No — this is osteomalacia not osteoporosis",
                    "Yes — Looser zones confirm osteoporosis",
                    "Cannot determine without bone biopsy",
                ],
                1,
                "DXA cannot distinguish osteomalacia from osteoporosis; low T-scores reflect defective mineralization.",
                ref("Case 1", "Answer: B) No"),
            ),
            mcq(
                f"{p}-q3",
                "Case 1 — treatment",
                "Best vitamin D regimen with daily calcium for this osteomalacia patient?",
                [
                    "1000 IU daily only",
                    "50,000 IU daily",
                    "50,000 IU weekly for several weeks then 600–1000 IU daily",
                    "600,000 IU stoss dose every 6–12 months",
                ],
                2,
                "High-dose repletion then maintenance is standard—50,000 IU weekly for weeks then daily maintenance.",
                ref("Case 1", "Answer: C) Vitamin D at 50,000 IU weekly for several weeks followed by 600 to 1000 IU daily"),
            ),
            mcq(
                f"{p}-q4",
                "Case 1 — biomarker recovery",
                "When should PTH and alkaline phosphatase normalize after repletion?",
                [
                    "Days",
                    "Weeks",
                    "Months",
                    "Never",
                ],
                2,
                "Calcium/phosphate normalize in days but PTH and ALP may take more than a year—months is the expected timeframe.",
                ref("Case 1", "Answer: C) Months"),
            ),
            mcq(
                f"{p}-q5",
                "Case 2 — dosing frequency",
                "Are daily (1500 IU), weekly (10,500 IU), and monthly (45,000 IU) vitamin D regimens equivalent in adults?",
                [
                    "Yes — no clinically important difference",
                    "No — only daily dosing is effective",
                    "No — monthly dosing is always superior",
                    "Yes — but only D2 formulations are equivalent",
                ],
                0,
                "Equivalent total doses given at different intervals produce similar outcomes.",
                ref("Case 2", "Answer: B) No"),
            ),
            mcq(
                f"{p}-q6",
                "Case 2 — pregnancy dose",
                "Recommended total daily vitamin D intake during pregnancy per IOM?",
                [
                    "100 IU daily",
                    "600 IU daily",
                    "5000 IU daily",
                    "10,000 IU daily",
                ],
                1,
                "IOM RDA is 600 IU daily in pregnancy; Endocrine Society recommends 1500–2000 IU for at-risk patients.",
                ref("Case 2", "Answer: B) 600 IU daily"),
            ),
            mcq(
                f"{p}-q7",
                "Case 2 — pregnancy outcomes",
                "Does vitamin D supplementation in pregnancy reduce complications like preeclampsia?",
                [
                    "Yes — definitively proven",
                    "Possibly",
                    "No",
                    "Only with calcium co-administration in all pregnancies",
                ],
                1,
                "Cochrane review suggests probable benefit for preeclampsia, gestational diabetes, and low birth weight—evidence still evolving.",
                ref("Case 2", "Answer: B) Possibly"),
            ),
            mcq(
                f"{p}-q8",
                "Case 2 — infant rickets",
                "Universal recommended vitamin D dose for breastfed infants to prevent rickets?",
                [
                    "200 IU daily",
                    "400 IU daily",
                    "600 IU daily",
                    "1000 IU daily",
                ],
                1,
                "400 IU daily from infancy prevents rickets; increase to 600 IU after age 1 year.",
                ref("Case 2", "Answer: B) 400 IU daily"),
            ),
            mcq(
                f"{p}-q9",
                "Case 2 — children",
                "Recommended daily vitamin D for 5- and 10-year-old children?",
                [
                    "400–600 IU daily",
                    "2500 IU daily",
                    "4000 IU daily",
                    "No supplementation needed if diet is adequate",
                ],
                0,
                "IOM RDA 600 IU; Endocrine Society 600–1000 IU for at-risk children—400–600 IU daily is the recommended range cited.",
                ref("Case 2", "Answer: A) 400-600 IU daily"),
            ),
            mcq(
                f"{p}-q10",
                "Case 3 — hip fracture community",
                "In community-dwelling individuals, does vitamin D with calcium decrease hip fracture risk?",
                [
                    "Yes — clearly in community dwellers alone",
                    "No — not demonstrated in community-dwelling individuals alone",
                    "No evidence exists",
                    "Yes — but only with 10,000 IU daily vitamin D",
                ],
                1,
                "Fracture benefit when combining trials is driven largely by institutionalized elderly; community benefit remains unclear.",
                ref("Case 3", "Answer: B) No"),
            ),
            mcq(
                f"{p}-q11",
                "Case 3 — cardiovascular",
                "Does vitamin D with calcium increase cardiovascular event risk?",
                [
                    "Yes",
                    "No",
                    "Possibly",
                    "Only in patients with baseline hypercalcemia",
                ],
                1,
                "Meta-analyses including VITAL do not show increased cardiovascular events with vitamin D plus calcium.",
                ref("Case 3", "Answer: B) No"),
            ),
            mcq(
                f"{p}-q12",
                "Case 3 — cancer",
                "Does vitamin D supplementation decrease cancer risk?",
                [
                    "Yes",
                    "No",
                    "Possibly",
                    "Only for skin cancer",
                ],
                1,
                "VITAL and meta-analyses show no clear cancer reduction with vitamin D supplementation alone.",
                ref("Case 3", "Answer: B) No"),
            ),
            mcq(
                f"{p}-q13",
                "Case 4 — COVID-19",
                "A COVID-19 patient is started on 50,000 IU weekly vitamin D to prevent complications. Best evidence statement?",
                [
                    "Yes — proven benefit",
                    "No — proven no benefit",
                    "Weak low-quality evidence only",
                    "No evidence available",
                ],
                3,
                "Systematic review found no association between vitamin D deficiency and COVID-19 outcomes—high doses unwarranted.",
                ref("Case 4", "Answer: D) No evidence available"),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Rickets",
                "400 IU daily vitamin D prevents rickets in infants.",
                True,
                "Universal infant supplementation largely eliminated nutritional rickets in developed countries.",
                ref("Main Conclusions", "Vitamin D, at dosages of 400 IU daily, prevents rickets in infants."),
            ),
            tf(
                f"{p}-tf2",
                "Young adults",
                "Vitamin D alone prevents fractures in ambulatory adults younger than 65.",
                False,
                "No demonstrated fracture or fall benefit in this age group.",
                ref(
                    "Main Conclusions",
                    "There is no benefit of vitamin D supplementation alone on fractures or falls in ambulatory adults younger than 65 years.",
                ),
            ),
            tf(
                f"{p}-tf3",
                "Calcium combination",
                "Vitamin D co-administered with calcium reduces hip and any fracture risk in elderly.",
                True,
                "Cochrane meta-analysis shows RR reductions for hip and any fractures with combined therapy.",
                ref(
                    "Main Conclusions",
                    "Vitamin D co-administered with calcium reduces the risk of hip fractures and any fractures.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Screening",
                "Routine 25-OHD screening is recommended for the general population.",
                False,
                "Screening reserved for high-risk individuals; does not meet WHO screening criteria.",
                ref(
                    "Should We Screen by Measuring Serum 25-OHD Levels?",
                    "screening for vitamin D deficiency is not recommended for the general population",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Non-skeletal benefits",
                "Vitamin D supplementation has proven beneficial effects on nonclassic outcomes.",
                False,
                "No beneficial effect on nonclassic outcomes demonstrated.",
                ref("Main Conclusions", "Vitamin D supplementation has no beneficial effect on nonclassic outcomes."),
            ),
            tf(
                f"{p}-tf6",
                "D3 superiority",
                "Vitamin D3 supplements are superior to D2 for efficacy.",
                True,
                "D3 is superior for raising and maintaining 25-OHD levels.",
                ref("Case 2", "Answer: A) Yes"),
            ),
            tf(
                f"{p}-tf7",
                "Safety 2000 IU",
                "Hypercalcemia is unlikely at vitamin D doses up to 2000 IU daily.",
                True,
                "Up to 2000 IU daily is unlikely to cause hypercalcemia or hypercalciuria.",
                ref(
                    "Main Conclusions",
                    "Hypercalcemia and hypercalciuria are unlikely to occur at dosages of up to 2000 IU daily.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "COVID-19",
                "High-dose vitamin D is proven to prevent COVID-19 complications.",
                False,
                "No good evidence of benefit; high doses unwarranted pending trial data.",
                ref(
                    "Main Conclusions",
                    "To date there is no good evidence of a beneficial effect of vitamin D on COVID-19-related complications.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Osteomalacia",
                "Assertion: Severe vitamin D deficiency with Looser zones represents nutritional osteomalacia not osteoporosis.",
                "Reason: DXA cannot distinguish osteomalacia from osteoporosis.",
                0,
                "Both true—biochemical and radiographic features define osteomalacia despite low T-scores on DXA.",
                ref("Case 1", "DXA does not distinguish osteomalacia from osteoporosis."),
            ),
            ar(
                f"{p}-ar2",
                "Repletion regimen",
                "Assertion: 50,000 IU vitamin D weekly followed by daily maintenance treats osteomalacia effectively.",
                "Reason: Several regimens can heal osteomalacia.",
                0,
                "Both true—high-dose repletion then maintenance is a standard effective approach.",
                ref(
                    "Treatment of Osteomalacia",
                    "Several regimens are used and all can heal osteomalacia effectively.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Assay bias",
                "Assertion: Laboratory assay variation can exceed differences between guideline 25-OHD targets.",
                "Reason: IOM and Endocrine Society differ by 10 ng/mL in desirable levels.",
                0,
                "Both true—parallel assay bias of up to 38 ng/mL dwarfs the 10 ng/mL guideline gap.",
                ref(
                    "Impact of Assay Variation on Management Strategies",
                    "serum values measured in parallel with 2 assays could vary between -38 to +19 ng/mL",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Community fractures",
                "Assertion: Vitamin D plus calcium clearly prevents hip fractures in community-dwelling adults alone.",
                "Reason: Combined therapy reduces hip fractures when institutionalized and community trials are pooled.",
                2,
                "A is false for community dwellers alone; R is true for pooled elderly data but doesn't prove community benefit.",
                ref(
                    "Case 3",
                    "The impact of routine supplementation on musculoskeletal outcomes in community-dwelling individuals remains unclear.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Pregnancy",
                "Assertion: Vitamin D supplementation in pregnancy probably reduces preeclampsia risk.",
                "Reason: WHO recommends routine vitamin D supplementation in all pregnancies.",
                2,
                "A is supported by Cochrane data; R is false—WHO 2012 guidelines recommend against routine supplementation.",
                ref(
                    "Case 2",
                    "the World Health Organization 2012 vitamin D guidelines in pregnancy recommend against routine vitamin D supplementation.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "COVID dosing",
                "Assertion: 50,000 IU weekly vitamin D is warranted to prevent COVID-19 complications.",
                "Reason: Vitamin D modulates innate and adaptive immunity.",
                2,
                "A is unsupported; R is true mechanistically but does not justify high-dose empiric use without outcome evidence.",
                ref(
                    "Case 4",
                    "the use of high dosages of vitamin D is unwarranted and awaits evidence from ongoing trials.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Infant dosing",
                "Assertion: 400 IU daily prevents rickets in breastfed infants.",
                "Reason: Nutritional rickets persists in high-risk global populations.",
                1,
                "Both true but unrelated—ongoing rickets in some regions doesn't negate 400 IU efficacy when given.",
                ref("Main Conclusions", "Vitamin D, at dosages of 400 IU daily, prevents rickets in infants."),
            ),
            ar(
                f"{p}-ar8",
                "Obesity",
                "Assertion: Obese patients need higher vitamin D supplementation doses.",
                "Reason: Obesity is associated with lower serum 25-OHD through reduced CYP2R1 expression.",
                0,
                "Both true—obesity lowers 25-OHD and requires higher replacement doses.",
                ref(
                    "Genetic Polymorphisms and Environmental Predictors of Serum 25-OHD Levels",
                    "obesity, type 1 and type 2 diabetes mellitus, fasting, and glucocorticoid therapy are associated with lower serum 25-OHD levels.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "14",
        "title": "Is There an Ideal Vitamin D Level and Dosage for All Circumstances?",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Ghada El-Hajj Fuleihan, MD, MPH",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_14_Is_There_an_Ideal_Vitamin_D_Level_and_Dosage_for_All_Circumstances.md",
        "items": items,
    }


def build_chapter_15() -> dict:
    p = "e21-15"
    items: list[dict] = []

    items.extend(
        [
            note(
                f"{p}-n1",
                "Drug offset",
                "Why osteoporosis drug offset patterns differ by class",
                "Bisphosphonates bind bone for years with slow offset; denosumab offset is rapid with rebound; anabolics lose BMD gains unless followed by antiresorptives.",
                ref(
                    "Main Conclusions",
                    "Anabolics (teriparatide, abaloparatide, romosozumab) Bone mineral density (BMD) gains during treatment are lost in the months following cessation. Therefore, for each of these agents, it is important to lock in the BMD gains with the use of an antiresorptive agent",
                ),
            ),
            note(
                f"{p}-n2",
                "Alendronate holiday",
                "How long alendronate persists after stopping",
                "After 5 years alendronate, a 1-year holiday is often appropriate; FLEX showed 5-year holiday does not increase nonvertebral fractures though vertebral fractures may rise.",
                ref(
                    "Case 2",
                    "The FLEX study indicates that a 5-year drug holiday will not increase her risk of nonvertebral fractures, but there may be a rise in the incidence of clinical vertebral fractures.",
                ),
            ),
            note(
                f"{p}-n3",
                "Risedronate offset",
                "How risedronate offset differs from alendronate",
                "Risedronate turnover suppression offsets within 12 months with femoral neck BMD returning to baseline—faster than alendronate or zoledronate.",
                ref(
                    "Bisphosphonates",
                    "Studies of risedronate demonstrate a more rapid offset of bone turnover suppression, within 12 months of drug discontinuation.",
                ),
            ),
            note(
                f"{p}-n4",
                "Zoledronate duration",
                "Why annual zoledronate is often unnecessary",
                "A single 5-mg IV dose inhibits turnover >5 years with hip BMD still 2% above baseline—clinicians often extend dosing intervals to 2–4 years.",
                ref(
                    "Bisphosphonates",
                    "its inhibition of bone turnover lasts for more than 5 years after a single dose, and hip BMD is still 2% above baseline at that time point.",
                ),
            ),
            note(
                f"{p}-n5",
                "Denosumab rebound",
                "How denosumab discontinuation causes catastrophic vertebral fractures",
                "After long-term denosumab, 15% develop vertebral fractures within months of stopping and 10% have multiple fractures—rebound resorption rises 50% above pretreatment.",
                ref(
                    "Denosumab",
                    "15% of women discontinuing the drug developed vertebral fractures in the following months, and in 10% of discontinuing participants, there were multiple vertebral fractures.",
                ),
            ),
            note(
                f"{p}-n6",
                "Denosumab bridge",
                "How to transition off denosumab safely",
                "Continue denosumab or transition to bisphosphonate—never stop without bridging; oral alendronate after 1 year denosumab prevents bone loss; zoledronate is only partial protection after long-term denosumab.",
                ref(
                    "Denosumab",
                    "After 1 year of denosumab treatment, transitioning to oral alendronate appears to provide good prevention of bone loss.",
                ),
            ),
            note(
                f"{p}-n7",
                "Teriparatide transition",
                "Why teriparatide must be followed by antiresorptive therapy",
                "After 18–24 months teriparatide, hip BMD returns nearly to baseline within a year off drug—convention is immediate transition to bisphosphonate or denosumab.",
                ref(
                    "Case 3",
                    "Bone loss commences once teriparatide is stopped, so neither a drug holiday (Answer B) nor permanent cessation of treatment (Answer C) is appropriate.",
                ),
            ),
            note(
                f"{p}-n8",
                "Romosozumab offset",
                "How romosozumab discontinuation behaves",
                "Stopping romosozumab causes substantial first-year BMD loss and BTM rebound similar to denosumab—transition to denosumab or alendronate maintains gains.",
                ref(
                    "Anabolics",
                    "Its discontinuation is followed by substantial BMD loss over the first year off treatment, and bone resorption markers show a rebound similar to that following denosumab.",
                ),
            ),
            note(
                f"{p}-n9",
                "FLEX half-dose",
                "How FLEX changed alendronate continuation strategy",
                "After 5 years alendronate, half-dose (70 mg every 2 weeks) maintains vertebral fracture prevention without full-dose continuation.",
                ref(
                    "Bisphosphonates",
                    "after 5 years treatment, the dosage of alendronate can be reduced by one-half without loss of efficacy.",
                ),
            ),
            note(
                f"{p}-n10",
                "Patient counseling",
                "Why offset must be discussed at treatment initiation",
                "Patients starting nonbisphosphonate drugs—especially denosumab—must be warned not to discontinue without medical consultation, like beta-blockers in coronary disease.",
                ref(
                    "Anabolics",
                    "the same warning must be provided to those starting nonbisphosphonate osteoporosis drugs, particularly denosumab.",
                ),
            ),
            note(
                f"{p}-n11",
                "Denosumab case",
                "How to manage 5-year denosumab patient wanting to stop",
                "With hip T-score -2.2 and no fractures, either continue denosumab or transition to bisphosphonate—never unbridged cessation.",
                ref("Case 1", "Answer: A or D) Continuation of current therapy or transition to a bisphosphonate"),
            ),
            note(
                f"{p}-n12",
                "Adherence reality",
                "Why unplanned discontinuation is common and dangerous with denosumab",
                "More than half of osteoporosis patients discontinue within 2 years—denosumab stoppers without bridging may fare worse than never having started.",
                ref(
                    "Denosumab",
                    "more than half of patients treated for osteoporosis discontinue their medications within 2 years of initiation.",
                ),
            ),
        ]
    )

    items.extend(
        [
            mcq(
                f"{p}-q1",
                "Case 1 — denosumab 5 years",
                "A woman on denosumab 5 years, fracture-free, hip T-score -2.2, wants to continue therapy. Best recommendation?",
                [
                    "Continue denosumab or transition to bisphosphonate",
                    "1-year drug holiday",
                    "Permanent cessation",
                    "Stop denosumab — protection is lasting",
                ],
                0,
                "Either continuation or bisphosphonate transition is acceptable; unbridged stopping risks rebound vertebral fractures.",
                ref("Case 1", "Answer: A or D) Continuation of current therapy or transition to a bisphosphonate"),
            ),
            mcq(
                f"{p}-q2",
                "Case 1 — denosumab stop harm",
                "Why is permanent denosumab cessation dangerous in Case 1?",
                [
                    "Denosumab causes permanent BMD gain without maintenance",
                    "Rebound bone resorption can cause multiple vertebral fractures",
                    "Denosumab must be taken lifelong by FDA mandate",
                    "Bisphosphonates are contraindicated after denosumab",
                ],
                1,
                "Rapid offset with rebound resorption causes vertebral fractures in up to 15% after long-term use.",
                ref(
                    "Denosumab",
                    "15% of women discontinuing the drug developed vertebral fractures in the following months",
                ),
            ),
            mcq(
                f"{p}-q3",
                "Case 2 — alendronate 5 years",
                "A woman on alendronate 5 years, fracture-free, hip T-score -2.2. Best recommendation?",
                [
                    "Continue full-dose alendronate indefinitely",
                    "1-year or 5-year drug holiday",
                    "Permanent cessation",
                    "Mandatory switch to IV bisphosphonate",
                ],
                1,
                "1- or 5-year drug holiday is preferred; FLEX supports holiday without increased nonvertebral fracture risk.",
                ref("Case 2", "Answer: B or C) A 1-year drug holiday or a 5-year drug holiday"),
            ),
            mcq(
                f"{p}-q4",
                "Case 2 — half-dose option",
                "Alternative to holiday after 5 years alendronate per FLEX?",
                [
                    "Double the alendronate dose",
                    "Reduce to half-dose (70 mg every 2 weeks) without loss of efficacy",
                    "Add teriparatide without stopping alendronate",
                    "Switch to calcitonin",
                ],
                1,
                "FLEX showed half-dose alendronate maintains vertebral fracture prevention after 5 years full dose.",
                ref(
                    "Bisphosphonates",
                    "after 5 years treatment, the dosage of alendronate can be reduced by one-half without loss of efficacy.",
                ),
            ),
            mcq(
                f"{p}-q5",
                "Case 2 — permanent stop",
                "Why is permanent alendronate cessation likely inappropriate in Case 2?",
                [
                    "Alendronate is addictive",
                    "If there was reasonable indication to start, permanent stop risks return of fracture risk",
                    "FDA prohibits stopping alendronate",
                    "Hip T-score -2.2 mandates lifelong full-dose therapy",
                ],
                1,
                "If initial treatment was justified, permanent cessation without reassessment is usually inappropriate.",
                ref(
                    "Case 2",
                    "If there was a reasonable indication for the initiation of alendronate in the first place, then permanent cessation of treatment (Answer D) is likely to be inappropriate.",
                ),
            ),
            mcq(
                f"{p}-q6",
                "Case 3 — teriparatide 2 years",
                "A woman completed 2 years teriparatide, fracture-free, hip T-score -2.2. Best next step?",
                [
                    "Continue teriparatide",
                    "1-year drug holiday",
                    "Permanent cessation without follow-on",
                    "Transition to bisphosphonate or denosumab",
                ],
                3,
                "Teriparatide is limited to 18–24 months; BMD loss follows cessation unless antiresorptive follow-on is given.",
                ref("Case 3", "Answer: D) Transition to a bisphosphonate or denosumab"),
            ),
            mcq(
                f"{p}-q7",
                "Teriparatide duration",
                "Why can teriparatide not be continued beyond 2 years?",
                [
                    "Human osteosarcoma signal in rat studies limits duration to 18–24 months",
                    "It loses all effect after 6 months",
                    "FDA bans all anabolic agents after 1 year",
                    "BMD always decreases while on teriparatide",
                ],
                0,
                "High-dose long-term teriparatide increased osteosarcoma in rats—clinical use capped at 18–24 months though human signal absent.",
                ref(
                    "Case 3",
                    "the use of teriparatide is restricted to 18 to 24 months across various jurisdictions.",
                ),
            ),
            mcq(
                f"{p}-q8",
                "Risedronate offset",
                "How quickly does risedronate's effect offset after stopping?",
                [
                    "More than 5 years",
                    "Within 12 months",
                    "Never — permanent binding",
                    "24 hours",
                ],
                1,
                "Risedronate turnover suppression offsets within 12 months—faster than alendronate.",
                ref(
                    "Bisphosphonates",
                    "Studies of risedronate demonstrate a more rapid offset of bone turnover suppression, within 12 months of drug discontinuation.",
                ),
            ),
            mcq(
                f"{p}-q9",
                "Zoledronate persistence",
                "After a single 5-mg zoledronate infusion, how long does turnover suppression last?",
                [
                    "6 weeks",
                    "6 months",
                    "More than 5 years",
                    "24 hours",
                ],
                2,
                "Zoledronate has highest bone affinity—single dose suppresses turnover >5 years.",
                ref(
                    "Bisphosphonates",
                    "its inhibition of bone turnover lasts for more than 5 years after a single dose",
                ),
            ),
            mcq(
                f"{p}-q10",
                "Denosumab rebound magnitude",
                "After missing one denosumab dose, bone resorption can rise to:",
                [
                    "Baseline levels",
                    "50% above pretreatment levels",
                    "Zero — permanent suppression",
                    "Levels seen only with teriparatide",
                ],
                1,
                "Phase 2 data show dramatic offset with resorption ~50% above pretreatment within months of missed dose.",
                ref(
                    "Denosumab",
                    "bone resorption rising to about 50% above pretreatment levels within months of drug discontinuation.",
                ),
            ),
            mcq(
                f"{p}-q11",
                "Denosumab bridge agent",
                "After 1 year denosumab, which transition best prevents bone loss?",
                [
                    "No therapy",
                    "Oral alendronate",
                    "Calcium alone",
                    "Teriparatide without antiresorptive follow-on",
                ],
                1,
                "Transitioning to oral alendronate after 1 year denosumab provides good bone loss prevention.",
                ref(
                    "Denosumab",
                    "After 1 year of denosumab treatment, transitioning to oral alendronate appears to provide good prevention of bone loss.",
                ),
            ),
            mcq(
                f"{p}-q12",
                "Romosozumab follow-on",
                "After completing 12 months romosozumab, necessary next step?",
                [
                    "No further therapy",
                    "Antiresorptive therapy to maintain BMD gains",
                    "Repeat romosozumab indefinitely",
                    "Stop all bone medications permanently",
                ],
                1,
                "Substantial BMD loss follows romosozumab cessation unless denosumab or alendronate follow-on is given.",
                ref(
                    "Anabolics",
                    "if patients transition to denosumab or to alendronate, positive changes in BMD are observed and fracture rates remain low.",
                ),
            ),
            mcq(
                f"{p}-q13",
                "Counseling",
                "When should drug offset characteristics be discussed with osteoporosis patients?",
                [
                    "Only at time of discontinuation",
                    "At treatment initiation — especially for denosumab",
                    "Never — too confusing for patients",
                    "Only after first fracture on therapy",
                ],
                1,
                "Offset counseling at initiation allows informed therapeutic strategy—critical for denosumab.",
                ref(
                    "Anabolics",
                    "it is critically important to counsel patients about the offset characteristics of osteoporosis drugs when they are first being prescribed",
                ),
            ),
        ]
    )

    items.extend(
        [
            tf(
                f"{p}-tf1",
                "Alendronate holiday",
                "A 1-year drug holiday after 5 years of alendronate is often appropriate for risedronate and 12–24 months for alendronate per main conclusions.",
                True,
                "Suggested discontinuation: 6 months holiday for risedronate, 12–24 months for alendronate when holiday is indicated.",
                ref(
                    "Main Conclusions",
                    "If a drug holiday is judged to be indicated, 6 months is usually appropriate for risedronate and 12 to 24 months for alendronate.",
                ),
            ),
            tf(
                f"{p}-tf2",
                "Denosumab holiday",
                "A drug holiday is appropriate after long-term denosumab if BMD has improved.",
                False,
                "Denosumab requires continuous therapy or bridged transition—no drug holiday.",
                ref("Case 1", "Cessation of therapy, whether temporary or permanent (Answers B and C), would expose her to risk of rebound vertebral fractures."),
            ),
            tf(
                f"{p}-tf3",
                "Teriparatide stop",
                "Bone density gains persist indefinitely after stopping teriparatide without follow-on therapy.",
                False,
                "Hip BMD returns nearly to baseline within a year; antiresorptive follow-on is required.",
                ref(
                    "Anabolics",
                    "One year after conclusion of a 1-year treatment course, spine BMD is still several percent above baseline, but hip BMD is only about 0.5% above baseline.",
                ),
            ),
            tf(
                f"{p}-tf4",
                "Zoledronate annual dosing",
                "Annual zoledronate is necessary in most patients because effects last only 6 months.",
                False,
                "Single dose suppresses turnover >5 years—annual dosing often unnecessary.",
                ref(
                    "Main Conclusions",
                    "Zoledronate inhibits bone resorption for more than 5 years, so annual dosing is unnecessary in most circumstances.",
                ),
            ),
            tf(
                f"{p}-tf5",
                "Denosumab fractures",
                "Up to 15% of patients stopping long-term denosumab experience vertebral fractures.",
                True,
                "FREEDOM extension documented this rebound fracture risk.",
                ref(
                    "Denosumab",
                    "15% of women discontinuing the drug developed vertebral fractures in the following months",
                ),
            ),
            tf(
                f"{p}-tf6",
                "FLEX vertebral",
                "FLEX showed continuing alendronate after 5 years still reduces clinical vertebral fractures by about half.",
                True,
                "Continued therapy reduced clinical vertebral fractures ~50% vs placebo in FLEX.",
                ref(
                    "Bisphosphonates",
                    "clinical vertebral fractures were reduced by about one-half in those who continued to take alendronate.",
                ),
            ),
            tf(
                f"{p}-tf7",
                "Romosozumab rebound",
                "Romosozumab discontinuation causes BTM rebound similar to denosumab.",
                True,
                "Resorption markers rebound after romosozumab cessation unless antiresorptive follow-on given.",
                ref(
                    "Anabolics",
                    "bone resorption markers show a rebound similar to that following denosumab.",
                ),
            ),
            tf(
                f"{p}-tf8",
                "Zoledronate after denosumab",
                "After long-term denosumab, zoledronate provides complete protection against bone loss.",
                False,
                "Zoledronate provides only partial protection after prolonged denosumab.",
                ref(
                    "Denosumab",
                    "after long-term denosumab treatment, zoledronate is only partially effective in preventing subsequent bone loss.",
                ),
            ),
        ]
    )

    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Denosumab",
                "Assertion: Denosumab must not be stopped without transition to another antiresorptive.",
                "Reason: Bone resorption rises to 50% above pretreatment after missed dose.",
                0,
                "Both true—rapid antibody clearance drives rebound resorption and vertebral fracture risk.",
                ref(
                    "Denosumab",
                    "bone resorption rising to about 50% above pretreatment levels within months of drug discontinuation.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Alendronate holiday",
                "Assertion: A 5-year alendronate holiday does not increase nonvertebral fracture risk per FLEX.",
                "Reason: Bisphosphonates bind bone mineral for years after stopping.",
                1,
                "Both true but R explains persistence mechanism rather than specifically the nonvertebral fracture finding.",
                ref(
                    "Case 2",
                    "a 5-year drug holiday will not increase her risk of nonvertebral fractures",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Teriparatide",
                "Assertion: Teriparatide should be followed by bisphosphonate or denosumab.",
                "Reason: BMD gains are lost within months after anabolic cessation.",
                0,
                "Both true—anabolic benefit must be locked in with antiresorptive follow-on.",
                ref(
                    "Main Conclusions",
                    "it is important to lock in the BMD gains with the use of an antiresorptive agent (bisphosphonate or denosumab) at the time of anabolic withdrawal.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Zoledronate duration",
                "Assertion: Annual zoledronate is unnecessary in most patients.",
                "Reason: A single 5-mg dose suppresses turnover for more than 5 years.",
                0,
                "Both true—prolonged skeletal retention obviates yearly dosing in many patients.",
                ref(
                    "Main Conclusions",
                    "Zoledronate inhibits bone resorption for more than 5 years, so annual dosing is unnecessary in most circumstances.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Risedronate",
                "Assertion: Risedronate offset occurs faster than alendronate.",
                "Reason: Risedronate has lower affinity for bone mineral than zoledronate.",
                1,
                "Both true but affinity comparison to zoledronate rather than alendronate is the stated mechanism in text.",
                ref(
                    "Bisphosphonates",
                    "Thus, zoledronate has the longest duration of action, whereas the effects of risedronate and ibandronate are more transient.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Denosumab continue",
                "Assertion: Continuing denosumab is acceptable for a 5-year fracture-free patient with hip T-score -2.2.",
                "Reason: Hip T-score above -2.5 always mandates stopping therapy.",
                2,
                "A is acceptable per Case 1; R is false—T-score alone does not mandate stopping.",
                ref("Case 1", "Either continuing current therapy (Answer A) or transitioning to a bisphosphonate (Answer D) would be acceptable answers."),
            ),
            ar(
                f"{p}-ar7",
                "Romosozumab",
                "Assertion: Romosozumab cessation requires antiresorptive follow-on.",
                "Reason: Romosozumab causes substantial BMD loss in the first year off treatment.",
                0,
                "Both true—rebound loss mirrors denosumab unless bridged to antiresorptive.",
                ref(
                    "Anabolics",
                    "Its discontinuation is followed by substantial BMD loss over the first year off treatment",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Counseling",
                "Assertion: Patients starting denosumab should be counseled about offset before discontinuing.",
                "Reason: More than half of osteoporosis patients discontinue therapy within 2 years.",
                0,
                "Both true—high real-world discontinuation rates make upfront offset counseling essential.",
                ref(
                    "Denosumab",
                    "more than half of patients treated for osteoporosis discontinue their medications within 2 years of initiation.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 2021,
        "chapterNo": "15",
        "title": "Stopping Bone-Ac Medications",
        "section": "Endocrine Self-Assessment Program 2021 (Endo 2021)",
        "authors": "Ian R. Reid, MD",
        "sourceFile": "williams_2024_chapters/endo2021_chapter_15_Stopping_BoneAc_Medications.md",
        "items": items,
    }


MODULES = {
    "endo2021_chapter_09_BONE_AND_MINERAL_METABOLISM.json": build_chapter_09,
    "endo2021_chapter_10_Evaluation_of_the_Patient_With_Hypophosphatemia.json": build_chapter_10,
    "endo2021_chapter_11_Challenging_Case_and_Mineral_Disease.json": build_chapter_11,
    "endo2021_chapter_12_Bone_Turnover_Markers_in_the_Management_of_Osteoporosis.json": build_chapter_12,
    "endo2021_chapter_13_Using_the_Best_Available_Evidence_to_Personalize_Osteoporosis_Treatment.json": build_chapter_13,
    "endo2021_chapter_14_Is_There_an_Ideal_Vitamin_D_Level_and_Dosage_for_All_Circumstances.json": build_chapter_14,
    "endo2021_chapter_15_Stopping_BoneAc_Medications.json": build_chapter_15,
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
