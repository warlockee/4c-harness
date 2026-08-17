# The 4C Theory of AI Harness

> **Use 4C to build the smallest Harness that can execute your task—and to see
> exactly what an existing framework will and will not solve for you.**

A model call is not a task. A **Harness** is the engineering layer that turns
bounded, mostly stateless model calls into task execution across tools, state,
providers and time.

4C gives architects and coding agents four questions for deciding what Harness
machinery is actually necessary:

| 4C | Pressure | Engineering decision |
|---|---|---|
| **Cost** | Resources are finite | Budget, route, cache, compress, parallelize or stop? |
| **Compatibility** | Systems differ | Which model, provider, tool and protocol differences need adapters or negotiation? |
| **Continuity** | Tasks unfold through time | What state, lifecycle and recovery semantics must survive one model call? |
| **Cognition** | Past runs produce evidence | Which reusable execution policy should improve from prior runs? |

![The 3 + 1 structure of 4C](assets/diagrams/3-plus-1.svg)

Cost, Compatibility and Continuity shape current execution. Cognition is the
cross-run feedback plane. That is the complete 4C core.

## What 4C does for you

### When choosing an open-source Harness

4C replaces vague feature comparison with four concrete questions:

- Does the framework control the resource policy you actually care about?
- Does it preserve the provider/tool semantics your task depends on?
- Does it provide the state and lifecycle guarantees your task requires?
- Does it learn reusable policy from outcomes—or merely collect traces?

The result is a **fit profile**, not a universal score. A framework with fewer
activated Cs can be the better choice for a smaller task.

### When building your own Harness

4C prevents two common failures:

- **Underbuilding:** treating a multi-step, effectful task as a prompt plus a
  `while` loop.
- **Overbuilding:** adding routers, memory, workflow engines, multi-agent
  orchestration and self-improvement before the task requires them.

Start with zero optional machinery. Add one mechanism only when a 4C
counterfactual says execution policy must change.

### When debugging production agents

4C narrows the search:

- budget exhausted, latency cliff, context overflow → **Cost**;
- provider/tool/schema mismatch → **Compatibility**;
- lost state, unsafe retry, runaway loop, broken resume → **Continuity**;
- the same failure repeats despite accumulated evidence → **Cognition gap**.

Accuracy and permission failures are deliberately not hidden inside a C. See
[the minimum correctness boundary](#the-minimum-correctness-boundary).

## How high-visibility open-source Harnesses map to 4C

Start with the required first test case: DeepSeek Harness. The broader
matrix then covers projects with substantial adoption across coding agents,
agent runtimes, workflows and LLM application platforms. It evaluates
documented mechanisms, not project quality or popularity.
`Strong` means the project exposes substantial first-class machinery for that
pressure; `Partial` means some mechanisms exist but application policy still
does most of the work; `Evidence` means the project records or evaluates runs
without demonstrating automatic reusable policy change; `External` means bring
another component if the task activates that pressure.

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
important—but they satisfy the correctness and authority boundary around 4C;
they are not evidence of a fifth C. The harder conclusion is that plugin
architecture is a powerful answer to Compatibility and extensibility, not a
substitute for Cost policy or Cognition. For a single bounded model/tool path,
the same plugin tree may be unnecessary machinery.

This is a repository-level assessment of the current developer preview, whose
own documentation warns that compatibility-breaking changes are expected. See
its [architecture document](https://github.com/deepseek-ai/deepseek-harness/blob/master/docs/architecture.md)
for the underlying mechanisms.

### Broader comparison

| Open-source system | Cost | Compatibility | Continuity | Cognition | Best fit / 4C takeaway |
|---|---|---|---|---|---|
| [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) | Partial | **Strong** | **Strong** | Evidence | Plugin-native coding/agent Harness with replaceable services and an event-sourced session model. Extensibility is not automatic learning. |
| [Dify](https://github.com/langgenius/dify) | Partial | **Strong** | **Strong** | Evidence | Broad LLM application platform spanning workflows, RAG, agents, model management and observability. Powerful when those product surfaces are required; excessive for a narrow execution kernel. |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Partial | **Strong** | **Strong** | Evidence | Coding-agent Harness with sandboxed execution and lifecycle control. Evaluation evidence does not by itself make the execution policy self-improving. |
| [AutoGen](https://github.com/microsoft/autogen) | Partial | **Strong** | **Strong** | External | Multi-agent framework with model clients, tools and orchestration. Teams are justified only when roles require genuinely different context, tools or authority. |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Partial | **Strong** | **Strong** | External | Useful when crews, delegated tasks, flows and memory are intrinsic to the task. Multi-agent structure is overhead when one agent plus tools suffices. |
| [LlamaIndex](https://github.com/run-llama/llama_index) | Partial | **Strong** | Partial | External | Data-centric LLM application framework with integrations, agents and workflows. Use it when ingestion/retrieval semantics are central, not merely to wrap one model call. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Partial | Partial | **Strong** | Evidence | Best when checkpoint, interrupt/resume, replay and explicit state transitions dominate. Do not adopt it merely for a one-call tool wrapper. |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Partial | **Strong** | **Strong** | Evidence | Lightweight general agent loop with tools, handoffs, guardrails, sessions, HITL and tracing. Tracing is not automatic learning. |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | Partial | **Strong** | **Strong** | Evidence | Strong fit for typed Python, multi-provider execution, structured validation and optional durable workflows. Evals still need an adaptation step to become Cognition. |
| [smolagents](https://github.com/huggingface/smolagents) | Partial | **Strong** | Partial | External | Good minimal baseline for code/tool agents across models. Add durable state or learning only when the task proves it needs them. |

Visibility snapshot: **2026-08-16**. DeepSeek Harness (~132k GitHub stars),
Dify (~153k), OpenHands (~84k), AutoGen (~60k), CrewAI (~57k), LlamaIndex
(~52k), LangGraph (~40k), smolagents (~29k), OpenAI Agents SDK (~29k) and
Pydantic AI (~19k). Stars determine inclusion here, never the 4C assessment.
Counts are rounded and will drift; the links point to project-owned repositories.

How to read the table:

- **LangGraph is not “better” than smolagents** because it has stronger
  Continuity. It is better only when your task has temporal state and recovery
  requirements.
- **A trace or eval platform does not automatically activate Cognition.** It
  becomes Cognition only when prior-run evidence produces a reusable change to
  prompt assembly, retrieval, routing, tool, retry or stopping policy.
- **A product can span layers.** vLLM batching, kernels and GPU scheduling
  optimize model computation and remain Infrastructure; task-level model
  routing or retry policy belongs to the Harness.

For sourced mechanism-by-mechanism mappings, see the [evidence
matrix](docs/evidence.md) and [validation system
tranches](docs/validation/systems-tranche-01.md).

## Build the minimum viable Harness with 4C

### Step 1: Write the task contract before choosing a framework

Specify:

``` text
input          What starts one task execution?
success        What observable result means the task is complete?
effects        Which tools, files, services or people may it affect?
evidence       What current facts must the model be able to observe?
limits         What token, time, money and attempt envelope applies?
```

If these are unknown, framework selection is premature.

### Step 2: Run the four removal tests

| Remove this reality | If execution policy no longer needs to change | Build |
|---|---|---|
| Resource scarcity | Cost is inactive | No router/cache/budget optimizer beyond a hard safety limit |
| Semantic differences | Compatibility is inactive | One direct provider and one typed tool interface |
| Temporal dependence | Continuity is inactive | One bounded call; no checkpoint store or workflow engine |
| Reusable prior experience | Cognition is inactive | Emit evidence, but do not build an optimizer or self-modifying loop |

Only an observed policy delta activates a C. “We may need it someday” does not.

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
execution selected by 4C. Keeping them separate prevents a dangerous mistake:
a tool call can be cheap, compatible, stateful and learned—and still be wrong or
unauthorized.

## Three example scopes

| Task | Active 4C | Minimum design |
|---|---|---|
| Extract a typed record from one document | Cost only if the document can exceed the envelope; Compatibility only if providers vary | One model call, typed output validation, hard token limit; no agent loop or memory |
| Research across web and private documents | Cost + Compatibility + Continuity | Evidence retrieval, typed tools, bounded loop, explicit state/citations and stop rule; add checkpoints only if execution must resume |
| Autonomous coding task | Cost + Compatibility + Continuity; Cognition optional | Sandboxed tools, stateful loop, tests/postcondition checks, scoped permissions, budget/step stops; add Cognition only when traces update a versioned coding policy |

## What 4C is not

1. **Not a feature taxonomy.** One mechanism can answer several pressures.
2. **Not a complete requirements checklist.** Correctness and authority remain
   explicit boundaries.
3. **Not a maturity score.** More activated Cs usually mean a harder task, not a
   better Harness.
4. **Not a product taxonomy.** Classify mechanisms by the object and decision
   they control.

The original claim that four unavoidable constraints exhaust Harness
engineering did not survive hostile testing. The revision preserves the useful
`3 + 1` decision lens and rejects the overclaim.

## Read further

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
