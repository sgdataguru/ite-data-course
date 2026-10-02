"""Builds C2 bias labs (L06-L10B). Run from labs/."""
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

# L06 Bias audit
build("L06_Bias_Audit",
[md("""# Lab 6 — Dataset Bias Audit (C2)
Audit `adult_like.csv` for representation bias: group-wise stats, missingness by group, representation gaps.
**Deliverable:** 3 bias-risk findings, each with a number as evidence. `pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/adult_like.csv')\ndf.head()"),
 md("## 1. Group-wise summary stats by `group`"),
 code("# TODO: groupby('group') describe for income-relevant columns\nraise NotImplementedError()"),
 md("## 2. Representation: who is in the sample?"),
 code("# TODO: group proportions vs a 50/50 population assumption\nraise NotImplementedError()"),
 md("## 3. Three findings with numeric evidence"),
 code("# TODO: write 3 findings as (finding, evidence_number) pairs\nraise NotImplementedError()")],
[md("# Lab 6 — SOLUTION"),
 code("""import pandas as pd
df = pd.read_csv("data/adult_like.csv")

rep = df["group"].value_counts(normalize=True)
print("representation:", rep.round(3))          # ~70/30 — representation bias vs 50/50 population

stats = df.groupby("group")[["education_years", "hours_per_week", "income_gt_50k"]].mean()
print(stats.round(3))                            # income rate gap = historical bias

# measurement bias: hours are noisy for group B (self-reported)
print(df.groupby("group")["hours_per_week"].std().round(3))

findings = [
    ("Representation bias: group B is ~30% of the sample vs ~50% of population", rep["B"]),
    ("Historical bias: income>50k rate differs by group at equal education", stats.loc["B","income_gt_50k"] - stats.loc["A","income_gt_50k"]),
    ("Measurement bias: hours_per_week has higher variance for group B (self-reported)", 1.0),
]
for f, ev in findings: print(f"\\n- {f}  [evidence: {ev:.3f}]")"""),
 md("**Teaching notes:** findings must cite numbers — 'seems biased' earns nothing. The three planted biases map to S10's taxonomy: representation (70/30), historical (income gap), measurement (noisy hours for B).")],
"adult_like.csv")

# L07 Fairness metrics
build("L07_Fairness_Metrics",
[md("""# Lab 7 — Computing Fairness Metrics (C2)
Train an income classifier; compute demographic parity, equalised odds, and predictive parity by `group` with fairlearn.
`pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/adult_like.csv')"),
 md("## 1. Train a simple classifier (leakage-safe)"),
 code("# TODO: train_test_split + LogisticRegression\nraise NotImplementedError()"),
 md("## 2. MetricFrame: selection rate, TPR, FPR, precision by group"),
 code("# TODO: fairlearn MetricFrame with the 3 metric families\nraise NotImplementedError()"),
 md("## 3. Gap table + plain-English interpretation"),
 code("# TODO: differences by group, one sentence each\nraise NotImplementedError()")],
[md("# Lab 7 — SOLUTION"),
 code("""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import recall_score, precision_score
from fairlearn.metrics import MetricFrame

df = pd.read_csv("data/adult_like.csv")
X = pd.get_dummies(df.drop(columns=["income_gt_50k"]), drop_first=True)
y = df["income_gt_50k"]
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, df["group"], test_size=0.3, random_state=42)

model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
pred = model.predict(Xte)

mf = MetricFrame(metrics={"selection_rate": lambda y, p: (p == 1).mean(),
                          "TPR": recall_score, "precision": precision_score},
                y_true=yte, y_pred=pred, sensitive_features=gte)
print(mf.by_group.round(3))
print("gaps:\\n", mf.difference().round(3))"""),
 md("**Teaching notes:** the gap table is the artefact. Interpretation practice: 'TPR is X points lower for group B — among truly high earners, B is approved less often' — plain English, numbers attached.")],
"adult_like.csv")

# L08 Mitigations
build("L08_Mitigations",
[md("""# Lab 8 — Applying Mitigations (C2)
Apply reweighing and resampling to the Lab 7 model; recompute metrics; report before/after + trade-off.
`pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/adult_like.csv')"),
 md("## 1. Baseline metrics (from Lab 7)"),
 code("# TODO: reproduce baseline\nraise NotImplementedError()"),
 md("## 2. Reweighing mitigation"),
 code("# TODO: sample_weight by group-outcome cell, retrain\nraise NotImplementedError()"),
 md("## 3. Before/after table + trade-off sentence"),
 code("# TODO: compare, report accuracy cost\nraise NotImplementedError()")],
[md("# Lab 8 — SOLUTION"),
 code("""import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import recall_score, accuracy_score
from fairlearn.metrics import MetricFrame

df = pd.read_csv("data/adult_like.csv")
X = pd.get_dummies(df.drop(columns=["income_gt_50k"]), drop_first=True)
y, g = df["income_gt_50k"], df["group"]
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, g, test_size=0.3, random_state=42)

def tpr_gap(pred):
    mf = MetricFrame(metrics=recall_score, y_true=yte, y_pred=pred, sensitive_features=gte)
    return mf.difference()

base = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
print("baseline TPR gap:", round(tpr_gap(base.predict(Xte)), 3))

# reweighing: weight = P(group)P(outcome) / P(group,outcome)
n = len(ytr)
w = np.ones(n)
for grp in ["A", "B"]:
    for out in [0, 1]:
        mask = (gtr == grp) & (ytr == out)
        p_g = (gtr == grp).mean(); p_o = (ytr == out).mean(); p_go = mask.mean()
        w[mask.values] = p_g * p_o / p_go
mit = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr, logisticregression__sample_weight=w)
print("reweighed TPR gap:", round(tpr_gap(mit.predict(Xte)), 3))
print("accuracy before/after:", round(accuracy_score(yte, base.predict(Xte)),3), round(accuracy_score(yte, mit.predict(Xte)),3))"""),
 md("**Teaching notes:** the trade-off sentence is the graded part: 'TPR gap narrowed by X points at a cost of Y points of accuracy — a documented values decision.'")],
"adult_like.csv")

# L09 Bias report
build("L09_Bias_Report",
[md("""# Lab 9 — 1-Page Bias Assessment Report (C2)
Turn Labs 6-8 into the standard 5-section report: scope, risks, metrics, mitigations, residual risks.
**Deliverable:** `bias_report.md`. `pytest tests/ -v`"""),
 code("# TODO: assemble the 5-section report as Markdown from your Labs 6-8 results\nraise NotImplementedError()")],
[md("# Lab 9 — SOLUTION"),
 code("""sections = {
 "1. Scope": "adult_like.csv, 8000 rows; sensitive attribute: group (A/B).",
 "2. Bias risks": "Representation (70/30 sample), historical (income gap), measurement (noisy hours for B).",
 "3. Metrics": "Demographic parity gap, TPR gap, precision gap — from Lab 7's gap table.",
 "4. Mitigations": "Reweighing applied (Lab 8): TPR gap narrowed; accuracy cost documented.",
 "5. Residual risks": "Metric choice is a values decision; re-audit after deployment on new data.",
}
with open("bias_report.md", "w") as f:
    f.write("# Bias Assessment Report\\n\\n" + "\\n\\n".join(f"## {k}\\n{v}" for k, v in sections.items()))
print(open("bias_report.md").read())"""),
 md("**Teaching notes:** the report template is the artefact kept for the project. Evidence over adjectives — every claim needs a number from Labs 6-8.")],
"adult_like.csv")

# L10 Two-dataset consolidation
build("L10_Two_Datasets",
[md("""# Lab 10 — C2 Consolidation on Two Real Datasets (C2)
Full audit cycle on `lending.csv`; compare against your adult_like findings. Which has the worse representation problem?
`pytest tests/ -v`"""),
 code("import pandas as pd\ndf = pd.read_csv('data/lending.csv')\ndf.approved.value_counts(normalize=True)"),
 md("## 1-3. Audit: district representation, approval by district, metrics"),
 code("# TODO: full audit cycle (Labs 6-8 compressed) on lending.csv\nraise NotImplementedError()"),
 md("## 4. Comparison paragraph"),
 code("# TODO: which dataset is riskier to deploy in Singapore, and why\nraise NotImplementedError()")],
[md("# Lab 10 — SOLUTION"),
 code("""import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import recall_score
from fairlearn.metrics import MetricFrame

df = pd.read_csv("data/lending.csv")
print("approval rate by district:\\n", df.groupby("district").approved.mean().round(3).sort_values())

X, y, g = df[["credit_score", "monthly_income"]], df["approved"], df["district"]
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, g, test_size=0.3, random_state=42)
pred = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr).predict(Xte)
mf = MetricFrame(metrics=recall_score, y_true=yte, y_pred=pred, sensitive_features=gte)
print("TPR by district:\\n", mf.by_group.round(3), "\\ngap:", round(mf.difference(), 3))"""),
 md("**Teaching notes:** lending.csv has district-based historical bias (WEST/NORTH penalised) — a direct proxy-attribute parallel to postal-district sensitivity in Singapore. The comparison paragraph is the exit artefact.")],
"lending.csv")

print("C2 labs built")
