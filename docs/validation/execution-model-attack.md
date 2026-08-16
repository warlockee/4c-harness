# Execution Model Attack

Date: **2026-08-15**<br>
Status: **linear pipeline falsified; transition loop survives**

## Target

The first v0.2 synthesis used:

``` text
Observe → Model Proposal → Admission → Commit → Outcome
```

This is attractive but may encode one tool-call implementation as theory. The
attack asks whether real Harness behavior has to move through those stages once,
in that order, with a model as the only proposer.

## Counterexamples

### Admission can precede proposal

An input guardrail can reject or transform incoming input before any model call.
The OpenAI Agents SDK documents input guardrails at the workflow entrance,
output guardrails on final output, and tool guardrails around each tool call
([guardrails](https://openai.github.io/openai-agents-python/guardrails/)).
Admission is therefore a boundary operation, not one post-model stage.

### Admission can follow commit-like execution

A tool output may be checked before it is returned to the model, and a final
answer may be checked before exposure to the user. An external operation may
also succeed technically while its result fails the task predicate. “Admit then
commit” does not capture output/result mediation without stretching `commit`.

### The model is not the only proposer

Deterministic orchestration code can select a route, trigger a retry, stop a
run, request human input or execute a fixed transition. A human can approve,
reject or edit a pending action. The Agents SDK runner itself handles tool calls,
handoffs, final outputs and maximum-turn errors around model output
([runner](https://openai.github.io/openai-agents-python/running_agents/)); its
HITL flow serializes state and resumes after an approval decision
([HITL](https://openai.github.io/openai-agents-python/human_in_the_loop/)).

Calling every such transition a “model proposal” assigns Harness behavior to
the model and fails the layer boundary.

### Observation is recurrent

Tool results, human input, errors and side effects create new evidence after
execution starts. They can cause another model call or deterministic transition.
Observation is not only the pipeline entrance.

### Commit is not always a world effect

A run may commit an internal state update, expose a final answer, suspend, hand
off or terminate with an error. “Effect” must include state and exposure, not
only consequential tool actions.

## Failed additions

The counterexamples do not establish new fundamental pressures:

| Candidate missing stage | Decomposition |
|---|---|
| Goal interpretation | Application intent plus Observation and proposal generation |
| Planning | Model/Application generation plus Harness transition lifecycle |
| Exception handling | Failure evidence plus Validity and Continuity policy |
| Human intervention | New evidence, Validity judgment, Authority decision or Application intent |
| Outcome verification | Observation of result plus Validity |
| Actuation | Application of an admitted transition |

They do show that a one-pass stage diagram is the wrong abstraction.

## Revised transition loop

``` text
APPLICATION: intent · success predicates · authority policy
                              │
                              ▼
┌────────────────────────── HARNESS ──────────────────────────┐
│                                                             │
│  state + available evidence                                 │
│             │                                               │
│             ▼                                               │
│  select candidate transition  ← model · code · human        │
│             │                                               │
│             ▼                                               │
│  mediate boundary             ← Validity · Authority        │
│             │                                               │
│       allow / reject / revise / escalate / suspend          │
│             │                                               │
│             ▼                                               │
│  apply or expose transition   → tool · state · output       │
│             │                                               │
│             └── outcome / event / error ──► observe/update ─┘
│                                                             │
│  4C varies policy across the loop:                          │
│  scarcity · heterogeneity · temporal extension · experience│
└─────────────────────────────────────────────────────────────┘
```

This is a logical loop, not a required module layout. Boundary mediation may
occur when accepting input, before a tool, after a tool, before exposing output,
or when resuming state. A mechanism may fuse several operations.

## Role of epistemic access

Epistemic Access determines which task-relevant evidence becomes available to
selection and mediation. It is not a single box: observation can happen at the
start, after a tool, after an error, on resume or through human input. The
constraint survives even if retrieval and state update are implemented inside
one function.

## Verdict

The original linear execution diagram is falsified as a general model. The
revised transition loop survives the tested counterexamples and yields clearer
predictions:

1. every externally visible effect or state transition has a selection source;
2. Validity and Authority can mediate multiple boundaries, not only tool calls;
3. every applied transition can produce new evidence and another transition;
4. deterministic and human decisions remain Harness-visible without being
   misattributed to model intelligence;
5. 4C explains why loop policy varies, not what makes a transition valid or
   permitted.

This remains provisional. A counterexample must now show a Harness-owned
execution operation that cannot be represented as evidence/state update,
transition selection, mediation or application without losing causal meaning.
