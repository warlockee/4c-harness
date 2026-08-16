# Browser / Embodied Environment Attack

Date: **2026-08-15**<br>
Status: **loop survives; outcome validity and uncertainty boundary strengthened**

## Threat

In browser, desktop and embodied environments, observations can be partial or
stale, the world can change between observation and action, an accepted command
can have an unexpected effect, and success may only be knowable later. This
could reveal a missing primitive such as Grounding, Controllability or
Uncertainty.

## Primary evidence

BrowserGym standardizes web-agent observation and action spaces
([paper](https://arxiv.org/abs/2412.05467)). WebArena supplies functional sites,
long-horizon tasks and functional completion evaluation
([paper](https://arxiv.org/abs/2307.13854)). OSWorld uses real operating systems,
initial-state setup and execution-based evaluators
([paper](https://arxiv.org/abs/2404.07972)). Voyager consumes environment
feedback and errors, self-verifies success and stores successful programs in a
reusable skill library without changing model weights
([paper](https://arxiv.org/abs/2305.16291)).

These sources establish recurring observation/action/outcome loops. Benchmark
scores are not used as theory evidence.

## Attack 1: Grounding

Grounding decomposes into:

- acquiring the current screen, DOM or world state → Epistemic Access;
- translating model actions into an environment action space → Compatibility;
- determining that a target is the intended entity → Validity;
- deciding whether the action may affect it → Authority.

**Verdict: rejected as a peer primitive.** It is a compound relation across
evidence, representation, task truth and permission.

## Attack 2: Environment coupling

Hold model, interface, resources, authority and history constant. The Harness
sends the correct click, but a concurrent page update moves the target or the
operation succeeds only partially. The candidate was valid, but the resulting
world state does not satisfy its postcondition.

``` text
precondition evidence
       ↓
candidate → pre-application mediation → apply
                                      ↓
                              observed outcome
                                      ↓
                           postcondition validity
```

The Harness cannot assume `accepted action = intended outcome`. It may need to
observe, verify, retry, compensate, escalate or replan.

No new loop operation is required: feedback updates evidence; postcondition
checking is Validity; freshness is Epistemic Access; recovery is Continuity;
permission remains Authority. Controllability is an achieved closed-loop
quality, not one irreducible decision.

**Verdict: rejected as a separate boundary, but the old proposal-only Validity
definition is falsified.** Validity applies before action and after outcome.

## Attack 3: Uncertainty

Uncertainty is the strongest causal candidate exposed here:

> A model can be wrong, observations can be incomplete, and an environment can
> respond differently from the intended transition.

It changes policy—inspect, simulate, verify, hedge, retry or escalate—and
survives all four Cs. But it currently fails admission as one new Harness
primitive because its consequences separate cleanly:

| Uncertainty about | Required Harness question |
|---|---|
| Current world state | Epistemic Access |
| Candidate task correctness | Pre-application Validity |
| Permission or acceptable risk | Authority |
| Whether the intended effect occurred | Observation + postcondition Validity |
| How to continue after mismatch | Continuity |

Uncertainty is therefore a deeper reality behind multiple boundary obligations,
not evidence that one should absorb the others. Calling it a fifth C would not
predict where mediation occurs.

**Status: high-threat rejected provisionally.** Reopen if a recurring
uncertainty-driven Harness decision cannot be expressed as evidence acquisition,
Validity, Authority or temporal transition policy.

## Attack 4: Voyager and 3 + 1

Voyager supplies an end-to-end stress case:

- environment state/errors → Epistemic Access;
- program generation/curriculum → model/Application selection;
- self-verification → Validity;
- iterative execution and extended skills → Continuity;
- code/environment interface → Compatibility;
- successful programs reused on new tasks → Cognition;
- query/attempt limits → Cost when enforced;
- a real deployment would require Authority, though a benchmark can
  pre-authorize its action set.

The skill library counts as Cognition because successful experience changes
future action policy. A static library of hand-authored functions would be
Compatibility/Application packaging.

## Findings

1. Validity includes postcondition and final-outcome checking, not only proposal
   acceptance.
2. Observation includes freshness and provenance, not merely data presence.
3. Application is an attempted transition, not a guarantee of effect.
4. Environment events can drive the next transition without a new model
   proposal; the revised loop already permits this.
5. Uncertainty is a fundamental background reality but currently decomposes
   across Epistemic Access, Validity, Authority and Continuity.

## Verdict

The mediated transition loop survives browser, desktop and embodied examples.
No new fifth adaptation dimension or execution operation is admitted, but the
one-sided definition of Validity is falsified. The canonical model must represent
both precondition and postcondition mediation.
