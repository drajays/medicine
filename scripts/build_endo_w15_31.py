#!/usr/bin/env python3
"""Generate Williams 15e module w15-31 — Kidney Stones."""
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
OUT_NAME = "w15-31_Kidney_Stones.json"


def build() -> dict:
    p = "w15-31"
    items: list[dict] = []

    # --- Notes (26; ≥14 Why/How for ≥54%) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why supersaturation is the fundamental stone mechanism",
                "Stones grow when free ion activity exceeds solubility for a given constituent—clinical prevention targets volume, pH, inhibitors, and ion excretion to keep urine undersaturated.",
                ref(
                    "KEY POINTS",
                    "Kidney stones form when urine becomes supersaturated with respect to the specific components of the stone's constituents.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How genetic hypercalciuria drives calcium stones",
                "Monogenic and polygenic disorders altering gut, bone, or renal calcium handling—or CaSR signaling—raise urinary calcium and supersaturation even when serum calcium is normal.",
                ref(
                    "KEY POINTS",
                    "A multitude of monogenic and polygenic hereditary disorders that result in changes of either calcium handling at the level of kidney, bone, and gut, or calcium sensing at the calcium-sensing receptor on the parathyroid glands and renal tubular cells can lead to hypercalciuria, urine supersaturation, and stone formation.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why every stone former deserves a basic evaluation",
                "Even a first stone may unmask systemic disease (PHPT, RTA, cystinuria, PHO); NIH consensus panels mandate at least basic metabolic workup for all patients.",
                ref(
                    "KEY POINTS",
                    "All patients, even those with a single stone, should undergo at least a basic evaluation to rule out a systemic etiology of stone formation.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "How increased fluid intake prevents recurrence",
                "Raising urine volume dilutes lithogenic solutes and is among the highest-yield, lowest-risk interventions—target ~2–2.5 L daily output.",
                ref(
                    "KEY POINTS",
                    "Increasing fluid intake is a simple measure that has considerable impact on reducing stone growth and new stone formation.",
                ),
            ),
            note(
                f"{p}-n5",
                "Epidemiology of Stone Formation",
                "Why calcium stones dominate in the United States",
                "Geography and genetics shift stone composition: >70% of US stones are calcium-based, whereas uric acid stones predominate in Mediterranean/Middle Eastern cohorts.",
                ref(
                    "Epidemiology of Stone Formation",
                    "By contrast, more than 70% of stones formed in the United States are calcium based.",
                ),
            ),
            note(
                f"{p}-n6",
                "Physiology",
                "How urinary pH shifts stone solubility",
                "Low pH favors uric acid supersaturation while reducing calcium/phosphate activity; citrate chelates calcium and lowers free ion activity of stone-forming ions.",
                ref(
                    "Physiology",
                    "A low urinary pH increases the free ion activity of uric acid ions but decreases the activity of calcium and phosphate ions. Citrate combines with calcium ions to form soluble complexes and will decrease the free ion activity of unbound citrate and calcium.",
                ),
            ),
            note(
                f"{p}-n7",
                "Physiology",
                "Why Randall plaques anchor calcium oxalate stones",
                "Interstitial apatite at the papillary tip provides a nidus for heterogeneous nucleation—calcium oxalate adheres to plaque rather than forming de novo in dilute urine.",
                ref(
                    "Physiology",
                    "This anchoring of crystals occurs at the renal papillae, over areas of interstitial calcium phosphate present in the form of apatite termed Randall plaques",
                ),
            ),
            note(
                f"{p}-n8",
                "Physiology",
                "How crystallization inhibitors protect against stones",
                "Uropontin, pyrophosphate, citrate, and nephrocalcin inhibit calcium crystallization—deficiency or low activity explains stones despite modest supersaturation on mass excretion alone.",
                ref(
                    "Physiology",
                    "Uropontin, pyrophosphate, citrate, and nephrocalcin are endogenously produced substances that have been shown to inhibit calcium crystallization.",
                ),
            ),
            note(
                f"{p}-n9",
                "Diet",
                "Why dietary calcium restriction is discouraged",
                "Low-calcium diets increase intestinal oxalate absorption and stone recurrence while risking bone demineralization—normal dietary calcium binds gut oxalate.",
                ref(
                    "Diet",
                    "Dietary calcium restriction should be strongly discouraged because it not only increases risk of stone formation but also engenders a significant risk of bone demineralization and development of osteoporosis.",
                ),
            ),
            note(
                f"{p}-n10",
                "Diet",
                "How sodium restriction lowers hypercalciuria",
                "Urinary calcium tracks sodium excretion; cap sodium at ~3000 mg/day to reduce calciuria and calcium-containing stone supersaturation—especially in IH.",
                ref(
                    "Diet",
                    "Patients are counseled to limit their daily sodium intake to a maximum of 3000 mg (~130 mEq) to reduce hypercalciuria.",
                ),
            ),
            note(
                f"{p}-n11",
                "Diet",
                "Why calcium supplements differ from dietary calcium",
                "Dietary calcium lowers stone risk, but supplemental calcium (often with vitamin D) increases stones in postmenopausal women—counsel food-based intake.",
                ref(
                    "Diet",
                    "Note that although dietary calcium intake has been associated with a reduced incidence of kidney stones, calcium intake in the form of supplements can exacerbate stone formation in older women.",
                ),
            ),
            note(
                f"{p}-n12",
                "Diet",
                "How the DASH diet reduces stone risk",
                "High potassium/calcium, low sodium, and moderate protein—despite oxalate-rich foods—lowers stone incidence compared with less DASH-like eating patterns.",
                ref(
                    "Diet",
                    "Indeed, the Dietary Approaches to Stop Hypertension (DASH) diet appears to reduce the risk of forming a kidney stone.",
                ),
            ),
            note(
                f"{p}-n13",
                "Pathogenesis of Idiopathic Hypercalciuria",
                "Why idiopathic hypercalciuria is the common calcium-stone driver",
                "IH is normocalcemic, familial, likely polygenic, and the leading metabolic cause of calcium stones—do not subtype into absorptive vs renal leak for therapy.",
                ref(
                    "Pathogenesis of Idiopathic Hypercalciuria",
                    "Idiopathic hypercalciuria (IH) is defined as excessive urinary calcium excretion in the setting of normocalcemia and the absence of secondary causes of hypercalciuria. IH is the most common cause of calcium-containing kidney stones.",
                ),
            ),
            note(
                f"{p}-n14",
                "Hypercalciuria",
                "How thiazides plus sodium restriction treat hypercalciuria",
                "Thiazides reduce urinary calcium, but efficacy requires dietary sodium restriction because calciuria parallels natriuresis—chlorthalidone 25–50 mg daily is preferred.",
                ref(
                    "Hypercalciuria",
                    "To maximize the efficacy of thiazides, patients must consume a sodium-restricted diet. Urinary calcium excretion parallels sodium excretion",
                ),
            ),
            note(
                f"{p}-n15",
                "Hypercalciuria",
                "Why potassium citrate accompanies thiazide therapy",
                "Thiazide-induced hypokalemia lowers urinary citrate (hypocitraturia)—replete with potassium citrate rather than chloride when citrate is needed.",
                ref(
                    "Hypercalciuria",
                    "Hypokalemia can result not only in cardiac and neuromuscular problems but also in hypocrituria—another risk factor for stone formation. The supplement of choice is potassium with a base, such as citrate or bicarbonate, as the accompanying anion.",
                ),
            ),
            note(
                f"{p}-n16",
                "Enteric Oxaluria",
                "How malabsorption causes enteric hyperoxaluria",
                "Unabsorbed fat binds luminal calcium, leaving free oxalate for colonic absorption—Crohn, sprue, bypass, and pancreatitis are classic settings (60–100 mg oxalate/day).",
                ref(
                    "Enteric Oxaluria",
                    "In these disorders, malabsorbed fatty acids bind calcium in the intestinal lumen, making more \"free\" oxalate available for absorption in the colon.",
                ),
            ),
            note(
                f"{p}-n17",
                "Primary Hyperoxaluria",
                "Why lumasiran changes type 1 primary hyperoxaluria",
                "Lumasiran silences glycolate oxidase upstream of defective AGT, markedly lowering plasma and urine oxalate—early diagnosis before systemic oxalosis is critical.",
                ref(
                    "Primary Hyperoxaluria",
                    "Lumasiran in a small interfering RNA has now been approved for treatment for type 1 primary hyperoxaluria.",
                ),
            ),
            note(
                f"{p}-n18",
                "Uric Acid Stones",
                "How low urine pH causes uric acid stones",
                "Undissociated uric acid precipitates at pH <6 in most stone formers; insulin resistance impairs ammoniagenesis and drives acidic urine even without hyperuricosuria.",
                ref(
                    "Uric Acid Stones",
                    "In four studies, every patient with uric acid stones had a urine pH less than 6.0.",
                ),
            ),
            note(
                f"{p}-n19",
                "Uric Acid Stones",
                "Why potassium citrate alkalinizes uric acid stone therapy",
                "Raise urine pH to ~6.5–7.0 to dissolve uric acid crystals, but keep pH <7.0 to avoid calcium phosphate stones—monitor with nitrazine paper.",
                ref(
                    "Uric Acid Stones",
                    "Ideally, the urinary pH should be elevated to approximately 6.5 to 7.0, a level that can dissolve existing crystals and stones. However, care should be taken to prevent the urine pH from rising above 7.0 to minimize the risk of calcium phosphate lithiasis.",
                ),
            ),
            note(
                f"{p}-n20",
                "Distal Renal Tubular Acidosis",
                "How dRTA favors calcium phosphate stones",
                "Defective distal acidification → alkaline urine, severe hypocitraturia, and hypercalciuria—ideal milieu for calcium phosphate precipitation and nephrocalcinosis.",
                ref(
                    "Distal Renal Tubular Acidosis",
                    "The increased filtered load of calcium and phosphate, along with the elevated urine pH and hypocitraturia, results in favorable conditions for calcium phosphate stone formation.",
                ),
            ),
            note(
                f"{p}-n21",
                "Struvite Stones",
                "Why E. coli is not implicated in struvite stones",
                "Struvite requires urease-producing organisms (Proteus, Klebsiella, etc.) to generate ammonium and alkaline urine—E. coli does not produce urease.",
                ref(
                    "Struvite Stones",
                    "Escherichia coli, despite its frequent role as a urinary tract pathogen, has not been shown to produce urease and thus is not implicated in the genesis of struvite stones.",
                ),
            ),
            note(
                f"{p}-n22",
                "Cystine Stones",
                "How cystine solubility limits drive cystinuria stones",
                "Autosomal recessive dibasic aminoaciduria raises cystine excretion, but stones form because cystine solubility is only ~250–300 mg/L—hexagonal crystals on urinalysis are a clue.",
                ref(
                    "Cystine Stones",
                    "The genetic defect would probably go unnoticed were it not for the low solubility of cystine of approximately 300 mg/L.",
                ),
            ),
            note(
                f"{p}-n23",
                "Therapy for Struvite Stones",
                "Why complete surgical removal is mandatory for struvite",
                "Antibiotics alone fail if stone material harbors urease-producing bacteria—aggressive PNL/ESWL with long-term suppression is required to prevent \"stone cancer\" recurrence.",
                ref(
                    "Therapy for Struvite Stones",
                    "Appropriate antibiotic therapy is essential but must be combined with long-term bacterial suppression and complete surgical or medical stone removal.",
                ),
            ),
            note(
                f"{p}-n24",
                "The Complete Evaluation",
                "How Table 31.1 targets guide 24-hour urine therapy",
                "Volume >2–2.5 L, calcium <250–300 mg, oxalate <40 mg, sodium <3000 mg, citrate >320 mg, and supersaturation indices define adequate prevention.",
                ref(
                    "The Complete Evaluation",
                    "The complete evaluation comprises the entire basic examination as well as a 24-hour urine collection to determine volume and levels of calcium, oxalate, citrate, sodium, urate, phosphorus, creatinine, and the urinary supersaturation with respect to the common solid phase components",
                ),
            ),
            note(
                f"{p}-n25",
                "Physiology",
                "Why supersaturation outperforms ion excretion alone",
                "Mass excretion per 24 h misses pH and complexation effects—laboratory supersaturation calculations better estimate lithogenic risk than calcium or oxalate milligrams alone.",
                ref(
                    "Physiology",
                    "It is clear, however, that the lithogenic potential of urine is better determined by the degree of supersaturation.",
                ),
            ),
            note(
                f"{p}-n26",
                "Medical Expulsive Therapy",
                "How tamsulosin facilitates ureteral stone passage",
                "α-Blockers reduce ureteral spasm and enhance peristalsis for stones <10 mm when pain is controlled and no infection/obstruction—tamsulosin 0.4 mg daily up to 4 weeks.",
                ref(
                    "Medical Expulsive Therapy",
                    "α-Blockers such as tamsulosin (0.4 mg once daily for up to 4 weeks) have been shown to facilitate stone passage.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Diet",
                "A 42-year-old man with recurrent calcium oxalate stones asks whether he should stop milk and cheese. His 24-hour urine shows hypercalciuria and mild hyperoxaluria. What dietary advice is best supported by evidence?",
                [
                    "Strict low-calcium diet (<500 mg/day)",
                    "Normal dietary calcium with sodium restriction and adequate fluids",
                    "High-dose calcium carbonate supplements with meals",
                    "High animal protein to bind oxalate",
                ],
                1,
                "Low-calcium diets worsen oxalate absorption and recurrence; normal calcium with low sodium and fluids lowers supersaturation per Borghi and cohort data.",
                ref(
                    "Diet",
                    "The group of men on a normal-calcium, low-sodium, and low-animal protein diet had a significantly lower recurrence of nephrolithiasis and a greater reduction in oxalate excretion and calcium oxalate supersaturation compared with the men on the low-calcium diet.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Struvite Stones",
                "A woman with a staghorn calculus has urine pH 7.2, pyuria, and culture growing Escherichia coli only. Which statement is most accurate?",
                [
                    "E. coli urease production explains the staghorn calculus",
                    "Struvite is unlikely from E. coli alone; seek urease-producing organisms",
                    "Oral antibiotics alone will eradicate the stone",
                    "ESWL is always first-line for infected staghorn stones",
                ],
                1,
                "E. coli does not produce urease; struvite requires urease-positive bacteria—request specific urease testing even with low colony counts.",
                ref(
                    "Struvite Stones",
                    "Escherichia coli, despite its frequent role as a urinary tract pathogen, has not been shown to produce urease and thus is not implicated in the genesis of struvite stones.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Hypercalciuria",
                "A hypercalciuric stone former is started on chlorthalidone 25 mg daily but continues a high-sodium diet. Repeat 24-hour urine shows unchanged hypercalciuria. Best next step?",
                [
                    "Switch to loop diuretic for greater calciuresis",
                    "Intensify dietary sodium restriction and recheck urine sodium",
                    "Add triamterene as first-line potassium-sparing agent",
                    "Stop thiazide because it is ineffective for IH",
                ],
                1,
                "Thiazide efficacy depends on sodium restriction—urinary calcium parallels sodium; triamterene can precipitate into stones and is avoided.",
                ref(
                    "Hypercalciuria",
                    "Urinary calcium excretion parallels sodium excretion (Fig. 31.6), and reducing sodium consumption is essential to reducing hypercalciuria.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Medications",
                "A patient on hydrochlorothiazide and amiloride for hypertension passes a yellow, faceted stone. Stone analysis is pending. Which medication is a known cause of drug-precipitated stones?",
                [
                    "Amiloride",
                    "Triamterene",
                    "Metoprolol",
                    "Lisinopril",
                ],
                1,
                "Triamterene can precipitate into stones/crystals; it is generally avoided as a potassium-sparing agent in stone formers.",
                ref(
                    "Medications",
                    "Certain crystals or stones can consist completely of precipitated medication. Such medications include intravenously administered acyclovir, triamterene, indinavir, and various sulfonamides, such as sulfidazine.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Epidemiology of Stone Formation",
                "A urologist reviews stone composition registries in the United States. Which distribution is most accurate?",
                [
                    "Uric acid stones account for >50% of US stones",
                    "Calcium-based stones account for >70% of US stones",
                    "Cystine stones account for ~15% of US stones",
                    "Struvite is the most common stone type in men",
                ],
                1,
                "US epidemiology: >70% calcium-based; uric acid <10%; cystine ~2%; struvite 10–25%.",
                ref(
                    "Epidemiology of Stone Formation",
                    "By contrast, more than 70% of stones formed in the United States are calcium based.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Physiology",
                "A researcher compares homogeneous vs heterogeneous nucleation in vitro. Which in vivo pattern is most likely?",
                [
                    "Homogeneous nucleation at lower supersaturation",
                    "Heterogeneous nucleation on Randall plaque or cells at lower supersaturation",
                    "Stones form only when urine is undersaturated",
                    "Citrate increases free calcium ion activity",
                ],
                1,
                "Heterogeneous nucleation on dissimilar surfaces (e.g., apatite plaque) dominates because crystals form at lower supersaturation than homogeneous clustering.",
                ref(
                    "Physiology",
                    "In vivo, this type of nucleation is more common than homogeneous nucleation because crystals form at a lower level of supersaturation in the presence of a solid phase.",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Pathogenesis of Idiopathic Hypercalciuria",
                "A 35-year-old normocalcemic man has IH and low bone density. His physician considers a low-calcium diet because of 'absorptive hypercalciuria.' What is the best approach?",
                [
                    "Low-calcium diet is first-line for absorptive IH",
                    "Avoid low-calcium diet; use nonspecific measures and thiazide if needed",
                    "High-dose vitamin D to suppress PTH",
                    "Parathyroidectomy for normocalcemic IH",
                ],
                1,
                "Subtype distinction (absorptive vs renal leak) is obsolete; low-calcium diets worsen stones and bone density—thiazides with sodium restriction are used for persistent hypercalciuria.",
                ref(
                    "Pathogenesis of Idiopathic Hypercalciuria",
                    "From a therapeutic standpoint, these findings have rendered obsolete both the need to clinically distinguish IH mechanisms in humans and also the prescription of a low-calcium diet in any of these patients.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Enteric Oxaluria",
                "A 28-year-old woman with Crohn disease and ileal resection has urinary oxalate 85 mg/day and recurrent calcium oxalate stones. Mechanism?",
                [
                    "Excess dietary spinach alone",
                    "Fat malabsorption binds luminal calcium, increasing free oxalate absorption",
                    "Primary AGT deficiency",
                    "Excess uric acid epitaxy only",
                ],
                1,
                "Enteric hyperoxaluria (60–100 mg/day) arises when fatty acids bind intestinal calcium, leaving oxalate available for colonic uptake.",
                ref(
                    "Enteric Oxaluria",
                    "In these disorders, malabsorbed fatty acids bind calcium in the intestinal lumen, making more \"free\" oxalate available for absorption in the colon.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Primary Hyperoxaluria",
                "A child has nephrocalcinosis, urine oxalate 220 mg/day, and AGXT mutation. Standard therapy is insufficient. Which targeted therapy is approved for type 1 PHO?",
                [
                    "Pyridoxine alone in all PHO types",
                    "Lumasiran",
                    "Allopurinol 300 mg daily",
                    "Acetazolamide for alkalinization",
                ],
                1,
                "Lumasiran (siRNA against glycolate oxidase) is approved for type 1 PHO, lowering oxalate production upstream of defective AGT.",
                ref(
                    "Primary Hyperoxaluria",
                    "Lumasiran reduces the levels of glycolate oxidase upstream of the abnormal hepatic enzyme AGT, resulting in less oxalate production.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Uric Acid Stones",
                "A 52-year-old obese man with metabolic syndrome passes a radiolucent 8 mm stone. Urine pH is 5.1, uric acid excretion normal. Best initial preventive therapy?",
                [
                    "Allopurinol 300 mg daily",
                    "Potassium citrate to raise urine pH toward 6.5–7.0",
                    "Low-fluid diet to concentrate urine",
                    "Calcium restriction",
                ],
                1,
                "Low urine pH (<6) is the dominant cause of uric acid stones in insulin-resistant patients—alkalinization with potassium citrate dissolves uric acid without necessarily needing allopurinol.",
                ref(
                    "Uric Acid Stones",
                    "A low urine pH is the major cause of uric acid nephropathy.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Distal Renal Tubular Acidosis",
                "A teenager has non–anion-gap acidosis, urine pH 6.8, nephrocalcinosis, and calcium phosphate stones. First-line medical therapy?",
                [
                    "Thiazide diuretic alone",
                    "Potassium citrate to correct acidosis and hypocitraturia",
                    "High animal protein diet",
                    "Sodium bicarbonate only without citrate monitoring",
                ],
                1,
                "dRTA causes alkaline urine, hypocitraturia, and hypercalciuria—potassium citrate (1–3 mEq/kg/day base) treats acidosis and raises citrate.",
                ref(
                    "Distal Renal Tubular Acidosis",
                    "Therapy consists of potassium citrate or potassium bicarbonate supplementation to treat both the metabolic acidosis and hypocitraturia.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Cystine Stones",
                "A 22-year-old man excretes 750 mg cystine/day. Fluids and alkalinization are insufficient. Which chelating agent is used?",
                [
                    "Allopurinol",
                    "Tiopronin or D-penicillamine",
                    "Chlorthalidone",
                    "Acetazolamide alone",
                ],
                1,
                "CBTDs (tiopronin, D-penicillamine) cleave cystine disulfide bonds to form more soluble cysteine-drug complexes when fluids/alkalinization fail.",
                ref(
                    "Cystine Stones",
                    "CBTDs such as tiopronin and D-penicillamine have sulfhydryl groups that weaken this disulfide bond, leading to a more soluble cysteine-drug compound.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Therapy for Struvite Stones",
                "A 60-year-old woman has a 3 cm infected staghorn struvite calculus. Most appropriate urologic approach?",
                [
                    "Antibiotics alone for 6 months",
                    "PNL or combined PNL/ESWL for complete removal plus antibiotics",
                    "Observation if asymptomatic",
                    "Oral potassium citrate as definitive therapy",
                ],
                1,
                "Large infected struvite stones require aggressive complete removal—PNL preferred for >2 cm/staghorn—with prolonged antibiotic suppression.",
                ref(
                    "Therapy for Struvite Stones",
                    "PNL is more effective in removing large (>2 cm) or staghorn calculi, as well as stones that do not fragment well with lithotripsy. Large, infected stones, such as struvite stones, in which complete removal is desired, are best treated with PNL.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Metabolic Evaluation of Stone Formers",
                "A 40-year-old man passes his first calcium oxalate stone. According to NIH consensus, what evaluation is warranted?",
                [
                    "No workup until a second stone",
                    "At least a basic evaluation for systemic etiology",
                    "Immediate open nephrolithotomy",
                    "Genetic panel for all stone formers only",
                ],
                1,
                "All patients—even with a single stone—should receive basic evaluation; complete metabolic workup is reserved for higher-risk groups.",
                ref(
                    "Metabolic Evaluation of Stone Formers",
                    "These panels determined that all patients, even those with a single stone, should undergo at least a basic evaluation to rule out a systemic etiologic mechanism.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "The Complete Evaluation",
                "A woman's 24-hour urine shows volume 1.6 L, sodium 3400 mg, citrate 250 mg, calcium 280 mg. Which target from Table 31.1 is NOT yet met?",
                [
                    "Oxalate <40 mg (she has 35 mg)",
                    "Volume >2.0–2.5 L and citrate >320 mg",
                    "Uric acid <750 mg in women",
                    "Creatinine ~10 mg/kg for collection adequacy",
                ],
                1,
                "Table 31.1 targets volume >2–2.5 L and citrate >320 mg—her low volume and hypocitraturia need fluid and citrate intervention.",
                ref(
                    "Hypocitraturia",
                    "Large amounts may be required (30–75 mEq/day) in divided doses to raise the urinary citrate concentration to more than 320 mg/day.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Medical Expulsive Therapy",
                "A 6 mm distal ureteral stone in a stable, noninfected patient causes controlled pain and normal renal function. Best adjunct to analgesia?",
                [
                    "Immediate PNL",
                    "Tamsulosin 0.4 mg daily for up to 4 weeks with follow-up imaging",
                    "High-dose furosemide",
                    "Prophylactic broad-spectrum antibiotics for 3 months",
                ],
                1,
                "MET with α-blockers (tamsulosin) is appropriate for ureteral stones <10 mm when obstruction/infection are absent and pain is manageable.",
                ref(
                    "Medical Expulsive Therapy",
                    "Medical expulsive therapy may be utilized with ureteral stones that are less than 10 mm in diameter for up to 6 weeks if kidney function is normal, there is no evidence of infection or significant obstruction, and pain can be controlled.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Surgical Treatment",
                "A 1.2 cm proximal ureteral calcium oxalate stone fails MET. The stone is radiopaque and patient is not pregnant. Preferred modality?",
                [
                    "Open pyelolithotomy first-line",
                    "ESWL or URS depending on location/expertise",
                    "Observation only",
                    "ESWL is contraindicated for all ureteral stones",
                ],
                1,
                "ESWL suits many kidney/proximal ureteral stones <~15 mm; URS excels for distal ureter—choice depends on location, size, and expertise.",
                ref(
                    "Surgical Treatment",
                    "Kidney stones less than approximately 15 mm, proximal ureteral stones, upper and middle pole kidney stones, and those not composed of cystine or calcium oxalate monohydrate respond best to ESWL.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "Surgical Treatment",
                "A 4 cm infected staghorn struvite stone needs maximal stone-free rates. Best procedure?",
                [
                    "ESWL alone",
                    "Percutaneous nephrolithotomy (PNL)",
                    "Extracorporeal shock wave only with MET",
                    "Ureteroscopy for all staghorn stones",
                ],
                1,
                "PNL is preferred for large (>2 cm) and staghorn calculi, especially infected struvite where complete removal is goal.",
                ref(
                    "Surgical Treatment",
                    "PNL is more effective in removing large (>2 cm) or staghorn calculi, as well as stones that do not fragment well with lithotripsy.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Hypercalciuria",
                "Which thiazide is favored for hypercalciuric nephrolithiasis and why?",
                [
                    "Hydrochlorothiazide because it is shortest acting",
                    "Chlorthalidone because of longer half-life and once-daily dosing",
                    "Furosemide because it reduces calcium reabsorption",
                    "Spironolactone because it spares potassium",
                ],
                1,
                "Chlorthalidone 25–50 mg daily (start 12.5 mg if needed) is preferred over HCTZ for sustained hypocalciuric effect.",
                ref(
                    "Hypercalciuria",
                    "Whereas hydrochlorothiazide is commonly used for hypertension, chlorthalidone is favored for treating hypercalciuria because it has a longer half-life and requires only once-daily dosing.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Uric Acid Stones",
                "A gout patient with uric acid stones has persistent hyperuricemia despite diet. Which medication lowers uric acid production?",
                [
                    "Potassium chloride",
                    "Allopurinol starting 100 mg/day up to 300 mg/day",
                    "Probenecid as first-line in low urine pH",
                    "Triamterene",
                ],
                1,
                "Allopurinol 100–300 mg/day reduces uric acid production when diet fails; alkalinization remains key for low-pH stone formers.",
                ref(
                    "Uric Acid Stones",
                    "In this setting, allopurinol should be prescribed at a starting dose of 100 mg/day, increasing to 300 mg/day as needed.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Cystine Stones",
                "Qualitative screening for cystinuria uses sodium nitroprusside. At what urine cystine concentration does the test turn positive?",
                [
                    ">250 mg/L",
                    ">75 mg/L",
                    "Any detectable cystine",
                    "Only homozygotes with >600 mg/day excretion",
                ],
                1,
                "Sodium nitroprusside turns purple-red when urine cystine exceeds ~75 mg/L—quantitative 24-hour cystine follows for therapy.",
                ref(
                    "Cystine Stones",
                    "Urine turns purple-red when sodium nitroprusside is added to a specimen containing cystine at a concentration greater than 75 mg/L.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Laboratory Tests",
                "A stone former has pyuria, urine pH 6.8, and low colony count. Struvite is suspected. What should the lab be asked to do?",
                [
                    "Dismiss culture because count is low",
                    "Identify organism and test for urease despite low colony counts",
                    "Assume E. coli and treat empirically only",
                    "Skip culture if CT shows no hydronephrosis",
                ],
                1,
                "Urease adequate for struvite may occur at ~50,000 CFU—labs must identify organisms and check urease production.",
                ref(
                    "Laboratory Tests",
                    "Because enough urease may be produced to form struvite stones even when colony counts are low (~50,000 colony-forming units), the microbiology laboratory should be instructed specifically to identify the organism and check for urease-producing bacteria despite low colony counts.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Nonspecific Therapy",
                "A postmenopausal woman with stones asks about calcium supplements for osteoporosis. Best advice?",
                [
                    "Take calcium supplements with vitamin D to prevent stones",
                    "Prefer dietary calcium; supplements may worsen stones in older women",
                    "Avoid all calcium including diet",
                    "Supplements are safer than dietary calcium",
                ],
                1,
                "Dietary calcium is protective; supplemental calcium (+ vitamin D) increased stone risk in postmenopausal women—food-based intake preferred.",
                ref(
                    "Nonspecific Therapy",
                    "Calcium supplements, however, were associated with an increased risk of stones in women.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Stone Analysis",
                "A patient passes a new stone with different color and texture than prior episodes. Best step?",
                [
                    "Assume same composition as last stone",
                    "Send stone for analysis (X-ray diffraction or infrared spectroscopy)",
                    "Start empiric thiazide without analysis",
                    "Defer analysis if ultrasound shows no hydronephrosis",
                ],
                1,
                "Stone analysis should be performed whenever possible—especially when presentation changes—to target metabolic workup and therapy.",
                ref(
                    "Stone Analysis",
                    "Stone analysis should be performed, whenever possible, in patients with a new history of nephrolithiasis or in patients with long-standing stone disease who note a difference in clinical presentation or in the color, shape, or texture of any stone passed.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Hyperoxaluria",
                "Dietary hyperoxaluria typically produces what 24-hour urinary oxalate range?",
                [
                    "80–300 mg/day",
                    "40–60 mg/day",
                    "10–20 mg/day",
                    ">400 mg/day only in PHO type 2",
                ],
                1,
                "Dietary oxaluria mildly elevates oxalate (40–60 mg/day); enteric 60–100; PHO 80–300 mg/day.",
                ref(
                    "Hyperoxaluria",
                    "Dietary oxaluria results in urinary oxalate levels that are mildly elevated (40–60 mg/day).",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Surgical Treatment",
                "Which stone composition is relatively contraindicated for ESWL monotherapy?",
                [
                    "Calcium oxalate dihydrate <10 mm",
                    "Cystine and calcium oxalate monohydrate",
                    "Uric acid if visible on fluoroscopy",
                    "Small distal ureteral stones",
                ],
                1,
                "Cystine and calcium oxalate monohydrate fragment poorly with ESWL—alternative surgical modalities are often required.",
                ref(
                    "Surgical Treatment",
                    "Kidney stones less than approximately 15 mm, proximal ureteral stones, upper and middle pole kidney stones, and those not composed of cystine or calcium oxalate monohydrate respond best to ESWL.",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "KEY POINTS",
                "Kidney stones form when urine is supersaturated with respect to stone constituents.",
                True,
                "Supersaturation of specific stone components is the fundamental requirement for growth of new stones and expansion of existing ones.",
                ref(
                    "KEY POINTS",
                    "Kidney stones form when urine becomes supersaturated with respect to the specific components of the stone's constituents.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Epidemiology of Stone Formation",
                "Cystine stones account for approximately 2% of all stones formed in the United States.",
                True,
                "Cystinuria is autosomal recessive and rare (~2% of stones) compared with calcium and uric acid stones.",
                ref(
                    "Epidemiology of Stone Formation",
                    "cystine stones, which are due to an autosomal recessive disorder and constitute only about 2% of all stones formed",
                ),
            ),
            tf(
                f"{p}-t3",
                "Physiology",
                "Heterogeneous nucleation requires higher supersaturation than homogeneous nucleation in vivo.",
                False,
                "Heterogeneous nucleation on a solid phase occurs at lower supersaturation and is more common in vivo.",
                ref(
                    "Physiology",
                    "In vivo, this type of nucleation is more common than homogeneous nucleation because crystals form at a lower level of supersaturation in the presence of a solid phase.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Diet",
                "Dietary calcium restriction is recommended to prevent recurrent kidney stones.",
                False,
                "Low-calcium diets increase stone recurrence and osteoporosis risk—maintain age-appropriate dietary calcium.",
                ref(
                    "Diet",
                    "Dietary calcium restriction should be strongly discouraged because it not only increases risk of stone formation but also engenders a significant risk of bone demineralization and development of osteoporosis.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Struvite Stones",
                "Escherichia coli produces urease and commonly causes struvite stones.",
                False,
                "E. coli is a common UTI pathogen but does not produce urease and is not implicated in struvite genesis.",
                ref(
                    "Struvite Stones",
                    "Escherichia coli, despite its frequent role as a urinary tract pathogen, has not been shown to produce urease and thus is not implicated in the genesis of struvite stones.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Uric Acid Stones",
                "Every patient with uric acid stones in several studies had urine pH less than 6.0.",
                True,
                "Persistently low urine pH is the dominant factor—solubility rises steeply as pH approaches 6.5.",
                ref(
                    "Uric Acid Stones",
                    "In four studies, every patient with uric acid stones had a urine pH less than 6.0.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Cystine Stones",
                "Cystine solubility in urine is less than 250 mg/L.",
                True,
                "Low cystine solubility (~250–300 mg/L) explains stone formation despite modest absolute excretion in heterozygotes.",
                ref(
                    "Cystine Stones",
                    "Low solubility of cystine (<250 mg/L)",
                ),
            ),
            tf(
                f"{p}-t8",
                "Hypercalciuria",
                "Triamterene is preferred as a potassium-sparing diuretic in thiazide-treated stone formers.",
                False,
                "Triamterene can precipitate into stones; amiloride is preferred if a potassium-sparing agent is needed.",
                ref(
                    "Hypercalciuria",
                    "Triamterene is generally avoided because it can precipitate into stones.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Primary Hyperoxaluria",
                "Lumasiran is approved for treatment of type 1 primary hyperoxaluria.",
                True,
                "Lumasiran lowers glycolate oxidase activity and reduces oxalate production in AGT-deficient PHO type 1.",
                ref(
                    "Primary Hyperoxaluria",
                    "Lumasiran in a small interfering RNA has now been approved for treatment for type 1 primary hyperoxaluria.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Distal Renal Tubular Acidosis",
                "Patients with dRTA fail to lower urine pH below 5.5 after an acid load.",
                True,
                "Defective distal acidification defines dRTA and produces alkaline urine with hypocitraturia.",
                ref(
                    "Distal Renal Tubular Acidosis",
                    "Patients with dRTA fail to lower their urine pH below 5.5 following ingestion of an acid load.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Nonspecific Therapy",
                "Nonspecific therapy targets urine volume of approximately 2 to 2.5 L per day.",
                True,
                "Fluid, sodium restriction, moderate protein reduction, and adequate dietary calcium are cornerstone measures for most stone types.",
                ref(
                    "Nonspecific Therapy",
                    "The mainstay of nonspecific therapy involves dietary measures (see the \"Diet\" discussion in the \"Pathogenesis of Stone Formation\" section): increased fluid intake to raise urine volume to approximately 2 to 2.5 L, a reduction in sodium intake to less than 3000 mg/day (130 mEq), moderate reduction in animal protein ingestion to approximately 1.0 mg/kg/day, ingestion of approximately 1 gram of elemental calcium per day, and perhaps eating certain fruits or juices high in citrate.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Surgical Treatment",
                "Stones less than 5 mm have roughly a 68% chance of passing spontaneously.",
                True,
                "Spontaneous passage rates fall sharply as stone size exceeds 5–10 mm—many require intervention.",
                ref(
                    "Surgical Treatment",
                    "Stones less than 5 mm in size have a 68% chance of passing spontaneously, whereas those greater than 5 mm but less than 10 mm have a spontaneous stone passage rate less than 50%.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Physiology",
                "Measuring 24-hour excretion of stone-forming elements alone is superior to supersaturation for assessing lithogenic risk.",
                False,
                "Supersaturation accounts for pH and complexation—better predicts risk than mass excretion alone.",
                ref(
                    "Physiology",
                    "It is clear, however, that the lithogenic potential of urine is better determined by the degree of supersaturation.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "KEY POINTS",
                "Assertion: All patients with kidney stones should undergo at least a basic evaluation.",
                "Reason: A single stone never has a systemic metabolic cause.",
                2,
                "Assertion true; reason false—systemic causes can present with even one stone per NIH consensus.",
                ref(
                    "Metabolic Evaluation of Stone Formers",
                    "These panels determined that all patients, even those with a single stone, should undergo at least a basic evaluation to rule out a systemic etiologic mechanism.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Diet",
                "Assertion: Dietary calcium intake is associated with reduced kidney stone incidence.",
                "Reason: Calcium supplements have the same protective effect as dietary calcium in older women.",
                2,
                "Assertion true; reason false—supplements can exacerbate stones in older women despite dietary calcium benefit.",
                ref(
                    "Diet",
                    "Note that although dietary calcium intake has been associated with a reduced incidence of kidney stones, calcium intake in the form of supplements can exacerbate stone formation in older women.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Physiology",
                "Assertion: Randall plaques provide a nidus for calcium oxalate stone attachment.",
                "Reason: Plaques form only within obstructed tubular lumens filled with crystals.",
                2,
                "Assertion true; reason false—apatite originates at thin loop basement membrane and extends to papillary surface without filling lumens.",
                ref(
                    "Physiology",
                    "The apatite crystals appear to originate at the basement membrane of tubular cells in the thin loop of Henle and extend into the interstitium without damaging the cells themselves or filling the tubular lumens.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Hypercalciuria",
                "Assertion: Thiazide diuretics reduce urinary calcium excretion in hypercalciuric stone formers.",
                "Reason: Thiazides are maximally effective without dietary sodium restriction.",
                2,
                "Assertion true; reason false—sodium restriction is essential because urinary calcium parallels sodium excretion.",
                ref(
                    "Hypercalciuria",
                    "To maximize the efficacy of thiazides, patients must consume a sodium-restricted diet.",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Enteric Oxaluria",
                "Assertion: Malabsorptive GI disorders can cause enteric hyperoxaluria.",
                "Reason: Malabsorbed fatty acids bind intestinal calcium, increasing free oxalate absorption.",
                0,
                "Both true and causally linked—fat-calcium binding in the lumen is the key enteric mechanism.",
                ref(
                    "Enteric Oxaluria",
                    "In these disorders, malabsorbed fatty acids bind calcium in the intestinal lumen, making more \"free\" oxalate available for absorption in the colon.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Uric Acid Stones",
                "Assertion: Low urine pH is the major cause of uric acid nephrolithiasis.",
                "Reason: Uric acid stone formers always have hyperuricosuria.",
                2,
                "Assertion true; reason false—many have normal uric acid excretion but persistently acidic urine.",
                ref(
                    "Uric Acid Stones",
                    "Most patients with uric acid stones have a reduced urinary pH, whereas other less common causes are low urine volume or elevated urinary uric acid levels.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Distal Renal Tubular Acidosis",
                "Assertion: dRTA promotes calcium phosphate stone formation.",
                "Reason: dRTA produces persistently acidic urine and high citrate excretion.",
                2,
                "Assertion true; reason false—dRTA causes alkaline urine and severe hypocitraturia.",
                ref(
                    "Distal Renal Tubular Acidosis",
                    "dRTA (type 1) is a disorder in which distal tubular hydrogen ion excretion is impaired, resulting in a non–anion gap metabolic acidosis and a persistently alkaline urine.",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Struvite Stones",
                "Assertion: Struvite stone formation requires urease-producing bacteria.",
                "Reason: Escherichia coli is a common urease producer implicated in struvite stones.",
                2,
                "Assertion true; reason false—E. coli does not produce urease.",
                ref(
                    "Struvite Stones",
                    "Escherichia coli, despite its frequent role as a urinary tract pathogen, has not been shown to produce urease and thus is not implicated in the genesis of struvite stones.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Cystine Stones",
                "Assertion: Cystinuria is an autosomal recessive disorder with low cystine solubility.",
                "Reason: Cystine readily dissolves at normal daily urine volumes regardless of excretion rate.",
                2,
                "Assertion true; reason false—cystine solubility is ~250–300 mg/L, so homozygotes with >600 mg/day excretion readily supersaturate.",
                ref(
                    "Cystine Stones",
                    "Patients heterozygous for this condition excrete about 400 mg/day, whereas homozygotes often excrete more than 600 mg/day.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Primary Hyperoxaluria",
                "Assertion: Lumasiran reduces oxalate production in type 1 PHO.",
                "Reason: Lumasiran directly replaces defective hepatic AGT enzyme activity.",
                2,
                "Assertion true; reason false—lumasiran inhibits glycolate oxidase upstream of AGT, not the enzyme itself.",
                ref(
                    "Primary Hyperoxaluria",
                    "Lumasiran reduces the levels of glycolate oxidase upstream of the abnormal hepatic enzyme AGT, resulting in less oxalate production.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Medical Expulsive Therapy",
                "Assertion: Tamsulosin facilitates passage of ureteral stones less than 10 mm.",
                "Reason: α-Blockers increase ureteral spasm to expel stones more forcefully.",
                2,
                "Assertion true; reason false—α-blockers reduce spasm and improve peristaltic stone transport.",
                ref(
                    "Medical Expulsive Therapy",
                    "α-Blockers act by reducing spasm of the ureteral smooth muscle and allowing ureteral peristalsis to more effectively move the stone through.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Therapy for Struvite Stones",
                "Assertion: Complete removal of struvite stones is necessary for cure.",
                "Reason: Antibiotics alone can reliably eradicate infected staghorn calculi without surgery.",
                2,
                "Assertion true; reason false—antibiotics must be combined with complete surgical stone removal.",
                ref(
                    "Therapy for Struvite Stones",
                    "Appropriate antibiotic therapy is essential but must be combined with long-term bacterial suppression and complete surgical or medical stone removal.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "31",
        "title": "Kidney Stones",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "David A. Bushinsky",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_31_Kidney_Stones.md",
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
