# S07 — Class Imbalance & Algorithm-Specific Prep (C1, 2 hrs)

## Prerequisites — do these BEFORE this session

- [ ] S05 (encoding) complete — you know one-hot vs ordinal
- [ ] Lab 3's encoded dataset is your starting point

## Python you need this week

- `df["label"].value_counts()` — count how many rows of each class (e.g. fraud vs not)
- `from imblearn.over_sampling import SMOTE` — borrow the SMOTE tool from imbalanced-learn
- `X_train, X_test, y_train, y_test = train_test_split(...)` — split data into a learning part and a testing part
- `from sklearn.neighbors import KNeighborsClassifier` — the KNN model — classifies by nearest neighbours



## Concept Note (Part 1: Imbalance)

**The problem.** A fraud dataset: 990 legitimate transactions, 10 fraudulent. A model that predicts "never fraud" is 99% accurate — and completely useless. Accuracy lies when classes are imbalanced.

**Two families of fixes:**

- **Undersampling** — randomly drop majority-class rows until classes balance. Cheap, but throws away data; risky when the majority class is small to begin with.
- **Oversampling** — duplicate minority-class rows. Keeps all data, but duplicates add no new information and can cause overfitting to the same examples.
- **SMOTE (Synthetic Minority Oversampling Technique)** — instead of copying, *interpolate*: pick a minority point, pick one of its minority neighbours, and create a new point on the line between them. New, plausible minority examples.

**Worked example by hand.** Minority points at (2, 2) and (4, 4). SMOTE picks a random fraction, say 0.5, and creates (3, 3) — halfway along the line. Repeat until balanced. Note what SMOTE does NOT do: it never invents a point far from real data, and it only interpolates *within* the minority class.

**When to use what:** large majority + cheap collection → undersample; small data → SMOTE; extreme imbalance → combine, and always evaluate with precision/recall or F1, never raw accuracy.

## Concept Note (Part 2: Algorithm-Specific Prep)

**Trees (decision tree, random forest, XGBoost).** Split on thresholds; scale-invariant; handle mixed types with modest encoding. Prep: encode categoricals, skip scaling.

**Distance-based (KNN, K-means, SVM).** Distances are dominated by large-range features. Prep: scaling is mandatory; one-hot with care (high-dimensional 0/1 columns distort distance).

**Linear (logistic/linear regression).** Coefficients assume comparable feature scales; standardisation helps optimisation converge. Prep: standardise numerics, encode categoricals, watch multicollinearity.

**The one-sentence summary:** prep is not generic — it is a function of the algorithm you plan to feed.

**What you will later ask an AI to do:** justify a resampling choice for a given imbalance ratio; write an imbalanced-learn pipeline that resamples training folds only; explain why a model's accuracy fell after SMOTE while recall rose.

## Slide Outline

1. **Title** — When 99% accuracy means failure.
2. **The lying metric** — the never-fraud model.
3. **Undersampling** — drop majority; cheap, lossy.
4. **Oversampling** — copy minority; no new information.
5. **SMOTE** — interpolate between minority neighbours; the (2,2)-(4,4) → (3,3) example.
6. **What SMOTE assumes** — local linear structure; fails for categorical-heavy data.
7. **Resampling belongs in training only** — never resample the test set.
8. **Evaluate with the right metric** — precision, recall, F1, confusion matrix.
9. **Algorithm prep: trees** — threshold splits; scale-invariant.
10. **Algorithm prep: distance-based** — scaling mandatory.
11. **Algorithm prep: linear** — standardise; watch collinearity.
12. **The prep decision matrix** — algorithm × prep requirement.
13. **Recap + lab preview** — Lab 4 applies SMOTE and per-algorithm prep.

## Mini-Quiz

1. **MCQ:** 99% accuracy on a 99:1 dataset most likely means: (a) excellent model (b) the model predicts the majority class ✅ (c) SMOTE worked (d) the test set leaked.
2. **MCQ:** SMOTE creates a new minority point by: (a) copying an existing point (b) interpolating between two minority neighbours ✅ (c) sampling from a normal distribution (d) duplicating a majority point.
3. **MCQ:** Which model needs scaling least? (a) KNN (b) SVM (c) decision tree ✅ (d) logistic regression.
4. **Short answer:** Why should resampling never be applied to the test set? *(Answer: the test set must reflect the real-world class distribution; resampling it changes what you're evaluating against and produces misleading metrics.)*
