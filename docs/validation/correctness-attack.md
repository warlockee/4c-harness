# Correctness Attack

Date checked: **2026-08-15**<br>
Status: **provisional theory failure; ownership dispute remains**

## Attack claim

4C may omit another fundamental Harness constraint:

> Model and tool outputs are fallible proposals. A harness may need to determine
> whether an intermediate or final result is valid before accepting, acting on
> or returning it.

Call this residual **current-run validity**. "Correctness" is shorthand but may
be too narrow: validity can include factual accuracy, tests, business
invariants, task completion and evidence sufficiency.

## Scope guard

The application usually defines what success means. The model supplies much of
the candidate reasoning. The Harness-owned residual is narrower: executing the
accept, reject, retry, repair, route or escalate transition around a candidate
result.

Offline benchmarking alone is not in scope here. The test concerns a decision
inside a live task execution.

## Primary-source observations

### Pydantic AI — output validation and retry

Pydantic AI validates model-produced structured data against declared types and
supports output functions or validators that can raise `ModelRetry`, feeding a
validation failure back to the model for another attempt
([output documentation](https://pydantic.dev/docs/ai/core-concepts/output/)).

**Relevant semantics:** a generated answer is not the run result merely because
the model emitted it. Validation controls acceptance and can cause another model
transition.

### OpenAI Codex — executable verification

Codex exposes terminal logs and test results so users can verify work, reports
test failures and uncertainty, and encourages running repository-specified
tests. OpenAI also states that generated code still requires review and
validation before integration
([Codex introduction](https://openai.com/index/introducing-codex/)).

**Relevant semantics:** code generation and task acceptance are separate. Tests
can reject an otherwise well-formed patch and keep the execution loop open.

### AutoGen — reviewer loop

AutoGen documents a reflection pattern in which a coder produces a candidate,
a reviewer returns approval or critique, and the interaction repeats until
approval or a stopping condition
([reflection pattern](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/design-patterns/reflection.html)).

**Relevant semantics:** the reviewer result determines whether execution commits
the candidate or generates another attempt.

### OpenAI Agents SDK — guardrail tripwires

The Agents SDK provides input, output and tool guardrails. A tripwire can stop
agent execution when a check fails, while tool guardrails can reject or replace
individual tool-call results
([guardrail documentation](https://openai.github.io/openai-agents-python/guardrails/)).

**Relevant semantics:** current-run validation controls which model or tool
result becomes externally visible or continues through the workflow.

## Minimal counterfactual

Use a read-only task: `return the sum of the invoice line items`. There is one
model, one provider, one schema-compatible calculator tool, unlimited resources,
one short run, no prior execution data, and blanket authority to read and
calculate. The candidate total is arithmetically wrong.

| Remove candidate cause | What remains | Reduction result |
|---|---|---|
| Cost | Checking and retrying are free. A wrong total still should not be accepted. | Not Cost |
| Compatibility | All schemas and tool semantics are perfectly normalized. Semantic error remains. | Not Compatibility |
| Continuity | A one-shot checker can accept or reject without durable state. Time does not supply the validity predicate. | Not Continuity |
| Cognition | The checker uses a static invariant and no historical evidence. | Not Cognition |
| Authority | The operation is harmless, read-only and fully authorized. It can still be wrong. | Not bounded authority |

The residual changes execution semantics: accept returns the result; reject,
retry or escalate does not.

## Why nearby mappings fail

### Compatibility

Compatibility answers whether a value conforms to a transport, schema, tool or
provider contract. A perfectly valid JSON invoice total can be numerically
wrong. Broadening Compatibility to every semantic contract would absorb task
specification, guardrails and much of application logic.

### Continuity

Continuity implements the retry, loop and stop mechanics. It does not supply the
predicate that declares the previous attempt invalid. The cause of a transition
and the machinery that carries it through time are different.

### Cognition

Cognition uses evidence from past execution to improve future policy. A static
assertion or test inside the current run needs no experience or learning.
Current-run verification may later produce Cognition evidence, but that is a
cross-C relationship rather than a reduction.

### Authority

Authority asks whether an action is permitted. Correct execution can be
unauthorized, and authorized execution can be wrong. Both mediate proposals but
use independent predicates.

## Admission-test result

| Requirement | Current evidence | Result |
|---|---|---|
| Independent durable fact | Model-driven outputs can be wrong despite technical validity and authorization. | Pass |
| Cross-architecture recurrence | Typed validators, tests, reviewer agents and guardrail tripwires implement the family. | Pass |
| Changes execution semantics | Validation selects accept, reject, retry, repair or escalation. | Pass |
| Not merely one mechanism | Tests, schemas, critics and deterministic invariants are distinct implementations. | Provisional pass |
| Folding into a C loses information | Existing Cs explain retry transport, schema form or later learning, not present-run semantic rejection. | Pass |

## Strongest objection: correctness belongs to Application

Task-specific truth and utility usually originate in application requirements.
A generic Harness cannot know whether a medical recommendation, invoice total or
code patch is correct without supplied criteria.

But external origin does not by itself remove a constraint from the Harness:
provider prices originate outside the Harness, tool schemas originate outside
the Harness, and evaluation criteria used by Cognition often originate in the
Application. The Harness compiles each into execution policy.

A stable split may be:

- **Application:** defines the success predicate and acceptable trade-offs.
- **Harness:** applies available evidence to that predicate and controls the
  execution transition.

This mirrors Cost: a business supplies the budget; the Harness changes execution
because of it.

## Can correctness and authority be one missing constraint?

They share a structural pattern:

``` text
model proposal → admission predicate → commit | reject | repair | escalate
```

But their predicates are orthogonal:

- **Validity:** would this action/result satisfy the task or specification?
- **Authority:** may this principal cause or expose it?

Merging them into generic "Control" would predict mediation but lose why a
correct proposal can be denied and an authorized proposal can be rejected as
wrong. It may still be useful to model both as an **execution-admission plane**
with separate axes.

## Current conclusion

Correctness is not cleanly reducible to 4C or bounded authority. This creates a
second provisional theory failure and weakens the idea that adding one fifth C
will repair completeness.

The likely structural problem is that 4C mixes causes of execution adaptation
while leaving acceptance predicates implicit. A robust revision may need two
levels:

1. **Execution pressures:** why strategy changes across resources, systems,
   time and experience.
2. **Execution admission:** whether a proposal is valid and authorized before
   it is committed.

This two-level model is only a hypothesis. It must next be tested against
reliability mechanisms such as transport failure, nondeterminism, idempotency
and partial side effects to see whether "validity" explains them or merely
renames the desired outcome.
