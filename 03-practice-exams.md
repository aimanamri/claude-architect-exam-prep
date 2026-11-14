# Claude Certified Architect – Foundations: Practice Exams

<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/02-commute-recall|Commute recall]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[Claude Certifications|Home]] ➡️
<!-- nav:end -->


Four sets of scenario questions. Sets A and B have 32 each; Sets C and D have 30 each.

**Sets A and B (standard).** Written in the course's style: "it worked in dev, broke in prod; pick the targeted fix." Each covers all ten courses, including the foundational C3:
- Q1–2: **C1** AI Capabilities & Limitations
- Q3–4: **C2** AI Fluency for Builders
- Q5–8: **C3** Platform & Model Foundations (foundational)
- Q9–14: **C4** Claude Platform 101
- Q15–19: **C5** Claude Code 101
- Q20–22: **C6** Introduction to MCP
- Q23–25: **C7** Introduction to subagents
- Q26–27: **C8** Product Foundations
- Q28–30: **C9** Deployment Architecture
- Q31–32: **C10** Delivery Methodology

**Sets C and D (advanced, certification style).** Harder, in the way vendor certification exams are built:
- longer scenarios with irrelevant detail;
- **two or more plausible answers**, where you pick the *BEST*, *FIRST*, *MOST* or *LEAST*;
- **NOT** stems;
- **"Choose TWO"** items (all-or-nothing scoring);
- **ordering** items.

Coverage for Sets C and D:
- Q1–3: **C3** (foundational)
- Q4–5: **C1**
- Q6–7: **C2**
- Q8–12: **C4**
- Q13–16: **C5**
- Q17–18: **C6**
- Q19–21: **C7**
- Q22–23: **C8**
- Q24–27: **C9**
- Q28–30: **C10**

Unless a question says "Choose TWO", pick ONE answer. **All answers and reasoning are at the end of the file.** Time yourself: about 60 s per question for Sets A/B and 90 s for Sets C/D.

> Habits Sets C/D train:
> 1. Find the **constraint word** (*FIRST, BEST, MOST, LEAST, NOT*).
> 2. Drop answers that are **true but don't address the stated symptom**.
> 3. Prefer the **structural fix in the right layer** (Project, Code Execution, hook, gateway, seat type, baseline) over "add more prompt text" or "use a bigger model".
> 4. When two answers both work, pick the one the course names as the **default or first step**.
> 5. Ignore scenario detail that doesn't change the decision (IDE brand, office location, Intune).

*Version-pinned facts (model IDs, tool type strings, beta headers, prices, retention windows): confirm at build time. Questions test the course's concepts, not exact version numbers.*

---

# SET A

**A1.** A research assistant built on Claude produces a literature summary that cites three studies, with authors, journals and DOIs. A reviewer finds two of the studies don't exist. Which diagnosis and fix match the course?
- A. Working Memory + Steerability; restart the conversation with the essentials up front
- B. Steerability alone; add "only cite real studies" to the prompt and repeat it
- C. Next Token Prediction + Knowledge; verify the specifics independently or ground the answer in retrieved sources
- D. Knowledge alone; set temperature to 0

**A2.** An analyst pastes a 60-page policy and asks about a rule on page 31. Claude handles the rules on pages 1 and 60 correctly but misses the page-31 rule. What is the best fix?
- A. Send only the relevant sections, put the critical rule first, and restate it near the end
- B. Paste the whole document twice
- C. Add "read the document carefully" to the prompt
- D. Switch to a model with a larger context window and change nothing else

**A3.** The clinic wait-time app passes every acceptance test the team wrote. In the demo, a "patient" with a phone and ten minutes can't find the current wait time. Where does the course tell the builder to look?
- A. Rewrite the coding prompt with more implementation detail
- B. Lens 1 (functional integrity): add more unit tests
- C. Switch the build to the "agency" collaboration mode
- D. Up the Description Chain: the requirement/spec link didn't capture the user's real need

**A4.** Which delegation does the course call "usually safe"?
- A. Deciding which features are worth shipping
- B. Implementation: writing, debugging and iterating on code
- C. Understanding which patients the clinic serves
- D. Deciding whether the product is good enough to launch

**A5.** Every Monday a coordinator opens a new Chat, pastes the same team background, stakeholder list and report format, then adds the week's updates. Output quality is fine, but 12 of the 40 minutes go on setup. What is the targeted change?
- A. Build a Project: background in the knowledge base, report format in the standing instructions
- B. Switch to Opus
- C. Turn on Research
- D. Save each week's report as an Artifact

**A6.** A monthly finance summary includes month-over-month percentage changes that Claude wrote in prose. Two were wrong. What is the targeted fix?
- A. Add "verify all arithmetic" to the instructions
- B. Move the workflow to Opus
- C. Upload last month's report to the knowledge base
- D. Use Code Execution for the calculations

**A7.** A consultant notices details from Client A's sessions appearing in work for Client B. What configuration does the course recommend?
- A. Use Incognito for every session
- B. Clear Memory manually before switching clients
- C. Separate Projects per client, with Project-scoped Memory
- D. A different model tier for each client

**A8.** Two hours into one session, Claude stops applying the analytical framework the user defined at the start. What does the course recommend?
- A. Paste the framework again into the same conversation
- B. Start a new conversation seeded with a summary of decisions, work in progress and open questions
- C. Switch to Opus to restore quality
- D. Turn on Research for more context

**A9.** A developer's endpoint returns `str(response.content)` to the UI, and users see something like `[TextBlock(text=...)]`. What is the fix?
- A. Raise `max_tokens`
- B. Iterate over `response.content` and join `block.text` for blocks whose `type` is `"text"`
- C. Add "reply in plain text only" to the system prompt
- D. Switch the call to streaming

**A10.** An agent worked in testing with one tool. In production it has `search_docs`, `search_tickets` and `search_customers`, and it keeps calling `search_docs` for ticket questions. What should you fix FIRST?
- A. Switch to Opus
- B. Merge the three tools into one generic search tool
- C. Rewrite each tool's `description` to say exactly what it searches, what it returns and when to use it
- D. Lower `max_tokens` so Claude decides faster

**A11.** A hand-written agent loop gets a 400 on the request after the first tool call: the API says a `tool_use` block has no matching `tool_result`. What is the fix?
- A. Append the assistant's full `response.content`, then a user message containing a `tool_result` (with the matching `tool_use_id`) for every `tool_use` block
- B. Retry the same request with exponential backoff
- C. Increase `max_tokens`
- D. Remove the `tools` parameter on the second request

**A12.** A team adds `thinking={"type": "adaptive", "effort": "high"}` to an Opus 4.7 request and gets a validation error. What is the correct shape?
- A. Replace it with `thinking={"type": "enabled", "budget_tokens": 8000}`
- B. Remove thinking and add "think step by step" to the prompt
- C. Set `temperature=0` alongside thinking
- D. Keep `thinking={"type": "adaptive"}` and pass `output_config={"effort": "high"}`

**A13.** A team adds the web search tool and writes loop code that waits for `stop_reason == "tool_use"` so it can run the search itself. The branch never fires, yet answers include citations. Why?
- A. Web search needs a beta header before it returns `tool_use`
- B. Web search only runs when `tool_choice` forces it
- C. Web search needs an `input_schema` before Claude can call it
- D. Web search is a server tool: Anthropic runs it and the result arrives in the same response (`server_tool_use` plus result blocks), so no client loop is involved

**A14.** A request with `mcp_servers=[{"type": "url", "url": "...", "name": "linear"}]` is rejected as invalid. What is missing?
- A. A `tools` entry `{"type": "mcp_toolset", "mcp_server_name": "linear"}`, plus the MCP-client beta header
- B. An `input_schema` for every Linear tool
- C. Running the Linear server locally over stdio
- D. Putting the server URL inside the `system` prompt

**A15.** A developer wants Claude Code to apply file edits without asking but still ask before running any shell command. Which mode?
- A. Plan mode
- B. Auto-accept mode
- C. Default (approval) mode
- D. Skipping permissions entirely

**A16.** A team's CLAUDE.md says "Run Prettier after every edit." Most sessions comply, but some commits arrive unformatted. What is the targeted fix?
- A. Put the CLAUDE.md line in bold capitals
- B. Remind Claude in every prompt
- C. Add a PostToolUse hook with matcher `Edit|MultiEdit|Write` that runs the formatter
- D. Create a formatting subagent

**A17.** A PreToolUse hook meant to block `rm -rf` prints a warning, but the command still runs. The script ends with `exit 1`. What should change?
- A. Exit 0 so Claude sees success
- B. Print the reason to stdout
- C. Exit 2 and write the reason to stderr, so the action is blocked and Claude gets the feedback
- D. Move the hook to PostToolUse

**A18.** A new hire's Claude Code doesn't have the Linear MCP server everyone else uses. What setup fixes this for every future hire?
- A. Each developer adds it at user scope
- B. Add it at project scope in `.mcp.json` and commit the file
- C. Add it at local scope on the team lead's machine
- D. Describe the server in CLAUDE.md

**A19.** After a long session on the billing feature, a developer starts an unrelated search feature in the same session. Claude keeps applying billing assumptions. Which command fits the course guidance?
- A. `/compact`
- B. `/context`
- C. `/init`
- D. `/clear`, with anything needed across sessions kept in CLAUDE.md

**A20.** Which MCP primitive is user-controlled (triggered by a button, a menu or a slash command)?
- A. Prompts
- B. Tools
- C. Resources
- D. Transports

**A21.** In an MCP-backed CLI, a user picks `@report.pdf` from autocomplete, and Claude then spends a tool call fetching it every time. The team wants the content in the prompt immediately. What should they use?
- A. A templated resource such as `docs://documents/{doc_id}`, which the app reads and injects into the prompt
- B. A second, faster tool
- C. An MCP prompt that tells Claude to call the tool sooner
- D. A larger context window

**A22.** A developer has written a FastMCP server and wants to check the tools without wiring up the full app. What does the course use?
- A. Unit tests only
- B. Install it straight into a production client
- C. Hand-craft `ListToolsRequest` JSON with curl
- D. `mcp dev mcp_server.py` to open the MCP Inspector, then Connect → List Tools → Run Tool

**A23.** A code-review subagent runs for 20 minutes and returns a long, unstructured essay the main agent can't use. What is the single most important fix, according to the course?
- A. Switch it to Opus
- B. Define a structured output format in its system prompt (Summary, Critical, Major, Minor, Recommendations, Approval status)
- C. Give it more tools
- D. Add "be concise" to its `description`

**A24.** A team chains three subagents: reproduce the bug → debug → fix. Fixes keep missing the root cause. What explanation does the course give?
- A. The subagents use the wrong models
- B. The subagents have too few tools
- C. Each step depends on the previous one's discoveries, and information gets lost at every handoff, so keep this work in the main thread
- D. The descriptions lack the word "proactively"

**A25.** A test-runner subagent reports "3 tests failed", and developers then write debug scripts to see why. What is the better design?
- A. Ask the subagent for a longer summary
- B. Run the tests in the main thread so the full output is visible
- C. Give the subagent Edit and Write tools
- D. Run the subagent on Opus

**A26.** A client says "we bought Claude for all 300 developers", but developers can't use Claude Code. What should you check first?
- A. The corporate proxy
- B. Whether the installer was corrupted
- C. The seat type: Standard seats are chat-only; Claude Code needs Chat + Code or Enterprise
- D. Which model is set as default

**A27.** A financial-services client runs on AWS, its policy requires processing inside approved AWS regions, and it wants Claude Code for 200 developers. Which path does the course recommend?
- A. Claude for Enterprise direct
- B. Claude.ai Teams
- C. Anthropic Console with API keys
- D. Amazon Bedrock with an LLM gateway, naming the trade-offs (no web surface, no Enterprise admin features)

**A28.** Day 1 install clinic: all 40 terminals hang on the first prompt. What is the right first move?
- A. Ask the network team whether traffic goes through a proxy and whether TLS inspection is on
- B. Have everyone reinstall
- C. Set `NODE_TLS_REJECT_UNAUTHORIZED=0` to get people working
- D. Point Claude Code at the client's SOCKS5 proxy

**A29.** Behind the client's LLM gateway, some Claude Code features quietly stop working, while the same build works against the direct API. What should you check?
- A. Model version pinning
- B. The gateway's rate limits
- C. Whether telemetry is enabled
- D. Whether the gateway passes the `anthropic-beta` and `anthropic-version` headers through intact

**A30.** A client is deploying on Bedrock. The CISO asks: "Do we get zero data retention?" What is the accurate answer?
- A. "Yes, ZDR covers Claude Code on every path."
- B. "No. ZDR is an Enterprise-direct capability; on Bedrock, retention follows the AWS policies you already control."
- C. "Yes, if you request it from AWS support."
- D. "I'll have to defer that to legal."

**A31.** Which primary metric does the course recommend for a migration pilot?
- A. PR cycle time (ticket to merge) for the migration tasks, with the baseline captured before Day 1
- B. Lines of migrated code per week
- C. Developer satisfaction score
- D. Self-reported hours per task

**A32.** Day 16 of a pilot: PR cycle time is flat against baseline, developers use Claude Code about 45 minutes a day, and prompting patterns haven't changed since Week 1. What is the read and the move?
- A. Adoption is failing; end the pilot
- B. It's too early to say; review again at Day 25
- C. A plateau: run a Code 201 session on plan mode and auto-accept for low-risk subtasks
- D. Hold daily stand-ups to monitor usage

---

# SET B

**B1.** A user writes "I think churn is driven by our price increase; confirm with the attached data." The data points elsewhere, but Claude agrees with the user. Which diagnosis and fix?
- A. Next Token Prediction + Working Memory; curate the context
- B. Working Memory alone; restart the conversation
- C. Steerability alone; use code execution
- D. Knowledge + Steerability (an agreeable bad premise); invite pushback: "Tell me if my assumption is wrong"

**B2.** "Make this email more professional" produces a formal email that still buries the actual request. What is the course's fix?
- A. Repeat the instruction in capitals
- B. Restate the goal next to the instruction ("…my goal is that the recipient sees the request in the first line")
- C. Switch to Opus
- D. Ask for it to be shorter

**B3.** Which two competencies form the inner loop of the 4D Framework?
- A. Description and Discernment
- B. Delegation and Diligence
- C. Delegation and Description
- D. Discernment and Diligence

**B4.** An AI-built booking app runs smoothly in development. With 200 concurrent users in production, some appointments are double-booked. Which lens should have caught it?
- A. Lens 1, functional integrity
- B. Lens 3, problem fit
- C. Lens 2, production readiness (concurrency, behaviour under load)
- D. Lens 5, responsible impact

**B5.** In a recurring contract-review Project, where do the contract documents for the current cycle (uploaded at the start of each session) belong?
- A. Standing instructions
- B. A Skill
- C. The knowledge base
- D. Code Execution

**B6.** Which statement about Projects is accurate?
- A. Every conversation in a Project shares the full context of the others
- B. Conversations in a Project share its standing instructions and knowledge base, but not context with each other
- C. Skills live inside a Project and only run there
- D. Projects turn off Memory

**B7.** A legal team must classify 500 standard vendor agreements as low, medium or high risk against a clear, unambiguous rubric, in one session. Which model?
- A. Haiku
- B. Opus
- C. Sonnet, because it's always the default
- D. Whichever model the plan defaults to

**B8.** Members of a Team-plan workspace can't find the web search toggle in Chat. What is the likely cause?
- A. They need a Research subscription
- B. The default model doesn't support search
- C. Incognito is on
- D. An Owner or Primary Owner hasn't enabled web search in the organization's capability settings

**B9.** A team is choosing a model for a new extraction feature. What process does the course recommend?
- A. Build a 20–30 example eval from the real workload, run it from Haiku upward, and stop at the cheapest model whose output you'd ship
- B. Start on Opus and step down if it costs too much
- C. Always use Sonnet
- D. Choose from a public benchmark leaderboard

**B10.** A team wants Claude to call three of its own Python functions in a loop. The functions must run on the team's servers, and the team doesn't want to hand-write JSON schemas or the loop. Which option fits?
- A. Managed agents
- B. Wrap the functions as an MCP server
- C. Server tools
- D. The SDK's tool runner

**B11.** An operations dashboard sends every document to Opus: classification, client-update drafts and RFP responses. The bill is high. What is the course's pattern?
- A. Move everything to Haiku
- B. Route per task within the endpoint: classify with Haiku, draft updates with Sonnet, write RFP responses with Opus
- C. Cache the prompts and keep Opus everywhere
- D. Use the Batches API for everything

**B12.** A chat app turns on server-side compaction. After a few turns the earlier context is simply gone, because the app appends only the reply's text string to its history. What is the fix?
- A. Raise the compaction trigger
- B. Switch to context editing (`clear_tool_uses`)
- C. Append the full `response.content`, including the compaction block, to the history
- D. Restart the conversation each time

**B13.** Which of the course's four context-management patterns is a design pattern rather than an API feature?
- A. Server-side compaction
- B. Just-in-time context
- C. Prompt caching
- D. The memory tool

**B14.** A managed-agent integration's logs show the session going idle, but the agent's first messages and tool calls are missing. What is the likely fix?
- A. Create a new agent for every run
- B. Poll the session instead of streaming
- C. Open the event stream before sending the `user.message` kickoff, because the stream only delivers events that happen after it opens
- D. Raise the HTTP timeout

**B15.** In Explore → Plan → Code → Commit, where is course-correcting cheapest?
- A. At commit time
- B. During coding
- C. After the tests run
- D. During plan mode, before any code is written

**B16.** Every session, Claude Code rediscovers the stack and writes API routes, although the team always uses server actions. What is the targeted fix?
- A. Add the stack and the "server actions, not API routes" rule to CLAUDE.md (or ask Claude to save the correction to memory)
- B. A PostToolUse hook that deletes API route files
- C. A subagent that knows the stack
- D. Run `/compact` more often

**B17.** `/context` shows a large share of the window taken by tool definitions from six MCP servers, four of them unrelated to the project. What does the course advise?
- A. Run `/clear`
- B. Switch to a larger-context model
- C. Add more notes to CLAUDE.md
- D. Disable the unused servers with `/mcp`, and prefer CLI equivalents such as `gh` where they exist

**B18.** A team wants every developer to use the same code-reviewer subagent. What does the course recommend?
- A. A project-level subagent with read-only tools, its config committed under `.claude/agents/`
- B. A user-level subagent on each developer's machine
- C. Give the reviewer Edit and Write so it can fix issues
- D. Describe the reviewer in CLAUDE.md

**B19.** Which MCP exchange lets a client discover the tools a server offers?
- A. CallToolRequest / CallToolResult
- B. ReadResourceRequest / ReadResourceResult
- C. ListToolsRequest / ListToolsResult
- D. GetPromptRequest / GetPromptResult

**B20.** A colleague says "MCP is just tool use with extra steps." Which statement matches the course?
- A. They're identical
- B. They're complementary: MCP servers supply ready-made tool schemas and functions, and tool use is how Claude calls tools; the difference is who implemented them
- C. MCP replaces tool use
- D. MCP only handles resources

**B21.** What is the most common transport when the MCP client and server run on the same machine?
- A. WebSockets
- B. HTTP
- C. Standard input/output (stdio)
- D. gRPC

**B22.** A team's custom subagent is never chosen automatically, even for tasks it was built for. What should they change?
- A. Rename the file
- B. Edit the `description`: add "proactively" and concrete trigger examples
- C. Switch its model to Opus
- D. Give it more tools

**B23.** Which tool set suits a research-only subagent?
- A. Glob, Grep, Read
- B. Edit, Write
- C. Bash, Edit
- D. Every tool, for flexibility

**B24.** Which subagent adds the least value, according to the course?
- A. A research subagent that maps where JWT validation happens
- B. A code-review subagent with fresh context
- C. A copywriting subagent with tone and audience instructions
- D. A "You are a Kubernetes expert" subagent

**B25.** A client has no residency requirement, but its security team needs SSO, audit logs and managed settings for 400 developers. Which path?
- A. Claude for Enterprise
- B. Claude.ai Teams
- C. Amazon Bedrock
- D. Anthropic Console

**B26.** Overnight autonomous refactors on Opus 4.8 at default effort fall slightly short on quality. What is the cheaper first lever?
- A. Move to a higher, more expensive model tier
- B. Run Haiku subagents
- C. Raise `max_tokens`
- D. Raise effort (e.g. to `xhigh`) before paying for a higher tier

**B27.** In Week 2 on Bedrock, a champion posts that "WebSearch doesn't work for anyone." What is the best reply?
- A. Open a support ticket and say it's being investigated
- B. Suggest personal claude.ai accounts for lookups
- C. Reply with the gap-memo line (WebSearch isn't available on Bedrock) and link the approved MCP alternative
- D. Ask everyone to reinstall

**B28.** A Vertex AI rollout kicks off in one week and no setup has started. What is the most time-critical item?
- A. Draft the CLAUDE.md
- B. Request Claude access in Model Garden now, since approval can take 24–48 hours
- C. Build the usage dashboard
- D. Choose subagent colors

**B29.** After `HTTPS_PROXY` is configured, Claude Code reports "self-signed certificate in certificate chain." What is the fix?
- A. `NODE_TLS_REJECT_UNAUTHORIZED=0`
- B. `NODE_EXTRA_CA_CERTS` pointing at the corporate root CA
- C. Switch to the SOCKS proxy
- D. Set only `HTTP_PROXY`

**B30.** Finance needs cost per team, including work done by nested subagents. What provides it?
- A. Corporate proxy logs
- B. A developer survey
- C. An LLM gateway that reads `X-Claude-Code-Session-Id`, `X-Claude-Code-Agent-Id` and `X-Claude-Code-Parent-Agent-Id`, with gateway tokens mapped to teams
- D. The Anthropic Console usage page on a Bedrock deployment

**B31.** A CTO offers two pilot use cases: add unit tests to a codebase at 82% coverage, or a Java-to-Spring Boot migration the team has been scoping for eight months. Which qualifies?
- A. Unit tests
- B. Both, in parallel
- C. Neither, because a pilot needs a greenfield project
- D. The migration, because it's structural and meets volume, complexity, measurability and readiness

**B32.** Two days before a pilot readout, which item is a renewal risk?
- A. No champion has been identified by Day 28
- B. Four of 12 developers are still in supervised mode
- C. PR cycle time is 20% better than baseline
- D. Three developers show very high weekly session counts

---
# SET C (advanced)

**C1.** A legal-operations manager at a Lisbon-based logistics firm (Team plan, about 30 seats, mostly Windows laptops) writes a quarterly vendor-risk memo. Each quarter she opens a new Chat, pastes the 40-page vendor policy, retypes the memo format, and asks Claude to compute each vendor's financial exposure from contract penalty rates. Last quarter two exposure figures were wrong and the format drifted from the template. Which change addresses the MOST problems at once?
- A. Move the work to Opus and turn on Research
- B. A Project with the policy in the knowledge base and the format in standing instructions, a Skill for the memo procedure, and Code Execution for the exposure figures
- C. Import the policy into Memory so every chat remembers it
- D. Save each memo as an Artifact so last quarter's version can be reused

**C2.** Which statement about Skills in Claude (claude.ai) is NOT accurate?
- A. A configured Skill reduces output variance but doesn't eliminate it
- B. Built-in Skills cover Excel, Word, PowerPoint and PDF tasks
- C. A third-party Skill should get a trust review, because it can reach whatever Claude can reach in the session
- D. A Skill lives inside one Project and only runs in that Project's conversations

**C3.** (Choose TWO) A consultant on an Enterprise plan handles two competing clients and occasionally does sensitive exploratory work. Which TWO statements are accurate?
- A. Incognito keeps a standalone chat out of Memory and chat history, but it doesn't override the organization's data retention
- B. Importing memories from another AI platform is documented for Enterprise plans
- C. Project-scoped Memory, with one Project per client, keeps each client's context out of the other's sessions
- D. Conversations inside one Project share context with each other, so splitting into Projects is the only isolation needed

**C4.** A firm's brief-drafting assistant writes in a confident tone. A partner finds an invented case citation, complete with docket number. The engineering lead proposes lowering temperature; the practice manager proposes adding "never hallucinate" to the system prompt. Which response is BEST?
- A. Lower the temperature, since it's the cheapest change
- B. Add "never hallucinate" to the system prompt and repeat it at the end
- C. Treat it as Next Token Prediction meeting a Knowledge gap: ground citations in retrieved sources and verify specifics before filing
- D. Switch to a model with a larger context window

**C5.** In a three-hour brainstorming chat, the user set a constraint at the start ("never mention Competitor X"). In hour three Claude mentions Competitor X twice. Which response is LEAST effective?
- A. Repeat the constraint more forcefully in the same thread every few messages
- B. Start a new conversation with the constraint and essentials up front
- C. Put the constraint in standing instructions or a system prompt
- D. Summarize the session's decisions and continue in a fresh conversation

**C6.** Which of these is NOT one of the course's five lenses of discernment for code?
- A. Problem fit
- B. Responsible impact
- C. Production readiness
- D. Cost efficiency

**C7.** A product squad asks an AI tool to "make the order-tracking dashboard look good." The result has generic layout, 9 px labels and color-only status chips, and the squad's designer is on leave. According to the course, what should the squad do FIRST?
- A. Ask again with "make it look much better"
- B. Write a design spec covering hierarchy, accessibility (text labels with color, minimum text size) and feedback states, rebuild against it, then audit the result
- C. Switch to a more capable model
- D. Ship it and gather user feedback

**C8.** A help-desk platform team (Kubernetes, Grafana dashboards, Go services) sends all traffic to Opus 4.8 at default effort: about 50,000 ticket classifications a day plus an occasional legal-response draft. Costs are high and classification latency draws complaints. What should the team do FIRST?
- A. Move everything to Haiku immediately
- B. Turn on adaptive thinking at `xhigh` for every call
- C. Build a small eval (20–30 representative examples per task), run it from Haiku upward, and route each task to the cheapest model that passes
- D. Turn on prompt caching for the system prompt and change nothing else

**C9.** (Choose TWO) Which TWO statements about Anthropic server tools (web search, code execution, web fetch) are accurate?
- A. Your code must execute them and return `tool_result` blocks
- B. Their results arrive in the same response; no client-side agent loop is needed
- C. You handle them by switching on `stop_reason == "tool_use"`
- D. The response contains `server_tool_use` blocks alongside the corresponding result blocks

**C10.** An internal assistant connects to a vendor's Slack MCP server, which exposes about 40 tools. Security wants the agent limited to reading, and the tool definitions are crowding the context. What is the BEST configuration?
- A. In the `mcp_toolset`, set `default_config: {"enabled": False}` and enable only `search_messages` and `list_channels` under `configs`
- B. Add "never post to Slack" to the system prompt
- C. Drop MCP and hand-write two custom Slack tools
- D. Use `tool_choice` to force the search tool on every call

**C11.** Which of these is NOT part of starting a managed-agent run, as taught in the course?
- A. Creating (or reusing) an agent with model, system prompt and toolset
- B. Creating an environment (for example, cloud with a networking config)
- C. Creating a session, then sending and streaming events
- D. Writing a `while` loop that switches on `stop_reason` and returns tool results

**C12.** A PMO wants every project manager's weekly status report to follow identical sections and tone. The reports need data from the company's internal delivery API and from Slack, through the vendor's published server. What is the MOST appropriate mapping?
- A. MCP for all three needs
- B. Custom tools for all three needs
- C. A Skill for the report procedure, a custom tool for the internal API, and MCP for Slack
- D. A Skill for Slack, MCP for the report format, a tool for the internal API

**C13.** At a payments company, a developer turned off permission prompts for speed, and a session overwrote a file in `config/prod/`. Leadership wants writes to that path blocked whatever anyone types or configures personally. What is the BEST control?
- A. A PreToolUse hook that exits 2 for writes under `config/prod/`, in checked-in `.claude/settings.json` (or enforced through managed settings)
- B. A CLAUDE.md line: "Never modify config/prod"
- C. Make plan mode the team default
- D. A reviewer subagent that inspects every diff

**C14.** Which statement about Claude Code permission modes is NOT true?
- A. Plan mode uses read-only tools to build a plan before any change
- B. Auto-accept mode runs shell commands without approval
- C. Default mode asks before editing files and before running shell commands
- D. Shift+Tab cycles through the modes

**C15.** Put the course's recommended workflow for adding WebP conversion to an image pipeline in order:
1. Commit after a subagent code review and a commit message in the team's style
2. Plan mode: decide where conversion happens and whether new dependencies are needed
3. Implement with explicit success criteria and a test suite
4. Explore the relevant upload-pipeline files

- A. 2 → 4 → 3 → 1
- B. 4 → 3 → 2 → 1
- C. 3 → 4 → 2 → 1
- D. 4 → 2 → 3 → 1

**C16.** (Choose TWO) Which TWO practices reduce context consumption in Claude Code, according to the course?
- A. Delegating exploration whose journey doesn't matter to a subagent that returns only a summary
- B. Writing shorter, vaguer prompts
- C. Keeping every configured MCP server enabled so tools are always ready
- D. Disabling unrelated MCP servers, or using CLI equivalents such as `gh`

**C17.** A document app's `@`-mention autocomplete should list every available document as the user types. The MCP server already has a `read_doc_contents` tool and a `format` prompt. What is the MOST appropriate way to populate the list?
- A. Let Claude call a `list_docs` tool whenever the user types `@`
- B. Add an MCP prompt that returns the list
- C. A direct resource (e.g. `docs://documents`, `application/json`) that the app reads with `read_resource`
- D. Have the app send a `CallToolRequest` for `read_doc_contents` on every document

**C18.** A server defines `@mcp.resource("docs://documents/{doc_id}", mime_type="text/plain")` over the handler `def fetch_doc() -> str:`. The Inspector shows an error when the template is used. What is the MOST likely fix?
- A. Change the MIME type to `application/json`
- B. Add a `doc_id: str` parameter, since the SDK passes URI template parameters as keyword arguments
- C. Convert the resource into a tool
- D. Add a `Field(description=...)` to the decorator

**C19.** A review subagent's findings are vague. Its transcript shows the main agent only told it: "use git diff to find the current changes." What is the BEST fix?
- A. Add to the subagent's `description`: "You must tell the agent precisely which files you want it to review"
- B. Give the subagent Edit and Write tools
- C. Switch the subagent to Opus
- D. Remove the subagent and review in the main thread

**C20.** Which proposed subagent is LEAST justified, according to the course?
- A. A copywriting subagent with tone, audience and style instructions
- B. A research subagent to locate where JWT validation happens
- C. A code-review subagent that sees the diff in fresh context
- D. A "senior Python expert" subagent with no other special instructions

**C21.** A subagent discovers that `npm test` only passes with `--runInBand`. Afterwards the main thread spends 15 minutes rediscovering the same flag. Under the course's subagent design guidance, which change fixes this at the source?
- A. Run the subagent on Haiku
- B. Give the subagent more tools
- C. Add an "Obstacles Encountered" section (workarounds, special flags, environment quirks) to the subagent's output format
- D. Set the subagent's model to `inherit`

**C22.** (Choose TWO) Which TWO statements about Claude Code surfaces are accurate?
- A. The IDE extensions are a lighter version with fewer tools than the CLI
- B. Desktop, Web and Mobile reach the filesystem and terminal only when the developer explicitly invokes the agent tooling
- C. Through the Agent SDK, Claude Code's access is whatever the host environment grants (in CI, the runner's access)
- D. Claude Code uses a different model family from Claude.ai

**C23.** A 120-developer fintech has a large GCP Committed Use Discount the CFO wants AI spend to count against, and regulators require processing in a GCP region the firm controls. (Developers use JetBrains; identity is Okta.) Security has also asked about managed settings. Which recommendation is BEST?
- A. Vertex AI with an LLM gateway, plus a written flag of the governance gap versus Enterprise (no web surface, no Compliance API, fewer managed admin features) for security to assess
- B. Claude for Enterprise, because security mentioned managed settings
- C. Claude.ai Teams, to start fast
- D. Anthropic Console API keys per developer

**C24.** On a 30-minute discovery call with a platform lead and a procurement manager, what should you pin down FIRST?
- A. Seat counts and wave-one rollout phasing
- B. IDE standards and repository layout
- C. Whether ZDR is a hard requirement
- D. Whether an EDP, CUD or MACC exists that procurement wants AI spend to count against, and how they prefer to buy

**C25.** Which is NOT a parity gap to put in the memo for a cloud-provider deployment?
- A. No bundled Claude on the web
- B. The Claude Code CLI is a different, reduced build on Bedrock
- C. Telemetry to Anthropic is off by default, so CoE metrics need OTel or a gateway
- D. The client owns model version pinning

**C26.** Halvern Bank, Day 1: terminals hang. Order the actions as the course's simulation resolves it:
1. Send security the allowlist, with a reason per domain
2. Confirm with the network team whether a proxy and TLS inspection are in the path
3. Push `HTTPS_PROXY` and `NO_PROXY` through MDM
4. Trust the corporate root CA via `NODE_EXTRA_CA_CERTS`

- A. 3 → 2 → 4 → 1
- B. 2 → 4 → 3 → 1
- C. 2 → 3 → 4 → 1
- D. 1 → 2 → 3 → 4

**C27.** A platform team picks LiteLLM as the LLM gateway in front of Bedrock and Vertex. They plan to `pip install litellm` from PyPI, front both providers with skip-auth flags, and attribute cost per team. What is MOST important to do before deploying?
- A. Check the LiteLLM version against Anthropic's gateway documentation, because versions 1.82.7 and 1.82.8 were compromised
- B. Install the newest PyPI release without checking
- C. Configure only OpenAI-format pass-through
- D. Strip `anthropic-beta` headers to reduce request size

**C28.** Which is the BEST primary success criterion for a migration pilot?
- A. "PR cycle time improves during the pilot."
- B. "Developers report they enjoy using Claude Code."
- C. "Lines of migrated code per developer rise 50%."
- D. "PR cycle time (ticket to merge) for the auth-service migration falls 25% against the Day 1 baseline by 15 March."

**C29.** End of Week 1: usage looks low, velocity has dipped, and the sponsor wants to schedule extra training. What is the BEST response?
- A. Schedule the extra training at once
- B. Explain that the Week-1 dip is expected calibration; continue technical calibration and CLAUDE.md setup, and watch for a plateau in Week 2
- C. Switch the cohort to Opus
- D. Pause the pilot until velocity recovers

**C30.** A client has ZDR enabled on Claude for Enterprise. Which planned Day 30 scorecard item is at risk of being unmeasurable?
- A. PR cycle time from GitHub
- B. Developer NPS from a short survey
- C. Contribution metrics from Claude Code analytics
- D. Daily active users from usage analytics

---

# SET D (advanced)

**D1.** For which task does the course's selection logic recommend Chat plus an Artifact, rather than building a Project?
- A. A weekly status report in the same format for six months
- B. A monthly variance analysis against a stable budget template
- C. A one-off reply to a vendor's payment-terms question, using the policy document and the email
- D. A recurring contract review against a fixed playbook

**D2.** An analyst running a long Opus session for a due-diligence report hits a usage limit midway. What does the course recommend for intensive work like this?
- A. Break the work into segments, save interim progress to the Project knowledge base, and restart from a summary
- B. Switch to Haiku mid-task so the session can continue
- C. Move the work into Incognito
- D. Keep extending the single session once the limit resets

**D3.** (Choose TWO) Which TWO tasks should go to Code Execution rather than prose generation?
- A. Drafting an apology email to a customer
- B. Deduplicating 3,000 contact records and normalizing their date formats
- C. Summarizing a meeting transcript
- D. Producing a downloadable .xlsx with variance calculations

**D4.** A user attaches the 2026 travel policy and asks about per-diem limits. Claude's answer mixes 2026 figures with older figures it learned in training. Which diagnosis and fix match the course?
- A. Next Token Prediction + Steerability; use code execution
- B. Working Memory alone; restart the conversation
- C. Knowledge alone; turn on web search
- D. Knowledge + Working Memory (stale context against trained knowledge); state which source wins: "Use only the attached document"

**D5.** Which statement about top-p sampling is accurate?
- A. It always keeps a fixed number of candidate tokens
- B. It keeps the smallest set of tokens whose probabilities add up to p, so fewer survive when the model is confident
- C. It raises the temperature
- D. It removes randomness completely

**D6.** In which collaboration mode does AI act with latitude inside boundaries you set?
- A. Agency
- B. Automation
- C. Augmentation
- D. Delegation

**D7.** An AI-built booking app works well for typical users. After launch, screen-reader users can't complete a booking. What would have caught this EARLIEST?
- A. More unit tests
- B. A load test
- C. Specifying accessibility in the design spec up front and auditing the AI output against it, since AI doesn't get accessibility right by default
- D. Asking the AI to "make it accessible" after launch

**D8.** Put the steps of a hand-written agent loop in order:
1. Your code runs the requested tool
2. Send messages along with the `tools` definitions
3. Append the assistant content and a user message carrying the `tool_result`
4. Claude returns `stop_reason: "tool_use"`
5. Repeat until `stop_reason` is `end_turn`

- A. 2 → 1 → 4 → 3 → 5
- B. 2 → 4 → 1 → 3 → 5
- C. 4 → 2 → 1 → 3 → 5
- D. 2 → 4 → 3 → 1 → 5

**D9.** A team moves a debugging assistant to Opus 4.7 and removes the `thinking` parameter, assuming adaptive thinking is on by default. Quality on hard bugs falls. What is the explanation?
- A. Opus 4.7 needs `budget_tokens` to think
- B. Temperature must be set to 1
- C. Web search has to be enabled for reasoning
- D. On Opus 4.7/4.8, leaving out `thinking` means no thinking; set `thinking={"type": "adaptive"}` explicitly and tune effort in `output_config`

**D10.** (Choose TWO) Which TWO statements about the memory tool are accurate, according to the course?
- A. Claude reads and writes a memory directory through tool calls
- B. Anthropic stores the memory server-side by default
- C. You implement the storage backend on the client side (files, a database, an encrypted store)
- D. The memory tool replaces prompt caching

**D11.** A file-share cleanup job has to walk thousands of files, move and archive them, flag the uncertain ones, run for minutes to hours, and survive network interruptions. Which surface is BEST?
- A. A hand-written agent loop inside a short-lived serverless function
- B. A tool-runner script triggered by cron on a laptop
- C. Managed agents: an agent, an environment and a session, with events streamed back
- D. A single `messages.create` call with a large `max_tokens`

**D12.** A team caches its 4,000-token system prompt, but `usage.cache_read_input_tokens` stays at 0. The system prompt begins with "Current time: {now}". What is the fix?
- A. Add more cache breakpoints
- B. Move the timestamp out of the cached prefix (after the last breakpoint), so the prefix stays byte-identical
- C. Switch to Opus
- D. Increase `max_tokens`

**D13.** Compliance needs a record of every shell command after it runs. Which hook?
- A. PostToolUse with matcher `Bash`
- B. PreToolUse with matcher `Bash`
- C. UserPromptSubmit
- D. Stop

**D14.** Which statement about CLAUDE.md is NOT what the course teaches?
- A. A project-level CLAUDE.md at the repo root is shared with the team through version control
- B. You can reference documents with `@README.md`
- C. Its contents are added to your prompt in every session
- D. Generate it with `/init` on day one and finalize it before any work starts

**D15.** A developer's configured MCP tools come to more than 10% of the context window. What does Claude Code do, according to the course?
- A. Returns an error and refuses to start
- B. Removes the largest servers automatically
- C. Switches to tool search mode, discovering tools on demand (which may be less reliable)
- D. Compacts the conversation immediately

**D16.** A developer opened a PR through Claude Code with `gh pr create`. The next day, reviewers leave comments. How does the developer resume with the original context?
- A. `/compact`, then reopen the session
- B. `claude --from-pr <PR_NUMBER>`
- C. `/commit-push-pr`
- D. `/context`

**D17.** (Choose TWO) Which TWO MCP statements are accurate?
- A. Tools are model-controlled: Claude decides when to call them
- B. A ReadResourceRequest returns a ReadResourceResult whose `contents` is a list
- C. Prompts are app-controlled
- D. Resources can only be reached when Claude makes a tool call

**D18.** A FastMCP server's generated tool schema shows parameters with no descriptions, and Claude often passes the wrong value to `old_str`. What is the targeted fix?
- A. Hand-write the JSON schema
- B. Switch the transport from stdio to HTTP
- C. Rename the tool
- D. Add Pydantic `Field(description=...)` to each parameter (e.g. "The text to replace. Must match exactly, including whitespace.")

**D19.** A subagent file won't load correctly. Its `description` spans three lines of YAML with example dialogues. What is the fix?
- A. Remove the `color` field
- B. Set `model: inherit`
- C. Put the description on a single line, using escaped `\n` for breaks
- D. Move the description into CLAUDE.md

**D20.** What does a subagent receive when it is launched?
- A. Its own system prompt from the config file, plus a task description written by the parent agent
- B. The parent's full conversation history
- C. Only the project's CLAUDE.md
- D. Only the user's original prompt, verbatim

**D21.** Put the course's steps for building an effective reviewer subagent in order:
1. `/agents` → Create new agent at project scope (Claude drafts name, description and prompt)
2. Restrict tools to read-only plus Bash for `git diff`
3. Add a structured output format, including an Obstacles Encountered section
4. Test it on real changes, and refine the description if it isn't triggered

- A. 2 → 1 → 3 → 4
- B. 1 → 3 → 4 → 2
- C. 3 → 1 → 2 → 4
- D. 1 → 2 → 3 → 4

**D22.** Fifty developers do routine feature work, and a small group runs overnight autonomous refactors. The CFO's proposal is "Opus for everyone, quality first." What is the BEST recommendation?
- A. Haiku for everyone, to save money
- B. Sonnet as the default and Opus for the overnight runs; Opus for all adds roughly 65% cost with no meaningful gain on routine work
- C. Opus for everyone, as proposed
- D. Sonnet for everyone, for one simple configuration

**D23.** (Choose TWO) Which TWO are Enterprise controls that Teams doesn't provide?
- A. A per-seat subscription fee
- B. Basic SSO
- C. SCIM provisioning
- D. The Compliance API

**D24.** An Azure-first client's CISO says: "We'll use Foundry, so everything stays in our tenancy, right?" What is the BEST answer?
- A. "No. Foundry requests are served on Anthropic-operated infrastructure. If hard tenancy residency is required, Bedrock or Vertex meets it."
- B. "Broadly yes; I'll validate the details."
- C. "Correct; that's the point of the native cloud path."
- D. "Residency doesn't depend on the path."

**D25.** With ZDR enabled on Claude for Enterprise, which item remains covered by ZDR?
- A. claude.ai chat conversations
- B. Claude Code on the web
- C. Claude Code inference (prompts and responses aren't stored after the response returns)
- D. `/feedback` submissions

**D26.** A gateway deployment needs per-user tokens that rotate, fetched from the client's vault. What does the course configure?
- A. Hardcode each token in a `.env` file
- B. `apiKeyHelper` in settings, running a script that fetches the token
- C. Only `ANTHROPIC_BASE_URL`
- D. `NO_PROXY`

**D27.** The same Claude Code configuration shows healthy cache reads in one region, but `cache_read_input_tokens` stays at 0 for a Bedrock deployment in another region. Nothing in the prompt varies. What should you check?
- A. Add more cache breakpoints
- B. Switch to Opus
- C. Look for a timestamp in the system prompt
- D. Whether prompt caching is available in that region, since availability varies by region on Bedrock and Vertex

**D28.** Which champion candidate is BEST?
- A. A senior developer who self-identified in Phase 2, influences team norms and wrote the first CLAUDE.md draft
- B. The most technically advanced developer, whose personal workflows are unusual
- C. A junior developer the manager assigned because they had free time
- D. The consultant, until the next engagement

**D29.** How should the Day 30 showcase demo be staffed?
- A. A polished recording made in advance
- B. Developers still at Stage 1, to show honest progress
- C. Two or three cohort developers at Stage 3–4 of the adoption curve, working on real pilot code
- D. The consultant, to keep the demo controlled

**D30.** Which statement about the two engagement modes is accurate?
- A. Mode 1 (2-day training) produces ROI data
- B. Mode 1 produces adoption signals but no ROI data; Mode 2 (30–45 days) produces ROI data because measurement is built before Day 1
- C. Mode 2 skips pre-kickoff to save time
- D. Both modes produce the same data

---
# ANSWERS AND REASONING

Each answer names the course section it comes from and explains why the closest wrong option fails.

## Set A

- **A1 C.** Hallucinated citations are where Next Token Prediction meets a Knowledge gap. The fix is to verify the specifics or ground them in retrieved sources (C1.7). *Closest wrong: D.* Temperature changes how sampling varies, not whether the model knows the source; a plausible fake can still be the most likely continuation.
- **A2 A.** This is lost-in-the-middle. Curate the input, put the key rule first and restate it near the end (C1.5). *Closest wrong: D.* A bigger window doesn't change the U-shaped attention; the rule would still sit in the middle.
- **A3 D.** Passing tests with an unhappy user means the wrong intent was described; trace back up the Description Chain (C2.4). *Closest wrong: B.* More lens-1 tests only re-check the intent that was already captured wrongly.
- **A4 B.** "Delegating implementation is usually safe. Delegating judgment is usually not" (C2.1, C2.3). *Closest wrong: D.* Deciding whether something is good enough to launch is judgment, which stays with the builder.
- **A5 A.** The task recurs, the background is stable and the format is fixed: build a Project (C3.2). *Closest wrong: D.* An Artifact is an output format and doesn't remove the weekly setup.
- **A6 D.** Numbers that will be reported should come from Code Execution, not prose (C3.3). *Closest wrong: A.* Asking the same prose generator to "verify" doesn't make the figures computed.
- **A7 C.** Project-scoped Memory follows Project boundaries (C3.4). *Closest wrong: B.* Clearing Memory by hand is error-prone and loses wanted continuity; A also gives up continuity.
- **A8 B.** For context degradation: restart from a summary (C3.7). *Closest wrong: A.* Repeating the framework keeps working inside the degraded thread.
- **A9 B.** `response.content` is a list of blocks; loop over it and read `text` blocks (C4.2). *Closest wrong: C.* No prompt changes the response structure.
- **A10 C.** Tool descriptions drive tool selection, and vague ones are the number-one cause of misfires (C4.5). *Closest wrong: B.* Merging tools hides the distinction rather than describing it.
- **A11 A.** Every `tool_use` needs a matching `tool_result` in the next user message, after the assistant turn has been appended (C4.4). *Closest wrong: B.* Retrying an identical malformed request fails the same way.
- **A12 D.** `effort` belongs in `output_config`, not inside `thinking` (C4.6). *Closest wrong: A.* `budget_tokens` is rejected on Opus 4.7 and later.
- **A13 D.** Server tools are run by Anthropic and their results come back in the same response (C4.7). *Closest wrong: A.* No beta header turns a server tool into a client `tool_use`.
- **A14 A.** The MCP connector needs both `mcp_servers` and an `mcp_toolset` with the same server name, plus the beta header (C4.9). *Closest wrong: B.* Claude introspects the server's tools; you never write their schemas.
- **A15 B.** Auto-accept applies edits automatically but still asks for commands (C5.2). *Closest wrong: D.* Skipping permissions would also run commands without asking.
- **A16 C.** Hooks are deterministic; CLAUDE.md is only usually followed (C5.10). *Closest wrong: A.* Louder text is still guidance, not enforcement.
- **A17 C.** Exit code 2 blocks the action, and stderr goes back to Claude. Exit 1 is a non-blocking error (C5.10). *Closest wrong: D.* PostToolUse runs after the command, too late to block it.
- **A18 B.** Project scope in a committed `.mcp.json` gives every teammate the same servers (C5.9). *Closest wrong: A.* User scope depends on each person remembering to set it up.
- **A19 D.** Use `/clear` when starting a new feature, and keep persistent facts in CLAUDE.md (C5.5). *Closest wrong: A.* `/compact` carries a summary of the old feature forward, which is exactly the bias to avoid.
- **A20 A.** Prompts are user-controlled, tools model-controlled, resources app-controlled (C6.8). *Closest wrong: C.* Resources are fetched by the app, not triggered by the user.
- **A21 A.** A resource is app-controlled: the app reads it and injects it, with no tool call (C6.6). *Closest wrong: C.* A prompt still relies on Claude choosing to call the tool.
- **A22 D.** The MCP Inspector (`mcp dev`) tests tools interactively and keeps state between calls (C6.4). *Closest wrong: C.* Hand-building protocol messages is possible but isn't the course's tool.
- **A23 B.** An output format gives the subagent natural stopping points and stops over-long runs; the course calls it the single most important improvement (C7.3). *Closest wrong: D.* The description shapes when the subagent is chosen and what it's told, not how it reports.
- **A24 C.** Sequential pipelines fail when each step depends on the last; handoffs lose information (C7.4). *Closest wrong: D.* "Proactively" affects triggering, not lost handoffs.
- **A25 B.** Test-runner subagents hide the output you need; the course reports this pattern did worst (C7.4). *Closest wrong: A.* A longer summary is still a lossy summary.
- **A26 C.** Standard seats are chat-only. Seat mismatch is the most common cause of activation delays (C8.3). *Closest wrong: A.* A proxy makes Claude Code hang; it doesn't make it unavailable to the account.
- **A27 D.** A residency requirement in AWS regions points to Bedrock plus a gateway, with the trade-offs named (C8.3, C9.1). *Closest wrong: A.* Enterprise is SaaS; Anthropic's infrastructure decides where processing happens.
- **A28 A.** The first enterprise ticket is a network ticket; ask the network team about the proxy and TLS inspection first (C9.3). *Closest wrong: B.* Forty identical failures aren't a bad build.
- **A29 D.** A gateway must forward `anthropic-beta` and `anthropic-version`. Stripping them degrades features silently (C9.4). *Closest wrong: B.* Rate limits cause errors, not quiet loss of features.
- **A30 B.** ZDR is Enterprise-direct only; on Bedrock, retention follows AWS policy in the client's account (C9.1, C9.5). *Closest wrong: D.* Deferring a question that's on every financial-services questionnaire costs credibility.
- **A31 A.** PR cycle time is objective and covers the whole loop, and the baseline is captured before Day 1 (C10.1–C10.3). *Closest wrong: D.* Self-reported hours are corroborating evidence and open to bias.
- **A32 C.** Steady usage with a flat result and unchanged patterns is the plateau signature; Code 201 lifts the delegation ceiling (C10.4). *Closest wrong: B.* Waiting to Day 25 leaves about five days to change the outcome.

## Set B

- **B1 D.** An agreeable bad premise is Knowledge meeting Steerability: invite pushback (C1.7). *Closest wrong: A.* The context here is the correct data; the failure is following the user's framing.
- **B2 B.** For letter over spirit, restate the goal (C1.6). *Closest wrong: D.* "Shorter" is another literal instruction that misses the intent.
- **B3 A.** The inner loop is Description + Discernment; the outer loop is Delegation + Diligence (C2.1). *Closest wrong: B.* That pair is the outer loop.
- **B4 C.** Lens 2, production readiness, covers concurrency and behaviour under load (C2.5). *Closest wrong: A.* Lens 1 checks correctness on real inputs, not concurrent ones.
- **B5 C.** Session-specific uploads are still reference material Claude reads, so they belong in the knowledge base (C3.5). *Closest wrong: A.* Standing instructions hold directives (what to do), not documents.
- **B6 B.** Project conversations share instructions and knowledge base, not context (C3.2). *Closest wrong: C.* Skills live at the account level.
- **B7 A.** Structured, high-volume work with a clear rubric is Haiku's profile (C3.6). *Closest wrong: C.* Sonnet is where you start, but the course's answer for this profile is Haiku.
- **B8 D.** On Team and Enterprise, an Owner or Primary Owner must enable web search first (C3.2). *Closest wrong: A.* Research is a separate feature; web search is available on all plans.
- **B9 A.** Eval first, climb from Haiku, stop at the cheapest model you'd ship (C4.3). *Closest wrong: C.* Sonnet is a sensible default but skips the evidence.
- **B10 D.** The tool runner builds schemas from your functions and runs the loop; the functions run on your own infrastructure (C4.5). *Closest wrong: A.* Managed agents run on Anthropic's infrastructure, which the team wants to avoid.
- **B11 B.** Route each task to its own model within one endpoint (C4.3). *Closest wrong: A.* Haiku for everything would under-serve the RFP work.
- **B12 C.** The compaction block has to go back into the history; append the full `response.content` (C4.10). *Closest wrong: B.* Context editing clears tool results; it's a different feature.
- **B13 B.** Just-in-time context is the design pattern; the other three are API features (C4.10). *Closest wrong: D.* The memory tool is an API primitive, even though you supply the storage.
- **B14 C.** Open the stream before sending the kickoff; it only delivers later events (C4.12). *Closest wrong: B.* Polling isn't the course's model; the issue is ordering.
- **B15 D.** Course-correct in plan mode, before any code exists (C5.4). *Closest wrong: B.* During coding, corrections already cost rework.
- **B16 A.** CLAUDE.md is persistent project memory; save corrections to it (C5.7). *Closest wrong: B.* A hook enforcing by deletion is heavy-handed; the problem is missing context.
- **B17 D.** MCP servers load all their tool definitions; disable unused ones and use CLIs where possible (C5.5, C5.9). *Closest wrong: A.* `/clear` empties the conversation, but the definitions load again.
- **B18 A.** A read-only reviewer, its config committed to the repo, gives the team consistent reviews (C5.6, C7.2). *Closest wrong: B.* User-level config can drift from person to person.
- **B19 C.** Discovery is ListTools (C6.2). *Closest wrong: A.* CallTool runs a tool that has already been discovered.
- **B20 B.** Complementary: MCP is about who implemented the tool, tool use is how Claude calls it (C6.1). *Closest wrong: C.* MCP tools are still called through tool use.
- **B21 C.** stdio is the common local transport (C6.2). *Closest wrong: B.* HTTP is for remote servers.
- **B22 B.** The description controls triggering; add "proactively" and examples (C7.2). *Closest wrong: C.* The main agent's model choice decides delegation, not the subagent's own model.
- **B23 A.** Research needs Glob, Grep and Read only (C7.3). *Closest wrong: C.* Bash is for reviewers that run `git diff`; Edit risks side effects.
- **B24 D.** Expert personas add nothing Claude doesn't already have (C7.4). *Closest wrong: C.* A copywriting subagent changes the default system prompt in a way that matters.
- **B25 A.** Governance needs with no residency requirement point to Enterprise, the controls tier (C8.3). *Closest wrong: B.* Teams has only basic SSO and no managed settings or Compliance API.
- **B26 D.** Try effort before a higher tier: "Model selection is an architecture decision; effort tuning is a performance lever" (C8.2). *Closest wrong: A.* That's the expensive move to make second.
- **B27 C.** Answer from the gap memo with the mitigation (C9.2). *Closest wrong: A.* A ticket comes back "works as designed" two days later, and you look like you don't know your own deployment.
- **B28 B.** Model Garden approval takes 24–48 hours: file on Day 1 (C9.1). *Closest wrong: A.* CLAUDE.md matters but has no external lead time.
- **B29 B.** Trust the corporate root CA (C9.3). *Closest wrong: A.* Turning off TLS verification fails the client's security review.
- **B30 C.** Gateway plus session, agent and parent-agent headers gives nested attribution (C9.4). *Closest wrong: D.* The Console has no Bedrock usage.
- **B31 D.** The migration is structural and meets all four criteria (C10.1). *Closest wrong: B.* Running both in parallel splits the signal.
- **B32 A.** No champion means the deployment decays after you leave (C10.6). *Closest wrong: B.* Some developers still in supervised mode at Day 28 is normal variation.

## Set C

- **C1 B.** It fixes every failure at once: re-pasting (Project and knowledge base), format drift (instructions plus Skill) and wrong numbers (Code Execution) (C3.2–C3.3). Lisbon and Windows are irrelevant. *Closest wrong: A.* Opus doesn't compute numbers reliably and doesn't remove the setup tax.
- **C2 D** (the NOT). Skills live at the account level and are invoked in any conversation (C3.3). *Closest wrong: A.* That statement is true; Skills still vary.
- **C3 A + C.** Incognito doesn't override org retention, and Project-scoped Memory separates clients (C3.4). *Closest wrong: B.* Memory import isn't documented for Enterprise. D is false: Project conversations don't share context with each other.
- **C4 C.** Name the pair (Next Token Prediction + Knowledge), then ground and verify (C1.3, C1.7). *Closest wrong: B.* A "don't hallucinate" instruction doesn't create knowledge; the model can't tell what it knows from what it's making up.
- **C5 A** (the LEAST effective). Forcing the instruction in a drifting thread doesn't close the gap (C1.6–C1.7). *Closest wrong: C.* A standing instruction is a legitimate fix, so it isn't the least effective option.
- **C6 D** (the NOT). The lenses are functional integrity, production readiness, problem fit, experience quality and responsible impact (C2.5). *Closest wrong: C.* Production readiness is lens 2.
- **C7 B.** "Make it look good is a wish, not a spec." Specify, then audit; AI doesn't do accessibility by default (C2.6). *Closest wrong: C.* A better model still has nothing concrete to follow.
- **C8 C.** Start with the eval-driven climb and route per task (C4.3). Kubernetes and Grafana are noise. *Closest wrong: D.* Caching is a good later lever but leaves the wrong model on 50,000 classifications a day.
- **C9 B + D.** Server tools return in the same response, with `server_tool_use` blocks (C4.7). *Closest wrong: A* (and C). Those describe client tools.
- **C10 A.** Disable everything by default and enable only the read tools. That covers read-only access and context (C4.9). *Closest wrong: B.* A prompt instruction isn't an access control.
- **C11 D** (the NOT). With managed agents you send and read events; you don't write a stop_reason loop (C4.12). *Closest wrong: B.* The environment is a required primitive.
- **C12 C.** "Tools for your stuff, Skills for your processes, MCP for everyone else's stuff" (C4.9). *Closest wrong: A.* The internal API has no provider-maintained MCP server.
- **C13 A.** Only a hook is deterministic, and checking it in or enforcing it through managed settings makes it org-wide (C5.10, C9.3). *Closest wrong: D.* A reviewer flags problems after the fact; it doesn't block the write.
- **C14 B** (the NOT). Auto-accept still asks for commands (C5.2). *Closest wrong: C.* That statement is true.
- **C15 D.** Explore → Plan → Code → Commit (C5.4). *Closest wrong: A.* Planning before exploring means planning without context.
- **C16 A + D.** Subagents keep the main context clean, and fewer MCP definitions use less context (C5.5). *Closest wrong: B.* Vague prompts cost *more* context, because Claude has to explore.
- **C17 C.** Populating UI autocomplete is app-controlled, so a direct resource fits (C6.6, C6.8). *Closest wrong: A.* A tool is model-controlled; Claude shouldn't be in the loop for UI autocomplete.
- **C18 B.** URI template parameters arrive as keyword arguments (C6.6). *Closest wrong: D.* `Field` describes tool parameters; the problem here is the missing parameter.
- **C19 A.** The description shapes the input prompt the main agent writes (C7.3). *Closest wrong: D.* Dropping the subagent throws away a valid fresh-eyes review.
- **C20 D** (the LEAST justified). An expert persona adds nothing (C7.4). *Closest wrong: A.* A copywriting subagent has a real custom system prompt.
- **C21 C.** Obstacle reporting in the output format stops the rediscovery (C7.3). *Closest wrong: B.* More tools don't change what the subagent reports back.
- **C22 B + C.** Desktop, Web and Mobile have scoped access; the Agent SDK has whatever the host grants (C8.1). *Closest wrong: A.* The IDE extension isn't lighter; it's the same agent.
- **C23 A.** A commitment plus residency points to the cloud path; name the governance gap so security can assess it (C8.3, C9.1). JetBrains and Okta are noise. *Closest wrong: B.* Enterprise can't put processing in the client's GCP region and ignores the CUD.
- **C24 D.** Cloud commitments and buying route decide the architecture; ask procurement (C9.1). *Closest wrong: C.* ZDR matters, but in the course's order compliance comes after commitments and buying route.
- **C25 B** (the NOT). The CLI is identical on every path (C9.1–C9.2). *Closest wrong: D.* Model pinning really is the client's job on cloud paths.
- **C26 C.** Diagnose (2) → deploy the proxy settings (3) → fix the certificate error that appears once the proxy is in place (4) → hand security the list (1) (C9.3). *Closest wrong: B.* The CA error only shows up after traffic reaches the inspecting proxy.
- **C27 A.** Supply-chain check: versions 1.82.7 and 1.82.8 were compromised (C9.4). *Closest wrong: B.* Installing whatever is newest without checking is the risk itself. D breaks features.
- **C28 D.** Metric, threshold, baseline and date: the course template (C10.2). *Closest wrong: A.* "Improves" is not a claim anyone can test.
- **C29 B.** The Week-1 dip is calibration, not a training problem (C10.4). *Closest wrong: A.* Intervening on velocity in Week 1 is what the course warns against.
- **C30 C.** Under ZDR, analytics show usage metrics but not contribution metrics (C9.5, C10.3). *Closest wrong: D.* Usage metrics stay available.

## Set D

- **D1 C.** A one-off draft with no reuse fits Chat + Artifact, card E (C3.8). *Closest wrong: B.* Recurring and templated work belongs in a Project.
- **D2 A.** Segment the work, persist interim results and restart from a summary (C3.7). *Closest wrong: B.* Changing model mid-task trades quality for headroom and doesn't solve the planning problem.
- **D3 B + D.** Data transformation and real downloadable files go to Code Execution (C3.3). *Closest wrong: C.* Summarizing is a language task.
- **D4 D.** Stale context against trained knowledge is Knowledge meeting Working Memory: state which source takes priority (C1.7). *Closest wrong: C.* Web search adds a third source rather than settling which one wins.
- **D5 B.** Top-p keeps the smallest set reaching p, so it adapts to confidence (C1.3). *Closest wrong: A.* That describes top-k.
- **D6 A.** Agency means latitude inside set boundaries (C2.3). *Closest wrong: C.* Augmentation means working together, not AI acting alone.
- **D7 C.** Specify accessibility, then audit; it's a design decision made up front (C2.6–C2.7). *Closest wrong: D.* After launch is the most expensive time to find it.
- **D8 B.** Send → `tool_use` → run → append assistant content and results → loop (C4.4). *Closest wrong: D.* You can't append a result before the tool has run.
- **D9 D.** On Opus 4.7 and 4.8, leaving out `thinking` turns it off; set adaptive explicitly (C4.6; skill-verified). *Closest wrong: A.* `budget_tokens` returns a 400 on 4.7.
- **D10 A + C.** Claude uses the memory directory through tool calls, and you own the storage (C4.10). *Closest wrong: B.* Storage is client-side.
- **D11 C.** Long-running, file-heavy work that must survive interruptions is the managed-agents case (C4.12). *Closest wrong: B.* The tool runner still runs on your side and doesn't resume on its own.
- **D12 B.** Caching matches a prefix; a timestamp at the start invalidates it on every call (C4.10). *Closest wrong: A.* More breakpoints after a changing prefix still miss.
- **D13 A.** PostToolUse runs after the command, which is where you log it (C5.10). *Closest wrong: B.* PreToolUse runs before execution; it fits blocking, not logging the result.
- **D14 D** (the NOT). The course says to start *without* a CLAUDE.md, add what you keep correcting, and keep it evolving (C5.7, C10.5). *Closest wrong: C.* That statement is true.
- **D15 C.** Above 10% of the window, Claude Code switches to tool search mode (C5.9). *Closest wrong: B.* It doesn't remove servers.
- **D16 B.** `claude --from-pr` resumes the session linked to the PR (C5.6). *Closest wrong: C.* `/commit-push-pr` creates PRs; it doesn't resume them.
- **D17 A + B.** Tools are model-controlled, and the resource result holds a `contents` list (C6.6, C6.8). *Closest wrong: C.* Prompts are user-controlled.
- **D18 D.** `Field(description=...)` goes into the generated schema and guides Claude (C6.3). *Closest wrong: A.* Hand-writing the schema throws away the SDK's main benefit.
- **D19 C.** The `description` must be a single line (C7.2). *Closest wrong: D.* The description belongs in the frontmatter.
- **D20 A.** A subagent gets its own system prompt plus a task written by the parent (C7.1). *Closest wrong: B.* Isolation is the whole point.
- **D21 D.** Create → scope the tools → define the output → test and refine (C7.2–C7.3). *Closest wrong: B.* Tool scoping happens when the agent is created, not after testing.
- **D22 B.** A tiered mix; Opus for everyone is about +65% cost for no gain (C8.2). *Closest wrong: D.* Sonnet for everyone overpays for high-volume scripted work.
- **D23 C + D.** SCIM and the Compliance API are Enterprise controls (C8.3). *Closest wrong: B.* Teams has basic SSO; Enterprise adds SSO with domain capture.
- **D24 A.** The Foundry routing nuance (C9.1, C9.5). *Closest wrong: B.* "Broadly yes" is backwards; the answer you'd later validate is no.
- **D25 C.** ZDR covers Claude Code inference (C9.5). *Closest wrong: B.* ZDR disables Claude Code on the web.
- **D26 B.** `apiKeyHelper` fetches rotating tokens (C9.4). *Closest wrong: C.* A base URL alone carries no token.
- **D27 D.** Prompt caching availability varies by region on Vertex and Bedrock (C9.2). *Closest wrong: C.* The prompt is identical across regions, so a timestamp isn't the cause.
- **D28 A.** The course's ideal: influence, motivation, self-identified (C10.5). *Closest wrong: B.* The course says "most technically advanced" is false; unusual workflows don't generalize.
- **D29 C.** Stage 3–4 developers on real code (C10.7). *Closest wrong: B.* Stage-1 demos show supervised mode and undersell the result.
- **D30 B.** Mode 1 produces adoption signals, Mode 2 produces ROI (C10.1). *Closest wrong: A.* Mode 1 has no baseline or measurement period.

---

## Answer distribution (check)

| Set | A | B | C | D |
|---|---|---|---|---|
| A (32) | 8 | 8 | 8 | 8 |
| B (32) | 8 | 8 | 8 | 8 |
| C (30 items, 34 letters incl. Choose TWO) | 8 | 8 | 9 | 9 |
| D (30 items, 34 letters incl. Choose TWO) | 8 | 9 | 9 | 8 |

## Score guide

| Set | Pass-ready | Review | Re-study |
|---|---|---|---|
| A or B (32) | **≥ 27 (85%)** | 22–26 | ≤ 21 |
| C or D (30) | **≥ 24 (80%)** | 19–23 | ≤ 18 |

- "Choose TWO" items score all-or-nothing. Ordering items need the exact sequence.
- **Map your misses**:
  - Q5–8 (A/B) or Q1–3 (C/D) → `00-platform-model-foundations-notes.md`.
  - Q9–14 (A/B) or Q8–12 (C/D) → C4, including the API drift table at the end of `01`.
  - Q15–25 (A/B) or Q13–21 (C/D) → C5–C7.
  - Q26–32 (A/B) or Q22–30 (C/D) → C8–C10, including the simulation answers in `01`.
- A missed question in Sets C/D usually comes from a trap in the stem. Re-read the constraint word (FIRST, BEST, LEAST, NOT) and check whether the option you chose was **true but off-symptom**.

---
<!-- nav:start -->
> ⬅️ [[claude-architect-exam-prep/02-commute-recall|Commute recall]] · 🏠 [[claude-architect-exam-prep/Architect Exam Prep|Architect index]] · [[Claude Certifications|Home]] · [[Claude Certifications|Home]] ➡️
<!-- nav:end -->
