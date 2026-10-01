"""Agent 2 pass: inject 'Python you need this week' primer + prerequisites box
into every theory concept note, per the updated Theory prompt.
Run from course/: python _agent2_primers.py"""
import re
from pathlib import Path

WEEKS = Path(__file__).resolve().parent / "weeks"

# per-session: (week, prereq lines, primer commands [(code, plain-english explanation)])
PRIMERS = {
"S01": ("W01",
 ["Complete the pre-course environment check (Python 3.11+, Jupyter installed)",
  "Open Jupyter and run a `print(\"hello\")` cell — if that works, you're ready"],
 [("df = pd.read_csv(\"file.csv\")", "load a spreadsheet-like file into a table called a DataFrame"),
  ("df.head()", "show the first 5 rows so you can see what the data looks like"),
  ("df.info()", "show every column, its type, and how many empty cells exist"),
  ("df[\"price\"].str.replace(\"$\", \"\")", "take the price column and delete every $ sign"),
  (".astype(float)", "turn text into decimal numbers"),
  ("df[\"col\"].isna().sum()", "count how many empty cells are in a column")]),
"S03": ("W01",
 ["Attend S01 (data types) — this session builds directly on it",
  "Have your Lab 1 notebook open: we will scale the data you cleaned"],
 [("from sklearn.preprocessing import StandardScaler", "borrow the standardisation tool from scikit-learn"),
  ("scaler.fit(X_train)", "learn the mean and spread from the TRAINING data only"),
  ("scaler.transform(X_test)", "apply that learned mean/spread to other data"),
  ("df[\"col\"].mean(), df[\"col\"].std()", "the average and the typical distance from the average"),
  ("df.describe()", "summary stats for every numeric column at once")]),
"S05": ("W02",
 ["Week 1 complete: Lab 1's cleaned_hdb.csv and Lab 2's scaling pipelines done",
  "You can already load a CSV and check dtypes with df.info()"],
 [("df[\"town\"].unique()", "list every different value in a column (no repeats)"),
  ("df[\"town\"].nunique()", "count how many different values exist"),
  ("pd.get_dummies(df, columns=[\"town\"])", "one-hot encode: one new 0/1 column per town"),
  ("df[\"col\"].map({\"LOW\": 0, \"HIGH\": 1})", "replace each value with the number you choose")]),
"S07": ("W02",
 ["S05 (encoding) complete — you know one-hot vs ordinal",
  "Lab 3's encoded dataset is your starting point"],
 [("df[\"label\"].value_counts()", "count how many rows of each class (e.g. fraud vs not)"),
  ("from imblearn.over_sampling import SMOTE", "borrow the SMOTE tool from imbalanced-learn"),
  ("X_train, X_test, y_train, y_test = train_test_split(...)", "split data into a learning part and a testing part"),
  ("from sklearn.neighbors import KNeighborsClassifier", "the KNN model — classifies by nearest neighbours")]),
"S10": ("W03",
 ["Weeks 1–2 complete: you can clean, scale, and encode a dataset",
  "Bring your Lab 5 prep-decisions table — the clinic reviews it"],
 [("df.groupby(\"group\")[\"income\"].mean()", "the average income separately for each group"),
  ("df[\"group\"].value_counts(normalize=True)", "each group's share of the rows, as percentages"),
  ("df.isna().sum()", "count empty cells per column — missingness patterns matter for bias")]),
"S12": ("W03",
 ["S10 (bias sources) complete — you know what to look for",
  "Lab 6's audit findings will be quantified in this session's lab"],
 [("from sklearn.metrics import confusion_matrix", "the table of correct/incorrect predictions"),
  ("(pred == 1).mean()", "the approval rate: the fraction predicted as 1"),
  ("from fairlearn.metrics import MetricFrame", "fairlearn's tool: computes any metric separately per group"),
  ("mf.by_group", "the metric broken down for each group side by side")]),
"S14": ("W04",
 ["S12 (fairness metrics) complete — you can compute a parity gap",
  "Lab 7's gap table is what we will now try to close"],
 [("sample_weight = ...", "tell the model 'count these rows more' during training"),
  ("model.fit(X, y, sample_weight=w)", "train with those importance weights (reweighing)"),
  ("df.groupby([\"group\", \"label\"]).size()", "count rows in each group-outcome combination")]),
"S16": ("W04",
 ["Labs 6–8 complete: you have findings and mitigations to document",
  "Keep your Lab 7 gap table and Lab 8 before/after numbers open"],
 [("df.to_markdown()", "turn a results table into Markdown you can paste into a report"),
  ("open(\"report.md\", \"w\").write(...)", "save your report as a file"),
  ("df.describe().round(2)", "rounded summary stats — evidence for your datasheet")]),
"S19": ("W05",
 ["Weeks 1–4 complete: you have a fully prepped, bias-audited dataset",
  "Bring your Lab 10 comparison paragraph — we now split the data properly"],
 [("from sklearn.model_selection import train_test_split", "the splitting tool"),
  ("train_test_split(X, y, test_size=0.2, random_state=42)", "80/20 split; random_state makes it repeatable"),
  ("set(df.index) & set(test.index)", "check for overlapping rows between two sets")]),
"S21": ("W05",
 ["S19 (splits) complete — leakage is the enemy this session refines",
  "Lab 11's leakage demo showed the problem; today we fix it properly"],
 [("from sklearn.model_selection import StratifiedKFold", "k-fold that keeps class ratios in every fold"),
  ("from sklearn.model_selection import TimeSeriesSplit", "k-fold for time data: only train on the past"),
  ("cross_val_score(model, X, y, cv=5)", "run 5-fold cross-validation and get 5 scores"),
  ("make_pipeline(scaler, model)", "bundle scaling + model so the scaler refits per fold")]),
"S23": ("W06",
 ["Week 5 complete: your data is split and cross-validated",
  "Lab 12's CV scores are your baseline for today's augmentation"],
 [("df[\"col\"] + np.random.normal(0, 1, len(df))", "add random noise to a column (Gaussian jitter)"),
  ("np.random.default_rng(42)", "a random-number generator that always gives the same numbers (seeded)"),
  ("pd.concat([df, df2])", "stack two tables on top of each other")]),
"S26": ("W07",
 ["Weeks 1–6 complete: you can prep, audit, split, and augment data",
  "Have your Lab 5 manual solution open — it is today's baseline for diffing"],
 [("\"\"\"prompt text\"\"\"", "a multi-line string — how you store a prompt in your notebook"),
  ("diff = my_code != ai_code", "comparing your attempt with the AI's, line by line"),
  ("pytest tests/ -v", "run the lab's checks to verify the AI's code actually works")]),
"S28": ("W07",
 ["S26 (vibe coding) complete — you have prompted and diffed once",
  "Bring your Lab 15 prompt log — we dissect what went wrong"],
 [("import sklearn.preprocessing", "check what a module really contains before trusting AI's import"),
  ("hasattr(module, \"ClassName\")", "test whether a class the AI mentioned actually exists"),
  ("try: ... except ImportError: ...", "catch a failed import instead of crashing")]),
"S30": ("W08",
 ["S26 + S28 complete — you know the loop and the risks",
  "Lab 16's three fixed failures are your case studies"],
 [("prompt = f\"Role: ... Schema: {df.columns.tolist()}\"", "build a prompt string that includes your real column names"),
  ("df.describe().to_dict()", "your data's summary stats — safe to paste into a prompt (no raw rows)")]),
"S33": ("W09",
 ["Weeks 1–8 complete — this session consolidates everything",
  "Bring ALL your lab notebooks; the review maps them to the exam"],
 [("(review session — no new commands; revisit the primers from Weeks 1–8)", "")]),
"S35": ("W09",
 ["S33 consolidation complete",
  "Bring your Lab 5 prep-decisions table and Lab 9 bias report — the mock uses both"],
 [("(mock walkthrough — practise under the 15/90/15 time budget)", "")]),
}

for sid, (week, prereqs, cmds) in PRIMERS.items():
    f = WEEKS / week / "theory" / f"{sid}_concept.md"
    if not f.exists():
        print("MISSING", f); continue
    text = f.read_text()
    if "Python you need this week" in text:
        print("skip (already has primer)", sid); continue
    prereq_block = "## Prerequisites — do these BEFORE this session\n\n" + \
        "\n".join(f"- [ ] {p}" for p in prereqs) + "\n\n"
    primer = "## Python you need this week\n\n" + \
        "\n".join(f"- `{c}` — {e}" for c, e in cmds if e) + "\n\n"
    # insert both right after the title line
    lines = text.split("\n")
    title_end = 0
    for i, l in enumerate(lines):
        if l.startswith("# "):
            title_end = i + 1
            break
    lines.insert(title_end, "\n" + prereq_block + primer)
    f.write_text("\n".join(lines))
    print("primed", sid, "->", week)
