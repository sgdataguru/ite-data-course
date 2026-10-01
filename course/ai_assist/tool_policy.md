# DE5002FP — Tool Policy & Prompt Library (Agent 4)

## Approved AI tools

| Tool | Status | Notes |
|---|---|---|
| Claude (claude.ai / API) | Approved (default) | Use Projects for context; never paste raw personal data |
| ChatGPT (GPT-4 class) | Approved (fall-back) | Same data rules |
| GitHub Copilot | Approved (fall-back) | In-editor completion; log usage |
| Cursor | Approved (fall-back) | Same data rules |
| Any tool on a personal/unknown account with real data | **Prohibited** | PDPA risk |

## Usage rules

1. **Attempt first.** Every AI-assist exercise requires an unaided attempt or sketch before prompting.
2. **Never paste raw personal data.** Describe schemas, statistics, and example *shapes* — not real rows, NRIC numbers, or customer records.
3. **Log every substantive use.** In labs: a prompt log cell in the notebook. In the project: the AI-usage ledger (tool, task, prompt summary, verification performed).
4. **Cite AI assistance.** Deliverables include a short "AI assistance statement": what was AI-generated, what you verified, what you changed.
5. **Verify before you submit.** The 6-point checklist: runs, seeded, leakage-free, spot-checked, APIs real, constraints respected.
6. **Assessments:** Practical test and mock test are **AI-free** (invigilated). The project **requires** documented GenAI use.

## Prompt library (consolidated starters — placeholders in [brackets])

**Cleaning**
1. "You are preparing [dataset description] for [model]. Convert column [X] from [format] to [target type], handling [edge cases]. Show a validation check for plausibility."
2. "This cast failed with [error]. Explain the cause and give a robust fix that doesn't silently drop values."

**Scaling**
3. "Given this distribution summary [stats], recommend a scaler for [algorithm] and justify in 3 sentences."
4. "Write a leakage-free sklearn Pipeline that standardises [columns], fitted only on training folds."

**Encoding**
5. "Column [X] is [nominal/ordinal] with [N] values, feeding a [model]. Recommend an encoding and implement it with [library]."
6. "Write fold-safe target encoding for [column] within a cross-validation loop."

**Imbalance**
7. "Write an imbalanced-learn Pipeline so SMOTE applies only to training folds. Evaluate with recall and F1, not accuracy."
8. "My dataset is [ratio] imbalanced with [N] rows. Argue for undersampling vs SMOTE in 5 sentences."

**Bias & fairness**
9. "List the plausible bias sources (historical, representation, measurement, aggregation, deployment) for this dataset description: [...]. For each, state the evidence you would look for."
10. "Compute demographic parity, equalised odds, and predictive parity from this table: [confusion matrices]. Interpret each gap in plain English."
11. "Explain reweighing for this group-outcome table [table], and compute the weights."

**Splitting & CV**
12. "Write seeded 70/15/15 splitting code, then a leakage-free preprocessing pipeline. Include an assertion that no test rows appear in training."
13. "Choose a cross-validation strategy for [data description] and implement it with the scaler inside the loop."

**Synthetic data**
14. "Generate [N] synthetic rows matching this schema [schema] and these summary statistics [stats]. Do not reproduce real records. Then critique your own output for plausibility."

**QA & verification**
15. "Write a data-readiness checklist runner: types, leakage, class balance, distribution drift, domain constraints [list]."
16. "Review this AI-generated prep script for: hallucinated APIs, train-test leakage, silent correctness bugs. [code]"
