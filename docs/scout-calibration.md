# Calibrating the Harness Scout

A single public call needs only the three-step [Bole
Challenge](bole-challenge.md). This document is the audit appendix used when 4C
starts claiming a success rate; it should not make the public workflow heavier.

A scout that publishes only its best-looking discoveries cannot know whether it
is good. High hit rate requires locked predictions, resolved failures, a stable
definition of success and comparison with simpler selection rules.

This document turns Harness Scout from a source-review method into an
accountable forecasting process. It optimizes for two different goals without
confusing them:

- **precision:** spend most trial budget on candidates likely to win a real
  terrain;
- **discovery:** reserve bounded budget for candidates with unusually large but
  uncertain upside, so the process can still find a horse consensus misses.

## 1. Define a hit before seeing the result

The primary Bole hit is not `Qualified`. A trace can confirm that code runs as
predicted while the product still loses the task.

| Outcome | Resolution rule | What it measures |
|---|---|---|
| **Task hit** | Candidate reaches `Task-proven` within the locked trial budget and deadline | Selection precision on current work |
| **Breakout hit** | Candidate reaches `Frontier-proven` on a locked rejected-backlog or adjacent task class | Ability to find a hidden “thousand-mile horse” |
| **Adoption hit** | Candidate reaches `Adoptable` after tails, failures and migration cost | Practical recommendation quality |
| **Miss** | A locked falsifier fires, the candidate fails the success threshold, or the budget/deadline expires after the required trial was runnable | Wrong prediction for this terrain |
| **Censored** | Trial cannot run because access, credentials or external state disappeared for reasons unrelated to the prediction | Unknown; excluded from hit rate and reported separately |

An abandoned trial is not automatically censored. If onboarding friction,
missing observability or configuration failure was inside the claim, it is a
miss.

## 2. A nomination must pass seven hard gates

Source signals earn attention. They do not earn a trial-ready slot until every
gate below passes.

| Gate | Required record | Failure disposition |
|---|---|---|
| **Real terrain** | Named current tasks, rejected backlog, adjacent probes and hard limits supplied by the evaluator or task owner | Discovery-only; do not estimate hit probability |
| **Activated pressure** | A concrete policy delta that disappears when the named 4C pressure is removed | Return to `Mapped` for this terrain |
| **Reachable edge** | Mechanism is on the shipped default or a documented configuration the trial will actually use | Watch; optional/demo code is not a product edge |
| **Causal chain** | Source mechanism → path delta → observable metric → external postcondition → user policy | Watch until every arrow is testable |
| **Evidence tripod** | Implementation, an executable test or invariant, and evidence that the path is shipped/reachable | P1 requires all three; a missing leg caps the candidate at exploratory priority |
| **Fair boundary** | Equal Epistemic Access, Validity and Authority obligations for candidate and baseline | Reject the comparison design |
| **Decisive trial** | Paired configuration, uplift threshold, falsifier, repetitions, budget, deadline and stop rule fixed before execution | Not trial-ready |

Fatal anti-signals override positive counts: hidden auxiliary calls, a broken
default, unbounded effects, unavailable postconditions, non-attributable
provider changes, or a result that depends on removing a required boundary.

## 3. Lock a causal prediction, not a score

Every trial-ready candidate must state one primary claim in this form:

``` text
For <locked terrain>, at <candidate commit/configuration>,
because <source mechanism> changes <real execution path>,
the candidate will improve <primary task metric> by at least <threshold>
while preserving <postcondition and boundaries>,
within <trial budget and deadline>.
It is falsified when <observable condition>.
```

Secondary metrics can diagnose a miss but cannot rescue the primary claim after
results are visible. For example, a latency nominee that loses verified task
yield cannot be silently relabeled an extensibility winner. That is a new claim
and a new cohort.

Do not assign numerical success probabilities before the repository has an
empirical reference class. Until then use `Uncalibrated`, preserve the ordering
logic, and publish the uncertainty. After enough resolved predictions exist,
estimate probabilities separately by terrain and archetype; do not pool a model
gateway with an end-user coding Harness.

## 4. Rank trial-ready candidates with a portfolio

A single queue either becomes conservative and misses breakouts or becomes
exciting and loses precision. Use three lanes:

| Lane | Default budget | Selection rule | Reported metric |
|---|---:|---|---|
| **Exploit** | 70% | Highest calibrated probability of `Task-proven`, then lower trial cost and downside | Task-hit precision |
| **Explore** | 20% | Large frontier upside with a complete causal chain but wider uncertainty | Breakout-hit precision |
| **Shadow** | 10% | Random sample from eligible Holds, evaluated cheaply and without promotion bias | False-negative estimate |

The split is a default, not a universal constant. Lock it before selecting the
cohort. Do not count established baselines as discoveries; they can be exploit
choices and comparison controls, but breakout credit requires that the
candidate was selected by a source prediction not already known from the
outcome evidence.

Within a lane, prefer pairwise dominance over an invented universal score. A
candidate dominates another for the same terrain only when it has at least as
complete a causal chain, no weaker boundary match, no greater trial cost and a
strictly better predicted probability or upside on one of those dimensions.
When candidates trade off, retain the tradeoff instead of hiding it in weights.

## 5. Measure the scout, not only the products

Resolve every locked cohort and publish:

``` text
Task precision@K       = Task hits among top-K trial-ready nominations / K
Breakout precision@K   = Breakout hits among top-K explore nominations / K
Adoption precision@K   = Adoption hits among recommendations / recommendations
Qualification leakage = Qualified candidates that failed Task-proven / Qualified
Censoring rate         = Censored trials / locked trials
False-negative sample  = Shadow Holds that reached Task-proven / resolved shadows
```

Also compare the same trial budget with three baselines:

1. select by repository visibility/popularity;
2. select by mechanism/feature coverage;
3. random selection from the eligible cohort.

The scout earns its name only when its out-of-sample hit rate or value lift
beats those baselines. Report Wilson intervals for hit rates. Once numerical
probabilities are issued, report calibration by probability bucket and Brier
score; a confident wrong prediction must hurt more than a cautious one.

## 6. Prevent hindsight and selection leakage

- Freeze the repository commit, information cutoff, terrain, baselines,
  thresholds, budget, lane and falsifiers before any measured run.
- Use a future task set, future release interval or hidden input tranche for
  resolution. Evidence used to choose the horse cannot also be the race result.
- Keep every candidate and Hold in an append-only ledger. Corrections append a
  superseding record; they never overwrite the original prediction.
- Resolve negative and expired cohorts. Publishing only promoted candidates
  makes precision unknowable.
- Separate source reviewer, adversarial falsifier and outcome adjudicator when
  practical. The adjudicator sees the locked postcondition, not the desired
  narrative.
- Record contamination: post-cutoff testimonials, benchmark results or product
  changes that became known before resolution.

## 7. Sequential trials improve both hit rate and cost

Spend evidence in stages and stop as soon as the primary claim cannot recover:

1. **Static gate:** verify default reachability, evidence tripod, attribution
   controls and boundary equivalence.
2. **Microtrace:** run the smallest case capable of exposing the claimed wait,
   call, token, state or extension-path delta.
3. **Paired task tranche:** run representative inputs to the locked
   postcondition; apply the predeclared early-stop rule.
4. **Tail/failure tranche:** only surviving candidates pay for p95/p99,
   recovery, restart and long-session evidence.
5. **Frontier tranche:** only candidates with a locked rejected backlog or
   adjacent probe can earn breakout credit.

This is not moving the goalposts. Every stage and stop condition is locked
before the first measured run.

## 8. Minimum cohort record

``` text
Cohort id and information cutoff:
Decision owner and real terrain:
Eligible candidate set:
Baseline Harness/configuration:
Selection baselines: popularity / feature coverage / random seed
Lane allocation: exploit / explore / shadow

Candidate commit and configuration:
Evidence tripod:
Activated 4C and boundary obligations:
Primary causal prediction:
Primary metric, uplift threshold and external postcondition:
Falsifier:
Repetitions, task tranche and attribution controls:
Trial budget, deadline and sequential stop rule:
Pre-run probability: Uncalibrated or calibrated value + reference class

Resolution: task hit / breakout hit / adoption hit / miss / censored
Evidence links and adjudicator:
Contamination and deviations:
```

The [calibration ledger](scouts/calibration-ledger.md) is the public record for
these cohorts. Machine-readable records live in `docs/scouts/cohorts/`; run
`python tools/scout_cohort_check.py` to reject incomplete counted cohorts.
