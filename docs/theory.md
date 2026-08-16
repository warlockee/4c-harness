# The 4C Theory of AI Harness

> **v1.0 promotion result:** the original exhaustive four-constraint claim is
> falsified by independent Epistemic Access, Validity and Authority residuals.
> The revised composed Harness model below passed hostile validation, source
> hardening and representative executable counterfactuals. Its `3 + 1`
> component is not a complete inventory of Harness requirements. See the
> [final audit](validation/v1-final-falsification-audit.md).

**Reading boundary:** Sections 1–4 contain the complete 4C core. Sections 5–7
clarify scope. Sections 8–10 document the optional adversarial model used to
test where 4C stops; they are not extra Cs and are not prerequisites for using
the lens.

## 1. Definition

A **Harness** is the engineering layer between model computation and
application behavior. Its unit of concern is not a forward pass but an
**execution**: a task spanning model calls, tools, state transitions,
retries, context transformations, checkpoints, human decisions and
outcomes.

> Infrastructure asks: **how do we execute a model call?**\
> Harness asks: **how do we execute a task using model calls?**

This distinction is mechanism-level. vLLM documents inference-serving concerns
such as PagedAttention, continuous batching and optimized kernels
([source](https://docs.vllm.ai/en/latest/)); the OpenAI Agents SDK runner instead
manages task turns, tools, handoffs and final output
([source](https://openai.github.io/openai-agents-python/running_agents/)). A
single product can span both surfaces.

Diagram source: [layer boundary](../assets/diagrams/layer-boundary.mmd).

## 2. Three operational pressures plus one feedback plane

Each C names a durable direction of execution-policy variation. They are not
four equivalent constraints and are not claimed to cover every Harness
obligation, lifecycle stage or quality property.

Cost, Compatibility and Continuity are **exogenous operational pressures** on
current execution. Cognition is the **endogenous feedback plane** that changes
future policy from execution evidence.

Diagram source: [3 + 1](../assets/diagrams/3-plus-1.mmd).

### Cost --- resource semantics

Resources are finite. Money is one resource signal, alongside tokens, latency,
compute, context, concurrency and attempts. Their bounds can change which task
execution policy is feasible or preferable.

**Cost engineering compiles resource constraints into task execution policy.**

Mechanisms include caching, compression, summarization, truncation,
routing, model cascades, task-level parallelism/speculation, token budgets and
context shaping.

The layer boundary is causal: choosing a model, context or stopping rule because
of a task resource envelope is Harness Cost; optimizing kernels, GPU placement
or continuous batching is Infrastructure even when it reduces monetary cost.
Provider controls such as reasoning effort and context truncation demonstrate
task-visible resource choices
([source](https://platform.openai.com/docs/api-reference/realtime)).

### Compatibility --- heterogeneous semantics

Models, providers, tools, schemas, protocols and environments differ in ways
that can change task execution semantics.

Compatibility absorbs accidental differences while preserving useful
provider-specific capabilities.

Mechanisms include adapters, canonical message formats, schema
normalization, capability negotiation, tool calling, structured output,
MCP, A2A and fallback.

Generic protocol plumbing is not automatically Harness Compatibility. The
Harness concern begins where translation, negotiation or selection must preserve
model-driven task meaning or capability.
Grammar-constrained decoding inside an inference server remains Infrastructure;
semantic acceptance of the decoded result is Validity.
MCP's version/capability negotiation and A2A's capability/modality discovery are
documented examples of execution-relevant heterogeneity
([MCP](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle),
[A2A](https://a2a-protocol.org/latest/specification/)).

### Continuity --- temporal semantics

Models are mostly stateless; tasks are stateful.

Continuity has two inseparable parts:

**State:** context, task state, tool state, filesystem/environment
state, memory, checkpoints.

**Lifecycle control:** stop conditions, retries, loop detection, temporal
timeouts, branching, fork/rewind, rollback, suspension, resumption and recovery.

"Control" here is deliberately temporal, not a claim that every rule governing
execution belongs to Continuity. Resource limits belong to Cost; capability
negotiation to Compatibility; result acceptance and action permission remain
open validation questions.

> **Loop lifecycle engineering is Continuity engineering.**

Persistence of task state is a Continuity primitive. Memory used to select
current evidence also involves Epistemic Access; memory transformed into
reusable future policy can involve Cognition. Context Engineering commonly spans
Cost + Continuity + Epistemic Access.

Persistence technology alone is a runtime substrate. Continuity at the Harness
layer determines what state means and which stop, retry, resume, replay or
compensation transition preserves the task.
LangGraph checkpoint/replay and Temporal event-history replay demonstrate this
substrate/semantics distinction
([LangGraph](https://docs.langchain.com/oss/python/langgraph/persistence),
[Temporal](https://docs.temporal.io/workflow-execution)).

### Cognition --- experiential semantics

Cognition means **system cognition**, not model intelligence.

It asks how future execution should improve because of past execution.

``` text
Observe → Reconstruct → Evaluate → Diagnose → Learn → Adapt
```

Tracing and observability provide evidence. Evals judge outcomes.
Diagnosis attributes causes. Learning turns runs into reusable findings.
Adaptation changes future policies.

Operationally, Cognition exists only when past-run evidence causes a reusable
change to future Harness policy—for example prompt/context assembly, retrieval,
routing, tool policy, retry or stopping. A stored trace is only observability;
a current-run score is Validity; a model-weight update belongs primarily to
model training.

> **Observability records experience. Cognition compounds it.**

Reflexion reuses stored linguistic feedback in later trials without changing
weights, while DSPy compiles examples and metrics into changed program
parameters
([Reflexion](https://arxiv.org/abs/2303.11366),
[DSPy](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html)).

## 3. Why 4C is not MECE

4C models **causes of execution-policy variation**, not code modules. A
feature can respond to multiple causes.

Compression may serve Cost and Continuity. Routing may serve Cost,
Compatibility and Cognition. A trace supports Cognition but is not
sufficient for Cognition.

The test is: **because of which reality must execution policy change?** This
test does not classify Observation or Mediation obligations merely because they
also constrain execution.

## 4. The 3 + 1 structure

-   **Scarcity → Cost:** execution resources are finite.
-   **Difference → Compatibility:** systems are heterogeneous.
-   **Time → Continuity:** tasks outlive one inference.
-   **Experience → Cognition:** past execution can provide evidence for a
    reusable future policy update.

Implementations can change while these realities persist.

Each pressure is conditional, not present in every minimal Harness. A fixed,
single-call system may activate none of Compatibility, Continuity or Cognition.
The claim is that these realities recur independently across Harness systems,
not that every product must implement every C.

The first three realities constrain execution when activated. Experience does
not impose the same kind of current-run constraint: Cognition is the optional
adaptation operator that turns historical evidence into a reusable policy
change. This asymmetry is part of the theory, not hidden for naming symmetry.

## 5. Causal coordinates, not a maturity ladder

Real systems can activate one operational pressure without another, and can
implement Cognition weakly or not at all. The coordinates describe why policy
varies; they do not rank products. An adapter is not “below” a runtime, and an
eval platform is not “above” a Harness merely because it supplies feedback.

## 6. Cognition as the feedback learning plane

The first three Cs shape execution. Cognition learns from execution and
can update them.

``` text
Execution → Evidence → Diagnosis → Learning → Policy
   ↑                                           ↓
   └──────── Cost / Compatibility / Continuity ┘
```

At maturity, Cognition becomes the harness's **learning plane**.

This makes Cognition structurally different from the first three Cs. Cost,
Compatibility and Continuity directly shape current execution; Cognition feeds
outcomes back into later policy. It remains in 4C because the taxonomy tracks
independent causes of policy variation, not equivalent lifecycle stages.

## 7. Scope

4C explains model-driven execution. It does not attempt to replace model
research, low-level inference engineering, accelerator/datacenter
infrastructure, product strategy, UX, business logic, market strategy or
organizational design.

Security, identity, permissions, governance and safety are often
cross-cutting concerns and should not be forced into a C merely to
preserve the acronym.

Validation has shown that this scope sentence is insufficient by itself:
Harness-level permission mediation cannot be dismissed merely because security
is cross-cutting. 4C now makes the narrower `3 + 1` claim: Cost, Compatibility
and Continuity are operational pressures, while Cognition is the feedback
learning plane. It does **not** claim that they exhaust what a Harness must
observe, validate or authorize.

## 8. Advanced validation model (not part of 4C)

To search for counterexamples outside the 4C lens, validation uses a mediated
transition system:

``` text
Harness validation model
  = mediated transition system       (what execution does)
  + boundary obligations             (what may enter, occur or leave)
  + 3 + 1 causal lens                (why Harness policy varies)
```

This composition is a test fixture, not the public 4C definition. Calling the
`3 + 1` lens alone a complete Harness architecture is a category error;
conversely, forcing Epistemic Access, Validity or Authority into the acronym
would hide the failure of the original exhaustive claim.

Diagram source: [mediated transition system](../assets/diagrams/mediated-transition-system.mmd).

``` text
Application intent / policy
           ↓
state + evidence + events
       ├→ select candidate(s) → mediate → apply / expose
       └← correlated outcome / error / cancellation ←┘

operational plane: Cost · Compatibility · Continuity
feedback plane: Cognition
```

This abstraction is induced from mechanisms rather than asserted from one
framework: Agents SDK supplies model/code/human transitions and recurring
guardrails; Temporal and Inngest supply external events, concurrency, replay and
late completion
([Agents SDK](https://openai.github.io/openai-agents-python/guardrails/),
[Temporal](https://docs.temporal.io/encyclopedia/workflow-message-passing),
[Inngest](https://www.inngest.com/docs/learn/how-functions-are-executed)).

- **Observation / Epistemic Access:** what evidence selection and inference can
  condition on, including its source, identity, freshness and provenance;
  observation recurs throughout execution.
- **3 + 1:** how scarcity, difference and time pressure current execution, and
  how experience can update later policy.
- **Selection:** a model, deterministic policy or human proposes the next
  transition; environment/system events can also make transitions eligible.
- **Mediation / Validity:** whether evidence, the candidate transition or its
  observed outcome satisfies the task predicate; applying an action does not
  prove its intended postcondition occurred.
- **Mediation / Authority:** whether the authenticated principal and delegation
  may cause or expose the effect, for the intended scope and audience.
- **Apply / expose:** execution or exposure of an admitted tool, state or output
  transition, including temporal recovery.

Browser/desktop environments make the postcondition distinction concrete:
OSWorld evaluates resulting computer state rather than treating dispatch as
success, and Voyager consumes environment feedback, execution errors and
self-verification
([OSWorld](https://arxiv.org/abs/2404.07972),
[Voyager](https://arxiv.org/abs/2305.16291)).

These are not asserted to be final or MECE. They state the current falsification
boundary: Observation, Validity and Authority may not be reduced to 4C without
new evidence.

The three parts answer different questions and therefore must not be counted as
peer categories:

| Part | Question | Failure if omitted |
|---|---|---|
| Transition system | What operation advances or exposes execution? | The model cannot represent the run topology. |
| Boundary obligations | Is the evidence/action/output knowable, acceptable and permitted? | An executable transition is mistaken for a legitimate one. |
| 3 + 1 lens | Which recurring reality changes execution policy? | Mechanisms are listed without a causal explanation. |

This composition is the current completeness claim: not that its labels
enumerate every feature or quality, but that every recurring Harness-owned
decision should be representable as a transition, mediated by the applicable
boundary obligations, with any 4C classification limited to causal policy
variation. A residual at any of those three levels triggers the kill criteria
below.

The system may have zero, one or many transitions in flight. A sequential agent
loop is one topology, not the theory itself. Correlation, causal ordering,
idempotency, cancellation and compensation are Continuity semantics at task
level; their queue, clock and storage implementations may be runtime
Infrastructure.

Policy, validator, skill, tool and permission changes are themselves candidate
transitions over versioned artifacts. They require evidence, Validity, Authority
and lifecycle semantics just like world-facing actions. Cognition may propose or
learn a reusable policy delta, but it cannot by itself legitimate a changed
success predicate or grant itself new authority; the root predicate and
delegation come from the Application/principal boundary for the execution under
analysis.

For multi-principal systems, A2A separates authentication from server-specific
authorization, while MCP requires audience-bound credentials and forbids token
passthrough
([A2A](https://a2a-protocol.org/latest/specification/),
[MCP](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)).

The full claim-to-source mapping and evidence limits are maintained in the
[evidence matrix](evidence.md).

## 9. Classification procedure

Apply the theory to a mechanism in this order:

1. **Name the execution unit.** Is it a model request, user task, agent task,
   evaluation run or deployment transition?
2. **Name the controlled object.** Model computation points toward
   Infrastructure; model-driven task state/action/output points toward Harness;
   user value and success policy point toward Application.
3. **State the counterfactual policy delta.** What decision changes, with all
   other candidate causes held fixed?
4. **Classify current operational pressure.** Resource boundary → Cost;
   execution-relevant semantic difference → Compatibility; temporal
   state/dependence → Continuity.
5. **Classify feedback.** Only a reusable future Harness-policy change caused by
   prior execution evidence → Cognition.
6. **Classify boundary obligation.** Missing/unattributable evidence → Epistemic
   Access; truth, integrity, acceptance or postcondition → Validity; principal,
   delegation, scope, audience or permission → Authority.
7. **Reject category errors.** A mechanism, architecture pattern, quality
   outcome or organizational process does not become a fundamental category
   until it leaves an independent execution decision under counterfactual
   removal.

A single mechanism can receive multiple classifications, but one causal reason
must not be counted twice. For example, a timeout used to cap spend is Cost; the
state transition that terminates the run consistently is Continuity. A test
failure supplies Validity; carrying out another attempt is Continuity.

## 10. Kill criteria

The revised model must be changed or abandoned if any of these occur:

1. a recurring Harness-owned current-execution policy delta survives removal of
   scarcity, semantic heterogeneity and temporal dependence;
2. reusable cross-run Harness-policy learning cannot be distinguished from
   observability, current-run Validity, Application development or Model
   training;
3. a recurring execution operation cannot be represented as evidence/state/event
   update, candidate selection, boundary mediation, apply/expose or correlated
   outcome;
4. a recurring evidence, acceptance or permission decision cannot be separated
   into Epistemic Access, Validity or Authority without losing predictive
   information;
5. mechanism-level layer ownership cannot be applied consistently across
   systems that span Model, Infrastructure, Harness and Application;
6. the classifications fail to predict different engineering behavior or
   failure modes better than a simpler rival model.

Passing examples never proves exhaustiveness. A counterexample that satisfies
one kill criterion outranks any number of friendly mappings.

## 11. Thesis

> **Models create intelligence. Infrastructure creates computation.
> Harnesses create execution. Applications create user value.**

As models commoditize, complexity does not disappear. It moves into the
harness.

The 4C lens explains three operational directions and one feedback direction of
that complexity. The broader Harness execution model composes that lens with
boundary mediation and transition structure; neither is a feature inventory.
