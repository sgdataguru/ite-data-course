# S30 — Prompt Design for Data Work (C3, 1 hr)

## Concept Note

**The five-part prompt.** Professional prompts for data work follow a structure:

1. **Role** — "You are a data engineer preparing data for a random forest model."
2. **Context** — "I have an HDB resale dataset, ~90k rows, 2017–2024 transactions."
3. **Data schema** — column names, types, example values (descriptive, not raw sensitive rows).
4. **Constraints** — "Use pandas + scikit-learn only; must run in a scikit-learn Pipeline; no fitting on test data."
5. **Examples** — one worked input/output pair of what you want.

**Worked example by hand.** Weak: "clean my data". Strong:

> Role: You are preparing an HDB resale dataset for a gradient-boosting regressor.
> Context: 90,000 rows, 2017–2024, data.gov.sg resale transactions.
> Schema: town (str, 26 values), flat_type (str, ordinal), floor_area_sqm (float, has 12 NaNs), resale_price (str like "$530,000", target).
> Constraints: pandas + sklearn only; output a single Pipeline; handle NaNs inside the pipeline; convert resale_price to float.
> Example: "$530,000" → 530000.0.

The strong prompt is answerable, verifiable, and safe (no raw rows).

**Prompt anti-patterns:** vague verbs ("clean", "improve"); pasting raw data; asking for five things in one prompt; no success criteria; accepting the first draft.

**Iteration is normal.** First draft → run → read the error → refine the prompt with the error message. The error message *is* context for the next prompt.

**What you will later ask an AI to do:** this session is AI-assisted — you'll build and test your own prompt library in Lab 17.

## Slide Outline

1. **Title** — The prompt is the program.
2. **The five parts** — role, context, schema, constraints, examples.
3. **Worked example** — weak vs strong prompt, side by side.
4. **Schema in, data out** — describe columns; never paste raw rows.
5. **Constraints do the heavy lifting** — libraries, pipelines, leakage rules.
6. **One prompt, one job** — split multi-part asks.
7. **Anti-patterns** — vague verbs, first-draft acceptance.
8. **The iteration loop** — error message as next-prompt context.
9. **Your prompt library** — a career asset you'll build in Lab 17.
10. **Recap + lab preview** — Lab 17: build, test, and diff your library.

## Mini-Quiz

1. **MCQ:** The five prompt parts are: (a) please, task, thanks (b) role, context, schema, constraints, examples ✅ (c) data, code, output (d) title, body, signature.
2. **MCQ:** To describe your data safely in a prompt you should: (a) paste 100 raw rows (b) describe columns, types, and example values ✅ (c) upload the CSV (d) send a screenshot.
3. **MCQ:** After the AI's code raises an error, the best next step is: (a) give up (b) re-prompt including the error message ✅ (c) delete the constraints (d) switch datasets.
4. **Short answer:** Why do constraints like "must fit inside a sklearn Pipeline" matter in a prompt? *(Answer: they force leakage-safe structure — transformations fitted only on training folds — and make the output verifiable against a concrete requirement.)*
