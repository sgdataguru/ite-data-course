# W04 AI-Assist Overlay — Lab L07

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L07's 2-hour plan — "Explain-the-gap block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my confusion-matrix table by group: [paste]. Compute demographic parity, equalised odds (TPR and FPR), and predictive parity (precision) for each group.
2. My TPR gap is 17 points between groups A and B. Explain what that means in plain English for a non-technical report, in 3 sentences.
3. Which of my three metrics failed worst, and what does that specific failure mean for a loan applicant from group B?

## Failure gallery — how AI goes wrong on THIS task
### Metric confusion
The AI calls an approval-rate gap 'equalised odds'. Fix: equalised odds is TPR+FPR equality - make it recompute from the confusion matrix.

### Wrong split
The AI computes fairness metrics on the training set. Fix: metrics belong on held-out predictions.


## Reflection scaffold (worked example)
> The AI computed all three metric tables correctly once I pasted the confusion matrices. It kept conflating parity with equalised odds in its explanation, so I rewrote the plain-English sentence myself using the theory note's definitions.
