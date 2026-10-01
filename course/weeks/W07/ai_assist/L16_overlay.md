# W07 AI-Assist Overlay — Lab L16

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 15 minutes inside Lab L16's 2-hour plan — "Self-critique tally block".
**Maturity level:** Week 7-8: full vibe-coding loops (40+ min core blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is code you previously generated for a data prep task: [paste script 2]. Critique it for train-test leakage, hallucinated APIs, and silent correctness bugs.
2. You said this script was correct. It resamples before splitting. Explain why that makes the reported recall a lie.
3. Generate a checklist that would have caught your own mistake here.

## Failure gallery — how AI goes wrong on THIS task
### Misses its own bug
The AI reviews its own SMOTE-before-split code and finds nothing wrong - the tally moment.

### Placating correction
When pushed, the AI apologises and 'fixes' it by moving one line instead of restructuring into a Pipeline.


## Reflection scaffold (worked example)
> The AI reviewed its own leaking script and called it correct. When I pasted the test-set class ratio as evidence, it apologised and moved a line - but the real fix was structural. I wrote the Pipeline myself. The tally: it found 0 of 3 planted bugs unaided.
