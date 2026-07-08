#!/usr/bin/env python3
"""Generate Williams 15e module w15-41 — Disorders of Lipoprotein Metabolism."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-41"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-41_Disorders_of_Lipoprotein_Metabolism.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why LDL and Lp(a) elevation drive cardiovascular risk",
                "Elevated LDL and Lp(a), together with mild-to-moderate hypertriglyceridemia, increase atherosclerotic cardiovascular disease risk; lowering LDL-C ameliorates or prevents events.",
                ref(
                    "KEY POINTS",
                    "Elevations of low-density lipoproteins (LDL) and lipoprotein(a) (Lp[a]) and mild to moderate elevations of plasma triglycerides are associated with an increased risk of cardiovascular disease, which can be ameliorated or prevented by lowering LDL-cholesterol (LDL-C) levels.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How intensified LDL lowering beyond statins reduces events",
                "When statin monotherapy cannot reach guideline LDL targets, adding ezetimibe, PCSK9 inhibitors, or other agents that preserve hepatic LDL receptor activity further reduces cardiovascular events.",
                ref(
                    "KEY POINTS",
                    "Aggressive lowering of LDL levels beyond that achievable with statins alone can further reduce the incidence of cardiovascular events.",
                ),
            ),
            note(
                f"{p}-n3",
                "KEY POINTS",
                "Why severe hypertriglyceridemia mandates urgent TG reduction",
                "Triglycerides above ~1000 mg/dL carry pancreatitis risk that outweighs chronic ASCVD concerns in the acute setting; marked TG lowering prevents recurrent pancreatitis.",
                ref(
                    "KEY POINTS",
                    "Severe hypertriglyceridemia can result from several conditions and is associated with an increased risk of pancreatitis, which can be prevented by markedly reducing triglyceride levels.",
                ),
            ),
            note(
                f"{p}-n4",
                "KEY POINTS",
                "Why raising HDL-C has not proven cardioprotective",
                "Low HDL-C correlates with risk epidemiologically, but niacin and CETP inhibitor trials failed to reduce events despite HDL increases—HDL-C is not a validated therapeutic target.",
                ref(
                    "KEY POINTS",
                    "Although low levels of high-density lipoprotein (HDL)-cholesterol (HDL-C) are associated with an increased risk of cardiovascular disease, strategies to specifically increase HDL-C levels have not been effective to date in reducing cardiovascular disease events.",
                ),
            ),
            note(
                f"{p}-n5",
                "Major Lipoproteins",
                "How lipoprotein classes differ in lipid composition",
                "Chylomicrons and VLDL carry triglycerides; IDL, LDL, and Lp(a) are cholesterol-rich; HDL is phospholipid-enriched—classification underlies clinical interpretation of the lipid panel.",
                ref(
                    "Major Lipoproteins",
                    "Chylomicrons, chylomicron remnants, and VLDLs are rich in TGs. Intermediate-density lipoproteins (IDLs), LDLs, and lipoprotein(a) (Lp[a]) are rich in cholesterol. HDLs are enriched in phospholipids.",
                ),
            ),
            note(
                f"{p}-n6",
                "LDL Receptor",
                "How the LDL receptor clears plasma LDL",
                "Hepatic LDL receptors bind apoB100 on LDL, cluster in coated pits, internalize particles, release ligand in acidic endosomes, and recycle to the surface—defective clearance raises plasma LDL-C.",
                ref(
                    "LDL Receptor",
                    "When LDL receptors bind lipoproteins, they migrate to coated pits, and clathrin directs the complex to a cell membrane region that folds inward, creating an intracellular vesicle or endosome",
                ),
            ),
            note(
                f"{p}-n7",
                "Proprotein Convertase Subtilisin/Kexin Type 9",
                "Why PCSK9 limits LDL receptor recycling",
                "Secreted PCSK9 binds the hepatic LDL receptor after internalization and targets it for lysosomal degradation rather than surface recycling—gain-of-function PCSK9 mutations cause familial hypercholesterolemia.",
                ref(
                    "LDL Receptor",
                    "In the presence of PCSK9 (see Fig. 41.13 and “Proprotein Convertase Subtilisin/Kexin Type 9” section), the LDL receptor conformation is altered, promoting degradation and preventing recycling to the cell surface.",
                ),
            ),
            note(
                f"{p}-n8",
                "Monogenic Familial Hypercholesterolemia",
                "How FH arises from LDLR, APOB, and PCSK9 defects",
                "Most FH is autosomal dominant LDLR loss-of-function; familial defective apoB reduces receptor binding; rare PCSK9 gain-of-function accelerates receptor degradation—all impair hepatic LDL clearance.",
                ref(
                    "Monogenic Familial Hypercholesterolemia",
                    "Among patients with FH, 80% to 85% of cases are caused by loss-of-function mutations in the LDLR gene, and another 5% to 10% are caused by missense mutations in the LDL receptor-binding domain of APOB-100 that reduce the ability of LDL to bind to hepatic LDL receptors (familial defective APOB [FDB]).",
                ),
            ),
            note(
                f"{p}-n9",
                "HMG-CoA Reductase Inhibitors (Statins)",
                "How statins lower LDL-C",
                "Statins inhibit hepatic HMG-CoA reductase, deplete intracellular cholesterol, upregulate SREBP-driven LDL receptor expression, and enhance LDL clearance—the cornerstone of ASCVD prevention.",
                ref(
                    "Cholesterol Metabolism",
                    "Statins, which are the major LDL-lowering agents, work by inhibiting cholesterol biosynthesis in the hepatocyte, thereby lowering intracellular cholesterol levels, which results in an increase in LDL receptor expression and transport to the hepatocyte cell surface, where they bind and internalize plasma LDL, thereby enhancing LDL removal",
                ),
            ),
            note(
                f"{p}-n10",
                "Ezetimibe",
                "How ezetimibe blocks intestinal cholesterol absorption",
                "Ezetimibe binds NPC1L1 on enterocytes, reducing dietary and biliary cholesterol reabsorption; added to statins it lowers LDL-C ~14–25% and reduces cardiovascular events.",
                ref(
                    "Cholesterol Absorption, Synthesis, and Excretion",
                    "NPC1L1 is the target of ezetimibe, a drug that lowers cholesterol and has been shown to decrease CVD.",
                ),
            ),
            note(
                f"{p}-n11",
                "PCSK9 Inhibitors",
                "How monoclonal PCSK9 inhibitors augment LDL clearance",
                "Alirocumab and evolocumab prevent PCSK9-mediated LDL receptor degradation, allowing receptor recycling and ~60% additional LDL lowering on statins, with proven ASCVD event reduction.",
                ref(
                    "PCSK9 Inhibitors",
                    "Clinical trials with both monoclonal antibody PCSK9 inhibitors (alirocumab and evolocumab) marketed in the United States demonstrate reductions in atherosclerotic CVD events, particularly in patients with recent acute coronary syndrome, multivessel CAD, or peripheral arterial disease.",
                ),
            ),
            note(
                f"{p}-n12",
                "PCSK9 Inhibitors",
                "How inclisiran silences hepatic PCSK9 synthesis",
                "GalNAc-conjugated siRNA inclisiran is given subcutaneously at baseline, 3 months, then every 6 months, lowering LDL-C ~51% by reducing hepatic PCSK9 production.",
                ref(
                    "PCSK9 Inhibitors",
                    "A meta-analysis of data from three randomized clinical trials demonstrated that inclisiran decreases LDL-C levels by 51% and is associated with a 24% lower risk of major adverse cardiovascular events.",
                ),
            ),
            note(
                f"{p}-n13",
                "Bempedoic Acid",
                "How bempedoic acid lowers LDL in statin-intolerant patients",
                "Bempedoic acid inhibits ATP-citrate lyase upstream of HMG-CoA reductase, reducing hepatic cholesterol synthesis and upregulating LDL receptors—useful alone or combined when statins are not tolerated.",
                ref(
                    "Bempedoic Acid",
                    "Thus, bempedoic acid inhibits cholesterol synthesis, which in turn leads to an increase in hepatic LDL receptor synthesis and reduced plasma LDL-C.",
                ),
            ),
            note(
                f"{p}-n14",
                "Lipoprotein(a) as a Major Cardiovascular Risk Factor",
                "Why Lp(a) is an independent genetic ASCVD risk factor",
                "Lp(a) levels are ~90% genetically determined; elevated Lp(a) confers MI, stroke, PAD, and aortic stenosis risk independent of LDL-C, yet no approved Lp(a)-specific therapy exists.",
                ref(
                    "Lipoprotein(a) as a Major Cardiovascular Risk Factor",
                    "In fact, Lp(a) is probably the most prevalent lipoprotein risk factor worldwide for CVD for which no specific therapy is currently available.",
                ),
            ),
            note(
                f"{p}-n15",
                "Lipoprotein Lipase",
                "Why APOC2 is required for triglyceride clearance",
                "LPL hydrolyzes TG on chylomicrons and VLDL at capillary endothelium; APOC2 is an obligate LPL cofactor—biallelic APOC2 loss causes severe hypertriglyceridemia mimicking LPL deficiency.",
                ref(
                    "Lipoprotein Lipase",
                    "Apolipoprotein C2 (APOC2), encoded by APOC2, is an obligate activator of LPL.",
                ),
            ),
            note(
                f"{p}-n16",
                "Severe Hypertriglyceridemia",
                "How severe hypertriglyceridemia causes pancreatitis",
                "TG >1000 mg/dL can precipitate chylomicronemia syndrome; pancreatic lipolysis of retained chylomicrons may generate toxic lysolecithin and free fatty acids, triggering acute pancreatitis with worse outcomes than other causes.",
                ref(
                    "Chylomicronemia Syndrome",
                    "However, by far the most serious consequence of severe hypertriglyceridemia is acute pancreatitis, which can be recurrent if TG levels are not adequately managed.",
                ),
            ),
            note(
                f"{p}-n17",
                "Drug Treatment for Mild to Moderately Severe Hypertriglyceridemia",
                "How fibrates lower triglycerides and raise HDL",
                "Fibrates activate PPARα, increasing LPL activity and apoA-I/A-II while lowering APOC3—typically reducing TG 25–50% and raising HDL-C 5–20%; fenofibrate is preferred with statins over gemfibrozil.",
                ref(
                    "Fibrates",
                    "Importantly, fibrates lower TGs by 25% to 50% and raise HDL-C by 5% to 20%, depending on the baseline levels of TGs.",
                ),
            ),
            note(
                f"{p}-n18",
                "Omega-3 Fatty Acids",
                "How icosapent ethyl reduced ASCVD in REDUCE-IT",
                "Prescription EPA (icosapent ethyl 4 g/day) reduced major coronary events in statin-treated patients with mild hypertriglyceridemia and established ASCVD or diabetes—distinct from mixed EPA/DHA trials that were neutral.",
                ref(
                    "Omega-3 Fatty Acids",
                    "However, a more recent study, Reduction of Cardiovascular Events With Icosapent Ethyl–Intervention Trial (REDUCE-IT), using 4 g of icosapent ethyl, a synthetic EPA, in mildly to moderately hypertriglyceridemic participants with known atherosclerosis or high risk (e.g., diabetes), dramatically reduced coronary events.",
                ),
            ),
            note(
                f"{p}-n19",
                "Niacin",
                "Why niacin use has declined despite lipid effects",
                "Niacin lowers TG and raises HDL but AIM-HIGH and HPS2-THRIVE showed no added benefit atop statins; flushing and hepatotoxicity limit use—now reserved for refractory hypertriglyceridemia or extreme Lp(a).",
                ref(
                    "Niacin",
                    "However, more recent trials of slow-release niacin in subjects whose LDL was already markedly reduced by statins failed to show additional clinical benefit with niacin,",
                ),
            ),
            note(
                f"{p}-n20",
                "Combined Hyperlipoproteinemias",
                "How familial combined hyperlipidemia presents",
                "FCHL features concurrent LDL and VLDL elevation from hepatic APOB overproduction (often with insulin resistance); phenotypes within families vary between isolated high TG, high LDL, or both over time.",
                ref(
                    "Combined Hyperlipoproteinemias",
                    "When it occurs within families, this phenotypic pattern has historically been termed familial combined hyperlipidemia (FCHL).",
                ),
            ),
            note(
                f"{p}-n21",
                "Tangier Disease",
                "Why Tangier disease causes near-absent HDL",
                "Biallelic ABCA1 loss impairs cholesterol efflux to apoA-I, producing extremely low HDL-C, orange tonsils, and hepatosplenomegaly; paradoxically LDL-C is also very low and major ASCVD risk is not clearly increased.",
                ref(
                    "Tangier Disease",
                    "Tangier disease results from biallelic homozygous loss-of-function or compound heterozygous mutations in the ABCA1 gene.",
                ),
            ),
            note(
                f"{p}-n22",
                "Cholesteryl Ester Transfer Protein",
                "How CETP reshapes HDL and LDL composition",
                "CETP exchanges cholesteryl esters from HDL for TG on VLDL/IDL/LDL, enriching atherogenic particles with cholesterol in humans—CETP deficiency raises HDL-C and lowers LDL-C.",
                ref(
                    "Cholesteryl Ester Transfer Protein",
                    "CETP promotes the exchange between lipoproteins of two classes of neutral lipids: cholesteryl esters and TGs.",
                ),
            ),
            note(
                f"{p}-n23",
                "Diabetes Mellitus",
                "How diabetes causes atherogenic dyslipidemia",
                "Insulin deficiency/resistance increases VLDL secretion, impairs LPL, and drives CETP-mediated formation of small dense LDL and low HDL—APOB is elevated even when LDL-C appears normal.",
                ref(
                    "Diabetes Mellitus",
                    "Diabetic dyslipidemia is characterized by moderate hypertriglyceridemia, low HDL-C, and an increased number of small LDL particles such that APOB, but not LDL-C, is elevated.",
                ),
            ),
            note(
                f"{p}-n24",
                "Hypothyroidism",
                "Why untreated hypothyroidism elevates LDL and TG",
                "Hypothyroidism reduces hepatic LDL receptors, bile acid synthesis, LPL activity, and CETP—restoring euthyroidism normalizes lipids and should be excluded before intensifying lipid drugs.",
                ref(
                    "Hypothyroidism",
                    "Uncontrolled hypothyroidism usually causes hypercholesterolemia, often accompanied by hypertriglyceridemia.",
                ),
            ),
            note(
                f"{p}-n25",
                "Patient Selection and Treatment Goals",
                "How ASCVD risk guides LDL-C treatment targets",
                "Secondary prevention CAD patients should reach LDL-C <70 mg/dL (European guidelines often <55 mg/dL in very high risk); primary prevention uses risk calculators and treats LDL-C >190 mg/dL regardless of score.",
                ref(
                    "Patient Selection and Treatment Goals",
                    "Almost all guidelines now agree that the LDL-C goal for secondary prevention in patients with existing CAD should be less than 70 mg/dL (1.8 mmol/L).",
                ),
            ),
            note(
                f"{p}-n26",
                "Laboratory Analysis of Lipids and Lipoproteins",
                "Why calculated LDL-C fails at high triglycerides",
                "Friedewald LDL-C becomes inaccurate when TG exceeds ~400 mg/dL and misclassifies risk when discordant from non–HDL-C; direct LDL or beta-quantification is needed in severe hypertriglyceridemia.",
                ref(
                    "Laboratory Analysis of Lipids and Lipoproteins",
                    "LDL-C measured by the Friedewald equation can be inaccurate in the presence of hypertriglyceridemia, and the standard lipid panel is not recommended for use with TGs over 400 mg/dL (4.5 mmol/L), although inaccuracies are present even at lower TG levels.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Monogenic Familial Hypercholesterolemia",
                "A 12-year-old with LDL-C 420 mg/dL, Achilles tendon thickening, and a parent with premature MI most likely has:",
                [
                    "Heterozygous familial hypercholesterolemia (LDLR mutation)",
                    "Homozygous LPL deficiency with chylomicronemia",
                    "Tangier disease with ABCA1 deficiency",
                    "Primary hypoalphalipoproteinemia from APOA1 mutation",
                ],
                0,
                "FH is the commonest monogenic hypercholesterolemia with tendon xanthomas and very high LDL from impaired receptor-mediated clearance.",
                ref(
                    "Monogenic Familial Hypercholesterolemia",
                    "Patients with FH have up to a 10-fold increased prevalence of CAD if untreated.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "PCSK9 Inhibitors",
                "A patient on maximally tolerated statin plus ezetimibe has LDL-C 95 mg/dL with recent ACS. Best additional therapy?",
                [
                    "PCSK9 monoclonal antibody (evolocumab or alirocumab)",
                    "High-dose niacin to raise HDL-C",
                    "CETP inhibitor to raise HDL",
                    "Fibrate monotherapy for triglycerides",
                ],
                0,
                "PCSK9 inhibitors are recommended when LDL remains ≥70 mg/dL on maximally tolerated oral therapy in high-risk ASCVD patients.",
                ref(
                    "PCSK9 Inhibitors",
                    "PCSK9 inhibitors are recommended for high-risk patients with LDL levels of 70 mg/dL (1.8 mmol/L) or higher on maximally tolerated oral therapies, including statins and/or ezetimibe.",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Ezetimibe",
                "Ezetimibe lowers LDL-C primarily by:",
                [
                    "Inhibiting NPC1L1-mediated intestinal cholesterol absorption",
                    "Blocking MTP and VLDL assembly",
                    "Activating PPARα and LPL",
                    "Inhibiting PCSK9 secretion from hepatocytes",
                ],
                0,
                "Ezetimibe targets the intestinal sterol transporter NPC1L1, complementing statin-mediated synthesis blockade.",
                ref(
                    "Cholesterol Absorption, Synthesis, and Excretion",
                    "NPC1L1 is the target of ezetimibe, a drug that lowers cholesterol and has been shown to decrease CVD.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Bempedoic Acid",
                "Bempedoic acid is especially useful in which clinical scenario?",
                [
                    "Statin-intolerant patient needing additional LDL lowering",
                    "Familial chylomicronemia with absent LPL activity",
                    "Severe hypertriglyceridemia requiring fibrate monotherapy",
                    "Tangier disease with absent HDL",
                ],
                0,
                "Bempedoic acid inhibits ATP-citrate lyase, reduces LDL-C 18–30%, and is active in the liver without systemic statin exposure.",
                ref(
                    "Bempedoic Acid",
                    "It may be especially useful in statin-intolerant patients.",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Lipoprotein(a) as a Major Cardiovascular Risk Factor",
                "A patient with LDL-C at goal on statin has Lp(a) 180 nmol/L and family history of early MI. Best approach?",
                [
                    "Treat Lp(a) as a risk-enhancing factor and intensify LDL lowering; measure Lp(a) once in relatives",
                    "Stop statin because statins always lower Lp(a)",
                    "Ignore Lp(a) if LDL-C is at target",
                    "Start fibrate solely to lower Lp(a)",
                ],
                0,
                "Elevated Lp(a) amplifies baseline ASCVD risk; maximize LDL-C lowering and address other risk factors—no approved Lp(a)-specific drug yet.",
                ref(
                    "Management of the Patient With High Lp(a)",
                    "Thus, all CVD risk factors should be optimally addressed according to the various guideline recommendations.",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Severe Hypertriglyceridemia",
                "A patient presents with TG 2800 mg/dL and epigastric pain. Immediate priority beyond IV fluids?",
                [
                    "Aggressive triglyceride lowering (diet, fibrate, omega-3) to prevent recurrent pancreatitis",
                    "High-intensity statin for LDL-C only",
                    "Ezetimibe monotherapy",
                    "Oral estrogen to raise HDL",
                ],
                0,
                "Severe hypertriglyceridemia causes acute pancreatitis; target TG <500 mg/dL to minimize recurrence risk.",
                ref(
                    "Drug Treatment for Severe Hypertriglyceridemia",
                    "The initial goal of drug treatment for the patient with severe hypertriglyceridemia is to prevent the development of TG-induced pancreatitis, the onset of which will not occur at levels below 500 to 750 mg/dL (5.6–8.5 mmol/L).",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Familial Chylomicronemia Syndrome",
                "A child with fasting TG >5000 mg/dL and absent post-heparin LPL activity has:",
                [
                    "Familial chylomicronemia syndrome (LPL deficiency)",
                    "Heterozygous FH with LDLR mutation",
                    "CETP deficiency with high HDL",
                    "Sitosterolemia from ABCG5/G8 mutations",
                ],
                0,
                "FCS features absent LPL activity, extreme fasting hyperchylomicronemia, and pancreatitis risk from childhood.",
                ref(
                    "Genetics of Severe Hypertriglyceridemia",
                    "FCS, also known as type I hyperlipoproteinemia or LPL deficiency, is an extremely rare autosomal-recessive genetic disorder characterized by absent plasma activity of LPL, which results in marked degrees of hypertriglyceridemia.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Apolipoproteins C1, C2, and C3",
                "Biallelic APOC2 deficiency causes severe hypertriglyceridemia because:",
                [
                    "APOC2 is an obligate cofactor required to activate LPL",
                    "APOC2 inhibits hepatic VLDL secretion",
                    "APOC2 blocks NPC1L1 cholesterol absorption",
                    "APOC2 is the LDL receptor ligand on LDL particles",
                ],
                0,
                "Without APOC2, LPL cannot hydrolyze TG on chylomicrons and VLDL, mimicking LPL deficiency.",
                ref(
                    "Apolipoproteins C1, C2, and C3",
                    "APOC2 plays a vital role in mediating TG clearance from plasma because it is an obligate activator of the enzyme LPL.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Fibrates",
                "When combining a fibrate with a statin for hypertriglyceridemia, which agent is preferred to minimize myopathy risk?",
                [
                    "Fenofibrate",
                    "Gemfibrozil",
                    "Clofibrate",
                    "Pemafibrate (if available) with gemfibrozil",
                ],
                0,
                "Gemfibrozil inhibits statin glucuronidation and raises myopathy risk; fenofibrate does not significantly affect statin metabolism.",
                ref(
                    "Fibrates",
                    "The combination of gemfibrozil and most statins is associated with an increased risk of myopathy due to increased statin blood levels, whereas fenofibrate does not interfere with statin metabolism and is preferred in fibrate/statin combination regimens.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Omega-3 Fatty Acids",
                "REDUCE-IT demonstrated cardiovascular benefit with:",
                [
                    "Icosapent ethyl 4 g/day added to statin therapy",
                    "Over-the-counter fish oil 1 g/day",
                    "Combined EPA+DHA that was stopped for futility",
                    "Dietary fish intake alone without statin",
                ],
                0,
                "Prescription EPA (icosapent ethyl) reduced coronary events in high-risk patients with TG 135–500 mg/dL on statins.",
                ref(
                    "Omega-3 Fatty Acids",
                    "Nonetheless, icosapent ethyl has been approved to reduce CVD in people with TG levels greater than 135 mg/dL (1.5 mmol/L), although it was not related to a decrease in plasma TG levels.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Combined Hyperlipoproteinemias",
                "Familial combined hyperlipidemia is best characterized by:",
                [
                    "Elevated LDL and VLDL with variable TG/LDL pattern in family members",
                    "Isolated Lp(a) elevation with normal LDL",
                    "Homozygous APOE2 causing palmar xanthomas only",
                    "Absent HDL from ABCA1 mutations",
                ],
                0,
                "FCHL reflects hepatic APOB overproduction with combined LDL and TG elevation and variable expression within pedigrees.",
                ref(
                    "Combined Hyperlipoproteinemias",
                    "Combined hyperlipoproteinemia usually refers to the simultaneous elevation of LDL and VLDL levels.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Tangier Disease",
                "Orange hypertrophic tonsils and HDL-C <5 mg/dL suggest:",
                [
                    "Tangier disease (ABCA1 deficiency)",
                    "LCAT deficiency with corneal opacity only",
                    "HeFH with tendon xanthomas",
                    "CETP deficiency with very high HDL",
                ],
                0,
                "Tangier disease features absent ABCA1-mediated cholesterol efflux, near-absent HDL, and characteristic tonsillar lipid deposition.",
                ref(
                    "Tangier Disease",
                    "Patients with Tangier disease have enlarged yellow- or orange-colored tonsils and enlarged livers, spleens, and lymph nodes, presumably due to inability to export cholesterol from tissue macrophages.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "CETP Deficiency",
                "Homozygous CETP deficiency typically produces:",
                [
                    "Markedly elevated HDL-C and reduced LDL-C",
                    "Absent LDL with abetalipoproteinemia",
                    "Severe hyperchylomicronemia and pancreatitis",
                    "Low HDL and high Lp(a) only",
                ],
                0,
                "Loss of CETP impairs cholesteryl ester transfer from HDL to apoB lipoproteins, raising HDL-C and lowering LDL-C.",
                ref(
                    "CETP Deficiency",
                    "Homozygous mutations in the CETP gene that result in complete loss of enzyme activity lead to increased HDL-C and reduced LDL-C levels because of impaired transfer of cholesteryl esters from HDLs to lower-density lipoproteins.",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Diabetes Mellitus",
                "A patient with type 2 diabetes has TG 280 mg/dL, HDL 34 mg/dL, and LDL-C 98 mg/dL. The most atherogenic feature is often:",
                [
                    "Elevated APOB from increased small dense LDL particles",
                    "Isolated LDL-C elevation above 190 mg/dL",
                    "Very low Lp(a) conferring protection",
                    "High HDL-C from insulin therapy",
                ],
                0,
                "Diabetic dyslipidemia elevates atherogenic particle number (APOB) despite seemingly normal LDL-C.",
                ref(
                    "Diabetes Mellitus",
                    "Diabetic dyslipidemia is characterized by moderate hypertriglyceridemia, low HDL-C, and an increased number of small LDL particles such that APOB, but not LDL-C, is elevated.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Hypothyroidism",
                "A patient with new hypercholesterolemia and fatigue has TSH 28 mIU/L. Before starting ezetimibe, you should:",
                [
                    "Treat hypothyroidism and recheck lipids",
                    "Start PCSK9 inhibitor immediately",
                    "Order LPL genotyping",
                    "Prescribe high-dose niacin first",
                ],
                0,
                "Secondary hypercholesterolemia from hypothyroidism often normalizes with levothyroxine—exclude treatable causes first.",
                ref(
                    "Hypothyroidism",
                    "Restoration of the euthyroid status leads to a return of lipid levels to their baseline status.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Chronic Kidney Disease and Nephrotic Syndrome",
                "Nephrotic syndrome commonly causes dyslipidemia through:",
                [
                    "Increased APOB synthesis (raising LDL) and elevated ANGPTL4 (raising TG)",
                    "Complete LPL deficiency from birth",
                    "CETP overactivity lowering HDL exclusively",
                    "Absent NPC1L1 preventing cholesterol absorption",
                ],
                0,
                "Nephrotic syndrome raises LDL via increased hepatic APOB production and TG via ANGPTL4-mediated LPL inhibition.",
                ref(
                    "Chronic Kidney Disease and Nephrotic Syndrome",
                    "Hypertriglyceridemia in nephrotic syndrome has been linked to increased circulating levels of the LPL inhibitor ANGPTL4.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "Patient Selection and Treatment Goals",
                "For secondary prevention in established coronary artery disease, current guidelines agree on an LDL-C target of:",
                [
                    "<70 mg/dL (1.8 mmol/L), with lower goals in very high-risk patients",
                    "<130 mg/dL without exceptions",
                    "50% reduction only, without absolute targets",
                    "Normalization of HDL-C above 60 mg/dL",
                ],
                0,
                "Secondary prevention CAD warrants LDL-C <70 mg/dL; European guidelines often target <55 mg/dL in very high risk.",
                ref(
                    "Patient Selection and Treatment Goals",
                    "Almost all guidelines now agree that the LDL-C goal for secondary prevention in patients with existing CAD should be less than 70 mg/dL (1.8 mmol/L).",
                ),
            ),
            mcq(
                f"{p}-m18",
                "HMG-CoA Reductase Inhibitors (Statins)",
                "A patient reports muscle aches on atorvastatin 80 mg. Creatine kinase is normal. Next step per chapter guidance:",
                [
                    "Exclude hypothyroidism and interacting drugs; consider lower dose or alternate-day rosuvastatin",
                    "Permanently discontinue all lipid therapy",
                    "Switch immediately to high-dose niacin monotherapy",
                    "Add gemfibrozil to improve tolerability",
                ],
                0,
                "Most statin myalgia occurs with normal CK; evaluate secondary causes and drug interactions before abandoning therapy.",
                ref(
                    "HMG-CoA Reductase Inhibitors (Statins)",
                    "In patients with muscle complaints after statin administration, creatinine kinase levels will be within normal limits in over 99% of cases.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Gain-of-Function Mutations in PCSK9",
                "Gain-of-function PCSK9 mutations cause hypercholesterolemia by:",
                [
                    "Enhancing lysosomal degradation of hepatic LDL receptors",
                    "Blocking APOB100 synthesis in the liver",
                    "Activating LPL on chylomicrons",
                    "Increasing HDL-mediated reverse cholesterol transport",
                ],
                0,
                "PCSK9 binds internalized LDL receptors and diverts them to degradation rather than recycling, reducing hepatic LDL clearance.",
                ref(
                    "Gain-of-Function Mutations in PCSK9",
                    "Gain-of-function mutations increase the ability of the secreted PCSK9 to mediate enhanced degradation of hepatic LDL receptors, reducing LDL receptor number, which leads to reduced plasma LDL clearance by the liver and a clinical picture of FH.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Multifactorial Chylomicronemia Syndrome",
                "A middle-aged man with TG 1600 mg/dL on prednisone and uncontrolled diabetes most likely has:",
                [
                    "Multifactorial chylomicronemia syndrome exacerbated by secondary factors",
                    "Homozygous CETP deficiency",
                    "Isolated HeFH without hypertriglyceridemia",
                    "Tangier disease",
                ],
                0,
                "MFCS results from polygenic hypertriglyceridemia worsened by drugs/metabolic conditions that saturate TG removal pathways.",
                ref(
                    "Causes and Pathogenesis",
                    "MFCS is nearly always the result of exacerbation of genetic forms of mild to moderate hypertriglyceridemia by disorders or drugs that can adversely affect TG levels",
                ),
            ),
            mcq(
                f"{p}-m21",
                "PCSK9 Inhibitors",
                "Inclisiran differs from alirocumab/evolocumab because it:",
                [
                    "Uses hepatic siRNA to reduce PCSK9 synthesis with dosing every 6 months",
                    "Is an oral MTP inhibitor taken daily",
                    "Directly inhibits LPL activity",
                    "Blocks intestinal NPC1L1",
                ],
                0,
                "Inclisiran is a GalNAc-conjugated siRNA given subcutaneously at extended intervals to silence hepatic PCSK9.",
                ref(
                    "PCSK9 Inhibitors",
                    "injections of inclisiran are given at baseline, 3 months, and then only at 6-month intervals.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Laboratory Analysis of Lipids and Lipoproteins",
                "When fasting TG is 520 mg/dL, calculated LDL-C by Friedewald is often:",
                [
                    "Underestimated or unreliable; direct LDL or non–HDL-C preferred",
                    "More accurate than at low TG",
                    "Equivalent to beta-quantification",
                    "Unaffected by Lp(a) content",
                ],
                0,
                "Friedewald LDL-C is inaccurate when TG >400 mg/dL; non–HDL-C or direct assays are preferred.",
                ref(
                    "Laboratory Analysis of Lipids and Lipoproteins",
                    "the standard lipid panel is not recommended for use with TGs over 400 mg/dL (4.5 mmol/L), although inaccuracies are present even at lower TG levels.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Niacin",
                "Extended-release niacin added to statin in patients with LDL already at goal failed to show benefit primarily because:",
                [
                    "AIM-HIGH and HPS2-THRIVE showed no incremental CVD reduction despite HDL/TG changes",
                    "Niacin cannot lower triglycerides",
                    "Niacin raises LDL-C dramatically",
                    "Niacin is contraindicated with any statin",
                ],
                0,
                "Recent outcome trials found no added event reduction from niacin atop statins despite favorable lipid shifts.",
                ref(
                    "Niacin",
                    "However, more recent trials of slow-release niacin in subjects whose LDL was already markedly reduced by statins failed to show additional clinical benefit with niacin,",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Hypercholesterolemia and Atherosclerosis",
                "The central causal lipoprotein in atherosclerosis development is:",
                [
                    "LDL, particularly when elevated over a lifetime",
                    "HDL, when mildly reduced only",
                    "Chylomicrons in all adults regardless of TG",
                    "Lp(a) only when LDL is very low",
                ],
                0,
                "LDL-C is the dominant causal factor for atherosclerotic CVD; lowering LDL prevents and regresses disease.",
                ref(
                    "Hypercholesterolemia and Atherosclerosis",
                    "Similarly, there is now overwhelming epidemiologic, experimental, and therapeutic data that plasma cholesterol, and specifically LDL-C, is the major causal factor responsible for the complications of atherosclerosis",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Drugs Causing Hyper- and Dyslipoproteinemia",
                "A woman with baseline TG 380 mg/dL starting oral estrogen for menopause is at risk of:",
                [
                    "Severe hypertriglyceridemia and pancreatitis if she has underlying genetic susceptibility",
                    "Isolated LDL lowering without TG change",
                    "Mandatory HDL elevation preventing ASCVD",
                    "LPL overactivation and hypoglycemia",
                ],
                0,
                "Oral estrogen increases hepatic VLDL production and can precipitate chylomicronemia in predisposed patients—check TG before therapy.",
                ref(
                    "Drugs Causing Hyper- and Dyslipoproteinemia",
                    "In the setting of an underlying genetic form of hypertriglyceridemia, severe hyperchylomicronemia and pancreatitis can occur in patients taking oral estrogen alone or estrogen-containing birth control pills",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Familial Chylomicronemia Syndrome",
                "Dietary management of familial chylomicronemia syndrome requires:",
                [
                    "Total fat restriction to <5–10 g/day (often with MCT supplementation)",
                    "High saturated fat to stimulate LPL",
                    "Unrestricted omega-3 fish oil at 4 g/day as sole therapy",
                    "High carbohydrate diet to lower VLDL",
                ],
                0,
                "FCS lacks functional LPL; all dietary fat must be severely restricted, with MCTs used because they bypass chylomicron formation.",
                ref(
                    "Approach to Management of the Patient With Severe Hypertriglyceridemia—Diet and Lifestyle Measures",
                    "in FCS, total dietary fat (all types, including saturated and unsaturated) intake should be limited to less than 5 to 10 g/day, which is difficult to maintain on an ongoing basis and is a major burden to patients.",
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
                "Lowering LDL-cholesterol can ameliorate or prevent cardiovascular disease associated with dyslipidemia.",
                True,
                "Key points state LDL-C lowering prevents or ameliorates CVD linked to LDL, Lp(a), and moderate TG elevations.",
                ref(
                    "KEY POINTS",
                    "which can be ameliorated or prevented by lowering LDL-cholesterol (LDL-C) levels.",
                ),
            ),
            tf(
                f"{p}-t2",
                "KEY POINTS",
                "Strategies to specifically increase HDL-C have been effective in reducing cardiovascular disease events to date.",
                False,
                "Key points explicitly state HDL-raising strategies have not reduced CVD events.",
                ref(
                    "KEY POINTS",
                    "strategies to specifically increase HDL-C levels have not been effective to date in reducing cardiovascular disease events.",
                ),
            ),
            tf(
                f"{p}-t3",
                "Lipoprotein Lipase",
                "Apolipoprotein C2 is an obligate activator of lipoprotein lipase.",
                True,
                "APOC2 is required as cofactor for LPL-mediated TG hydrolysis.",
                ref(
                    "Lipoprotein Lipase",
                    "Apolipoprotein C2 (APOC2), encoded by APOC2, is an obligate activator of LPL.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Monogenic Familial Hypercholesterolemia",
                "Heterozygous familial hypercholesterolemia affects approximately 1 in 250 people.",
                True,
                "Updated population data suggest HeFH prevalence ~1:250, higher than historic 1:500 estimates.",
                ref(
                    "Monogenic Familial Hypercholesterolemia",
                    "Although the prevalence of HeFH was previously thought to be about 1:500, more recent population data suggest a prevalence of about 1:250.",
                ),
            ),
            tf(
                f"{p}-t5",
                "PCSK9 Inhibitors",
                "Statins lower lipoprotein(a) levels by approximately 10% on average.",
                False,
                "Statins do not lower Lp(a); they may raise Lp(a) ~10% while lowering LDL-C.",
                ref(
                    "Management of the Patient With High Lp(a)",
                    "Statins do not lower Lp(a) and, in fact, can raise Lp(a) by approximately 10%, but this increase can be up to 20%.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Severe Hypertriglyceridemia",
                "Acute pancreatitis is the most serious consequence of severe hypertriglyceridemia.",
                True,
                "Chylomicronemia syndrome's gravest complication is TG-induced pancreatitis.",
                ref(
                    "Chylomicronemia Syndrome",
                    "by far the most serious consequence of severe hypertriglyceridemia is acute pancreatitis",
                ),
            ),
            tf(
                f"{p}-t7",
                "Fibrates",
                "Fenofibrate is preferred over gemfibrozil when combined with statins because fenofibrate does not interfere with statin metabolism.",
                True,
                "Gemfibrozil raises statin levels and myopathy risk; fenofibrate lacks this interaction.",
                ref(
                    "Fibrates",
                    "whereas fenofibrate does not interfere with statin metabolism and is preferred in fibrate/statin combination regimens.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Combined Hyperlipoproteinemias",
                "Familial combined hyperlipidemia can result from increased VLDL secretion leading to elevated LDL production.",
                True,
                "Hepatic overproduction of APOB-containing lipoproteins underlies combined LDL/VLDL elevation in FCHL.",
                ref(
                    "Etiology of Hypercholesterolemia",
                    "Increased LDL-C also can result from increased VLDL secretion leading to increased LDL production, as occurs in familial combined hyperlipidemia",
                ),
            ),
            tf(
                f"{p}-t9",
                "Tangier Disease",
                "Tangier disease is caused by mutations in the ABCA1 gene.",
                True,
                "ABCA1 deficiency impairs cholesterol efflux to apoA-I, causing Tangier disease.",
                ref(
                    "Tangier Disease",
                    "Tangier disease results from biallelic homozygous loss-of-function or compound heterozygous mutations in the ABCA1 gene.",
                ),
            ),
            tf(
                f"{p}-t10",
                "Diabetes Mellitus",
                "Diabetes mellitus is a prominent cause of hypertriglyceridemia.",
                True,
                "Insulin resistance increases VLDL secretion and impairs TG clearance in diabetes.",
                ref(
                    "Diabetes Mellitus",
                    "Diabetes mellitus is a prominent cause of hypertriglyceridemia.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Patient Selection and Treatment Goals",
                "Most guidelines recommend drug treatment for any patient with LDL-C greater than 190 mg/dL irrespective of risk score.",
                True,
                "LDL-C ≥190 mg/dL warrants therapy even without calculated risk score elevation.",
                ref(
                    "Patient Selection and Treatment Goals",
                    "Most guidelines recommend drug treatment for any patient with LDL-C greater than 190 mg/dL (4.9 mmol/L), irrespective of risk score.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Familial Chylomicronemia Syndrome",
                "Fibrates are largely effective in lowering triglycerides in familial chylomicronemia syndrome.",
                False,
                "FCS lacks LPL activity; fibrates that work via LPL upregulation are largely ineffective.",
                ref(
                    "Familial Chylomicronemia Syndrome",
                    "Fibrates, which effectively lower TGs in most situations, are largely ineffective in lowering TGs in FCS.",
                ),
            ),
            tf(
                f"{p}-t13",
                "Lipoprotein(a) as a Major Cardiovascular Risk Factor",
                "Lp(a) levels are approximately 90% determined by genetic variation at the LPA locus.",
                True,
                "Lp(a) is highly heritable with minimal adult environmental influence.",
                ref(
                    "Regulation of Lp(a) Levels",
                    "levels are approximately 90% determined by genetic variation at the LPA locus.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "LDL Receptor",
                "Assertion: PCSK9 promotes degradation of the hepatic LDL receptor.",
                "Reason: PCSK9 is synthesized only in adipose tissue and has no hepatic role.",
                2,
                "Assertion true—PCSK9 targets LDL receptor for lysosomal degradation; reason false—hepatic PCSK9 secretion regulates plasma LDL.",
                ref(
                    "Proprotein Convertase Subtilisin/Kexin Type 9",
                    "Although it is secreted by a number of tissues, it is the hepatic secretion that is of relevance to regulation of plasma LDL concentrations.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Monogenic Familial Hypercholesterolemia",
                "Assertion: Patients with homozygous FH may have LDL-C exceeding 1000 mg/dL.",
                "Reason: Homozygous FH results from two normal LDLR alleles with enhanced receptor activity.",
                2,
                "Assertion true—HoFH causes extreme LDL-C; reason false—HoFH requires two defective LDLR (or equivalent) alleles.",
                ref(
                    "Monogenic Familial Hypercholesterolemia",
                    "and even exceeding 1000 mg/dL (25.9 mmol/L) in those with HoFH.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "HMG-CoA Reductase Inhibitors (Statins)",
                "Assertion: Statins are the cornerstone of LDL-lowering therapy.",
                "Reason: Statins work by increasing intestinal cholesterol absorption via NPC1L1.",
                2,
                "Assertion true—statins are first-line for LDL lowering; reason false—that describes ezetimibe, not statins.",
                ref(
                    "HMG-CoA Reductase Inhibitors (Statins)",
                    "Statins are the cornerstone of therapy to lower LDL-C and have been in use since 1984.",
                ),
            ),
            ar(
                f"{p}-ar4",
                "PCSK9 Inhibitors",
                "Assertion: PCSK9 monoclonal antibodies can lower LDL-C by nearly 60% beyond statins alone.",
                "Reason: PCSK9 inhibitors block hepatic VLDL secretion entirely.",
                2,
                "Assertion true—PCSK9 antibodies markedly augment LDL lowering; reason false—they preserve LDL receptors, not block VLDL secretion.",
                ref(
                    "PCSK9 Inhibitors",
                    "leading to a nearly 60% further reduction in circulating LDL beyond that achieved by statins alone",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Lipoprotein(a) as a Major Cardiovascular Risk Factor",
                "Assertion: Elevated Lp(a) is an independent causal risk factor for cardiovascular disease.",
                "Reason: Lp(a) levels are primarily determined by dietary saturated fat intake.",
                2,
                "Assertion true—genetic and epidemiologic data support Lp(a) causality; reason false—~90% of Lp(a) is genetically determined.",
                ref(
                    "Lp(a) Epidemiology",
                    "have established that Lp(a) is an independent, causal, and genetic risk factor for CVD in both primary and secondary settings.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Apolipoproteins C1, C2, and C3",
                "Assertion: Biallelic APOC2 deficiency causes severe hypertriglyceridemia.",
                "Reason: APOC2 is an inhibitor of lipoprotein lipase activity.",
                2,
                "Assertion true—APOC2 loss mimics LPL deficiency; reason false—APOC2 activates LPL; APOC3 inhibits LPL.",
                ref(
                    "Apolipoproteins C1, C2, and C3",
                    "Humans with biallelic loss-of-function mutations of APOC2, which is extremely rare, have severe hypertriglyceridemia, mimicking LPL deficiency.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Chylomicronemia Syndrome",
                "Assertion: Severe hypertriglyceridemia can cause acute pancreatitis.",
                "Reason: Pancreatitis only occurs when triglycerides are below 200 mg/dL.",
                2,
                "Assertion true—TG-induced pancreatitis rises with levels >1000 mg/dL; reason false—risk increases at high, not low, TG.",
                ref(
                    "Chylomicronemia Syndrome",
                    "However, by far the most serious consequence of severe hypertriglyceridemia is acute pancreatitis",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Omega-3 Fatty Acids",
                "Assertion: Icosapent ethyl reduced coronary events in the REDUCE-IT trial.",
                "Reason: REDUCE-IT used a combined EPA and DHA preparation stopped for futility.",
                2,
                "Assertion true—icosapent ethyl (EPA alone) showed benefit; reason false—the futility trial used EPA+DHA, not icosapent ethyl.",
                ref(
                    "Omega-3 Fatty Acids",
                    "Importantly, a study using a similar design but with an agent that contained both EPA and DHA was stopped early for futility.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "Tangier Disease",
                "Assertion: Tangier disease causes near absence of HDL-C.",
                "Reason: Tangier disease results from CETP overactivity.",
                2,
                "Assertion true—ABCA1 loss abolishes HDL; reason false—Tangier is ABCA1 deficiency, not CETP excess.",
                ref(
                    "Tangier Disease",
                    "Although affected individuals have a near absence of HDL-C due to the inability to transport cellular FC to APOA1",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Hypothyroidism",
                "Assertion: Uncontrolled hypothyroidism causes hypercholesterolemia.",
                "Reason: Hypothyroidism increases hepatic LDL receptor number.",
                2,
                "Assertion true—hypothyroidism raises LDL and TG; reason false—it reduces LDL receptor expression.",
                ref(
                    "Hypothyroidism",
                    "Mechanisms include a reduction in LDL receptors, reduced cholesterol  $ 7\\alpha $-hydroxylase, low CETP activity, and decreased LPL.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Patient Selection and Treatment Goals",
                "Assertion: The adage 'the lower the LDL, the better' guides treatment in high-risk patients.",
                "Reason: Recent trials show no benefit from LDL-C below 70 mg/dL.",
                2,
                "Assertion true—aggressive LDL lowering regresses plaque; reason false—trials support benefit below 70 mg/dL including <50 mg/dL.",
                ref(
                    "Hypercholesterolemia and Atherosclerosis",
                    "Thus, the adage that “the lower the LDL, the better” is now the guideline for treatment goals in high-risk patients.",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Secondary Forms of Hyper- and Dyslipoproteinemia",
                "Assertion: Treating underlying diabetes can improve diabetic dyslipidemia.",
                "Reason: Diabetes causes dyslipidemia solely through CETP deficiency.",
                2,
                "Assertion true—glycemic control improves TG and particle profile; reason false—diabetes dyslipidemia involves VLDL overproduction and impaired LPL, not CETP loss.",
                ref(
                    "Diabetes Mellitus",
                    "Although patients with diabetes do not have increased LDL-C compared with age- and sex-matched controls, improved diabetes control can be associated with reduced LDL-C levels and, importantly, reduced numbers of atherogenic particles.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "41",
        "title": "Disorders of Lipoprotein Metabolism",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Alan Chait, Joseph L. Witztum, and Henry N. Ginsberg",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_41_Disorders_of_Lipoprotein_Metabolism.md",
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
