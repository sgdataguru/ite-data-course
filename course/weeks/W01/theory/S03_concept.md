# S03 — Scaling vs Normalisation vs Standardisation (C1, 1 hr)

## Prerequisites — do these BEFORE this session

- [ ] Attend S01 (data types) — this session builds directly on it
- [ ] Have your Lab 1 notebook open: we will scale the data you cleaned

## Python you need this week

- `from sklearn.preprocessing import StandardScaler` — borrow the standardisation tool from scikit-learn
- `scaler.fit(X_train)` — learn the mean and spread from the TRAINING data only
- `scaler.transform(X_test)` — apply that learned mean/spread to other data
- `df["col"].mean(), df["col"].std()` — the average and the typical distance from the average
- `df.describe()` — summary stats for every numeric column at once



## Concept Note

**The problem.** An HDB dataset has `floor_area_sqm` (40–200) and `resale_price` (150,000–1,500,000). Any distance-based or gradient-based model will be dominated by price — not because price matters more, but because its numbers are bigger. Scaling puts features on a comparable footing.

**Three tools, three situations:**

- **Standardisation (StandardScaler)** — subtract the mean, divide by the standard deviation. Result: mean 0, std 1. Use when data is roughly bell-shaped or the algorithm assumes normality (logistic regression, linear models, PCA).
- **Normalisation (MinMaxScaler)** — squeeze values into [0, 1]: `(x − min) / (max − min)`. Use when you need a bounded range (neural networks) and your data has few extreme outliers.
- **Robust scaling (RobustScaler)** — subtract the median, divide by the IQR. Use when outliers exist and you don't want them dictating the range.

**Worked example by hand.** Floor areas: [40, 80, 120, 160, 200]. Mean = 120, std = 40. Standardised: [−2, −1, 0, 1, 2]. Min-max: min 40, max 200 → [0, 0.25, 0.5, 0.75, 1]. Now add one outlier flat of 400 sqm. Min-max collapses everything into [0, 0.47] — the outlier stretched the scale. Robust scaling (median 120, IQR 80) barely moves. **Moral: know your outliers before you pick a scaler.**

**When NOT to scale.** Tree-based models (decision trees, random forests) split on thresholds — a split at "floor_area > 95" works identically whether the column is raw or standardised. Scaling trees wastes effort but does no harm; scaling KNN or logistic regression is essential.

**The golden rule:** fit the scaler on training data only, then transform test data with the same scaler. Fitting on the full dataset leaks test information — a preview of data leakage in C3.

**What you will later ask an AI to do:** pick a scaler given a distribution summary; explain why a model's performance changed after scaling; write a leakage-free scaling pipeline.

## Slide Outline

1. **Title** — Same data, different scales, different models.
2. **The domination problem** — sqm vs price; big columns bully small ones.
3. **Standardisation** — mean 0, std 1; the formula; when (linear, PCA).
4. **Normalisation (min-max)** — the [0,1] formula; when (bounded ranges, NNs).
5. **Robust scaling** — median & IQR; the outlier-resistant choice.
6. **Worked example** — [40, 80, 120, 160, 200] through all three scalers.
7. **The outlier disaster** — add 400 sqm; watch min-max collapse.
8. **Trees don't care** — threshold splits are scale-invariant.
9. **Fit on train, transform test** — the leakage rule.
10. **Decision table** — bell-shaped → standardise; bounded → min-max; outliers → robust; trees → skip.
11. **Recap + lab preview** — Lab 2 builds all three pipelines.

## Mini-Quiz

1. **MCQ:** For a dataset with extreme salary outliers feeding a KNN model, the best scaler is: (a) StandardScaler (b) MinMaxScaler (c) RobustScaler ✅ (d) no scaling.
2. **MCQ:** Standardising [40, 80, 120, 160, 200] gives: (a) [0, 0.25, 0.5, 0.75, 1] (b) [−2, −1, 0, 1, 2] ✅ (c) [40, 80, 120, 160, 200] (d) [−1, −0.5, 0, 0.5, 1].
3. **MCQ:** Scaling is least necessary for: (a) KNN (b) logistic regression (c) random forest ✅ (d) PCA.
4. **Short answer:** Why must the scaler be fit on training data only? *(Answer: fitting on the full dataset lets test-set statistics — min, max, mean — leak into training, inflating evaluation and breaking the simulation of unseen data.)*
