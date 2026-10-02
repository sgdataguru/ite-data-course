# W02 AI-Assist Overlay — Lab L04

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L04's 2-hour plan — "Argue-the-tradeoff block".
**Maturity level:** Week 1-2: explain-my-error (small blocks, heavy scaffolding)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. My fraud dataset is 990:10 with 1,000 rows. Argue undersampling vs oversampling vs SMOTE in 5 sentences, then recommend one.
2. Here is my resampling code: [paste]. Does SMOTE touch my test set anywhere? Show me the exact line if so.
3. Why did my accuracy stay at 99% after SMOTE while recall jumped? Explain like I'm new to this.

## Failure gallery — how AI goes wrong on THIS task
### SMOTE before split
The AI resamples the whole dataset before splitting - the test set becomes synthetic-balanced and recall is a beautiful lie. Fix: imblearn Pipeline so resampling happens per training fold.

### Accuracy-only evaluation
The AI reports only accuracy on a 99:1 problem. Fix: recall, F1, and a confusion matrix.


## Reflection scaffold (worked example)
> The AI's SMOTE argument was solid and matched what we learned. Its first code snippet resampled before the split - exactly the bug from the failure gallery. I wrapped it in an imblearn Pipeline and the honest metrics appeared.
