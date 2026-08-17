# The 4C Theory of AI Harness

> **Build the smallest Harness that can execute your task — and see exactly what
> an existing framework will and will not solve for you.**

A model call is not a task. A **Harness** is the engineering layer that turns
bounded, mostly stateless model calls into task execution across tools, state,
providers and time.

## What this changes for you

Most agent projects fail in one of two directions: a multi-step effectful task
built as a prompt plus a `while` loop, or a document extractor carrying a
router, a vector store, a workflow engine and a multi-agent layer it never
needed. 4C is a test for telling those apart before you commit.

**Delete a reality from your task. Does a decision still have to be made?**

| Delete this | If nothing changes | Then don't build |
|---|---|---|
| Resource scarcity — make it free, instant, unlimited | Cost is inactive | Router, cache, budget optimizer beyond one hard stop |
| Semantic difference — one provider, one tool schema | Compatibility is inactive | Adapters, capability negotiation, fallback |
| Time — one call, no history, no resume | Continuity is inactive | Checkpoint store, workflow engine, durable runtime |
| Prior experience — no past runs to learn from | Cognition is inactive | Optimizer, self-modifying loop, memory system |

Worked example. *Extract a typed record from one uploaded invoice.* Free and
instant? Still fine — Cost inactive. One provider? Still fine — Compatibility
inactive. One call, no resume? Still fine — Continuity inactive. So the correct
build is one model call, typed output validation and a token ceiling. Not an
agent loop, not memory, not a framework. If the invoice can exceed the context
window, Cost activates and you add exactly one mechanism: a size check and a
stop.

That is the whole method. The rest of this repository is the argument for why
those four questions, and the record of trying to break it.

| 4C | Pressure | The decision it governs |
|---|---|---|
| **Cost** | Resources are finite | Budget, route, cache, compress, parallelize or stop? |
| **Compatibility** | Systems differ | Which model, provider, tool and protocol differences need adapters or negotiation? |
| **Continuity** | Tasks unfold through time | What state, lifecycle and recovery semantics must survive one model call? |
| **Cognition** | Past runs produce evidence | Which reusable execution policy should improve from prior runs? |

![The 3 + 1 structure of 4C](assets/diagrams/3-plus-1.svg)

Cost, Compatibility and Continuity shape current execution. Cognition is the
cross-run feedback plane. That is the complete 4C core.

Two more places it pays off:

- **Choosing a framework.** You get a *fit profile*, not a score. Ask whether
  the framework controls the resource policy you care about, preserves the
  provider semantics your task depends on, gives the state guarantees you need,
  and learns from outcomes or merely records them. A framework with fewer
  activated Cs is often the better choice.
- **Debugging production agents.** Budget exhausted, latency cliff, context
  overflow → **Cost**. Provider, tool or schema mismatch → **Compatibility**.
  Lost state, unsafe retry, runaway loop, broken resume → **Continuity**. The
  same failure repeating despite accumulated evidence → **Cognition gap**.
  Wrong answers and unpermitted actions are deliberately *not* inside a C — see
  [the minimum correctness boundary](#the-minimum-correctness-boundary).

## Why you should — and shouldn't — trust this

Frameworks-as-theory are cheap to publish and hard to check. Here is the honest
ledger, so you can decide how much weight to put on it.

**The theory already broke once, and the break is published.** The original
claim was that four constraints *exhaust* Harness engineering. Hostile testing
found three decisions that survive removing all four: whether the model can see
the facts it needs (**Epistemic Access**), whether a result is actually correct
(**Validity**), and whether this principal may cause this effect (**Authority**).
That claim is [rejected in the canonical documents](docs/theory.md) rather than
quietly renamed, and two published predictions record their own falsification.
A framework that had never failed a test would be the more worrying artifact.

**Some of it is executable.** Six experiments in [`experiments/`](experiments/README.md)
run pinned upstream packages and check a claimed policy delta. They also carry
an explicit evidence level, because running real code is not automatically
independent evidence:

| Evidence level | Experiments | Weight |
|---|---|---|
| Third-party behaviour | LiteLLM translation, Codex sandbox enforcement, ONNX Runtime computation policy | Independently supports the classification |
| Instrumented illustration | LangGraph authority/continuity, Autoevals cognition boundary | Shows the distinction is mechanisable; does not corroborate it |
| Declared interface | Codex/Claude control surfaces | Shows the surface exists; enforcement untested |

Three of six independently support a classification. The Authority and
Cognition boundaries currently rest on desk research plus one genuine
enforcement observation.

**What is still weak.** Most system mappings are desk research over vendor
documentation, which shows a mechanism is claimed, not that it works. And every
rejected rival category — Reliability, Coordination, Planning, Control,
Uncertainty — was rejected by the same authors who defined the categories. No
attack in the ledger was authored by someone with an interest in 4C failing.
Both limits are recorded in the [evidence matrix](docs/evidence.md#evidence-limits).

**It states how to kill it.** [Six kill criteria](docs/theory.md#10-kill-criteria)
and per-claim reopening conditions are published. The shortest version: find a
recurring Harness decision that survives removing scarcity, difference, time and
prior experience, and the model reopens. One counterexample outweighs every
successful mapping here — that is what the [review guide](REVIEW_GUIDE.md) asks
you for.

## Build the minimum viable Harness with 4C

### Step 1: Write the task contract before choosing a framework

``` text
input          What starts one task execution?
success        What observable result means the task is complete?
effects        Which tools, files, services or people may it affect?
evidence       What current facts must the model be able to observe?
limits         What token, time, money and attempt envelope applies?
```

If these are unknown, framework selection is premature.

### Step 2: Run the four removal tests

Use the table at the top of this file. Only an observed policy delta activates
a C. "We may need it someday" does not.

### Step 3: Add the smallest mechanism for each active C

| Active pressure | Minimum useful mechanism | Add later only when proven necessary |
|---|---|---|
| Cost | usage accounting + hard budget/stop | routing, caching, compression, speculative parallelism |
| Compatibility | typed model/tool boundary | multi-provider adapters, capability negotiation, fallback |
| Continuity | explicit state + step limit + terminal states | durable checkpoints, replay, fork, compensation, distributed workflow runtime |
| Cognition | traces + outcome labels + versioned policy artifact | automated diagnosis, optimization, rollout and rollback |

The minimal Harness is therefore usually not a framework. It is a small
execution kernel:

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

Give the implementation agent this brief:

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

This prompt makes an agent optimize for **necessary execution semantics**, not
for framework-shaped code.

## The minimum correctness boundary

4C tells you **why execution policy changes**. It does not by itself make an
agent accurate or safe. Every effectful Harness still needs three checks:

- **Epistemic Access:** did the model observe the task-relevant, attributable
  and sufficiently fresh evidence?
- **Validity:** do the input, proposed action, output and observed postcondition
  satisfy the task contract?
- **Authority:** may this principal cause or expose this effect for this scope
  and audience?

These checks are not extra Cs. They are the minimum boundary around the
execution selected by 4C, and they are exactly the residuals that falsified the
original exhaustive claim. Keeping them separate prevents a dangerous mistake: a
tool call can be cheap, compatible, stateful and learned — and still be wrong or
unauthorized.

## Three example scopes

| Task | Active 4C | Minimum design |
|---|---|---|
| Extract a typed record from one document | Cost only if the document can exceed the envelope; Compatibility only if providers vary | One model call, typed output validation, hard token limit; no agent loop or memory |
| Research across web and private documents | Cost + Compatibility + Continuity | Evidence retrieval, typed tools, bounded loop, explicit state/citations and stop rule; add checkpoints only if execution must resume |
| Autonomous coding task | Cost + Compatibility + Continuity; Cognition optional | Sandboxed tools, stateful loop, tests/postcondition checks, scoped permissions, budget/step stops; add Cognition only when traces update a versioned coding policy |

## Applied: how high-visibility open-source Harnesses map to 4C

This section demonstrates the lens on real systems. It evaluates documented
mechanisms — not project quality, popularity or how good the software is to use.

Grades for Cost, Compatibility and Continuity: `Strong` means substantial
first-class machinery; `Partial` means mechanisms exist but application policy
still does most of the work; `External` means bring another component.
Cognition uses its own three rungs — `Evidence` (records runs), `Adaptive`
(prior outcomes automatically change live policy) and `Strong` (evidence
produces a versioned, reusable policy artifact) — defined in the
[selection audit](docs/validation/popular-harness-selection.md#how-cognition-is-graded).

### 1. DeepSeek Harness: the first 4C analysis

[DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) is an
especially useful attack on 4C because its claim is architectural: **everything
is a plugin**. Model adapters, tools, persistence, sandboxing, approval policy
and the agent loop are composed as replaceable services rather than hidden in a
privileged core.

| 4C pressure | Assessment | What the documented architecture shows |
|---|---|---|
| **Cost** | Partial | Prompt assembly, telemetry and stopping provide control points, but the architecture does not itself demonstrate a closed-loop budget, routing or cache policy. |
| **Compatibility** | **Strong** | Plugin-defined model adapters, tool registries and capability providers make implementation seams explicit and replaceable. |
| **Continuity** | **Strong** | An append-only session-event log supports reconstruction, persistence, resume, fork and recovery across steps and turns. |
| **Cognition** | Evidence | Logs, telemetry and benchmarks can supply learning evidence; no documented mechanism automatically turns outcomes into a versioned future execution policy. |

Its guarded tool pipeline, sandbox, approvals and validation hooks are also
important — but they satisfy the correctness and authority boundary around 4C;
they are not evidence of a fifth C. The harder conclusion is that plugin
architecture is a powerful answer to Compatibility and extensibility, not a
substitute for Cost policy or Cognition. For a single bounded model/tool path,
the same plugin tree may be unnecessary machinery.

This is a repository-level assessment of the current developer preview, whose
own documentation warns that compatibility-breaking changes are expected. See
its [architecture document](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
for the underlying mechanisms.

### Like-for-like comparison

Only highly visible, open-source systems that directly run agent tasks appear
here. Application platforms, data frameworks and libraries for building a
Harness are held out of this cohort.

| Open-source system | Cost | Compatibility | Continuity | Cognition | Best fit / 4C takeaway |
|---|---|---|---|---|---|
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Partial | **Strong** | **Strong** | Evidence | Plugin-native coding/agent Harness with replaceable services and an event-sourced session model. Extensibility is not automatic learning. |
| [Codex](https://github.com/openai/codex) | Partial | **Strong** | **Strong** | Evidence | Open-source coding Harness with sandboxed tools, approval policy, MCP/skills and resumable sessions. Configuration and traces do not by themselves create Cognition. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | **Strong** | **Strong** | **Strong** | Evidence | Coding Harness with model routing, token caching, MCP/extensions, sandboxing, checkpointing and session management. Its broad coverage is useful only when the task activates it. |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Partial | **Strong** | **Strong** | Evidence | Coding-agent Harness with sandboxed execution and lifecycle control. Evaluation evidence does not by itself make the execution policy self-improving. |
| [Cline](https://github.com/cline/cline) | Partial | **Strong** | **Strong** | Evidence | Coding Harness across IDE, CLI and SDK with many model providers, plugins/MCP, checkpoints and persistent agent state. Multi-agent and scheduled automation can be unnecessary for smaller tasks. |
| [Aider](https://github.com/Aider-AI/aider) | Partial | **Strong** | Partial | Evidence | Focused terminal coding Harness with broad model support, repository maps, git-backed edits/undo and a public benchmark. Its smaller profile is often an advantage. |
| [browser-use](https://github.com/browser-use/browser-use) | Partial | **Strong** | Partial | Evidence | Domain-specific browser Harness with provider choice, custom tools, persistent browser resources and an open benchmark. Browser specialization should not be mistaken for general Harness completeness. |

### Ecosystem coverage cases

The cohort above would overrepresent coding agents. These four cover distinct
adjacent architectures that can own Harness mechanisms, and are listed
separately because their product units are not comparable with a terminal or IDE
agent.

| Representative system | Archetype | Cost | Compatibility | Continuity | Cognition | Why it matters to 4C |
|---|---|---|---|---|---|---|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Stateful agent runtime | Partial | Partial | **Strong** | Evidence | Tests whether explicit graph state, checkpoint, interrupt/resume and replay fit Continuity without turning durability into a universal requirement. |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Multi-agent orchestration framework | Partial | **Strong** | **Strong** | *Adaptive* | Tests whether roles, delegation, flows and memory introduce a fifth constraint; 4C instead predicts differences, shared temporal state and authority boundaries. |
| [Langflow](https://github.com/langflow-ai/langflow) | Visual agent/workflow platform | Partial | **Strong** | **Strong** | Evidence | Tests 4C against composed workflows, deployment and a large integration surface rather than one local agent loop. |
| [LiteLLM](https://github.com/BerriAI/litellm) | Model gateway | **Strong** | **Strong** | Partial | *Adaptive* | Tests the request/task boundary through cost tracking, routing, fallback, provider normalization, guardrails and logging. |

How to read both tables:

- **Gemini CLI is not "better" than Aider** because it exposes more first-class
  machinery. It is better only when your task requires that machinery.
- **A trace or eval platform does not automatically activate Cognition.** Only
  two systems here reach `Adaptive`, and none reaches `Strong` — a claim that
  should be corrected if a project documents otherwise.
- **A product can span layers.** vLLM batching, kernels and GPU scheduling
  optimize model computation and remain Infrastructure; task-level model routing
  or retry policy belongs to the Harness.

Eligibility is at least 30k GitHub stars, an OSI-approved license on the
relevant mechanism code, and activity in the prior six months. Stars gate
admission, never the assessment. Live counts, licenses and grading rationale are
in the [selection audit](docs/validation/popular-harness-selection.md), kept
current by `tools/visibility_check.py`. For sourced mechanism-by-mechanism
mappings, see the [evidence matrix](docs/evidence.md) and
[validation tranches](docs/validation/systems-tranche-01.md).

## What 4C is not

1. **Not a feature taxonomy.** One mechanism can answer several pressures.
2. **Not a complete requirements checklist.** Correctness and authority remain
   explicit boundaries.
3. **Not a maturity score.** More activated Cs usually mean a harder task, not a
   better Harness.
4. **Not a product taxonomy.** Classify mechanisms by the object and decision
   they control.

## Read further

- [Glossary](docs/glossary.md) — every term in one plain sentence; start here if
  the vocabulary gets heavy
- [Theory](docs/theory.md) — precise definitions; sections 1–4 are the core
- [Review guide](REVIEW_GUIDE.md) — 5-minute, 30-minute and adversarial paths
- [Evidence matrix](docs/evidence.md) — primary sources and reopening conditions
- [Case studies](docs/case-studies.md) — concrete boundary decisions
- [Validation ledger](docs/validation/README.md) — full hostile research record
- [Empirical reproductions](experiments/README.md) — pinned counterfactual tests

> **Try to break 4C before promoting 4C.** A recurring Harness-owned policy
> cause outside scarcity, semantic difference, temporal dependence and reusable
> experience reopens the theory.

Status: **v1.0 promotion gate passed for the revised, explicitly falsifiable
theory. The original exhaustive formulation remains rejected.**
