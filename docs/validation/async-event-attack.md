# Asynchronous / Event-Driven Attack

Date: **2026-08-15**<br>
Status: **serial loop falsified; mediated transition system survives**

## Threat

A loop diagram suggests one current state, one selected transition and one
outcome at a time. Event-driven Harnesses can instead have:

- external events that arrive without a model proposal;
- multiple in-flight actions and out-of-order outcomes;
- cancellation that cannot stop an active side effect;
- late results after the task has changed or ended;
- replay that must not repeat already completed effects.

If these require a global ordering or a new coordination primitive, the current
execution model and Continuity definition fail.

## Primary evidence

Inngest defines steps as checkpointed, independently retriable units whose
successful results are memoized so later execution can resume without repeating
completed work
([steps](https://www.inngest.com/docs/learn/inngest-steps),
[execution model](https://www.inngest.com/docs/learn/how-functions-are-executed)).
Functions can begin from events, schedules or webhooks
([functions](https://www.inngest.com/docs/learn/inngest-functions)).

Its cancellation semantics expose the hard case: cancellation occurs between
steps, while an actively executing step continues to completion
([cancellation](https://www.inngest.com/docs/features/inngest-functions/cancellation)).
In race mode, losing steps are not necessarily cancelled and may continue after
the winner lets function code proceed
([parallel steps](https://www.inngest.com/docs/guides/step-parallelism)).

These are runtime guarantees. They become Harness semantics only when the steps
and events carry a model-driven task's state, actions or outcomes.

### Independent replication: Temporal

Temporal independently exposes the same structure. Workflow Executions have
exclusive local state while running concurrently, communicate through Signals
and the environment through Activities, generate multiple Commands, and recover
by replaying Event History
([execution](https://docs.temporal.io/workflow-execution)). Its message model
separates read-only Queries, asynchronous state-changing Signals and tracked
Updates that can be validated before acceptance
([message passing](https://docs.temporal.io/encyclopedia/workflow-message-passing)).

This reproduces external-event transition sources, concurrent executions,
correlated histories and mediation before a state-changing update. It also
reinforces the runtime boundary: Temporal supplies durable state-transition
machinery; the model-driven task defines evidence, Validity, Authority and the
semantic meaning of those transitions.

## Attack 1: Who selects a transition?

The earlier model listed model, code and human sources. External environment and
system events are a fourth source. A webhook, timeout, cancellation event or tool
completion can make a transition eligible without new inference.

This is not a new fundamental constraint. It corrects the selection model:
selection can be reactive to an event, and event correlation determines which
execution state it may affect.

## Attack 2: Seriality

With concurrent actions there is no single total sequence:

``` text
state/evidence ─► select A ─► mediate ─► apply A ─────────► outcome A
       │
       └────────► select B ─► mediate ─► apply B ─► outcome B
                                                    (A still in flight)
```

The Harness must preserve causal relations, not pretend every event has one
global order. Results need execution identity, attempt identity and relevance to
the current state.

**Result:** “mediated transition loop” is too narrow if read literally. The
surviving abstraction is a **mediated transition system** that permits zero, one
or many in-flight transitions. A loop is its common sequential projection.

## Attack 3: Cancellation and revocation

Suppose Authority is revoked after an action begins. Cancellation prevents
future transitions but may not retract the in-flight effect. The decomposition
is:

- whether a new action may dispatch → Authority;
- correlate revocation with the affected run/action → Continuity;
- stop future lifecycle transitions → Continuity carrying Authority policy;
- observe whether an in-flight effect completed → Epistemic Access;
- check the resulting state → postcondition Validity;
- undo or compensate → Continuity, subject again to Authority.

Revocation is not rollback. This strengthens the boundary between permission and
temporal effect management; it does not merge them.

## Attack 4: Race and Coordination

Concurrent transitions can conflict over shared state. The earlier Coordination
rejection survives:

- protocol/representation mismatch → Compatibility;
- resource contention → Cost;
- causal ordering, ownership version and conflict handling → Continuity;
- whether a merged/resulting state is acceptable → Validity;
- who may win, write or compensate → Authority.

Multiplicity still does not supply one new causal primitive. The task may demand
serialization, optimistic validation, idempotency or compensation, but those are
temporal consistency policies.

## Runtime/Harness boundary

| Mechanism | Runtime substrate | Harness-owned meaning |
|---|---|---|
| Checkpoint/memoization | Store step result and replay metadata | Decide which task transition may be reused safely |
| Event delivery | Queue, trigger and retry delivery | Correlate evidence/event with the correct task state |
| Cancellation | Stop scheduling future steps | Decide semantic stop, compensation and final outcome |
| Concurrency limit | Cap active work | Choose task-level parallelism under Cost/Validity constraints |
| Race | Surface first completion | Decide whether late outcomes remain relevant or harmful |

An event engine is not a Harness merely because an agent can run on it.

## Revised execution abstraction

``` text
APPLICATION: intent · predicates · authority policy
                              │
                              ▼
┌────────────── MEDIATED HARNESS TRANSITION SYSTEM ──────────────┐
│ state + evidence + events                                      │
│        │                                                       │
│        ├─► select candidate(s) ← model · code · human · event  │
│        │           │                                           │
│        │           ▼                                           │
│        │      mediate boundaries ← Validity · Authority        │
│        │           │                                           │
│        │           ▼                                           │
│        │      apply/expose zero or more transitions            │
│        │           │                                           │
│        └◄── correlated outcomes/errors/cancellation ───────────┘
│                                                                │
│ operational plane: Cost · Compatibility · Continuity           │
│ feedback plane:    Cognition                                   │
└────────────────────────────────────────────────────────────────┘
```

## Verdict

The serial-loop reading is falsified. The mediated transition **system**
survives external events, concurrency, races, cancellation and late completion
across both Inngest and Temporal. No new 4C dimension or boundary obligation is
admitted.

The result creates explicit falsifiers: the model fails if a Harness-owned
operation cannot be represented as state/evidence/event update, candidate
selection, boundary mediation, application/exposure or correlated outcome—or if
concurrent semantics leave an independent residual after Continuity, Validity
and Authority are held fixed.
