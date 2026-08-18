# Glossary

This repository uses precise terms because the validation record needs them.
That precision costs readers, so every term is restated here in one plain
sentence, with the shortest example that distinguishes it.

If you only read one page after the README, read this one.

## The layers

| Term | Plain sentence | Distinguishing example |
|---|---|---|
| **Model** | The thing that produces tokens. | A weight update is Model work, even when an optimizer you wrote launched it. |
| **Infrastructure** | Machinery that decides *how a model call is computed*. | GPU batching and kernel choice, even though both save money. |
| **Harness** | Machinery that decides *how a task is executed using model calls*. | Deciding to stop after three tool failures. |
| **Application** | Machinery that decides *what counts as user value*. | Deciding that "the invoice is filed" is what success means. |
| **Execution** | One task run: model calls, tools, state, retries and outcomes together. | Not one forward pass. |

The test is never the product name. Ask what object the mechanism controls:
computation, task execution, or user value.

## The 3 + 1 lens

| Term | Plain sentence | It is *not* |
|---|---|---|
| **Cost** | Something is finite (tokens, time, money, context, attempts) and that changes what the task may do. | Not "make it cheaper." Kernel optimization saves money and is still Infrastructure. |
| **Compatibility** | Two systems mean different things by the same request, and something must translate or negotiate. | Not any protocol plumbing; only differences that change task meaning or capability. |
| **Continuity** | The task outlives one model call, so state and lifecycle need explicit semantics. | Not a database. Storage is a substrate; Continuity is what the state *means* and which transitions preserve the task. |
| **Cognition** | Evidence from past runs changes the policy future runs use. | Not traces, not dashboards, not a score on the current run, not model training. |
| **Activated** | The pressure actually changes a decision in your system. | "We might need it someday" does not activate anything. |
| **Policy delta** | The specific decision that changes when one cause changes and everything else is held fixed. | The unit of every argument in this repository. |

## The boundary obligations

These are the three things 4C was originally claimed to cover and demonstrably
does not. They are the reason the exhaustive claim is rejected.

| Term | Plain sentence | The one-line case for it |
|---|---|---|
| **Epistemic Access** | Did the model actually get to see the facts the task depends on? | With free unlimited context and one call, a model still cannot use a private fact nobody showed it. |
| **Validity** | Is this input, action, output or observed result actually correct for the task? | A call can be cheap, compatible, stateful and permitted, and still be wrong. |
| **Authority** | May this principal cause or expose this effect, at this scope, to this audience? | `delete_account(id)` is a perfectly valid call that you may not be allowed to make. |

## Terms used in the validation record

| Term | Plain sentence |
|---|---|
| **Mediated transition system** | A model of execution as: look at state and evidence → propose a next step → check it → do it → observe what happened. The "mediated" part is the checking. |
| **Counterfactual removal** | Delete a candidate cause from the scenario and see whether a decision still has to be made. If it does, that cause did not explain the decision. |
| **Residual** | A decision left over after removal: the thing that breaks a theory. |
| **Kill criterion** | A stated observation that would force this model to change or be abandoned. |
| **Reopening condition** | The narrower version, attached to one claim. |
| **Peer constraint / peer category** | A candidate proposed as a fifth C rather than as a mechanism. Most candidates fail here. |
| **Postcondition** | What is true in the world after an action, as opposed to the action having been dispatched successfully. |
| **Evidence level** | For experiments: whether the observed behaviour came from the upstream system or from code written here. See [`experiments/README.md`](../experiments/README.md). |

## What to read, and what to skip

- **Using 4C on a real system:** the [README](../README.md) is sufficient. Steps
  1–4 are the whole method.
- **Checking the definitions:** [theory sections 1–4](theory.md). That is the
  entire core; sections 5–11 are scope and adversarial apparatus.
- **Attacking it:** [review guide](../REVIEW_GUIDE.md), then the
  [validation ledger](validation/README.md).
- **Everything else** is an audit trail. It exists so the claims can be checked,
  not because reading it is required.
