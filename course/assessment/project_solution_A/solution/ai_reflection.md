# AI-Usage Reflection — Option A Worked Solution (exemplar)

## Ledger

| Date | Tool | Task | Prompt summary | Verification performed | What I changed |
|---|---|---|---|---|---|
| M1 | Claude | Explain dtype error | "resale_price astype(float) failed with: [error]" | Ran the fix; range check 100k–2M passed | Nothing — the fix was correct |
| M1 | Claude | Suggest sanity checks | "What two sanity checks should I run after converting prices from strings?" | Compared against the theory note's list | Added the null-count-before/after check it missed |
| M2 | Claude | Draft bias report | "Draft the mitigation section from these before/after numbers: [paste]" | Recomputed every number myself | Rewrote 2 sentences that overstated the fix |
| M3 | Claude | Vibe-code the ColumnTransformer | 5-part prompt: role, context, schema, constraints, example | pytest + diff against my manual Lab 5 approach | Kept mine — the AI's ordinal order was alphabetical |
| M4 | Claude | Review QA checklist | "Does my readiness checklist check for train-test leakage?" | Read the checklist line by line | Added the leakage check it had skipped |

## Reflection (the graded 3–5 lines)

The AI was fastest at explaining errors and drafting report prose. It twice produced
plausible-but-wrong output: an alphabetical ordinal order (inventing an order that
would mislead the model) and a report sentence claiming bias was "removed" when the
gap had only narrowed. My verification — recomputing every number and diffing against
my manual pipeline — caught both. The lesson I keep: the AI drafts, I decide.

## What I would tell a student

If your ledger says the AI was always right, you weren't verifying. The best entries
in this ledger are the two where the AI was wrong and I can prove it.
