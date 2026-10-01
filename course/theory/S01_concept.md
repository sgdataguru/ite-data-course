# S01 — Data Types & Conversion for ML (C1, 1 hr)

## Concept Note

**Why types matter.** Machine learning models are mathematics: they multiply numbers. A pandas column of strings like `"1,200"` or `"N/A"` cannot enter a model until it becomes a number. Data type conversion is the first gate every dataset must pass.

**The core types.** Numeric (int, float), categorical (object/category), boolean, datetime. ML sees the world as: numbers for maths, integers for categories, and nothing else.

**Conversion in plain English.** You take a raw column and coerce it: `"1,200"` → `1200.0` (strip comma, cast to float); `"Y"/"N"` → `1/0`; `"2024-05-01"` → a datetime you can decompose into year, month, day-of-week.

**Worked example by hand.** An HDB resale CSV has a column `resale_price` with values `"\$530,000"` and `"N/A"`. Step 1: strip the `\$` and comma → `"530000"`. Step 2: decide what `N/A` means — missing (drop or impute) or zero (wrong — a missing price is not a free flat). Step 3: cast → 530000.0. Step 4: sanity-check — is the range plausible? A resale price of 53 or 53,000,000 signals a conversion bug.

**Formatting.** Dates become features (month of resale, age of flat). Text becomes categories. Units must be consistent — mixing SGD and USD in one column is a silent correctness bug.

**What you will later ask an AI to do:** convert a messy column with a one-line instruction; explain why a cast failed; write a validation check that flags implausible values after conversion.

## Slide Outline

1. **Title** — Why ML is picky about types. *Models do arithmetic; strings don't arithmetic.*
2. **The four data types** — numeric, categorical, boolean, datetime; what each looks like in pandas.
3. **What models actually accept** — numbers and integer codes; everything else must be transformed.
4. **Conversion = translation, not deletion** — preserve meaning while changing representation.
5. **Worked example: `"\$530,000"`** — strip → cast → sanity-check, step by step.
6. **Missing values are not zero** — `N/A` ≠ 0; the imputation decision comes later.
7. **Datetime decomposition** — a date is one column; year/month/weekday are three features.
8. **Silent failure modes** — mixed units, comma-decimal locales, leading zeros eaten by Excel.
9. **Sanity checks after conversion** — range, distribution, count of nulls before/after.
10. **Recap + lab preview** — Lab 1: you will fix a real messy CSV.

## Mini-Quiz

1. **MCQ:** A pandas column contains `"N/A"` strings where resale prices are missing. The worst automated choice is: (a) drop the rows (b) impute with the median (c) replace with 0 ✅ (d) keep as NaN and decide later.
2. **MCQ:** `"1,200"` fails `astype(float)` because: (a) floats can't be that large (b) the comma is not a numeric character ✅ (c) pandas requires ints (d) the string is too short.
3. **MCQ:** Converting `date_of_sale` to datetime and extracting `month` is useful because: (a) it reduces file size (b) it creates a numeric feature models can use ✅ (c) datetime is required by sklearn (d) it removes missing values.
4. **Short answer:** Give two sanity checks you would run on a price column immediately after converting it from string to float, and what bug each would catch. *(Answer: range check — catches comma/decimal misplacement; null count before vs after — catches silent coercion failures.)*
