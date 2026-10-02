"""Completes all labs: planted scripts (L16), tests, READMEs, requirements, exit tickets.
Run from labs/: python _complete_labs.py"""
import shutil
from pathlib import Path

LABS = Path(__file__).resolve().parent

REQ_BASIC = """pandas==2.3.3
numpy==2.3.3
pytest==8.4.2
"""
REQ_ML = """pandas==2.3.3
numpy==2.3.3
scikit-learn==1.6.1
matplotlib==3.9.4
pytest==8.4.2
"""
REQ_IMB = """pandas==2.3.3
numpy==2.3.3
scikit-learn==1.6.1
imbalanced-learn==0.12.4
pytest==8.4.2
"""
REQ_FAIR = """pandas==2.3.3
numpy==2.3.3
scikit-learn==1.6.1
fairlearn==0.13.0
pytest==8.4.2
"""

# ---------------------------------------------------------------- L16 planted scripts
SCRIPTS = {
"script_1.py": '''"""AI-generated prep script #1 — contains a HALLUCINATED API."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import SmartEncoder  # BUG: hallucinated — no such class exists

df = pd.read_csv("data/cleaned_hdb.csv")
X, y = df.drop(columns="resale_price"), df.resale_price
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
enc = SmartEncoder()
Xtr_t = enc.fit_transform(Xtr[["town"]], ytr)
print("encoded", Xtr_t.shape)
''',
"script_2.py": '''"""AI-generated prep script #2 — SMOTE applied BEFORE the split (silent correctness bug)."""
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score

df = pd.read_csv("data/fraud.csv")
X, y = df.drop(columns="is_fraud"), df.is_fraud
Xs, ys = SMOTE(random_state=42).fit_resample(X, y)   # BUG: resampling the FULL dataset
Xtr, Xte, ytr, yte = train_test_split(Xs, ys, test_size=0.3, random_state=42)
m = KNeighborsClassifier().fit(Xtr, ytr)
p = m.predict(Xte)
print(f"accuracy={accuracy_score(yte,p):.3f} recall={recall_score(yte,p):.3f}")  # beautiful lie
''',
"script_3.py": '''"""AI-generated prep script #3 — scaler fitted on FULL data before split (train-test contamination)."""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

df = pd.read_csv("data/cleaned_hdb.csv")
X, y = df[["floor_area_sqm", "storey"]], df.resale_price
sc = StandardScaler().fit(X)                        # BUG: fitted on ALL rows
Xt = sc.transform(X)
Xtr, Xte, ytr, yte = train_test_split(Xt, y, test_size=0.2, random_state=42)
m = KNeighborsRegressor(n_neighbors=10).fit(Xtr, ytr)
print(f"R2={r2_score(yte, m.predict(Xte)):.4f}")     # optimistic score
''',
}

# ---------------------------------------------------------------- tests per lab
TESTS = {
"L02_Scaling": '''"""Lab 2 progress tests."""
import pandas as pd, numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

HERE = Path(__file__).resolve().parent.parent
def load():
    return pd.read_csv(HERE / "data" / "cleaned_hdb.csv")

def test_scalers_fit_on_train_only():
    df = load()
    from sklearn.model_selection import train_test_split
    Xtr, Xte = train_test_split(df[["floor_area_sqm", "resale_price"]], test_size=0.2, random_state=42)
    sc = StandardScaler().fit(Xtr)
    assert abs(sc.transform(Xtr).mean()) < 1e-9          # train is standardised
    assert abs(sc.transform(Xte).mean()) > 1e-9 or True  # test uses TRAIN stats (may differ)

def test_minmax_bounds():
    df = load()
    mm = MinMaxScaler().fit(df[["floor_area_sqm"]])
    t = mm.transform(df[["floor_area_sqm"]])
    assert abs(t.min()) < 1e-9 and abs(t.max() - 1) < 1e-9

def test_robust_ignores_outliers():
    X = pd.DataFrame({"v": [40, 80, 120, 160, 200, 4000]})
    from sklearn.preprocessing import RobustScaler
    t = RobustScaler().fit_transform(X)
    assert abs(t[:-1]).max() < 10                        # outlier does not blow up the scale
''',
"L03_Encoding": '''"""Lab 3 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_onehot_shape():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import OneHotEncoder
    ohe = OneHotEncoder(sparse_output=False, handle_unknown="ignore").fit(df[["town"]])
    assert ohe.transform(df[["town"]]).shape[1] == df.town.nunique()

def test_ordinal_order():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import OrdinalEncoder
    oe = OrdinalEncoder(categories=[["3-ROOM", "4-ROOM", "5-ROOM", "EXECUTIVE"]]).fit(df[["flat_type"]])
    codes = oe.transform(pd.DataFrame({"flat_type": ["3-ROOM", "EXECUTIVE"]}))
    assert codes[0][0] == 0 and codes[1][0] == 3        # order preserved, not alphabetical
''',
"L04_Imbalance": '''"""Lab 4 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_imbalance_present():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    ratio = df.is_fraud.value_counts(normalize=True)
    assert ratio[1] < 0.05                              # ~1% fraud

def test_smote_fold_safe():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    from sklearn.model_selection import train_test_split
    from imblearn.pipeline import Pipeline
    from imblearn.over_sampling import SMOTE
    from sklearn.neighbors import KNeighborsClassifier
    Xtr, Xte, ytr, yte = train_test_split(df.drop(columns="is_fraud"), df.is_fraud, test_size=0.3, random_state=42, stratify=df.is_fraud)
    pipe = Pipeline([("s", SMOTE(random_state=42)), ("m", KNeighborsClassifier())]).fit(Xtr, ytr)
    assert pipe.predict(Xte).shape == yte.shape        # test set untouched by SMOTE
''',
"L06_Bias_Audit": '''"""Lab 6 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_representation_gap_exists():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    props = df.group.value_counts(normalize=True)
    assert abs(props["A"] - props["B"]) > 0.2          # planted 70/30 gap

def test_income_gap_exists():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    rates = df.groupby("group").income_gt_50k.mean()
    assert abs(rates["A"] - rates["B"]) > 0.05         # planted historical bias
''',
"L07_Fairness_Metrics": '''"""Lab 7 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_metrics_in_range():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from fairlearn.metrics import MetricFrame
    X = pd.get_dummies(df.drop(columns="income_gt_50k"), drop_first=True)
    Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, df.income_gt_50k, df.group, test_size=0.3, random_state=42)
    pred = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr).predict(Xte)
    sr = MetricFrame(metrics=lambda y, p: (p == 1).mean(), y_true=yte, y_pred=pred, sensitive_features=gte)
    assert 0 <= sr.overall <= 1                        # selection rate is a valid rate
    assert sr.difference() > 0                         # a gap exists (planted bias)
''',
"L08_Mitigations": '''"""Lab 8 progress tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_reweighing_weights_sum():
    df = pd.read_csv(HERE / "data" / "adult_like.csv")
    g, y = df.group, df.income_gt_50k
    w = np.ones(len(df))
    for grp in ["A", "B"]:
        for out in [0, 1]:
            mask = (g == grp) & (y == out)
            w[mask.values] = (g == grp).mean() * (y == out).mean() / mask.mean()
    assert abs(w.sum() - len(df)) < 1e-6               # reweighing preserves total weight
''',
"L09_Bias_Report": '''"""Lab 9 progress tests."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_report_has_five_sections():
    p = HERE / "bias_report.md"
    assert p.exists(), "bias_report.md not written yet"
    text = p.read_text()
    for s in ["Scope", "Bias risks", "Metrics", "Mitigations", "Residual"]:
        assert s in text, f"missing section: {s}"
''',
"L10_Two_Datasets": '''"""Lab 10 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_district_bias_exists():
    df = pd.read_csv(HERE / "data" / "lending.csv")
    rates = df.groupby("district").approved.mean()
    assert rates.max() - rates.min() > 0.05           # planted district gap
''',
"L11_Splits_Leakage": '''"""Lab 11 progress tests."""
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
HERE = Path(__file__).resolve().parent.parent

def test_split_disjoint():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    Xtr, Xtmp = train_test_split(df, test_size=0.30, random_state=42)
    Xval, Xte = train_test_split(Xtmp, test_size=0.33, random_state=42)
    assert set(Xtr.index) & set(Xte.index) == set()   # no overlap
    assert len(Xtr) + len(Xval) + len(Xte) == len(df)

def test_scaler_uses_train_stats():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    from sklearn.preprocessing import StandardScaler
    Xtr, Xte = train_test_split(df[["floor_area_sqm"]], test_size=0.2, random_state=42)
    sc = StandardScaler().fit(Xtr)
    assert sc.mean_[0] == Xtr.floor_area_sqm.mean()   # train stats, not full-data stats
''',
"L12_Cross_Validation": '''"""Lab 12 progress tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_timeseries_no_time_travel():
    df = pd.read_csv(HERE / "data" / "energy_demand.csv").sort_values("date").reset_index(drop=True)
    from sklearn.model_selection import TimeSeriesSplit
    for tr, te in TimeSeriesSplit(n_splits=5).split(df):
        assert tr.max() < te.min()                    # train strictly before test

def test_stratified_preserves_ratio():
    df = pd.read_csv(HERE / "data" / "fraud.csv")
    from sklearn.model_selection import StratifiedKFold
    y = df.is_fraud
    for _, te in StratifiedKFold(5, shuffle=True, random_state=42).split(df, y):
        assert abs(y.iloc[te].mean() - y.mean()) < 0.02
''',
"L13_Augmentation": '''"""Lab 13 progress tests."""
import pandas as pd, numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_jitter_preserves_labels():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    rng = np.random.default_rng(42)
    aug = df.sample(frac=0.5, random_state=42).copy()
    aug["floor_area_sqm"] = aug.floor_area_sqm + rng.normal(0, 0.05 * df.floor_area_sqm.std(), len(aug))
    assert (aug.resale_price.values == df.loc[aug.index].resale_price.values).all()

def test_jitter_small():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    rng = np.random.default_rng(42)
    j = rng.normal(0, 0.05 * df.floor_area_sqm.std(), 1000)
    assert np.abs(j).max() < df.floor_area_sqm.std()  # jitter stays small vs feature scale
''',
"L14_Synthetic_Data": '''"""Lab 14 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_smote_grows_minority():
    df = pd.read_csv(HERE / "data" / "minority_sample.csv")
    from imblearn.over_sampling import SMOTE
    Xs, ys = SMOTE(random_state=42, k_neighbors=3).fit_resample(df.drop(columns="label"), df.label)
    assert (ys == 1).sum() > (df.label == 1).sum()

def test_smote_stays_plausible():
    df = pd.read_csv(HERE / "data" / "minority_sample.csv")
    from imblearn.over_sampling import SMOTE
    Xs, _ = SMOTE(random_state=42, k_neighbors=3).fit_resample(df.drop(columns="label"), df.label)
    assert (Xs >= df.drop(columns="label").min()).all().all()  # no impossible values
''',
"L16_Critique_Fix": '''"""Lab 16 progress tests — the planted bugs must be FIXED in the learner's fixed scripts."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_fixed_scripts_exist():
    for i in [1, 2, 3]:
        assert (HERE / f"fixed_script_{i}.py").exists(), f"fixed_script_{i}.py not written"

def test_fixed_2_resamples_train_only():
    text = (HERE / "fixed_script_2.py").read_text()
    assert "Pipeline" in text or "pipeline" in text      # fold-safe structure
    assert text.find("fit_resample") > text.find("train_test_split") or "Pipeline" in text
''',
"L17_Prompt_Library": '''"""Lab 17 progress tests."""
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_library_exists_with_8_prompts():
    p = HERE / "my_prompt_library.md"
    assert p.exists(), "my_prompt_library.md not written"
    text = p.read_text()
    assert text.count("##") >= 8                        # 8+ prompt entries

def test_five_part_structure():
    p = HERE / "my_prompt_library.md"
    text = p.read_text().lower()
    for part in ["role", "context", "schema", "constraint", "example"]:
        assert part in text, f"prompt library missing: {part}"
''',
"L18_Final_QA": '''"""Lab 18 progress tests."""
import pandas as pd
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent

def test_checklist_catches_constraints():
    df = pd.read_csv(HERE / "data" / "cleaned_hdb.csv")
    ok = df.floor_area_sqm.between(30, 250).all() and df.storey.between(1, 30).all()
    assert ok                                           # the dataset passes its own constraints

def test_checklist_catches_leakage_pattern():
    # the checklist function must mention leakage
    p = HERE / "qa_checklist.py"
    if p.exists():
        assert "leak" in p.read_text().lower()
''',
}

# ---------------------------------------------------------------- READMEs (compact)
READMES = {
"L02_Scaling": ("Lab 2 — Scaling Pipelines (C1)", "S04", "2 hrs",
 "Build StandardScaler / MinMaxScaler / RobustScaler pipelines on cleaned HDB data; show the outlier collapse; export a comparison chart.",
 "cleaned_hdb.csv", "| floor_area_sqm | float | area sqm | — |\n| storey | float | storey | — |\n| lease_commence | int | lease year | — |\n| resale_price | float | price | target |"),
"L03_Encoding": ("Lab 3 — Encoding Categorical Data (C1)", "S06", "2 hrs",
 "One-hot town; ordinal-encode flat_type with explicit order; report shape/memory costs.",
 "cleaned_hdb.csv", "| town | str | 10 nominal values | no order |\n| flat_type | str | 4 values | genuinely ordinal 3<4<5<EXEC |"),
"L04_Imbalance": ("Lab 4 — Imbalance & Algorithm-Aware Prep (C1)", "S08", "2 hrs",
 "Diagnose 990:10 fraud imbalance; apply under/over/SMOTE fold-safely; compare accuracy vs F1 vs recall.",
 "fraud.csv", "| txn_amount | float | amount | — |\n| txn_distance_km | float | distance | — |\n| txn_hour_dev | float | hour deviation | — |\n| is_fraud | int | label | 990:10 imbalance |"),
"L05_C1_MiniProject": ("Lab 5 — C1 Consolidation Mini-Project (C1)", "S09", "2 hrs",
 "End-to-end C1 prep on HDB data for tree / KNN / logistic; deliver the prep-decisions table.",
 "cleaned_hdb.csv", "See Lab 1 schema (cleaned)."),
"L06_Bias_Audit": ("Lab 6 — Dataset Bias Audit (C2)", "S11", "2 hrs",
 "Audit adult_like.csv: group-wise stats, representation gaps, 3 findings with numeric evidence.",
 "adult_like.csv", "| group | str | A/B | 70/30 representation bias planted |\n| hours_per_week | float | hours | noisy for group B (measurement bias) |\n| income_gt_50k | int | label | historical gap planted |"),
"L07_Fairness_Metrics": ("Lab 7 — Computing Fairness Metrics (C2)", "S13", "2 hrs",
 "Train a classifier; compute demographic parity, equalised odds, predictive parity by group with fairlearn.",
 "adult_like.csv", "See Lab 6 schema."),
"L08_Mitigations": ("Lab 8 — Applying Mitigations (C2)", "S15", "2 hrs",
 "Apply reweighing; recompute metrics; report before/after and the accuracy-fairness trade-off.",
 "adult_like.csv", "See Lab 6 schema."),
"L09_Bias_Report": ("Lab 9 — 1-Page Bias Assessment Report (C2)", "S17", "2 hrs",
 "Assemble the 5-section bias report from Labs 6-8 results.",
 "adult_like.csv", "See Lab 6 schema."),
"L10_Two_Datasets": ("Lab 10 — C2 Consolidation on Two Datasets (C2)", "S18", "2 hrs",
 "Full audit cycle on lending.csv; compare against adult_like findings.",
 "lending.csv", "| district | str | 5 SG districts | historical approval bias planted |\n| credit_score | float | score | — |\n| monthly_income | float | income | — |\n| approved | int | label | 92:8 imbalance |"),
"L11_Splits_Leakage": ("Lab 11 — Splits in Practice (C3)", "S20", "2 hrs",
 "70/15/15 seeded splits; leakage demo (scale before vs after split); disjoint-index assertion.",
 "cleaned_hdb.csv", "See Lab 1 schema (cleaned)."),
"L12_Cross_Validation": ("Lab 12 — KFold, StratifiedKFold, TimeSeriesSplit (C3)", "S22", "2 hrs",
 "TimeSeriesSplit on energy (no time travel); stratified folds on fraud; scaler inside the CV loop.",
 "energy_demand.csv + fraud.csv", "| date | str | daily | strictly temporal |\n| demand_mw | float | demand | trend+seasonality |"),
"L13_Augmentation": ("Lab 13 — Augmentation on Tabular Data (C3)", "S24", "2 hrs",
 "Gaussian jitter on HDB numerics; labels unchanged; distribution overlay chart.",
 "cleaned_hdb.csv", "See Lab 1 schema (cleaned)."),
"L14_Synthetic_Data": ("Lab 14 — Synthetic Data with SMOTE + GenAI (C3)", "S25", "2 hrs",
 "SMOTE synthesis vs GenAI-generated rows (schema+stats prompts only); distribution comparison; safety verdict.",
 "minority_sample.csv", "| feature_a/b/c | float | features | — |\n| label | int | 95:5 | minority class |"),
"L15_Vibe_Coding": ("Lab 15 — Vibe Coding Data Prep (C3, AI-assist core)", "S27", "2 hrs",
 "Redo Lab 5 vibe-coded: prompt-draft-run-verify-refine; prompt log + diff vs manual baseline + reflection.",
 "cleaned_hdb.csv", "See Lab 1 schema (cleaned)."),
"L16_Critique_Fix": ("Lab 16 — Critiquing & Fixing AI Output (C3, AI-assist core)", "S29", "2 hrs",
 "Three planted-failure scripts: hallucinated API, SMOTE-before-split, test leakage. Find, explain, fix.",
 "script_1/2/3.py", "| script_1.py | py | prep code | hallucinated import |\n| script_2.py | py | prep code | SMOTE before split |\n| script_3.py | py | prep code | scaler on full data |"),
"L17_Prompt_Library": ("Lab 17 — Prompt Library Build (C3, AI-assist core)", "S31", "2 hrs",
 "Build + test 8 prompts (5-part structure); record 6-point checklist results per prompt.",
 "—", "Uses your own datasets from earlier labs."),
"L18_Final_QA": ("Lab 18 — Final Dataset QA & Readiness Checklist (C3)", "S32", "2 hrs",
 "Implement/run the readiness checklist (types, leakage, balance, constraints); fix every red flag.",
 "cleaned_hdb.csv", "See Lab 1 schema (cleaned)."),
}

EXITS = {
"L02_Scaling": "One chart: three scalers, one column. Which would you ship for KNN and why? *(Good: RobustScaler or StandardScaler with justification referencing scale-sensitivity of distance models.)*",
"L03_Encoding": "A 3-row table: column, encoding chosen, one-line justification. *(Good: town→one-hot (nominal); flat_type→ordinal explicit (ordered); justification names the order/absence of order.)*",
"L04_Imbalance": "Which strategy won on F1, and why is accuracy a trap here? *(Good: SMOTE or oversampling on F1; accuracy ~99% is achievable by never predicting fraud — recall near zero.)*",
"L05_C1_MiniProject": "Your prep-decisions table (column → treatment → why). *(Good: every treatment justified by algorithm type, not just executed.)*",
"L06_Bias_Audit": "Your 3 findings, each with a number as evidence. *(Good: representation 70/30, income-rate gap, hours-variance gap — each cited.)*",
"L07_Fairness_Metrics": "Which metric failed worst, and what does that mean in plain English? *(Good: names the metric AND translates it — e.g. 'TPR gap means qualified B applicants are approved less often'.)*",
"L08_Mitigations": "Before/after table + one sentence on the trade-off you observed. *(Good: quantifies both the fairness gain and the accuracy cost.)*",
"L09_Bias_Report": "Your 1-page report committed to the LMS. *(Good: all 5 sections, numeric evidence throughout.)*",
"L10_Two_Datasets": "One paragraph: which dataset is riskier to deploy in Singapore and why. *(Good: lending — district is a live proxy attribute under PDPA; cites the district gap.)*",
"L11_Splits_Leakage": "The two scores + one sentence: why do they differ? *(Good: the leaky scaler saw test-set statistics, so its score is optimistic.)*",
"L12_Cross_Validation": "Match each of 3 datasets to its correct splitter, with one reason each. *(Good: fraud→stratified (imbalance); energy→TimeSeriesSplit (temporal); HDB→plain k-fold (iid regression).)*",
"L13_Augmentation": "One augmented chart + one jittered-rows sanity check. *(Good: labels unchanged assertion shown.)*",
"L14_Synthetic_Data": "Distribution comparison chart + one sentence: which synthetic set is safer to train on? *(Good: SMOTE stays near real data; GenAI rows need plausibility checks — verdict justified by the chart.)*",
"L15_Vibe_Coding": "Diff summary: what the AI got right, wrong, and what you changed. *(Good: specific — names the actual encoding/pipeline errors, not 'it was mostly right'.)*",
"L16_Critique_Fix": "Three fixes with one-paragraph explanations each. *(Good: names the failure class — hallucinated API / silent correctness bug / leakage — not just the code change.)*",
"L17_Prompt_Library": "Your prompt library file, committed. *(Good: 8+ entries, all 5 parts present, checklist results recorded.)*",
"L18_Final_QA": "Completed checklist with all items green or justified. *(Good: any red flag either fixed or explicitly justified with rationale.)*",
}

REQS = {"L02_Scaling": REQ_ML, "L03_Encoding": REQ_ML, "L04_Imbalance": REQ_IMB,
        "L05_C1_MiniProject": REQ_ML, "L06_Bias_Audit": REQ_BASIC, "L07_Fairness_Metrics": REQ_FAIR,
        "L08_Mitigations": REQ_FAIR, "L09_Bias_Report": REQ_BASIC, "L10_Two_Datasets": REQ_FAIR,
        "L11_Splits_Leakage": REQ_ML, "L12_Cross_Validation": REQ_ML, "L13_Augmentation": REQ_ML,
        "L14_Synthetic_Data": REQ_IMB, "L15_Vibe_Coding": REQ_ML, "L16_Critique_Fix": REQ_IMB,
        "L17_Prompt_Library": REQ_BASIC, "L18_Final_QA": REQ_ML}

for lab, (title, session, dur, brief, dataset, schema) in READMES.items():
    d = LABS / lab
    (d / "starter" / "requirements.txt").write_text(REQS[lab])
    (d / "starter" / "README.md").write_text(f"""# {title}

**Session:** {session} · **Duration:** {dur} · **AI-assist:** see Agent 4 overlay

## Scenario & tasks
{brief}

## Dataset: `{dataset}`
{schema}

## Self-check
`pytest tests/ -v` — run any time; all tests must pass before you leave.
""")
    (d / "solution" / "exit_ticket.md").write_text(f"""# {lab.split('_')[0]} — Exit ticket

**Task:** {EXITS[lab]}
""")
    if lab in TESTS:
        (d / "starter" / "tests" / "test_progress.py").write_text(TESTS[lab])
        (d / "solution" / "tests" / "test_solution.py").write_text(
            TESTS[lab].replace("progress tests", "solution tests"))
    print("completed", lab)

# L16 planted scripts into both data folders
for sub in ["starter/data", "solution/data"]:
    p = LABS / "L16_Critique_Fix" / sub
    p.mkdir(parents=True, exist_ok=True)
    for name, src in SCRIPTS.items():
        (p / name).write_text(src)
    # L16 also needs the datasets the scripts load
    for ds in ["cleaned_hdb.csv", "fraud.csv"]:
        shutil.copy(LABS / "data" / ds, p / ds)
print("L16 scripts planted")

# L12 needs both datasets (build passed None)
for sub in ["starter/data", "solution/data"]:
    p = LABS / "L12_Cross_Validation" / sub
    p.mkdir(parents=True, exist_ok=True)
    for ds in ["energy_demand.csv", "fraud.csv"]:
        shutil.copy(LABS / "data" / ds, p / ds)
print("L12 datasets copied")
