# Core Four Symmetry Audit

Date: **2026-08-15**<br>
Status: **causal test passed; peer-constraint symmetry later falsified**

## Purpose

New candidates were required to pass counterfactual independence and layer
ownership tests. This audit applies the same burden to the original four. A
brand name is not evidence, and no C is protected from removal.

## Common test

For each C:

1. State the underlying reality without naming its mechanisms.
2. Construct a minimal case where that reality alone changes task execution.
3. Hold the other Cs and the three residual obligations constant.
4. Separate Application policy, Harness policy and Infrastructure mechanism.
5. Remove the C if no Harness-level causal residual remains.

The test does **not** require every Harness instance to activate every pressure.
A single-provider stateless wrapper may activate none of Compatibility,
Continuity or Cognition. “Persistent” means recurring across the domain;
“conditional” means activated only when its underlying reality affects the task.

## Cost attack

### Strongest attack

“Money” is neither necessary nor sufficient. A free local model still has a
context limit and latency; an expensive fixed call may offer no Harness choice.
GPU utilization, batching and kernels also respond to scarcity but primarily
belong to Infrastructure. Cost risks being a bag of unrelated optimization.

### Minimal residual

Use one provider, one stateless read-only task, no historical learning and fixed
authority/validity rules. The Harness can either spend one remaining model call
on more evidence or stop and answer. Changing only the remaining call budget
changes the valid execution policy.

The residual is not money. It is:

> Finite resources create tradeoffs among otherwise feasible task executions.

OpenAI's API exposes reasoning effort and truncation controls that change token
use, latency/cache behavior and what remains in context
([Realtime reference](https://platform.openai.com/docs/api-reference/realtime)).
Those controls become Harness concerns when selected according to task policy;
the provider's batching, cache storage and compute implementation remain
Infrastructure.

### Layer boundary

| Decision | Owner |
|---|---|
| Business budget, SLA or value of completion | Application |
| Model/context/route/attempt/stopping choice under that envelope | Harness |
| Kernel, GPU placement, continuous batching, device scheduling | Infrastructure |

### Verdict

**Survives, renamed at the semantic level.** The C may remain “Cost,” but its
underlying reality is **resource scarcity**, not money. It applies only where a
resource boundary changes task execution policy.

## Compatibility attack

### Strongest attack

Adapters and protocol clients exist throughout software. If ordinary
integration work counts as Harness Compatibility, the category has no layer
boundary. A one-model, one-tool system can also avoid it entirely.

### Minimal residual

Hold resources, history, task duration, evidence, validity and authority fixed.
Give two models the same intended operation but different supported tool-call
representations or capabilities. The Harness must translate, negotiate, choose
or fail differently solely because execution targets are semantically
heterogeneous.

MCP makes the mechanism explicit: initialization negotiates protocol versions
and optional client/server capabilities, and incompatible versions can terminate
the connection
([specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)).
The protocol implementation alone is not necessarily a Harness; using negotiated
capabilities to preserve task semantics is.

### Layer boundary

| Decision | Owner |
|---|---|
| Which product behavior is required | Application |
| How task semantics map across model/tool capabilities | Harness |
| Transport parsing, drivers and generic protocol serving | Infrastructure / integration substrate |

### Verdict

**Survives conditionally.** The reality is not “there are APIs,” but
**execution-relevant semantic heterogeneity**. Pure wire-format conversion with
no model-driven task-policy consequence is insufficient.

## Continuity attack

### Strongest attack

Databases, queues and workflow engines already provide persistence, retries and
scheduling. Calling them Continuity could merely relabel runtime infrastructure.
Moreover, a one-call task has no continuity requirement.

### Minimal residual

Use one provider with ample resources and no learning. A task performs model
proposal A, receives a tool result, then performs proposal B whose meaning
depends on A and that result. Even with no crash or delay, the Harness must
preserve task state and decide the valid next transition. Removing temporal
semantics changes the task, not merely its implementation.

LangGraph separates the two levels in practice. Its checkpointer persists graph
state and permits resume, replay and fault recovery; snapshots also record the
next nodes and step history
([persistence](https://docs.langchain.com/oss/python/langgraph/persistence)).
The database is a substrate. Which state is task-relevant, whether replay is
safe, and where execution resumes are Harness semantics.

### Layer boundary

| Decision | Owner |
|---|---|
| Task goal and business workflow | Application |
| State meaning, transition, stop/retry/resume/compensation semantics | Harness |
| Durable storage, queueing, worker recovery and clocks | Runtime / Infrastructure |

### Verdict

**Survives conditionally.** The reality is **temporal extension and dependence
across bounded operations**, not persistence technology. Failure is not required;
state-dependent multi-step execution is enough.

## Cognition result

The dedicated [Cognition attack](cognition-attack.md) found a parallel but
second-order residual: hold the future run constant and vary only retained
experience; if future Harness policy changes, Cognition is active. Evidence
storage or scoring without policy adaptation does not qualify.

## Symmetric result

| C | Durable reality | Harness-owned policy delta | Excluded neighbor |
|---|---|---|---|
| Cost | Resource scarcity | Allocate model calls, context, routes, attempts and stopping | Compute optimization itself |
| Compatibility | Semantic heterogeneity | Preserve task meaning across capabilities and targets | Generic protocol plumbing |
| Continuity | Temporal extension/dependence | Preserve state and task-valid transitions | Persistence substrate itself |
| Cognition | Reusable experience | Change future execution policy from past evidence | Tracing, current validation or weight training alone |

All four survive the causal policy-delta test. None is unavoidable in every
Harness instance, and none owns every mechanism associated with its vocabulary.
The later [optimizer attack](optimizer-cognition-boundary-attack.md) shows that
this does not make them the same type: Cognition is an endogenous feedback
operator, while the other three are exogenous operational pressures.

## Theory correction forced by the audit

The causal-audit statement was:

> 4C identifies four recurrent, independently activatable realities that cause
> Harness execution policy to vary: scarcity, heterogeneity, temporal extension
> and experience.

The later optimizer attack supersedes any implication of type symmetry. The
current formulation is three exogenous operational pressures plus one endogenous
feedback plane.

The words **unavoidable constraints** and the equation **Money → Cost** are too
strong. The audit supports a causal coordinate system, not a complete checklist
and not a claim that every coordinate is active in every system.
