# W08 AI-Assist Overlay — Lab L17

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 40 minutes inside Lab L17's 2-hour plan — "Library build-and-test block".
**Maturity level:** Week 7-8: full vibe-coding loops (40+ min core blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. Here is my prompt draft for an encoding task: [paste]. Score it against the 5-part structure (role, context, schema, constraints, examples) and rewrite the missing parts.
2. Test this prompt yourself: [paste]. What code would you return, and does it respect my constraint of fold-safe target encoding?
3. For each of my 8 prompts, predict the single most likely way the output would fail verification.

## Failure gallery — how AI goes wrong on THIS task
### Constraint-free prompts
The AI happily 'improves' a prompt by removing constraints for brevity. Fix: constraints are the point.

### Untested confidence
The AI declares all 8 prompts 'excellent' without running them. Fix: every entry needs a recorded checklist result.


## Reflection scaffold (worked example)
> The AI rewrote my vague cleaning prompt into a proper 5-part structure - big improvement. But it kept deleting my constraints to 'simplify', and declared untested prompts excellent. My library now records a test result for every entry.
