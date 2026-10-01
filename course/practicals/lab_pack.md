# DE5002FP — Practical Lab Pack (Agent 3)

Labs are 2-hr blocks unless noted. Every lab produces a kept artefact (notebook + chart/report). Labs flagged `ai_assist_candidate: true` have a baseline path that works without AI — Agent 4 adds the overlay.

---

## Lab 1 (S02) — Load & Fix a Messy Dataset (C1)

**Brief:** You receive `hdb_messy.csv` — a corrupted HDB resale extract: prices as "$530,000" strings, 47 NaNs in floor_area, mixed date formats, one duplicated block column. Goal: a clean, typed DataFrame ready for scaling.

**Starter notebook outline:** imports → load CSV → `df.info()` audit → TODO: fix price column → TODO: parse dates → TODO: handle missing floor_area → TODO: drop duplicate column → final audit cell.

**Solution highlights:** `str.replace` + `astype(float)` for price; `pd.to_datetime(..., errors='coerce')`; median imputation for floor_area (justified: <1% missing, roughly symmetric); `df.loc[:, ~df.columns.duplicated()]`.

**Exit ticket:** Commit your cleaned CSV + one sentence: "The hardest bug I fixed was ___."

---

## Lab 2 (S04) — Scaling Pipelines (C1)

**Brief:** Using the cleaned HDB data, build three sklearn Pipelines (StandardScaler, MinMaxScaler, RobustScaler) and show how each transforms `floor_area_sqm` and `resale_price`. Plot before/after distributions.

**Starter:** load cleaned CSV → split X/y → TODO: build 3 pipelines → TODO: fit on train only → TODO: transform + plot → TODO: compare ranges.

**Solution highlights:** fit on training split, transform test with same scaler; RobustScaler demo with an injected 400 sqm outlier; matplotlib histograms side by side.

**Exit ticket:** One chart: three scalers, one column. Which would you ship for KNN and why?

---

## Lab 3 (S06) — Encoding Categorical Data (C1)

**Brief:** Encode `town` (26 nominal values), `flat_type` (ordinal), and `street_name` (high-cardinality) appropriately. Compare column counts and memory before/after.

**Starter:** load → TODO: one-hot town → TODO: ordinal flat_type with explicit order → TODO: target-encode street_name (fold-safe) → TODO: report shapes.

**Solution highlights:** `OneHotEncoder(handle_unknown='ignore')`; `OrdinalEncoder(categories=[...])` with explicit order; `TargetEncoder` from sklearn with CV; rare-category grouping into 'OTHER' first.

**Exit ticket:** A 3-row table: column, encoding chosen, one-line justification.

---

## Lab 4 (S08) — Imbalance & Algorithm-Aware Prep (C1)

**Brief:** A synthetic fraud dataset (990:10). Diagnose imbalance, apply random under/over and SMOTE (training folds only), train a KNN, and compare accuracy vs F1 across strategies.

**Starter:** load → TODO: class distribution → TODO: three resampling strategies → TODO: train + evaluate → TODO: confusion matrices.

**Solution highlights:** `imblearn.Pipeline` (resampling inside pipeline = fold-safe); the "99% accuracy, 0% recall" reveal; F1/recall as the honest metrics.

**Exit ticket:** Which strategy won on F1, and why is accuracy a trap here?

---

## Lab 5 (S09) — C1 Consolidation Mini-Project (C1)

**Brief:** End-to-end C1 on HDB resale: clean → scale → encode → handle imbalance in `town` representation → prep for three algorithms (tree, KNN, logistic). Deliverable: one notebook + a prep-decisions table.

**Starter:** full scaffold with section headers and TODOs per stage.

**Solution:** the reference pipeline; decisions table mapping each column to its treatment.

**Exit ticket:** Your prep-decisions table (column → treatment → why).

---

## Lab 5B (S09B) — Algorithm-Aware Prep Clinic (C1)

**Brief:** Peer-review clinic: swap notebooks with a partner and audit their Lab 5 prep against the algorithm-prep matrix (trees/KNN/linear). Fix what the review surfaces.

**Exit ticket:** Two review comments given, one fix applied.

---

## Lab 6 (S11) — Dataset Bias Audit (C2)

**Brief:** Audit UCI Adult income for representation bias: group-wise summary stats by sex and race; missing-value patterns by group; visualise representation gaps.

**Starter:** load Adult → TODO: group-wise stats → TODO: missingness by group → TODO: representation charts → TODO: write 3 bias-risk findings.

**Solution:** `df.groupby(...)` tables; bar charts of group representation; findings written with evidence (numbers, not adjectives).

**Exit ticket:** Your 3 findings, each with a number as evidence.

---

## Lab 7 (S13) — Computing Fairness Metrics (C2)

**Brief:** Train a simple income classifier on Adult; compute demographic parity, equalised odds, and predictive parity by sex using fairlearn. Report gaps.

**Starter:** train model → TODO: MetricFrame for selection rate → TODO: TPR/FPR by group → TODO: precision by group → TODO: gap table.

**Solution:** `fairlearn.metrics.MetricFrame`; the three metrics side by side; a gap table with plain-English interpretation.

**Exit ticket:** Which metric failed worst, and what does that mean in plain English?

---

## Lab 8 (S15) — Applying Mitigations (C2)

**Brief:** Apply reweighing and resampling mitigations to the Adult model; recompute the three metrics; report before/after.

**Starter:** TODO: reweigh → retrain → TODO: resample → retrain → TODO: before/after table.

**Solution:** `fairlearn.reductions`/AIF360 reweighing; honest reporting of the accuracy–fairness trade-off.

**Exit ticket:** Before/after table + one sentence on the trade-off you observed.

---

## Lab 9 (S17) — 1-Page Bias Assessment Report (C2)

**Brief:** Turn Labs 6–8 into the standard 1-page bias report (5 sections: scope, risks, metrics, mitigations, residual risks). Markdown template provided.

**Exit ticket:** Your 1-page report committed to the LMS.

---

## Lab 10 (S18) — C2 Consolidation on Two Real Datasets (C2)

**Brief:** Full audit cycle (Labs 6–9 compressed) on a lending dataset, then compare findings against your Adult report. Which dataset has the worse representation problem?

**Exit ticket:** One paragraph: which dataset is riskier to deploy in Singapore and why.

---

## Lab 10B (S18B) — Bias Report Peer Review Clinic (C2)

**Brief:** Swap bias reports; review against the traceability checklist (evidence over adjectives, all 5 sections, before/after numbers). Rewrite the weakest section of your own report.

**Exit ticket:** The rewritten section.

---

## Lab 11 (S20) — Splits in Practice (C3)

**Brief:** On the HDB data: build 70/15/15 and 80/10/10 splits; demonstrate leakage by fitting a scaler before vs after splitting; show the score difference.

**Starter:** TODO: split → TODO: scaler-before-split (buggy) → TODO: scaler-after-split (correct) → TODO: compare.

**Solution:** the leakage demo with a measurable score gap; `random_state` seeds throughout.

**Exit ticket:** The two scores. One sentence: why do they differ?

---

## Lab 12 (S22) — KFold, StratifiedKFold, TimeSeriesSplit (C3)

**Brief:** On an energy-demand time series + the fraud dataset: run all three splitters; show why plain k-fold breaks time series and why stratification matters for imbalance.

**Solution:** fold visualisations; TimeSeriesSplit expanding-window demo; stratified fold class-ratio table.

**Exit ticket:** Match each of 3 datasets to its correct splitter, with one reason each.

---

## Lab 13 (S24) — Augmentation on Tabular + Image (C3)

**Brief:** Apply Gaussian jitter to HDB numeric features; apply rotation/flip/zoom to a Fashion-MNIST subset; verify labels survive augmentation.

**Exit ticket:** One augmented image grid + one jittered-rows sanity check.

---

## Lab 14 (S25) — Synthetic Data with SMOTE + GenAI (C3)

**Brief:** Generate synthetic minority rows two ways: SMOTE, and a GenAI tool prompted with schema + statistics (no raw rows). Compare distributions of real vs synthetic.

**Exit ticket:** Distribution comparison chart + one sentence: which synthetic set is safer to train on?

---

## Lab 15 (S27) — Vibe Coding Data Prep (C3) *(AI-assist core lab)*

**Brief:** Redo Lab 5's pipeline entirely vibe-coded: prompt → draft → run → verify → refine. Keep a prompt log. Baseline = your Lab 5 manual solution for diffing.

**Exit ticket:** Diff summary: what the AI got right, wrong, and what you changed.

---

## Lab 16 (S29) — Critiquing & Fixing AI Output (C3) *(AI-assist core lab)*

**Brief:** You are given three AI-generated prep scripts, each containing one planted failure (hallucinated API, SMOTE-before-split, test-set leakage). Find, explain, and fix all three.

**Exit ticket:** Three fixes with one-paragraph explanations each.

---

## Lab 17 (S31) — Prompt Library Build (C3) *(AI-assist core lab)*

**Brief:** Build a personal prompt library of 8+ tested prompts (cleaning, scaling, encoding, imbalance, metrics, mitigation, splitting, QA) using the 5-part structure. Test each on a real task.

**Exit ticket:** Your prompt library file, committed.

---

## Lab 18 (S32) — Final Dataset QA & Readiness Checklist (C3)

**Brief:** Run the data-readiness checklist (types, leakage, balance, distributions, constraints, documentation) on your project dataset; fix every red flag.

**Exit ticket:** Completed checklist with all items green or justified.

---

## Consolidation Lab (S34, 1 hr) — Mixed C1–C3 refresher: 6 timed micro-tasks (one per examinable idea), self-marked against keys.

## Mock Practical Test (S36, 2 hrs) — Parallel-form mock under exam conditions (Agent 5's paper).

## Project Studio (S38–S41, 15 hrs) — Supervised end-to-end project time with milestone gates at 25/50/75/100% (Agent 5's brief).
