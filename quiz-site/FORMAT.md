# CCAR exam portal: run it, add sets, CI

## Run it
```bash
cd "claude-architect-exam-prep/quiz-site"
python3 server.py --open          # http://localhost:8775
```
Or double-click `Start Quiz.command` in Finder. Python 3 only, nothing to install. Progress, paused exams and scores are saved in your browser's local storage, **separately for each track** (`ccar.f.*` and `ccar.p.*`).

## Hosted copy (GitHub Pages) and CI
- **Live site:** https://aimanamri.github.io/claude-architect-exam-prep/, rebuilt by `.github/workflows/pages.yml` on every push to `main`.
- **CI:** `.github/workflows/ci.yml` runs on every push and pull request:
  - syntax checks of the JS and Python
  - the manifest, icons and `og-image.png` are present
  - a full static build
  - `validate.js` over the built `sets.json`
- **Validation gate:** the Pages deploy runs the same validation, so a broken set never goes live.

Check before pushing:
```bash
python3 quiz-site/build_static.py --out _site && node quiz-site/validate.js _site/sets.json
```
`validate.js` fails on:
- skipped questions (no answer, or an answer letter that isn't an option)
- answers with no reasoning
- a set whose track isn't in `quiz.config.json`
- course codes not in `moduleNames`
- duplicate set keys
- a track with neither sets nor planned exams

## Tracks and where questions come from
`quiz.config.json` defines:
- **`tracks`**: `F` = CCAR-F Foundations, `P` = CCAR-P Professional. Each track has a `notice` shown on the dashboard and a list of `placeholders` (planned exams, rendered as disabled "Coming soon" cards).
- **`moduleNames`**: course codes C1–C10, shown as section names, chips and score-report rows.
- **`sources`**, each tagged with a `track`:
  - `../03-practice-exams.md` → Foundations Sets A–D (course ranges and timing per set are in the config)
  - `sets/foundations/` → every `.md` file here is a CCAR-F set
  - `sets/professional/` → every `.md` file here is a CCAR-P set

Files starting with `_` or `.` are ignored (each folder has a `_README.md`).

**After the 17 December 2026 exam update:** when a planned exam's set is added, remove its entry from that track's `placeholders`, and update or remove the track `notice`. Re-check Sets A–D against the new Foundations exam guide.

## Set file format
```markdown
---
title: CCAR-F · Mock exam 1      # card title
minutes: 60                      # time limit (or secondsPerQuestion: 90)
description: One line shown on the card.
code: M1                         # optional: exam code becomes CCARF-M1 (defaults to the ID letters)
shuffle: always                  # optional: always shuffle questions and options (drills)
---
# SET K (mock exam 1)

## C3 Platform & Model Foundations    # a heading with a course code C1–C10 sets the course for the questions below it

**K1.** Question stem. Add #core at the end to tag a repeated must-remember item.
- A. Option text
- B. Option text
- C. Option text
- D. Option text

**K2.** (Choose TWO) Multi-select stem.
- A. ...
- B. ...
- C. ...
- D. ...
- E. ...

# ANSWER KEY & REASONING

**K1 – C.** Reasoning shown after the exam (and after "Check answer" in Practice mode).

**K2 – A + D.** Multi-select answers list every correct letter, separated by `,` `+` or `&`. They're scored all-or-nothing.
```

Rules the parser relies on:
- **IDs:** question IDs are 1–3 capital letters plus a number (`K1`, `MR12`), written as `**K1.**`. The letters must be **unique across the track**; `A`–`D` are already used by Sets A–D.
- **Options:** list items `- A.` to `- F.`.
- **Answers:** `**K1 – C.**` (an en dash, a hyphen, or just a space all work) followed by the reasoning. A table row `| K1 | C |` also works as a fallback.
- **Multi-select:** more than one answer letter makes the question multi-select; the UI asks for exactly that many.
- **Markdown:** stems and reasoning support `code`, **bold**, *italic*, bullet lists and fenced code blocks. Long case-study stems work best in split view.

## Prompt to generate a new set with Claude
```
Read claude-architect-exam-prep/01-full-study-notes.md (the CCAR notes, courses C1–C10),
the updated <Foundations|Professional> exam guide published on 17 December 2026,
and quiz-site/FORMAT.md. Write a new practice set in that exact format as
claude-architect-exam-prep/quiz-site/sets/<foundations|professional>/set-<ID>.md:
- <N> questions, minutes: <M>, IDs <ID>1–<ID><N> (ID letters unused in this track)
- "## C<n> <course name>" headings, weighting courses as the updated exam guide does
- 8–10 items tagged #core that re-test the most important must-remember facts
- 3–4 "(Choose TWO)" items with 5 options, 2+ NOT stems, at least one ordering item
- scenario stems with plausible distractors; balance correct letters across A–D
- every answer gets 1–3 sentences of reasoning saying why the distractors are wrong
- use only facts from the notes and the exam guide; don't invent numbers
Then run: python3 quiz-site/build_static.py --out _site && node quiz-site/validate.js _site/sets.json
and remove the matching entry from "placeholders" in quiz.config.json.
```
