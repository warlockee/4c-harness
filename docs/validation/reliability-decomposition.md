# Reliability Decomposition

Date checked: **2026-08-15**<br>
Status: **no new fundamental residual found**

## Question

Does "Reliability" name an independent Harness constraint, or does it combine
failure causes and recovery mechanisms already explained by Continuity,
Compatibility, Cost, Validity and Authority?

This test separates four commonly conflated problems:

1. transport or worker failure;
2. nondeterminism during generation or replay;
3. duplicate execution and idempotency;
4. partial side effects and compensation.

## Primary-source observations

### LangGraph

LangGraph retries nodes after selected exceptions, applies timeouts, invokes
error handlers after retry exhaustion, and checkpoints state for recovery
([fault tolerance](https://docs.langchain.com/oss/python/langgraph/fault-tolerance)).
Its functional runtime persists task results so resumed runs follow the same
recorded steps. It requires side-effecting tasks to be idempotent because a task
that starts but does not complete may run again
([functional API](https://docs.langchain.com/oss/javascript/langgraph/functional-api)).

Interrupt resumption re-enters node execution, so effects before an interrupt
must be idempotent, moved after the interrupt or isolated in separate nodes
([interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts)).

### Temporal

Temporal requires deterministic workflow command sequences so event history can
be replayed. Non-deterministic external operations—including model calls—belong
in Activities outside the replay path; Activities are automatically retried
([workflow definition](https://docs.temporal.io/workflow-definition)). Temporal
recommends idempotent Activities because retries can execute an operation more
than once without intending multiple effects
([activity definition](https://docs.temporal.io/activity-definition)).

These semantics predate agent harnesses. Their use in agent runtimes is evidence
that durable-agent reliability inherits distributed-workflow constraints rather
than creating a novel AI-specific category.

## 1. Transport and worker failure

**Case.** A model or tool request times out, returns a retryable server error, or
the worker dies after a checkpoint.

**Why execution changes.** The task outlives one failed attempt. The runtime must
bound attempts, wait, retry, resume, fail over or surface terminal failure.

**Mapping.** **Continuity.** This is exactly controlled execution across time and
inference/process boundaries.

Other Cs may modify policy without changing the primary cause:

- provider-specific error normalization is Compatibility;
- retry and fallback budgets are Cost;
- learned retry policy is Cognition;
- whether a recovered result is acceptable is Validity.

**Verdict:** clean Continuity fit; no residual.

## 2. Nondeterminism

"Nondeterminism" has two distinct meanings.

### Model stochasticity

Different fresh invocations may produce different valid or invalid candidates.
Stochasticity alone is a model property, not a Harness constraint. Its execution
effects decompose:

- sample/rerun within a budget → Cost + Continuity;
- accept or reject this candidate → Validity;
- learn which policy performs better across runs → Cognition.

### Replay nondeterminism

The same durable run may take a different control path when replayed if time,
randomness, model calls or network results are recomputed inline.

The object being preserved is the temporal identity and history of one
execution. Recording external results and replaying the same command sequence
are therefore **Continuity** mechanisms.

**Verdict:** model stochasticity decomposes; replay consistency is Continuity.
No independent residual.

## 3. Idempotency and duplicate execution

Idempotency prevents a repeated attempt from multiplying an intended effect.
It becomes necessary because failure can occur after an effect but before the
runtime records completion, leaving the runtime unable to distinguish "not run"
from "ran but acknowledgment was lost."

Counterfactual test: remove retry, resume and ambiguous completion across time.
If the action executes exactly once and its completion is known, the duplicate
problem disappears. Therefore idempotency is causally downstream of
**Continuity**, not independent from it.

Authority affects the blast radius—an unauthorized duplicate is still
unauthorized—but cannot ensure exactly-once behavior. Validity may reject a
duplicate final state but does not implement replay safety.

**Verdict:** Continuity mechanism, amplified by Consequence/Authority; no new
constraint.

## 4. Partial side effects

**Case.** A task reserves inventory, then payment or notification fails. The
world is left between intended start and terminal states.

Mechanisms include checkpoints, sagas, compensating actions, reconciliation and
manual escalation.

The causal structure is:

``` text
multi-step execution through time
        + non-atomic external effects
        ↓
record progress → resume | compensate | escalate
```

This is a **Continuity** problem at task granularity. The Harness coordinates
recovery across tools; the underlying services or workflow runtime may own
transactional enforcement.

Two admission predicates remain separate:

- Validity: does the recovered or compensated state satisfy the task invariant?
- Authority: may the Harness perform the compensating action?

**Verdict:** Continuity + Validity + Authority where applicable; no third
admission predicate established.

## Failure-cause matrix

| Observed failure | Primary cause | Primary mapping | Why |
|---|---|---|---|
| Timeout / transient 5xx | Attempt failed while task remains live | Continuity | Retry and recovery span attempts through time. |
| Provider error mismatch | Heterogeneous failure semantics | Compatibility | Errors require normalization or provider-specific handling. |
| Retry exceeds budget | Finite resources | Cost | Economics bound otherwise valid recovery. |
| Schema-invalid call | Technical contract violation | Compatibility | Proposal cannot be expressed under the target interface. |
| Schema-valid but wrong result | Task validity failure | Validity residual | Technical compatibility does not imply semantic success. |
| Correct but disallowed action | Permission failure | Authority residual | Validity does not grant authority. |
| Resume repeats a side effect | Replay across uncertain completion | Continuity | Idempotency preserves effect semantics across attempts. |
| History teaches a better retry policy | Experience changes future policy | Cognition | Improvement depends on prior executions. |

## Layer boundary

Durability, replay and idempotency are general distributed-systems concerns.
They enter 4C only when the optimized object is a model-driven **task execution**.
The database transaction engine, message broker or worker scheduler remains
Infrastructure/runtime. The Harness decides task-level retry, checkpoints,
compensation and escalation using those primitives.

This mirrors the vLLM boundary test: shared mechanism names do not erase the
optimized-object distinction.

## Verdict

Reliability fails the admission test as a peer constraint because it does not
have one independent causal reality or one distinctive mechanism family. It is
an outcome generated by handling different failure causes correctly.

The two-level hypothesis survives this attack:

- execution pressures explain adaptation across resources, systems, time and
  experience;
- execution admission applies Validity and Authority predicates before commit;
- Reliability describes the resulting property across both.

This is evidence for the two-level model, not proof. Coordination and context
remain capable of producing additional residuals.
