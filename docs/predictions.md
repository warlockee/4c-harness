# Predictions from the 4C Theory

A useful theory should make claims that can later be wrong.

## P1. Model commoditization will increase harness importance

As model capability becomes cheaper and more interchangeable,
differentiation will move toward execution policy rather than disappear.

**Falsifier:** production systems increasingly use raw model APIs
directly while harness complexity materially declines.

## P2. Compatibility mechanics will partially commoditize

Protocols and common interfaces will reduce accidental integration
complexity.

However, capability and provider-semantic differences will remain.

**Falsifier:** providers become sufficiently homogeneous that
provider-specific execution logic becomes economically insignificant.

## P3. Continuity will become a defining production capability

Agent systems will increasingly require externalized state,
checkpoint/resume, durable execution, controlled loops and long-lived
task semantics.

**Falsifier:** valuable autonomous workloads remain overwhelmingly
single-call or short-lived.

## P4. Observability will evolve toward Cognition

The value chain will move from traces and dashboards toward replay,
evaluation, diagnosis, policy learning and adaptation.

``` text
Trace → Replay → Eval → Diagnosis → Learning → Adaptation
```

**Falsifier:** production teams gain most value from passive
observability and automated policy learning remains marginal.

## P5. Provider-specific empirical knowledge will become a harness moat

As pricing and execution semantics grow more complex, trial-derived
knowledge about provider behavior will become strategically valuable.

**Falsifier:** official interfaces become sufficiently transparent and
standardized that empirical provider policy produces negligible
advantage.

## P6. The Cognition plane will increasingly optimize the three operational Cs

Execution history will automatically inform routing, caching,
compatibility handling, context policy, retries and loop control.

**Falsifier:** these policies remain predominantly hand-authored despite
abundant execution data.

## P7. Harness interfaces will become richer than universal chat interfaces

A lowest-common-denominator `chat()` abstraction will be insufficient
for systems optimizing provider-specific economics, capabilities and
continuity.

**Falsifier:** universal chat abstractions remain sufficient for
state-of-the-art multi-provider execution without material loss.

## P8. Context Engineering will split into pressure and evidence policy

**Original prediction falsified (2026-08-15):** “Context Engineering will be
absorbed by Cost and Continuity.” The [context
attack](validation/context-attack.md) found an Epistemic Access residual after
removing Cost, Compatibility, Continuity and Cognition.

The revised prediction is that mature systems will distinguish capacity and
history policy (Cost/Continuity) from evidence acquisition, attribution,
freshness and relevance policy (Epistemic Access), even when one context
assembly component implements both.

**Falsifier:** production context systems need no separate decision about what
task-relevant evidence the model can observe once resource and persistence
policy are fixed.

## P9. Loop Engineering will compose with, not collapse into, durable runtimes

**Original equivalence prediction falsified (2026-08-15):** durable runtimes
provide checkpoint, replay, event and cancellation substrates, but Harnesses
still own task-state meaning, mediation and transition semantics. A serial loop
is only one topology of a concurrent mediated transition system.

The revised prediction is that production Harnesses will integrate with durable
runtimes while retaining an explicit task-level transition and boundary-policy
layer above runtime persistence.

**Falsifier:** durable-runtime configuration alone determines task-state
meaning, candidate acceptance, authority and safe effect semantics, leaving no
recurring Harness policy above it.

## P10. The frontier will move from Harness Engineering to Harness Learning

The major transition after stateful execution will be systems that
improve their own execution policies from accumulated runs.

> **The previous generation made agents stateful. The next generation
> will make harnesses self-improving.**

**Falsifier:** execution evidence remains largely disconnected from reusable
prompt, retrieval, routing, tool or lifecycle policy changes, or those changes
move entirely into model-weight training.

## P11. Better tool-use models will not eliminate Harness mediation

Models will increasingly learn tool selection and argument generation, but
effectful systems will continue to mediate evidence, Validity and Authority
outside model weights.

**Falsifier:** production systems safely and correctly let trained models apply
consequential tool calls directly, with no external validation, permission or
outcome-observation semantics.

## P12. Effectful Harnesses will separate action acceptance from outcome validity

Browser, coding and embodied systems will increasingly verify postconditions
instead of treating a successfully dispatched action as task success.

**Falsifier:** pre-action validation plus transport success proves sufficient
across changing environments, with post-effect observation adding negligible
value.

## P13. Mature systems will expose mixed layer surfaces

Products will increasingly combine inference, runtime, Harness and evaluation
mechanisms, making component-level mapping more predictive than vendor-level
categories.

**Falsifier:** important systems converge on clean single-layer boundaries and
product-level labels predict mechanism ownership without recurring exceptions.

## P14. Authority will remain independent from compatibility

Protocols will improve capability discovery and tool interoperability, but will
not determine which principal may cause a particular effect.

**Falsifier:** standardized capability negotiation also supplies sufficient
delegation, consent and revocation semantics across consequential agent systems,
eliminating separate Harness permission mediation.
