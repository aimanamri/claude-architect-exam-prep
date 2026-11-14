# Claude Certified Architect – Foundations: Full Study Notes

<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/00-platform-model-foundations-notes|Foundations notes]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/02-commute-recall|Commute recall]] ➡️
<!-- nav:end -->


Source: the ten courses on the Skilljar **Claude Architect** learning path (`/path/claude-architect/`), extracted 2026-11-03. The certification page says the exam tests foundational trade-off decisions across **Claude Code, the Claude Agent SDK, the Claude API and MCP**.

| # | Course | Format | Focus |
|---|---|---|---|
| **C1** | AI Capabilities and Limitations | 14 lessons, video + text | Four machine properties and how they collide |
| **C2** | AI Fluency for Builders | 9 lessons, video + text | The 4D Framework applied to building products |
| **C3** | Claude Platform & Model Foundations (**foundational**, see `00-…`) | 1 SCORM module | Entry point, capability layer, model, context |
| **C4** | Claude Platform 101 | 13 lessons, video + full articles | Messages API, agent loop, tools, thinking, skills, MCP, managed agents |
| **C5** | Claude Code 101 | 12 lessons, video + text | Loop, permissions, workflow, context, CLAUDE.md, subagents, MCP, hooks |
| **C6** | Introduction to Model Context Protocol | 12 lessons, written summaries | Building MCP servers and clients in Python |
| **C7** | Introduction to subagents | 4 lessons, video + text | Creating, designing and choosing subagents |
| **C8** | Product Foundations | 3 interactive lessons | What Claude Code is, model selection, the seven platform paths |
| **C9** | Deployment Architecture | 5 interactive lessons + simulations | Path decision, parity gaps, proxy, LLM gateway, ZDR and residency |
| **C10** | Delivery Methodology | 7 interactive lessons + simulations | Qualification, pilot design, ROI, adoption curve, champions, 30-day activation |

Each section uses the same layout:
- **MUST REMEMBER**: facts that exam questions are built on
- **SYNTAX**: exact names, fields, files, headers and code shapes (only where the course has them)
- **DEBUG PRIORITY**: what to check first when this area fails
- **TRADE-OFFS & FIXES**: the cost of each option, plus the fix for each failure

> Two ideas repeat across the whole path. **Technically:** put the right thing in the right layer (prompt vs Skill vs hook vs tool vs MCP vs subagent; proxy vs gateway; Enterprise vs cloud path). **In delivery:** decide and measure *before* Day 1 (path, gaps, baseline, champion). Most exam scenarios ask which layer or which pre-work was missing.

### Panels that didn't render or weren't captured
- **C1, C2, C4, C5, C7**: lesson **videos were not transcribed**; the written lesson text was captured in full. C4's articles mirror the videos.
- **C6**: every lesson's video player showed *"This video is still being processed … Something went wrong"*. The written summaries were captured.
- **C1**: the "lock in your guess" continuum widgets: the typical placement for each warm-up question shows only after you commit a guess, so it wasn't captured. The widget's enables / fails / product-feature lists were recovered from the page script.
- **C4** "What is tool use?": two example response payloads were images or embeds with no text.
- **C5** "Skills" lesson: only a pointer to a separate *Introduction to agent skills* course, which isn't on this path.
- **End-of-course quizzes** (C1 13 questions, C2, C4, C5, and the C6 final assessment) were **not attempted**. They record graded attempts, and you chose to skip them.

### API syntax status
Course code was checked against the `claude-api` skill (cached 2026-10-06). Where the course shape has since changed, the note says so, and the current shape is in **API drift** at the end of this file. **Confirm every model ID, tool `type` string, beta header and price at build time.**

---

# MODULE C1: AI Capabilities and Limitations

## C1.1 Generative AI and the four properties

**MUST REMEMBER**
- Most AI in daily use (spam filters, recommendations, fraud detection) **classifies or predicts**. This course covers **generative**, transformer-based text models that produce new content **one token at a time**.
- The **4D Framework** (C2) describes the **human** competencies. This course describes the **machine** properties those competencies respond to: two halves of one system.
- Four properties, each a **continuum** from capability to limitation. The same mechanism produces both ends. The further right a task sits, the more you verify and compensate.

| Property | Question | Capability end | Limitation end |
|---|---|---|---|
| **Next Token Prediction** | Where do answers come from? | Well-worn paths: summarize, reformat, explain common concepts | Novel or sparse territory; "true vs sounds true" |
| **Knowledge** | What does it actually know? | Frequent, recent-in-training, consistent topics | Rare, post-cutoff, niche, local, contested |
| **Working Memory** | What is it attending to now? | Material fits; session current; you supply context | Very long documents or conversations; expecting cross-session continuity (**the cliff**) |
| **Steerability** | How much am I in control? | Short, concrete, verifiable instructions ("as a table", "under 100 words") | Long reasoning chains, abstract asks, native numeric precision |

- **Calibrated trust** means locating the task on each continuum, not trusting or distrusting AI wholesale.
- The properties stay stable as models improve; only the boundaries move. That's why the material is durable.

**DEBUG PRIORITY**: when an output disappoints, **name the property first**. It points to the fix.

## C1.2 How AI gets its character (training)

**MUST REMEMBER**
- **Pretraining** teaches next-token prediction over vast text and produces a **document completer** with no concept of helping.
- **Fine-tuning** on human preferences produces the **assistant**: it treats input as a request, answers helpfully and declines harmful asks (helpful, honest, harmless).
- Fine-tuning leaves four **fingerprints**: **sycophancy**, a **verbosity** default, occasional **over-caution**, and **loose calibration** between stated confidence and actual reliability.

**TRADE-OFFS & FIXES**
- Sycophancy → explicitly invite disagreement ("tell me if I'm wrong").
- Verbosity → state the length ("answer in one sentence").
- Over-caution → judge whether the hedging is proportionate to the real risk.

## C1.3 Next Token Prediction

**MUST REMEMBER**
- It works like autocomplete at scale rather than a search engine. The same mechanism gives **fluency and hallucination**.
- Failure modes:
  - **Hallucination**: the plausible continuation isn't the true one.
  - **Confabulation**: it fills gaps with plausible material instead of flagging them.
  - **Inconsistency**: sampling means the same prompt can give different outputs.
  - **Misplaced confidence**: smooth prose can wrap a guess.
- **Fabrication concentrates in specifics**: names, dates, statistics, citations, URLs, quotes. The more precise the claim, the more it needs verifying.
- Product mitigations: **citations and source grounding**, **uncertainty signaling**, **constrained generation / Skills**, **generator–verifier loops**.
- 4D link: Next Token Prediction is the foundation of **Discernment**.

**Sampling (from the "Text Your Friend Markov" interactive)**
- A frequency table of word transitions, normalized per row, gives a probability distribution. Choosing the next word from it is called **sampling**, and LLMs use the same term.
- **Temperature** sharpens (low) or flattens (high) the distribution. **Top-k** keeps only the *k* most likely tokens. **Top-p** keeps the smallest set whose probabilities sum to *p*, so it adapts to how confident the model is.
- A Markov chain reads only the last word. An LLM reads the whole context through a forward pass of billions of parameters. Both output a distribution and **sample the same way**; training is what differs.
- History: Markov (1906) → phone n-gram prediction (~2010) → RNNs (~2015) → transformers (2017).
- *API note:* the newest Claude models reject non-default `temperature`/`top_p`/`top_k` with a 400. *(Confirm per model at build time; see API drift.)*

## C1.4 Knowledge

**MUST REMEMBER**
- The model knows only what it was trained on, frozen at the **knowledge cutoff**, with no real-time browsing by default. The question to ask is *"how well-represented was this in what it read?"*
- Failure modes: **knowledge cutoff**, **staleness**, **uneven coverage**, **inherited bias** (what counts as "default"), **source amnesia** (it can't say where a fact came from).
- Fixes: **web search**, **retrieval (RAG) / MCP**, **tool use** (calculators, databases, APIs), **explicit cutoff disclosure**.
- 4D link: knowing where coverage is uneven drives **Delegation**.

**Embeddings (from the "Visualizing 1024D Space" interactive)**
- Text becomes a **fixed-length vector**: 1,024 values in the demo (VoyageAI embeddings), whatever the input length. One chunk of text is one point.
- Similar meanings land near each other. Retrieval plots the query in the same space and returns the **nearest k**.
- The axes **emerge from training and are unlabeled**; nobody chooses them, and you can't name dimension 847.
- **Cosine similarity** compares vector **direction**, not distance: −1 opposite, 0 unrelated, 1 identical.

## C1.5 Working Memory

**MUST REMEMBER**
- The **context window** is a fixed-size workspace. The model attends only to what's inside it.
- This property has a **cliff, not a gradient**. **Silent truncation** is the characteristic failure, and you aren't always warned.
- Other failures: **lost in the middle**; **no persistent memory by default**; **no learning from your corrections** (corrections change the context, not the model).
- Fixes: **Memory**, **compaction / summarization**, **Projects / workspaces**, **Skills** (load content only when needed), **larger windows**, multi-agent workflows.
- 4D link: Working Memory is what **Description** acts on.
- **Lost in the Middle** (Liu et al., 2023): accuracy dropped **30%+** when the key fact sat in the middle of a long context. It's structural: attention weights the edges more (primacy and recency, a U-shaped curve).
- *Precision note:* the "silent truncation" framing is this course's general model. On the Claude API an oversized request fails with an error, claude.ai auto-summarizes, and Claude Code compacts. See C3, C4.10 and C5.6.

**TRADE-OFFS & FIXES**
- **Front-load** important material, **chunk** long work, **re-supply** critical context.
- Put key instructions **at the start and repeat them near the end**.
- More context isn't better context: **curate, place deliberately, repeat what matters**.

## C1.6 Steerability

**MUST REMEMBER**
- The model follows instructions by **continuing a pattern** (fine-tuning taught it to follow instructions). It matches patterns; it doesn't understand intent. There's always a gap between the words and the intent.
- Failure modes:
  - **Reasoning drift**: small errors compound over long chains.
  - **Letter over spirit**: the instruction is satisfied literally while the intent is missed.
  - **Prompt injection**: instructions inside documents can get followed too.
- Fixes: **system prompts / custom instructions**, **code execution** for math, **visible reasoning** (catch drift at step 2), **structured output modes**.
- When an instruction is followed literally but uselessly, **restate the goal**. Repeating the instruction more forcefully doesn't close the gap.
  - "Make it shorter" really meant "surface the ask for a skimmer".
  - "More professional" meant "reframe for another audience".
  - "Add detail" meant "expand only what drives the decision".

**DEBUG PRIORITY**: a multi-step answer that is wrong at the end → **look for an early error** and add a checkpoint after step 2.

## C1.7 When properties collide (diagnostic pairs)

**MUST REMEMBER**: most real failures are **two properties meeting**. Name the pair and you know the fix.

| Pair | Failure | Fix |
|---|---|---|
| Next Token Prediction + Knowledge | **Hallucinated citations** | Verify specifics independently, or ground in real sources |
| Working Memory + Steerability | **Long-conversation drift** (later messages override early constraints) | Re-supply critical context, or start fresh with the essentials up front |
| Next Token Prediction + Steerability | **Confidently wrong reasoning** | Visible reasoning to catch drift early, or move precise steps to code execution |
| Next Token Prediction + Working Memory | **Context-poisoned generation** (fluent output built on bad context) | Curate the context; bad input gives confident bad output |
| Knowledge + Steerability | **Agreeable bad premises** | Invite pushback: "Tell me if my assumption is wrong" |
| Knowledge + Working Memory | **Stale context vs trained knowledge** (it blends both) | State priority: "Use only the attached document" or "Use your training" |

- The course names two pairs explicitly (Next Token Prediction + Knowledge, Working Memory + Steerability). The other four come from the interactive widget's script.
- The four fixes in short: **verify specifics · re-supply context · offload to code execution · invite pushback**. Diagnosing the pair *is* Discernment.

---

# MODULE C2: AI Fluency for Builders

## C2.1 AI Fluency and the 4D Framework

**MUST REMEMBER**
- **AI Fluency** means working with AI **effectively, efficiently, ethically and safely**.
- The four Ds:
  - **Delegation**: what AI handles vs what stays with you.
  - **Description**: communicating what you need and how to approach it.
  - **Discernment**: evaluating output before acting on it.
  - **Diligence**: owning the final result whatever AI's role.
- **Inner loop** = **Description + Discernment** (every interaction). **Outer loop** = **Delegation + Diligence** (bigger decisions about when and how to use AI).
- "**Delegating implementation is usually safe. Delegating judgment is usually not.**"
- Most AI failures trace back to an earlier failure of description, discernment or diligence.
- The 4Ds are **dynamic, not a sequence**.
- The **builder brief** is a reusable context document: what you're building and for whom, your role, your constraints (team, stack, timelines, non-negotiables), and where AI is and isn't involved.

## C2.2 AI capabilities for builders

**MUST REMEMBER**
- Three things made modern LLMs possible: the **transformer architecture**, **vast training data** and **massive compute**.
- Two training stages: pre-training, then fine-tuning.
- Strengths: **versatility, conversational fluency, tool use**. Limits: **knowledge cutoffs, hallucinations, unreliable complex reasoning**.
- The **hallucination test** for builders: AI-recommended libraries, packages and documentation must be checked. Does it exist? Is the API accurate? Is the version current?

## C2.3 Delegation and the builder's toolkit

**MUST REMEMBER**

| Stage | AI strength | Note |
|---|---|---|
| Empathy | **Weak** | It can surface data and personas, but it can't feel the gap |
| Design | Moderate | Fast patterns; you supply taste and context |
| Architecture | Moderate | Knows common patterns; your constraints are yours to specify |
| **Implementation** | **Strong** | Delegate freely |
| **Judgment** | **Weak** | Can list options; can't own the call |
| Shipping | Moderate | Automates steps; responsibility stays yours |

- AI is **strongest in the middle** (implementation). Keep **empathy, judgment and shipping** in your hands.
- Three collaboration modes:
  - **Automation**: AI does it, you check.
  - **Augmentation**: you and AI work it together.
  - **Agency**: AI acts with latitude inside boundaries you set.
- **Write acceptance tests before code**: a shared definition of done. Each test must be concrete enough that a stranger can mark pass or fail ("a patient with a basic smartphone finds the wait time in under 30 s without an account", not "easy to use").
- As implementation gets cheap, the builder's value moves to **framing problems and raising the bar**.

## C2.4 Description: the Description Chain

**MUST REMEMBER**
- **User voice → requirement → technical spec → AI instruction → tests.** Prompt engineering is just one link, and the builder translates at every step. **AI can't hear what the user didn't say.**
- **Code that works but a product that doesn't is a description failure.** Find the upstream link that broke.
- **Tests are the most precise form of description.** A passing test with an unhappy user means the wrong intent was described.
- Every adjective in a requirement is a decision ("fast" → how fast). Add edge cases: closed clinic, no data, zero wait.

**DEBUG PRIORITY**: tests pass but users are unhappy → **trace back up the chain**. Don't keep re-prompting the code.

## C2.5 Discernment for code: five lenses

| Lens | Question | Typical AI failure |
|---|---|---|
| 1 **Functional integrity** | Does it work? | Passes unit tests, breaks on real data the prompt never covered |
| 2 **Production readiness** | Does it work well? | Smooth in dev, broken under load, races with concurrent users |
| 3 **Problem fit** | Is it the right thing? | Meets the literal spec, misses the need |
| 4 **Experience quality** | Is it good? | Generic, uninvested UI |
| 5 **Responsible impact** | Is it responsible? | Generated content presented as authoritative; a demographic left out by default |

- Lens 1 is easy to test. By lens 5 you're making judgment calls AI can't make.
- AI's predictable blind spots: **concurrency, security, anything that only breaks at scale**. Taste is a builder skill.

## C2.6 Discernment for UX: four principles

**MUST REMEMBER**
- **Clarity**: every element states its purpose. Example: "Place Order — $16.50", not "Submit"; currency symbols; labelled navigation.
- **Hierarchy**: visual weight matches priority (order total and arrival time stand out).
- **Accessibility**: about **1 in 5 people has a disability**. AI designs for the median user. Watch for color-only status, 9 px text, abbreviations ("qty") and jargon ("ETA", "T&C").
- **Feedback**: errors say what happened, what to do next and how to get help. Never a raw "Error 503".
- "**Make it look good** is a wish, not a spec." AI doesn't get accessibility right by default: **specify it, then audit**. A critique you'd give a colleague and a description AI can execute are different artifacts; learn to translate.

## C2.7 Diligence: stand behind what you build

**MUST REMEMBER**
- You own the **outcome, not the output**. "AI wrote it" explains and excuses nothing.
- Shipping vocabulary AI **won't raise unless asked**: **migrations, versioning, rate limits, feature flags**.
- Tests make post-launch iteration safe. **Prototype freely, ship selectively**, and be willing to retire your own work.
- Access is a design decision.
- Pre-ship checklist: understanding · testing (edge cases) · access · responsibility (be open about AI's role) · feedback loop. Then decide: **ship it, fix it, or stop it**.

**TRADE-OFFS & FIXES (C2 overall)**: cheap code creates value only when paired with honest evaluation. The usual fix for weak AI output is **better description upstream** or **a stricter lens**, not more re-prompting.

---
## C1–C2 checkpoint answers
- The end-of-course quizzes for C1 (13 questions) and C2 weren't attempted (you chose to skip them). The one C1 question seen before skipping was "What does the pretraining stage produce?" → **a document completer that predicts what comes next**.
- C1 warm-up placement prompts, for self-check: summarize a long report (Next Token Prediction) · explain last week's news (Knowledge; post-cutoff, so verify carefully or use search) · review a 50-page contract (Working Memory; lost in the middle) · write exactly 100 words (Steerability; native precision, so check).

---

# MODULE C3: Claude Platform & Model Foundations (foundational)

Full notes, the commute block and a 10-question quiz are in **`00-platform-model-foundations-notes.md`**. This is the condensed version.

## C3.1 Behavioral properties
**MUST REMEMBER**: responses vary · a confident tone isn't accuracy · context is a budget (claude.ai auto-summarizes near the limit on paid plans with Code Execution) · training cutoff · Skills reduce variance but don't remove it.

## C3.2 Entry points
**MUST REMEMBER**
- Chat for one-off work. A **Project** when two of three hold (recurs, stable background, consistent format); setup pays back in 2–3 sessions. **Artifact** for a deliverable. **Research** for deep multi-source work (web search for a quick lookup).
- Conversations inside a Project **share instructions and knowledge base, not context**.
- Team/Enterprise web search must be enabled by an **Owner or Primary Owner**.

**DEBUG PRIORITY**: re-explaining background every session → **the entry point is wrong**.

## C3.3 Capability layer
**MUST REMEMBER**
- Projects = context · Skills = procedure (**account level, auto-invoked**) · Code Execution = verified computation (numbers, transforms, charts, real files) · Memory = continuity.
- Standing instructions = **what to do**; knowledge base = **what to know**.
- Third-party Skills need a trust review: a Skill can reach whatever Claude can reach.

**DEBUG PRIORITY**: wrong figures → **were they generated as prose?** Use Code Execution.

## C3.4 Memory
**MUST REMEMBER**
- Curate at least monthly. **Project-scoped Memory** separates clients.
- **Incognito** keeps a standalone chat out of Memory and history but **doesn't override org retention**.
- Memory import is experimental (June 2026), not on Enterprise; the fallback is to add facts to Memory manually. *(Confirm at build time.)*

## C3.5 Models
**MUST REMEMBER**
- Haiku = structured volume · **Sonnet = start here** · Opus = ambiguity, high stakes, client-facing.
- On metered plans, tier choice is a cost choice too.
- The exam uses the **three-tier** frame; the Fable tier is noted as not exam-relevant. *(Confirm the lineup at build time.)*

## C3.6 Context hygiene
**MUST REMEMBER**
- Signs of degradation: earlier instructions ignored; replies only to the latest turn; accuracy drops.
- **Restart / Summarize / Persist.**
- Usage limits: a rolling session window plus weekly limits, with a separate pool for the top tier. *(Confirm at build time.)*

**TRADE-OFFS & FIXES**: drift → **new chat seeded with a summary**. Not a bigger model, not repeating instructions.

## C3 checkpoint answers
- **Contract-review buckets**: playbook-departure rule → standing instructions · clause-extraction procedure → Skill · playbook → knowledge base · penalty exposure → Code Execution · this cycle's contracts → knowledge base.
- **Exercise**: S1 → B (Research) · S2 → A (Project + Skill) · S3 → D (Project + Artifact · Opus; model answer: depth at the cost of speed) · S4 → C (Code Execution) · S5 → F (Project + Code Execution + Skill) · S6 → E (Chat + Artifact).
- **Quiz**: Q1 B · Q2 C · Q3 C (Haiku) · Q4 C (new chat + summary) · Q5 C (separate Projects + Project-scoped Memory).

---

# MODULE C4: Claude Platform 101

## C4.1 What the Claude Platform is

**MUST REMEMBER**
- Anthropic's infrastructure for building with Claude **programmatically**: a **REST API**, **SDKs**, **CLIs**, and the **Console** (API keys, usage, deploying managed agents, testing prompts).
- Three layers:
  - **Primitives**: Messages API, tool use, files, web search, code execution, MCP servers, skills.
  - **Infrastructure**: managed agents, retries, queues, observability.
  - **Controls**: dashboards, evals.
- In short: **"build with primitives, scale on infrastructure, run with control."**
- The point is to go from "ask Claude a question" to "Claude is part of my product", by wiring Claude into an existing feature (for example a "draft reply" button on a help desk).

**SYNTAX: a minimal request (Python)**
```python
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-haiku-4-5",   # a simple drafting task suits Haiku (course example; confirm IDs at build time)
    max_tokens=1024,            # caps the response length
    system=TONE_AND_GUIDELINES, # role, tone and guidelines
    messages=[{"role": "user", "content": ticket_content}],
)
draft = "".join(b.text for b in response.content if b.type == "text")
```

## C4.2 Your first API call

**MUST REMEMBER**
- Get the API key from **platform.claude.com** (credits must be purchased first). Store it in an env file such as **`.env.local`**, never hardcoded or committed.
- Install: `npm install @anthropic-ai/sdk` (TypeScript) or `pip install anthropic` (Python).
- Every call needs **`model`**, **`max_tokens`** and **`messages`** (`user` / `assistant` roles). Add `system` to shape the persona.
- **`response.content` is an array of blocks, not a string.** Blocks can be `text`, `tool_use`, `thinking` and others, so loop over them and check `block.type`.

**SYNTAX (TypeScript)**
```ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();
const response = await client.messages.create({
  model: "claude-opus-4-8",
  max_tokens: 1024,
  system: "You are a terse senior code reviewer. Give feedback in one paragraph.",
  messages: [{ role: "user", content: `Review this code:\n${buggyCode}` }],
});
for (const block of response.content) {
  if (block.type === "text") console.log(block.text);
}
```

**DEBUG PRIORITY**: `TypeError` or odd output when reading the reply → **check for code treating `response.content` as a string**.

## C4.3 Choosing the right model

**MUST REMEMBER**
- Model tiers are chosen with the **`model`** parameter:
  - **Haiku**: fastest, cheapest; classification, extraction, routing.
  - **Sonnet**: balanced; most production work.
  - **Opus**: deep reasoning, complex analysis, multi-step coding, nuanced writing; slowest and costliest of the three core tiers.
  - **Fable**: a newer tier above Opus at significantly higher cost.
- **Build a simple eval before production code**: **20–30 representative examples** from the real workload, scored against what "good" means.
- Run the eval **from Haiku upward** and stop at **the cheapest model whose output you'd actually ship**.
- **`response.usage`** returns input and output tokens, which is what you're billed on.
- **Route per task inside one endpoint**: classify every file with Haiku, draft client updates with Sonnet, write RFP responses with Opus.

**SYNTAX**
```python
for model in ["claude-haiku-4-5", "claude-sonnet-4-6", "claude-opus-4-7"]:
    r = client.messages.create(model=model, max_tokens=300,
                               messages=[{"role": "user", "content": prompt}])
    print(model, r.usage)  # input_tokens / output_tokens
```

**TRADE-OFFS & FIXES**
- Defaulting to the smartest model gives a surprise bill. Defaulting to the cheapest gives output that doesn't hold up.
- The fix is the **eval-driven climb**.
- *Current lineup (claude-api skill, cached 2026-10-06): Haiku 4.5 has a 200K context window, Sonnet 4.6 / Opus 4.7 / 4.8 have 1M; newer IDs exist (`claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-fable-5-1`). Confirm IDs and prices at build time.*

## C4.4 The agent loop

**MUST REMEMBER**
- An **agent** is Claude running both sides of the loop without a human in the middle.
- The loop:
  1. Send messages **with tools**.
  2. Claude replies with a final answer or a tool request.
  3. **Your code** runs the tool.
  4. Send the result back.
  5. Repeat until **`stop_reason == "end_turn"`**.
- "**You own the loop and the tools. Claude owns the reasoning.**"
- The weather demo takes **two API calls and one tool execution**: turn 1 ends with `tool_use`, turn 2 with `end_turn`.
- In production the same loop shape uses real tools, streams results to the UI as **server-sent events**, and persists findings (for example rows in a risk-findings table).

**SYNTAX (manual loop, Python)**
```python
while True:
    response = client.messages.create(model=MODEL, max_tokens=1024,
                                      tools=tools, messages=messages)
    if response.stop_reason == "end_turn":
        print("".join(b.text for b in response.content if b.type == "text"))
        break
    if response.stop_reason == "tool_use":
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,          # ties the result to the call
                    "content": run_tool(block.name, block.input),
                })
        messages.append({"role": "assistant", "content": response.content})  # full content, not just text
        messages.append({"role": "user", "content": tool_results})            # ALL results in ONE user message
        continue
    break  # max_tokens, refusal, pause_turn etc.: handle explicitly in production
```

**DEBUG PRIORITY**
- A loop that never ends, or a 400 about a tool_use with no matching result → **check that every `tool_use` id gets a `tool_result` in the next user message** and that the assistant turn was appended.
- A loop that stops early → **check which `stop_reason` you branch on**.

## C4.5 Tool use

**MUST REMEMBER**
- A tool is a function you define and expose. **Claude decides when to call it; your code executes it.**
- A definition has three parts: **`name`**, **`description`**, **`input_schema`** (JSON Schema), passed as the **`tools`** array.
- **The description is what Claude reads to decide whether to call the tool.** A vague description is the **number one reason agents misfire** or ignore available tools.
- With several tools, Claude picks by matching descriptions to the request ("today's weather" → `get_weather`, "the next few days" → `get_forecast`), sometimes calling both in one turn.
- Adding a tool means adding it to the array **plus** a case in your dispatch.
- The **tool runner** (SDK; TypeScript, Python, Ruby in the course, more languages now) builds schemas from your functions and runs the whole loop. On the spectrum from "you execute" through "you delegate the loop", **managed agents** sit at the far end.

**SYNTAX: tool definition**
```json
{
  "name": "lookup_building_code",
  "description": "Look up a specific building code section by its identifier. Returns the full text of that code section.",
  "input_schema": {
    "type": "object",
    "properties": {
      "section": {"type": "string", "description": "The building code section to look up"}
    },
    "required": ["section"]
  }
}
```

**SYNTAX: tool runner (current SDK shape per the claude-api skill)**
```python
from anthropic import beta_tool

@beta_tool
def get_weather(city: str) -> str:
    """Get today's current weather for a city."""
    return lookup(city)

runner = client.beta.messages.tool_runner(
    model=MODEL, max_tokens=1024, tools=[get_weather],
    messages=[{"role": "user", "content": "Weather in Denver today?"}],
)
final_message = runner.until_done()
```
*The course's TypeScript example passes plain functions to `client.beta.messages.toolRunner(...)`. Per the claude-api skill, TypeScript tools are wrapped with `betaZodTool({...})` from `@anthropic-ai/sdk/helpers/beta/zod`, and the runner is awaited. Confirm at build time.*

**DEBUG PRIORITY**: a tool exists but Claude never calls it, or calls the wrong one → **fix the description first**, before the prompt or the model.

**TRADE-OFFS & FIXES**
- Manual loop: full control, more code, schemas written twice.
- Tool runner: less code; the schema comes from function types and docs.
- Managed agents: no loop at all, but less control.

## C4.6 Extended / adaptive thinking

**MUST REMEMBER**
- Extended thinking lets Claude reason step by step before answering. The reasoning appears as **thinking blocks** in the response.
- From **Opus 4.7** onward thinking is **adaptive**: no token budget; Claude decides when and how much to think.
- Depth is set with **`effort`**, which goes **inside `output_config`**, not next to `thinking`. Levels: `low`, `medium`, `high`, `xhigh`, `max`.
- **Use thinking for**: math and multi-step logic, debugging, regulatory analysis, trade-off comparisons. **Skip it for**: simple classification, extraction, boilerplate (it adds latency and cost for no gain).

**SYNTAX**
```python
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},   # low | medium | high | xhigh | max
    tools=[weather_tool],
    messages=[{"role": "user", "content": "Plan a road trip out of San Francisco with two stops, weighing weather and drive time."}],
)
```
*Drift notes (claude-api skill):*
- `budget_tokens` returns a **400** on Opus 4.7/4.8/5/5.5, Sonnet 5/5.5 and Fable.
- On **Opus 4.7/4.8, omitting `thinking` means no thinking**, so set `{"type": "adaptive"}` explicitly. On Opus 5.5, thinking can't be disabled.
- The default effort is `high` on most models but **`medium` on Opus 5.5 and Haiku 5.5**.
- `display` defaults to `"omitted"` on new models: thinking text is empty unless you set `display: "summarized"`.
- *Confirm at build time.*

**DEBUG PRIORITY**: 400 on a thinking request → **check for `budget_tokens`, or `effort` placed next to `thinking` instead of inside `output_config`**.

## C4.7 Built-in (server and client) tools

**MUST REMEMBER**
- **Server tools** (declared by you, **run by Anthropic**): **web search** (results with citations), **code execution** (Python in a sandbox), **web fetch** (full content of a URL).
  - **No agent loop needed**: the result comes back in the **same response**. You don't switch on `stop_reason` or push results back.
  - New block types: **`server_tool_use`**, plus result blocks such as **`bash_code_execution_tool_result`** (`.content.stdout`) and `web_search_tool_result`.
- **Client tools** (shipped in the SDK, **run where your code runs**): **memory** (read and write across sessions) and **bash** (persistent shell). The SDK supplies the schema and a runner.
- Web-validated still doesn't mean true; keep checking Claude's work.

**SYNTAX**
```python
tools=[{"type": "web_search_20260209", "name": "web_search"}]
tools=[{"type": "code_execution_20260120", "name": "code_execution"}]   # course; current default per skill: code_execution_20260521
tools=[{"type": "web_fetch_20260209", "name": "web_fetch"}]
tools=[{"type": "memory_20250818", "name": "memory"}]                  # client tool; you implement the storage
```
*Per the claude-api skill: the `_20260209` web search and fetch variants have dynamic filtering built in, so don't also declare `code_execution`. Server-tool errors arrive as HTTP 200 with an error object in the result block, not as exceptions. Confirm type strings at build time.*

## C4.8 Skills (API)

**MUST REMEMBER**
- A Skill is a **folder of instructions, scripts and resources** with a **`SKILL.md`** at its core. Upload it once, then attach it to calls by ID.
- **Tools = what Claude can do** (data and actions). **Skills = how you want it done** (a procedure, which may run bundled scripts).
- **Progressive loading**: only the **name and description** load at startup. The full Skill loads when the agent decides it's relevant, which keeps context lean.
- Skills attach through **`container.skills`**, a **list**, so you can layer several. Pair them with **code execution** when the procedure has to do real work.
- Use case: standardize output (every PM's status report gets the same sections, tone and order without anyone pasting a template).

**SYNTAX (course shape)**
```python
skill = client.beta.skills.create(display_title="Status Report Generator",
                                  files=files_from_dir("status-report-skill"))
response = client.beta.messages.create(
    model="claude-sonnet-4-5", max_tokens=4096,
    betas=["skills-2025-10-02", "code-execution-2025-08-25"],
    container={"skills": [{"type": "custom", "skill_id": skill.id, "version": "latest"}]},
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": f"Generate the daily status report from this activity log:\n\n{activity_log}"}],
)
```
*Drift (claude-api skill): the Skills API is **out of beta**. Use `client.skills.*` with **no `skills-2025-10-02` header**. Attaching still uses `client.beta.messages.create` with `container={"skills": [...]}`, the `code_execution_20260521` tool and the `code-execution-2025-08-25` beta. Confirm at build time.*

## C4.9 MCP (API connector)

**MUST REMEMBER**
- MCP exists because of **maintenance**. With custom tools you write **and maintain** a wrapper for Asana, Slack and Google Calendar. With MCP the **service provider maintains the server** and you change nothing when their API changes.
- **Tools** = your own systems (you maintain them) · **Skills** = your procedures · **MCP** = third-party services (the provider maintains them). "**Tools for your stuff, skills for your processes, MCP for everyone else's stuff.**"
- Claude **introspects the server** and discovers its tools; you write no schemas.
- **Scope down** what's exposed: disable everything by default, then enable specific tools. This keeps a server read-only and saves context.

**SYNTAX**
```python
response = client.beta.messages.create(
    model=MODEL, max_tokens=1000,
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[{
        "type": "url",
        "url": "https://mcp.linear.app/mcp",
        "name": "linear",
        "authorization_token": os.environ["LINEAR_MCP_TOKEN"],
    }],
    tools=[{"type": "mcp_toolset", "mcp_server_name": "linear"}],   # REQUIRED: mcp_servers alone is rejected
    messages=[{"role": "user", "content": "What tools do you have available?"}],
)

# read-only scoping
tools=[{
    "type": "mcp_toolset",
    "mcp_server_name": "slack",
    "default_config": {"enabled": False},
    "configs": {"search_messages": {"enabled": True}, "list_channels": {"enabled": True}},
}]
```

**DEBUG PRIORITY**: a validation error with an MCP server → **check that the `mcp_toolset` entry exists, that its `mcp_server_name` matches the server's `name`, and that the beta header is present**.

## C4.10 Context management (API)

**MUST REMEMBER**
- Context is everything Claude sees on a turn: system prompt, history, **tool definitions and results**, attached files and skills, **thinking blocks**. You pay for it on the way in and on the way out. **Once the window is full, the request fails.**
- Four patterns: three API features and one design pattern.
  1. **Just-in-time context**, the **design pattern**: load what's needed now and let tools pull the rest (a `lookup_building_code` tool, not the whole code book in the system prompt).
  2. **Server-side compaction**: the API summarizes old turns into one block once input crosses a trigger threshold.
  3. **Prompt caching**: mark stable parts (system prompt, tools, long documents) and reuse them at a fraction of the cost. A 4,000-token system prompt sent 100 times an hour is the course's example.
  4. **Memory tool**: Claude reads and writes a **memory directory** through tool calls. **You implement the storage backend** client-side (files, a database, an encrypted store). Anthropic auto-injects an instruction to check memory before starting.
- Each pattern answers a different failure: **cost** (caching), **window size** (just-in-time, compaction), **statelessness** (memory). In production you layer them.
- **Managed agents ship with caching and compaction on by default.**

**SYNTAX**
```python
# Course shape
context_management={"edits": [{"type": "compact"}]}

# Current shape per the claude-api skill (confirm at build time)
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model=MODEL, max_tokens=16000, messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
messages.append({"role": "assistant", "content": response.content})  # keep the compaction block
```
- Compaction **summarizes** (default trigger around 150K tokens per the skill). **Context editing** (`clear_tool_uses_20250919`, beta `context-management-2025-06-27`) **clears** old tool results instead. They're different features.
- Prompt caching: `cache_control: {"type": "ephemeral"}` (top-level auto-caching, or per block). Render order is **tools → system → messages**. Any byte change in the prefix invalidates everything after it. Verify with **`usage.cache_read_input_tokens`**.

**DEBUG PRIORITY**
- Compaction "doesn't work" → **check whether only the text was appended**; the compaction block must go back in.
- Cache reads at 0 → **check for a timestamp or varying content in the prefix**, or for a region where caching isn't available (C9).

## C4.11 Managed agents: what they are

**MUST REMEMBER**
- **Claude Managed Agents** is a suite of APIs to build and deploy agents at scale. **Anthropic hosts the agent loop**. Claude works in an **isolated container** with file system access, bash and web search. It has its own section in the Console.
- Building blocks:
  - **Agents**: tools, persona, capabilities.
  - **Sessions**: individual runs fired from your app.
  - **Environments**: sandboxes with packages and network controls.
  - **Tools**: including **custom tools on your backend**.
  - **MCP**, **Memory** (read before, write after), **Outcomes** (rubrics and **graders**), **multi-agent coordination**.
- Patterns from the course examples:
  - **Kanban board**: a ticket fires a session. The environment has Lighthouse and Puppeteer, the repo is mounted, and a **rubric** defines done. A **separate grader in its own context window** checks the output; Claude fixes and resubmits (score 96). **Parallel sessions run in separate containers.**
  - **Recurring research agent**: web search, Python cost analysis, an Excel skill, Slack and Asana via MCP, and a **memory store** so the report shows *changes since last week*.
  - **Incident response**: a coordinator delegates to three specialists, each with **its own context window on a shared file system**. A **permissions policy** holds the Slack post until a **human approves**. Memory spots a recurring DNS/TTL pattern.

## C4.12 Building your first managed agent

**MUST REMEMBER**
- Use managed agents when the loop would run **minutes to hours**, across many tools, with state and files, and must **survive network interruptions**. Use a manual loop when you want full control.
- Managed agents are **enabled by default** for every API account.
- Four primitives, in order:
  - **Agent**: model, system prompt, toolset; **reusable**.
  - **Environment**: cloud or local, networking.
  - **Session**: one run, the **unit of work**.
  - **Events**: everything flowing in and out.
- You **send events and read events** instead of writing a while loop.
- **Open the event stream before sending the kickoff message.** The stream only delivers events that happen after it opens.

**SYNTAX (course shape, matches the claude-api skill; confirm at build time)**
```python
agent = client.beta.agents.create(
    name="Line Counter", model="claude-opus-4-8",
    system="You are a helpful agent that completes small file tasks.",
    tools=[{"type": "agent_toolset_20260401", "default_config": {"enabled": True}}],  # bundled file, bash and web tools
)
environment = client.beta.environments.create(
    name="line-counter-env",
    config={"type": "cloud", "networking": {"type": "unrestricted"}},
)
session = client.beta.sessions.create(agent=agent.id, environment_id=environment.id, title="Count lines demo")

with client.beta.sessions.events.stream(session_id=session.id) as stream:   # 1. open the stream FIRST
    client.beta.sessions.events.send(                                       # 2. then send the kickoff
        session_id=session.id,
        events=[{"type": "user.message",
                 "content": [{"type": "text", "text": "Create a file in the temp directory, count its lines, and report back."}]}],
    )
    for event in stream:
        if event.type == "agent.message":
            print("".join(b.text for b in event.content if b.type == "text"))
        elif event.type == "agent.tool_use":
            print(f"[tool] {event.name}")
        elif event.type == "session.status_idle":
            break
```
- The `managed-agents-2026-04-01` beta header is set by the SDK.
- Per the skill: create agents **once** (or sync them as files with `ant apply`), never in the request path. With `limited` networking, `allowed_hosts` also limits web tools. **Vault credentials** keep secrets out of the sandbox.

**DEBUG PRIORITY**: a session "does nothing" or the first events are missing → **check that the stream was opened before the kickoff `events.send`**.

## C4.13 Building with Claude Code
**MUST REMEMBER**
- Stub the file, ask Claude Code to fill it, and **review the diff**.
- The built-in **Claude API skill** is invoked with **`/claude-api`**, or automatically when the TypeScript SDK is detected. If it's missing, add the marketplace with `/plugin marketplace add AnthropicsSkills` (note the trailing **s**). *(Confirm at build time.)*
- A good prompt names **the file, the pattern and the end state**. Claude Code writes the code, runs it, reads errors and patches in place.
- The usual shape of API code: **define a tool → hand it to a runner → return the result.**

## C4 checkpoint answers
- The course quiz wasn't attempted (you chose to skip it). Self-check questions are built into Practice Sets A–D (C4 items).

---
# MODULE C5: Claude Code 101

## C5.1 What Claude Code is and how it works

**MUST REMEMBER**
- Claude Code is an **agentic coding tool**. It reads the codebase, edits files, runs commands, searches the web and connects to developer tools.
- Surfaces: **terminal, VS Code, JetBrains, Claude Desktop, web**.
- Unlike Claude.ai, it has **direct access to files, terminal and codebase** and does the work itself.
- An **agent** is an LLM running **in a loop in real time** with tools.
- The loop: prompt → gather context (the model returns text or a tool call) → act → **verify** → finish or loop again. You can add context, interrupt or steer at any point.
- When the context limit is reached, Claude Code **compacts** the conversation automatically.
- Three things to keep in mind: the **context window** (it searches agentically rather than loading the whole repo); it **asks permission by default**; it **can make mistakes** (stay in the loop).

## C5.2 Permission modes

| Mode | File edits | Shell commands | Use |
|---|---|---|---|
| **Default / approval** | Asks | Asks | Hands-on control |
| **Auto-accept** | Automatic | **Still asks** | Trusted edits |
| **Plan mode** | None: **read-only tools** | None | Research, then a plan, before any change; safe code review |

- **Shift + Tab** cycles the modes. They're configurable in the settings file.
- Be careful skipping permissions: a mistake becomes harder to catch before it happens.

**Distractor alert**: "auto-accept also runs commands without asking" ✗

## C5.3 Installing and surfaces

**MUST REMEMBER**
- macOS, Linux and WSL install with **curl**. **Homebrew** works but **doesn't auto-update**. Windows uses PowerShell `Invoke-RestMethod` or CMD `curl`; **winget doesn't auto-update**.
- Run **`claude`** in the project directory. It can reach **that directory and all its subfolders**.
- Sign in with a Claude account (Pro, Max or **Enterprise**; pick Enterprise if the org has it) or an API key.
- VS Code: the extension by Anthropic with the blue verified check. JetBrains: the Marketplace plugin. Desktop: the **"Code"** toggle (folder, permissions, cloud environment). Web: **claude.ai/code**, **GitHub repos only**.
- **The terminal gets new features first.** IDEs are nearly identical. Desktop suits background work; the web suits remote work on GitHub repos.

## C5.4 Explore → Plan → Code → Commit

**MUST REMEMBER**
- "If you take one thing away": **Explore, Plan, Code, Commit.** Jumping straight to "write code" means more course-correcting later.
- **Explore and Plan** happen in **plan mode** (it can't edit). It reads files and searches the web. **The cheapest place to course-correct is before any code exists.** The **Explore subagent** can summarize the codebase outside plan mode.
- **Code**:
  - **define success criteria** (what "correct" looks like);
  - **add tools** (for example the Claude in Chrome extension so Claude Code can test the UI in a browser);
  - **include a test suite** as a reliable source of truth (avoid false positives).
  - If the same issue keeps recurring, have Claude **save the fix to CLAUDE.md**.
- **Commit**: test it yourself, run a **subagent code reviewer** (fresh eyes, no bias from the session), then have Claude write the commit message in your style.

**DEBUG PRIORITY**: lots of rework after implementation → **check whether plan mode and explicit success criteria were skipped**.

## C5.5 Context management (Claude Code)

**MUST REMEMBER**
- Prompts, file reads, tool calls and tool results all fill the window. Near the limit, **auto-compaction** summarizes and drops unneeded tool results, and **can lose details**.

| Command | Effect | When |
|---|---|---|
| **`/compact`** | Summarizes so far and keeps a memory of it | Same feature, near the limit |
| **`/clear`** | Wipes everything | **Starting a new feature** (avoid carry-over bias) |
| **`/context`** | Shows size, the biggest categories and a breakdown | Diagnosing what's eating context |

- Facts needed across sessions go into **CLAUDE.md**.
- Saving context:
  - **Be specific.** A vague prompt costs *more* context because Claude has to explore.
  - **Manage MCP servers.** They load **all their tool definitions into context by default**, even unused; turn off unrelated servers.
  - **Skills** don't load everything upfront.
  - **Subagents** use a separate window and return only a summary.

## C5.6 Code review and git workflow

**MUST REMEMBER**
- Review with a **subagent** before a PR (its own context, fresh eyes).
- A **code-reviewer subagent gets read-only tools** (it flags issues, it doesn't edit). **Commit the subagent config to the repo** so the whole team uses the same reviewer.
- **`/commit-push-pr`** commits, pushes and opens the PR in one step. With a Slack MCP server and channels listed in CLAUDE.md, it posts the PR link automatically.
- A PR created via `gh pr create` links to the session. Resume later with **`claude --from-pr <PR_NUMBER>`**.

## C5.7 CLAUDE.md

**MUST REMEMBER**
- Persistent project memory: a Markdown file at the **project root**, **read automatically at the start of every session**, with its contents **appended to your prompt**. Think of it as an onboarding script.
- Typical sections: project and stack, commands (dev, test, lint), code style.
- Commit it to version control. Hierarchy:
  - **project-level** (repo root, shared with the team);
  - **user-level** (your config folder; personal, all projects).
- Tips:
  - Ask Claude to **save repeated corrections** to memory.
  - Reference documents with **`@path`** (e.g. `@README.md`).
  - **Start without a CLAUDE.md** to see where you keep course-correcting, which keeps it short.
  - **`/init`** generates one.

**SYNTAX**
```markdown
# Project
This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`

# Code Style
- Use server actions instead of API routes where possible

## README.md
Please read if you need more info: @README.md
```

**DEBUG PRIORITY**: Claude re-discovers the stack every session or keeps breaking a convention → **check CLAUDE.md** (missing, or never updated with the correction).

## C5.8 Subagents (overview)
**MUST REMEMBER**
- Subagents run **in parallel** with their **own isolated context window** and return a **summary**.
- They're defined as **Markdown files with YAML frontmatter**. Create one with **`/agents` → Create new agent**.
- Options include persistent memory, and **preloading skills** via the `skills` key. Preloaded skills load **in full** into the subagent's context, unlike the main conversation's progressive loading.
- Full detail in C7.

## C5.9 MCP in Claude Code

**MUST REMEMBER**
- Add a server with **`claude mcp add`**. Transport types:
  - **HTTP**: remote, hosted by the provider.
  - **stdio**: a local process.
- **`/mcp`** inside a session shows status and lets you disable servers.

| Scope | Where | Who gets it |
|---|---|---|
| **Local** | Current project | Just you |
| **User** | All your projects | Just you |
| **Project** | **`.mcp.json`** in version control | **Everyone on the codebase** |

- Context cost: server tool definitions sit in context **even when unused**.
  - A **CLI equivalent** (`gh`, `aws`) is more context-efficient: no persistent definitions.
  - A **Skill** loads only its name and description until needed.
- If MCP tools exceed **10% of the context window**, Claude Code switches to **tool search** mode, finding tools on demand, which may be less reliable. *(Confirm the threshold at build time.)*

**DEBUG PRIORITY**: a new teammate lacks the servers everyone else has → **check that they're in project-scoped `.mcp.json`**, not local scope.

## C5.10 Hooks

**MUST REMEMBER**
- Hooks run commands at lifecycle points and are **deterministic: they always run**. A CLAUDE.md instruction is *usually* followed.
- "**If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.**"
- Configured in **`settings.json`** (event + optional **matcher** + command), or through **`/hooks`**.
- Events listed in the course:
  - **PreToolUse**: before a tool call.
  - **PostToolUse**: after a tool call.
  - **UserPromptSubmit**: before Claude processes the prompt.
  - **Stop**: when Claude finishes responding.
  - **Notification**.
- **PreToolUse blocking**: the hook receives the tool name and input as **JSON on stdin**.

| Exit code | Effect |
|---|---|
| **0** | Proceed |
| **2** | **Block**; **stderr is fed back to Claude** so it can adjust |
| Anything else | Non-blocking error, shown to you |

- Team sharing: **`.claude/settings.json`** is project-level and checked in. Use the **`CLAUDE_PROJECT_DIR`** environment variable to reference scripts regardless of the current directory.

**SYNTAX (settings.json shape; confirm at build time)**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|MultiEdit|Write",
        "hooks": [{"type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/format.sh"}]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-rm-rf.sh"}]
      }
    ]
  }
}
```

**DEBUG PRIORITY**
- "Claude sometimes skips Prettier" → **move the rule from CLAUDE.md to a PostToolUse hook**.
- A PreToolUse guard that doesn't block → **check that it exits with 2** (exit 1 is non-blocking) and writes its reason to **stderr**.

**TRADE-OFFS & FIXES**: CLAUDE.md is guidance (flexible, not guaranteed). A hook is enforcement (guaranteed, but it needs a script and maintenance). A permission mode decides who approves.

## C5 checkpoint answers
- The course quiz wasn't attempted (you chose to skip it). Its topics are covered by Practice Set items on permission modes, `/compact` vs `/clear`, MCP scopes, hook exit codes and CLAUDE.md.

---

# MODULE C6: Introduction to Model Context Protocol

## C6.1 What MCP is

**MUST REMEMBER**
- MCP is a **communication layer** that gives Claude context and tools without you writing tedious integration code. It **moves tool definitions and execution off your server** onto MCP servers.
- Architecture: an **MCP client** (inside your server) connects to **MCP servers**, which expose **tools, prompts and resources**. Each server is an interface to an outside service.
- Anyone can write a server; providers often publish official ones (for example AWS).
- "Isn't MCP the same as tool use?" **No.** They're complementary:
  - **MCP provides** ready-made tool schemas and functions.
  - **Tool use** is how Claude calls tools.
  - The difference is **who did the implementation work**.

## C6.2 MCP clients and transport

**MUST REMEMBER**
- The client bridges your server and MCP servers. It handles the message exchange and protocol details.
- MCP is **transport agnostic**. The most common setup is client and server on the same machine over **stdio** (standard input/output). HTTP, WebSockets and others also work.
- Message pairs:
  - **ListToolsRequest / ListToolsResult**: "what tools do you have?"
  - **CallToolRequest / CallToolResult**: "run this tool with these arguments."
- End-to-end flow:
  1. User query reaches your server.
  2. Your server asks the client for tools; the client sends **ListTools** to the MCP server.
  3. Your server sends the query **plus the tools** to Claude.
  4. Claude returns `tool_use`.
  5. Your server asks the client to run it; the client sends **CallTool**.
  6. The MCP server calls the external API (e.g. GitHub) and returns a **CallToolResult**.
  7. Your server sends the `tool_result` to Claude, which writes the final answer for the user.

**DEBUG PRIORITY**: Claude never sees the server's tools → **check that your server fetched ListTools and passed them in the `tools` array**.

## C6.3 Building a server: tools (Python SDK)

**SYNTAX**
```python
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")
docs = {"report.pdf": "The report details the state of a 20m condenser tower."}

@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string.",
)
def read_document(doc_id: str = Field(description="Id of the document to read")):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```
**MUST REMEMBER**
- Decorators plus type hints plus Pydantic **`Field(description=...)`** produce the schema automatically. You write no JSON schema.
- Errors are ordinary Python exceptions.
- Tools register through the decorator.

## C6.4 The MCP Inspector

**MUST REMEMBER**
- Start it with **`mcp dev mcp_server.py`** (or `uv run mcp dev mcp_server.py`). It opens a browser UI, typically at `http://127.0.0.1:6274`.
- Click **Connect**, then use the Resources, Tools and Prompts tabs (**List Tools**, then **Run Tool**).
- **State persists between calls**, so you can edit a document and then read it back.
- Use it to iterate, test edge cases and debug **without a full app**.

## C6.5 Implementing a client

**MUST REMEMBER**
- In real projects you build a client **or** a server, rarely both.
- The client is your own wrapper class around the SDK's **`ClientSession`**, so connections get cleaned up properly.

**SYNTAX**
```python
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools

async def call_tool(self, tool_name: str, tool_input: dict) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```
Run with `uv run mcp_client.py`, then `uv run main.py`.

## C6.6 Resources

**MUST REMEMBER**
- Resources **expose data**, like GET handlers. They're for **fetching**, not acting.
- The client sends **ReadResourceRequest(URI)** and gets back a **ReadResourceResult**.
- **Direct resources** have a static URI. **Templated resources** have `{params}` in the URI, which the SDK parses into keyword arguments.
- `mime_type` hints the format (`application/json`, `text/plain`, `application/pdf`). The SDK serializes return values for you.
- Use case: **@-mentions**. Resource content is **injected straight into the prompt**, so Claude needs **no tool call**.

**SYNTAX**
```python
@mcp.resource("docs://documents", mime_type="application/json")
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]

# client side
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
    if isinstance(resource, types.TextResourceContents):
        if resource.mimeType == "application/json":
            return json.loads(resource.text)
        return resource.text
```
The Inspector lists direct resources under **Resources** and templated ones under **Resource Templates**.

## C6.7 Prompts

**MUST REMEMBER**
- Prompts are **pre-built, tested instruction templates** published by the server author, who encodes domain expertise and edge-case handling.
- They return a **list of messages** (user and/or assistant). Client arguments become the function's keyword arguments.
- In a client UI they surface as slash commands (`/format plan.md`).
- Benefits: consistency, encoded expertise, reuse across clients, maintenance in one place.

**SYNTAX**
```python
from mcp.server.fastmcp.prompts import base

@mcp.prompt(name="format", description="Rewrites the contents of the document in Markdown format.")
def format_document(doc_id: str = Field(description="Id of the document to format")) -> list[base.Message]:
    prompt = f"Reformat the document below as Markdown.\n<document_id>\n{doc_id}\n</document_id>\nUse the 'edit_document' tool to save it."
    return [base.UserMessage(prompt)]

# client side
async def list_prompts(self) -> list[types.Prompt]:
    return (await self.session().list_prompts()).prompts

async def get_prompt(self, prompt_name, args: dict[str, str]):
    return (await self.session().get_prompt(prompt_name, args)).messages
```

## C6.8 Which primitive? Who controls it

| Primitive | Controlled by | Use it to | Example in the Claude app |
|---|---|---|---|
| **Tools** | **The model** (Claude decides when to call) | Give Claude new capabilities | Running code for a calculation |
| **Resources** | **The app** (your code decides when to fetch) | Get data into the UI or context | "Add from Google Drive" |
| **Prompts** | **The user** (button, menu, slash command) | Offer predefined workflows | Workflow buttons under the chat input |

"**Tools serve the model, resources serve your app, prompts serve your users.**"

**DEBUG PRIORITY**
- Claude makes needless tool calls just to read a document the user already chose → **expose it as a resource** and inject it (app-controlled).
- Users write poor ad-hoc prompts for a common workflow → **publish an MCP prompt** (user-controlled).

## C6 checkpoint answers
- The final assessment wasn't attempted (you chose to skip it). Practice Sets cover the primitive-to-controller mapping, the message pairs, transports and resource types.

---

# MODULE C7: Introduction to subagents

## C7.1 What subagents are

**MUST REMEMBER**
- Specialized helpers, each in its **own context window**. They do the work and return **only a summary**. The intermediate reads and searches stay isolated, and **the subagent's conversation is then discarded**.
- A subagent receives **two inputs**:
  1. its **custom system prompt** (from the config file);
  2. a **task description written by the parent agent**.
- Trade-off: you **lose visibility** into how it reached its conclusions.
- Built-ins:
  - **General purpose**: multi-step tasks, exploring and acting.
  - **Explore**: fast search and navigation.
  - **Plan**: used in plan mode for research before the plan is presented.

## C7.2 Creating a subagent

**MUST REMEMBER**
- Run **`/agents` → Create new agent**. Choose the scope:
  - **project-level**: this project only;
  - **user-level**: every project on the machine.
- The recommended way is to **let Claude generate** the name, description and system prompt from your description.
- Tool categories: read-only, edit, execution, MCP, other.
- Model: **`haiku` / `sonnet` / `opus` / `inherit`** (inherit uses the main conversation's model). Pick a color for the UI.
- Saved at **`.claude/agents/<name>.md`**. The body below the frontmatter is the **system prompt**.

**SYNTAX**
```markdown
---
name: code-quality-reviewer
description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance.
tools: Bash, Glob, Grep, Read, WebFetch, WebSearch
model: sonnet
color: purple
---
You are an expert code reviewer specializing in quality assurance, security best practices, and adherence to project standards...
```
- **`description` must be a single line** (use escaped `\n` for line breaks). It may include example conversations.
- Invoke a subagent by name or with **`@agent code-quality-reviewer`**.
- To get **automatic delegation**, put the word **"proactively"** in the description and add concrete trigger examples.

**DEBUG PRIORITY**: the subagent is never used when expected → **fix the description** (specific triggers and examples, "proactively").

## C7.3 Designing effective subagents (four fixes)

**MUST REMEMBER**
- The **name and description of every subagent go into the main agent's system prompt**. That's how the main agent picks one.
- The description **also shapes the input prompt** the main agent writes for the subagent.
  - Adding "*You must tell the agent precisely which files you want it to review*" makes the main agent list the files.
  - Adding "*return sources that can be cited*" does the same for a web-search subagent.
- **Define an output format** in the system prompt. This is the **single most important improvement**: it gives natural stopping points and **prevents runs that go on too long**. Example sections: Summary / Critical / Major / Minor / Recommendations / Approval status.
- **Report obstacles**: add an "Obstacles Encountered" section (setup issues, workarounds, environment quirks, commands that needed special flags, problem dependencies) so the main thread doesn't have to rediscover them.
- **Limit tool access**:
  - research or read-only → **Glob, Grep, Read**;
  - reviewer → plus **Bash** (for `git diff`), **no Edit or Write**;
  - code-modifying agent → Edit and Write.

**DEBUG PRIORITY**
- A subagent runs for ages → **add an output format**.
- The main thread re-solves a setup problem → **add obstacle reporting**.
- The subagent got vague instructions → **tighten its description**.

## C7.4 When to use subagents (and when not to)

**MUST REMEMBER**
- The decision rule: "**Does the intermediate work matter?**" No → delegate. Yes → keep it in the main thread.
- **Use subagents for**:
  - **research and exploration** ("JWT validation is in `middleware/auth.js` line 42");
  - **code reviews**: Claude reviews better when the code is presented as someone else's. The thread that wrote it gives weak feedback;
  - tasks needing a **custom system prompt**, such as copywriting (Claude Code's default prompt is concise and code-focused) or styling against design-system files.
- **Avoid subagents for**:
  - **"expert" personas** ("you are a Python expert" adds nothing);
  - **sequential pipelines** where each step depends on the last (reproduce → debug → fix loses information at each handoff);
  - **test runners** (they hide the full failure output; the course reports this pattern **performed worst** in testing).

**TRADE-OFFS & FIXES**: a subagent buys a clean main context and pays with lost visibility and a lossy summary. That trade only pays off when the main thread doesn't need the journey.

## C7 checkpoint answers
- This course has no quiz. Practice Sets cover description-driven triggering, output formats, tool scoping and the three anti-patterns.

---
# MODULE C8: Product Foundations

## C8.1 What Claude Code is (advisory framing)

**MUST REMEMBER**
- A chat interface answers and generates text. It has no access to files, terminal or project and is stateless between messages.
- **Claude Code reads, edits, runs and loops.** It works inside the codebase and keeps going until the task is done or you pause it.
- The loop:
  - **Observe**: greps, opens the files it judges relevant, reads terminal output. It doesn't assume the project structure.
  - **Plan**: steps, files, commands, order; for larger tasks it can show the plan for approval first.
  - **Act**: real edits and commands, **logged and visible**.
  - **Verify**: surfaces the result and waits; a failure feeds into a fresh Observe pass.
- **Every tool call is logged and reviewable.** That auditability is what makes autonomous operation safe to authorize.
- **Same model, same loop on every surface.** "The surface changes the integration point, not the intelligence."

| Surface | Access | Note |
|---|---|---|
| **CLI** | Native, OS-level filesystem and terminal | The baseline and reference for all configuration decisions |
| **IDE extensions** (VS Code, JetBrains) | Native (runs the local agent) | A wrapper, not a lighter version |
| **Agent SDK** | Whatever the host grants (e.g. the CI runner's access) | Pipelines, CI/CD, multi-agent workflows |
| **Desktop / Web / Mobile** | **Scoped**: runs tasks in the cloud; reaches filesystem and terminal **only when the developer explicitly invokes the agent tooling** | Business-facing work |

**C8 lesson-1 checks**
- "Claude Code uses a different model tier than Claude.ai" → **False**. Same model family; the model is chosen at deployment.
- "It can run bash and edit files on the machine where it's installed" → **True**. The tools are configurable and an admin can restrict them.
- "The IDE extension has different capabilities from the CLI" → **False**. Same agent, model and tools; what matters is the **access surface**, not the label.

## C8.2 Model selection for Claude Code

**MUST REMEMBER (course lineup; confirm at build time)**

| Model | Cost / context | Best for |
|---|---|---|
| **Haiku 4.5** | Lowest · 200k | Real-time apps, **sub-agents**, CI/CD pipelines, inline completions, high-volume scripted tasks |
| **Sonnet 4.6** | Mid · 1M | **The production default for Claude Code**: day-to-day development, functions, tests, docs, features. Most pilots start here |
| **Opus 4.8** | Highest · 1M | Autonomous refactoring runs, multi-hour tasks, architectural review |

- **Start with Sonnet.** Use **Opus** for sustained reasoning and **Haiku** when volume and cost dominate. Most enterprise teams do better with a **tiered mix** than one model.
- **The effort lever: try effort before switching models; it's cheaper.**
  - **Opus 4.8** supports **`xhigh`**, the recommended setting for coding and agentic work.
  - **Sonnet 4.6** effort goes up to **`high`**.
  - Higher effort pays off on multi-file refactors with cross-module dependencies, not on unit tests for a 20-line utility.
- "**Model selection is an architecture decision; effort tuning is a performance lever.**"

**Scenario answer** (50 developers doing routine work plus a small group running overnight autonomous refactors): **Sonnet 4.6 by default, Opus 4.8 for the overnight runs.**
- All Haiku degrades the complex work.
- All Opus adds roughly **65% cost** for no gain on routine work.
- All Sonnet overpays for high-volume scripted tasks (docstrings, inline completions) that Haiku handles.

## C8.3 The seven platform paths

**MUST REMEMBER**
- The seven paths: **Claude.ai Teams, Claude.ai Enterprise, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Azure AI Foundry, Anthropic API, Anthropic Console.**
- Three categories:
  1. **Claude-managed (Teams + Enterprise)**: full feature set **including web and mobile**, central billing, no infrastructure. **The default recommendation** for most GSI-led activations.
  2. **Cloud-native (Bedrock, Vertex, Foundry)**: runs through the client's cloud with IAM, regional data controls and cloud billing. **No Claude.ai web surface.** Choose it for existing cloud commitments or data residency, and **flag the governance gap**.
  3. **API / Console**: individual developers, API-key auth, pay-as-you-go, **no enterprise controls**. Name it only to rule it out for a governed rollout.
- The picker asks, in order: **cloud posture first, then governance, then scope**.

| Residency in a client-controlled region? | Governance asks (SSO, audit logs, managed settings, Compliance API)? | Scope | Result |
|---|---|---|---|
| Yes: AWS / GCP / Azure | any | any | **Bedrock / Vertex / Foundry + LLM gateway** (flag: no web, no managed settings, no Compliance API) |
| No | Yes | Team or org | **Claude for Enterprise** |
| No | No | Team or org | **Claude.ai Teams** (move up to Enterprise as soon as SSO, audit logs or managed settings come up) |
| No | any | Single developer / prototype | **Anthropic API / Console** |

- "**Enterprise isn't more seats. It's the controls tier.**"
  - **Teams**: usage-based billing plus a per-seat fee; team management, admin tools, **basic SSO**.
  - **Enterprise**: **SSO with domain capture, SCIM provisioning, RBAC, Compliance API, managed policy settings.**
- "**Cloud-native routing satisfies an existing commitment, not a security requirement.**"
- **LLM gateway**: middleware that routes model calls through corporate controls (logging, filtering, policy) before they reach the provider. It sits between Claude Code and any provider and adds central auth, usage tracking and rate limits.

**Seat types (usage-based model)**

| Seat | Claude Code? | Watch for |
|---|---|---|
| **Standard** | **No** (chat only) | The most common mismatch: "we have Claude" doesn't mean Claude Code |
| **Chat + Code** | Yes (the **minimum** for Claude Code) | What was demoed vs what was bought |
| **Claude Enterprise** | Yes, plus all controls and the Compliance API | Security asks for audit logs or managed settings → this tier |

- Legacy seat-based plans use **Standard and Premium** names, so confirm which pricing model the client is on.
- **Seat mismatches are a common cause of activation delays.** Check the seat type before kickoff.

**Scenario answer** (financial services, AWS-heavy, processing must stay in approved AWS regions, devices managed with Intune, 200 developers): **Bedrock + LLM gateway.**
- Enterprise is SaaS: Anthropic's infrastructure decides the processing location.
- Name the trade-off: no web surface and no Enterprise admin features.
- **Intune affects distribution to endpoints, not the deployment architecture.** It's a distractor.

**DEBUG PRIORITY**: developers "have Claude" but can't run Claude Code → **check the seat type** before anything technical.

---

# MODULE C9: Deployment Architecture

## C9.1 The deployment decision framework

**MUST REMEMBER**
- The path decides **who bills, how users authenticate, where usage data lands, and which features exist**.
  - Procurement signs against the billing route, security reviews the auth model, and finance builds chargeback on the cost-tracking surface.
  - Reversing the path means **re-running all three**. It's a **one-way door**.
- On a 30-day activation the path is decided in **pre-kickoff (Day −14 to Day 0)**, alongside the security questionnaire, not in a mid-engagement change request.
- The working rule: **the client's existing cloud commitments and compliance posture pick the path.** Surface them before the client picks by default.

| Path | Billing | Auth | Audit / cost | Notes |
|---|---|---|---|---|
| **Claude for Enterprise (direct)** | Seat-based contract | Claude.ai **SSO** + domain capture, roles | Usage dashboard, compliance API | **The only path that bundles Claude on the web**; **the only path eligible for ZDR**; Anthropic's recommended default |
| **Amazon Bedrock** | PAYG via AWS (burns down commitments) | **IAM** or Bedrock API keys | **CloudTrail**; **Cost Explorer**; **Bedrock Guardrails** filtering | Traffic stays in the client's AWS account; the client enables models per account and region |
| **Google Vertex AI** | GCP billing | GCP credentials + **ADC**, IAM roles | **Cloud Audit Logs** | Access requested per project via **Model Garden**, **24–48 h** approval; global, multi-region and regional endpoints |
| **Microsoft Foundry** | Azure billing | API key or **Entra ID**; RBAC | **Azure Monitor** | The client provisions deployments in the Foundry portal; **requests go to Anthropic-operated infrastructure** (unlike Bedrock and Vertex) |

**Decision drivers, asked in this order**
1. **Cloud commitments**: AWS **EDP**, GCP **CUD**, Azure **MACC**. This is the strongest pull. Ask **procurement**, not only IT.
2. **How procurement buys**: seats on a new Anthropic contract vs **PAYG through a marketplace they already use** (days vs months to approve).
3. **Compliance posture**: **ZDR → Enterprise direct only**. Traffic inside their own tenancy and regions → **Bedrock or Vertex**.
4. **Who manages users and budgets**: Enterprise has them built in. Cloud paths need IAM plus cost tooling, or an LLM gateway.

**The trade-off to say out loud**
- Cloud paths keep the client's perimeter and tooling. The cost: **no bundled web, no ZDR**, a few capability gaps, **the client pins model versions** (unpinned aliases can lag releases or point at models not enabled in their account), and **the client builds the usage dashboard** (Cost Explorer, GCP Billing, Azure Cost Management, or a gateway).
- Enterprise direct gives the full surface. The cost: a new vendor, seat pricing instead of commitment burn-down, and traffic going to Anthropic's platform rather than their own tenancy.

**Pre-kickoff blockers by path**

| Path | Long pole | Checklist |
|---|---|---|
| Enterprise | **Identity** | SSO and domain capture with the IdP team; seat list and roles; managed policy settings; **ZDR request to the account team if required (confirmed per organization)** |
| Bedrock | Mostly same-day | Use-case form **per AWS account** (access is immediate); IAM policy for model invocation and inference profiles; enable models per region; **pin model IDs before anyone installs** |
| Vertex | **File the access request on Day 1** | Enable the Vertex AI API; request Claude in Model Garden (**24–48 h**); confirm regional quota; pin model IDs |
| Foundry | Versions | Provision the resource; create deployments with **fixed versions, not auto-update**; agree Entra ID roles or key handling; pin deployment names |

**Meridian Capital simulation (strong / defensible / costly)**
- Discovery, first question: **cloud commitments and buying route** (2) · seat phasing (1) · IDE and repo setup (0).
- A 3-year AWS EDP the CFO wants to burn down, security review pending: **Bedrock, conditional on the security review** (2) · Enterprise as the premium option (1) · Foundry because they use Entra ID (0).
- The CISO asks "ZDR on Bedrock?": **"No. On Bedrock, retention is governed by AWS in your account"** (2) · "I'll confirm" (1) · "ZDR applies everywhere" (0).
- The CIO asks "what do we give up?": **name the gaps** (no web, no Anthropic ZDR, **no WebSearch**, the client owns pinning) and offer a one-page memo (2) · billing only (1) · "functionally nothing" (0).

## C9.2 Feature parity gaps: the gap memo

**MUST REMEMBER**
- Every gap gets discovered; the only question is **by whom and when**: week 1 (a champion), week 2 (an empty CoE dashboard), or Day 30 (the readout).
- "**A gap flagged at contract time is consulting. The same gap discovered in week three is a defect with your name on it.**"
- Deliver **a one-page gap memo with the path recommendation, before signature.**

| Gap | Applies to | Mitigation |
|---|---|---|
| **WebSearch unavailable** | **Bedrock** | Approved MCP alternative, scoped in pre-kickoff |
| **No bundled Claude on the web** | All cloud paths | The client buys a chat surface separately if needed (comes up at the first exec demo) |
| **Anthropic ZDR doesn't apply** | All cloud paths | Retention follows the provider's policies: "**different control, not absent control**" |
| **Model versions are the client's job** | All cloud paths | Pin in shared settings. Aliases like `sonnet` can lag or point at models that aren't enabled. **Background tasks default to the primary model**, not a cheaper Haiku-class one |
| **Telemetry off by default** | All cloud (third-party) paths | Anthropic metrics, error reporting and **`/feedback`** submission are disabled (`/feedback` **writes a local bundle**). CoE metrics need **OTel or a gateway** |
| **Vertex fine print** | Vertex (caching: Vertex **and** Bedrock) | 24–48 h Model Garden approval; **MCP tool search is off by default** (enable it or large catalogs load upfront); **prompt caching availability varies by region**, so cache counts at zero mean check the region |

- **Structure of each memo line**: name the gap → place the moment (which week, person, meeting) → **lead with the mitigation**. A bare comparison table reads as a reason to stall the deal.

**Northgate Logistics simulation**
- The CTO wants the memo trimmed: **keep every line, reframed as mitigations, and offer to walk security through it** (2) · move it to the kickoff deck (1) · trim to two items (0).
- "WebSearch doesn't work, is our install broken?": **reply with the memo line and the approved MCP alternative** (2) · open a support ticket (1) · tell people to use personal claude.ai accounts (0; unmanaged accounts outside the perimeter).
- "Where's our usage data?": **telemetry is off by default on Bedrock; the data lives in OTel, Cost Explorer or the gateway** (2) · run a survey (1) · "the Anthropic Console has it" (0; Console usage views belong to Enterprise direct).

## C9.3 Corporate proxy configuration

**MUST REMEMBER**
- **The first support ticket of every enterprise activation is a network ticket.** Find out what sits between the terminal and the model endpoint **before 40 people install**.
- **A corporate proxy gets traffic out of the building** (HTTP/HTTPS proxy, TLS inspection, firewall allowlists). Claude Code respects the standard proxy environment variables.
- **An LLM gateway controls what happens to model traffic** (auth, budgets, attribution). It's configured through **base-URL overrides, not proxy variables**. The two stack.

**SYNTAX**
```bash
export HTTPS_PROXY=https://proxy.client.com:8080
export HTTP_PROXY=http://proxy.client.com:8080                 # fallback if the proxy has no HTTPS endpoint
export NO_PROXY="localhost,.client.com,169.254.169.254"        # comma- or space-separated
export HTTPS_PROXY=http://user:pass@proxy.client.com:8080      # basic auth; credentials from a secrets manager, never hardcoded

export NODE_EXTRA_CA_CERTS=/etc/ssl/corp-root-ca.pem           # trust the corporate root CA (TLS inspection)
export CLAUDE_CODE_CERT_STORE=system                           # which trust stores to use (default: system)
export CLAUDE_CODE_CLIENT_CERT=/path/to/client-cert.pem        # mTLS
export CLAUDE_CODE_CLIENT_KEY=/path/to/client-key.pem
```
- The course says proxy variables are **OS-level and can't be set in Claude Code settings files**; deploy them org-wide through **MDM** (Jamf or Kandji on macOS, registry policy on Windows). One simulation answer talks about shipping the CA setting "in the same managed settings block", which is inconsistent. **Confirm at build time** whether your Claude Code version honours `env` in settings.
- **SOCKS proxies aren't supported**, so rule them out.
- **NTLM or Kerberos proxy auth** isn't supported directly; **escalate to an LLM gateway** that handles enterprise auth.
- **TLS inspection** (Zscaler, Netskope) re-signs traffic. Claude Code trusts the **OS system store by default**.
  - "**Self-signed certificate in certificate chain**" means the proxy is working as designed.
  - Fix it by **trusting the corporate root CA**. **Never disable verification** (`NODE_TLS_REJECT_UNAUTHORIZED=0` fails the client's security review).

**Allowlist, with a reason per domain**

| Domain | Why |
|---|---|
| `api.anthropic.com` | API on the direct path **and the WebFetch domain-safety preflight on every path**. If it's blocked on Bedrock, WebFetch fails even though model traffic works, unless settings disable the preflight |
| `claude.ai`, `platform.claude.com` | Auth for claude.ai and Console accounts; mostly the direct path |
| `downloads.claude.ai` | Native installer, auto-updater, plugin downloads (skippable if you distribute through your own artifact registry) |
| Cloud provider endpoints | Model and auth traffic on Bedrock, Vertex and Foundry (usually already reachable) |

Verify the final posture with **`/status`** inside Claude Code.

**managed-settings.json**
- The **top of the settings hierarchy**, above user and project settings. **Developers can't override it.**
- Use it to lock permissions, **enforce allowed MCP servers**, require SSO login and pin version floors.
- Three delivery paths:
  1. **server-managed** via the Anthropic admin console (**Enterprise only**);
  2. **MDM / OS-level** (plist on macOS, registry on Windows, via Jamf or Kandji);
  3. **file-based** (`managed-settings.json` in the OS system directory).
- All three require admin rights, which is the point.

**Halvern Bank simulation** (40 terminals hanging)
- First move: **ask the network team about the proxy and TLS inspection** (2) · test on a hotspot (1) · reinstall (0).
- Rollout: **push `HTTPS_PROXY` and `NO_PROXY` through MDM** (2) · post export commands in the channel (1) · use the SOCKS5 proxy (0).
- Certificate error: **`NODE_EXTRA_CA_CERTS` pointing at the corporate root** (2) · request a TLS-inspection bypass (1) · `NODE_TLS_REJECT_UNAUTHORIZED=0` (0).
- Security wants the domain list: **the allowlist with a reason per domain, the preflight nuance and the optional telemetry** (2) · wildcards (1) · "it's just HTTPS on 443" (0).

**DEBUG PRIORITY**
- Every terminal hangs on the first prompt → **proxy**.
- "Self-signed certificate in chain" → **corporate CA trust**.
- WebFetch fails on Bedrock while chat works → **`api.anthropic.com` preflight blocked**.

## C9.4 The LLM gateway pattern

**MUST REMEMBER**
- "**A proxy passes traffic. A gateway understands it.**" A proxy can't answer *who is spending what*; a gateway can.
- Five things a gateway does that a proxy can't:
  1. **Centralized auth**: provider credentials in one place; developers hold short-lived gateway tokens; rotation happens once.
  2. **Per-team cost attribution** from headers.
  3. **Budget enforcement**: rate limits and spend caps **at the request boundary, before the model call**. This is enforcement, not reporting.
  4. **Model routing**: switch providers or versions behind one stable endpoint (Bedrock and Vertex behind one URL); developer machines don't change.
  5. **Compliance audit logging** in the client's stack. On cloud paths where telemetry to Anthropic is off, this is where observability comes from.

**SYNTAX**
```bash
# Gateway exposing the Anthropic API format
export ANTHROPIC_BASE_URL=https://llm-gateway.client.com
export ANTHROPIC_AUTH_TOKEN=team-token-from-gateway

# Bedrock behind the gateway
export CLAUDE_CODE_USE_BEDROCK=1
export ANTHROPIC_BEDROCK_BASE_URL=https://llm-gateway.client.com/bedrock
export CLAUDE_CODE_SKIP_BEDROCK_AUTH=1

# Vertex behind the gateway
export CLAUDE_CODE_USE_VERTEX=1
export ANTHROPIC_VERTEX_BASE_URL=https://llm-gateway.client.com/vertex
export CLAUDE_CODE_SKIP_VERTEX_AUTH=1
```
- The **skip-auth flags** are where centralized auth shows up in code: Claude Code stops signing requests because the gateway injects provider credentials server-side.
- **Rotating per-user tokens** → **`apiKeyHelper`** in settings runs a script that fetches the token from the vault.
- **Gateway acceptance criterion (a pilot go/no-go): forward the `anthropic-beta` and `anthropic-version` headers intact.** Stripping them silently degrades Claude Code features and looks like a product bug until someone inspects the traffic.

**Session headers** (sent automatically; the gateway reads them **without parsing the request body**)

| Header | Level | Enables |
|---|---|---|
| `X-Claude-Code-Session-Id` | Session | Cost and duration per session |
| `X-Claude-Code-Agent-Id` | Subagent | Cost per agent thread |
| `X-Claude-Code-Parent-Agent-Id` | Parent link | Nested subagents roll up to one team |

Map gateway tokens to teams and you get **cost per team per week, sessions per developer, and budget alerts before the invoice**.

- **LiteLLM** is the reference implementation in Anthropic's gateway docs (`code.claude.com/docs/en/llm-gateway`). It passes through both Anthropic Messages format and OpenAI-compatible format.
- **Security notice: LiteLLM PyPI versions 1.82.7 and 1.82.8 were compromised** with credential-stealing malware. Verify a safe version before any client deployment. This is a supply-chain risk.
- **Positioning**: recommend a gateway **before the client asks**: more than one team, a chargeback requirement, or multi-cloud routing.

**DEBUG PRIORITY**: beta features missing only behind the gateway → **check that the gateway forwards `anthropic-beta` / `anthropic-version`**.

## C9.5 Data residency, compliance posture, ZDR

**MUST REMEMBER**
- The **security questionnaire is the first pre-kickoff item**; nothing else proceeds until it clears.
- **Training**: Anthropic doesn't train generative models on code or prompts sent to Claude Code **under commercial terms** (Team, Enterprise, API, cloud paths). The exception is **explicit opt-in**, such as the **Development Partner Program**: an org admin has to join, and it isn't available on Bedrock or Vertex. Say "**no, unless you explicitly opt in**", not "no, never".
- **Retention**:
  - Server-side retention is governed by the **customer agreement**, so confirm the window with the account team. The scenario's top answer uses **30 days**. *(Confirm at build time.)*
  - **Claude Code also caches session transcripts locally**, in **plaintext under the user's home directory**, configurable (30 days by default per the scenario). That's a **device-management** conversation.

| Path | Encryption at rest |
|---|---|
| Anthropic direct | AES-256; **ZDR** for eligible Enterprise orgs |
| Bedrock | Client's AWS account; AES-256 with AWS-managed keys; customer-managed via **KMS** |
| Vertex | Client's GCP project; Google-managed by default; **CMEK** optional |
| Foundry | Azure billing, Entra ID, RBAC; **confirm data routing with Anthropic before advising residency-bound clients** (requests go to Anthropic-operated infrastructure) |

**ZDR, precisely**
- It applies to **Claude Code on Claude for Enterprise**, **enabled per organization by the Anthropic account team after an eligibility review**. It's **not in standard Enterprise by default** and **not available on cloud paths**.
- **Covers**: Claude Code inference. Prompts and responses aren't stored after the response returns (except where law or abuse handling requires). Admin cost controls, analytics and audit logs keep working.
- **Doesn't cover**: claude.ai chat, Cowork, admin metadata (seat assignments), anything **third-party MCP servers** process.
- **Disables** (they need server-side storage): **Claude Code on the web, remote sessions from the desktop app, `/feedback`**.
- **Flagged sessions can still be retained up to 2 years** under the usage policy.
- Analytics under ZDR shows **usage metrics, not contribution metrics**, so design the Day 30 scorecard around what's measurable.
- **Each new org under the same account needs its own enablement.**

**Residency and certifications**
- **Residency follows the path**: Bedrock region selection; Vertex global, multi-region or regional endpoints. On the direct path, region-level processing guarantees are an **account-team conversation**; don't improvise one.
- The **certification artifacts are self-serve at trust.anthropic.com**:
  - SOC 2 Type 2; ISO 27001:2022; ISO/IEC 27017 and 27018; **ISO/IEC 42001** (AI management systems); CSA STAR Level 2;
  - **HIPAA with BAA available**; GDPR; NIST 800-171 attestation; **FedRAMP High through Claude for Government**;
  - annual third-party penetration test summaries.
- The working rule: **answer from facts you can cite, name the one thing you'll verify, and never improvise a guarantee.** "I'll confirm" is forgiven; a wrong yes isn't.

**Corvane Health simulation** (CISO, live)
- Training: **"No under commercial terms, unless you explicitly opt in"** (2) · "I'll send the policy" (1) · "it's anonymized first" (0; invented mechanism).
- Retention without ZDR: **server-side window plus local plaintext transcripts** (2) · agreement only (1) · "ephemeral" (0; sessions resume, so they're stored).
- ZDR plus Claude Code on the web: **"They conflict; choose deliberately"** (2) · "ZDR now, web later" (1) · "both, standard" (0).
- Foundry: "stays in our tenancy?" → **"No; Foundry routes to Anthropic infrastructure; Bedrock or Vertex meet that requirement"** (2) · "broadly yes" (1) · "correct" (0).
- Certifications and pen test by Friday: **send the Trust Center links today** (2) · "SOC 2 covers it" (1) · a two-week legal request (0).

**Course artifact**: the **Deployment Decision Doc** has five sections: path recommendation, parity-gap memo, network posture, gateway design and compliance posture. A colleague then red-teams it as the CISO for 15 minutes.

## C9 checkpoint answers
- The simulation best answers are listed above per lesson. The scoring bands for each: ≥7/8 (Meridian, Halvern), 6/6 (Northgate) or ≥9/10 (Corvane) = "Delivery ready".

---
# MODULE C10: Delivery Methodology

## C10.1 Use-case identification and qualification

**MUST REMEMBER**
- **Marginal gain**: the same work, faster. The unit of work doesn't change (autocomplete, boilerplate, inline docs). Good for adoption momentum, hard to isolate in 30 days, and a weak anchor for a CIO business case.
- **Structural gain**: **the unit of work changes** (four people for six weeks becomes two people for two weeks). It's measurable before Day 30 and **anchors renewal**.

| Engagement mode | What it is | What it produces |
|---|---|---|
| **Mode 1**: 2-day training activation | Code 101 plus admin setup | **Adoption signals, not ROI data** (no measurement period, owner or baseline) |
| **Mode 2**: 30–45 day program | Training + pre-kickoff + use-case definition + **midpoint check at Day 20–25** + closeout with **champion-presented** results | **ROI data**, because measurement was built before Day 1 |

**Three patterns that reliably give structural gains**

| Pattern | What it is | Measure |
|---|---|---|
| Code modernization | Legacy stacks, language translation, dependency upgrades | Claude-assisted commits ÷ total commits |
| New feature build | The full loop | **PR cycle time** before and after (best with clear scope and a well-maintained CLAUDE.md) |
| Code migration | Frameworks, cloud providers, architectural patterns | Velocity, visible **within two weeks** |

**Four qualification criteria**
- **Volume**: recurs enough to produce 30 days of data.
- **Complexity**: real leverage. "A junior could do it in an afternoon" is marginal; "a senior takes three weeks" is structural.
- **Measurability**: a baseline exists **before Day 1**. This one is **non-negotiable**.
- **Developer readiness**: willing to change the workflow, not just try a tool.

**The qualification rule**: "**A use case that scores well on complexity but fails on measurability is not a pilot candidate. It is a risk.**"

**Arvana simulation**: Java-to-Spring Boot migration, not unit tests at 82% coverage · baseline **PR cycle time, ticket to merge** (not self-reported hours, not lines of code) · cohort of **8–10 developers who own the migration backlog**.

## C10.2 Pilot design

**MUST REMEMBER**
- Choose the cohort by **ownership, not availability**: **use-case owners**, not enthusiasts. Enthusiasts' data doesn't extrapolate.
- Scope:
  1. **Define the use case precisely** ("Java-to-Spring Boot migration of the auth service module").
  2. Pick the cohort by ownership.
  3. **Set the duration from task cycle time**: at least **two complete ticket-to-merge cycles per developer**, usually **25–30 days** for migration work.
  4. **Lock the scope before Day 1**; new ideas go into a **Phase 2** log.
- Success criteria, **all set before Day 1**: **baseline metric**, **target threshold** ("25% reduction" is a claim; "improved" isn't), **measurement method** (git, JIRA or PR analytics over self-report), **target date**.
- The template: "*[Metric] will [improve/decrease] by [threshold] compared to the Day 1 baseline by [date].*"
- The design rule: "**A success criterion you can't measure before Day 1 is a hypothesis, not a commitment.**"

**Kellner simulation**: the **8 migration owners** · **PR cycle time with a Day 1 baseline** (satisfaction is supporting evidence only; lines of code is a proxy "Claude games by default") · a mid-pilot doc-project request → **log it for Phase 2 and protect the scope** (tracking it separately is defensible only with baselines separated from Day 1).

## C10.3 ROI measurement

**MUST REMEMBER**
- "**A baseline captured after the pilot starts is already contaminated.**" A captured baseline is objective data; an estimated one is a negotiation.
- Typical baselines: **PR cycle time** for the use case, **self-reported hours** on the task category, **developer NPS or satisfaction**. Capture all three **before kickoff**.

| Metric category | Examples | Source |
|---|---|---|
| **Developer productivity** | Feature development time, prototyping velocity, suggestion acceptance rate | PR analytics, JIRA, sprint data |
| **Code quality** | First-pass review success, security-fix velocity, coverage | PR reviews, static analysis |
| **Usage and adoption** | DAU/WAU, % still using after 30 days, hours in the tool | Claude usage analytics |
| **Sentiment and culture** | Developer NPS, qualitative feedback, interest from other teams (a **leading indicator for expansion**) | 3–5 question surveys |

**The Day 30 readout: one headline number and one business implication**
1. **Lock the headline metric**: PR cycle time for a migration; spec-to-working-code time for a feature build.
2. **Translate it once into business terms**, scoped to the use case: "ships in 5.4 days what used to take 8.2, about 35% roadmap acceleration *for this use case*". Not "developers are 34% more productive".
3. **The Day 30 scorecard** fits on one page: use-case story, headline before and after, supporting metrics from the other three categories, champion anecdotes, a proposed **Day 60 goal**. This page is the Activation Summary deck.

**Voxfield simulation**: lead with **PR cycle time 8.2 → 5.4 days** (not satisfaction, not +55% lines of code) · the scoped roadmap translation · next step **expand the same use case to 20 developers plus one new use case with its own baseline** (not all 60 at once, not repeating the pilot).

## C10.4 Phased rollout and the adoption curve

**MUST REMEMBER**

| Phase | Behaviour | What you do |
|---|---|---|
| **Week 1: supervised use** | Manual approval of every action; **velocity is often slower** | Technical calibration, CLAUDE.md setup and first commit. **Don't intervene on velocity** |
| **Weeks 2–3: increasing autonomy** | More pre-approval, larger chunks, **plan mode**; some **auto-accept** on low-risk work. CLAUDE.md quality starts to matter | Review delegation patterns, run **Code 201**, watch for plateau |
| **Weeks 3–4: agentic for defined task classes** | Hand off reliable task types; **PR cycle-time gains become visible** | Auto-accept for defined classes, **hook configuration**, agentic task structuring |
| **Day 30+: institutionalized** | Routine use with informal norms. The target state; it **can't be forced earlier** | Week 4: document what worked, what broke, what CLAUDE.md should say |

- Two dynamics unique to AI rollouts:
  - **The Week-1 dip**: velocity drops while people calibrate. **That's not a signal for more training.**
  - **The plateau effect**: developers settle on one or two delegation patterns and stop experimenting. It looks like adoption, but the ceiling is low. Break it with a champion or a **Code 201** session.
- **The intervention test**:
  - Stuck on a **Claude Code problem** (hallucinations, prompt failures, context issues) → **technical help, now**.
  - Doing the same tasks with Claude as faster autocomplete → **workflow-design problem**: rethink delegation, not prompting.
- The adoption rule: "**A developer who has stopped experimenting is not a success story. Plateau is not adoption.**"

**Helios Day 16** (flat PR cycle time, 45 minutes a day of use, prompting unchanged since Week 1) → **plateau** (not failure, not "too early"). Run **Code 201 on plan mode and auto-accept for low-risk subtasks** (not daily stand-ups, which monitor without changing behaviour). Then a **30-minute peer demo** from the champion (Priya, −40%): her CLAUDE.md, her delegation patterns, and before/after PRs. Not ten one-to-ones.

## C10.5 Champion enablement and documentation

**MUST REMEMBER**
- **Champion** is a role, not a title.
  - **Does**: maintains CLAUDE.md, runs weekly office hours or a channel, onboards new developers, escalates blockers.
  - **Doesn't**: act as the only expert (that's fragile).
  - **Needs**: a populated CLAUDE.md, a **custom command catalogue of 3–5+ commands**, and an escalation path. **The handoff happens before Day 30, not on it.**
- A good candidate is **senior enough to shape norms, technical enough to write CLAUDE.md, and intrinsically motivated**. The best ones **identify themselves in Phase 2**.
- **CLAUDE.md is institutional memory Claude reads every session.** About 30 minutes a week maintaining it compounds. A generic CLAUDE.md gives a generic Claude.
- **The handoff package**: an **enterprise-level CLAUDE.md**, at least one **repo-specific CLAUDE.md** for the pilot project, and a **command catalogue** (≥3–5 commands with frontmatter, parameter descriptions and example invocations).
- The handoff principle: "**The quality of a deployment 90 days after you leave is determined by the quality of the CLAUDE.md you hand over.**"
- True/false checks:
  - "The champion should be the most technically advanced developer" → **False** (influence and motivation matter more).
  - "CLAUDE.md should be finalized and stable before the engagement ends" → **False** (it's a living document with an owner).
  - "Custom commands are optional for a small team" → **False** (3–5 commands are non-negotiable).

## C10.6 Six failure modes (none technical)

| # | Failure | Preemption |
|---|---|---|
| 1 | **No baseline** → the ROI case collapses | **A baseline sprint in the week before kickoff**, non-negotiable |
| 2 | **No champion** → decays to zero within a quarter | **Name the champion by Day 15**; start handoff prep in Phase 2 |
| 3 | **Use case too marginal** → flat metrics despite high usage | Structural vs marginal qualification **before scoping** |
| 4 | **Stuck in supervised mode** → plateau, "slow", "not useful" | **A weekly CoE touchpoint with usage review**; workflow-fit coaching in Phase 2 |
| 5 | **CLAUDE.md not maintained** → Claude falls back to generic behaviour | **A weekly CLAUDE.md review** as a named champion responsibility |
| 6 | **Readout not tied to business outcomes** → the conversation moves to cost, and renewal stalls in procurement | **Align the CIO narrative with the sponsor in week one** |

- **A clean close has four artifacts**:
  1. the complete Delivery Plan Pack (qualification, pilot design, ROI scorecard, champion plan);
  2. CLAUDE.md (enterprise + repo) and the command catalogue;
  3. the Day 30 readout against the success criteria, **in the client's hands 48 hours before the showcase**;
  4. a named champion with an escalation path and **the 30-day post-engagement check-in date**.
- Risk-spotting exercise (12-developer pilot, two days before the readout):
  - **Risks**: no baseline · no champion at Day 28 · **no custom commands** (CLAUDE.md exists but the catalogue is empty).
  - **Not risks**: 4 of 12 still in supervised mode at Day 28 (normal) · PR cycle time −20% (the CIO headline) · three heavy users (champion candidates).
- *Course inconsistency to note:* L6 says name the champion **by Day 15**; L7 says identify the champion candidate **in week three**. Both statements are in the course.

## C10.7 The 30-day activation arc

| Phase | Work | Exit condition |
|---|---|---|
| **Pre-kickoff** | Qualification, cohort, **baseline from version control**, **draft CLAUDE.md** | Baseline captured, CLAUDE.md drafted, cohort confirmed, kickoff date set |
| **Week 1: onboarding sprint** | Install, connect to the approved deployment config (C9), supervised tasks; **first office hours on Day 3 or 4** | Whole cohort active, no install blockers |
| **Weeks 2–3: active pilot** | **CoE touchpoints on Day 8 and Day 15**, usage review, coaching; champion candidate found in week 3 | **At least half the cohort past supervised mode**; champion candidate identified |
| **Week 4: ramp and showcase prep** | Metrics vs criteria, readout and CIO narrative, champion handoff (CLAUDE.md review, command catalogue, escalation path); **readout to the sponsor 48 h before** | Readout sent, champion briefed, four artifacts complete |
| **Day 30: showcase** | Live demo, metrics, renewal conversation; **sponsor in the room, or reschedule** | A decision on Phase 2 |

- The consultant usually owns the exit conditions for phases 1 and 5; the champion candidate owns phases 2–4.
- **CoE touchpoint**: 30 minutes, consultant-led, Days 8 and 15, with the champion candidate or engineering lead (**not the whole cohort**). Agenda: usage data, who is stuck in supervised mode, **one concrete coaching action per stalled developer**, CLAUDE.md updates. The output is an intervention or a green light.
- **Office hours**: 60 minutes, open Q&A. Session 1 is consultant-led; **the champion co-facilitates from session 2 and runs it from session 3**. This is **the main handoff mechanism**.
- **Put both on the calendar, with video links, before kickoff.** Treat them as immovable.
- **The Day 30 showcase**: 30 minutes, three parts.
  1. **Live demo** (10 min) by 2–3 developers at **stage 3 or 4** of the curve, on real code, not a script.
  2. **Metrics** (10 min), headline first, every number against the agreed criteria. **Name unmet criteria before the sponsor asks.**
  3. **Renewal** (10 min): Phase 2, the champion, the 90-day health check, a specific next step. The sponsor should leave with a **decision**, not a follow-up.

## C10 checkpoint answers
- The simulation best answers are listed above per lesson. All of C10's interactive checks were captured; there's no end-of-course quiz.

---

# Cross-module "symptom → check FIRST / not this" table

| Symptom | Check FIRST | Not this |
|---|---|---|
| Re-explaining background every session | Entry point → **Project** (C3) | Bigger model |
| Wrong totals in a generated report | **Code Execution** for numbers (C3, C1.6) | "Double-check your math" in the prompt |
| Long session stops following the early framework | **New conversation + summary**; on the API, compaction (C3, C1.5) | Repeat the instructions; switch to Opus |
| Fabricated citations or URLs | NTP + Knowledge → **verify specifics / ground in sources** (C1.7) | Lower temperature |
| Model agrees with a wrong premise | Knowledge + Steerability → **invite pushback** (C1.7) | Longer prompt |
| Literal but useless output ("make it shorter") | **Restate the goal** (C1.6) | Repeat the instruction more forcefully |
| Tests pass, users unhappy | **Description chain**, upstream link (C2.4) | Re-prompt the code |
| Works in dev, breaks under load | **Lens 2, production readiness**: concurrency, scale (C2.5) | Lens 1 unit tests |
| `TypeError` reading the reply | `response.content` **is a list of blocks** (C4.2) | Model choice |
| Tool exists but is never or wrongly called | **Tool description** (C4.5) | Switch model |
| Agent loop errors after a tool call | Every `tool_use` id → a **`tool_result`** in the **next user message**; assistant content appended (C4.4) | Raise `max_tokens` |
| 400 on a thinking request | `budget_tokens` on a new model, or `effort` outside **`output_config`** (C4.6) | Retry |
| MCP connector validation error | Missing **`mcp_toolset`** / name mismatch / **beta header** (C4.9) | Rewrite the server |
| Compaction "lost" state | **Append the full `response.content`** (C4.10) | Bigger window |
| Cache reads always 0 | Changing prefix bytes; on Vertex/Bedrock, **regional availability** (C4.10, C9.2) | More breakpoints |
| Managed-agent session shows no early events | **Open the stream before `events.send`** (C4.12) | Recreate the agent |
| Lots of rework after Claude Code edits | **Plan mode + success criteria + tests** (C5.4) | Auto-accept |
| Context full of unrelated tool definitions | **Disable unused MCP servers**, use a CLI or Skill (C5.5, C5.9) | `/clear` mid-feature |
| Starting a new feature in an old session | **`/clear`** (C5.5) | `/compact` |
| New teammate lacks the team's MCP servers | **Project scope `.mcp.json`** (C5.9) | Local scope |
| Formatter or guard runs only sometimes | **Hook** (PostToolUse / PreToolUse) (C5.10) | More CLAUDE.md text |
| PreToolUse guard doesn't block | **Exit code 2 + stderr** (C5.10) | Exit 1 |
| Claude can't see an MCP server's tools in your app | **ListTools fetched and passed in `tools`** (C6.2) | CallTool |
| Claude makes tool calls to read a doc the user already picked | Make it a **resource** (app-controlled) (C6.6, C6.8) | Another tool |
| Subagent runs forever or returns mush | **Output format** in its system prompt (C7.3) | Bigger model |
| Subagent never triggers | **Description** ("proactively", examples) (C7.2–C7.3) | Rename the file |
| Test-runner subagent hides failures | **Run tests in the main thread** (C7.4) | Better summary prompt |
| "We have Claude" but no Claude Code | **Seat type** (Standard vs Chat + Code) (C8.3) | Reinstall |
| Data must stay in the client's AWS regions | **Bedrock + gateway** (C8.3, C9.1) | Enterprise; Foundry |
| CISO asks for ZDR on a cloud path | **ZDR is Enterprise direct only**; provider retention applies (C9.1, C9.5) | "Applies everywhere" |
| Week-2 "WebSearch is broken" on Bedrock | **Known gap → approved MCP alternative** (C9.2) | Support ticket; personal accounts |
| CoE dashboard empty on Bedrock | **Telemetry off by default → OTel or gateway** (C9.2) | Anthropic Console |
| 40 terminals hang on Day 1 | **Proxy / TLS inspection** → `HTTPS_PROXY` via MDM (C9.3) | Reinstall |
| "Self-signed certificate in chain" | **`NODE_EXTRA_CA_CERTS`** (corporate root) (C9.3) | `NODE_TLS_REJECT_UNAUTHORIZED=0` |
| WebFetch fails on Bedrock, chat works | **`api.anthropic.com` preflight blocked** (C9.3) | Model access |
| Features missing only behind the gateway | **Forward `anthropic-beta` / `anthropic-version`** (C9.4) | File a product bug |
| Need cost per team | **Gateway + `X-Claude-Code-*` headers** (C9.4) | Proxy logs |
| ZDR + Claude Code on the web requested | **They conflict; choose** (C9.5) | "Both, standard" |
| Flat metrics despite high usage | **Use case too marginal** (C10.1, C10.6) | More training |
| Day 16: flat PR time, steady usage | **Plateau → Code 201** (C10.4) | Daily stand-ups; "too early" |
| Week-1 velocity dip | **Expected calibration**; don't intervene (C10.4) | Extra training |
| Adoption collapses after you leave | **Champion + CLAUDE.md + commands** (C10.5, C10.6) | Longer engagement |

---

# Headers, identifiers and numbers to memorize

**Claude API (confirm at build time)**
- Request: `model`, `max_tokens`, `messages`, `system`, `tools`. Reply: `response.content` (list of blocks), `response.usage` (input/output tokens), `stop_reason` (`end_turn`, `tool_use`, `max_tokens`, `refusal`, `pause_turn`).
- Thinking: `thinking={"type": "adaptive"}` · `output_config={"effort": ...}` with low / medium / high (default on most models) / xhigh / max.
- Server tools: `web_search_20260209` · `web_fetch_20260209` · `code_execution_20260120` (course) / `code_execution_20260521` (current) · result blocks `server_tool_use`, `bash_code_execution_tool_result`.
- Client tools: memory `memory_20250818` · bash.
- Skills: `container={"skills": [{"type": "custom", "skill_id": ..., "version": "latest"}]}` · course beta `skills-2025-10-02` (Skills API now GA) · `code-execution-2025-08-25`.
- MCP connector: `mcp_servers=[{"type": "url", "url", "name", "authorization_token"}]` + `{"type": "mcp_toolset", "mcp_server_name"}` · beta `mcp-client-2025-11-20` · scoping with `default_config` / `configs`.
- Compaction: `context_management={"edits": [...]}` · current `compact_20260112` + beta `compact-2026-01-12` · trigger around 150K by default. Context editing: `clear_tool_uses_20250919`.
- Caching: `cache_control: {"type": "ephemeral"}`; order tools → system → messages; check `usage.cache_read_input_tokens`.
- Managed agents: `client.beta.agents / environments / sessions`, `sessions.events.stream / send` · toolset `agent_toolset_20260401` · events `user.message`, `agent.message`, `agent.tool_use`, `session.status_idle` · networking `unrestricted` / `limited` · beta `managed-agents-2026-04-01`.
- Tool runner: `client.beta.messages.tool_runner` + `@beta_tool` → `until_done()` (Python) · `client.beta.messages.toolRunner` + `betaZodTool` (TypeScript).
- Model IDs in the course: `claude-haiku-4-5` (200K), `claude-sonnet-4-5`, `claude-sonnet-4-6` (1M), `claude-opus-4-7`, `claude-opus-4-8` (1M). Current per skill: `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-fable-5-1`.

**Claude Code**
- Modes: default / auto-accept / plan (**Shift+Tab**).
- Commands: `/compact` · `/clear` · `/context` · `/init` · `/agents` · `/mcp` · `/hooks` · `/status` · `/commit-push-pr` · `/claude-api` · `claude --from-pr <N>` · `claude mcp add`.
- Files: `CLAUDE.md` (project root / user config), `.claude/agents/<name>.md`, `.mcp.json`, `.claude/settings.json`, `managed-settings.json`.
- Hooks: PreToolUse · PostToolUse · UserPromptSubmit · Stop · Notification · exit **0** proceed / **2** block (stderr goes to Claude) / other = non-blocking · `CLAUDE_PROJECT_DIR` · matcher `Edit|MultiEdit|Write`.
- MCP scopes: local / user / project. Tool search above **10%** of context.
- Subagent frontmatter: `name`, `description` (single line; "proactively"), `tools`, `model` (`sonnet` / `opus` / `haiku` / `inherit`), `color`, `skills`.

**Network and gateway**
- `HTTPS_PROXY`, `HTTP_PROXY`, `NO_PROXY` · `NODE_EXTRA_CA_CERTS` · `CLAUDE_CODE_CERT_STORE` · `CLAUDE_CODE_CLIENT_CERT` / `_KEY`.
- `ANTHROPIC_BASE_URL` · `ANTHROPIC_AUTH_TOKEN` · `CLAUDE_CODE_USE_BEDROCK` / `_VERTEX` · `ANTHROPIC_BEDROCK_BASE_URL` / `ANTHROPIC_VERTEX_BASE_URL` · `CLAUDE_CODE_SKIP_BEDROCK_AUTH` / `_VERTEX_AUTH` · `apiKeyHelper`.
- Headers: `anthropic-beta`, `anthropic-version` (must pass through) · `X-Claude-Code-Session-Id`, `X-Claude-Code-Agent-Id`, `X-Claude-Code-Parent-Agent-Id`.
- Domains: `api.anthropic.com`, `claude.ai`, `platform.claude.com`, `downloads.claude.ai`, `trust.anthropic.com`.
- LiteLLM **1.82.7 / 1.82.8** compromised.

**MCP (Python SDK)**
- `FastMCP`, `@mcp.tool`, `@mcp.resource`, `@mcp.prompt`, `Field`, `base.UserMessage`, `ClientSession`, `list_tools` / `call_tool` / `read_resource` / `list_prompts` / `get_prompt`.
- `mcp dev mcp_server.py` (Inspector at 127.0.0.1:6274).
- ListTools / CallTool / ReadResource request/result pairs.
- Tools = model · resources = app · prompts = user.

**Numbers**
- 4 decisions · 4 layers · Project when 2 of 3 · payback in 2–3 sessions · Memory review monthly.
- C1: 4 properties · Lost in the Middle drop 30%+ · 1,024-dim embeddings · Markov 1906 / transformers 2017.
- C2: 6 toolkit stages · 5 lenses · 4 UX principles · 1 in 5 people with a disability.
- C4: model eval with 20–30 examples.
- C8: Opus-for-everyone ≈ +65% cost · 7 paths / 3 categories · Haiku 200k, Sonnet and Opus 1M.
- C9: pre-kickoff Day −14 → 0 · Vertex approval 24–48 h · ZDR flagged retention up to 2 years · 30-day transcript default (confirm).
- C10:
  - Mode 1 = 2 days; Mode 2 = 30–45 days; midpoint Day 20–25.
  - Cohort 8–10; two ticket-to-merge cycles; 25–30 days.
  - Baselines: 3; metric categories: 4; failure modes: 6; close-out artifacts: 4.
  - Champion by Day 15; CoE touchpoints Day 8 and Day 15 (30 min); office hours 60 min, first on Day 3–4; champion runs them from session 3.
  - Readout 48 h before the showcase; showcase 30 min = 10/10/10; ≥ half the cohort past supervised mode; command catalogue ≥ 3–5.

---

# API drift: course shape vs current API (claude-api skill, cached 2026-10-06; confirm at build time)

| Area | Course shows | Current |
|---|---|---|
| Sampling | Explained conceptually (C1) | `temperature` / `top_p` / `top_k` return **400** on Opus 4.7+ and the newer families; the skill notes they 400 on every model from API version 2026-10-21. Steer through prompting and `effort` |
| Thinking | `thinking={"type": "adaptive"}` + `output_config.effort` | Same shape. `budget_tokens` → 400 on 4.7+. On Opus 4.7/4.8, **omitting `thinking` = no thinking**. On Opus 5.5, thinking can't be disabled and **default effort is `medium`**. `display` defaults to `"omitted"` |
| Forced tool use | Not covered | `tool_choice` `any` / `tool` → **400** on Opus 5.5, Sonnet 5.5, Fable 5.1; use `auto` + `strict: true` or structured outputs |
| Code execution | `code_execution_20260120` / `_20250825` | `code_execution_20260521` (result `bash_code_execution_tool_result`); `_20260120` still exists for REPL persistence and programmatic tool calling |
| Web search / fetch | `web_search_20260209` | Same (dynamic filtering); don't also declare `code_execution`; on Vertex only `web_search_20250305` |
| Skills | `client.beta.skills.create` + beta `skills-2025-10-02` | **Skills API is GA**: `client.skills.*`, no skills beta header; attaching still uses `client.beta.messages.create` + `container.skills` + `code-execution-2025-08-25` |
| Compaction | `{"type": "compact"}` on `messages.create` | `client.beta.messages.create`, beta `compact-2026-01-12`, edit type `compact_20260112`; append the full `response.content` |
| Tool runner (TS) | Plain functions passed to `toolRunner` | Wrap tools with `betaZodTool({...})`; Python uses `@beta_tool` + `until_done()` |
| MCP connector | `mcp_servers` + `mcp_toolset` + `mcp-client-2025-11-20` | Same; both halves are required |
| Managed agents | agents / environments / sessions / events | Same shapes; beta `managed-agents-2026-04-01` set by the SDK; vault credentials for secrets; sync agents with `ant apply` |
| Models | Haiku 4.5, Sonnet 4.5/4.6, Opus 4.7/4.8, Fable | Default `claude-opus-5-5` ($4 / $20 per MTok); Sonnet 5.5, Haiku 5.5, Fable 5.1 exist |

---
<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/00-platform-model-foundations-notes|Foundations notes]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/02-commute-recall|Commute recall]] ➡️
<!-- nav:end -->
