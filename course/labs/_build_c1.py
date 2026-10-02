"""Builds all remaining lab folders (L02-L18) with starter/solution notebooks,
tests, READMEs, requirements. Datasets are copied from labs/data/.
Run from labs/: python _build_rest.py"""
import nbformat as nbf
import shutil
from pathlib import Path

LABS = Path(__file__).resolve().parent
DATA = LABS / "data"

md = lambda s: nbf.v4.new_markdown_cell(s)
code = lambda s: nbf.v4.new_code_cell(s)

def build(lab_dir, starter_cells, solution_cells, dataset, extra_starter=None):
    for sub in ["starter/data", "starter/tests", "solution/data", "solution/tests"]:
        (LABS / lab_dir / sub).mkdir(parents=True, exist_ok=True)
    for sub, cells, name in [("starter", starter_cells, "starter.ipynb"),
                             ("solution", solution_cells, "solution.ipynb")]:
        nb = nbf.v4.new_notebook()
        nb.cells = cells
        nb.metadata.kernelspec = {"name": "python3", "display_name": "Python 3"}
        nbf.write(nb, LABS / lab_dir / sub / f"{lab_dir.split('_')[0]}_{name}")
    if dataset:
        for sub in ["starter/data", "solution/data"]:
            shutil.copy(DATA / dataset, LABS / lab_dir / sub / dataset)
    print("built", lab_dir)

REQ = """pandas==2.3.3
numpy==2.3.3
scikit-learn==1.6.1
imbalanced-learn==0.12.4
fairlearn==0.13.0
matplotlib==3.9.4
pytest==8.4.2
"""

# ================================================================ L02 Scaling
build("L02_Scaling",
[md("""# Lab 2 — Scaling Pipelines (C1)
Build StandardScaler / MinMaxScaler / RobustScaler pipelines on the cleaned HDB data.
Compare transformations of `floor_area_sqm` and `resale_price`; plot before/after.
**Self-check:** `pytest tests/ -v`"""),
 code("""import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

df = pd.read_csv("data/cleaned_hdb.csv")
X = df[["floor_area_sqm", "resale_price"]]
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
X_train.describe()"""),
 md("## 1. Fit three scalers on TRAIN ONLY, transform both"),
 code("# TODO: fit 3 scalers on X_train, transform X_train and X_test\nraise NotImplementedError()"),
 md("## 2. Inject an outlier and show why MinMax collapses"),
 code("# TODO: append a 400 sqm row, re-fit MinMaxScaler, observe the collapse\nraise NotImplementedError()"),
 md("## 3. Plot before/after distributions"),
 code("# TODO: matplotlib histograms, 3 scalers side by side\nraise NotImplementedError()"),
 md("## 4. Export the comparison chart"),
 code("# TODO: savefig('scaling_comparison.png')\nraise NotImplementedError()")],
[md("# Lab 2 — SOLUTION"),
 code("""import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

df = pd.read_csv("data/cleaned_hdb.csv")
X = df[["floor_area_sqm", "resale_price"]]
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

scalers = {"standard": StandardScaler(), "minmax": MinMaxScaler(), "robust": RobustScaler()}
fitted = {k: s.fit(X_train) for k, s in scalers.items()}
for k, s in fitted.items():
    tr = s.transform(X_train); te = s.transform(X_test)
    print(k, "train range", tr.min().round(2), tr.max().round(2), "| test range", te.min().round(2), te.max().round(2))

# outlier collapse demo
X_out = X_train.copy(); X_out.loc[0, "floor_area_sqm"] = 400
mm = MinMaxScaler().fit(X_out)
print("after 400sqm outlier, minmax range:", mm.data_min_.round(1), mm.data_max_.round(1))

fig, axes = plt.subplots(1, 4, figsize=(16, 3))
axes[0].hist(X_train.floor_area_sqm, bins=40); axes[0].set_title("raw")
for ax, (k, s) in zip(axes[1:], fitted.items()):
    ax.hist(s.transform(X_train)[:, 0], bins=40); ax.set_title(k)
plt.savefig("scaling_comparison.png", dpi=120)
print("chart saved")"""),
 md("**Teaching notes:** the key reveal is the outlier collapse — min-max squeezes real data into [0, 0.47] when a 400 sqm point enters. Learners must fit on train only; the test asserts transform ranges.")],
"cleaned_hdb.csv")

# ================================================================ L03 Encoding
build("L03_Encoding",
[md("""# Lab 3 — Encoding Categorical Data (C1)
Encode `town` (10 nominal), `flat_type` (ordinal), and a high-cardinality `street_name` appropriately.
**Self-check:** `pytest tests/ -v`"""),
 code("""import pandas as pd
df = pd.read_csv("data/cleaned_hdb.csv")
df[["town", "flat_type"]].nunique()"""),
 md("## 1. One-hot encode town"),
 code("# TODO: one-hot encode town\nraise NotImplementedError()"),
 md("## 2. Ordinal-encode flat_type with an EXPLICIT order"),
 code("# TODO: OrdinalEncoder with categories=[['3-ROOM','4-ROOM','5-ROOM','EXECUTIVE']]\nraise NotImplementedError()"),
 md("## 3. Report shapes before/after"),
 code("# TODO: compare column counts and memory\nraise NotImplementedError()")],
[md("# Lab 3 — SOLUTION"),
 code("""import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder

df = pd.read_csv("data/cleaned_hdb.csv")
ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
town_encoded = ohe.fit_transform(df[["town"]])
print("one-hot town ->", town_encoded.shape[1], "columns")

order = [["3-ROOM", "4-ROOM", "5-ROOM", "EXECUTIVE"]]
oe = OrdinalEncoder(categories=order)
df["flat_type_code"] = oe.fit_transform(df[["flat_type"]])
print("flat_type mapping:", dict(zip(order[0], range(4))))

print("before:", df.shape[1], "cols | after one-hot:", df.shape[1] - 1 + town_encoded.shape[1])"""),
 md("**Teaching notes:** alphabetical label-encoding of flat_type is the planted trap — EXECUTIVE would code below 3-ROOM. The explicit categories argument is the fix. High-cardinality discussion: with 8,000 streets, one-hot explodes; target encoding (fold-safe) is the C3 follow-up.")],
"cleaned_hdb.csv")

# ================================================================ L04 Imbalance
build("L04_Imbalance",
[md("""# Lab 4 — Imbalance & Algorithm-Aware Prep (C1)
The fraud dataset is 990:10. Diagnose, apply three strategies (fold-safe!), and compare accuracy vs F1.
**Self-check:** `pytest tests/ -v`"""),
 code("""import pandas as pd
df = pd.read_csv("data/fraud.csv")
df.is_fraud.value_counts()"""),
 md("## 1. Baseline: the lying metric"),
 code("# TODO: train KNN on raw data, report accuracy AND recall\nraise NotImplementedError()"),
 md("## 2. Three strategies — resample TRAINING FOLDS ONLY (imblearn Pipeline)"),
 code("# TODO: RandomUnderSampler, RandomOverSampler, SMOTE via imblearn.pipeline\nraise NotImplementedError()"),
 md("## 3. Compare accuracy vs F1 vs recall"),
 code("# TODO: results table\nraise NotImplementedError()")],
[md("# Lab 4 — SOLUTION"),
 code("""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler

df = pd.read_csv("data/fraud.csv")
X, y = df.drop(columns="is_fraud"), df.is_fraud
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

base = KNeighborsClassifier().fit(Xtr, ytr)
pred = base.predict(Xte)
print(f"baseline: acc={accuracy_score(yte,pred):.3f} recall={recall_score(yte,pred):.3f}")

results = []
for name, sampler in [("under", RandomUnderSampler(random_state=42)),
                      ("over", RandomOverSampler(random_state=42)),
                      ("SMOTE", SMOTE(random_state=42))]:
    pipe = Pipeline([("s", sampler), ("m", KNeighborsClassifier())]).fit(Xtr, ytr)
    p = pipe.predict(Xte)
    results.append((name, accuracy_score(yte,p), recall_score(yte,p), f1_score(yte,p)))
print(pd.DataFrame(results, columns=["strategy","accuracy","recall","F1"]).round(3))"""),
 md("**Teaching notes:** the baseline shows ~99% accuracy with near-zero recall — the 'lying metric' reveal. imblearn Pipeline resamples inside CV folds only; resampling before the split is the classic bug (revisited in Lab 16).")],
"fraud.csv")

# ================================================================ L05 C1 consolidation
build("L05_C1_MiniProject",
[md("""# Lab 5 — C1 Consolidation Mini-Project (C1)
End-to-end C1 on the HDB data: clean → scale → encode → prep for three algorithms.
**Deliverable:** notebook + prep-decisions table (column → treatment → why).
**Self-check:** `pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/cleaned_hdb.csv')\ndf.head()"),
 md("## 1-4. Full prep pipeline (TODO per section)"),
 code("# TODO: scale numerics, encode categoricals, assemble X for tree / KNN / logistic\nraise NotImplementedError()"),
 md("## 5. Prep-decisions table"),
 code("# TODO: DataFrame of column, treatment, rationale\nraise NotImplementedError()")],
[md("# Lab 5 — SOLUTION"),
 code("""import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv("data/cleaned_hdb.csv")
num = ["floor_area_sqm", "storey", "lease_commence"]
cat_nom = ["town"]
cat_ord = ["flat_type"]

# trees: no scaling needed; KNN/logistic: standardise numerics
prep_knn = ColumnTransformer([
    ("num", StandardScaler(), num),
    ("nom", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_nom),
    ("ord", OrdinalEncoder(categories=[["3-ROOM","4-ROOM","5-ROOM","EXECUTIVE"]]), cat_ord),
])
prep_tree = ColumnTransformer([
    ("num", "passthrough", num),
    ("nom", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_nom),
    ("ord", OrdinalEncoder(categories=[["3-ROOM","4-ROOM","5-ROOM","EXECUTIVE"]]), cat_ord),
])
decisions = pd.DataFrame([
    ("floor_area_sqm", "standardise (KNN/logistic) / passthrough (tree)", "distance & linear models are scale-sensitive; trees are not"),
    ("town", "one-hot", "nominal, 10 values — no fake order"),
    ("flat_type", "ordinal with explicit order", "genuinely ordered 3<4<5<EXEC"),
    ("storey", "standardise / passthrough", "numeric, same rule as area"),
], columns=["column", "treatment", "why"])
decisions.to_csv("prep_decisions.csv", index=False)
print(decisions)"""),
 md("**Teaching notes:** the decisions table is the graded artefact — justification matters more than code. Peer-review clinic (Lab 5B) audits this table against the algorithm-prep matrix.")],
"cleaned_hdb.csv")

print("C1 labs built")
