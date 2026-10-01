"""Agent 4 pass: generate per-week, per-lab AI-assist overlays into weeks/W##_ai_assist/.
Each overlay fills the exact AI-assist block reserved in Agent 3's 2-hour plan.
Run from course/: python _agent4_overlays.py"""
from pathlib import Path

WEEKS = Path(__file__).resolve().parent / "weeks"

# lab -> (week, block_minutes, block_description, prompts, failures, reflection_example)
OVERLAYS = {
"L01": ("W01", 20, "Explain-my-error block (Week 1-2 maturity level)",
  ["My code `df['resale_price'].astype(float)` failed with this error: [paste error]. Explain in simple English what is wrong and how to fix it.",
   "I have a column with values like \"$530,000\". Write one line of pandas code to turn it into numbers, and explain each part.",
   "After converting my price column, what two sanity checks should I run to catch conversion bugs?"],
  [("Silent coercion", "The AI suggests errors='ignore' on the cast - bad values survive as strings with no warning. Fix: coerce, then assert the dtype and check the range."),
   ("Zero-fill trap", "The AI fills missing prices with 0 - a missing price is not a free flat. Fix: NaN and decide (drop/impute) explicitly.")],
  "The AI explained my comma error clearly and its fix worked. It wanted to fill missing prices with 0, which would corrupt the data. I used median imputation instead and added a range check."),
"L02": ("W01", 20, "Justify-or-challenge block",
  ["My floor_area_sqm column has this distribution: [paste describe() output]. I am using KNN. Which scaler should I use and why, in 3 sentences?",
   "Here is my scaling code: [paste code]. Is there any train-test leakage in it? Point to the exact line if so.",
   "I added a 400 sqm outlier and my min-max scaling collapsed. Explain what happened and which scaler resists this."],
  [("Fit-on-everything", "The AI fits the scaler on the full dataset before splitting - contamination. Fix: fit on train, transform test with the same scaler."),
   ("Wrong ranges reported", "The AI applies RobustScaler but reports min-max ranges as if they were [0,1]. Fix: verify by computing the transformed ranges yourself.")],
  "The AI correctly picked RobustScaler for my outlier-heavy data and caught that I'd forgotten random_state. It initially fit the scaler on all rows - I moved the fit after the split and re-ran."),
"L03": ("W02", 20, "Critique-my-choices block",
  ["I one-hot encoded town (10 values) and ordinal-encoded flat_type with the order 3-ROOM<4-ROOM<5-ROOM<EXECUTIVE. Critique these two choices in 3 sentences.",
   "My dataset has a street_name column with 8,000 different values. Why is one-hot a bad idea here, and what should I do instead?",
   "Write fold-safe target encoding for my high-cardinality column inside a cross-validation loop."],
  [("Label-encodes nominal", "The AI label-encodes town, inventing an order the model will use. Fix: one-hot with handle_unknown='ignore'."),
   ("Alphabetical ordinal", "The AI ordinal-encodes flat_type alphabetically so EXECUTIVE codes below 3-ROOM. Fix: pass categories=[...] explicitly.")],
  "The AI spotted my alphabetical ordinal order immediately - good catch. It then suggested label-encoding town 'for simplicity', which would invent an order. I kept one-hot and documented why."),
"L04": ("W02", 20, "Argue-the-tradeoff block",
  ["My fraud dataset is 990:10 with 1,000 rows. Argue undersampling vs oversampling vs SMOTE in 5 sentences, then recommend one.",
   "Here is my resampling code: [paste]. Does SMOTE touch my test set anywhere? Show me the exact line if so.",
   "Why did my accuracy stay at 99% after SMOTE while recall jumped? Explain like I'm new to this."],
  [("SMOTE before split", "The AI resamples the whole dataset before splitting - the test set becomes synthetic-balanced and recall is a beautiful lie. Fix: imblearn Pipeline so resampling happens per training fold."),
   ("Accuracy-only evaluation", "The AI reports only accuracy on a 99:1 problem. Fix: recall, F1, and a confusion matrix.")],
  "The AI's SMOTE argument was solid and matched what we learned. Its first code snippet resampled before the split - exactly the bug from the failure gallery. I wrapped it in an imblearn Pipeline and the honest metrics appeared."),
"L05": ("W02", 25, "Review-my-decisions block",
  ["Here is my prep-decisions table: [paste table]. I'm feeding a random forest, KNN, and logistic regression. Flag any row where the treatment mismatches the algorithm.",
   "For a random forest, which of my prep steps are wasted effort and why? Answer in 3 sentences.",
   "Generate 5 quiz questions on choosing encodings, with answers, to test my partner."],
  [("Invented API", "The AI describes a sklearn.preprocessing.TargetEncoder signature that doesn't match the installed version. Fix: check the docs, pin the version."),
   ("Generic advice", "The AI says 'scale everything' without distinguishing trees from KNN. Fix: ask it to justify per algorithm, then verify against the matrix.")],
  "The AI found my real mistake - I was scaling features for the tree model unnecessarily. It couldn't explain WHY trees are scale-invariant, so I wrote that justification myself from the theory note."),
"L06": ("W03", 20, "Brainstorm-then-verify block",
  ["Here is my dataset description: [paste schema + describe()]. List the plausible bias sources (historical, representation, measurement, aggregation, deployment) and what evidence I'd look for in the data.",
   "Write pandas code for group-wise summary statistics of income_gt_50k by group, and missingness counts by group.",
   "Draft one bias-risk paragraph from these numbers: [paste your group stats]. Use numbers, not adjectives."],
  [("Adjective findings", "The AI writes 'the model seems biased' with no numbers. Fix: demand evidence - every finding cites a computed value."),
   ("Drop-the-column", "The AI suggests removing the sensitive attribute entirely to 'avoid bias'. Fix: you need it to measure; proxies survive deletion anyway.")],
  "The AI's brainstorm matched two of my three findings and suggested one I'd missed (aggregation). But its findings had zero numbers. I made it rewrite with evidence, then verified each number myself."),
"L07": ("W04", 20, "Explain-the-gap block",
  ["Here is my confusion-matrix table by group: [paste]. Compute demographic parity, equalised odds (TPR and FPR), and predictive parity (precision) for each group.",
   "My TPR gap is 17 points between groups A and B. Explain what that means in plain English for a non-technical report, in 3 sentences.",
   "Which of my three metrics failed worst, and what does that specific failure mean for a loan applicant from group B?"],
  [("Metric confusion", "The AI calls an approval-rate gap 'equalised odds'. Fix: equalised odds is TPR+FPR equality - make it recompute from the confusion matrix."),
   ("Wrong split", "The AI computes fairness metrics on the training set. Fix: metrics belong on held-out predictions.")],
  "The AI computed all three metric tables correctly once I pasted the confusion matrices. It kept conflating parity with equalised odds in its explanation, so I rewrote the plain-English sentence myself using the theory note's definitions."),
"L08": ("W04", 20, "Draft-then-verify block",
  ["Explain reweighing for this group-outcome table: [paste]. Compute the weight for each cell and show your working.",
   "Here are my before/after metrics: [paste]. Draft the mitigation section of my bias report - what was applied, what changed, at what cost.",
   "My mitigation closed the TPR gap but cost 4 points of accuracy. Is that a good trade? Argue both sides in 4 sentences."],
  [("Mitigates the test set", "The AI applies reweighing weights to test data. Fix: weights are a training-time concept only."),
   ("Declares victory", "The AI claims bias was 'removed' without re-measuring. Fix: recompute all three metrics and report the residual gap.")],
  "The AI's reweighing arithmetic was correct and its draft report section was usable. It declared the bias 'resolved' after one metric improved - I re-measured all three and reported the honest residual gap."),
"L09": ("W04", 25, "Traceability-review block",
  ["Here is my bias report: [paste]. Review it against the 5-section structure (scope, risks, metrics, mitigations, residual risks) and list every missing traceability element.",
   "Rewrite this finding so the evidence is numeric: 'the dataset seems to under-represent group B'.",
   "What three facts must a datasheet entry record about this dataset's provenance? Answer for my adult_like.csv."],
  [("Fabricated provenance", "The AI invents collection dates and sources for the datasheet. Fix: only document what you can verify from the data itself."),
   ("Structure over substance", "The AI confirms all 5 sections exist without checking each claim has a number. Fix: ask it to flag adjective-only claims.")],
  "The AI found two gaps I'd missed: my residual-risks section was empty and one finding had no number. It then invented a collection date for the datasheet - I deleted that and wrote only what I could verify."),
"L10": ("W04", 20, "Defend-your-verdict block",
  ["I claim the lending dataset is riskier to deploy in Singapore than the income dataset because district is a live proxy attribute. Challenge my argument in 4 sentences.",
   "Compute the approval-rate gap by district from this table: [paste]. Which districts are systematically disadvantaged?",
   "Under PDPA, what makes district a sensitive-adjacent attribute even though it's 'just location'?"],
  [("Superficial comparison", "The AI compares dataset sizes instead of bias risk. Fix: force it to compare the specific gaps and proxy sensitivity."),
   ("Reassuring nonsense", "The AI says 'both datasets are fine for deployment'. Fix: paste the numbers and make it reconcile them with the claim.")],
  "The AI pushed back hard on my verdict and made me cite the actual district gap number instead of gesturing at 'proxy risk'. My verdict survived, but it's now defensible - and it caught that I'd compared approval rates, not TPR."),
"L11": ("W05", 20, "Spot-the-leak block",
  ["Here are my column names: [paste list]. One of them likely leaks the answer for predicting loan approval. Which one, and why?",
   "Write seeded 70/15/15 splitting code with an assertion that no test rows appear in training.",
   "My validation score is 0.99 on a messy real-world dataset. Give me three possible explanations ranked by likelihood."],
  [("Splits after fitting", "The AI splits the data after fitting the scaler - contamination by ordering. Fix: split first, always."),
   ("Double-split overlap", "The AI calls train_test_split twice on the same data, creating overlapping validation and test sets. Fix: split the holdout once, assert disjointness.")],
  "The AI spotted the leaky column instantly (days_late_on_payment) and explained the time-travel problem well. Its splitting code had a subtle overlap bug my disjoint-index assertion caught - the test I wrote in the lab saved me."),
"L12": ("W05", 20, "Verify-the-reasoning block",
  ["My data is [daily energy demand, 2 years]. Choose a cross-validation strategy, implement it, and justify the choice in 3 sentences.",
   "Here is my CV loop: [paste]. Is the scaler inside or outside the loop? What does that mean for my scores?",
   "My 5-fold scores vary from 0.61 to 0.89. Explain what that variance tells me about my data or my pipeline."],
  [("K-fold on time series", "The AI uses plain KFold on temporal data - training on the future to predict the past. Fix: TimeSeriesSplit."),
   ("Scaler outside CV", "The AI scales before cross_val_score, leaking fold statistics. Fix: make_pipeline puts the scaler inside.")],
  "The AI chose TimeSeriesSplit correctly but couldn't articulate WHY until I asked for the justification - the reasoning mattered more than the code. Its first loop had the scaler outside; the pipeline fix was the whole lesson."),
"L13": ("W06", 20, "Write-then-check block",
  ["Write Gaussian jitter augmentation for these columns: [paste]. The noise must be 5% of each column's std, seeded, and must NOT touch the label. Then explain how I verify the labels survived.",
   "Here is my augmentation code: [paste]. Did I accidentally jitter the label or the test set?",
   "My augmented distribution looks identical to the original. Is that success or failure? Explain."],
  [("Jitters the label", "The AI includes the target column in the jitter loop - the label no longer means anything. Fix: exclude it, assert equality before/after."),
   ("Augments the test set", "The AI augments all rows including test. Fix: augment training data only.")],
  "The AI's jitter code was clean and seeded, but it included resale_price in the loop - my labels-unchanged assertion caught it immediately. That assert is now permanently in my notebook."),
"L14": ("W06", 30, "Schema-stats-only synthesis block",
  ["Generate 50 synthetic rows matching this schema [paste schema] and these summary statistics [paste describe()]. Do NOT reproduce real records. Then critique your own output for plausibility.",
   "Compare my real vs synthetic distributions: [paste stats]. Which synthetic set (SMOTE or your generated rows) stays closer to the real data, and where does each drift?",
   "What plausibility constraints should I assert on synthetic rows for this schema (ranges, no negatives, valid categories)?"],
  [("Impossible rows", "The AI generates negative ages and 999-room flats - plausible-looking, impossible values. Fix: assert domain constraints on every generated row."),
   ("Ratio drift", "The AI's synthetic rows quietly change the class ratio. Fix: check value_counts before and after."),
   ("Memorisation risk", "The AI offers to 'reuse' real rows 'for realism'. Fix: schema + statistics only, never raw data in the prompt.")],
  "The AI's synthetic rows looked convincing but included two negative feature values my plausibility check caught. SMOTE stayed closer to the real distribution. My verdict: SMOTE for training, GenAI rows only with constraint checks - and never raw rows in the prompt."),
"L15": ("W07", 50, "Full vibe-coding loop (core lab)",
  ["You are preparing an HDB dataset for KNN. Standardise floor_area_sqm, storey, lease_commence; one-hot town with handle_unknown='ignore'; ordinal-encode flat_type as 3<4<5<EXEC. Output a single sklearn ColumnTransformer.",
   "Your previous output label-encoded town. town is nominal - use OneHotEncoder(handle_unknown='ignore') and re-output the full transformer.",
   "Now justify each prep choice in one sentence per column, as if for a decisions table."],
  [("First-draft encoding bug", "The AI label-encodes town despite the constraint - refined in round 2."),
   ("Alphabetical ordinal", "The AI's flat_type order is alphabetical until explicitly constrained."),
   ("No justification", "The AI cannot say WHY tree prep skips scaling - the human adds the rationale.")],
  "The AI got the pipeline structure right and fast. It label-encoded town (wrong) and could not justify treatment choices. I fixed the encoding, added handle_unknown, and wrote the rationale myself. The diff against my Lab 5 baseline showed we converged on the same pipeline - but mine, I can defend."),
"L16": ("W07", 15, "Self-critique tally block",
  ["Here is code you previously generated for a data prep task: [paste script 2]. Critique it for train-test leakage, hallucinated APIs, and silent correctness bugs.",
   "You said this script was correct. It resamples before splitting. Explain why that makes the reported recall a lie.",
   "Generate a checklist that would have caught your own mistake here."],
  [("Misses its own bug", "The AI reviews its own SMOTE-before-split code and finds nothing wrong - the tally moment."),
   ("Placating correction", "When pushed, the AI apologises and 'fixes' it by moving one line instead of restructuring into a Pipeline.")],
  "The AI reviewed its own leaking script and called it correct. When I pasted the test-set class ratio as evidence, it apologised and moved a line - but the real fix was structural. I wrote the Pipeline myself. The tally: it found 0 of 3 planted bugs unaided."),
"L17": ("W08", 40, "Library build-and-test block",
  ["Here is my prompt draft for an encoding task: [paste]. Score it against the 5-part structure (role, context, schema, constraints, examples) and rewrite the missing parts.",
   "Test this prompt yourself: [paste]. What code would you return, and does it respect my constraint of fold-safe target encoding?",
   "For each of my 8 prompts, predict the single most likely way the output would fail verification."],
  [("Constraint-free prompts", "The AI happily 'improves' a prompt by removing constraints for brevity. Fix: constraints are the point."),
   ("Untested confidence", "The AI declares all 8 prompts 'excellent' without running them. Fix: every entry needs a recorded checklist result.")],
  "The AI rewrote my vague cleaning prompt into a proper 5-part structure - big improvement. But it kept deleting my constraints to 'simplify', and declared untested prompts excellent. My library now records a test result for every entry."),
"L18": ("W08", 20, "Checklist-review block",
  ["Here is my data-readiness checklist runner: [paste]. Does it check for train-test leakage? If not, add that check.",
   "What domain constraints should my readiness check assert for an HDB dataset? Give the ranges and the reasoning.",
   "Review my checklist output: [paste]. Which red flags are fixable in 10 minutes, and which need a documented justification?"],
  [("Skips leakage", "The AI's checklist covers types, NaNs, and ranges but never leakage - the planted M3 lesson. Fix: add the fitted-on-train-only check."),
   ("Runs-is-correct fallacy", "The AI's tests only assert the code runs, not that outputs are right. Fix: assert actual values.")],
  "The AI's checklist was professional-looking and missed leakage entirely - exactly what the theory note predicted. I added the leakage check and it immediately flagged my own scaler bug from an earlier lab. Every red flag is now fixed or justified in writing."),
}

TEMPLATE = """# {week} AI-Assist Overlay — Lab {lab}

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** {mins} minutes inside Lab {lab}'s 2-hour plan — "{desc}".
**Maturity level:** {maturity}

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
{prompts}

## Failure gallery — how AI goes wrong on THIS task
{failures}

## Reflection scaffold (worked example)
> {reflection}
"""

MATURITY = {"W01": "Week 1-2: explain-my-error (small blocks, heavy scaffolding)",
            "W02": "Week 1-2: explain-my-error (small blocks, heavy scaffolding)",
            "W03": "Week 3-6: draft-then-diff (medium blocks)",
            "W04": "Week 3-6: draft-then-diff (medium blocks)",
            "W05": "Week 3-6: draft-then-diff (medium blocks)",
            "W06": "Week 3-6: draft-then-diff (medium blocks)",
            "W07": "Week 7-8: full vibe-coding loops (40+ min core blocks)",
            "W08": "Week 7-8: full vibe-coding loops (40+ min core blocks)"}

for lab, (week, mins, desc, prompts, failures, reflection) in OVERLAYS.items():
    p_lines = "\n".join(f"{i+1}. {p}" for i, p in enumerate(prompts))
    f_lines = "\n".join(f"### {name}\n{fix}\n" for name, fix in failures)
    out = TEMPLATE.format(week=week, lab=lab, mins=mins, desc=desc,
                          maturity=MATURITY[week], prompts=p_lines,
                          failures=f_lines, reflection=reflection)
    (WEEKS / week / "ai_assist" / f"{lab}_overlay.md").write_text(out)
    print("overlay:", week, lab, f"({mins} min)")
