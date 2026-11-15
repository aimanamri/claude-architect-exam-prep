<div align="center">

<img src="assets/hero.gif" alt="ARCH: Claude Certified Architect (CCAR). Pick CCAR-F Foundations or CCAR-P Professional." width="100%">

<br>

[![Exam portal](https://img.shields.io/badge/exam%20portal-open-2F5BB7?style=for-the-badge&labelColor=1a1917)](https://aimanamri.github.io/claude-architect-exam-prep/)
[![CI](https://img.shields.io/github/actions/workflow/status/aimanamri/claude-architect-exam-prep/ci.yml?branch=main&style=for-the-badge&label=ci&labelColor=1a1917)](https://github.com/aimanamri/claude-architect-exam-prep/actions/workflows/ci.yml)
![Status](https://img.shields.io/badge/status-in%20progress-D97757?style=for-the-badge&labelColor=1a1917)
![CCAR-F](https://img.shields.io/badge/CCAR--F-notes%20ready-F3AA8A?style=for-the-badge&labelColor=1a1917)
![CCAR-P](https://img.shields.io/badge/CCAR--P-planned-8A8478?style=for-the-badge&labelColor=1a1917)
![Practice sets](https://img.shields.io/badge/practice%20sets-4-F3AA8A?style=for-the-badge&labelColor=1a1917)

**Study notes and practice exams for the Claude Certified Architect certification.**

[Choose your track](#choose-your-track) · [Exam portal](#exam-portal) · [Study path](#study-path) · [Courses covered](#courses-covered) · [Roadmap](#roadmap) · [Repo map](#repo-map)

<img src="assets/divider.gif" alt="" width="100%">

</div>

> **Work in progress.** The CCAR-F notes, practice sets and the timed [exam portal](https://aimanamri.github.io/claude-architect-exam-prep/) are here now. The CCAR exams are being updated on **17 December 2026**: CCAR-F content will be reviewed against the new guide, and new mocks plus CCAR-P material come after it is published.

## Choose your track

| | **CCAR-F**: Foundations | **CCAR-P**: Professional |
|---|---|---|
| **Status** | Notes and practice sets ready | Planned |
| **What's here** | Notes for all 10 Architect courses, commute cards, 4 practice sets | Nothing yet, waiting on the new exam guide |
| **Start with** | [`00-platform-model-foundations-notes.md`](00-platform-model-foundations-notes.md) | See the [roadmap](#roadmap) |
| **Exam portal** | Sets A–D, random mock; more mocks after 17 Dec | Track scaffolded: planned exams shown as "Coming soon" |

## Exam portal

<a href="https://aimanamri.github.io/claude-architect-exam-prep/"><img src="quiz-site/icons/icon-192.png" alt="CCAR Exam Portal icon" width="64" height="64" align="left"></a>

**[▶ Open the exam portal: aimanamri.github.io/claude-architect-exam-prep](https://aimanamri.github.io/claude-architect-exam-prep/)**<br>
Free, no sign-up, runs in the browser. It's checked by CI and redeployed on every push to `main`.

<br clear="left">

Pick **CCAR-F Foundations** or **CCAR-P Professional** at the top of the dashboard. Each track keeps its own exams, progress and history.

| Track | Available now | After the 17 Dec 2026 update |
|---|---|---|
| **CCAR-F** | Sets A–D (124 questions), random mock | Mock exams 1–2, Good/Better/Best set, Must-Remember drill; Sets A–D reviewed |
| **CCAR-P** | Planned exams listed as "Coming soon" | Mock exams, case-study set, Good/Better/Best set, Must-Remember drill |

**Features** (shared with the [Developer exam portal](https://github.com/aimanamri/claude-dev-exam-prep)):
- **Exam portal:** dashboard, briefing screen, a timer you can hide, pause/resume, flag for review, question navigator, strike-out, and Exam or Practice mode.
- **Accessibility:** A−/A+ text size, high-contrast dark mode, highlighter, resizable split view for long scenarios, full keyboard control, and WCAG AA contrast.
- **Score report:** a per-course (C1–C10) breakdown, reasoning for every answer, retake, and "retry missed".
- **Installable PWA:** works offline, with a pixel-art icon made from a [Pixelbolt](https://github.com/skulitom/Pixelbolt) recipe.
- **Private:** progress stays in your browser's `localStorage`.

<details>
<summary><b>Run it locally, add sets, and CI</b></summary>

```bash
cd quiz-site
python3 server.py --open      # http://localhost:8775, Python 3 only
```

- **Add a set:** drop a markdown file into `quiz-site/sets/foundations/` or `quiz-site/sets/professional/` (format in [`quiz-site/FORMAT.md`](quiz-site/FORMAT.md)). Press **Reload sets** locally, or push to `main`. Planned "coming soon" cards live in `quiz-site/quiz.config.json`.
- **CI** ([`ci.yml`](.github/workflows/ci.yml)) runs on every push and pull request. It syntax-checks the code, checks the manifest and icons, builds the static site, and runs [`validate.js`](quiz-site/validate.js), which fails on any skipped question, missing answer, unknown track or unknown course code. The Pages deploy runs the same validation first.
- **Check locally before pushing:** `python3 quiz-site/build_static.py --out _site && node quiz-site/validate.js _site/sets.json`

</details>

## Study path

For CCAR-F. Each step feeds the next.

| Step | Do this | Why |
|:-:|---|---|
| **1** | Read the foundations notes ([`00`](00-platform-model-foundations-notes.md)) | The four decisions behind every session: entry point, capability layer, model, context |
| **2** | Read the full notes ([`01`](01-full-study-notes.md)) | All ten courses, each with must-remember facts, syntax, debug priority and trade-offs |
| **3** | Reread the recall cards daily ([`02`](02-commute-recall.md)) | Short, phone-friendly blocks: one per stop |
| **4** | Take Sets A and B | 32 questions each, course-style: "it worked in dev, broke in prod; pick the targeted fix" |
| **5** | Take Sets C and D | 30 questions each, certification-style: BEST/FIRST/NOT, choose-two and ordering items |

Two ideas repeat across the whole path:
- **Technically:** put the right thing in the right layer (prompt vs Skill vs hook vs tool vs MCP vs subagent; proxy vs gateway; Enterprise vs cloud path).
- **In delivery:** decide and measure before Day 1: path, gap memo, baseline, champion.

## Courses covered

Notes follow the ten courses on the Skilljar **Claude Architect** learning path. Every section uses the same layout: **must remember**, **syntax**, **debug priority**, **trade-offs and fixes**.

| # | Course | Focus |
|:-:|---|---|
| C1 | AI Capabilities and Limitations | Four machine properties and how they collide |
| C2 | AI Fluency for Builders | The 4D Framework applied to building products |
| C3 | Claude Platform & Model Foundations | Entry point, capability layer, model, context |
| C4 | Claude Platform 101 | Messages API, agent loop, tools, thinking, skills, MCP, managed agents |
| C5 | Claude Code 101 | Loop, permissions, workflow, context, CLAUDE.md, subagents, MCP, hooks |
| C6 | Introduction to Model Context Protocol | Building MCP servers and clients in Python |
| C7 | Introduction to subagents | Creating, designing and choosing subagents |
| C8 | Product Foundations | What Claude Code is, model selection, the seven platform paths |
| C9 | Deployment Architecture | Path decision, parity gaps, proxy, LLM gateway, ZDR and residency |
| C10 | Delivery Methodology | Qualification, pilot design, ROI, adoption curve, champions, 30-day activation |

<details>
<summary><b>Known gaps in the notes</b></summary>

- Lesson **videos** in C1, C2, C4, C5 and C7 were not transcribed; the written lesson text was captured in full.
- C6 lesson videos failed to load; the written summaries were captured.
- End-of-course quizzes were not attempted.
- Course code was checked against the `claude-api` skill (cached 2026-10-06). Where the shape has since changed, the note says so under **API drift** at the end of the full notes.

</details>

## Roadmap

- [x] CCAR-F notes for all ten courses
- [x] Commute recall cards
- [x] Practice Sets A–D with answers and reasoning
- [ ] Review everything against the new exam guide (17 December)
- [x] Timed exam portal with CCAR-F / CCAR-P tracks, PWA and CI ([#1](https://github.com/aimanamri/claude-architect-exam-prep/issues/1))
- [ ] CCAR-F mock exams, Good/Better/Best set and Must-Remember drill (after 17 December)
- [ ] CCAR-P notes and practice sets

## Repo map

```text
.
├── 00-platform-model-foundations-notes.md   the foundational course (C3)
├── 01-full-study-notes.md                   all ten courses
├── 02-commute-recall.md                     recall cards
├── 03-practice-exams.md                     Sets A–D with answers and reasoning
├── quiz-site/                               exam portal / PWA (server.py, static build, validate.js, sets/, icons/)
├── .github/workflows/                       ci.yml (checks) and pages.yml (deploy)
├── assets/                                  README pixel art and the script that generates it
└── Architect Exam Prep.md                   Obsidian index note
```

The notes are Obsidian-flavoured markdown (`[[wikilinks]]`) but read fine anywhere.

## Disclaimer

Unofficial study material, written from the course modules for personal exam preparation. Not affiliated with or endorsed by Anthropic or Pearson. The portal has the [full disclaimer](https://aimanamri.github.io/claude-architect-exam-prep/#disclaimer). Confirm version-specific details (model IDs, prices, limits, beta headers) at [platform.claude.com](https://platform.claude.com) before relying on them.

<div align="center">
<sub>Pixel art in <code>assets/</code> is generated by <a href="assets/make_art.py"><code>make_art.py</code></a>. The app icon is a <a href="https://github.com/skulitom/Pixelbolt">Pixelbolt</a> recipe generated by <a href="quiz-site/og/make_icon.py"><code>make_icon.py</code></a>.</sub>
</div>
