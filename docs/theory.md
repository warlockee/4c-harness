# The 4C Theory of AI Harness

## 1. Definition

A **Harness** is the engineering layer between model computation and
application behavior. Its unit of concern is not a forward pass but an
**execution**: a task spanning model calls, tools, state transitions,
retries, context transformations, checkpoints, human decisions and
outcomes.

> Infrastructure asks: **how do we execute a model call?**\
> Harness asks: **how do we execute a task using model calls?**

## 2. Four unavoidable constraints

### Cost --- economic semantics

Resources are finite. Pricing, tokens, latency, compute and context
therefore change optimal execution.

**Cost engineering compiles provider economics into execution policy.**

Mechanisms include caching, compression, summarization, truncation,
routing, model cascades, batching, speculative execution, token budgets
and context shaping.

### Compatibility --- heterogeneous semantics

Models, providers, tools, schemas, protocols and environments differ.

Compatibility absorbs accidental differences while preserving useful
provider-specific capabilities.

Mechanisms include adapters, canonical message formats, schema
normalization, capability negotiation, tool calling, structured output,
MCP, A2A and fallback.

### Continuity --- temporal semantics

Models are mostly stateless; tasks are stateful.

Continuity has two inseparable parts:

**State:** context, task state, tool state, filesystem/environment
state, memory, checkpoints.

**Control:** stop conditions, retries, loop detection, budgets,
timeouts, branching, fork/rewind, rollback, suspension, resumption and
recovery.

> **Loop Engineering is Continuity Engineering.**

Memory is a Continuity primitive. Context Engineering commonly spans
Cost + Continuity. Workflow graphs and durable runtimes are structured
implementations of Continuity.

### Cognition --- experiential semantics

Cognition means **system cognition**, not model intelligence.

It asks how future execution should improve because of past execution.

``` text
Observe → Reconstruct → Evaluate → Diagnose → Learn → Adapt
```

Tracing and observability provide evidence. Evals judge outcomes.
Diagnosis attributes causes. Learning turns runs into reusable findings.
Adaptation changes future policies.

> **Observability records experience. Cognition compounds it.**

## 3. Why 4C is not MECE

4C classifies **constraints**, not code modules. A feature can serve
multiple constraints.

Compression may serve Cost and Continuity. Routing may serve Cost,
Compatibility and Cognition. A trace supports Cognition but is not
sufficient for Cognition.

The test is: **which fundamental execution constraint is this mechanism
solving?**

## 4. The four underlying realities

-   **Money → Cost:** resources are finite.
-   **Difference → Compatibility:** systems are heterogeneous.
-   **Time → Continuity:** tasks outlive one inference.
-   **Experience → Cognition:** past runs should improve future runs.

Implementations can change while these realities persist.

## 5. Coordinate system, not strict ladder

A common path is:

``` text
Compatibility → Adapter
+ Cost         → Optimizer
+ Continuity   → Harness
+ Cognition    → Platform
```

But real systems can be strong in one C and weak in another. 4C is
therefore primarily a **capability coordinate system**, not a single
maturity score.

## 6. Cognition as the learning plane

The first three Cs shape execution. Cognition learns from execution and
can update them.

``` text
Execution → Evidence → Diagnosis → Learning → Policy
   ↑                                           ↓
   └──────── Cost / Compatibility / Continuity ┘
```

At maturity, Cognition becomes the harness's **learning plane**.

## 7. Scope

4C explains model-driven execution. It does not attempt to replace model
research, low-level inference engineering, accelerator/datacenter
infrastructure, product strategy, UX, business logic, market strategy or
organizational design.

Security, identity, permissions, governance and safety are often
cross-cutting concerns and should not be forced into a C merely to
preserve the acronym.

## 8. Thesis

> **Models create intelligence. Infrastructure creates computation.
> Harnesses create execution. Applications create user value.**

As models commoditize, complexity does not disappear. It moves into the
harness.
