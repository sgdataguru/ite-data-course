# DE5002FP — AI-Assist Overlay (Agent 4)

Default tool: **Claude**. Fall-backs: ChatGPT, GitHub Copilot. Substance is tool-agnostic.

**Universal rules for every AI-assist exercise:**
1. **Attempt first.** Sketch or attempt the task unaided (≥15 min) before prompting.
2. **Diff.** Compare AI output against your attempt.
3. **Verify.** Prove correctness with the 6-point checklist: (1) runs without error, (2) deterministic (seeded), (3) no train-test leakage, (4) spot-check outputs by hand, (5) APIs exist in the installed versions, (6) constraints respected (libraries, pipeline structure).
4. **Reflect.** End with 3–5 lines: what the AI got right, what it got wrong, what you changed.

---

## Session overlays (flagged sessions from Agent 1)

### S02 Lab 1 — Messy data cleaning (1 hr AI-assist)
- **Prompt library starters:** "Convert column X from '$530,000' strings to float, handling NaN and thousands separators"; "Write a validation check that flags implausible values in resale_price after conversion"; "Explain why this astype call failed: [error]".
- **Guided exercise:** clean 3 columns by hand (15 min) → prompt the AI for the remaining 7 → diff approaches → verify with the checklist.
- **Failure gallery:** AI uses `errors='ignore'` (silently leaves bad values); AI fills NaN with 0 for price.

### S04 Lab 2 — Scaling (1 hr)
- **Prompts:** "Choose a scaler for this distribution summary: [stats]"; "Write a leakage-free scaling pipeline for these 5 numeric columns"; "Why did my KNN accuracy change after scaling?"
- **Exercise:** pick scalers manually → ask AI to justify or challenge → resolve disagreements with a plotted experiment.
- **Failures:** AI fits scaler on full dataset before split; AI applies RobustScaler but reports min-max ranges.

### S06 Lab 3 — Encoding (1 hr)
- **Prompts:** "Given cardinality N and model type M, recommend an encoding with rationale"; "Write fold-safe target encoding"; "Why did one-hot explode my memory?"
- **Failures:** AI label-encodes nominal `town`; AI target-encodes without fold protection.

### S08 Lab 4 — Imbalance (1 hr)
- **Prompts:** "Write an imblearn pipeline so SMOTE applies only to training folds"; "Justify undersampling vs SMOTE for ratio 99:1 and 10k rows".
- **Failures:** AI resamples before splitting (the classic); AI evaluates with accuracy only.

### S09 Lab 5 — C1 mini-project (1 hr) & S09B clinic (0.5 hr)
- **Prompts:** "Review my prep-decisions table and flag any column whose treatment mismatches its algorithm"; "Generate 5 quiz questions on encoding choice".
- **Failures:** AI invents `sklearn.preprocessing.TargetEncoder` API details wrong for the installed version.

### S11 Lab 6 — Bias audit (1 hr)
- **Prompts:** "List plausible bias sources for this dataset description"; "Write group-wise summary statistics code for columns [...] by [attribute]"; "Draft a bias-risk paragraph from these numbers".
- **Failures:** AI writes findings with adjectives, no numbers; AI suggests dropping the sensitive column entirely.

### S13 Lab 7 — Fairness metrics (1 hr)
- **Prompts:** "Compute demographic parity, equalised odds, and predictive parity from this confusion-matrix table"; "Explain this parity gap in plain English for a non-technical report".
- **Failures:** AI conflates parity with equalised odds; AI computes metrics on the training set.

### S15 Lab 8 — Mitigations (1 hr)
- **Prompts:** "Explain reweighing weights for this small table"; "Draft the mitigation section of a bias report with before/after".
- **Failures:** AI applies mitigation to test data; AI claims mitigation "removed bias" without re-measuring.

### S17 Lab 9 — Bias report (0.5 hr) & S18 Lab 10 (0.5 hr) & S18B clinic (0.5 hr)
- **Prompts:** "Review my bias report against the 5-section structure and list missing traceability elements"; "Rewrite this finding so the evidence is numeric".
- **Failures:** AI fabricates dataset provenance details for the datasheet.

### S20 Lab 11 — Splits (1 hr)
- **Prompts:** "Write leakage-free 70/15/15 splitting code with seeds"; "Spot the leaky feature in this column list: [...]"; "Why is my validation score 99%?"
- **Failures:** AI splits after fitting; AI uses `train_test_split` twice producing overlapping validation/test.

### S22 Lab 12 — CV (1 hr)
- **Prompts:** "Choose a CV strategy for [data description]"; "Write a pipeline-based stratified CV loop"; "Explain fold-to-fold score variance".
- **Failures:** AI uses k-fold on time series; AI puts the scaler outside the CV loop.

### S24 Lab 13 — Augmentation (1 hr)
- **Prompts:** "Write Gaussian jitter augmentation preserving labels"; "Generate an augmented image grid with matplotlib".
- **Failures:** AI augments the test set; AI jitters so hard the label no longer holds.

### S25 Lab 14 — Synthetic data (1.5 hr)
- **Prompts:** "Generate 50 synthetic rows matching this schema and these summary statistics — do not use real records"; "Write a distribution comparison between real and synthetic columns"; "Critique your own generated rows for plausibility".
- **Failures:** AI generates impossible rows (negative ages); AI drifts the class ratio.

### S26 Theory — Vibe coding (1 hr, in-session AI-assist)
- Live prompt-evolution demo: weak vs strong prompt for the same task; students annotate why the strong prompt wins.

### S27 Lab 15 — Vibe coding core lab (2 hr)
- Full loop on Lab 5's task: manual baseline exists → prompt → draft → run → verify → refine → diff → reflect. Prompt log required.

### S28 Theory — AI risks (0.5 hr, in-session AI-assist)
- Students ask an AI to critique its own earlier output; class tallies the bugs it missed.

### S29 Lab 16 — Critique & fix (2 hr)
- Three planted-failure scripts (hallucinated API, SMOTE-before-split, test leakage). Find, explain, fix. Checklist-driven.

### S30 Theory — Prompt design (1 hr, in-session AI-assist)
- Students draft and test 5-part prompts live; peer-score prompt quality.

### S31 Lab 17 — Prompt library (2 hr)
- Build + test 8 prompts (one per module topic); each prompt must pass the checklist on a real task.

### S32 Lab 18 — Final QA (1 hr)
- **Prompts:** "Write a data-readiness checklist runner for these constraints"; "Generate unit-test skeletons for my prep pipeline".
- **Failures:** AI's checklist skips leakage; AI tests only that code runs, not that outputs are right.

### S33 Revision theory (0.5 hr) & S34 consolidation lab (1 hr)
- AI-generated flashcards on the ten examinable ideas; students verify each card against their notes (AI can hallucinate definitions).

### S38–S41 Project studio (7.5 hr AI-assist total)
- Milestone-appropriate prompting: M1-style prep prompts (25%), bias-analysis prompts (50%), augmentation/synthesis prompts (75%), QA + presentation prompts (100%). AI-usage ledger mandatory (Agent 5 policy).

---

## Cross-cutting mini-modules (6 hrs, counted in the ledger)

### M1 — Prompting for data work (2 hrs, inside S30/S31)
Role, context, data schema, constraints, examples. Anti-patterns. Iteration with error messages. Deliverable: tested prompt library.

### M2 — Verifying AI-generated code (2 hrs, inside S28/S29)
Reproducibility (seeds), deterministic tests, diffing AI vs manual, test harnesses, spot-checking by hand. Deliverable: three fixed failure scripts.

### M3 — Risks, licensing and data leakage (2 hrs, inside S28/S32)
What never goes into a public LLM (raw personal data, NRIC, customer rows); enterprise-safe patterns (schema + statistics, not rows); provenance; hallucinated APIs; licence contamination. Deliverable: a personal "never paste" list + QA checklist.
