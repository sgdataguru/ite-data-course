"""Builds C3 labs (L11-L18). Run from labs/."""
import nbformat as nbf
import shutil
from pathlib import Path

LABS = Path(__file__).resolve().parent
DATA = LABS / "data"
md = lambda s: nbf.v4.new_markdown_cell(s)
code = lambda s: nbf.v4.new_code_cell(s)

def build(lab_dir, starter_cells, solution_cells, dataset):
    for sub in ["starter/data", "starter/tests", "solution/data", "solution/tests"]:
        (LABS / lab_dir / sub).mkdir(parents=True, exist_ok=True)
    for sub, cells, name in [("starter", starter_cells, "starter.ipynb"),
                             ("solution", solution_cells, "solution.ipynb")]:
        nb = nbf.v4.new_notebook(); nb.cells = cells
        nb.metadata.kernelspec = {"name": "python3", "display_name": "Python 3"}
        nbf.write(nb, LABS / lab_dir / sub / f"{lab_dir.split('_')[0]}_{name}")
    if dataset:
        for sub in ["starter/data", "solution/data"]:
            shutil.copy(DATA / dataset, LABS / lab_dir / sub / dataset)
    print("built", lab_dir)

# L11 Splits & leakage
build("L11_Splits_Leakage",
[md("""# Lab 11 — Splits in Practice (C3)
Build 70/15/15 splits; demonstrate leakage by scaling BEFORE vs AFTER splitting; measure the score difference.
`pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/cleaned_hdb.csv')"),
 md("## 1. Seeded 70/15/15 split"),
 code("# TODO: two train_test_split calls, random_state=42\nraise NotImplementedError()"),
 md("## 2. The leakage demo: scaler BEFORE split (buggy) vs AFTER (correct)"),
 code("# TODO: fit scaler on full data vs train only; compare KNN scores\nraise NotImplementedError()"),
 md("## 3. Assert no overlap"),
 code("# TODO: assert train/test indices are disjoint\nraise NotImplementedError()")],
[md("# Lab 11 — SOLUTION"),
 code("""import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("data/cleaned_hdb.csv")
X, y = df[["floor_area_sqm", "storey", "lease_commence"]], df["resale_price"]
Xtr, Xtmp, ytr, ytmp = train_test_split(X, y, test_size=0.30, random_state=42)
Xval, Xte, yval, yte = train_test_split(Xtmp, ytmp, test_size=0.33, random_state=42)
assert len(set(Xtr.index) & set(Xte.index)) == 0

# buggy: fit scaler on FULL data before split
sc_bug = StandardScaler().fit(X)
Xtr_b, Xte_b = sc_bug.transform(Xtr), sc_bug.transform(Xte)
# correct: fit on train only
sc_ok = StandardScaler().fit(Xtr)
Xtr_o, Xte_o = sc_ok.transform(Xtr), sc_ok.transform(Xte)

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(Xtr_b, ytr); bug = r2_score(yte, knn.predict(Xte_b))
knn.fit(Xtr_o, ytr); ok = r2_score(yte, knn.predict(Xte_o))
print(f"leaky: {bug:.4f} | correct: {ok:.4f} | difference: {bug-ok:+.4f}")"""),
 md("**Teaching notes:** the score difference is usually small but real — the point is the *principle*, and the leakage grows with distribution shift. The disjoint-index assertion is the test the learners keep.")],
"cleaned_hdb.csv")

# L12 CV
build("L12_Cross_Validation",
[md("""# Lab 12 — KFold, StratifiedKFold, TimeSeriesSplit (C3)
Show why plain k-fold breaks time series (energy data) and why stratification matters (fraud data).
`pytest tests/ -v`"""),
 code("import pandas as pd\nenergy = pd.read_csv('data/energy_demand.csv')\nfraud = pd.read_csv('data/fraud.csv')"),
 md("## 1. TimeSeriesSplit on energy — no time travel"),
 code("# TODO: TimeSeriesSplit(5) fold visualisation\nraise NotImplementedError()"),
 md("## 2. StratifiedKFold on fraud — class ratios per fold"),
 code("# TODO: compare KFold vs StratifiedKFold fold class ratios\nraise NotImplementedError()"),
 md("## 3. Scaler INSIDE the CV loop"),
 code("# TODO: cross_val_score with a Pipeline\nraise NotImplementedError()")],
[md("# Lab 12 — SOLUTION"),
 code("""import pandas as pd, numpy as np
from sklearn.model_selection import KFold, StratifiedKFold, TimeSeriesSplit, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression

energy = pd.read_csv("data/energy_demand.csv").sort_values("date").reset_index(drop=True)
tss = TimeSeriesSplit(n_splits=5)
for i, (tr, te) in enumerate(tss.split(energy)):
    print(f"fold {i}: train {energy.date.iloc[tr].min()}..{energy.date.iloc[tr].max()} -> test {energy.date.iloc[te].min()}..{energy.date.iloc[te].max()}")

fraud = pd.read_csv("data/fraud.csv")
Xf, yf = fraud.drop(columns="is_fraud"), fraud.is_fraud
for name, cv in [("KFold", KFold(5, shuffle=True, random_state=42)), ("StratifiedKFold", StratifiedKFold(5, shuffle=True, random_state=42))]:
    ratios = [yf[te].mean() for _, te in cv.split(Xf, yf)]
    print(name, "fold positive ratios:", np.round(ratios, 3))

pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print("pipeline CV F1:", cross_val_score(pipe, Xf, yf, cv=StratifiedKFold(5, shuffle=True, random_state=42), scoring="f1").round(3))"""),
 md("**Teaching notes:** the fold-date printout makes time-travel visible (train always ends before test begins). The KFold vs StratifiedKFold ratio table shows the imbalance hazard directly.")],
None)

# L13 Augmentation
build("L13_Augmentation",
[md("""# Lab 13 — Augmentation on Tabular Data (C3)
Apply Gaussian jitter to HDB numerics; verify labels survive; compare distributions.
(Image augmentation demo: instructor-led with Fashion-MNIST subset — optional offline.)
`pytest tests/ -v`"""),
 code("import pandas as pd, numpy as np\ndf = pd.read_csv('data/cleaned_hdb.csv')"),
 md("## 1. Gaussian jitter (5% of std) on numeric features"),
 code("# TODO: jitter floor_area_sqm, storey; keep resale_price label unchanged\nraise NotImplementedError()"),
 md("## 2. Sanity checks: labels unchanged, distributions comparable"),
 code("# TODO: assert labels equal; plot before/after histograms\nraise NotImplementedError()")],
[md("# Lab 13 — SOLUTION"),
 code("""import pandas as pd, numpy as np, matplotlib.pyplot as plt
df = pd.read_csv("data/cleaned_hdb.csv")
rng = np.random.default_rng(42)
num_cols = ["floor_area_sqm", "storey", "lease_commence"]
aug = df.sample(frac=0.5, random_state=42).copy()
for c in num_cols:
    aug[c] = aug[c] + rng.normal(0, 0.05 * df[c].std(), len(aug))
combined = pd.concat([df, aug], ignore_index=True)
assert (combined.loc[:len(df)-1, "resale_price"].values == df.resale_price.values).all()
print("original:", len(df), "-> augmented total:", len(combined))
fig, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].hist(df.floor_area_sqm, bins=40, alpha=.6, label="orig")
ax[0].hist(aug.floor_area_sqm, bins=40, alpha=.6, label="aug")
ax[1].hist(df.storey, bins=30, alpha=.6, label="orig")
ax[1].hist(aug.storey, bins=30, alpha=.6, label="aug")
ax[0].legend(); plt.savefig("augmentation_check.png", dpi=120)
print("chart saved")"""),
 md("**Teaching notes:** jitter must never touch the label — the assertion is the teaching point. Distribution overlay shows augmentation adds density, not new shapes.")],
"cleaned_hdb.csv")

# L14 Synthetic data
build("L14_Synthetic_Data",
[md("""# Lab 14 — Synthetic Data with SMOTE + GenAI (C3)
Generate synthetic minority rows two ways: SMOTE, and a GenAI tool prompted with schema + statistics (NO raw rows).
Compare real vs synthetic distributions. `pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/minority_sample.csv')\ndf.label.value_counts()"),
 md("## 1. SMOTE synthesis"),
 code("# TODO: SMOTE on minority class only\nraise NotImplementedError()"),
 md("## 2. GenAI synthesis — prompt with schema + summary stats only"),
 code("""# TODO: build the prompt (schema + describe() output), paste into your AI tool,
# save the generated rows to genai_synthetic.csv, then load it here
raise NotImplementedError()"""),
 md("## 3. Distribution comparison + safety verdict"),
 code("# TODO: compare distributions; which synthetic set is safer to train on?\nraise NotImplementedError()")],
[md("# Lab 14 — SOLUTION"),
 code("""import pandas as pd, numpy as np
from imblearn.over_sampling import SMOTE

df = pd.read_csv("data/minority_sample.csv")
X, y = df.drop(columns="label"), df.label
sm = SMOTE(random_state=42, k_neighbors=3)
Xs, ys = sm.fit_resample(X, y)
smote_syn = pd.DataFrame(Xs, columns=X.columns).assign(label=ys)
minor = smote_syn[smote_syn.label == 1]
print("SMOTE minority rows:", len(minor))
print("real minority describe:\\n", df[df.label==1].describe().loc[["mean","std"]].round(2))
print("SMOTE minority describe:\\n", minor.describe().loc[["mean","std"]].round(2))
# GenAI comparison: learners bring genai_synthetic.csv; check plausibility constraints
# e.g., assert no negative feature values, class ratio preserved"""),
 md("**Teaching notes:** SMOTE interpolates (means match, variance shrinks); GenAI rows can hallucinate impossible values — the plausibility check (no negatives, ranges) is the graded critique. Never paste raw rows into the prompt — schema + stats only (M3 rule).")],
"minority_sample.csv")

# L15 Vibe coding
build("L15_Vibe_Coding",
[md("""# Lab 15 — Vibe Coding Data Prep (C3) — AI-ASSIST CORE LAB
Redo Lab 5's pipeline entirely vibe-coded: prompt → draft → run → verify → refine.
**Baseline:** your Lab 5 manual solution (for diffing). Keep a prompt log.
**Rules (Agent 4):** attempt/compare, verify with the 6-point checklist, reflect 3-5 lines."""),
 code("# TODO: paste your Lab 5 prep-decisions table here as the manual baseline\nraise NotImplementedError()"),
 md("## Prompt log — one row per prompt: intent, prompt, outcome"),
 code("""# TODO: prompt_log = [(intent, prompt_summary, outcome), ...]
raise NotImplementedError()"""),
 md("## Diff: AI output vs your manual baseline"),
 code("# TODO: what the AI got right / wrong / what you changed\nraise NotImplementedError()"),
 md("## Reflection (required, 3-5 lines)"),
 code("# TODO: reflection as Markdown\nraise NotImplementedError()")],
[md("# Lab 15 — SOLUTION (instructor: exemplar prompt log + diff)"),
 code("""prompt_log = [
 ("prep pipeline", "You are preparing an HDB dataset for KNN. Standardise floor_area_sqm, storey, lease_commence; one-hot town; ordinal-encode flat_type as 3<4<5<EXEC. Output a single sklearn ColumnTransformer.", "correct structure, but AI label-encoded town first attempt — refined"),
 ("fix", "town is nominal — use OneHotEncoder(handle_unknown='ignore')", "fixed"),
]
# Typical diff findings: AI picks correct scalers but forgets handle_unknown;
# AI's ordinal order was alphabetical until explicitly constrained;
# AI could not justify WHY tree prep skips scaling — the human added the rationale.
reflection = "AI got the pipeline structure right and fast. It label-encoded town (wrong) and could not justify treatment choices. I fixed the encoding, added handle_unknown, and wrote the rationale myself."
print(prompt_log, reflection)"""),
 md("**Teaching notes:** the graded artefacts are the prompt log + reflection, not the code. The 6-point checklist: runs, seeded, leakage-free, spot-checked, APIs real, constraints respected.")],
"cleaned_hdb.csv")

# L16 Critique & fix
build("L16_Critique_Fix",
[md("""# Lab 16 — Critiquing & Fixing AI Output (C3) — AI-ASSIST CORE LAB
Three AI-generated prep scripts are in `data/`. Each contains ONE planted failure:
1. hallucinated API, 2. SMOTE before split, 3. test-set leakage.
Find, explain, and fix all three. `pytest tests/ -v`"""),
 code("# TODO: read data/script_1.py, data/script_2.py, data/script_3.py — find the bug in each\nraise NotImplementedError()"),
 md("## Fixes with explanations"),
 code("# TODO: fixed versions + one-paragraph explanation each\nraise NotImplementedError()")],
[md("# Lab 16 — SOLUTION"),
 code("""# script_1 bug: hallucinated API — sklearn has no 'preprocessing.TargetEncoder' in older versions
#   fix: from sklearn.preprocessing import TargetEncoder requires >=1.3; else use category_encoders
# script_2 bug: SMOTE applied BEFORE train_test_split — test set is synthetic-balanced
#   fix: imblearn Pipeline([('smote', SMOTE(...)), ('clf', ...)]) so resampling happens per training fold
# script_3 bug: scaler fitted on X (full data) then split — train-test contamination
#   fix: split first; fit scaler on X_train only; transform X_test with it
print("All three failures map to S28's taxonomy: hallucinated API, silent correctness bug, leakage.")"""),
 md("**Teaching notes:** learners run each script, observe crash vs silent-wrongness (script 1 crashes; 2 and 3 run fine and lie). The one-paragraph explanations are graded — naming the failure class matters more than the fix.")],
None)

# L17 Prompt library
build("L17_Prompt_Library",
[md("""# Lab 17 — Prompt Library Build (C3) — AI-ASSIST CORE LAB
Build a personal library of 8+ tested prompts (one per module topic) using the 5-part structure:
role, context, schema, constraints, examples. Test each on a real task.
**Deliverable:** `my_prompt_library.md`. `pytest tests/ -v`"""),
 code("# TODO: draft 8 prompts (cleaning, scaling, encoding, imbalance, metrics, mitigation, splitting, QA)\nraise NotImplementedError()"),
 md("## Test each prompt on a real task; record pass/fail of the 6-point checklist"),
 code("# TODO: test log\nraise NotImplementedError()")],
[md("# Lab 17 — SOLUTION (exemplar entries)"),
 code("""library = '''
## Encoding prompt (tested on Lab 3 task)
Role: You are preparing an HDB dataset for a gradient-boosting model.
Context: 6000 rows, Singapore resale transactions.
Schema: town (str, 10 nominal values), flat_type (str, ordinal 3-ROOM<4-ROOM<5-ROOM<EXECUTIVE).
Constraints: pandas + sklearn only; one-hot for town with handle_unknown='ignore'; explicit ordinal categories.
Example: "BEDOK" -> one-hot vector; "EXECUTIVE" -> 3.
'''
# 6-point checklist per prompt: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected
print(library)"""),
 md("**Teaching notes:** the library is a career artefact — graded on structure (all 5 parts present) and evidence of testing (checklist results recorded), not on the AI's answers.")],
None)

# L18 Final QA
build("L18_Final_QA",
[md("""# Lab 18 — Final Dataset QA & Readiness Checklist (C3)
Run the data-readiness checklist on your project dataset: types, leakage, balance, distributions, constraints, documentation.
Fix every red flag. `pytest tests/ -v`"""),
 code("# TODO: implement the checklist runner (or vibe-code it, then verify)\nraise NotImplementedError()"),
 md("## Run on your dataset; record green/justified per item"),
 code("# TODO: checklist results table\nraise NotImplementedError()")],
[md("# Lab 18 — SOLUTION"),
 code("""import pandas as pd, numpy as np

def readiness_checklist(df, target=None, constraints=None):
    results = {}
    results["types_numeric_or_code"] = all(pd.api.types.is_numeric_dtype(df[c]) for c in df.columns if c != target)
    if target:
        results["no_nans_target"] = df[target].notna().all()
        results["class_balance_reported"] = df[target].value_counts(normalize=True).round(3).to_dict()
    if constraints:
        results["domain_constraints"] = {c: bool(df[c].between(lo, hi).all()) for c, (lo, hi) in constraints.items()}
    return results

df = pd.read_csv("data/cleaned_hdb.csv")
print(readiness_checklist(df, target=None, constraints={"floor_area_sqm": (30, 250), "storey": (1, 30)}))"""),
 md("**Teaching notes:** the checklist is the project's final gate. Learners who vibe-code the runner must verify it covers leakage — AI checklists often skip it (a planted M3 lesson).")],
"cleaned_hdb.csv")

print("C3 labs built")
