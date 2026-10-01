# W06 AI-Assist Overlay — Lab L13

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L13's 2-hour plan — "Write-then-check block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Write Gaussian jitter augmentation for these columns: [paste]. The noise must be 5% of each column's std, seeded, and must NOT touch the label. Then explain how I verify the labels survived.
2. Here is my augmentation code: [paste]. Did I accidentally jitter the label or the test set?
3. My augmented distribution looks identical to the original. Is that success or failure? Explain.

## Failure gallery — how AI goes wrong on THIS task
### Jitters the label
The AI includes the target column in the jitter loop - the label no longer means anything. Fix: exclude it, assert equality before/after.

### Augments the test set
The AI augments all rows including test. Fix: augment training data only.


## Reflection scaffold (worked example)
> The AI's jitter code was clean and seeded, but it included resale_price in the loop - my labels-unchanged assertion caught it immediately. That assert is now permanently in my notebook.
