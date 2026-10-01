# S12 — Fairness Metrics (C2, 2 hrs)

## Concept Note

**Setup.** A loan model approves or rejects applicants. We care whether it treats groups (defined by a sensitive attribute) equally. Three metrics, three definitions of "fair" — and they can conflict.

**1. Demographic Parity.** The approval *rate* should be equal across groups.
P(approve | group A) = P(approve | group B).
Simple, intuitive. Weakness: it ignores whether the groups genuinely differ in qualification — parity might force the model to approve unqualified applicants from one group.

**2. Equalised Odds.** Among *qualified* applicants, approval rates should be equal; among *unqualified* applicants, rejection rates should be equal. Formally: equal true-positive rates AND equal false-positive rates across groups. This is the strictest popular criterion — it demands the model be equally *accurate* across groups, not just equally *generous*.

**3. Predictive Parity.** Among applicants the model *approves*, the actual qualification rate should be equal across groups. Equal precision per group. A lender's view: "of the people I approve from each group, the same fraction should repay."

**Worked example by hand.** 100 applicants per group.
- Group A: 80 qualified, 20 not. Model approves 70 of the qualified, 5 of the unqualified → TPR = 70/80 = 87.5%, approval rate = 75/100 = 75%.
- Group B: 60 qualified, 40 not. Model approves 42 of the qualified, 8 of the unqualified → TPR = 42/60 = 70%, approval rate = 50/100 = 50%.
Demographic parity: fails (75% vs 50%). Equalised odds: fails (TPR 87.5% vs 70%). Predictive parity: precision A = 70/75 = 93.3%, precision B = 42/50 = 84% — also fails. One model, three failures — metrics are diagnostic, not automatic fixes.

**Why you can't have everything.** Impossibility results show that when base rates differ between groups, you generally cannot satisfy all criteria simultaneously. Choosing a fairness metric is a *values* decision that must be documented — which is why C2 includes documentation.

**What you will later ask an AI to do:** compute these three metrics from a confusion-matrix table; explain a parity gap in plain English for a report; suggest which metric fits a given business context.

## Slide Outline

1. **Title** — Three definitions of fair.
2. **The setup** — a loan model, two groups, one question.
3. **Demographic parity** — equal approval rates; the formula; the weakness.
4. **Equalised odds** — equal TPR and FPR; the strictest criterion.
5. **Predictive parity** — equal precision; the lender's view.
6. **Worked example, part 1** — Group A's numbers by hand.
7. **Worked example, part 2** — Group B's numbers by hand.
8. **Scoring the example** — all three metrics fail; what now?
9. **The impossibility result** — differing base rates break compatibility.
10. **Choosing a metric is a values decision** — document it.
11. **Metrics are diagnostics** — they locate unfairness; mitigation (next) addresses it.
12. **Recap + lab preview** — Lab 7 computes all three with fairlearn.

## Mini-Quiz

1. **MCQ:** Demographic parity requires: (a) equal TPR across groups (b) equal approval rates across groups ✅ (c) equal precision across groups (d) identical features.
2. **MCQ:** Equalised odds demands equality of: (a) approval rates only (b) TPR and FPR across groups ✅ (c) precision only (d) dataset sizes.
3. **MCQ:** Predictive parity is about: (a) who gets approved (b) whether approved people are equally qualified across groups ✅ (c) training speed (d) feature importance.
4. **Short answer:** Why can't a model usually satisfy all three metrics when group base rates differ? *(Answer: impossibility results — when qualification rates differ between groups, equalising one of approval rate, error rates, or precision necessarily breaks another; trade-offs are mathematically forced.)*
