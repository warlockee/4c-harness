# Counterarguments and Falsification

A theory that explains everything explains nothing. This document
records the strongest attacks on 4C.

## 1. The four Cs are not at the same abstraction level

**Attack:** Cost looks like an outcome, Compatibility a property,
Continuity a runtime capability, and Cognition a meta-capability.

**Response:** 4C should not be presented as four software modules. They
are four constraints imposed on execution by four realities: finite
resources, heterogeneity, time, and experience.

This objection remains useful: if a definition drifts from the
constraint level into implementation detail, the theory weakens.

## 2. Why isn't Control a fifth C?

Control is essential, but under 4C it is inseparable from Continuity.
State without control can preserve an infinite loop perfectly.

Continuity therefore means **persistent + controlled execution across
time**, not memory alone.

## 3. Why isn't Safety/Security/Governance a fifth C?

These are major production concerns, but often cross-cut model,
infrastructure, harness and application layers.

4C intentionally describes the fundamental constraints of **model-driven
execution**, not the complete requirements of an AI company or product.

This is an open pressure point: if a harness-specific safety constraint
cannot be reduced to the existing Cs without distortion, it may falsify
completeness.

## 4. Cognition is anthropomorphic

Cognition here means **system cognition**, not consciousness or model
intelligence.

Operational definition:

``` text
Observe → Reconstruct → Evaluate → Diagnose → Learn → Adapt
```

A system with only traces has Cognition infrastructure, not mature
Cognition.

## 5. Features overlap multiple Cs

Correct. That is expected.

4C classifies **why** a mechanism exists, not where code belongs.
Overlap is evidence that a mechanism responds to multiple constraints,
not necessarily a taxonomy failure.

## 6. Cost is just optimization

If Cost meant "spend less," the criticism would be strong.

The stronger definition is **economic semantics**: provider pricing and
resource constraints alter execution policy. Caching, context shaping,
routing and compression can become necessary parts of correct economic
execution.

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

If planning produces a distinct harness-level constraint irreducible to
the four realities, it is a candidate counterexample.

## 9. Reliability is missing

Reliability is usually an outcome produced by mechanisms across
Compatibility, Continuity and Cognition rather than a distinct
underlying constraint.

The theory should be challenged if important reliability mechanisms
cannot be explained through those constraints.

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
