# DE5002FP — End-to-End Data Prep Project (40%, 15 hrs, C1→C3)

**For you, the student.** This is your biggest piece of work in the module — and the most like a real job. You'll pick ONE real Singapore dataset, take it from raw and messy to clean, fair, and machine-learning-ready, and present it like you would to a boss.

**Read this whole brief once before you start.** Then use the checklists at each milestone.

---

## The three options — all real data from data.gov.sg

All three options use **real, public Singapore government data** from [data.gov.sg](https://data.gov.sg). Each one has a different "flavour" — pick the one that interests you most.

### Option A — HDB Resale Price Prep 🏢
**Dataset:** *Resale Flat Prices* (data.gov.sg) — every HDB resale transaction, updated regularly. ~90,000+ rows.
**Your job:** A property company wants to build a flat-price prediction model. Prepare the data so the model is accurate AND fair across towns and flat types.
**Why it's interesting:** You'll find out which towns are "under-represented" in the data, whether the model would systematically misprice certain flat types, and how to fix that.
**Data link:** search "Resale Flat Prices" on data.gov.sg (HDB / SingStat publisher). CSV download, licence: Singapore Open Data Licence.

### Option B — Taxi & Transport Demand Prep 🚕
**Dataset:** *Passenger Volume by Train Station* or *Taxi Availability* (data.gov.sg, LTA / MyTransport) — MRT entry/exit volumes per station per day, or real-time taxi availability records.
**Your job:** A transport planner wants to predict crowd demand at stations. Prepare the data — handle the time-series properly (no time travel!), check fairness across station lines (does the model under-serve the North?), and make it model-ready.
**Why it's interesting:** This is a **time-series** project — you'll use TimeSeriesSplit, and you'll discover how rush-hour patterns and under-represented stations create bias.
**Data link:** search "Passenger Volume by Train Station" on data.gov.sg (LTA publisher). CSV/API, Singapore Open Data Licence.

### Option C — Energy & Household Prep ⚡
**Dataset:** *Monthly Household Electricity Consumption by Town* or *Half-Hourly Energy Demand* (data.gov.sg, EMA / SingStat) — electricity usage by planning area, month, and dwelling type.
**Your job:** An energy company wants to predict household consumption for planning. Prepare the data — handle the town-level representation gaps (small towns = few rows), audit whether dwelling types are treated fairly, and deliver an ML-ready dataset.
**Why it's interesting:** You'll see how **aggregation bias** appears in real life — one model for all towns hides very different usage patterns — and you'll practise grouping rare categories.
**Data link:** search "Household Electricity Consumption" or "Energy Demand" on data.gov.sg (EMA publisher). CSV/XLSX, Singapore Open Data Licence.

**How to choose:** Pick A if you like property/money questions. Pick B if you like transport and time-series. Pick C if you like sustainability and town-level patterns. **All three are marked identically** — choose by interest, not by "which is easier".

---

## What you must hand in (all five, no exceptions)

1. **Cleaned dataset** (CSV) — your final, prepared, ML-ready data.
2. **Jupyter notebook** — your full working, with every decision explained in Markdown cells.
3. **1-page bias report** (`bias_report.md`) — the 5-section template from Lab 9.
4. **1-page AI-usage reflection** (`ai_reflection.md`) — your honest ledger of GenAI use.
5. **5-slide presentation** — your story: problem → data → what you found → what you fixed → what's still risky.

---

## The four milestones (your studio sessions are your checkpoints)

### Milestone 1 — 25% (Week 10 studio): Clean & Type
- [ ] Downloaded your dataset from data.gov.sg and loaded it in pandas
- [ ] `df.info()` audit: every column typed correctly (dates parsed, numbers are numbers)
- [ ] Missing values handled — each choice justified (drop / impute / flag)
- [ ] Implausible values caught (negative prices? future dates? zero consumption?)
- [ ] **Prep-decisions table**: column → what you did → why (like Lab 5)
- [ ] GenAI used at least once here, logged (e.g., "explain this error", "suggest sanity checks")

### Milestone 2 — 50% (Week 11 studio): Bias Audit & Mitigation
- [ ] Representation check: which groups/towns/stations are under-represented? (numbers, not vibes)
- [ ] Group-wise summary stats — where do the gaps appear?
- [ ] Three fairness metrics computed on a sensitive-ish attribute (town / line / dwelling type)
- [ ] ONE mitigation applied (reweighing or resampling) — before/after table
- [ ] **1-page bias report** written (5 sections, every claim has a number)
- [ ] GenAI used to draft or critique your report — logged, and you verified every number

### Milestone 3 — 75% (Week 11 studio): Split, Enhance, Cross-Validate
- [ ] Leakage-free 70/15/15 split (or TimeSeriesSplit if Option B) — seeded
- [ ] Disjoint-index assertion passes
- [ ] CV strategy chosen and justified (stratified? time-series? why?)
- [ ] Augmentation OR synthetic data applied — with plausibility checks
- [ ] GenAI used for one prep task (vibe-coded), diffed against your manual attempt — logged

### Milestone 4 — 100% (Week 12 studio): QA, Reflect, Present
- [ ] Final QA checklist run (Lab 18's): types, leakage, balance, constraints — all green or justified
- [ ] AI-usage ledger complete: every session, tool, task, verification
- [ ] 5-slide deck built and rehearsed once
- [ ] All five artefacts submitted

---

## How to use GenAI in this project (required — and graded)

You MUST use GenAI tools in this project. But you must use them **like a professional, not like a shortcut**. Here is exactly how, with examples for each option.

### The golden rules
1. **Attempt first.** Try it yourself. Then ask the AI. Then compare.
2. **Never paste raw personal data.** data.gov.sg data is public and aggregated, so it's safe — but never develop the habit of pasting raw rows. Describe the schema and statistics instead.
3. **Verify everything.** The AI's code is a hypothesis until your tests pass and your spot-checks agree.
4. **Log every use.** Your ledger is graded. Undisclosed AI use = academic dishonesty.

### Real example prompts (copy, adapt, and log)

**Milestone 1 — cleaning (any option):**
> "You are helping me prepare the data.gov.sg HDB resale dataset for a price prediction model. The column `resale_price` is a string like '$530,000'. Context: 90,000 rows, 2017–2024. Schema: town (str, 26 values), flat_type (str, 7 values), floor_area_sqm (float), resale_price (str, target). Constraints: pandas only; convert resale_price to float; show me a sanity check that the range is plausible. Example: '$530,000' → 530000.0."

**Milestone 2 — bias audit (Option A):**
> "My HDB dataset has these town representation shares: [paste value_counts output]. Which towns are under-represented relative to Singapore's actual dwelling distribution, and what evidence would I look for to show representation bias? Answer with the checks I should run, not conclusions."

**Milestone 2 — fairness metrics (Option B):**
> "I computed daily MRT entry volumes per station. My model under-predicts North-South Line stations by 15% on average compared to East-West Line. Explain what this gap means in plain English for a transport planner, in 3 sentences. Then suggest one mitigation I could apply to the training data."

**Milestone 3 — vibe-coded prep (any option):**
> "You are preparing [my dataset] for [my model]. Standardise the numeric columns [list], one-hot encode [nominal column] with handle_unknown='ignore', and ordinal-encode [ordered column] with this order: [order]. Output a single sklearn ColumnTransformer. Do not fit anything yet — just build the object."

**Milestone 4 — QA (any option):**
> "Here is my data-readiness checklist code: [paste]. Review it: does it check for train-test leakage? Does it verify domain constraints (no negative prices, no future dates)? Add any missing check."

### What "good GenAI use" looks like in your ledger

| Date | Tool | Task | Prompt summary | Verification performed | What I changed |
|---|---|---|---|---|---|
| W10 | Claude | Explain dtype error | "resale_price astype(float) failed with [error]" | Ran the fix; checked range 100k–2M | Nothing — fix was correct |
| W11 | Claude | Draft bias report section | "Draft mitigation section from these before/after numbers" | Recomputed every number myself | Rewrote 2 sentences that overstated the fix |
| W11 | ChatGPT | Vibe-code the ColumnTransformer | 5-part prompt with schema | Ran pytest; diffed vs my Lab 5 approach | Kept mine — AI's ordinal order was alphabetical |

### What "bad GenAI use" looks like (and loses marks)
- ❌ Pasting the AI's code straight into your notebook with no verification
- ❌ Asking the AI to "write my bias report" and submitting its output
- ❌ A ledger that says "used AI for everything" with no specifics
- ❌ No reflection on what the AI got wrong (if it never got anything wrong, you weren't verifying)

---

## Marking rubric (100 marks)

| Criterion | Marks | What the marker looks for |
|---|---|---|
| Data Preparation | 20 | Correct types, justified missing-value handling, sanity checks, decisions table |
| Bias Detection & Mitigation | 20 | Numeric evidence, correct metrics, honest before/after, trade-off stated |
| Dataset Splitting & Enhancement | 15 | Leakage-free, seeded, justified CV strategy, disjoint assertion |
| Dataset Enhancement (augmentation/synthetic) | 15 | Plausibility checks, labels preserved, distribution comparison |
| Use of GenAI to automate data preparation | 15 | Ledger quality, attempt-first evidence, verification shown, reflection honest |
| Data Analysis & Visualisation | 15 | Charts that tell the story; the 5-slide deck |

**AI-usage requirement:** the project MUST demonstrate GenAI use with a complete ledger. Fabricating or omitting entries is academic dishonesty (see behavioural rubric).
