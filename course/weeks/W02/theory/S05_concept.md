# S05 — Categorical Encoding (C1, 1 hr)

## Prerequisites — do these BEFORE this session

- [ ] Week 1 complete: Lab 1's cleaned_hdb.csv and Lab 2's scaling pipelines done
- [ ] You can already load a CSV and check dtypes with df.info()

## Python you need this week

- `df["town"].unique()` — list every different value in a column (no repeats)
- `df["town"].nunique()` — count how many different values exist
- `pd.get_dummies(df, columns=["town"])` — one-hot encode: one new 0/1 column per town
- `df["col"].map({"LOW": 0, "HIGH": 1})` — replace each value with the number you choose



## Concept Note

**The problem.** `town` in the HDB dataset has values like `ANG MO KIO`, `BEDOK`, `CLEMENTI`. Models need numbers. The three standard translations each carry a hidden assumption.

**One-hot encoding.** Create one 0/1 column per category. `BEDOK` → [0,1,0,0,...]. No fake ordering is imposed. Cost: a `town` with 26 values becomes 26 columns; a high-cardinality column (e.g., postal code) explodes the width. Use for nominal categories with modest cardinality.

**Label (ordinal) encoding.** Map each category to an integer: ANG MO KIO=0, BEDOK=1, CLEMENTI=2. Compact — but the model now believes BEDOK is "between" the others. Only legitimate when the category is genuinely ordered: `LOW < MEDIUM < HIGH` → 0, 1, 2.

**Target encoding.** Replace each category with the mean of the target for that category: if flats in BEDOK average \$520k, BEDOK → 520000. Powerful for high cardinality, but dangerous: it leaks the target into the feature and must be computed on training folds only (a cross-validation topic from C3).

**Worked example by hand.** Flat sizes: `EXECUTIVE`, `5-ROOM`, `4-ROOM`, `3-ROOM`. One-hot → 4 columns, no order. Label-encode alphabetically → EXECUTIVE=0, 5-ROOM=1... the model reads "5-ROOM is greater than EXECUTIVE" — nonsense. But encode by size order 3-ROOM=0, 4-ROOM=1, 5-ROOM=2, EXECUTIVE=3 and the integer now means something. **The encoding must match the meaning.**

**Rule of thumb:** nominal & few categories → one-hot; genuinely ordinal → label/ordinal; nominal & many categories → target (with care) or group rare categories.

**What you will later ask an AI to do:** choose an encoding given cardinality and model type; explain why one-hot exploded your memory; write a target encoder that respects fold boundaries.

## Slide Outline

1. **Title** — Turning words into numbers without lying.
2. **The hidden assumption** — every encoding tells the model a story about order.
3. **One-hot** — 0/1 columns; no fake order; the cardinality cost.
4. **Label/ordinal** — compact integers; only for true order.
5. **Target encoding** — category → mean target; power and leakage risk.
6. **Worked example: flat types** — alphabetical vs size-ordered encoding.
7. **Cardinality decision table** — few / ordered / many.
8. **The dummy variable trap** — collinearity when you keep all one-hot columns (conceptual).
9. **Rare categories** — group the tail into `OTHER` before encoding.
10. **Recap + lab preview** — Lab 3 applies all three encoders.

## Mini-Quiz

1. **MCQ:** `town` (26 nominal values) should usually be: (a) label-encoded (b) one-hot encoded ✅ (c) target-encoded with no safeguards (d) dropped.
2. **MCQ:** Label-encoding `RED, GREEN, BLUE` for a colour column is risky because: (a) colours can't be numbers (b) it invents an order the model will use ✅ (c) it uses too much memory (d) sklearn forbids it.
3. **MCQ:** Target encoding must be computed within training folds because: (a) it's faster (b) otherwise the target leaks into features ✅ (c) test sets have no target (d) one-hot is better anyway.
4. **Short answer:** A `postal_code` column has 8,000 distinct values. Why is one-hot a poor choice, and what would you do instead? *(Answer: 8,000 new sparse columns — memory and overfitting risk; instead group rare codes, use target encoding with fold-safe computation, or engineer district-level features.)*
