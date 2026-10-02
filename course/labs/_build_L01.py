"""Builds Lab 1 starter + solution notebooks as valid .ipynb files."""
import nbformat as nbf

def build(path, cells):
    nb = nbf.v4.new_notebook()
    nb.cells = cells
    nb.metadata.kernelspec = {"name": "python3", "display_name": "Python 3"}
    with open(path, "w") as f:
        nbf.write(nb, f)
    print("wrote", path)

md = lambda s: nbf.v4.new_markdown_cell(s)
code = lambda s: nbf.v4.new_code_cell(s)

# ============================================================ STARTER
starter = [
md("""# Lab 1 — Load & Fix a Messy Dataset (C1)

**Scenario:** You are a junior data analyst at a Singapore property analytics firm. A colleague exported `hdb_messy.csv` and something went wrong. Your job: produce a clean, typed DataFrame ready for scaling.

**Time budget:** 100 min. **Exit ticket:** cleaned CSV + one sentence on the hardest bug.

Run the progress tests any time: `pytest tests/ -v`"""),

md("## 0. Imports & load"),
code("""import pandas as pd
import numpy as np

df = pd.read_csv("data/hdb_messy.csv")
df.head()"""),

code("""# First audit — what's wrong here?
df.info()"""),

md("""## 1. Fix the price column
`resale_price` is a string like `$530,000`. Convert to float.
**Hint:** `str.replace` both `$` and `,`, then `astype(float)`."""),
code("""# TODO: convert resale_price to float
raise NotImplementedError()"""),

md("""## 2. Parse the dates
`sale_date` mixes `%Y-%m-%d` and `%d/%m/%Y` formats.
**Hint:** `pd.to_datetime(..., format="mixed", dayfirst=True)` or parse each format separately."""),
code("""# TODO: parse sale_date to datetime
raise NotImplementedError()"""),

md("""## 3. Handle missing values
`floor_area_sqm` has ~47 NaNs (plus implausible outliers like 9999 and -50); `storey` has a few.
Decide: drop, impute, or flag — and justify."""),
code("""# TODO: fix implausible floor_area values first, then handle NaNs
raise NotImplementedError()"""),

md("""## 4. Drop the duplicate column
`floor_area_sqm.1` is a stray export artefact. Note: it has a *different name*, so `df.columns.duplicated()` will NOT catch it — drop it by name."""),
code("""# TODO: drop the duplicate column
raise NotImplementedError()"""),

md("""## 5. Final audit & export
Sanity-check: dtypes, null counts, plausible ranges. Then export."""),
code("""# TODO: final audit + export to cleaned_hdb.csv
raise NotImplementedError()"""),

md("## Self-check\nRun `pytest tests/ -v` from the `starter/` folder. All tests should pass when you're done."),
]

# ============================================================ SOLUTION
solution = [
md("""# Lab 1 — SOLUTION (instructor reference)
Fully worked clean-up of `hdb_messy.csv` with commentary on each decision."""),
code("""import pandas as pd
import numpy as np

df = pd.read_csv("data/hdb_messy.csv")
df.info()  # 8 columns; resale_price is object; floor_area_sqm.1 duplicate; NaNs present"""),
md("### 1. Price: strip `$` and comma, cast to float"),
code("""df["resale_price"] = (df["resale_price"].str.replace("$", "", regex=False)
                        .str.replace(",", "", regex=False).astype(float))
df["resale_price"].dtype  # float64"""),
md("### 2. Dates: the format is mixed — parse with dayfirst for the dd/mm/yyyy rows"),
code("""df["sale_date"] = pd.to_datetime(df["sale_date"], format="mixed", dayfirst=True)
df["sale_date"].head()"""),
md("""### 3. Implausible values BEFORE imputation
9999, -50, 0 sqm are export bugs, not real flats. Treat as missing, then median-impute
(<1% of rows, roughly symmetric distribution → median is robust and simple)."""),
code("""bad = ~df["floor_area_sqm"].between(30, 250)
df.loc[bad, "floor_area_sqm"] = np.nan
df["floor_area_sqm"] = df["floor_area_sqm"].fillna(df["floor_area_sqm"].median())
df["storey"] = df["storey"].fillna(df["storey"].median())
df[["floor_area_sqm", "storey"]].isna().sum()  # 0, 0"""),
md("### 4. Duplicate column — note it has a *different name*, so `columns.duplicated()` won't catch it. Drop by name."),
code("""df = df.drop(columns=[\"floor_area_sqm.1\"])
assert "floor_area_sqm.1" not in df.columns"""),
md("### 5. Final audit + export"),
code("""assert df["resale_price"].dtype == float
assert df["resale_price"].between(100000, 2000000).all()
assert df["sale_date"].notna().all()
df.to_csv("cleaned_hdb.csv", index=False)
df.describe()"""),
md("**Teaching notes:** the most common learner errors — imputing *before* removing the 9999 outliers (median becomes garbage); using `errors='ignore'` in parsing (silently leaves bad values); forgetting the range sanity-check. The exit ticket asks which bug was hardest — expect 'the mixed dates' or 'the 9999 outlier'."),
]

build("L01_Messy_Data/starter/L01_starter.ipynb", starter)
build("L01_Messy_Data/solution/L01_solution.ipynb", solution)
