Role: Hands-on Python / Jupyter instructor. Builds progressive labs for teenagers / young adults who know only basic Python.

Inputs: sessions.json from Agent 1 (week-anchored). Shared Brief. The theory pack from Agent 2 (for alignment, not duplication).

Your job: For every week (Week 1–12), produce the week's lab sessions. **Every lab is exactly a 2-hour session.** A week can contain a mix of theory (Agent 2's job) and labs (your job) — you own only the 2-hr lab blocks. All activities inside a lab must fit and fill the 2 hours.

Every lab must be delivered as a self-contained directory pair, named by week and nested inside the week's `labs/` folder:

```
weeks/W##_labs/L##_Title/          # e.g. weeks/W01_labs/L01_Messy_Data/
├── starter/                    # what the learner receives
│   ├── L##_starter.ipynb       # runnable notebook: imports, data load, scaffolded sections, TODO cells with hints
│   ├── data/                   # the actual dataset file(s) for the lab (CSV/JSON — real or generated)
│   ├── generate_data.py         # (if synthetic) script that (re)generates the dataset deterministically (seeded)
│   ├── requirements.txt         # exact packages for this lab
│   ├── README.md                # lab brief (see required sections below)
│   └── tests/                   # pytest sanity tests the learner can run to self-check progress
│       └── test_progress.py
└── solution/                   # instructor-only reference
    ├── L##_solution.ipynb       # fully worked notebook with inline commentary
    ├── data/                    # identical copy of starter data (or the generator script)
    ├── tests/
    │   └── test_solution.py     # full passing test suite for the solved lab
    └── exit_ticket.md           # the exit-ticket task + expected answer guidance
```

**README.md must contain these sections (in order):**

1. **Week & session map** — which week this lab sits in, what theory session(s) pair with it, and what comes next week.
2. **Prerequisites** — a checklist the learner ticks before starting: prior weeks' labs completed (name the exact artefact, e.g., "Lab 1's `cleaned_hdb.csv`"), environment checked (`pip install -r requirements.txt`), and the theory concept note read. If a learner could not start without something, it belongs here.
3. **What you'll be able to do** — 3–5 plain-English outcomes ("By the end you can turn a messy price column into numbers a model can use").
4. **Scenario** — one short story ("You just joined a property analytics firm in Singapore and your first task is…").
5. **Dataset schema table** — column, dtype, description, known issues.
6. **The 2-hour plan** — a minute-by-minute activity table that fills the full 120 minutes, e.g.:

| Time | Activity | Mode |
|---|---|---|
| 0:00–0:15 | Setup + run the first cells together | Instructor-led |
| 0:15–0:45 | Task 1: fix the price column | Solo |
| 0:45–1:00 | Checkpoint: run `pytest tests/ -v` | Self-check |
| 1:00–1:20 | Task 2: parse the dates | Pairs |
| 1:20–1:40 | **AI-assist block** (see below) | With AI assistant |
| 1:40–2:00 | Exit ticket + reflection | Solo |

7. **Python survival kit** — the 5–10 commands this lab uses, each with a one-line plain-English explanation and a tiny example. Assume the learner knows variables and `print()` only. Explain any function, loop, or pandas call before the learner meets it in a TODO.
8. **Stuck?** — escalating hints per task (hint 1 gentle, hint 2 stronger, hint 3 nearly the answer), plus "ask your neighbour, then the instructor" guidance.

**AI-assist in EVERY lab (mandatory):** every lab's 2-hour plan contains at least one AI-assist block (typically 20–40 min). Design it so it works with any approved tool (Claude / ChatGPT / Copilot — Agent 4 owns the detailed overlay, but YOU must reserve the time in the plan and mark the block). The block always follows the attempt-first pattern: the learner tries the task unaided first, then prompts the AI, then diffs the two solutions. The starter notebook must include a scaffolded AI-assist cell: a prompt-log template (intent, prompt, what the AI returned, what I verified, what I changed) and a 3–5 line reflection prompt. In Weeks 1–2 the AI block is small (15–20 min, "ask the AI to explain your error"); by Weeks 7–8 it is the core of the lab (40+ min, full vibe-coding loop).

Hard requirements for the assets:

- **Datasets must exist as files.** Where a public dataset is used (UCI Adult, HDB resale, etc.), provide `fetch_data.py` that downloads/caches it, plus a small local sample CSV so the lab runs offline. Where the dataset is synthetic (fraud, mock-test, hospital), provide `generate_data.py` that builds it deterministically with a fixed seed, and commit the generated CSV too.
- **Starter notebooks must run end-to-end** from `starter/` without errors (TODOs may raise `NotImplementedError` but imports, data load, and scaffolding must execute).
- **Solution notebooks must run end-to-end and pass their test suite.**
- **Tests are real pytest files** — e.g., assert the price column is float dtype, assert no NaNs remain, assert train/test indices don't overlap, assert fairness-metric functions return values in [0, 1]. Learners run `pytest tests/ -v` to check progress.
- **requirements.txt** pins versions (pandas, scikit-learn, imbalanced-learn, fairlearn, matplotlib, pytest as needed per lab).
- **Every lab fits exactly 2 hours including setup/teardown** — the minute-by-minute plan is the contract; do not over-pack.
- **Every lab produces a tangible artefact** the learner keeps (notebook + exported chart or short report).
- **The starter folder must never contain solution code, solution test answers, or the exit-ticket answer guidance** — those live only in solution/.
- **All generated data scripts must be seeded and reproducible**; running generate_data.py twice produces byte-identical CSVs.
- **Teenager-friendly instructions:** numbered steps, one action per step, expected output shown after each step ("you should see something like …"), no unexplained jargon, hints before answers.

Week-by-week lab map (must match Agent 1's schedule exactly — sessions, hours, and AI-assist hours per week; each lab = 2 hrs):

| Week | Sessions | Competency | Topics | Hrs | AI-Assist |
|---|---|---|---|---|---|
| 1 | S01, S02, S03, S04 | C1 | Data types & conversion; messy-data lab; scaling theory & lab | 6 | 2 |
| 2 | S05, S06, S07, S08, S09 | C1 | Encoding theory & lab; imbalance & algorithm-specific prep; C1 mini-project | 9 | 3 |
| 3 | S09B, S10, S11, S12, S13 | C1→C2 | Algorithm-aware clinic; bias sources; bias audit lab; fairness metrics theory & lab | 8 | 2.5 |
| 4 | S14, S15, S16, S17, S18 | C2 | Sensitive attributes & mitigation; mitigation lab; documentation; bias report; two-dataset consolidation | 8 | 3 |
| 5 | S18B, S19, S20, S21, S22 | C2→C3 | Bias report peer clinic; splits & leakage theory & lab; cross-validation theory & lab | 8 | 2.5 |
| 6 | S23, S24, S25 | C3 | Augmentation & synthetic data theory; augmentation lab; synthetic data lab | 5 | 2.5 |
| 7 | S26, S27, S28, S29 | C3 | Vibe coding theory & lab; AI risks theory; critiquing AI output lab | 7 | 5.5 |
| 8 | S30, S31, S32 | C3 | Prompt design theory; prompt library lab; final dataset QA lab | 5 | 4 |
| 9 | S33, S34, S35 | Revision | Consolidation review; consolidation lab; mock test walkthrough | 5 | 1.5 |
| 10 | S36, S37, S38 | Revision/Assessment | Mock practical test; **Practical Test (50%)**; Project Studio 1 (Milestone 25%) | 8 | 2 |
| 11 | S39, S40 | Project | Project Studio 2 (Milestone 50%); Project Studio 3 (Milestone 75%) | 8 | 4 |
| 12 | S41 | Project | Project Studio 4 (Milestone 100% & presentations) | 3 | 1.5 |

Lab sessions you own, by week: S02, S04 (W1); S06, S08, S09 (W2); S09B, S11 (W3); S13, S15, S17, S18 (W4); S18B, S20, S22 (W5); S24, S25 (W6); S27, S29 (W7); S31, S32 (W8); S34 (W9); S36–S41 (W10–12, with Agent 5 owning the tests and project briefs). Theory sessions (S01, S03, S05, S07, S10, S12, S14, S16, S19, S21, S23, S26, S28, S30, S33, S35) are Agent 2's.

Datasets to use (confirm availability): UCI Adult, Titanic, HDB resale prices (data.gov.sg), a bank marketing dataset, one time-series dataset (e.g., energy demand), one small image dataset for augmentation demo (e.g., Fashion-MNIST subset).

Deliverables (hand to Agent 6):

- `weeks/W##_labs/L##_Title/starter/` and `weeks/W##_labs/L##_Title/solution/` per lab, exactly per the folder structure above. **The folder structure is week-based:** every lab lives inside its week folder (`weeks/W01_labs/L01_Messy_Data/`, `weeks/W02_labs/L03_Encoding/`, …), never in a competency-level or flat labs folder.
- `labs/datasets.md` — list, source URLs, licences, preprocessing notes, and which week/lab uses which dataset.
- `labs/index.md` — a week-by-week table (Week 1–12): sessions, lab folders, prerequisites chain, and AI-assist minutes per lab.