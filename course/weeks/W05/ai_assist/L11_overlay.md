# W05 AI-Assist Overlay — Lab L11

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L11's 2-hour plan — "Spot-the-leak block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here are my column names: [paste list]. One of them likely leaks the answer for predicting loan approval. Which one, and why?
2. Write seeded 70/15/15 splitting code with an assertion that no test rows appear in training.
3. My validation score is 0.99 on a messy real-world dataset. Give me three possible explanations ranked by likelihood.

## Failure gallery — how AI goes wrong on THIS task
### Splits after fitting
The AI splits the data after fitting the scaler - contamination by ordering. Fix: split first, always.

### Double-split overlap
The AI calls train_test_split twice on the same data, creating overlapping validation and test sets. Fix: split the holdout once, assert disjointness.


## Reflection scaffold (worked example)
> The AI spotted the leaky column instantly (days_late_on_payment) and explained the time-travel problem well. Its splitting code had a subtle overlap bug my disjoint-index assertion caught - the test I wrote in the lab saved me.
