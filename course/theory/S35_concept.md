# S35 — Mock Test Walkthrough (Revision, 2 hrs)

## Concept Note

**Purpose.** The mock is a parallel-form rehearsal of the 2-hour practical test (50%). Same structure, same timing, same marking criteria — different dataset. Treat it as a dress rehearsal: the goal is to surface gaps *before* the real test.

**The test shape (mirrors the official TOS):**
1. **Data formatting & preparation** (~30 min) — fix types, handle missing values, sanity-check.
2. **Scaling & encoding** (~30 min) — appropriate scaler choices, correct encoding per column type.
3. **Imbalance handling** (~20 min) — diagnose imbalance, apply a justified strategy to training data only.
4. **Bias analysis & mitigation** (~30 min) — compute fairness metrics on a sensitive attribute, apply one mitigation, report before/after.
5. **Documentation** (~10 min) — a short traceability section: decisions, rationale, checks.

**Walkthrough method (this session):** the instructor works the mock live, narrating time checkpoints and decision points; then students mark a sample submission against the rubric to internalise what "good" looks like.

**Time budget discipline:** 15 min read + plan → 90 min work in the order above → 15 min final checks (leakage, sanity, documentation). Students who fail this test usually fail on *time*, not knowledge.

**What markers reward (from the official TOS):** Data Conversion Accuracy; Feature Scaling & Normalisation; Categorical Encoding Techniques; Handling Imbalanced Data; Bias Detection & Analysis; Appropriate Application of Mitigation Strategies. Every rubric line traces to a performance criterion in the module spec.

## Slide Outline

1. **Title** — The dress rehearsal.
2. **Why a mock** — surface gaps cheaply.
3. **The five test sections** — with time budgets.
4. **Section 1 walkthrough** — the instructor's first 15 minutes.
5. **Sections 2–3 walkthrough** — scaler and SMOTE decisions, narrated.
6. **Section 4 walkthrough** — metrics, mitigation, before/after.
7. **Section 5** — the 10-minute documentation habit.
8. **Marking a sample submission** — students apply the rubric.
9. **What "good" looks like** — score bands with examples.
10. **Common pitfalls** — leakage, no sanity checks, undocumented choices.
11. **Time discipline** — the 15/90/15 budget.
12. **Next week** — the real test; logistics and rules.

## Mini-Quiz

1. **MCQ:** The mock test exists to: (a) count toward your grade (b) rehearse timing and surface gaps ✅ (c) replace revision (d) rank students.
2. **MCQ:** The recommended time budget is: (a) 120 min work (b) 15 plan / 90 work / 15 check ✅ (c) 60/60 (d) no planning needed.
3. **MCQ:** The most common failure mode in the practical test is: (a) missing knowledge (b) poor time management ✅ (c) broken laptops (d) hard datasets.
4. **Short answer:** Name two things you should verify in your final 15 minutes. *(Answer: no train-test leakage in any fitted transformation; sanity checks on converted columns; complete documentation/traceability section.)*
