# W04 AI-Assist Overlay — Lab L08

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L08's 2-hour plan — "Draft-then-verify block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Explain reweighing for this group-outcome table: [paste]. Compute the weight for each cell and show your working.
2. Here are my before/after metrics: [paste]. Draft the mitigation section of my bias report - what was applied, what changed, at what cost.
3. My mitigation closed the TPR gap but cost 4 points of accuracy. Is that a good trade? Argue both sides in 4 sentences.

## Failure gallery — how AI goes wrong on THIS task
### Mitigates the test set
The AI applies reweighing weights to test data. Fix: weights are a training-time concept only.

### Declares victory
The AI claims bias was 'removed' without re-measuring. Fix: recompute all three metrics and report the residual gap.


## Reflection scaffold (worked example)
> The AI's reweighing arithmetic was correct and its draft report section was usable. It declared the bias 'resolved' after one metric improved - I re-measured all three and reported the honest residual gap.
