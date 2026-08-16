# Cognition Attack

Date: **2026-08-15**<br>
Status: **survives, but only under a narrower operational definition**

## Threat

Cognition is structurally unlike Cost, Compatibility and Continuity. The first
three can constrain a current execution. Cognition looks like a second-order
feedback loop, and its parts can apparently be reassigned: traces to
observability, scores to Validity, weight updates to model training and product
metrics to the Application. If nothing remains at the Harness layer, Cognition
is not a fourth pressure.

## Operational test

Cognition exists only when evidence from an earlier execution causally changes
the Harness policy used by a later execution.

``` text
past execution → evidence → evaluation/diagnosis → policy update
                                                   ↓
future intent + current observation → different execution policy
```

Hold the future intent, current observation, model, tools, resources and task
state constant. If changing only retained experience changes routing,
prompt/context policy, tool policy, stopping, retry or another Harness decision,
there is a Cognition effect.

This rejects several false positives:

| Mechanism | Why it is not sufficient |
|---|---|
| Store a trace | Observability records evidence but need not change policy. |
| Score the current output | Validity judges a proposal but need not affect a later run. |
| Retry inside the same task | Usually current-run Validity plus Continuity. |
| Fine-tune model weights | Model/training work unless the Harness changes its deployed policy. |
| Analyze business KPIs | Application analytics unless findings compile into execution policy. |

## Minimal surviving case

Consider one model, one tool, ample resources and independent one-shot trials.
After a failed trial, the system stores a textual diagnosis. On the next
otherwise identical trial, the Harness inserts that diagnosis or a derived rule
into context, changing the action without changing model weights.

Cost, Compatibility and Continuity do not explain the difference: no resource
boundary changed, no interface difference appeared, and the later trial does
not resume the earlier task. Only reusable experience changed the policy.

Reflexion demonstrates this mechanism directly: it converts task feedback into
linguistic reflection, stores it in episodic memory and uses it for decisions in
subsequent trials without weight updates
([paper](https://arxiv.org/abs/2303.11366)). This is a Harness-level learning
loop, not model training.

## Independence from Validity

Validity and Cognition are coupled but not identical.

- A static validator can accept, reject or retry forever without learning.
- Cognition can learn a cheaper route or retrieval policy from trace evidence
  without changing the semantic acceptance predicate.
- When scores drive learning, Validity supplies evidence; Cognition performs the
  cross-run policy update.

LangSmith documents the separation: online evaluation identifies production
failures, failures become offline cases, fixes are validated, and a changed
application is redeployed
([concepts](https://docs.langchain.com/langsmith/evaluation-concepts),
[workflow](https://docs.langchain.com/langsmith/evaluation)). Evaluation reaches
Cognition only when findings alter future execution.

## Layer ownership

| Changed object | Primary owner |
|---|---|
| Model weights or architecture | Model / training infrastructure |
| Business objective or user workflow | Application |
| Prompt assembly, retrieval, routing, tool policy, retry or stopping policy | Harness |
| Compute kernel, batching or device scheduler | Infrastructure |

Calling all optimization "Cognition" would erase the Harness boundary;
excluding non-weight policy learning would erase a real Harness mechanism.

## Structural asymmetry

Cognition survives, but not as the same kind of current-run pressure:

- Cost, Compatibility and Continuity are first-order conditions used during
  execution.
- Cognition is the feedback pressure by which outcomes revise later policy.

This is acceptable only because the narrowed 4C claim classifies **causes of
policy variation**, not lifecycle stages. Experience is an independent cause
even when its effect arrives through a feedback path.

## Verdict

The attack does not remove Cognition. It removes the loose equation
`observability + evals = cognition`.

> **Cognition is retained iff prior execution evidence is converted into a
> reusable change to future Harness policy.**

The underlying reality is **experience** and the mechanism is **cross-run
learning**. “Cognition” remains the label, but does not mean consciousness,
model intelligence or every form of optimization. This strengthens the partial
adaptation model; it does not restore the falsified completeness claim.
