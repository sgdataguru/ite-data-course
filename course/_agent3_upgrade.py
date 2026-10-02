"""Agent 3 pass: rewrite lab READMEs with the 8 required sections (incl. 2-hour
plan with AI-assist block + Python survival kit + stuck hints), and inject an
AI-assist scaffold cell into every starter notebook.
Run from course/: python _agent3_upgrade.py"""
import nbformat as nbf
from pathlib import Path

WEEKS = Path(__file__).resolve().parent / "weeks"

def ranges(tasks):
    t = 0
    out = []
    for name, mins, mode in tasks:
        start = t; t += mins
        out.append((f"{start//60}:{start%60:02d}-{t//60}:{t%60:02d}", name, mode))
    return out

AI_CELL = """# AI-ASSIST BLOCK - prompt log (fill this in during the AI part of the lab)
#
# Rules: attempt the task yourself FIRST. Then prompt the AI. Then DIFF the two
# solutions and verify with the lab's tests (pytest tests/ -v).
#
# | # | Intent (what I wanted) | Prompt (summary) | What the AI returned | What I verified | What I changed |
# |---|---|---|---|---|---|
# | 1 |  |  |  |  |  |
# | 2 |  |  |  |  |  |
#
# 6-point verification checklist:
#   [ ] runs without error   [ ] deterministic (seeded)   [ ] no train-test leakage
#   [ ] spot-checked by hand [ ] APIs exist in installed versions
#   [ ] constraints respected (libraries, pipeline structure)
#
# REFLECTION (required, 3-5 lines): what the AI got right, what it got wrong, what I changed.
"""

LABS = {
"L01_Messy_Data": dict(week="W01", session="S02", title="Load & Fix a Messy Dataset",
  outcomes=["Turn a messy price column like \"$530,000\" into numbers a model can use",
            "Parse dates that come in two different formats",
            "Decide what to do with missing values - and justify your choice",
            "Spot impossible values (a 9,999 sqm flat?) before they ruin your analysis"],
  tasks=[("Setup + run the first cells together", 15, "Instructor-led"),
         ("Task 1: fix the price column", 30, "Solo"),
         ("Checkpoint: run pytest tests/ -v", 10, "Self-check"),
         ("Task 2: parse the mixed dates", 20, "Pairs"),
         ("AI-assist block: ask the AI to explain your hardest error", 20, "With AI assistant"),
         ("Task 3: missing values + outliers, then export", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Week 1 theory S01 read (data types & conversion)",
           "Environment checked: pip install -r requirements.txt",
           "Jupyter opens and runs a print() cell"],
  kit=[("pd.read_csv(\"data/hdb_messy.csv\")", "load the messy file into a table"),
       ("df.head()", "peek at the first 5 rows"),
       ("df.info()", "every column, its type, and empty-cell counts"),
       ("df[\"col\"].str.replace(\"$\", \"\", regex=False)", "delete every $ in a text column"),
       (".astype(float)", "turn text into decimal numbers"),
       ("pd.to_datetime(col, format=\"mixed\", dayfirst=True)", "parse dates, day-first for dd/mm/yyyy rows"),
       ("df[\"col\"].fillna(df[\"col\"].median())", "replace empty cells with the middle value"),
       ("df.drop(columns=[\"name\"])", "remove a column")],
  hints=["Hint 1: the $ and comma are characters - remove them first, then cast.",
         "Hint 2: pd.to_datetime with format=\"mixed\" handles both date styles.",
         "Hint 3: fix the 9999/-50 outliers BEFORE imputing, or your median becomes garbage."]),
"L02_Scaling": dict(week="W01", session="S04", title="Scaling Pipelines",
  outcomes=["Build StandardScaler, MinMaxScaler, and RobustScaler pipelines",
            "Show why one outlier can collapse a min-max scale",
            "Fit a scaler on training data only - and explain why"],
  tasks=[("Setup + load your Lab 1 cleaned CSV", 15, "Instructor-led"),
         ("Task 1: fit 3 scalers on TRAIN only", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: inject the 400 sqm outlier, watch min-max collapse", 20, "Pairs"),
         ("AI-assist block: ask the AI to justify or challenge your scaler choice", 20, "With AI assistant"),
         ("Task 3: plot before/after + export chart", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Lab 1 complete - you need cleaned_hdb.csv from your solution folder",
           "Week 1 theory S03 read (scaling vs normalisation vs standardisation)"],
  kit=[("train_test_split(X, test_size=0.2, random_state=42)", "split into train (80%) and test (20%), repeatable"),
       ("StandardScaler().fit(X_train)", "learn mean & spread from training data only"),
       ("scaler.transform(X_test)", "apply the learned stats to the test data"),
       ("plt.hist(col, bins=40)", "draw a histogram"),
       ("plt.savefig(\"chart.png\")", "save your chart as a file")],
  hints=["Hint 1: fit() learns, transform() applies - never fit on the test set.",
         "Hint 2: for the outlier demo, change one value to 400 and re-fit min-max.",
         "Hint 3: the chart needs 4 panels: raw + three scalers."]),
"L03_Encoding": dict(week="W02", session="S06", title="Encoding Categorical Data",
  outcomes=["One-hot encode a nominal column without inventing fake order",
            "Ordinal-encode with an explicit order you control",
            "Explain the memory cost of one-hot on high-cardinality columns"],
  tasks=[("Setup + load cleaned data", 10, "Instructor-led"),
         ("Task 1: one-hot encode town", 25, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: ordinal-encode flat_type with explicit order", 25, "Pairs"),
         ("AI-assist block: ask the AI to critique your encoding choices", 20, "With AI assistant"),
         ("Task 3: report shapes/memory before & after", 20, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Week 1 complete (Lab 1's cleaned_hdb.csv)",
           "Week 2 theory S05 read (one-hot vs label vs target encoding)"],
  kit=[("OneHotEncoder(sparse_output=False, handle_unknown=\"ignore\")", "one 0/1 column per category; unseen values won't crash"),
       ("OrdinalEncoder(categories=[[\"3-ROOM\",\"4-ROOM\",\"5-ROOM\",\"EXECUTIVE\"]])", "encode with YOUR order, not alphabetical"),
       ("df.memory_usage()", "how much memory each column uses"),
       ("ohe.fit_transform(df[[\"town\"]])", "learn the categories and encode in one step")],
  hints=["Hint 1: town has no natural order - one-hot it.",
         "Hint 2: flat_type IS ordered, but only if you pass the categories explicitly.",
         "Hint 3: compare df.shape[1] before and after to see the column explosion."]),
"L04_Imbalance": dict(week="W02", session="S08", title="Imbalance & Algorithm-Aware Prep",
  outcomes=["Diagnose a 990:10 imbalanced fraud dataset",
            "Apply under/over/SMOTE so only training folds are resampled",
            "Explain why 99% accuracy can mean a useless model"],
  tasks=[("Setup + see the lying metric demo", 15, "Instructor-led"),
         ("Task 1: baseline KNN - accuracy vs recall", 25, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: three resampling strategies via imblearn Pipeline", 30, "Pairs"),
         ("AI-assist block: ask the AI to argue under vs over vs SMOTE for your data", 20, "With AI assistant"),
         ("Task 3: results table accuracy/recall/F1", 10, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Week 2 theory S07 read (SMOTE intuition, algorithm-specific prep)",
           "Labs 1-3 complete"],
  kit=[("df[\"is_fraud\"].value_counts()", "count each class - see the 990:10 imbalance"),
       ("from imblearn.pipeline import Pipeline", "a pipeline that resamples INSIDE training folds only"),
       ("SMOTE(random_state=42)", "synthesise minority points between neighbours"),
       ("recall_score(y_test, pred)", "of all real frauds, how many did we catch?"),
       ("f1_score(y_test, pred)", "the balance of precision and recall")],
  hints=["Hint 1: put SMOTE inside the imblearn Pipeline, never before the split.",
         "Hint 2: accuracy near 99% with recall near 0 = the model never predicts fraud.",
         "Hint 3: stratify=y in train_test_split keeps the ratio in both halves."]),
"L05_C1_MiniProject": dict(week="W02", session="S09", title="C1 Consolidation Mini-Project",
  outcomes=["Run a full C1 prep: clean, scale, encode, prep for 3 algorithms",
            "Justify every prep decision in a decisions table"],
  tasks=[("Setup + review the algorithm-prep matrix", 15, "Instructor-led"),
         ("Task 1: assemble prep for tree / KNN / logistic", 45, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("AI-assist block: ask the AI to review your decisions table for mismatches", 25, "With AI assistant"),
         ("Task 2: write the prep-decisions table", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Labs 1-4 complete - this lab reuses all of them",
           "Week 2 theory S05 + S07 read"],
  kit=[("ColumnTransformer([...])", "apply different prep to different columns in one object"),
       ("make_pipeline(...)", "chain steps so they run in order"),
       ("pd.DataFrame([...], columns=[...])", "build your decisions table")],
  hints=["Hint 1: trees don't need scaling; KNN and logistic do.",
         "Hint 2: the decisions table is the graded artefact - justify, don't just execute.",
         "Hint 3: reuse your Lab 3 encoders; don't rebuild from scratch."]),
"L06_Bias_Audit": dict(week="W03", session="S11", title="Dataset Bias Audit",
  outcomes=["Audit a dataset for representation bias with group-wise stats",
            "Write 3 bias findings, each backed by a number"],
  tasks=[("Setup + the five bias sources recap", 15, "Instructor-led"),
         ("Task 1: group-wise summary stats", 25, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: representation + missingness by group", 25, "Pairs"),
         ("AI-assist block: ask the AI to brainstorm bias sources, then verify with your own numbers", 20, "With AI assistant"),
         ("Task 3: write 3 findings with evidence", 35, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Week 3 theory S10 read (sources of bias)",
           "Weeks 1-2 labs complete"],
  kit=[("df.groupby(\"group\")[\"col\"].mean()", "the mean separately per group"),
       ("df[\"group\"].value_counts(normalize=True)", "each group's share of the sample"),
       ("df.groupby(\"group\").std()", "the spread per group - measurement-bias clue")],
  hints=["Hint 1: representation = value_counts(normalize=True) vs the real population.",
         "Hint 2: 'seems biased' earns nothing - every finding needs a number.",
         "Hint 3: hours_per_week has higher variance for group B - that's measurement bias."]),
"L07_Fairness_Metrics": dict(week="W04", session="S13", title="Computing Fairness Metrics",
  outcomes=["Compute demographic parity, equalised odds, and predictive parity by group",
            "Interpret each gap in plain English"],
  tasks=[("Setup + train the baseline classifier", 20, "Instructor-led"),
         ("Task 1: MetricFrame - selection rate, TPR, precision by group", 35, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("AI-assist block: ask the AI to explain your worst gap in plain English, then check it", 20, "With AI assistant"),
         ("Task 2: gap table + interpretations", 25, "Pairs"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Lab 6 complete - you know where the bias lives",
           "Week 3 theory S12 read (the three fairness metrics)"],
  kit=[("MetricFrame(metrics=..., y_true=..., y_pred=..., sensitive_features=...)", "any metric, computed separately per group"),
       ("mf.by_group", "the per-group values side by side"),
       ("mf.difference()", "the gap: largest minus smallest group value"),
       ("recall_score(y, p)", "TPR: of real positives, how many were caught")],
  hints=["Hint 1: selection rate = (pred == 1).mean() per group.",
         "Hint 2: equalised odds needs BOTH TPR and FPR compared.",
         "Hint 3: the interpretation sentence is graded as hard as the number."]),
"L08_Mitigations": dict(week="W04", session="S15", title="Applying Mitigations",
  outcomes=["Apply reweighing to close a fairness gap",
            "Report the accuracy-fairness trade-off honestly"],
  tasks=[("Setup + reweighing intuition", 15, "Instructor-led"),
         ("Task 1: compute reweighing weights", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: retrain with weights, recompute gaps", 25, "Pairs"),
         ("AI-assist block: ask the AI to draft your mitigation report section, then verify", 20, "With AI assistant"),
         ("Task 3: before/after table + trade-off sentence", 20, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Lab 7 complete - you have baseline gaps to close",
           "Week 4 theory S14 read (sensitive attributes & mitigation)"],
  kit=[("model.fit(X, y, sample_weight=w)", "train with importance weights"),
       ("w[mask] = p_g * p_o / p_go", "the reweighing formula: expected share / actual share"),
       ("mf.difference()", "re-measure the gap after mitigation")],
  hints=["Hint 1: weights sum to the original row count - check it.",
         "Hint 2: mitigation is never free - report the accuracy cost too.",
         "Hint 3: never apply mitigation to the test set."]),
"L09_Bias_Report": dict(week="W04", session="S17", title="1-Page Bias Assessment Report",
  outcomes=["Assemble the standard 5-section bias report from your Labs 6-8 results"],
  tasks=[("Setup + the 5-section structure", 15, "Instructor-led"),
         ("Task 1: draft all 5 sections from your lab results", 45, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("AI-assist block: ask the AI to review your report for missing traceability, then fix", 25, "With AI assistant"),
         ("Task 2: polish evidence - numbers not adjectives", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Labs 6-8 complete - the report is built from their results",
           "Week 4 theory S16 read (documentation for traceability)"],
  kit=[("open(\"bias_report.md\", \"w\")", "create your report file"),
       ("df.to_markdown()", "turn a results table into Markdown for the report")],
  hints=["Hint 1: the 5 sections: scope, risks, metrics, mitigations, residual risks.",
         "Hint 2: every claim needs a number from Labs 6-8.",
         "Hint 3: this exact template is reused in the project - learn it now."]),
"L10_Two_Datasets": dict(week="W04", session="S18", title="C2 Consolidation on Two Datasets",
  outcomes=["Run the full audit cycle on a lending dataset",
            "Compare bias risk across two datasets and argue which is riskier"],
  tasks=[("Setup + lending dataset intro", 15, "Instructor-led"),
         ("Task 1: full audit cycle (Labs 6-8 compressed)", 45, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("AI-assist block: ask the AI to challenge your comparison, then defend with numbers", 20, "With AI assistant"),
         ("Task 2: comparison paragraph", 20, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Labs 6-9 complete - this is the compressed full cycle",
           "Bring your Lab 9 report as the template"],
  kit=[("df.groupby(\"district\").approved.mean()", "approval rate per district - the proxy-bias view"),
       ("MetricFrame(...)", "same tool as Lab 7, new sensitive feature: district")],
  hints=["Hint 1: district is a proxy attribute - treat it as sensitive (PDPA context).",
         "Hint 2: the comparison paragraph is the exit artefact.",
         "Hint 3: cite the district gap number in your verdict."]),
"L11_Splits_Leakage": dict(week="W05", session="S20", title="Splits in Practice",
  outcomes=["Build seeded 70/15/15 splits",
            "Demonstrate leakage and measure the score difference"],
  tasks=[("Setup + the sacred test set", 15, "Instructor-led"),
         ("Task 1: 70/15/15 seeded splits + disjoint assertion", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: the leakage demo - scale before vs after split", 30, "Pairs"),
         ("AI-assist block: ask the AI to spot the leaky feature in a column list", 20, "With AI assistant"),
         ("Task 3: compare scores + explain the difference", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Weeks 1-4 complete - you have a fully prepped dataset to split",
           "Week 5 theory S19 read (splits & leakage)"],
  kit=[("train_test_split(X, y, test_size=0.30, random_state=42)", "first split: 70% train, 30% holdout"),
       ("train_test_split(Xtmp, test_size=0.33)", "second split: carve 15% val + 15% test from the holdout"),
       ("set(a.index) & set(b.index)", "the overlap between two index sets - should be empty"),
       ("r2_score(y_test, pred)", "how good a regression prediction is (1.0 = perfect)")],
  hints=["Hint 1: two train_test_split calls make 70/15/15.",
         "Hint 2: the buggy path fits the scaler on ALL rows before splitting.",
         "Hint 3: assert the index sets are disjoint - keep that check forever."]),
"L12_Cross_Validation": dict(week="W05", session="S22", title="KFold, StratifiedKFold, TimeSeriesSplit",
  outcomes=["Show why plain k-fold breaks time series",
            "Keep class ratios stable with stratified folds",
            "Put the scaler inside the CV loop"],
  tasks=[("Setup + fold mechanics on the board", 15, "Instructor-led"),
         ("Task 1: TimeSeriesSplit on energy - no time travel", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: KFold vs StratifiedKFold ratios on fraud", 30, "Pairs"),
         ("AI-assist block: ask the AI to choose a CV strategy, then verify its reasoning", 20, "With AI assistant"),
         ("Task 3: pipeline-based cross_val_score", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Lab 11 complete - splits before folds",
           "Week 5 theory S21 read (cross-validation methods)"],
  kit=[("TimeSeriesSplit(n_splits=5)", "expanding-window folds: train on the past only"),
       ("StratifiedKFold(5, shuffle=True, random_state=42)", "folds that keep the class ratio"),
       ("cross_val_score(pipe, X, y, cv=5)", "run the whole loop and collect the scores"),
       ("make_pipeline(StandardScaler(), model)", "scaler INSIDE the loop - refits per fold")],
  hints=["Hint 1: for time data, train.max() < test.min() in every fold.",
         "Hint 2: compare fold positive-ratios: KFold wobbles, Stratified doesn't.",
         "Hint 3: if the scaler is outside the CV loop, you've leaked."]),
"L13_Augmentation": dict(week="W06", session="S24", title="Augmentation on Tabular Data",
  outcomes=["Apply Gaussian jitter without touching labels",
            "Verify augmented data with distribution overlays"],
  tasks=[("Setup + augmentation vs synthesis", 15, "Instructor-led"),
         ("Task 1: jitter the numeric features (seeded)", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: labels-unchanged assertion + overlay chart", 30, "Pairs"),
         ("AI-assist block: ask the AI to write the jitter, then check it didn't touch labels", 20, "With AI assistant"),
         ("Task 3: export the sanity-check chart", 15, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Week 5 complete - augmented data needs split-awareness",
           "Week 6 theory S23 read (augmentation taxonomy)"],
  kit=[("rng = np.random.default_rng(42)", "a seeded random generator - same numbers every run"),
       ("col + rng.normal(0, 0.05*col.std(), len(col))", "add noise worth 5% of the column's spread"),
       ("pd.concat([df, aug])", "stack original + augmented rows"),
       ("plt.hist(..., alpha=0.6)", "overlapping histograms for comparison")],
  hints=["Hint 1: jitter features, NEVER the label.",
         "Hint 2: assert labels unchanged before and after.",
         "Hint 3: 5% of std is enough - more distorts the data."]),
"L14_Synthetic_Data": dict(week="W06", session="S25", title="Synthetic Data with SMOTE + GenAI",
  outcomes=["Generate synthetic minority rows with SMOTE and with a GenAI tool",
            "Judge which synthetic set is safer to train on"],
  tasks=[("Setup + SMOTE vs GANs vs LLM recap", 15, "Instructor-led"),
         ("Task 1: SMOTE synthesis + plausibility checks", 30, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: GenAI synthesis - schema + stats prompts ONLY (no raw rows)", 30, "With AI assistant"),
         ("Task 3: distribution comparison chart", 25, "Pairs"),
         ("Task 4: safety verdict + reflection", 10, "Solo")],
  prereqs=["Lab 13 complete - augmentation before synthesis",
           "Week 6 theory S23 read; Agent 4's tool policy read (never paste raw rows)"],
  kit=[("SMOTE(random_state=42, k_neighbors=3)", "interpolate new minority points between neighbours"),
       ("df.describe()", "your data's summary stats - safe to put in a prompt"),
       ("(Xs >= X.min()).all()", "plausibility check: no impossible values")],
  hints=["Hint 1: the GenAI prompt gets schema + describe() - never real rows.",
         "Hint 2: SMOTE shrinks variance (interpolation); GenAI can hallucinate values.",
         "Hint 3: the verdict must cite your comparison chart."]),
"L15_Vibe_Coding": dict(week="W07", session="S27", title="Vibe Coding Data Prep (AI-assist core)",
  outcomes=["Run the full loop: prompt, draft, run, verify, refine",
            "Diff AI output against your manual Lab 5 baseline"],
  tasks=[("Setup + the loop and the 6-point checklist", 15, "Instructor-led"),
         ("Task 1: manual baseline recap (your Lab 5)", 15, "Solo"),
         ("Task 2: full vibe-coding loop on the same task", 50, "With AI assistant"),
         ("Checkpoint: pytest tests/ -v on the AI-assisted pipeline", 10, "Self-check"),
         ("Task 3: diff + prompt log completion", 20, "Solo"),
         ("Exit ticket + reflection (required)", 10, "Solo")],
  prereqs=["Lab 5 complete - your manual solution IS the baseline",
           "Week 7 theory S26 read (vibe coding principles)"],
  kit=[("prompt = f\"Role: ... Schema: {df.columns.tolist()} ...\"", "build a 5-part prompt with your real schema"),
       ("pytest tests/ -v", "verify the AI's code against the lab's checks"),
       ("pd.testing.assert_series_equal(a, b)", "programmatically diff two columns")],
  hints=["Hint 1: attempt first - the baseline exists so the diff is meaningful.",
         "Hint 2: log every prompt: intent, prompt, outcome.",
         "Hint 3: the reflection is graded: right / wrong / what you changed."]),
"L16_Critique_Fix": dict(week="W07", session="S29", title="Critiquing & Fixing AI Output (AI-assist core)",
  outcomes=["Find and fix three planted AI failures: hallucinated API, SMOTE-before-split, leakage",
            "Name each failure class, not just the code change"],
  tasks=[("Setup + run the three scripts, watch them fail differently", 20, "Instructor-led"),
         ("Task 1: script 1 - the hallucinated API", 25, "Pairs"),
         ("Task 2: script 2 - SMOTE before split (silent lie)", 25, "Pairs"),
         ("Task 3: script 3 - scaler on full data (contamination)", 25, "Pairs"),
         ("AI-assist block: ask the AI to critique its own output - tally what it missed", 15, "With AI assistant"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Lab 15 complete - you have prompt-log experience",
           "Week 7 theory S28 read (risks & limitations of AI code)"],
  kit=[("hasattr(sklearn.preprocessing, \"SmartEncoder\")", "test whether a class really exists"),
       ("try: import ... except ImportError:", "catch a failed import gracefully"),
       ("imblearn Pipeline([('smote', ...), ('clf', ...)])", "the fold-safe fix for script 2")],
  hints=["Hint 1: script 1 crashes; scripts 2 and 3 run fine and lie - that's the point.",
         "Hint 2: the fix for 2 is structural (Pipeline), not cosmetic.",
         "Hint 3: your paragraph must name the failure CLASS."]),
"L17_Prompt_Library": dict(week="W08", session="S31", title="Prompt Library Build (AI-assist core)",
  outcomes=["Build 8 tested, five-part prompts - one per module topic",
            "Record 6-point checklist results for each"],
  tasks=[("Setup + the 5-part structure with examples", 15, "Instructor-led"),
         ("Task 1: draft 8 prompts (one per topic)", 35, "Solo"),
         ("Task 2: test each on a real task from earlier labs", 40, "With AI assistant"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 3: record checklist results + polish", 10, "Solo"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Labs 15-16 complete - you've seen good and bad prompts",
           "Week 8 theory S30 read (prompt design)"],
  kit=[("f\"Role: ... Context: ... Schema: {cols} ...\"", "the 5-part template as a format string"),
       ("df.describe().to_dict()", "stats for the Context part - safe to share")],
  hints=["Hint 1: one prompt per topic: cleaning, scaling, encoding, imbalance, metrics, mitigation, splitting, QA.",
         "Hint 2: a prompt without constraints gets generic code.",
         "Hint 3: untested prompts don't count - record the checklist result."]),
"L18_Final_QA": dict(week="W08", session="S32", title="Final Dataset QA & Readiness Checklist",
  outcomes=["Run a full readiness check: types, leakage, balance, constraints",
            "Fix or justify every red flag"],
  tasks=[("Setup + the checklist walkthrough", 15, "Instructor-led"),
         ("Task 1: implement (or vibe-code) the checklist runner", 35, "Solo"),
         ("Checkpoint: pytest tests/ -v", 10, "Self-check"),
         ("Task 2: run it on your project dataset; fix red flags", 30, "Pairs"),
         ("AI-assist block: ask the AI to review your checklist for missed leakage checks", 20, "With AI assistant"),
         ("Exit ticket + reflection", 10, "Solo")],
  prereqs=["Labs 11-17 complete - the checklist uses all of them",
           "Your project dataset chosen (Agent 5's brief)"],
  kit=[("df.notna().all()", "no empty cells anywhere"),
       ("df[\"col\"].between(lo, hi).all()", "every value inside the plausible range"),
       ("df[\"target\"].value_counts(normalize=True)", "class balance, reported not assumed")],
  hints=["Hint 1: if you vibe-code the runner, verify it covers leakage - AI checklists skip it.",
         "Hint 2: every red flag is either fixed or justified in writing.",
         "Hint 3: this checklist is your project's final gate."]),
}

for lab, spec in LABS.items():
    labdir = WEEKS / spec["week"] / "labs" / lab
    plan_rows = "\n".join(f"| {r} | {n} | {m} |" for r, n, m in ranges(spec["tasks"]))
    prereq_lines = "\n".join("- [ ] " + p for p in spec["prereqs"])
    outcome_lines = "\n".join("- " + o for o in spec["outcomes"])
    kit_lines = "\n".join(f"- `{c}` - {e}" for c, e in spec["kit"])
    hint_lines = "\n".join("- " + h for h in spec["hints"])
    readme = f"""# {lab.split('_')[0]} - {spec['title']}

**Week:** {spec['week']} | **Session:** {spec['session']} | **Duration:** 2 hrs

## Week & session map
This lab sits in **{spec['week']}** (session {spec['session']}). Pair it with the week's theory session(s) before starting - the concept note's Python primer covers the commands used here. Next week builds on this lab's artefacts.

## Prerequisites - tick before you start
{prereq_lines}

## What you'll be able to do
{outcome_lines}

## Scenario
You are a junior data analyst in Singapore working on real datasets. This week's client needs your result by the end of the session.

## Dataset schema
See `data/` - columns, types, and known issues are listed in the starter notebook's first cells.

## The 2-hour plan
| Time | Activity | Mode |
|---|---|---|
{plan_rows}

## Python survival kit
{kit_lines}

## Stuck?
{hint_lines}
Still stuck? Ask your neighbour, then the instructor. Attempting first is part of the mark.

## Self-check
`pytest tests/ -v` - run any time; all tests must pass before you leave.
"""
    (labdir / "starter" / "README.md").write_text(readme)

    nb_path = labdir / "starter" / f"{lab.split('_')[0]}_starter.ipynb"
    if nb_path.exists():
        nb = nbf.read(nb_path, as_version=4)
        if not any("AI-ASSIST BLOCK" in c.get("source", "") for c in nb.cells):
            nb.cells.append(nbf.v4.new_markdown_cell(AI_CELL))
            nbf.write(nb, nb_path)
            print("notebook + AI cell:", lab)
        else:
            print("notebook already has AI cell:", lab)
    print("README upgraded:", spec["week"], lab)
