# S33 — C1–C3 Consolidation Review (Revision, 2 hrs)

## Prerequisites — do these BEFORE this session

- [ ] Weeks 1–8 complete — this session consolidates everything
- [ ] Bring ALL your lab notebooks; the review maps them to the exam

## Python you need this week





## Concept Note

**The map of the module.** C1 makes data *usable* (types, scaling, encoding, imbalance, algorithm-aware prep). C2 makes it *fair* (bias sources, metrics, sensitive attributes, mitigation, documentation). C3 makes it *ready* (splits, CV, augmentation/synthesis, vibe coding, QA). The project runs all three in sequence on one dataset.

**The ten most examinable ideas:**
1. Conversion preserves meaning; sanity-check after every cast.
2. Scaler choice follows distribution and algorithm (trees don't care; KNN does).
3. Encoding must match meaning: nominal → one-hot; ordinal → label; high-cardinality → target (fold-safe).
4. Resample training folds only; evaluate with precision/recall, not accuracy.
5. The five bias sources; proxies are sensitive too.
6. Demographic parity / equalised odds / predictive parity — three different "fairs".
7. Measure with the sensitive attribute; decide without it.
8. Split before you fit; the test set is sacred.
9. Stratified CV for classification; TimeSeriesSplit for time.
10. AI output is a hypothesis: verify with seeds, tests, and diffs.

**Common misconceptions to kill in revision:**
- "99% accuracy = good model" (imbalanced data).
- "Deleting the race column removes bias" (proxies).
- "Scaling helps all models" (trees).
- "SMOTE goes before the split" (the classic bug).
- "AI code that runs is correct" (silent bugs).

**Mock test walkthrough preview (S35):** the mock mirrors the practical test — a messy dataset with deliberate type, scaling, encoding, imbalance, and bias issues; you fix, prep, analyse, mitigate, and document in a Jupyter notebook within 2 hours.

## Slide Outline

1. **Title** — The whole module on one page.
2. **C1 recap** — usable data; the five examinable ideas.
3. **C2 recap** — fair data; metrics and mitigation.
4. **C3 recap** — ready data; splits, CV, AI-assist.
5. **The ten ideas** — rapid-fire review.
6. **Misconception 1–2** — accuracy lies; deleting columns doesn't.
7. **Misconception 3–4** — trees and scaling; SMOTE placement.
8. **Misconception 5** — running ≠ correct.
9. **How the exam is structured** — the practical test shape.
10. **Time management in a 2-hr test** — 20 min read/plan, 80 min work, 20 min check.
11. **What markers reward** — traceability, sanity checks, documented decisions.
12. **Q&A + mock preview**.

## Mini-Quiz

1. **MCQ:** Which pair is correctly matched? (a) nominal + label encoding (b) ordinal + one-hot (c) high-cardinality nominal + fold-safe target encoding ✅ (d) datetime + SMOTE.
2. **MCQ:** The correct order is: (a) SMOTE → split → scale (b) split → scale → SMOTE on training folds ✅ (c) scale all → split → SMOTE all (d) split → SMOTE all → scale.
3. **MCQ:** Equalised odds requires equal: (a) approval rates (b) TPR and FPR across groups ✅ (c) precision (d) group sizes.
4. **Short answer:** In the last 20 minutes of a practical test, what three checks give the most marks per minute? *(Answer: verify no leakage (fitted on train only), sanity-check converted columns (ranges/nulls), and ensure documentation/report sections are complete — markers reward traceability.)*
