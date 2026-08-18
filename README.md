# A new Harness shipped. Should you switch?

> **4C turns that question into two answers: whether the new Harness changes
> any decision your task actually forces, and what the migration would cost,
> line by line.**

You are already running something. A new Harness appears, it looks better, and
the two things you want are an evaluation and a migration estimate. Neither is
served by what is currently available.

| Signal you have today | What it answers | What it leaves open |
|---|---|---|
| Task benchmarks (SWE-bench, Aider's benchmark, OSWorld, WebArena) | How well a model and Harness scored on someone else's task distribution | Whether it changes anything for *your* task, and how much of the score is the model |
| Feature matrix and docs | Which mechanisms exist | Whether you need them, and what you would rebuild |
| Stars, release cadence, demos | Attention and maintenance | Fit, and the cost of leaving what you have |
| **4C** | Which of your execution decisions the switch would change, and what carries over | Usability, latency, output quality, how good it feels to use |

A model call is not a task. A **Harness** is the engineering layer that turns
bounded, mostly stateless model calls into task execution across tools, state,
providers and time. Two Harnesses differ only where they take a different
execution decision. 4C names the four reasons a decision has to change, so
"should I switch" becomes a diff instead of an impression.

## Evaluate the candidate

Hand this to your coding agent. It works on any Harness, not just the ones
profiled below.

``` text
Read https://github.com/warlockee/4c-harness (README, then docs/theory.md
sections 1-4).

Current Harness: <what you run today>
Candidate Harness: <the new one>
My task: <input, success condition, effects, required evidence, hard limits>

Produce:
1. Activation profile. Which of Cost / Compatibility / Continuity / Cognition
   does my task actually activate? For each, state the exact policy delta.
   Deleting the pressure must change a decision, or it is inactive.
2. Difference table. For each activated pressure only, what does the candidate
   decide differently from my current Harness? Cite documented mechanisms, not
   marketing.
3. Verdict: stay, switch, or adopt for one subtask. An inactive pressure where
   the candidate is stronger is not a reason to switch.
4. What the benchmarks did not measure for my case.
```

An inactive pressure is the most common finding, and it is the one that saves
the migration. A candidate with a stronger router changes nothing if your token
envelope never binds.

## Price the migration

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

## Profiles for the systems most people are comparing

Pre-computed, so you can skip the analysis if your candidate is here. These
evaluate documented mechanisms, not project quality or how good the software is
to use.

| Open-source system | Cost | Compatibility | Continuity | Cognition | Best fit |
|---|---|---|---|---|---|
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Partial | **Strong** | **Strong** | Evidence | Plugin-native coding/agent Harness with replaceable services and an event-sourced session model. Extensibility is not automatic learning. |
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
another component. Table eligibility is 30k+ GitHub stars, an OSI-approved
license and activity in the prior six months; live counts and sources are in the
[selection audit](docs/validation/popular-harness-selection.md).

## The method behind the answers

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

## If you are building rather than switching

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

## Case study: DeepSeek Harness

A useful test because its claim is architectural. Model adapters, tools,
persistence, sandboxing, approval policy and the agent loop are all plugins
rather than a privileged core.

| 4C pressure | Assessment | What the documented architecture shows |
|---|---|---|
| **Cost** | Partial | Prompt assembly, telemetry and stopping give control points, but no closed-loop budget, routing or cache policy. |
| **Compatibility** | **Strong** | Plugin-defined model adapters, tool registries and capability providers make the seams explicit and replaceable. |
| **Continuity** | **Strong** | An append-only session-event log supports reconstruction, persistence, resume, fork and recovery. |
| **Cognition** | Evidence | Logs, telemetry and benchmarks supply evidence; nothing automatically turns outcomes into a versioned future policy. |

What a feature list would miss: plugin architecture is a powerful answer to
Compatibility, not a substitute for Cost policy or Cognition, and for a single
bounded model/tool path the same plugin tree is unnecessary machinery. Its
guarded tool pipeline, sandbox and approvals matter, but they satisfy the
boundary you always own rather than adding a fifth C. See its
[architecture document](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
for the mechanisms; this assesses a developer preview whose own documentation
warns that breaking changes are expected.

## Why these classifications are worth acting on

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

## Read further

- [Glossary](docs/glossary.md): every term in one plain sentence
- [Theory](docs/theory.md): precise definitions; sections 1–4 are the core
- [Evidence matrix](docs/evidence.md): primary sources and reopening conditions
- [Case studies](docs/case-studies.md): concrete boundary decisions
- [Review guide](REVIEW_GUIDE.md): 5-minute, 30-minute and adversarial paths
- [Validation ledger](docs/validation/README.md): the full hostile research record
- [Empirical reproductions](experiments/README.md): pinned counterfactual tests

Status: **v1.0. The revised `3 + 1` model passed its promotion gate; the
original exhaustive four-constraint claim remains rejected.**
