# W04 AI-Assist Overlay — Lab L10

**Tool:** Claude (default) | fall-backs: ChatGPT, Copilot. Substance is tool-agnostic.
**Block:** 20 minutes inside Lab L10's 2-hour plan — "Defend-your-verdict block".
**Maturity level:** Week 3-6: draft-then-diff (medium blocks)

## Ground rules (every AI-assist exercise)
1. **Attempt first** — try the task yourself before prompting. No "ask the AI and submit".
2. **Diff** — compare the AI's solution against your attempt.
3. **Verify** — the 6-point checklist: runs / seeded / leakage-free / spot-checked / APIs real / constraints respected. Run `pytest tests/ -v`.
4. **Reflect** — 3–5 lines: what the AI got right, what it got wrong, what you changed. (The starter notebook's AI-ASSIST BLOCK cell has the log table.)

## Prompt library for this block
1. I claim the lending dataset is riskier to deploy in Singapore than the income dataset because district is a live proxy attribute. Challenge my argument in 4 sentences.
2. Compute the approval-rate gap by district from this table: [paste]. Which districts are systematically disadvantaged?
3. Under PDPA, what makes district a sensitive-adjacent attribute even though it's 'just location'?

## Failure gallery — how AI goes wrong on THIS task
### Superficial comparison
The AI compares dataset sizes instead of bias risk. Fix: force it to compare the specific gaps and proxy sensitivity.

### Reassuring nonsense
The AI says 'both datasets are fine for deployment'. Fix: paste the numbers and make it reconcile them with the claim.


## Reflection scaffold (worked example)
> The AI pushed back hard on my verdict and made me cite the actual district gap number instead of gesturing at 'proxy risk'. My verdict survived, but it's now defensible - and it caught that I'd compared approval rates, not TPR.
