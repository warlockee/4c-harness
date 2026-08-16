# Counterarguments and Falsification

A theory that explains everything explains nothing. This document
records the strongest attacks on 4C.

The current theory is explicitly compositional. The 4C `3 + 1` lens answers why
execution policy varies; a mediated transition system answers what execution
does; Epistemic Access, Validity and Authority answer what may cross execution
boundaries. Treating the lens alone as the complete architecture would revive
the already-falsified original claim.

## 1. The four Cs are not at the same abstraction level

**Attack:** Cost looks like an outcome, Compatibility a property,
Continuity a runtime capability, and Cognition a meta-capability.

**Response:** 4C should not be presented as four software modules. They
are a `3 + 1` causal structure: finite resources, heterogeneity and time impose
conditionally activated operational pressures; experience supplies the feedback
plane that can revise later policy.

This objection remains useful: if a definition drifts from the
constraint level into implementation detail, the theory weakens.

## 2. Why isn't Control a fifth C?

“Control” is a functional role, not one cause. Resource control maps to Cost;
capability control to Compatibility; lifecycle control to Continuity; evidence,
Validity and Authority control retain their own questions.

Continuity therefore means **state plus lifecycle control across time**, not
memory alone and not every rule that affects execution.

## 3. Why isn't Safety/Security/Governance a fifth C?

These are major production concerns, but often cross-cut model,
infrastructure, harness and application layers.

4C intentionally describes the fundamental constraints of **model-driven
execution**, not the complete requirements of an AI company or product.

This answer is currently under successful attack. "Cross-cutting" is an
architectural description, not a proof that the concern is reducible to 4C.
Coding, tool and browser harnesses enforce permissions, sandbox boundaries and
approval decisions that change the permitted action set.

The first [authority attack](validation/authority-attack.md) found that bounded
authority remains necessary in a one-shot, single-provider, single-tool,
unlimited-resource, no-history execution. It therefore survives the removal of
Cost, Compatibility, Continuity and Cognition.

Current status: **the original exhaustive 4C claim is falsified**. Authority is
retained as a separate mediation obligation in the revised non-exhaustive model,
and has been independently replicated in Codex, Claude Code, MCP and agent-SDK
approval mechanisms. Calling the residual "safety" does not reduce it.

## 4. Cognition is anthropomorphic

Cognition here means **system cognition**, not consciousness or model
intelligence.

Operational definition:

``` text
Observe → Reconstruct → Evaluate → Diagnose → Learn → Adapt
```

A system with only traces has Cognition infrastructure, not mature
Cognition.

The [Cognition attack](validation/cognition-attack.md) adds the causal test:
past-run evidence must produce a reusable change in future Harness policy.
Current-run evaluation and model training alone do not qualify.

## 5. Features overlap multiple Cs

Correct. That is expected.

4C classifies **why** a mechanism exists, not where code belongs.
Overlap is evidence that a mechanism responds to multiple constraints,
not necessarily a taxonomy failure.

## 6. Cost is just optimization

If Cost meant either "spend less" or "optimize all compute," the criticism
would succeed.

The stronger definition is **resource semantics**: finite tokens, latency,
context, concurrency, attempts, compute or money alter task execution policy.
Caching, context shaping, routing and stopping can therefore be Harness Cost.
Kernel optimization, GPU placement and continuous batching remain
Infrastructure even when they save money.

The [Core Four symmetry audit](validation/core-four-symmetry-audit.md) retained
Cost only under this layer-specific causal definition.

## 7. Compatibility will be standardized away

Standards may commoditize accidental protocol differences. But
heterogeneity can persist through capabilities, economics, modalities,
context limits, tool behavior, versions and provider-specific semantics.

A falsification test is whether future systems become sufficiently
homogeneous that Compatibility ceases to require meaningful harness
logic.

## 8. Planning is missing

Planning crosses layers.

"What goal should be pursued?" can belong to application or agent
policy.

"How does the plan persist, branch, retry, pause and resume?" belongs to
Continuity.

The [Planning and Control attack](validation/planning-control-attack.md) did not
find an irreducible residual. Plan generation is usually model intelligence or
Application policy. The Harness exposes observations and tools, persists plan
state, schedules steps, validates progress and mediates actions. Those execution
semantics decompose across the tested categories.

Current status: **rejected as a peer constraint**, while remaining an important
mechanism and artifact.

## 9. Reliability is missing

Reliability as a service-level aggregate is an outcome produced by mechanisms
across several constraints. That does not settle the narrower current-run
problem: a model proposal can be syntactically valid, authorized and still
wrong.

The [correctness attack](validation/correctness-attack.md) shows that validation,
verification and accept/reject/retry policy remain necessary after removing the
four proposed causes. Calling retries Continuity describes how another attempt
occurs, not why the first result was rejected. Calling validation Compatibility
confuses schema conformance with semantic task validity. Calling it Cognition
confuses current-run checking with improvement from past experience.

Current status: **the exhaustive claim is falsified; Validity is a separate
mediation obligation**. The Application commonly owns the predicate while the
Harness evaluates or transports it before actions, after observed effects and
before output exposure. Predicate ownership does not erase enforcement semantics.

## 10. Context is missing

The original answer was that Context Engineering spans Cost and Continuity:
context is finite, and task state must survive across bounded inference windows.
That answer covers capacity management and temporal preservation, but not the
one-shot epistemic problem.

The [context attack](validation/context-attack.md) shows that a model cannot use
a private or current fact it has not observed, even with free unlimited context,
one model, one call and no history. Compatibility can expose a data source and
Validity can reject an unsupported answer, but neither selects and presents the
evidence required for inference.

Current status: **the exhaustive claim is falsified; Epistemic Access is a
separate evidence obligation**. Applications and tools may own data, but the
Harness still determines what task-relevant evidence becomes available to
model-driven selection and mediation.

## 11. Uncertainty or controllability is missing

Browser and embodied agents show that observations can be stale and accepted
actions can fail to create their intended postconditions.

The [browser/embodied attack](validation/browser-embodied-attack.md) treats
uncertainty as a deep background reality, but not one Harness primitive. Current
world uncertainty maps to Epistemic Access; candidate and postcondition judgment
to Validity; risk/permission to Authority; recovery to Continuity.

Current status: **provisionally rejected as a peer category**. Reopen if a
recurring uncertainty-driven decision survives removal of all four questions.

# Falsifying 4C

4C should be revised if we discover a recurring, harness-specific
engineering problem that:

1.  is fundamental rather than an implementation fashion;
2.  cannot reasonably be derived from finite resources, heterogeneity,
    time, or experience;
3.  changes execution semantics;
4.  persists across providers and architectures;
5.  cannot be assigned to an existing C without semantic contortion.

A credible fifth constraint would be more valuable than preserving the
acronym.
