# DE5002FP — Assessment Pack (Agent 5)

Weightings: Practical Test 50% + Project 40% + Behavioural 10% = 100%. Marker-to-candidate ratio 1:20.

---

## 1. Practical Test (2 hrs, 50%, C1 + C2) — `assessment/practical_test.md`

**Scenario brief:** You are a junior data analyst at a Singapore fintech. You are given `loan_prep_test.csv` (~8,000 rows): applicant data with deliberate issues — income as "$X,XXX" strings, mixed date formats, 3% missing values in a key column, a 92:8 approval imbalance, and sensitive attributes (`gender`, `district`).

**Dataset shape:** 8,000 rows × 12 columns. Deliberate issues: (1) string-formatted numerics, (2) inconsistent dates, (3) missing values, (4) class imbalance in target `approved`, (5) sensitive attributes for bias analysis, (6) one leaky feature (`loan_outcome_note`) planted for detection.

**Candidate deliverable:** one Jupyter notebook (.ipynb) using the provided template: sections for cleaning, scaling, encoding, imbalance handling, bias analysis, mitigation, and a final documentation cell.

**Tasks (with dry-run time estimates):**
1. Data formatting & preparation (25 min) — fix types, handle missing, sanity-check.
2. Scaling & encoding (25 min) — justified choices per column.
3. Imbalance handling (20 min) — diagnose, apply strategy to training data only.
4. Bias analysis (25 min) — compute demographic parity + equalised odds by one sensitive attribute; interpret.
5. Mitigation (15 min) — apply one mitigation; report before/after.
6. Documentation (10 min) — decisions, rationale, checks.

**Marking rubric (100 marks):**

| Criterion | Marks | Traces to Performance Criterion |
|---|---|---|
| Data Conversion Accuracy | 20 | C1: "Convert raw data into numerical and categorical formats suitable for modelling" |
| Feature Scaling & Normalisation | 15 | C1: "Scale and normalise numerical features appropriately" |
| Categorical Encoding Techniques | 15 | C1: "Encode categorical variables using suitable techniques" |
| Handling Imbalanced Data | 15 | C1: "Handle imbalanced datasets to improve model performance" |
| Bias Detection & Analysis | 20 | C2: "Analyse datasets for potential sources of bias"; "Detect imbalances in sensitive or protected attributes" |
| Appropriate Application of Mitigation Strategies | 15 | C2: "Suggest basic mitigation strategies"; "Document bias assessment results for traceability" |

**Marker instructions:** What good looks like — justified choices (not just running code), leakage-free pipelines, numeric evidence in bias findings, complete documentation cell. Common pitfalls: fitting on full data before split; accuracy-only evaluation; adjective-only bias findings; missing documentation. Score bands: 80+ (distinction-ready, all criteria with justification), 60–79 (competent, minor gaps), 40–59 (partial, key gaps in bias or imbalance), <40 (not yet competent — retest pathway per CP policy). Retest eligible (CP Type 1, per official TOS).

**AI-tool policy for the test:** **Not allowed.** Invigilated lab, no AI assistants, no internet access to AI tools. (Consolidated in `ai_usage_policy.md`.)

---

## 2. Project (15 hrs, 40%, C1→C3) — `assessment/project_brief.md`

**Brief — choose ONE (all real data.gov.sg datasets; full teenager-friendly brief in `project_brief.md`):**
- **Option A — HDB Resale Price Prep:** *Resale Flat Prices* (data.gov.sg) — prep for a price model; audit town/flat-type representation and fairness.
- **Option B — Transport Demand Prep:** *Passenger Volume by Train Station* (data.gov.sg, LTA) — time-series prep for a demand model; fairness across lines and stations.
- **Option C — Energy & Household Prep:** *Household Electricity Consumption by Town* (data.gov.sg, EMA) — prep for a consumption model; aggregation bias across towns and dwelling types.

**Milestones (gates at supervised studio sessions):**
- **25% (S38):** cleaned + typed dataset, prep-decisions table.
- **50% (S39):** bias report (1 page) with metrics and one mitigation applied.
- **75% (S40):** leakage-free splits + CV strategy; augmentation/synthetic data applied.
- **100% (S41):** final QA checklist, AI-usage ledger, 5-slide presentation, submission.

**Required artefacts:** cleaned dataset, Jupyter notebook, 1-page bias report, 1-page AI-usage reflection, 5-slide deck.

**Rubric (100 marks):**

| Criterion | Marks | Traces to |
|---|---|---|
| Data Preparation | 20 | C1 performance criteria |
| Bias Detection & Mitigation | 20 | C2 performance criteria |
| Dataset Splitting & Enhancement (splits, CV) | 15 | C3: splits + cross-validation |
| Dataset Enhancement (augmentation/synthetic) | 15 | C3: augmentation + synthetic data |
| Use of GenAI to automate data preparation | 15 | C3: vibe coding criteria |
| Data Analysis & Visualisation | 15 | Cross-cutting (TSC Data Analysis L2) |

**Explicit AI requirement:** the project MUST demonstrate GenAI use (prompt log + AI-usage ledger + reflection). Undisclosed AI use = academic dishonesty (see behavioural rubric).

---

## 3. Behavioural & Attitudinal Attributes (10%) — `assessment/behavioural_rubric.md`

| Attribute | Descriptor | Marks |
|---|---|---|
| Attendance & punctuality | Present and on time for sessions | 3 |
| Lab conduct & safety | Follows lab rules; environment hygiene; submits exit tickets | 3 |
| Peer collaboration | Constructive peer review (clinics); supports classmates | 2 |
| Honest AI-usage disclosure | Accurate, complete AI-usage logs; no undisclosed AI use | 2 |

---

## 4. Mock Practical Test (2 hrs, S36) — `assessment/mock_practical.md`

Parallel form of the practical test: `telecom_churn_prep_mock.csv` (~7,000 rows) with the same six issue classes (string numerics, dates, missing, 90:10 imbalance, sensitive attributes, one leaky feature). Same template, same rubric, same timing. Marked for feedback only (not graded); students self-mark against the key in S35's walkthrough, then sit the mock under exam conditions.

---

## 5. AI-Usage Policy (consolidated) — `assessment/ai_usage_policy.md`

| Assessment | AI tools |
|---|---|
| Practical Test (50%) | **Prohibited** — invigilated, AI-free |
| Mock Practical Test | **Prohibited** — mirrors real test conditions |
| Project (40%) | **Required** — documented GenAI use with ledger |
| Labs / exit tickets | Permitted per Agent 4's overlay rules (attempt-first, verify, reflect) |

**Project AI-usage ledger format:** date | tool | task | prompt summary | verification performed | what you changed. Fabricating or omitting entries is treated as academic dishonesty under the behavioural rubric.
