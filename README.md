# Curriculum Design Course Generator

A set of agent prompts that turns one **course work document** (a module spec, syllabus, or skills-standard extract) into a complete course pack you can teach from. The pack covers the schedule, theory notes, hands-on labs, AI-assisted exercises, assessments with rubrics, and an offline HTML course portal.

The prompts are written for any course. Every number, competency, topic, and assessment comes from the document you supply.

## Quick start

1. Put your course document in `inputs/` (Markdown, PDF, or Word), or paste or attach it in the chat.
2. Open an AI coding assistant (Claude Code, Copilot Chat, etc.) in this repo.
3. Give it [.github/prompts/0-Curriculum Architect.md](.github/prompts/0-Curriculum%20Architect.md) along with the document, and ask it to run the full pipeline.
4. Find the output in `courses/<slug>/`. Start with `brief.md` to check what was extracted and what was assumed, then open `course_portal.html`.

To build another course, repeat with a new document. Each course gets its own folder under `courses/`.

## The pipeline

| Step | Prompt | Produces |
|---|---|---|
| 0. Orchestrator | [0-Curriculum Architect.md](.github/prompts/0-Curriculum%20Architect.md) | `brief.md`, `brief.json`: the Shared Brief pulled from your document |
| 1. Session Blueprint Architect | [0.1-Session Blueprint Architect.md](.github/prompts/0.1-Session%20Blueprint%20Architect.md) | `sessions.json`, `schedule.md`: every session, week by week |
| 2. Theory Content Designer | [1-Theory Content Designer.md](.github/prompts/1-Theory%20Content%20Designer.md) | Concept notes, tool primers, slide outlines, quizzes, reading lists |
| 3. Practical Lab Designer | [2-Practical Lab Designer.md](.github/prompts/2-Practical%20Lab%20Designer.md) | Starter and solution labs with data, self-checks, and exit tickets |
| 4. AI-Assist Integration Specialist | [3-AI-Assist Integration Specialist.md](.github/prompts/3-AI-Assist%20Integration%20Specialist.md) | AI overlay for each lab, mini-modules M1–M3, tool policy, AI-assist hours ledger |
| 5. Assessment Designer | [4-Assessment Designer.md](.github/prompts/4-Assessment%20Designer.md) | One pack per assessment, mocks, rubrics, criteria coverage table |
| 6. Web Design & Delivery Agent | [5-Web Design & Delivery Agent.md](.github/prompts/5-Web%20Design%20%26%20Delivery%20Agent.md) | `course_portal.html`, `GAPS.md`, `handoff_note.md` |

Each agent does only its own job and builds on the output of the agents before it. `schedule.md` is the single source of truth for what happens in each week.

## What the course document should contain

The more of these the document states, the fewer assumptions the pipeline makes:

- Module code, title, duration (months or weeks), and total hours
- Theory / practical hour split
- Competencies, each with scope topics, hours, and performance criteria
- Assessments: name, type, duration, weight, which competencies they cover, AI policy
- Learner profile and delivery mode (classroom, lab, tools used)

When something is missing, Step 0 fills it with a default and records the choice in `brief.md` under *Assumptions & Gaps*. Review that section before you teach from the pack.

| If the document doesn't say… | Default |
|---|---|
| AI-assist share | 40% of total hours |
| Lab length | 2-hour blocks |
| Weeks | months × 4.33, rounded (3 months = 12 weeks) |
| Theory / practical split | 25% / 75% |
| Locale and data-protection law | Singapore, PDPA |
| Tools | Inferred from the subject (for example, data courses use Python + Jupyter) |
| AI policy for assessments | Not allowed in timed tests; allowed with citation in projects |

## Output layout

```
courses/<slug>/
├── brief.md / brief.json         # Shared Brief + Assumptions & Gaps
├── sessions.json / schedule.md   # Blueprint
├── weeks/W01 … W##/
│   ├── theory/                   # Concept notes per theory session
│   ├── labs/L##_<Title>/         # starter/ + solution/
│   ├── ai_assist/                # Overlay per lab
│   └── assessment/               # Only in weeks with an assessment sitting
├── theory/  labs/  ai_assist/  assessment/   # Items that span several weeks
├── course_portal.html
├── GAPS.md
└── handoff_note.md
```

## Design principles in every course

- **AI-assist rule.** About 40% of teaching time (or the share the document sets) has learners actively using an AI assistant, spread through every competency.
- **Attempt first.** Learners try each task on their own, then prompt the AI, then compare and critique the two results.
- **Traceability.** Every session links to a competency, every rubric criterion to a performance criterion, and every AI-assist hour to the ledger.
- **No fabrication.** Later agents fill in what was scheduled. Anything missing goes into `GAPS.md`.

## Other files

- [.github/prompts/00-Design the Webpage](.github/prompts/00-Design%20the%20Webpage%20): a standalone prompt for designing and building a web page. It is not part of the pipeline.
