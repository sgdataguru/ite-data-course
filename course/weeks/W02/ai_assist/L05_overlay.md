# W02 AI-Assist Overlay — Lab L05

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 25 minutes inside Lab L05's 2-hour plan — "Review-my-decisions block".
**Maturity level:** Week 1-2: explain-my-error (small blocks, heavy scaffolding)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my prep-decisions table: [paste table]. I'm feeding a random forest, KNN, and logistic regression. Flag any row where the treatment mismatches the algorithm.
2. For a random forest, which of my prep steps are wasted effort and why? Answer in 3 sentences.
3. Generate 5 quiz questions on choosing encodings, with answers, to test my partner.

## Failure gallery — how AI goes wrong on THIS task
### Invented API
The AI describes a sklearn.preprocessing.TargetEncoder signature that doesn't match the installed version. Fix: check the docs, pin the version.

### Generic advice
The AI says 'scale everything' without distinguishing trees from KNN. Fix: ask it to justify per algorithm, then verify against the matrix.


## Reflection scaffold (worked example)
> The AI found my real mistake - I was scaling features for the tree model unnecessarily. It couldn't explain WHY trees are scale-invariant, so I wrote that justification myself from the theory note.
