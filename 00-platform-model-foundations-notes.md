# C3: Claude Platform & Model Foundations (foundational module): Study Notes

<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/01-full-study-notes|Full study notes]] ➡️
<!-- nav:end -->


The foundations module of the Claude Architect path (Skilljar course "Claude Platform & Model Foundations", the SCORM file `Associate_M1_vF2.html`, labelled "Associate path, Module 1: Product & Model Selection"). Every later course assumes you can make its four decisions without looking them up. The course frames them at the claude.ai level (Chat, Projects, Skills, Memory). Courses C4 and C8 restate the model choice at the API and Claude Code level.

Extracted 2026-11-03. Every panel rendered: the flip cards, the tab panels, the checkpoint buckets, the exercise cards, the "Reveal model answer" text and the quiz rationales. Answer keys were read from the page script.

Layout per section (same as `01-full-study-notes.md`):
- **MUST REMEMBER**: facts that exam questions are built on
- **SYNTAX**: exact names and shapes (this module is product-level, so there is little code)
- **DEBUG PRIORITY**: what to check first when this area fails
- **TRADE-OFFS & FIXES**: the cost of each option, plus the fix for each failure

The four decisions that set the **quality ceiling** of every session:
1. **Entry point**: Chat, Project, Artifact or Research
2. **Capability layer**: Projects, Skills, Code Execution, Memory
3. **Model**: Haiku, Sonnet or Opus
4. **Context management**: restart, summarize or persist

---

## 3.1 Five behavioral properties (flip cards)

**MUST REMEMBER**

| # | Property | What it means for a workflow |
|---|---|---|
| 1 | **Responses vary** | Output is generated from probabilities, not retrieved from a fixed store. Two runs give two different answers, so build review into the process. |
| 2 | **A confident tone is not a sign of accuracy** | A made-up statistic reads exactly as fluently as a checked one. Verification is a habit you build, not a signal you read. |
| 3 | **Context is a budget** | Near the limit, claude.ai **auto-summarizes earlier messages** (paid plans with Code Execution enabled). Summaries compress detail, so instructions given early lose force late in a long session. |
| 4 | **Knowledge has a training boundary** | After the cutoff, connect a source, turn on web search, or use Research. |
| 5 | **Configured procedures still vary** | A Skill **reduces** variance but **doesn't eliminate** it. Review stays in the workflow. |

**Distractor alert**: "a Skill guarantees identical output" ✗ · "a confident answer can skip review" ✗

---

## 3.2 Entry points: Chat, Projects, Artifacts, Research

**MUST REMEMBER**
- **Chat**: the default, unstructured entry point. It **is saved to history** and can be continued; Memory and past-chat search can carry some context forward. What it lacks is a Project's **standing instructions** and **curated knowledge base**. Use it for one-off tasks.
  - The sign that a workstream has outgrown Chat: you paste the same background paragraph every week.
- **Project**: a persistent workspace holding three things:
  1. **Standing instructions**: what Claude should know and do in every conversation in the Project
  2. **Knowledge base**: documents uploaded once, available every session
  3. **Its own conversation list**: conversations share the Project's instructions and knowledge base but **do not share context with each other**
- **Artifact**: the **output format** for a deliverable (draft documents, tables, reports, code). It appears as a separate editable block beside the chat. Answers you act on inside the conversation stay inline.
- **Research**: deep, multi-step, **multi-source synthesis** (paid plans).
  - **Web search** is a per-chat toggle available on all plans. On **Team/Enterprise**, an **Owner or Primary Owner** must first enable web search for the workspace in the organization's capability settings. The docs don't say whether the toggle starts on or off. *(Confirm at build time.)*

| Task | Entry point |
|---|---|
| One-off question or quick task | **Chat** |
| Recurring work, stable context | **Project** |
| Output is a deliverable someone will open | **Artifact** |
| Deep multi-source investigation | **Research** (a quick current lookup is **web search in Chat**) |

**The "is a Project worth building?" test**: (1) Does the task recur? (2) Is the background stable? (3) Is the output format consistent? **Two or more yes answers means build it.** The setup time pays back within **2–3 sessions**.

**Worked example**: a weekly status report took 40 minutes in Chat, 12 of them spent loading context. In a Project it took 25 minutes at the same quality. The entry-point decision removed the "setup tax", not a quality problem.

**DEBUG PRIORITY**: if every session starts with re-explaining background, **check the entry point** (Chat used for recurring work) before touching the prompt or the model.

**TRADE-OFFS & FIXES**
- A Project costs setup time and upkeep of the knowledge base. Chat costs re-entry time on every session.
- Research costs time and plan access. Web search in Chat is enough for a quick current fact.
- Distractors: "conversations inside one Project share context with each other" ✗ (they share instructions and knowledge base only) · "Chat isn't saved" ✗

---

## 3.3 The capability layer (four-layer model)

**MUST REMEMBER**

| Layer | Solves | Holds |
|---|---|---|
| **Projects** | Context | Background knowledge and standing instructions for a workstream |
| **Skills** | Procedure | How a task is executed, consistently |
| **Code Execution** | Verified computation | Results that must be **correct**, not just plausible |
| **Memory** | Continuity | Facts carried across sessions without re-entry |

- The layers are **independent**. A one-off question needs none of them, and a recurring analytical workflow may need all four.

**Skills**
- Built-in Skills cover **Excel, Word, PowerPoint and PDF**. Custom Skills are added through settings.
- Skills live at the **account level, not inside a Project**. Claude invokes them **automatically** when they're relevant, in any conversation inside or outside a Project.
- They **reduce variance but don't eliminate it**.
- **Trust evaluation**: a Skill can reach whatever Claude can reach in the session. Review a third-party Skill's source and requested permissions before enabling it. Anthropic-provided and org-approved Skills are the lower-risk starting point.

**Code Execution**
- A sandbox where **Claude writes and runs the code**; you don't write it.
- Prose generation produces *plausible* numbers. Running code produces a *verified* result.
- Use it whenever:
  - a number will be used or reported;
  - data needs transforming or cleaning (date normalization, deduplication, field formatting);
  - the output is a chart;
  - the output is a **real downloadable file** (.xlsx, .pptx, .docx, .pdf).

**DEBUG PRIORITY**
- Wrong figures in a report → **check whether the numbers came from prose generation**. The fix is Code Execution, not a better prompt or a bigger model.
- Inconsistent report formatting week to week → a **Skill** (procedure), plus review.

**TRADE-OFFS & FIXES**: in the course scenario, a monthly regulatory report went from **65 to 30 minutes** after moving to Project + knowledge base + Skill + Code Execution, and **the verification step still ran**. The layers save time; they don't remove review.

| Question the analyst asked | Layer it pointed to |
|---|---|
| Which parts are the same every time? | Standing instructions + Skill |
| Which reference material recurs? | Knowledge base |
| What must be computed correctly? | Code Execution |
| What should carry over without re-entry? | Memory |

---

## 3.4 Memory

**MUST REMEMBER**
- Memory holds role context, format preferences, frequent collaborators and standing constraints.
- **Curate it**: review at least **monthly** for active users, delete or update stale entries, and keep only what genuinely recurs. A stale memory is **actively misleading**. Accuracy matters more than volume.
- **Project-scoped Memory** keeps Memory separate per Project, so Client A's context doesn't appear in Client B's sessions. Separate Projects per workstream; Memory follows the same boundaries.
- **Incognito** keeps a session out of Memory **and** chat history (standalone chats, outside Projects). It **does not override the organization's data retention**.
- **Memory import** from other AI platforms is **experimental as of June 2026**. It's documented for Free, Pro, Max and Team, **not Enterprise**. The fallback is to add key facts to Memory manually, **not** to put them in a Project knowledge base. *(Confirm at build time.)*

**DEBUG PRIORITY**: one client's details appearing in another client's work → **check Memory scoping** (separate Projects with Project-scoped Memory).

**TRADE-OFFS & FIXES**
- Incognito for every session would also lose the continuity you want. Separate Projects solve the separation problem.
- Clearing Memory by hand before every client switch is error-prone and fixes nothing structurally.

---

## 3.5 Checkpoint answers (contract-review buckets)

| Component | Layer | Why |
|---|---|---|
| "Flag any clause that departs from the playbook; explain in one sentence" | **Standing instructions** | A behavioral directive |
| Procedure that extracts flagged clauses into the standard review template | **Skill** | Repeatable output procedure |
| The standard contract playbook | **Knowledge base** | Stable reference |
| Financial exposure from a variable-rate penalty clause | **Code Execution** | A number that must be right |
| This cycle's contract documents, uploaded each session | **Knowledge base** | Reference material Claude reads |

**The test**: is this telling Claude **what to do** (instructions) or **what to know** (knowledge base)?

---

## 3.6 Choosing models (Haiku / Sonnet / Opus)

**MUST REMEMBER**

| Profile | Model |
|---|---|
| Routine, structured extraction or classification **at volume** | **Haiku** (fastest, most efficient; speed compounds at volume) |
| Most professional drafting, synthesis and analysis | **Sonnet** (the balanced tier and the starting point) |
| Complex judgment, high stakes, ambiguous or multi-layered input, client-facing deliverables | **Opus** (quality ranks above speed) |

- Start on **Sonnet**. Move **up** to Opus when quality falls short on complex work. Move **down** to Haiku when the task is structured and speed or volume dominate.
- On **metered or API plans**, the speed/capability trade-off is also a **per-call cost** trade-off: Opus uses more per call. On a claude.ai subscription, treat speed and usage headroom as the stand-in for cost.
- The model picker lineup, the default model and auto-switching vary by plan and over time.
- The course notes a fourth tier above Opus (**Claude Fable**, generally available from 2026-06-09). The **certification uses the three-tier Haiku/Sonnet/Opus frame**, and the course marks the fourth tier "not exam-relevant". *(Confirm the model lineup at build time.)*

**DEBUG PRIORITY**: if a session degrades over time, **don't reach for a bigger model**. Model tier doesn't fix context exhaustion (see 3.7).

**TRADE-OFFS & FIXES**
- Opus buys depth at the cost of speed (and per-call cost on metered plans).
- Haiku under-resources nuanced interpretation.
- Model answer for the 15-page board analysis (exercise S3): **Opus**. Interpreting ambiguous signals across four sources makes the quality ceiling matter more than turnaround. Sonnet fits if the same work were routine or time-critical.

---

## 3.7 Context management, conversation hygiene, usage limits

**MUST REMEMBER**
- As the window fills, claude.ai **auto-summarizes** earlier messages (paid plans with Code Execution enabled). The full history remains available for reference, but detail compresses, so instructions from minute 10 may not hold at minute 90.
- **Signs that a session needs intervention**:
  - Claude stops following instructions it followed earlier;
  - replies address only the latest exchange;
  - accuracy drops in ways consistent with missing early context.
- **Three responses**:
  - **Restart**: open a new conversation. Project instructions and knowledge base carry over; the thread doesn't. Use it when the session has drifted beyond recovery or a genuinely new task starts.
  - **Summarize**: ask for a summary of decisions, work in progress and open questions, then paste it into a new conversation.
  - **Persist**: save to Memory or update the Project knowledge base, for facts every future session needs.
- **Usage limits**: a short **rolling session window** plus **weekly limits** on paid plans across models, with a **separate weekly pool for the highest tier**. These vary by plan. *(Confirm at build time.)* For intensive work, split tasks into segments, save interim progress to the knowledge base, and restart from a summary.

**DEBUG PRIORITY**: in a two-hour session where the framework stopped being followed, the answer is **a new conversation seeded with a summary**.

**TRADE-OFFS & FIXES**
- **Repeating the instructions** in the degraded thread ✗ (it extends a degraded session).
- **Switching to Opus** ✗ (doesn't address context exhaustion).
- **Turning on Research** ✗ (unrelated).

---

## 3.8 Exercise answers (six scenarios → configuration cards)

| Card | Configuration |
|---|---|
| A | Project + Skill · Sonnet |
| B | Research · Sonnet |
| C | Code Execution · Haiku or Sonnet |
| D | Project (knowledge base) + Artifact · Opus |
| E | Chat + Artifact · Sonnet |
| F | Project + Code Execution + Skill · Sonnet |

| Scenario | Card | Signal |
|---|---|---|
| S1 Competitor launches in the last 90 days | **B** | Current information beyond the training data |
| S2 Weekly meeting notes, same template for 6 months | **A** | Recurring, stable, fixed format |
| S3 15-page board analysis from 4 reports, ambiguous | **D** | Nuanced, multi-source, high stakes |
| S4 800 survey responses, rates by department, flag < 60% | **C** | Calculation that must be accurate |
| S5 Monthly variance analysis, flag > 10%, standard template | **F** | Recurring + verified numbers + format |
| S6 Quick one-off reply on vendor payment terms | **E** | One-off draft, no capability layer |

## 3.9 Module quiz answers

| Q | Scenario | Answer |
|---|---|---|
| Q1 | Weekly inventory reconciliation against an unchanged threshold doc | **B**: Project + threshold doc in the knowledge base + format instructions + Code Execution |
| Q2 | Compound interest with five variables | **C**: Code Execution |
| Q3 | 500 vendor agreements with a clear rubric | **C**: Haiku (Opus only if the rubric needed nuanced judgment) |
| Q4 | Two-hour session drifting | **C**: new conversation plus a summary (B extends the degraded thread; A doesn't fix context) |
| Q5 | Keep Client A and Client B separate | **C**: separate Projects with Project-scoped Memory |

## 3.10 Recap: five takeaways
1. Choose the entry point **before** writing the prompt.
2. Four layers solve four different problems.
3. Model tiers are a speed/capability trade-off.
4. Context is a budget: restart, summarize or persist.
5. Variation is inherent, so review is built into the structure.

---

## Commute block (30-second read)

- **Four decisions**: entry point · capability layer · model · context.
- **Chat** for one-off · **Project** when 2 of 3 hold (recurs, stable context, same format) · **Artifact** for a deliverable · **Research** for deep multi-source work (web search for a quick lookup).
- **Instructions = what to do; knowledge base = what to know.**
- **Skill** = procedure (account level, auto-invoked, still varies) · **Code Execution** = numbers that must be right · **Memory** = continuity (curate monthly; Project-scoped for client separation; Incognito doesn't override org retention).
- **Haiku** = structured volume · **Sonnet** = default · **Opus** = ambiguity and high stakes.
- **Drift in a long session** → new chat + summary. Not a bigger model, not repeating instructions.

---

## Mini quiz (10 questions)

**F1.** A team pastes the same client background into a new Chat every Monday for a recurring report. What is the first change?
A. Switch to Opus · B. Build a Project with that background in the knowledge base and standing instructions · C. Turn on Research · D. Save each output as an Artifact

**F2.** Which statement about Skills is accurate?
A. They live inside one Project and only run there · B. They guarantee identical output on every run · C. They live at the account level, are invoked automatically when relevant, and reduce but don't eliminate variance · D. They replace the need for review

**F3.** A quarterly forecast table built in Chat contains two wrong totals. What is the targeted fix?
A. Add "double-check your math" to the prompt · B. Use Opus · C. Put the figures in the knowledge base · D. Use Code Execution for the calculations

**F4.** "Flag any clause that departs from the playbook" belongs in which layer?
A. Standing instructions · B. Knowledge base · C. Code Execution · D. Memory

**F5.** Which is the best signal that a workflow belongs in a Project?
A. The task recurs and its background is stable · B. The task needs current web data · C. The output is a one-off email · D. The task involves a calculation

**F6.** A consultant must keep two clients' context apart. What is the course's configuration?
A. Incognito for every session · B. Clear Memory manually before each switch · C. Separate Projects with Project-scoped Memory · D. A different model per client

**F7.** In a 2-hour session, Claude stops applying the framework set at the start. What is the best response?
A. Repeat the framework in the same thread · B. Switch to Opus · C. Enable Research · D. Start a new conversation seeded with a summary of decisions and open questions

**F8.** 500 standard agreements must be classified low/medium/high against an unambiguous rubric in one session. Which model?
A. Haiku · B. Opus · C. Sonnet, always · D. Whichever is the plan default

**F9.** Memory import from another AI platform isn't available on the account. What is the documented fallback?
A. Upload the facts to a Project knowledge base · B. Add the key facts to Memory manually in memory settings · C. Use Incognito · D. Paste them into every Chat

**F10.** Which statement about Incognito is accurate?
A. It overrides the organization's data retention · B. It works inside Projects · C. It keeps a standalone chat out of Memory and chat history but doesn't override org retention · D. It disables Code Execution

**Answers**
- **F1 B.** The recurring background goes into a Project once. A (bigger model) doesn't remove the setup tax.
- **F2 C.** Skills are account-level and auto-invoked; they still vary, so review stays. A is the most common distractor.
- **F3 D.** Prose produces plausible numbers; Code Execution produces verified ones. A asks the same prose generator to check itself.
- **F4 A.** It's a behavioral directive (what to do), not reference material (what to know).
- **F5 A.** Recurrence plus stable context are two of the three Project criteria. D points to Code Execution, not a Project.
- **F6 C.** Project-scoped Memory follows Project boundaries. B is manual and error-prone; A loses wanted continuity.
- **F7 D.** Context degradation is fixed by restarting from a summary. A extends the degraded thread; B doesn't fix context.
- **F8 A.** Structured, high-volume, clear rubric is Haiku's profile. B fits only if nuanced judgment were needed.
- **F9 B.** The documented fallback is Memory itself, not a Project knowledge base (A).
- **F10 C.** Incognito applies to standalone chats and doesn't change org retention (A is the trap).

---
<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/01-full-study-notes|Full study notes]] ➡️
<!-- nav:end -->
