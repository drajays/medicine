#!/usr/bin/env python3
"""Generate Williams 15e module w15-44 — The Immunoendocrinopathy Syndromes."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_endo_esap_modules import ar, mcq, note, ref, tf  # noqa: E402

PREFIX = "w15-44"
PORTAL_DATA = ROOT / "endo" / "data"
MASTER_DATA = Path("/Users/dr.ajayshukla/endo_masterapp/data")
OUT_NAME = "w15-44_The_Immunoendocrinopathy_Syndromes.json"


def build() -> dict:
    p = PREFIX
    items: list[dict] = []

    # --- Notes (26; all Why/How) ---
    items.extend(
        [
            note(
                f"{p}-n1",
                "KEY POINTS",
                "Why recognizing polyendocrine associations speeds diagnosis",
                "Endocrine autoimmune diseases cluster; awareness of these links prompts earlier detection of additional component disorders.",
                ref(
                    "KEY POINTS",
                    "Endocrine diseases may occur together, and understanding of these associations can lead to earlier diagnosis of additional disorders.",
                ),
            ),
            note(
                f"{p}-n2",
                "KEY POINTS",
                "How rare immunoendocrinopathy syndromes inform immunology",
                "Studying APS-I, IPEX, and related disorders has uncovered genetic bases and defined critical immune tolerance pathways.",
                ref(
                    "KEY POINTS",
                    "Studies of these disorders have uncovered the genetic basis for these rare syndromes and have helped to define important immune pathways.",
                ),
            ),
            note(
                f"{p}-n3",
                "Introduction",
                "Why APS-I and APS-II differ in inheritance and genetics",
                "APS-I is autosomal recessive with AIRE mutations; APS-II is polygenic with dominant HLA-region susceptibility and adult onset.",
                ref(
                    "Introduction",
                    "Autoimmune polyendocrine syndrome type I (APS-I) is a rare disorder with autosomal-recessive inheritance that is caused by defects in the autoimmune regulator (AIRE) gene.",
                ),
            ),
            note(
                f"{p}-n4",
                "Introduction",
                "How APS-II encompasses APS-III and APS-IV clinically",
                "This chapter groups Addison-plus-diabetes/thyroid (APS-II), thyroid-plus-other-autoimmunity (APS-III), and other combinations (APS-IV) under APS-II for simplicity.",
                ref(
                    "Introduction",
                    "For purposes of simplicity in this chapter, APS-II encompasses what some clinicians divide into APS-II (Addison disease plus type 1 diabetes or thyroid autoimmunity), APS-III (thyroid autoimmunity plus other autoimmune diseases, not Addison disease or type 1 diabetes), and APS-IV (two or more other organ-specific autoimmune disorders).",
                ),
            ),
            note(
                f"{p}-n5",
                "Introduction",
                "Why Schmidt syndrome is historical nomenclature for APS-II",
                "Schmidt syndrome, polyglandular autoimmune disease, and related terms all describe the same overlapping APS-II spectrum including nonendocrine autoimmunity.",
                ref(
                    "Introduction",
                    "APS-II has also been known by various other names, including Schmidt syndrome, polyglandular autoimmune disease, polyglandular failure syndrome, organ-specific autoimmune disease, and polyendocrinopathy diabetes.",
                ),
            ),
            note(
                f"{p}-n6",
                "Autoimmunity Primer",
                "How FOXP3+ Tregs maintain peripheral tolerance",
                "CD4+/CD25high FOXP3-expressing regulatory T cells actively suppress autoreactive T cells; FOXP3 loss causes neonatal fulminant autoimmunity (IPEX).",
                ref(
                    "Autoimmunity Primer",
                    "Deletion of this transcription factor leads to fulminant autoimmunity in neonates (e.g., neonatal type 1 diabetes and enteropathy), often resulting in death within the first year of life (IPEX syndrome; see later discussion).",
                ),
            ),
            note(
                f"{p}-n7",
                "Autoimmunity Primer",
                "Why CTLA4 and PD1 are brakes on autoimmunity",
                "CTLA4 competes with CD28 for CD80/CD86; PD1 delivers inhibitory signals on chronically activated T cells—blockade in cancer therapy can trigger endocrine autoimmunity.",
                ref(
                    "Autoimmunity Primer",
                    "The importance of both PD1 and CTLA4 in peripheral tolerance is underscored in knockout mouse models that develop spontaneous multiorgan autoimmunity and in cancer patients treated with antibodies that block their activity where many of these patients develop autoimmune complications (see later discussion).",
                ),
            ),
            note(
                f"{p}-n8",
                "Genetic Associations",
                "How shared HLA loci explain overlapping autoimmunity",
                "DR3-DQ2/DR4-DQ8 confers extreme type 1 diabetes risk; DR3-DQ2 links celiac and thyroid disease; DRB1*0404 associates with Addison disease.",
                ref(
                    "Genetic Associations",
                    "For example, the highest-risk HLA genotype for type 1 diabetes is DR3-DQ2, DR4-DQ8 (DQ8 = DQA1*0301-DQB1*0302).",
                ),
            ),
            note(
                f"{p}-n9",
                "Genetic Associations",
                "Why AIRE mutations cause APS-I but rarely sporadic Addison",
                "AIRE defects are specific to APS-I; AIRE mutations are exceedingly rare in non-APS-I Addison disease.",
                ref(
                    "Genetic Associations",
                    "Analysis of mutations of the AIRE gene indicates that it generally does not play a role in APS-II or sporadic Addison disease, with 1 (1.1%) in 90 patients with Addison disease (non-APS-I) and 1 (0.2%) in 576 control subjects having AIRE mutations.",
                ),
            ),
            note(
                f"{p}-n10",
                "Development of Organ-Specific Autoimmunity",
                "How organ-specific autoantibodies precede clinical disease",
                "Highly specific autoantibodies (GAD, IA2, ZnT8, 21-hydroxylase, tTG) appear years before gland failure and stratify risk for additional autoimmunity.",
                ref(
                    "Development of Organ-Specific Autoimmunity",
                    "Organ-specific autoantibodies (identified with appropriate assays) are rarely present (approximately 1 in 100) in the general population and identify a subset of people who are at greater risk for clinical disease.",
                ),
            ),
            note(
                f"{p}-n11",
                "Autoimmune Polyendocrine Syndrome Type I",
                "Why APS-I triad is candidiasis, hypoparathyroidism, and Addison",
                "APECED classically combines mucocutaneous candidiasis with autoimmune hypoparathyroidism and Addison disease—features rare in APS-II.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "APS-I (Mendelian Inheritance in Man [MIM] 240300), also known as autoimmune polyendocrinopathy-candidiasis-ectodermal dystrophy, or APECED, is characterized by the classic triad of mucocutaneous candidiasis, autoimmune hypoparathyroidism, and Addison disease, which form three of the most common components of the disorder.",
                ),
            ),
            note(
                f"{p}-n12",
                "Autoimmune Polyendocrine Syndrome Type I",
                "How APS-I demands lifelong surveillance",
                "Component disorders accrue over decades; early childhood candidiasis may precede endocrinopathies by many years.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "Decades can elapse between the diagnosis of one disorder and the onset of another in the same patient. Consequently, lifelong follow-up is important to allow early detection of additional components.",
                ),
            ),
            note(
                f"{p}-n13",
                "Genetics",
                "Why AIRE promotes thymic expression of tissue self-antigens",
                "AIRE is a thymic transcriptional activator driving expression of thousands of peripheral TSAs, enabling negative selection of autoreactive T cells.",
                ref(
                    "Genetics",
                    "Thus, Aire appears to act as a transcriptional activator that promotes the expression of a wide array of TSAs in the thymus to promote central tolerance (Fig. 44.4).",
                ),
            ),
            note(
                f"{p}-n14",
                "Diagnosis",
                "How anti-interferon antibodies screen for APS-I",
                "Anti-IFNα and anti-IFNω antibodies are present in nearly all APS-I patients regardless of age and can distinguish APS-I from other polyautoimmunity.",
                ref(
                    "Diagnosis",
                    "Autoantibodies against IFNα and IFNω have been identified in almost 100% of subjects with APS-I, regardless of age at screening.",
                ),
            ),
            note(
                f"{p}-n15",
                "Diagnosis",
                "Why Th17 cytokine autoantibodies explain candidiasis in APS-I",
                "Autoantibodies to IL-17A, IL-17F, and IL-22 impair Th17 effector function, mirroring IL-17 receptor defects and increasing Candida susceptibility.",
                ref(
                    "Diagnosis",
                    "Thus, it appears that the Candida susceptibility in APS-I may be due to an autoimmune response against this effector cytokine family.",
                ),
            ),
            note(
                f"{p}-n16",
                "Autoimmune Polyendocrine Syndrome Type II",
                "How APS-II defines overlapping adult polyautoimmunity",
                "APS-II requires two or more of Addison, Graves, autoimmune thyroiditis, type 1A diabetes, hypogonadism, myasthenia gravis, or celiac disease—with female predominance.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "APS-II (MIM 269200) is defined by the occurrence in the same patient of two or more of the following: primary adrenal insufficiency (Addison disease), Graves disease, autoimmune thyroiditis, type 1A diabetes, primary hypogonadism, myasthenia gravis, and celiac disease.",
                ),
            ),
            note(
                f"{p}-n17",
                "Autoimmune Polyendocrine Syndrome Type II",
                "Why type 1 diabetes mandates thyroid and celiac screening",
                "Thyroid peroxidase antibodies affect 10–20% of T1D children; tTG antibodies occur in 10–12%, with higher rates in HLA-DQ2 carriers.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "With the identification of tTG as the major endomysial autoantigen of celiac disease, radioimmunoassays were developed and demonstrated that 10% to 12% of patients with type 1 diabetes have tTG autoantibodies.",
                ),
            ),
            note(
                f"{p}-n18",
                "Diagnosis",
                "How 21-hydroxylase autoantibodies predict Addison in APS-II",
                "Recombinant 21-hydroxylase assays are highly specific; positive antibodies warrant annual ACTH and cosyntropin testing before cortisol failure.",
                ref(
                    "Diagnosis",
                    "Adrenal autoantibodies reacting with recombinant 21-hydroxylase usually precede the development of Addison disease.",
                ),
            ),
            note(
                f"{p}-n19",
                "Therapy",
                "Why adrenal function must be assessed before levothyroxine in APS-II",
                "Thyroxine can unmask or precipitate addisonian crisis in untreated adrenal insufficiency; falling insulin needs may be the earliest adrenal clue in T1D.",
                ref(
                    "Therapy",
                    "Thyroxine therapy can precipitate a life-threatening addisonian crisis in a patient with untreated adrenal insufficiency and hypothyroidism.",
                ),
            ),
            note(
                f"{p}-n20",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "Why FOXP3 mutations cause IPEX",
                "X-linked FOXP3 loss abolishes regulatory T-cell generation, producing neonatal T1D, severe enteropathy, dermatitis, and early death without HSCT.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "IPEX (MIM 340790, MIM 300292), first described in 1982, is a rare, X-linked recessive disorder that is characterized by immune dysregulation and results in multiple autoimmune diseases and early death (see Fig. 44.4). It is caused by mutations of the FOXP3 gene.",
                ),
            ),
            note(
                f"{p}-n21",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "How HSCT is definitive therapy for IPEX",
                "Hematopoietic stem cell transplantation reverses enteropathy and other autoimmune components, though established diabetes and thyroid disease often persist.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "Definitive treatment is with hematopoietic stem cell transplantation (HSCT). HSCT results in reversal of the enteropathy and other autoimmune components.",
                ),
            ),
            note(
                f"{p}-n22",
                "Anti-Insulin Receptor Autoantibodies",
                "How type B insulin resistance presents clinically",
                "Anti-insulin receptor antibodies cause profound insulin resistance, acanthosis nigricans, variable hyper- or hypoglycemia, and often coexisting autoimmune disease.",
                ref(
                    "Anti-Insulin Receptor Autoantibodies",
                    "In this rarely reported disorder (<100 patients), also called type B insulin resistance or acanthosis nigricans, insulin resistance is caused by the presence of anti-insulin receptor antibodies and anti-insulin antibodies.",
                ),
            ),
            note(
                f"{p}-n23",
                "POEMS Syndrome",
                "Why POEMS combines neuropathy, organomegaly, and endocrinopathy",
                "POEMS features progressive polyneuropathy, hepatosplenomegaly, plasma cell dyscrasia, sclerotic bone lesions, diabetes, and gonadal failure.",
                ref(
                    "POEMS Syndrome",
                    "The components of the multisystem disorder POEMS (plasma cell dyscrasia with polyneuropathy, organomegaly, endocrinopathy, monoclonal plasma cell disorder, and skin changes), also known as Crow-Fukase syndrome (MIM 192240), consist of diabetes mellitus (3%–36% of patients), primary gonadal failure (55%–89% of patients), plasma cell dyscrasia, sclerotic bone lesions, and neuropathy.",
                ),
            ),
            note(
                f"{p}-n24",
                "Environmental Triggers",
                "How immune checkpoint inhibitors induce endocrine autoimmunity",
                "Anti-CTLA4 and anti-PD1 therapies can trigger thyroiditis, type 1 diabetes, lymphocytic hypophysitis, and adrenalitis in treated cancer patients.",
                ref(
                    "Environmental Triggers",
                    "These autoimmune complications are broad but now include the induction of endocrine-related autoimmunity including thyroiditis, type 1 diabetes, lymphocytic hypophysitis, and adrenalitis.",
                ),
            ),
            note(
                f"{p}-n25",
                "Paraneoplastic Autoimmune Hypophysitis",
                "How checkpoint inhibitor hypophysitis causes ACTH deficiency",
                "PD1/PDL1 inhibitor–related hypophysitis selectively impairs ACTH secretion, producing secondary adrenal insufficiency—sometimes via paraneoplastic POMC autoimmunity.",
                ref(
                    "Paraneoplastic Autoimmune Hypophysitis",
                    "In immune checkpoint inhibitor–related hypophysitis, PD1/PDL1 inhibitor–related hypophysitis causes a specific defect in ACTH secretion and secondary adrenal insufficiency.",
                ),
            ),
            note(
                f"{p}-n26",
                "Conclusion",
                "How APS-I and IPEX teach central and peripheral tolerance",
                "Rare monogenic disorders illuminate thymic peripheral antigen expression and regulatory T-cell biology applicable to common autoimmune endocrinopathies.",
                ref(
                    "Conclusion",
                    "Through the study of rare disorders such as APS-I and IPEX, the processes of thymic expression of peripheral antigens and development of regulatory T cells are beginning to be defined.",
                ),
            ),
        ]
    )

    # --- MCQs (26) ---
    items.extend(
        [
            mcq(
                f"{p}-m1",
                "Autoimmune Polyendocrine Syndrome Type I",
                "A 6-year-old with chronic oral candidiasis, hypocalcemia, and primary adrenal insufficiency has a sibling with similar findings. Most likely diagnosis?",
                [
                    "Autoimmune polyendocrine syndrome type I (APECED) with AIRE mutation",
                    "Autoimmune polyendocrine syndrome type II (Schmidt syndrome)",
                    "IPEX syndrome with FOXP3 mutation",
                    "POEMS syndrome from plasma cell dyscrasia",
                ],
                0,
                "Childhood candidiasis plus hypoparathyroidism and Addison with sibling involvement defines autosomal-recessive APS-I/APECED.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "APS-I is characteristically recognized in early childhood. Infants can present with chronic or recurrent mucocutaneous candidiasis in the first year of life, followed by hypoparathyroidism and Addison disease, but new components can develop at any age.",
                ),
            ),
            mcq(
                f"{p}-m2",
                "Genetics",
                "AIRE knockout mice develop multiorgan lymphocytic infiltrates. Primary mechanism?",
                [
                    "Decreased thymic expression of peripheral tissue-specific self-antigens",
                    "Gain-of-function FOXP3 enhancing regulatory T cells",
                    "Excess insulin receptor autoantibody production",
                    "Mitochondrial DNA deletion in endocrine tissues",
                ],
                0,
                "Aire promotes thymic TSA expression; defective Aire allows autoreactive T cells to escape negative selection.",
                ref(
                    "Genetics",
                    "Detailed analyses of antigen-presenting epithelial cells in the thymus of Aire knockout mice have shown that these cells have decreased expression of peripheral tissue-specific self-antigens (TSAs)",
                ),
            ),
            mcq(
                f"{p}-m3",
                "Diagnosis",
                "An adolescent with multiple autoimmune endocrinopathies tests positive for anti-IFNα and anti-IFNω antibodies. Next step?",
                [
                    "Sequence the AIRE gene to confirm APS-I",
                    "Diagnose APS-II and screen only for HLA-DR3",
                    "Start rituximab for type B insulin resistance",
                    "Order VEGF for POEMS syndrome",
                ],
                0,
                "Anti-interferon antibodies are present in ~100% of APS-I patients and are proposed to screen polyautoimmune patients for APS-I.",
                ref(
                    "Diagnosis",
                    "it has been proposed to use this autoantibody to screen subjects with multiple autoimmune diseases for APS-I.",
                ),
            ),
            mcq(
                f"{p}-m4",
                "Autoimmune Polyendocrine Syndrome Type II",
                "A 35-year-old woman with Addison disease is found to have autoimmune thyroiditis. This combination best fits:",
                [
                    "Autoimmune polyendocrine syndrome type II",
                    "Autoimmune polyendocrine syndrome type I (APECED)",
                    "IPEX syndrome",
                    "Kearns-Sayre syndrome",
                ],
                0,
                "APS-II commonly combines Addison with autoimmune thyroid disease and/or type 1 diabetes in adult women.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "Among 224 patients with Addison disease and APS-II reported by Neufeld and colleagues, type 1 diabetes and autoimmune thyroid disease were the most common coexisting conditions (52% and 69% of patients, respectively).",
                ),
            ),
            mcq(
                f"{p}-m5",
                "Introduction",
                "A patient has autoimmune thyroiditis plus vitiligo without Addison disease or type 1 diabetes. Per this chapter's taxonomy, this is classified as:",
                [
                    "APS-III, grouped under the APS-II spectrum",
                    "APS-I with AIRE mutation",
                    "IPEX with FOXP3 mutation",
                    "Isolated Graves disease only—no polyendocrine label",
                ],
                0,
                "APS-III (thyroid plus other autoimmunity without Addison/T1D) is encompassed within APS-II in this chapter.",
                ref(
                    "Introduction",
                    "APS-III (thyroid autoimmunity plus other autoimmune diseases, not Addison disease or type 1 diabetes)",
                ),
            ),
            mcq(
                f"{p}-m6",
                "Introduction",
                "A patient has myasthenia gravis and pernicious anemia without classic endocrine autoimmunity. Classification per APS taxonomy?",
                [
                    "APS-IV (two or more organ-specific autoimmune disorders)",
                    "APS-I with mucocutaneous candidiasis required",
                    "POEMS syndrome",
                    "Wolfram syndrome (DIDMOAD)",
                ],
                0,
                "APS-IV describes two or more organ-specific autoimmune disorders outside the classic APS-II core—grouped under APS-II here.",
                ref(
                    "Introduction",
                    "APS-IV (two or more other organ-specific autoimmune disorders).",
                ),
            ),
            mcq(
                f"{p}-m7",
                "Genetic Associations",
                "A child inherits DR3-DQ2 and DR4-DQ8 from a sibling with type 1 diabetes. Approximate risk for developing autoimmunity by age 12?",
                [
                    "Greater than 75% risk for autoimmunity; greater than 50% for diabetes",
                    "Less than 1%—HLA has no predictive value",
                    "100% certainty of diabetes by age 5",
                    "Protected from all autoimmune disease",
                ],
                0,
                "Shared highest-risk HLA genotype with an affected sibling confers >75% autoimmunity and >50% diabetes risk by age 12.",
                ref(
                    "Genetic Associations",
                    "children who inherited the same DR3-DQ2, DR4-DQ8 as a sibling with type 1 diabetes are at greater than 75% risk for development of autoimmunity by age 12 years and at greater than 50% risk of developing diabetes by 12 years.",
                ),
            ),
            mcq(
                f"{p}-m8",
                "Development of Organ-Specific Autoimmunity",
                "TrialNet screens first-degree relatives of type 1 diabetes patients. Rationale for antibody screening?",
                [
                    "Multiple diabetes-related autoantibodies increase progression risk before hyperglycemia",
                    "Autoantibodies appear only after clinical diabetes onset",
                    "ICA testing replaces all molecular HLA typing",
                    "ZnT8 antibodies are present in 90% of the general population",
                ],
                0,
                "Organ-specific autoantibodies precede disease; risk rises with number and persistence of positive antibodies.",
                ref(
                    "Development of Organ-Specific Autoimmunity",
                    "This approach has been employed in studies such as TrialNet for type 1 diabetes to screen first-degree relatives of patients with type 1 diabetes for diabetes-related autoantibodies. In this and other cohorts, risk for development of diabetes increases with the number of autoantibodies and their persistence.",
                ),
            ),
            mcq(
                f"{p}-m9",
                "Autoimmune Polyendocrine Syndrome Type II",
                "A patient with type 1 diabetes has positive 21-hydroxylase autoantibodies but normal morning cortisol. Best monitoring strategy?",
                [
                    "Annual basal ACTH with cosyntropin stimulation if indicated",
                    "No further testing—antibodies are not predictive",
                    "Immediate bilateral adrenalectomy",
                    "Start levothyroxine empirically",
                ],
                0,
                "21-hydroxylase antibodies precede Addison; annual ACTH and dynamic testing detects impending adrenal failure.",
                ref(
                    "Diagnosis",
                    "Annual screening with a basal level of corticotropin with follow-up cosyntropin stimulation testing is an effective strategy for identifying adrenal insufficiency in patients with 21-hydroxylase autoantibodies.",
                ),
            ),
            mcq(
                f"{p}-m10",
                "Autoimmune Polyendocrine Syndrome Type II",
                "A 14-year-old with type 1 diabetes has rising TSH and positive thyroid peroxidase antibodies. Long-term outcome data suggest:",
                [
                    "High likelihood of eventual hypothyroidism with prolonged follow-up",
                    "Antibodies always resolve without thyroid dysfunction",
                    "Graves hyperthyroidism is the only possible progression",
                    "Thyroid disease never coexists with type 1 diabetes",
                ],
                0,
                "After >15 years follow-up, 80% of T1D patients with thyroid peroxidase antibodies became hypothyroid.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "One study showed that after follow-up for more than 15 years, 80% of patients with thyroid peroxidase autoantibodies and type 1 diabetes became hypothyroid.",
                ),
            ),
            mcq(
                f"{p}-m11",
                "Autoimmune Polyendocrine Syndrome Type II",
                "A type 1 diabetes patient has high-titer tTG antibodies. Next step per APS-II management?",
                [
                    "Confirm on repeat assay and pursue small bowel biopsy if positive",
                    "Start gluten challenge without antibody confirmation",
                    "Diagnose POEMS and measure VEGF",
                    "Treat with high-dose fluconazole for candidiasis",
                ],
                0,
                "Positive tTG warrants repeat testing and biopsy confirmation before instituting a gluten-free diet.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "If the results are positive and are confirmed on repeat assay, small bowel biopsy to document celiac disease is warranted, with institution of a gluten-free diet if the disease is present.",
                ),
            ),
            mcq(
                f"{p}-m12",
                "Therapy",
                "A patient with APS-II has untreated adrenal insufficiency and new autoimmune hypothyroidism. Before starting levothyroxine you must:",
                [
                    "Evaluate and treat adrenal insufficiency first",
                    "Start metformin for insulin resistance",
                    "Administer checkpoint inhibitor therapy",
                    "Proceed with thyroidectomy",
                ],
                0,
                "Thyroxine without glucocorticoid replacement can precipitate fatal addisonian crisis.",
                ref(
                    "Therapy",
                    "Therefore, it is necessary to evaluate adrenal function in all hypothyroid patients in whom the syndrome is suspected before instituting such therapy.",
                ),
            ),
            mcq(
                f"{p}-m13",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "A male infant develops neonatal diabetes, intractable diarrhea, and eczema. Definitive long-term therapy?",
                [
                    "Hematopoietic stem cell transplantation",
                    "Lifelong fluconazole for candidiasis only",
                    "Thiamine for Wolfram syndrome",
                    "Radiation to sclerotic bone lesions",
                ],
                0,
                "IPEX is caused by FOXP3 mutations; HSCT reverses enteropathy and immune dysregulation though diabetes may persist.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "Definitive treatment is with hematopoietic stem cell transplantation (HSCT).",
                ),
            ),
            mcq(
                f"{p}-m14",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "FOXP3 is expressed primarily in which T-cell population?",
                [
                    "CD4+/CD25+ regulatory T cells",
                    "CD8+ cytotoxic T cells only",
                    "B lymphocytes producing IgM",
                    "Natural killer cells without TCR",
                ],
                0,
                "FOXP3 is the transcription factor defining CD4+/CD25+ regulatory T cells that suppress other T cells.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "FOXP3 has been shown to be expressed in CD4 $ ^{+} $/CD25 $ ^{+} $ regulatory T cells.",
                ),
            ),
            mcq(
                f"{p}-m15",
                "Anti-Insulin Receptor Autoantibodies",
                "A woman with SLE has extreme insulin resistance requiring >10,000 U insulin/day, acanthosis nigricans, and episodic hypoglycemia. Diagnosis?",
                [
                    "Type B insulin resistance from anti-insulin receptor antibodies",
                    "Type A insulin resistance from INSR mutation",
                    "Factitious insulin administration only",
                    "Insulinoma with Whipple triad",
                ],
                0,
                "Type B insulin resistance features anti-receptor antibodies, profound resistance, acanthosis, and often coexisting autoimmune disease.",
                ref(
                    "Anti-Insulin Receptor Autoantibodies",
                    "Approximately one-third of patients with these antibodies have an associated autoimmune illness such as SLE or Sjögren syndrome.",
                ),
            ),
            mcq(
                f"{p}-m16",
                "Anti-Insulin Receptor Autoantibodies",
                "First-line immunotherapy regimen for type B insulin resistance per NIH experience?",
                [
                    "Rituximab with cyclophosphamide and pulse corticosteroids",
                    "Metformin monotherapy only",
                    "Levothyroxine suppression",
                    "Gluten-free diet",
                ],
                0,
                "NIH protocol using rituximab, cyclophosphamide, and pulse steroids has successfully treated this rare disorder.",
                ref(
                    "Anti-Insulin Receptor Autoantibodies",
                    "A treatment regimen developed at the National Institutes of Health that includes rituximab that targets B lymphocytes with cyclophosphamide and pulse corticosteroids has been used successfully to treat this rare disorder.",
                ),
            ),
            mcq(
                f"{p}-m17",
                "POEMS Syndrome",
                "A 58-year-old presents with progressive sensorimotor neuropathy, hepatosplenomegaly, hyperpigmentation, and λ-chain gammopathy. Likely diagnosis?",
                [
                    "POEMS syndrome (Crow-Fukase)",
                    "APS-I with AIRE mutation",
                    "IPEX syndrome",
                    "Autoimmune lymphoproliferative syndrome from CTLA4 haploinsufficiency only",
                ],
                0,
                "POEMS combines polyneuropathy, organomegaly, endocrinopathy, monoclonal plasma cell disorder, and skin changes.",
                ref(
                    "POEMS Syndrome",
                    "Patients usually present with severe progressive sensorimotor polyneuropathy, hepatosplenomegaly, lymphadenopathy, and hyperpigmentation.",
                ),
            ),
            mcq(
                f"{p}-m18",
                "POEMS Syndrome",
                "Elevated vascular endothelial growth factor in POEMS suggests:",
                [
                    "A pathogenic cytokine target correlating with disease activity",
                    "Exclusive mitochondrial DNA deletion",
                    "AIRE-mediated thymic tolerance failure",
                    "FOXP3 regulatory T-cell expansion",
                ],
                0,
                "VEGF levels correlate with POEMS disease state and fall with immunosuppressive therapy.",
                ref(
                    "POEMS Syndrome",
                    "In several studies, elevated levels of vascular endothelial growth factor (VEGF) correlated with the disease state, and treatment with immunosuppressive agents reduced the symptoms of the disease and the levels of VEGF, suggesting that this growth factor plays a role in the disease.",
                ),
            ),
            mcq(
                f"{p}-m19",
                "Environmental Triggers",
                "A melanoma patient on pembrolizumab develops fatigue, hypotension, and hyponatremia. Most likely immune-related adverse event?",
                [
                    "Checkpoint inhibitor–related hypophysitis with ACTH deficiency",
                    "Type B insulin resistance from anti-receptor antibodies",
                    "APS-I with mucocutaneous candidiasis",
                    "Kearns-Sayre mitochondrial syndrome",
                ],
                0,
                "PD1/PDL1 inhibitor hypophysitis causes isolated ACTH deficiency and secondary adrenal insufficiency.",
                ref(
                    "Paraneoplastic Autoimmune Hypophysitis",
                    "In immune checkpoint inhibitor–related hypophysitis, PD1/PDL1 inhibitor–related hypophysitis causes a specific defect in ACTH secretion and secondary adrenal insufficiency.",
                ),
            ),
            mcq(
                f"{p}-m20",
                "Environmental Triggers",
                "A patient receiving ipilimumab and nivolumab develops new-onset insulin-dependent diabetes. Mechanism class?",
                [
                    "Immune checkpoint blockade–induced endocrine autoimmunity",
                    "POEMS-related plasma cell cytokine excess only",
                    "Wolframin ER-stress β-cell apoptosis",
                    "Methimazole-associated Hirata disease",
                ],
                0,
                "Checkpoint inhibitors blocking CTLA4 or PD1 can induce thyroiditis, T1D, hypophysitis, and adrenalitis.",
                ref(
                    "Environmental Triggers",
                    "Immune checkpoint blockade is now an approved treatment approach for several cancers, and these antibodies that block CTLA4 or PD1 on T cells have both been associated with the induction of autoimmune complications in a subset of patients.",
                ),
            ),
            mcq(
                f"{p}-m21",
                "Paraneoplastic Autoimmune Hypophysitis",
                "A thymoma patient develops combined GH, prolactin, and TSH deficiency with anti-PIT-1 antibodies. Mechanism?",
                [
                    "Ectopic PIT-1 expression in tumor breaks tolerance (paraneoplastic hypophysitis)",
                    "AIRE mutation causing APS-I",
                    "Anti-insulin receptor antibody blockade",
                    "IgA deficiency from APS-II",
                ],
                0,
                "Tumor ectopic PIT-1 expression evokes anti-PIT-1 immunity destroying PIT-1–expressing anterior pituitary cells.",
                ref(
                    "Paraneoplastic Autoimmune Hypophysitis",
                    "Thymoma and other malignancies that ectopically express PIT-1 caused the breakdown of immune tolerance against PIT-1, resulting in a production of circulating anti-PIT-1 antibody and cytotoxic T cells (CTLs) that react with PIT-1 expressing anterior pituitary cells.",
                ),
            ),
            mcq(
                f"{p}-m22",
                "Thymic Tumors",
                "A patient with thymoma develops myasthenia gravis and autoimmune thyroid disease. This parallels:",
                [
                    "APS-II spectrum disorders associated with thymomas",
                    "APS-I with AIRE mutations only",
                    "IPEX with FOXP3 mutations",
                    "Wolfram syndrome DIDMOAD",
                ],
                0,
                "Thymoma-associated illnesses resemble APS-II though with different incidences; AIRE dysregulation may contribute.",
                ref(
                    "Thymic Tumors",
                    "The illnesses associated with thymomas are similar to those seen in APS-II, although the incidence of specific disorders is different.",
                ),
            ),
            mcq(
                f"{p}-m23",
                "Autoimmune Polyendocrine Syndrome Type I",
                "Chronic oral candidiasis in APS-I is best explained by:",
                [
                    "Autoantibodies against IL-17A, IL-17F, and IL-22 impairing Th17 immunity",
                    "Excess insulin receptor autoantibody activity",
                    "Mitochondrial DNA deletions in Candida",
                    "Hypergastrinemia from gastrinoma",
                ],
                0,
                "APS-I patients harbor autoantibodies to Th17 cytokines, impairing antifungal effector function.",
                ref(
                    "Diagnosis",
                    "it has also been shown that many APS-I subjects also harbor autoantibodies to IL17A, IL17F, and IL22.",
                ),
            ),
            mcq(
                f"{p}-m24",
                "Autoimmune Polyendocrine Syndrome Type I",
                "A child with APS-I has Howell-Jolly bodies on smear. Management priority?",
                [
                    "Pneumococcal vaccination and consider antibiotic prophylaxis",
                    "Immediate total thyroidectomy",
                    "High-dose checkpoint inhibitor therapy",
                    "VEGF-targeted therapy for POEMS",
                ],
                0,
                "Asplenia occurs in up to 15% of APS-I patients; pneumococcal immunization and prophylactic antibiotics if response inadequate.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "If asplenia is identified, immunization with polyvalent pneumococcal vaccine should be administered, and follow-up antibody titers should be obtained. If an adequate response is not produced, daily prophylactic antibiotics may be necessary.",
                ),
            ),
            mcq(
                f"{p}-m25",
                "Diagnosis",
                "In type 1 diabetes, the four most informative autoantibody assays target:",
                [
                    "Insulin, GAD65, ICA512/IA2, and ZnT8",
                    "21-hydroxylase and 17α-hydroxylase only",
                    "Anti-IFNα and anti-IFNω only",
                    "PIT-1 and POMC exclusively",
                ],
                0,
                "Modern T1D risk stratification uses insulin, GAD65, IA2, and ZnT8 autoantibody assays.",
                ref(
                    "Diagnosis",
                    "In type 1 diabetes, the four most informative assays identify autoantibodies reacting with insulin, GAD65, ICA512/IA2, and ZnT8.",
                ),
            ),
            mcq(
                f"{p}-m26",
                "Other Polyendocrine Deficiency Autoimmune Syndromes",
                "A patient with APS-II develops progressive muscle stiffness and spasms. Reported association in Table 44.3?",
                [
                    "Stiff-man syndrome (rare APS-II component)",
                    "POEMS polyneuropathy as mandatory feature",
                    "IPEX enteropathy",
                    "Wolfram optic atrophy",
                ],
                0,
                "Stiff-man syndrome is listed among rare reported disorders in subjects with APS-II.",
                ref(
                    "Other Polyendocrine Deficiency Autoimmune Syndromes",
                    "Stiff-man syndrome",
                ),
            ),
        ]
    )

    # --- True/False (13) ---
    items.extend(
        [
            tf(
                f"{p}-t1",
                "Introduction",
                "APS-I is caused by defects in the AIRE gene with autosomal-recessive inheritance.",
                True,
                "APS-I is a rare autosomal-recessive disorder from AIRE mutations.",
                ref(
                    "Introduction",
                    "Autoimmune polyendocrine syndrome type I (APS-I) is a rare disorder with autosomal-recessive inheritance that is caused by defects in the autoimmune regulator (AIRE) gene.",
                ),
            ),
            tf(
                f"{p}-t2",
                "Introduction",
                "APS-II has a strong association with polymorphic HLA genes on chromosome 6p21.3.",
                True,
                "HLA-region genes are the unifying genetic characteristic of APS-II.",
                ref(
                    "Introduction",
                    "A unifying characteristic within APS-II is the strong association with polymorphic genes of the human leukocyte antigen (HLA) region located on the short arm of chromosome 6 (band 6p21.3).",
                ),
            ),
            tf(
                f"{p}-t3",
                "Autoimmune Polyendocrine Syndrome Type I",
                "Hypoparathyroidism and mucocutaneous candidiasis are virtually absent in APS-II compared with APS-I.",
                True,
                "Table 44.2 contrasts APS-I propensity for hypoparathyroidism and candidiasis versus APS-II features.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "Note some of the distinctions in the pattern of disease features of the two syndromes, particularly the propensity for hypoparathyroidism and candidiasis in APS-I, which is virtually absent in APS-II.",
                ),
            ),
            tf(
                f"{p}-t4",
                "Autoimmune Polyendocrine Syndrome Type I",
                "In Finnish APS-I series, all 89 patients had chronic candidiasis at some time.",
                True,
                "Perheentupa series: 100% candidiasis, 86% hypoparathyroidism, 79% Addison.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "In a series of 89 Finnish patients described by Perheentupa, all had chronic candidiasis at some time, 86% had hypoparathyroidism, and 79% had Addison disease.",
                ),
            ),
            tf(
                f"{p}-t5",
                "Diagnosis",
                "Anti-IFNα autoantibodies are present in almost 100% of APS-I subjects.",
                True,
                "Anti-interferon antibodies are highly sensitive for APS-I screening.",
                ref(
                    "Diagnosis",
                    "Autoantibodies against IFNα and IFNω have been identified in almost 100% of subjects with APS-I, regardless of age at screening.",
                ),
            ),
            tf(
                f"{p}-t6",
                "Autoimmune Polyendocrine Syndrome Type II",
                "Celiac disease is frequently observed in APS-II but is not seen in APS-I.",
                True,
                "Table 44.2 notes celiac in APS-II but not APS-I.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type I",
                    "Likewise, celiac disease is frequently observed in APS-II but is not seen in APS-I.",
                ),
            ),
            tf(
                f"{p}-t7",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "IPEX is an X-linked recessive disorder caused by FOXP3 mutations.",
                True,
                "FOXP3 loss abolishes regulatory T cells causing neonatal multiorgan autoimmunity.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "IPEX (MIM 340790, MIM 300292), first described in 1982, is a rare, X-linked recessive disorder that is characterized by immune dysregulation and results in multiple autoimmune diseases and early death (see Fig. 44.4). It is caused by mutations of the FOXP3 gene.",
                ),
            ),
            tf(
                f"{p}-t8",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "Hematopoietic stem cell transplantation generally reverses established type 1 diabetes in IPEX.",
                False,
                "HSCT reverses enteropathy and other components; established T1D and thyroid disease usually do not resolve.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "Generally, established type 1 diabetes and thyroid disease do not resolve.",
                ),
            ),
            tf(
                f"{p}-t9",
                "Anti-Insulin Receptor Autoantibodies",
                "Ketoacidosis is common despite marked hyperglycemia in type B insulin resistance.",
                False,
                "Profound insulin resistance occurs but ketoacidosis is uncommon; hypoglycemia can occur from insulin-mimetic antibody effects.",
                ref(
                    "Anti-Insulin Receptor Autoantibodies",
                    "Despite hyperglycemia and marked insulin resistance, ketoacidosis is uncommon.",
                ),
            ),
            tf(
                f"{p}-t10",
                "POEMS Syndrome",
                "POEMS patients typically present in the fifth to sixth decades with median survival about 14 years after diagnosis.",
                True,
                "POEMS is a later-onset plasma cell dyscrasia with chronic course.",
                ref(
                    "POEMS Syndrome",
                    "Patients present in the fifth to sixth decades of life and have a median survival time after diagnosis of 14 years.",
                ),
            ),
            tf(
                f"{p}-t11",
                "Environmental Triggers",
                "Immune checkpoint inhibitors can induce thyroiditis, type 1 diabetes, lymphocytic hypophysitis, and adrenalitis.",
                True,
                "Endocrine irAEs are recognized complications of anti-CTLA4 and anti-PD1 therapy.",
                ref(
                    "Environmental Triggers",
                    "These autoimmune complications are broad but now include the induction of endocrine-related autoimmunity including thyroiditis, type 1 diabetes, lymphocytic hypophysitis, and adrenalitis.",
                ),
            ),
            tf(
                f"{p}-t12",
                "Genetic Associations",
                "AIRE mutations commonly cause sporadic Addison disease in the absence of APS-I.",
                False,
                "AIRE mutations are rare in non-APS-I Addison (1.1% of 90 patients).",
                ref(
                    "Genetic Associations",
                    "Analysis of mutations of the AIRE gene indicates that it generally does not play a role in APS-II or sporadic Addison disease, with 1 (1.1%) in 90 patients with Addison disease (non-APS-I) and 1 (0.2%) in 576 control subjects having AIRE mutations.",
                ),
            ),
            tf(
                f"{p}-t13",
                "KEY POINTS",
                "Ectopic pituitary antigen presentation by tumors can cause paraneoplastic autoimmune hypophysitis.",
                True,
                "KEY POINTS define paraneoplastic hypophysitis from ectopic pituitary antigen in complicated tumors.",
                ref(
                    "KEY POINTS",
                    "Ectopic pituitary antigen presentation by the complicated tumor can cause autoimmunity against anterior pituitary cells, which is defined as paraneoplastic autoimmune hypophysitis.",
                ),
            ),
        ]
    )

    # --- Assertion-Reason (12) ---
    items.extend(
        [
            ar(
                f"{p}-ar1",
                "Introduction",
                "Assertion: APS-I is caused by AIRE gene defects with autosomal-recessive inheritance.",
                "Reason: APS-I is inherited in a polygenic pattern with HLA-DR3 and DR4 as the primary susceptibility loci.",
                2,
                "Assertion true—APS-I is AIRE-related autosomal recessive; reason false—that describes APS-II genetics.",
                ref(
                    "Introduction",
                    "Autoimmune polyendocrine syndrome type I (APS-I) is a rare disorder with autosomal-recessive inheritance that is caused by defects in the autoimmune regulator (AIRE) gene.",
                ),
            ),
            ar(
                f"{p}-ar2",
                "Autoimmunity Primer",
                "Assertion: FOXP3 is essential for CD4+/CD25+ regulatory T-cell function.",
                "Reason: FOXP3 deletion has no effect on neonatal immune tolerance.",
                2,
                "Assertion true—FOXP3 defines Tregs; reason false—FOXP3 deletion causes fulminant neonatal autoimmunity (IPEX).",
                ref(
                    "Autoimmunity Primer",
                    "The function of the population of CD4+/CD25high cells involves an active suppressive activity and relies on the transcription factor FOXP3.",
                ),
            ),
            ar(
                f"{p}-ar3",
                "Genetics",
                "Assertion: AIRE promotes expression of tissue-specific self-antigens in the thymus.",
                "Reason: AIRE knockout mice show increased thymic expression of peripheral antigens.",
                2,
                "Assertion true—Aire is a thymic transcriptional activator of TSAs; reason false—Aire knockout decreases TSA expression.",
                ref(
                    "Genetics",
                    "Aire knockout mice also spontaneously develop autoimmune features. Detailed analyses of antigen-presenting epithelial cells in the thymus of Aire knockout mice have shown that these cells have decreased expression of peripheral tissue-specific self-antigens (TSAs)",
                ),
            ),
            ar(
                f"{p}-ar4",
                "Autoimmune Polyendocrine Syndrome Type II",
                "Assertion: APS-II is more common than APS-I and preferentially affects females.",
                "Reason: APS-II has equal gender incidence with onset in infancy.",
                2,
                "Assertion true—APS-II is commoner with female preponderance and adult onset; reason false—that describes APS-I.",
                ref(
                    "Autoimmune Polyendocrine Syndrome Type II",
                    "APS-II is more common than APS-I. It occurs more often in female than in male patients, often has its onset in adulthood, and exhibits familial aggregation (see Table 44.2).",
                ),
            ),
            ar(
                f"{p}-ar5",
                "Diagnosis",
                "Assertion: 21-hydroxylase autoantibodies precede clinical Addison disease.",
                "Reason: Adrenal autoantibodies have no predictive value for future adrenal failure.",
                2,
                "Assertion true—21-hydroxylase antibodies mark preclinical Addison; reason false—antibodies are predictive and guide screening.",
                ref(
                    "Diagnosis",
                    "Adrenal autoantibodies reacting with recombinant 21-hydroxylase usually precede the development of Addison disease.",
                ),
            ),
            ar(
                f"{p}-ar6",
                "Therapy",
                "Assertion: Levothyroxine can precipitate addisonian crisis if adrenal insufficiency is untreated.",
                "Reason: Thyroid hormone replacement always improves adrenal cortisol production directly.",
                2,
                "Assertion true—thyroxine unmasks adrenal failure; reason false—thyroxine does not restore cortisol and can worsen crisis.",
                ref(
                    "Therapy",
                    "Thyroxine therapy can precipitate a life-threatening addisonian crisis in a patient with untreated adrenal insufficiency and hypothyroidism.",
                ),
            ),
            ar(
                f"{p}-ar7",
                "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                "Assertion: IPEX is caused by FOXP3 mutations on the X chromosome.",
                "Reason: FOXP3 encodes a forkhead winged-helix transcription factor expressed in regulatory T cells.",
                0,
                "Both true and linked—FOXP3 is the X-linked transcription factor whose loss abolishes Tregs in IPEX.",
                ref(
                    "Immunodysregulation Polyendocrinopathy Enteropathy X-Linked Syndrome",
                    "FOXP3 encodes a protein that is a member of the forkhead class of winged helix transcription factors (forkhead box protein 3).",
                ),
            ),
            ar(
                f"{p}-ar8",
                "Anti-Insulin Receptor Autoantibodies",
                "Assertion: Type B insulin resistance features profound insulin resistance from anti-receptor antibodies.",
                "Reason: Ketoacidosis is the typical presenting metabolic complication.",
                2,
                "Assertion true—anti-receptor antibodies cause extreme resistance; reason false—ketoacidosis is uncommon despite hyperglycemia.",
                ref(
                    "Anti-Insulin Receptor Autoantibodies",
                    "Despite hyperglycemia and marked insulin resistance, ketoacidosis is uncommon.",
                ),
            ),
            ar(
                f"{p}-ar9",
                "POEMS Syndrome",
                "Assertion: POEMS includes polyneuropathy, organomegaly, endocrinopathy, and monoclonal plasma cell disorder.",
                "Reason: POEMS is caused by AIRE mutations with autosomal-recessive inheritance.",
                2,
                "Assertion true—POEMS is a plasma cell dyscrasia syndrome; reason false—POEMS is not AIRE-related APS-I.",
                ref(
                    "POEMS Syndrome",
                    "The components of the multisystem disorder POEMS (plasma cell dyscrasia with polyneuropathy, organomegaly, endocrinopathy, monoclonal plasma cell disorder, and skin changes), also known as Crow-Fukase syndrome (MIM 192240), consist of diabetes mellitus (3%–36% of patients), primary gonadal failure (55%–89% of patients), plasma cell dyscrasia, sclerotic bone lesions, and neuropathy.",
                ),
            ),
            ar(
                f"{p}-ar10",
                "Environmental Triggers",
                "Assertion: Immune checkpoint blockade can induce endocrine autoimmunity including hypophysitis.",
                "Reason: CTLA4 and PD1 blockade has no effect on immune tolerance in cancer patients.",
                2,
                "Assertion true—checkpoint inhibitors cause thyroiditis, T1D, hypophysitis, adrenalitis; reason false—blockade breaks peripheral tolerance causing irAEs.",
                ref(
                    "Environmental Triggers",
                    "Immune checkpoint blockade is now an approved treatment approach for several cancers, and these antibodies that block CTLA4 or PD1 on T cells have both been associated with the induction of autoimmune complications in a subset of patients.",
                ),
            ),
            ar(
                f"{p}-ar11",
                "Paraneoplastic Autoimmune Hypophysitis",
                "Assertion: Anti-PIT-1 hypophysitis causes combined GH, prolactin, and TSH deficiency.",
                "Reason: PIT-1 is expressed only in tumors and never in normal anterior pituitary cells.",
                2,
                "Assertion true—anti-PIT-1 destroys PIT-1+ pituitary cells; reason false—PIT-1 is a normal pituitary transcription factor also ectopically expressed in tumors.",
                ref(
                    "Paraneoplastic Autoimmune Hypophysitis",
                    "Anti-PIT-1 hypophysitis is characterized by an acquired deficiency in GH-, PRL-, and TSH-producing pituitary cells caused by autoimmunity against a pituitary-specific transcription factor PIT-1 (POU1F1).",
                ),
            ),
            ar(
                f"{p}-ar12",
                "Development of Organ-Specific Autoimmunity",
                "Assertion: Organ-specific autoantibodies can be present years before overt endocrine disease.",
                "Reason: Autoantibodies in the general population occur in approximately 50% of adults.",
                2,
                "Assertion true—autoantibodies precede disease for years; reason false—only ~1 in 100 in the general population have these antibodies.",
                ref(
                    "Development of Organ-Specific Autoimmunity",
                    "These autoantibodies may be expressed for years before the disease develops, and additional autoantibodies can develop over time.",
                ),
            ),
        ]
    )

    return {
        "id": p,
        "volume": 15,
        "chapterNo": "44",
        "title": "The Immunoendocrinopathy Syndromes",
        "section": "Williams Textbook of Endocrinology 15th Edition (2024)",
        "authors": "Jennifer M. Barker, Yutaka Takahashi, Peter A. Gottlieb, and Mark S. Anderson",
        "sourceFile": "williams_2024_chapters/williams2024_chapter_44_The_Immunoendocrinopathy_Syndromes.md",
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
