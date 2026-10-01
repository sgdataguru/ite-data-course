# S19 — Train/Test/Validation Splits & Leakage (C3, 1 hr)

## Concept Note

**The three-way split.** **Training set** — the model learns from it. **Validation set** — you tune decisions on it (which scaler, which features, which hyperparameters). **Test set** — touched once, at the end, to estimate real-world performance. If you tune on the test set, it silently becomes a second validation set and your performance estimate becomes optimistic.

**Typical ratios.** 70/15/15 or 80/10/10. With small datasets, cross-validation (next session) replaces the validation split.

**Data leakage.** Any way information from outside the training set sneaks into training. Two classic forms:

1. **Train-test contamination** — fitting a scaler (or imputer, or target encoder) on the *full* dataset before splitting. The scaler's mean now contains test-set information.
2. **Feature leakage** — a feature that contains the answer: predicting resale price when a column `price_per_sqm × floor_area` exists; predicting loan default when `days_late_on_payment` is present. The model looks brilliant; it is cheating.

**Worked example by hand.** 1,000 rows, 80/10/10. You compute the mean of `floor_area` on all 1,000 rows (120.0), then split. The training scaler uses 120.0 — but the training-only mean is 119.2. The 0.8 difference is test information, leaked. Correct order: split first, compute the mean on 800 training rows, transform the other 200 with it.

**Randomness and reproducibility.** Splits are random; set a `random_state` seed so your results — and your markers' — are reproducible.

**What you will later ask an AI to do:** write a leakage-free prep pipeline; spot the leaky feature in a column list; explain why a 99% validation score is suspicious.

## Slide Outline

1. **Title** — Three sets, one rule: the test set is sacred.
2. **Train / validation / test** — learn / tune / final estimate.
3. **Why three** — tuning needs its own playground.
4. **Typical ratios** — 70/15/15, 80/10/10.
5. **Leakage type 1: contamination** — fitting before splitting.
6. **Leakage type 2: feature leakage** — the answer hidden in a column.
7. **Worked example** — the 120.0 vs 119.2 mean.
8. **The correct order** — split → fit on train → transform.
9. **Seed everything** — reproducibility for you and your marker.
10. **Recap + lab preview** — Lab 11 builds leakage-free splits.

## Mini-Quiz

1. **MCQ:** The test set should be used: (a) for hyperparameter tuning (b) once, for final evaluation ✅ (c) in every training epoch (d) to fit the scaler.
2. **MCQ:** Fitting a scaler on the full dataset before splitting causes: (a) feature leakage (b) train-test contamination ✅ (c) class imbalance (d) overfitting of trees.
3. **MCQ:** A `days_late` column in a default-prediction model is likely: (a) a useful feature (b) feature leakage ✅ (c) a proxy for age (d) redundant with ID.
4. **Short answer:** Why does tuning on the test set inflate your performance estimate? *(Answer: the model (indirectly, through your choices) adapts to the test data, so it no longer simulates unseen data; the score measures fit-to-test-set, not generalisation.)*
