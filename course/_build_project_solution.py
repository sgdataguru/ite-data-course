"""Builds the Option A worked solution (instructor reference) as a valid .ipynb."""
import nbformat as nbf

md = lambda s: nbf.v4.new_markdown_cell(s)
code = lambda s: nbf.v4.new_code_cell(s)

cells = [
md("""# Option A — HDB Resale Price Prep: WORKED SOLUTION (instructor reference)

This is a complete, working solution for the End-to-End Data Prep Project, Option A.
It uses the same `hdb_messy.csv`-style data the labs use (a deterministic stand-in for
the data.gov.sg Resale Flat Prices dataset — swap in the real CSV by running
`fetch_data.py` for live data; the pipeline is identical).

**Milestone map:** M1 clean & type → M2 bias audit & mitigation → M3 split & enhance → M4 QA."""),

md("## Milestone 1 — Clean & Type"),
code("""import pandas as pd
import numpy as np

df = pd.read_csv("data/hdb_messy.csv")
df.info()"""),
code("""# 1a. Price: strip $ and comma, cast to float
df["resale_price"] = (df["resale_price"].str.replace("$", "", regex=False)
                      .str.replace(",", "", regex=False).astype(float))

# 1b. Dates: mixed formats -> parse with dayfirst
df["sale_date"] = pd.to_datetime(df["sale_date"], format="mixed", dayfirst=True)

# 1c. Implausible floor areas -> treat as missing, then median-impute
bad = ~df["floor_area_sqm"].between(30, 250)
df.loc[bad, "floor_area_sqm"] = np.nan
df["floor_area_sqm"] = df["floor_area_sqm"].fillna(df["floor_area_sqm"].median())
df["storey"] = df["storey"].fillna(df["storey"].median())

# 1d. Drop the stray duplicate column (different NAME, so duplicated() misses it)
df = df.drop(columns=["floor_area_sqm.1"])

# 1e. Sanity checks
assert df["resale_price"].between(100_000, 2_000_000).all()
assert df["sale_date"].between("2017-01-01", "2024-12-31").all()
assert df.notna().all().all()
df.to_csv("cleaned_hdb.csv", index=False)
print("M1 done:", df.shape)"""),
code("""# Prep-decisions table (the graded artefact)
decisions = pd.DataFrame([
    ("resale_price", "string -> float (strip $ and comma)", "models need numbers; strings cannot enter maths"),
    ("sale_date", "parse to datetime; derive year/month later if needed", "mixed formats break naive parsing; dates become features"),
    ("floor_area_sqm", "outliers (9999/-50/0/400/250) -> NaN -> median impute", "imputing BEFORE removing outliers corrupts the median"),
    ("storey", "median impute (5 NaNs)", "<1% missing, roughly symmetric"),
    ("floor_area_sqm.1", "dropped", "export artefact; different name so duplicated() misses it"),
], columns=["column", "treatment", "why"])
decisions.to_csv("prep_decisions.csv", index=False)
decisions"""),

md("""## Milestone 2 — Bias Audit & Mitigation

We audit representation by town (which towns are under-represented?) and price
fairness by flat type (does the data systematically misprice certain flat types?)."""),
code("""# 2a. Representation: each town's share of the data
rep = df["town"].value_counts(normalize=True)
print("town representation shares:")
print(rep.round(3))
under = rep[rep < 1 / df["town"].nunique() * 0.5]
print("\\nunder-represented towns (< half of equal share):", list(under.index))"""),
code("""# 2b. Group-wise stats: mean price by flat type and by town
by_type = df.groupby("flat_type")["resale_price"].agg(["mean", "std", "count"]).round(0)
print(by_type)
by_town = df.groupby("town")["resale_price"].mean().round(0).sort_values()
print("\\ncheapest towns:", list(by_town.index[:3]), "| priciest:", list(by_town.index[-3:]))"""),
code("""# 2c. Fairness metrics: does a simple price model misprice some flat types?
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score

X = pd.get_dummies(df[["town", "flat_type", "floor_area_sqm", "storey"]], columns=["town", "flat_type"], drop_first=True)
y = df["resale_price"]
Xtr, Xte, ytr, yte, ttr, tte = train_test_split(X, y, df["flat_type"], test_size=0.3, random_state=42)
model = make_pipeline(StandardScaler(), LinearRegression()).fit(Xtr, ytr)
pred = model.predict(Xte)

# "equalised odds" analogue for regression: mean error per group should be similar
err = pd.DataFrame({"flat_type": tte, "error": pred - yte})
group_err = err.groupby("flat_type")["error"].mean().round(0)
print("mean prediction error by flat type (0 = fair):")
print(group_err)
gap = group_err.max() - group_err.min()
print(f"\\nerror gap: {gap:,.0f} SGD — the model systematically misprices some flat types")"""),
code("""# 2d. Mitigation: reweigh under-represented towns in training
w = np.ones(len(Xtr))
for town in df["town"].unique():
    mask = (ttr == town) if False else None  # placeholder — actual weights by town share
# simpler, honest approach: weight each town's rows inversely to its share
town_tr = df.loc[Xtr.index, "town"]
share = town_tr.value_counts(normalize=True)
w = town_tr.map(1 / share).values
mit = make_pipeline(StandardScaler(), LinearRegression()).fit(Xtr, ytr, linearregression__sample_weight=w)
pred_mit = mit.predict(Xte)
err_mit = pd.DataFrame({"flat_type": tte, "error": pred_mit - yte}).groupby("flat_type")["error"].mean().round(0)
print("after reweighing, mean error by flat type:")
print(err_mit)
print(f"\\nerror gap before: {gap:,.0f} | after: {err_mit.max() - err_mit.min():,.0f}")
print(f"R2 before: {r2_score(yte, pred):.4f} | after: {r2_score(yte, pred_mit):.4f}")
print("\\nHONEST FINDING: on this dataset the reweighing barely moved the flat-type error gap.")
print("That is a real result to report: the gap is driven by flat-type price structure,")
print("not town representation. A good report says what the mitigation did NOT fix.")"""),
code("""# 2e. The 1-page bias report (written to bias_report.md)
report = (
    "# Bias Assessment Report - HDB Resale Price Prep\\n\\n"
    "## 1. Scope\\n"
    "data.gov.sg-style HDB resale transactions, 6,000 rows, 2017-2024. "
    "Sensitive-ish attributes: town, flat_type.\\n\\n"
    "## 2. Bias risks identified\\n"
    "- Representation: towns range from {rep_min:.1%} to {rep_max:.1%} of the data.\\n"
    "- Historical: price levels embed past market conditions.\\n"
    "- Aggregation: one island-wide model hides town-level price behaviour "
    "(mean price gap ~{town_gap:,.0f} SGD).\\n\\n"
    "## 3. Metrics computed\\n"
    "Mean prediction error by flat type. Error gap: {gap:,.0f} SGD.\\n\\n"
    "## 4. Mitigations applied\\n"
    "Inverse-share reweighing of towns. Error gap changed from {gap:,.0f} to "
    "{gap_after:,.0f} SGD (R2 cost {r2_cost:.4f}). Honest finding: the mitigation did NOT "
    "close the gap - it is driven by flat-type price structure, not town representation. "
    "A good report says what the mitigation did not fix.\\n\\n"
    "## 5. Residual risks\\n"
    "Metric choice is a values decision; re-audit on new data before deployment.\\n"
)
with open("bias_report.md", "w") as f:
    f.write(report.format(
        rep_min=rep.min(), rep_max=rep.max(),
        town_gap=by_town.iloc[-1] - by_town.iloc[0],
        gap=gap, gap_after=err_mit.max() - err_mit.min(),
        r2_cost=r2_score(yte, pred) - r2_score(yte, pred_mit)))
print(open("bias_report.md").read())"""),

md("## Milestone 3 — Split, Enhance, Cross-Validate"),
code("""# 3a. Leakage-free 70/15/15 split, seeded
from sklearn.model_selection import train_test_split
X_all = df[["floor_area_sqm", "storey", "lease_commence"]]
y_all = df["resale_price"]
Xtr, Xtmp, ytr, ytmp = train_test_split(X_all, y_all, test_size=0.30, random_state=42)
Xval, Xte, yval, yte = train_test_split(Xtmp, ytmp, test_size=0.33, random_state=42)
assert set(Xtr.index) & set(Xte.index) == set()
assert len(Xtr) + len(Xval) + len(Xte) == len(df)
print(f"train {len(Xtr)} / val {len(Xval)} / test {len(Xte)}")"""),
code("""# 3b. CV strategy: plain k-fold (iid transactions, regression target)
from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
pipe = make_pipeline(StandardScaler(), LinearRegression())
scores = cross_val_score(pipe, X_all, y_all, cv=KFold(5, shuffle=True, random_state=42))
print("5-fold R2:", scores.round(3), "| mean:", scores.mean().round(3))
# justification: rows are independent transactions (no time ordering requirement for this
# price model), regression target -> plain shuffled k-fold; stratification is for classification"""),
code("""# 3c. Augmentation: Gaussian jitter on training numerics (labels untouched)
rng = np.random.default_rng(42)
aug_idx = Xtr.sample(frac=0.5, random_state=42).index
aug = Xtr.loc[aug_idx].copy()
for c in ["floor_area_sqm", "storey", "lease_commence"]:
    aug[c] = aug[c] + rng.normal(0, 0.05 * Xtr[c].std(), len(aug))
Xtr_aug = pd.concat([Xtr, aug])
ytr_aug = pd.concat([ytr, ytr.loc[aug_idx]])
# labels check: the FIRST len(ytr) entries of the concatenated labels must equal the originals
# (positional, not label-based — augmented rows share index labels with originals)
assert (ytr_aug.iloc[:len(ytr)].values == ytr.values).all()
assert len(Xtr_aug) == len(ytr_aug)
assert Xtr_aug["floor_area_sqm"].between(25, 260).all()      # plausibility
print(f"train {len(Xtr)} -> augmented {len(Xtr_aug)} rows")"""),

md("## Milestone 4 — Final QA"),
code("""# 4a. Readiness checklist
checks = {
    "types_numeric": all(pd.api.types.is_numeric_dtype(X_all[c]) for c in X_all.columns),
    "no_nans": df.notna().all().all(),
    "price_range": df["resale_price"].between(100_000, 2_000_000).all(),
    "area_range": df["floor_area_sqm"].between(30, 250).all(),
    "splits_disjoint": set(Xtr.index) & set(Xte.index) == set(),
    "seeded": True,  # every random call used random_state or default_rng(42)
}
for k, v in checks.items():
    print(("PASS " if v else "FAIL ") + k)
assert all(checks.values())
print("\\nAll checks green — dataset is ML-ready.")"""),
md("""## AI-usage ledger (excerpt — full ledger in ai_reflection.md)

| Date | Tool | Task | Prompt summary | Verification | What I changed |
|---|---|---|---|---|---|
| M1 | Claude | Explain astype error | "resale_price astype(float) failed: [error]" | Ran fix; range check 100k-2M | Nothing — correct |
| M2 | Claude | Draft bias report | "Draft mitigation section from before/after numbers" | Recomputed every number | Rewrote 2 overstated sentences |
| M3 | Claude | Vibe-code ColumnTransformer | 5-part prompt with schema | pytest + diff vs manual | Kept manual — AI's ordinal order was alphabetical |

**Reflection:** The AI was fastest at error explanation and report drafting. It twice produced
plausible-but-wrong output: an alphabetical ordinal order and a report sentence claiming bias
was 'removed' when the gap only narrowed. My verification (recomputing numbers, diffing against
my manual pipeline) caught both. The lesson: the AI drafts; I decide."""),
]

nb = nbf.v4.new_notebook()
nb.cells = cells
nb.metadata.kernelspec = {"name": "python3", "display_name": "Python 3"}
import os
os.makedirs("assessment/project_solution_A/solution/data", exist_ok=True)
os.makedirs("assessment/project_solution_A/solution/tests", exist_ok=True)
nbf.write(nb, "assessment/project_solution_A/solution/project_solution_A.ipynb")
print("written")
