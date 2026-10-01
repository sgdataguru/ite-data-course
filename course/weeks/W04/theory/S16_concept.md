# S16 — Bias Documentation for Traceability (C2, 1 hr)

## Prerequisites — do these BEFORE this session

- [ ] Labs 6–8 complete: you have findings and mitigations to document
- [ ] Keep your Lab 7 gap table and Lab 8 before/after numbers open

## Python you need this week

- `df.to_markdown()` — turn a results table into Markdown you can paste into a report
- `open("report.md", "w").write(...)` — save your report as a file
- `df.describe().round(2)` — rounded summary stats — evidence for your datasheet



## Concept Note

**Why document.** An undocumented bias assessment cannot be audited, defended, or repeated. Traceability means: a reviewer can reconstruct what you measured, what you found, what you did about it, and why.

**Two introductory frameworks:**

1. **Datasheets for Datasets** (Gebru et al.) — a "nutrition label" for a dataset: motivation and composition; collection process; preprocessing; distribution and uses; maintenance. Key questions: Who collected this? When? What population does it represent? What was removed or transformed?
2. **Model Cards** (Mitchell et al.) — a standard record for a model: intended use, out-of-scope uses, training data summary, evaluation metrics (including per-group), ethical considerations, caveats.

At this level you need the *habit*, not the full paperwork: every dataset you prepare in this module gets a short datasheet; every bias assessment gets a mini model card.

**The 1-page bias assessment report structure** (used in Lab 9 and the project):
1. Dataset & scope (source, size, sensitive attributes)
2. Bias risks identified (which of the five sources, evidence)
3. Metrics computed (which fairness metrics, values, gaps)
4. Mitigations applied (strategy, parameters, before/after)
5. Residual risks & recommendations

**Worked example by hand.** UCI Adult income dataset: a datasheet entry would note it's 1994 US census data (so representation bias for present-day use), the target is ">50K income" (so historical pay inequity is baked in), and `sex` and `race` columns are present (so fairness analysis is possible but sensitive handling is required). Three sentences, three traceable facts.

**What you will later ask an AI to do:** draft a datasheet from a dataset description; turn your metric table into report prose; review your report for missing traceability elements.

## Slide Outline

1. **Title** — If it isn't documented, it didn't happen.
2. **Traceability** — reconstructable decisions.
3. **Datasheets for Datasets** — the nutrition label; the key questions.
4. **Model Cards** — intended use, per-group metrics, caveats.
5. **The habit, not the paperwork** — short datasheet per dataset, mini card per model.
6. **The 1-page bias report** — the five-section structure.
7. **Worked example** — three traceable facts about UCI Adult.
8. **Evidence over adjectives** — "seems biased" vs "TPR gap of 17 points".
9. **Documentation is a C2 performance criterion** — it's assessed.
10. **Recap + lab preview** — Lab 9 produces your first 1-page report.

## Mini-Quiz

1. **MCQ:** A datasheet primarily documents: (a) model hyperparameters (b) dataset provenance, composition, and preprocessing ✅ (c) server costs (d) team members.
2. **MCQ:** A Model Card's "out-of-scope uses" section exists to: (a) limit liability (b) prevent deployment bias ✅ (c) satisfy PDPA (d) speed up training.
3. **MCQ:** The strongest bias-report sentence is: (a) "the model seems unfair" (b) "TPR is 87.5% for Group A vs 70% for Group B" ✅ (c) "bias was found" (d) "we fixed the bias".
4. **Short answer:** Name two facts a datasheet for the HDB resale dataset should record. *(Answer: e.g., source = data.gov.sg, collection period, that prices are transaction-declared and may under-represent cash components, and any filtering applied such as town or flat-type exclusions.)*
