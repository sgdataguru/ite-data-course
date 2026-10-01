# S28 — Risks & Limitations of AI-Generated Code (C3, 1 hr)

## Concept Note

**Four failure classes to know cold:**

1. **Hallucinated APIs.** The AI invents `pandas.fill_missing_values()` or a `sklearn.preprocessing.TargetEncoder` signature that doesn't exist (or exists only in a different library version). The code *looks* right; it crashes — or worse, it doesn't.
2. **Silent correctness bugs.** The code runs and produces wrong answers: scaling *after* the split when you asked for a pipeline (leakage), SMOTE applied to the *test* set, a fairness metric computed on the wrong axis. No error message — just a wrong number you might submit.
3. **Licensing contamination.** Generated code can reproduce GPL-licensed snippets or copyrighted patterns. In a workplace, shipping contaminated code creates legal exposure. Mitigation: review, rewrite in your own style, check provenance.
4. **Data leakage into prompts.** Pasting real customer rows, NRIC fragments, or company data into a public LLM sends that data outside your organisation — a PDPA incident in Singapore. Enterprise rule: schema and statistics, never raw sensitive rows.

**Why AI fails this way.** LLMs predict plausible text, not verified truth. Plausible-looking code is exactly what they're built to produce. The failure modes aren't bugs in your prompt — they're the technology's nature, which is why verification (M2) is a taught skill.

**Worked example by hand.** You ask: "apply SMOTE to my dataset." The AI returns code that resamples *before* splitting — the test set is now synthetic-balanced, your recall is a beautiful lie, and nothing crashes. This single bug pattern is the most common AI failure in data prep. The fix is a checklist question: *"Is any transformation fitted on data that includes the test set?"*

**The defence:** deterministic seeds, small reproducible tests, diffing AI output against your manual attempt, and a written reflection of what the AI got wrong.

**What you will later ask an AI to do:** this session is AI-assisted — you'll ask an AI to critique *its own* previous output and watch it miss bugs.

## Slide Outline

1. **Title** — Plausible is not correct.
2. **Failure 1: hallucinated APIs** — functions that don't exist.
3. **Failure 2: silent correctness bugs** — runs fine, answers wrong.
4. **The SMOTE-before-split bug** — the classic worked example.
5. **Failure 3: licensing contamination** — provenance and exposure.
6. **Failure 4: data leakage into prompts** — PDPA stakes.
7. **Why LLMs fail this way** — plausibility is the product.
8. **The defence stack** — seeds, tests, diffs, reflection.
9. **The checklist question** — "was anything fitted on test data?"
10. **Recap + lab preview** — Lab 16: hunting bugs in real AI output.

## Mini-Quiz

1. **MCQ:** A hallucinated API is: (a) a slow function (b) a plausible-looking call to something that doesn't exist ✅ (c) deprecated code (d) a type error.
2. **MCQ:** The most dangerous AI failure in data prep is: (a) syntax errors (b) silent correctness bugs ✅ (c) slow code (d) verbose comments.
3. **MCQ:** Pasting customer rows into a public chatbot risks: (a) licensing (b) a PDPA data breach ✅ (c) mode collapse (d) overfitting.
4. **Short answer:** Why do deterministic seeds help when verifying AI-generated code? *(Answer: they make runs reproducible, so you can diff AI output against your own attempt and trust that differences come from the code, not randomness.)*
