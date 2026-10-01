# S10 — Sources of Bias in Datasets (C2, 1 hr)

## Concept Note

**Definition.** Bias is systematic error — the data misrepresents reality in a *consistent direction*, so a model trained on it will be consistently unfair or wrong.

**Five sources to know:**

1. **Historical bias.** The data faithfully records an unfair past. A loan dataset from an era when certain districts were redlined reflects discriminatory lending — the model learns discrimination as "pattern".
2. **Representation bias.** The sample doesn't cover the population. A health dataset collected at one polyclinic under-represents residents who use private care; a face dataset of mostly light-skinned subjects fails dark-skinned users.
3. **Measurement bias.** The *way* we measure differs across groups. If part-time workers' income is self-reported but full-time workers' is verified by IRAS records, income comparisons across employment types are distorted.
4. **Aggregation bias.** One model for heterogeneous groups. Averaging HDB resale prices island-wide hides that the relationship between floor area and price differs sharply between central and non-central towns.
5. **Deployment bias.** The model is used in a context it wasn't built for. A credit model trained on salaried applicants deployed to gig-economy applicants — the data was fine, the *use* is biased.

**Worked example by hand.** A hiring dataset: 80% male applicants in tech roles historically, and 90% of past hires were male. A model learning "what past hires looked like" will rank male CVs higher — historical bias compounded by representation bias. The data is "accurate"; the outcome is unfair.

**Singapore/APAC lens.** Sensitive attributes here include race, religion, age, gender, marital status, and — carefully — postal district (a proxy for ethnicity and income in some analyses). PDPA governs the handling of personal data; proxies (postal code standing in for race) must be treated as sensitive.

**What you will later ask an AI to do:** brainstorm plausible bias sources for a dataset description; write group-wise summary statistics to expose representation gaps; draft a bias-risk paragraph for a report.

## Slide Outline

1. **Title** — Biased data, biased models.
2. **Bias = systematic error** — wrong in a consistent direction.
3. **Historical bias** — the unfair past, faithfully recorded.
4. **Representation bias** — who's missing from the sample?
5. **Measurement bias** — same concept, different rulers.
6. **Aggregation bias** — one model, many populations.
7. **Deployment bias** — right model, wrong context.
8. **Worked example** — the hiring dataset.
9. **Proxies are sensitive too** — postal district ↔ ethnicity/income.
10. **PDPA context** — sensitive data handling in Singapore.
11. **Recap + lab preview** — Lab 6 audits a real dataset for these five.

## Mini-Quiz

1. **MCQ:** A face-recognition dataset with 90% light-skinned subjects exhibits: (a) historical bias (b) representation bias ✅ (c) aggregation bias (d) deployment bias.
2. **MCQ:** Historical bias is hard because the data is: (a) inaccurate (b) accurate but reflects unfair practice ✅ (c) too small (d) unlabeled.
3. **MCQ:** Using postal district as a stand-in for income is dangerous because: (a) districts change (b) it's a proxy that behaves like a sensitive attribute ✅ (c) postal data is expensive (d) models can't read strings.
4. **Short answer:** Give one example of measurement bias in a Singapore context. *(Answer: e.g., income verified via IRAS for employed residents but self-reported for self-employed/freelancers, making cross-group income comparisons systematically distorted.)*
