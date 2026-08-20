# 4C — The Harness Evaluation Standard

> **See a Harness. Ask four questions: Cost, Compatibility, Continuity,
> Cognition.**

[![4C Open-Source Harness Ladder: DeepSeek Harness leads the candidate-blind source exam at 86 across 15 pinned code audits.](assets/4c-harness-ladder.svg)](docs/scouts/2026-08-19-open-source-ladder.md)

**Current source-exam leader: DeepSeek Harness — 86/100.** The opening ladder
ranks all 15 active open-source coding Harnesses that pass the dated 10k-star
scope rule. Every candidate answers the same 12 frozen questions; missing
evidence scores zero, and a contract hash prevents candidate-specific weights
or post-hoc question changes. The [exam](docs/scouts/interactive-coding-v2-exam.json),
[answer sheets](docs/scouts/interactive-coding-v2-results.json), and exact-commit
evidence are machine-checked. Each candidate now links to its official GitHub
repository and shows a dated star snapshot; stars are context, never a scoring
input. Commercial and source-insufficient
products remain tracked—without invented scores—in the rule-based
[market universe](docs/validation/market-universe.md).

[**Run the 4C Check ↓**](#run-the-4c-check-in-five-minutes) ·
[Scorecards](docs/scouts/2026-08-19-open-source-ladder.md) ·
[Market coverage](docs/validation/market-universe.md) ·
[Add a missing Harness](https://github.com/warlockee/4c-harness/issues/new?template=market-coverage.yml) ·
[Challenge a score](https://github.com/warlockee/4c-harness/issues/new?template=score-challenge.yml) ·
[Full method](docs/harness-scout.md)

## Every Harness. The same four questions.

When a new AI Harness appears, feature lists and demos tell you what exists.
4C tells you what changes the result for a specific task—and what evidence
would prove that judgment wrong.

| Ask | The decision question | Inspect the execution path for |
|---|---|---|
| **Cost** | Does it turn limited time, money, tokens and attention into more verified outcomes? | waits, calls, retries, context tax, concurrency and cache behavior |
| **Compatibility** | Does it preserve the model, tool, provider and modality semantics the task needs? | translation loss, native controls, tool contracts and extension seams |
| **Continuity** | Does useful work survive turns, failures, handoffs and change? | state, checkpoints, reconstruction, rollback and migration |
| **Cognition** | Does evidence improve future policy—not merely accumulate more memory? | attributable updates, evaluation, promotion and rollback |

4C is not a universal feature score. First name the task terrain, then activate
only the pressures that change the decision. The same Harness can be excellent
for interactive coding and poor for a durable high-authority workflow.

``` text
name the terrain → activate the Cs → inspect the shipped path
                 → score the evidence → try to falsify it
```

The ruthless rule: **if removing a pressure changes no decision, it does not
count.** Every score carries its exact version, evidence stage and boundary
status, so source predictions cannot masquerade as measured wins.

For a public comparison, broad 0–5 grades are not the leaderboard. 4C first
freezes a candidate-blind exam: shared subquestions, shared weights, explicit
half/full-credit rules, and a contract hash. Harnesses answer the exam; the exam
does not move to flatter a Harness.

## Run the 4C Check in five minutes

Hand this prompt to a coding agent:

``` text
Use the 4C Harness Evaluation Standard from
https://github.com/warlockee/4c-harness.

Harness: <name + exact version or commit>
Task terrain: <real task, limits and externally checkable finish line>

1. Decide which Cost / Compatibility / Continuity / Cognition pressures
   actually change this task. Give inactive Cs zero weight.
2. Lock terrain weights across every active C; inactive Cs get zero weight.
3. Inspect the shipped execution path at the exact commit. For every active C,
   link implementation, executable invariant and reachability.
4. For one Scout Card, grade each active C from 0–5. For a comparison, freeze
   candidate-blind subquestions and weights before opening candidate answers.
5. Return the score + frozen contract + evidence stage + boundary status. Separate source
   facts, source inferences and runtime observations. Do not award points for
   feature count, popularity, testimonials or an unlinked benchmark number.
```

For a switch decision, continue into the [source-path and yield
audit](docs/execution-yield.md), [migration bill](#make-the-candidate-pay-the-moving-bill)
and a locked paired trial.

## DeepSeek Harness: 86/100 on the fixed source exam

> **4C Source Exam: 86/100 · Source-examined · Nominated · Boundary unknown**

Terrain: latency- and quota-sensitive interactive coding with on-demand local
extension.

| Active C | Available | Earned | Lost points |
|---|---:|---:|---|
| **Cost Efficiency** | 45 | 40 | Hard budget/stop enforcement receives only half credit. |
| **Compatibility** | 35 | 30.5 | General tool-protocol coverage receives only half credit. |
| **Continuity** | 20 | 15.5 | Crash-tail integrity and session rollback each receive only half credit. |
| **Cognition** | 0 | 0 | Inactive for this terrain. |

Same terrain, same frozen exam:

| DeepSeek | Pi | Qwen Code | Gemini CLI | Codex | Zed Agent |
|---:|---:|---:|---:|---:|---:|
| **86** | 84 | 82.5 | 78 | 76.5 | 75.5 |

The old whole-C grade compressed five candidates to 80. The
[candidate-blind exam](docs/scouts/interactive-coding-v2-exam.json) replaces
that coarse leaderboard with 12 shared questions and mechanical scoring.
DeepSeek leads, but does not receive a private curve or a perfect source score.

Every non-zero answer resolves to a public, commit-pinned evidence row: the
[implementation, executable invariant, shipped reachability and
falsifier](docs/scouts/fit-score-evidence.json). `source-observed` means the
row states only what the code or test establishes; `source-inferred` means the
user-visible effect is a prediction, never a measured result. Think a grade is
wrong? [Challenge that exact score](https://github.com/warlockee/4c-harness/issues/new?template=score-challenge.yml)—counterevidence can lower it as readily as
new evidence can raise it.

## A standard must survive public challenges

Disagree with a grade? [Challenge the exact C, terrain and
version](https://github.com/warlockee/4c-harness/issues/new?template=score-challenge.yml).
The response must be pinned counterevidence, not brand preference. Accepted
challenges change the evidence row and score together in public history.

The [Bole Challenge](docs/bole-challenge.md) tests a harder, secondary claim:
can 4C use this standard to identify an underappreciated Harness before runtime
trials or consensus reveal the answer? That prospective hit rate is proof of
the standard, not the brand positioning.

[**Open a public Bole trial →**](https://github.com/warlockee/4c-harness/issues/new?template=bole-challenge.yml) ·
[Scout board](docs/scouts/README.md) ·
[Calibration protocol](docs/scout-calibration.md)

> **Bole status: UNPROVEN** — 0/20 prospective calls resolved, 0 hits; 0/5 shadow calls.

The first source sweep found the code paths that can explain DeepSeek Harness's
speed and extensibility, but happened too late to count as prediction. The
machine-readable [certification status](docs/scouts/bole-status.json) is checked
in CI, so that claim cannot advance ahead of the evidence.

## Why the usual signals do not answer the question

| Signal you have today | What it answers | What it leaves open |
|---|---|---|
| Task benchmarks (SWE-bench, Aider's benchmark, OSWorld, WebArena) | How well a model and Harness scored on someone else's task distribution | Whether it changes anything for *your* task, and how much of the score is the model |
| Feature matrix and docs | Which mechanisms exist | Whether you need them, and what you would rebuild |
| Stars, release cadence, demos | Attention and maintenance | Fit, and the cost of leaving what you have |
| **4C activation** | Which pressures your task makes relevant | Whether either implementation realizes them well |
| **Source-path + yield audit** | What the real code path adds or avoids, which rejected tasks become feasible, and what a pinned trial distribution delivers | Long-term behavior outside the sampled task portfolio |

A model call is not a task. A **Harness** is the engineering layer that turns
bounded, mostly stateless model calls into task execution across tools, state,
providers and time. Two Harnesses differ in a way that matters only where they
take a different execution decision. 4C names the four reasons that decision
has to change, so “should I switch?” becomes a diff instead of an impression.

## Make the candidate pay the moving bill

If the verdict is switch, the cost is not "learn a new CLI". It is the set of
execution decisions you currently get for free and would have to re-establish.
Price these seven line items; the first four are the pressures, the last three
are the boundary obligations that no framework removes from you.

| Line item | What you are actually moving | Usual cost |
|---|---|---|
| **Cost** | Budget accounting, stop rules, cache and routing policy | Low if your app owns the envelope, high if you relied on the Harness's routing or caching to stay in budget |
| **Compatibility** | Provider adapters, tool schemas, MCP servers, structured output | Low for MCP tools and standard schemas, high for bespoke tool wrappers written against one Harness's API |
| **Continuity** | Session format, checkpoints, resume, fork, history, undo | Usually the largest item. Session and checkpoint formats are product-specific, so in-flight work and history rarely port |
| **Cognition** | Rule files, memory, learned or accumulated policy | Low for hand-authored context files, which are text. Adaptive state does not transfer |
| **Epistemic Access** | Retrieval, repository maps, ignore rules, context assembly | Re-tune, then verify the model still sees the facts the task needs. Silent regressions here look like model quality drops |
| **Validity** | Output checks, test gates, postcondition verification | Carries if you own it in CI, rebuilds if you leaned on Harness-side validation hooks |
| **Authority** | Permission rules, sandbox profile, approval policy, effect scope | Re-express and re-verify. Two products can advertise the same guarantee and enforce a different scope, so test it rather than reading it |

That last row is not theoretical. Codex's `:workspace` profile also grants the
system temporary directory, which the
[enforcement experiment](experiments/codex_sandbox_authority.py) had to work
around. Assume nothing about a new sandbox until a denied write actually fails.

``` text
Continue from the evaluation above.

Price my migration across the seven line items in the README's migration table.
For each: what carries over unchanged, what I rebuild, what I must re-verify by
running it rather than by reading docs. Flag anything I currently get from the
Harness that I would silently lose.
```

## Mechanism map, not a leaderboard

These pre-computed rows tell you which mechanisms deserve inspection. They do
**not** let you skip the source-path and yield audit: `Strong` / `Partial` /
`Evidence` are coverage labels, never performance grades.

This older mechanism-validation cohort is deliberately narrower than the
opening [market universe](docs/validation/market-universe.md): it admits only
high-visibility open implementations and also samples adjacent architectures.

The coverage columns below remain mechanism maps, not product grades. A pinned
source rerun now advances nine terrain-specific prospects to `Nominated` while
holding two ecosystem candidates at `Mapped`; see the
[2026-08-19 Harness Scout source sweep](docs/scouts/2026-08-19-source-sweep.md).
DeepSeek is the key correction: its default execution and change paths reveal a
P1 prospect that the coverage table hid. None is yet `Qualified` or
`Task-proven`; the [promotion ladder](docs/harness-scout.md#4-the-promotion-ladder)
makes that missing evidence explicit.

| Open-source system | Cost controls | Compatibility mechanisms | Continuity mechanisms | Cognition machinery | What source/docs establish |
|---|---|---|---|---|---|
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Partial | **Strong** | **Strong** | Evidence | Replaceable services and event-sourced sessions; its direct stream, off-path persistence/telemetry, parallel tool scheduler and agent-operable plugin loop predict low path tax and a short change path that still require a task trial. |
| [Codex](https://github.com/openai/codex) | Partial | **Strong** | **Strong** | Evidence | Sandboxed tools, approval policy, MCP/skills and resumable sessions. Configuration and traces do not by themselves create Cognition. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | **Strong** | **Strong** | **Strong** | Evidence | Model routing, token caching, MCP/extensions, sandboxing, checkpointing. Broad coverage is useful only when the task activates it. |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Partial | **Strong** | **Strong** | Evidence | Sandboxed execution and lifecycle control for autonomous runs. Evaluation evidence does not make the policy self-improving. |
| [Cline](https://github.com/cline/cline) | Partial | **Strong** | **Strong** | Evidence | One coding core across IDE, CLI and SDK, with checkpoints and persistent state. Multi-agent and scheduling can be unnecessary for smaller tasks. |
| [Aider](https://github.com/Aider-AI/aider) | Partial | **Strong** | Partial | Evidence | Focused terminal editing with repository maps and git-backed undo. Its smaller profile is often an advantage. |
| [browser-use](https://github.com/browser-use/browser-use) | Partial | **Strong** | Partial | Evidence | Browser execution loop with provider choice and persistent browser resources. Specialization is not general completeness. |

Adjacent architectures that can own Harness mechanisms, listed separately
because their product unit is not a terminal or IDE agent:

| Representative system | Archetype | Cost | Compatibility | Continuity | Cognition | Reach for it when |
|---|---|---|---|---|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful agent runtime | Partial | Partial | **Strong** | Evidence | Continuity dominates: durable state, interrupt/resume, replay |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Multi-agent orchestration | Partial | **Strong** | **Strong** | *Adaptive* | Two or more roles genuinely need different tools, authority or context |
| [Langflow](https://github.com/langflow-ai/langflow) | Visual workflow platform | Partial | **Strong** | **Strong** | Evidence | Composition and deployment matter more than one local agent loop |
| [LiteLLM](https://github.com/BerriAI/litellm) | Model gateway | **Strong** | **Strong** | Partial | *Adaptive* | Cost and Compatibility dominate: budgets, routing, fallback, many providers |

Three things these tables are not saying:

- **Gemini CLI is not better than Aider** for exposing more machinery. More
  activated Cs mean a harder task, not a better product. If your task does not
  activate a pressure, machinery serving it is migration cost with no return.
- **A trace or eval feature is not Cognition.** Only two systems here reach
  `Adaptive`, where prior outcomes automatically change live policy, and none
  reaches `Strong`. Rungs are defined in the
  [selection audit](docs/validation/popular-harness-selection.md#how-cognition-is-graded).
- **A product can span layers.** vLLM batching and GPU scheduling optimize model
  computation and stay Infrastructure; task-level routing or retry policy is
  Harness.

`Strong` is substantial first-class machinery, `Partial` is mechanisms that
exist while application policy does most of the work, `External` means bring
another component. None of those labels means fast, cheap, reliable or
pleasant. Table eligibility is 30k+ GitHub stars, an OSI-approved license and
activity in the prior six months; live counts and sources are in the
[selection audit](docs/validation/popular-harness-selection.md).

## The engine: three pressures + one feedback plane

Four questions, one per durable reason execution policy has to change:

| 4C | Pressure | The decision it governs |
|---|---|---|
| **Cost** | Resources are finite | Budget, route, cache, compress, parallelize or stop? |
| **Compatibility** | Systems differ | Which model, provider, tool and protocol differences need adapters or negotiation? |
| **Continuity** | Tasks unfold through time | What state, lifecycle and recovery semantics must survive one model call? |
| **Cognition** | Past runs produce evidence | Which reusable execution policy should improve from prior runs? |

![The 3 + 1 structure of 4C](assets/diagrams/3-plus-1.svg)

Cost, Compatibility and Continuity shape current execution. Cognition is the
cross-run feedback plane that can update them.

A pressure counts only when deleting it from your task changes a decision:

| Delete this | If nothing changes | Then you need no |
|---|---|---|
| Resource scarcity: make it free, instant, unlimited | Cost is inactive | Router, cache, budget optimizer beyond one hard stop |
| Semantic difference: one provider, one tool schema | Compatibility is inactive | Adapters, capability negotiation, fallback |
| Time: one call, no history, no resume | Continuity is inactive | Checkpoint store, workflow engine, durable runtime |
| Prior experience: no past runs to learn from | Cognition is inactive | Optimizer, self-modifying loop, memory system |

"We may need it someday" does not activate anything. Only an observed policy
delta does.

The same four questions narrow a production incident: budget exhausted, latency
cliff or context overflow is **Cost**; provider, tool or schema mismatch is
**Compatibility**; lost state, unsafe retry, runaway loop or broken resume is
**Continuity**; the same failure repeating despite accumulated evidence is a
**Cognition gap**. Wrong answers and unpermitted actions are deliberately not
inside a C; see [the boundary you always own](#the-boundary-you-always-own).

## The boundary you always own

4C tells you why execution policy changes. It does not make an agent accurate
or safe, and no framework takes these three off your hands:

- **Epistemic Access:** did the model observe the task-relevant, attributable
  and sufficiently fresh evidence?
- **Validity:** do the input, proposed action, output and observed postcondition
  satisfy the task contract?
- **Authority:** may this principal cause or expose this effect for this scope
  and audience?

A tool call can be cheap, compatible, stateful and learned, and still be wrong
or unauthorized. These three are also the residuals that falsified the original
version of this theory, which is why they are named separately instead of being
folded into a C, and why they are line items in the migration table.

## Building one? Start smaller than feels comfortable

### Step 1: Write the task contract before choosing a framework

``` text
input          What starts one task execution?
success        What observable result means the task is complete?
effects        Which tools, files, services or people may it affect?
evidence       What current facts must the model be able to observe?
limits         What token, time, money and attempt envelope applies?
```

### Step 2: Run the four removal tests

Use the table above.

### Step 3: Add the smallest mechanism for each active C

| Active pressure | Minimum useful mechanism | Add later only when proven necessary |
|---|---|---|
| Cost | usage accounting + hard budget/stop | routing, caching, compression, speculative parallelism |
| Compatibility | typed model/tool boundary | multi-provider adapters, capability negotiation, fallback |
| Continuity | explicit state + step limit + terminal states | durable checkpoints, replay, fork, compensation, distributed workflow runtime |
| Cognition | traces + outcome labels + versioned policy artifact | automated diagnosis, optimization, rollout and rollback |

The minimal Harness is usually not a framework. It is a small execution kernel:

``` text
task input
  → assemble current evidence
  → call one model through one typed boundary
  → validate and authorize any proposed effect
  → execute, observe the outcome and update task state
  → stop on success, budget or explicit failure
  → emit a trace for later evaluation
```

Do not add multi-agent delegation until two roles require different tools,
authority or context. Do not add durable execution until a task must survive a
process boundary. Do not add model routing until resource or capability
differences change a real decision. Do not add Cognition until you can name the
versioned policy artifact that evaluation will update.

### Step 4: Make the coding agent prove minimality

``` text
Build the minimum Harness for this task:

Task contract:
- Input: <one execution input>
- Success/postcondition: <observable condition>
- Allowed effects: <tools/resources and scope>
- Required evidence: <facts the model must observe>
- Hard limits: <tokens/time/money/attempts>

4C activation:
- Cost: <inactive, or exact policy delta>
- Compatibility: <inactive, or exact semantic difference>
- Continuity: <inactive, or exact state/lifecycle requirement>
- Cognition: <inactive, or prior evidence → versioned policy artifact>

Implementation rules:
1. Start with one agent, one model path and explicit typed tools.
2. Implement only mechanisms justified above.
3. Keep application success criteria outside model self-judgment.
4. Validate tool arguments and observable postconditions.
5. Enforce effect scope independently of model output.
6. Add a hard step/budget stop and structured execution trace.
7. For every extra abstraction, state the failure it prevents and the test
   that proves the abstraction is necessary.

Deliver:
- the smallest runnable implementation;
- tests for success, invalid output, denied effect, budget stop and tool failure;
- a 4C decision record listing active and deliberately inactive mechanisms;
- no router, workflow engine, vector memory, multi-agent layer or optimizer
  unless its activation test is demonstrated.
```

| Task | Active 4C | Minimum design |
|---|---|---|
| Extract a typed record from one document | Cost only if the document can exceed the envelope; Compatibility only if providers vary | One model call, typed output validation, hard token limit; no agent loop or memory |
| Research across web and private documents | Cost + Compatibility + Continuity | Evidence retrieval, typed tools, bounded loop, explicit state/citations and stop rule; add checkpoints only if execution must resume |
| Autonomous coding task | Cost + Compatibility + Continuity; Cognition optional | Sandboxed tools, stateful loop, tests/postcondition checks, scoped permissions, budget/step stops; add Cognition only when traces update a versioned coding policy |

## Worked example: DeepSeek Harness

This is the case that exposed the missing evaluation layer. The earlier audit
correctly found its mechanisms and still failed to surface why a person might
love using it.

| 4C pressure | Machinery | What the documented architecture shows |
|---|---|---|
| **Cost** | Partial | Prompt assembly, telemetry and stopping give control points, but no closed-loop budget, routing or cache policy. |
| **Compatibility** | **Strong** | Plugin-defined model adapters, tool registries and capability providers make the seams explicit and replaceable. |
| **Continuity** | **Strong** | An append-only session-event log supports reconstruction, persistence, resume, fork and recovery. |
| **Cognition** | Evidence | Logs, telemetry and benchmarks supply evidence; nothing automatically turns outcomes into a versioned future policy. |

`Cost: Partial` says only that DeepSeek exposes fewer cost-policy controls. It
does **not** say DeepSeek is slow or expensive. Source-path inspection at
upstream commit [`141eb6f`](https://github.com/deepseek-ai/deepseek-harness/tree/141eb6fef83422698aef7a981029e843e8161534)
finds a different kind of evidence:

| Code-path property | What it predicts |
|---|---|
| Direct SSE streaming; chunks enter the session stream as they arrive | Little Harness amplification before useful output |
| Native translation of DeepSeek thinking, tool calls, cache usage and provider errors | Less loss at the Model–Harness seam than a lowest-common-denominator adapter |
| Write-behind session persistence and a non-blocking telemetry contract | Durability and observation avoid awaited storage/network work on the response path |
| Bounded parallel scheduling for parallel-safe tool calls | Independent tools can reduce wall time while results remain model-ordered |
| Per-package token and KV-cache-effect documentation | Prompt tax and cache invalidation are inspectable rather than hidden |
| Live Cordis inspection plus agent-callable define/run/stop tools and reversible plugin effects | A short change path from missing capability to running, rollbackable extension |

Those facts explain why low-latency interaction and on-demand self-extension
are plausible user experiences. They still do not prove provider latency,
cost, correct completion or delight. The [full source-to-yield audit](docs/execution-yield.md#7-deepseek-harness-what-source-inspection-should-have-surfaced)
states the predictions, evidence limits and runtime measurements needed for a
switch verdict. DeepSeek is therefore **Nominated** for latency-, quota- and
extension-sensitive terrain—not declared a winner. This separation lets code
reveal implementation quality without turning a testimonial into a benchmark
or a mechanism inventory into a score. Its [Scout
Card](docs/scouts/deepseek-harness.md) states the exact terrain, falsifiers and
qualification trial.

## Evidence, scars and ways this theory can die

Six experiments in [`experiments/`](experiments/README.md) run pinned upstream
packages and check a claimed policy delta: LiteLLM's own parameter translation,
the Codex sandbox denying an out-of-scope write, ONNX Runtime holding a result
fixed across computation policies. Each names the observation that would have
falsified it, and each declares whether the evidence comes from the upstream
system or from local instrumentation.

``` shell
python3 -m venv .venv
.venv/bin/pip install -r experiments/requirements.txt
.venv/bin/python experiments/run_all.py
.venv/bin/python tools/scout_cohort_check.py
```

The original claim here was that four constraints exhaust Harness engineering.
Attack found three decisions that survive removing all four, so that claim is
[rejected in the canonical documents](docs/theory.md) instead of quietly
renamed, and two published predictions record their own falsification. What
remains is the part that survived, plus [six kill
criteria](docs/theory.md#10-kill-criteria) stating how to end it: find a
recurring Harness decision that survives removing scarcity, difference, time and
prior experience. One counterexample outranks every mapping in this repository,
and the [review guide](REVIEW_GUIDE.md) says where to send it.

## Go deeper

- [Glossary](docs/glossary.md): every term in one plain sentence
- [Theory](docs/theory.md): precise definitions; sections 1–4 are the core
- [Bole Challenge](docs/bole-challenge.md): call, race and publish one candidate
- [Harness Scout](docs/harness-scout.md): nomination signals, promotion ladder and scout card
- [Scout Calibration](docs/scout-calibration.md): hard gates, hit-rate metrics and leakage control
- [Scout Board](docs/scouts/README.md): current candidate stages and evidence gaps
- [Calibration ledger](docs/scouts/calibration-ledger.md): locked cohorts, misses and resolutions
- [Source sweep](docs/scouts/2026-08-19-source-sweep.md): exact-commit rerun of all 11 candidates
- [Execution Yield](docs/execution-yield.md): source-path audit, runtime evidence and product verdicts
- [Evidence matrix](docs/evidence.md): primary sources and reopening conditions
- [Case studies](docs/case-studies.md): concrete boundary decisions
- [Review guide](REVIEW_GUIDE.md): 5-minute, 30-minute and adversarial paths
- [Validation ledger](docs/validation/README.md): the full hostile research record
- [Empirical reproductions](experiments/README.md): pinned counterfactual tests

Status: **v1.0. The revised `3 + 1` model passed its promotion gate; the
original exhaustive four-constraint claim remains rejected.**
