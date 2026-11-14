# Commute Recall Cards: Claude Architect Exam

<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/01-full-study-notes|Full study notes]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/03-practice-exams|Practice exams]] ➡️
<!-- nav:end -->


Short and phone-friendly. Read one block per stop.

---

## The 2 ideas behind every course
- **Right thing, right layer**: prompt vs Skill vs hook vs tool vs MCP vs subagent · proxy vs gateway · Enterprise vs cloud path.
- **Decide and measure before Day 1**: path, gap memo, baseline, champion.

---

## C1: AI Capabilities & Limitations

**Four properties, each a continuum**
- **Next Token Prediction**: fluency AND hallucination; fabrication clusters in **specifics**
- **Knowledge**: frozen at the cutoff; staleness · uneven coverage · bias · source amnesia
- **Working Memory**: a **cliff**, not a gradient; lost in the middle (30%+ drop)
- **Steerability**: pattern-following; drift · letter over spirit · prompt injection

**Collisions → fix**
- NTP + Knowledge = fake citations → **verify / ground**
- Memory + Steer = long-chat drift → **re-supply / restart**
- NTP + Steer = confident wrong reasoning → **visible reasoning / code**
- NTP + Memory = poisoned context → **curate input**
- Knowledge + Steer = agreeable bad premise → **invite pushback**
- Knowledge + Memory = stale doc vs training → **say which source wins**

**Training fingerprints**: sycophancy · verbosity · over-caution · loose confidence

**Sampling**: temperature · top-k (fixed count) · top-p (adapts to confidence)

---

## C2: AI Fluency for Builders
- **4Ds**: Delegation · Description · Discernment · Diligence
- **Inner loop** = Description + Discernment · **outer loop** = Delegation + Diligence
- **Implementation safe to delegate, judgment isn't**
- Toolkit: Empathy weak · Design mid · Arch mid · **Impl strong** · **Judgment weak** · Ship mid
- Modes: **Automation** (AI does, you check) · **Augmentation** (together) · **Agency** (latitude in bounds)
- **Description chain**: user voice → requirement → spec → AI instruction → tests
- Code works, product doesn't → **description failure**
- **5 lenses**: works? · works well? · right thing? · good? · responsible?
- **4 UX principles**: clarity · hierarchy · accessibility (1 in 5) · feedback
- Ship vocabulary AI won't raise: migrations · versioning · rate limits · feature flags

---

## C3: Platform & Model Foundations (foundational)
- **4 decisions**: entry point · capability layer · model · context
- **Project** if 2 of 3: recurs · stable background · same format
- **Instructions = what to do · knowledge base = what to know**
- **Skills**: account level, auto-invoked, still vary · **Code Execution**: numbers must be right
- **Memory**: curate monthly · **Project-scoped** for clients · Incognito ≠ org retention
- **Haiku** volume · **Sonnet** default · **Opus** ambiguity and high stakes
- **Drift** → new chat + summary (not Opus, not repeating instructions)

---

## C4: Claude Platform 101

**Request basics**
- Required: `model` · `max_tokens` · `messages` (+ `system`)
- `response.content` = **list of blocks** · `response.usage` = what you're billed on
- Model eval: **20–30 examples**, climb from Haiku, **cheapest you'd ship**

**Agent loop**
- send with tools → `tool_use` → **your code runs it** → `tool_result` (matching `tool_use_id`) → until **`end_turn`**
- "You own the loop and tools; Claude owns the reasoning"
- Vague tool **description** = #1 misfire cause

**Thinking**
- `thinking={"type": "adaptive"}` + `output_config={"effort": ...}`
- Effort goes **inside output_config**
- Use for math, debugging, trade-offs; skip for classification and extraction

**Built-in tools**
- **Server tools** (Anthropic runs them, no loop): web search · code execution · web fetch
- **Client tools** (you run them, SDK schema): memory · bash

**Skills / MCP**
- **Skills** = how (SKILL.md, progressive loading, `container.skills` list)
- **MCP** = third party maintains it; `mcp_servers` + **`mcp_toolset`** + beta header
- "Tools = your stuff · Skills = your process · MCP = everyone else's stuff"

**Context patterns**
- just-in-time (a **design pattern**) · compaction · caching · memory tool (**you own storage**)

**Managed agents**
- **Agent → Environment → Session → Events**
- **Open the stream BEFORE sending the kickoff**
- `agent.message` · `agent.tool_use` · `session.status_idle`
- Graders in a separate context · permission policy = human approval

---

## C5: Claude Code 101

**Modes** (Shift+Tab)
- default (asks everything) · auto-accept (edits auto, **commands still ask**) · plan (read-only)

**Workflow**: **Explore → Plan → Code → Commit**
- Correct course in the plan, before any code
- Success criteria + tests + reviewer subagent

**Context**
- `/compact` = same feature · `/clear` = new feature · `/context` = see usage
- Vague prompt = MORE context · MCP loads all tool definitions · CLI is leaner

**CLAUDE.md**
- Root, read every session, **appended to the prompt**
- Project vs user level · `@path` refs · start without one · `/init`

**MCP scopes**
- local · user · **project = `.mcp.json`** · tool search above 10%

**Hooks** (deterministic)
- PreToolUse · PostToolUse · UserPromptSubmit · Stop · Notification
- **exit 2 = block + stderr to Claude** · exit 0 = proceed · other = non-blocking
- `.claude/settings.json` · `CLAUDE_PROJECT_DIR`

**Git**: `/commit-push-pr` · `claude --from-pr <N>`

---

## C6: Intro to MCP
- Client (in your server) ↔ servers exposing **tools · resources · prompts**
- Transport-agnostic; default **stdio**
- **ListTools / CallTool / ReadResource** request ↔ result pairs
- `FastMCP` + `@mcp.tool` + `Field(description=...)` → no hand-written schema
- Inspector: `mcp dev mcp_server.py`
- Resources: **direct** (static URI) vs **templated** `{doc_id}`; `mime_type`
- **Tools = model · Resources = app · Prompts = user**
- "MCP vs tool use?" Complementary: MCP = who wrote the tool

---

## C7: Subagents
- Own context window · returns a **summary** · conversation discarded
- Gets: **its system prompt + a task written by the parent**
- Built-ins: general-purpose · **Explore** · **Plan**
- File: `.claude/agents/<name>.md` · single-line `description` · `model: inherit` option
- "**proactively**" in description = auto-delegation
- **4 design fixes**: specific description · **output format** (#1) · obstacle report · limited tools
- Tools: research = Glob/Grep/Read · reviewer = + Bash, no Edit/Write
- **Use**: research, reviews, custom system prompt
- **Avoid**: "expert" personas · dependent pipelines · test runners
- Rule: **does the intermediate work matter?**

---

## C8: Product Foundations
- Loop: **Observe → Plan → Act → Verify**; logged = safe to authorize
- Same agent on every surface; **Desktop/Web/Mobile = scoped access**
- **Sonnet default**, Opus for overnight autonomy, Haiku for volume/sub-agents
- **Try effort before a bigger model** (xhigh on Opus 4.8)
- 7 paths / 3 categories: **Claude-managed** (default) · **cloud-native** (commitments, residency) · **API/Console** (single dev)
- **Enterprise = controls tier**: SSO + domain capture, SCIM, RBAC, Compliance API, managed settings
- Seats: **Standard = no Claude Code** · Chat + Code = minimum · Enterprise = full
- Intune = endpoint distribution, not architecture

---

## C9: Deployment Architecture

**Path decision**
- Decided **pre-kickoff, Day −14..0**; a one-way door
- Ask in order: **commitments (EDP/CUD/MACC) → buying route → compliance → admin ownership**
- **ZDR & web surface = Enterprise direct only**
- **Foundry → Anthropic-operated infrastructure** (Bedrock and Vertex stay in-tenancy)
- **Vertex**: Model Garden 24–48 h → file on Day 1

**Gap memo** (before signature)
- Bedrock: no WebSearch
- Cloud paths: no web · no Anthropic ZDR · **you pin models** · **telemetry off** (`/feedback` local)
- Vertex: MCP tool search off · caching varies by region

**Proxy**
- `HTTPS_PROXY` / `NO_PROXY` **via MDM** · no SOCKS · NTLM/Kerberos → gateway
- TLS inspection → **`NODE_EXTRA_CA_CERTS`**, never disable verification
- Allowlist: `api.anthropic.com` (incl. WebFetch preflight) · `claude.ai` · `platform.claude.com` · `downloads.claude.ai`
- `managed-settings.json` = top of the hierarchy; server (Enterprise) / MDM / file

**Gateway**
- auth · attribution · **budget enforcement** · routing · audit
- `ANTHROPIC_BASE_URL` + token · `CLAUDE_CODE_USE_BEDROCK` + `ANTHROPIC_BEDROCK_BASE_URL` + `CLAUDE_CODE_SKIP_BEDROCK_AUTH`
- **Must forward `anthropic-beta` / `anthropic-version`**
- `X-Claude-Code-Session-Id` / `-Agent-Id` / `-Parent-Agent-Id`
- LiteLLM 1.82.7/1.82.8 compromised

**Compliance**
- Training: "**no, unless you opt in**" · local plaintext transcripts
- ZDR: per org, eligibility review; disables web, remote sessions, `/feedback`; flagged sessions kept up to 2 y
- Certs **self-serve at trust.anthropic.com**

---

## C10: Delivery Methodology
- **Structural** (unit of work changes) beats **marginal**
- Mode 1 (2-day) = adoption only · **Mode 2 (30–45 d) = ROI**
- Criteria: volume · complexity · **measurability (non-negotiable)** · readiness
- Cohort = **owners, not enthusiasts** (8–10) · ≥2 ticket-to-merge cycles · lock scope
- Criterion: "[metric] by [threshold] vs Day 1 baseline by [date]"
- Baseline **before kickoff**; after = contaminated
- 4 metric families: productivity · quality · adoption · sentiment
- **Headline: PR cycle time**, scoped translation (not "34% more productive", not lines of code)
- Curve: supervised (wk 1, dip) → autonomy (wk 2–3) → agentic (wk 3–4) → institutionalized
- **Plateau ≠ adoption** → Code 201 + peer demo
- Champion: influence + motivation; CLAUDE.md + **3–5 commands** + escalation path; **by Day 15**
- 6 failures: no baseline · no champion · marginal use case · supervised stagnation · stale CLAUDE.md · no business translation
- Arc: CoE touchpoints Day 8 & 15 · office hours Day 3–4 (champion runs from session 3) · readout **48 h before** · showcase 10/10/10 · **sponsor in the room or reschedule**

---

## Numbers flash list
- **2 of 3** → build a Project · payback **2–3 sessions** · Memory review **monthly**
- Lost in the Middle **30%+** · embeddings **1,024** dims · 1 in **5** people with a disability
- Model eval **20–30** examples · Haiku 4.5 **200k** · Sonnet 4.6 / Opus 4.8 **1M**
- Opus for everyone ≈ **+65%** cost
- **7** paths · **3** categories · **4** cloud decision drivers · **6** parity gaps
- Pre-kickoff **Day −14 → 0** · Vertex approval **24–48 h**
- MCP tool search above **10%** of context
- Hook exit **2** blocks
- ZDR flagged retention up to **2 years** · transcripts **30 days** default (confirm)
- LiteLLM **1.82.7 / 1.82.8** compromised
- Mode 1 = **2 days** · Mode 2 = **30–45 days** · midpoint **Day 20–25**
- Cohort **8–10** · pilot **25–30** days · **≥2** cycles
- **3** baselines · **4** metric families · **6** failure modes · **4** close-out artifacts
- Champion **by Day 15** · CoE touchpoints **Day 8 / 15** (30 min) · office hours **60 min**, first **Day 3–4**
- Readout **48 h** before the showcase · showcase **30 min** (10/10/10) · **≥½** of the cohort past supervised mode
- Command catalogue **≥3–5**

*Version-pinned facts (model IDs, prices, beta headers, limits, retention windows): confirm at build time.*

---
<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/01-full-study-notes|Full study notes]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[claude-architect-exam-prep/03-practice-exams|Practice exams]] ➡️
<!-- nav:end -->
