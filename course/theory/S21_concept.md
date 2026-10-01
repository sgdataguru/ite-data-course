# S21 — Cross-Validation Methods (C3, 1 hr)

## Concept Note

**The problem.** A single 80/20 split wastes 20% of data on one evaluation, and the score depends on *which* rows landed in the test set. Cross-validation (CV) rotates the test set so every row gets evaluated once.

**K-fold.** Split the data into K equal folds (typically 5 or 10). Train on K−1 folds, validate on the held-out fold; repeat K times; average the scores. Every row is used for both training and validation (never both at once). Cost: K training runs.

**Stratified K-fold.** Plain k-fold can, by chance, put too few minority-class rows in a fold — with a 95:5 dataset, a fold might have almost no positives. Stratified k-fold preserves the class ratio in every fold. **Default choice for classification.**

**Time-series split.** Random splitting breaks time series: training on 2024 to predict 2023 is time travel. TimeSeriesSplit uses only the *past* to validate the *future*: train on folds 1..k, validate on fold k+1, expanding window. Use for any temporal data — energy demand, MRT ridership, SGX prices.

**Worked example by hand.** 10 rows, 5-fold. Folds: [1,2], [3,4], [5,6], [7,8], [9,10]. Round 1: train on rows 3–10, test on 1–2. Round 2: train on 1–2, 5–10, test on 3–4. … Round 5: train on 1–8, test on 9–10. Average the five scores. With stratification, each fold would be constructed to keep the class ratio at the global 95:5.

**The CV + pipeline rule.** If you scale outside CV, the validation fold's statistics leak into training. The fix: put the scaler *inside* the CV pipeline so each round fits its own scaler on its own training folds. This is where C1's scaling meets C3's splitting.

**What you will later ask an AI to do:** choose a CV strategy given the data's structure; write a pipeline-based CV loop; explain why a score varies across folds.

## Slide Outline

1. **Title** — Every row deserves to be tested.
2. **The single-split problem** — luck of the draw.
3. **K-fold mechanics** — the 10-row, 5-fold diagram.
4. **Choosing K** — 5 or 10; the cost trade-off.
5. **Stratified k-fold** — preserving class ratios; the classification default.
6. **Time-series split** — expanding windows; no time travel.
7. **Worked example** — fold-by-fold walkthrough.
8. **The pipeline rule** — scaler inside CV, not outside.
9. **Decision table** — classification → stratified; temporal → TimeSeriesSplit; regression → plain k-fold.
10. **Recap + lab preview** — Lab 12 runs all three splitters.

## Mini-Quiz

1. **MCQ:** In 5-fold CV, each row is used for validation: (a) once ✅ (b) five times (c) never (d) twice.
2. **MCQ:** For a 98:2 imbalanced classification problem, use: (a) plain k-fold (b) stratified k-fold ✅ (c) TimeSeriesSplit (d) no CV.
3. **MCQ:** For daily energy-demand data, the correct splitter is: (a) k-fold (b) stratified k-fold (c) TimeSeriesSplit ✅ (d) random 50/50.
4. **Short answer:** Why must the scaler live inside the CV pipeline? *(Answer: otherwise each validation fold's statistics leak into its own training via the globally fitted scaler; the pipeline refits per fold, keeping every validation fold unseen.)*
