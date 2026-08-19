# Harness Scout Calibration Ledger

This is an append-only prediction ledger. It records selection decisions before
outcomes are known and retains misses, Holds and censored trials. A correction
adds a new row that names the superseded record; it does not rewrite history.

Resolution rules and metrics are defined in [Scout
Calibration](../scout-calibration.md).

The machine-readable record is
[`cohorts/2026-08-19-source-sweep.json`](cohorts/2026-08-19-source-sweep.json).
Run `python tools/scout_cohort_check.py` from the repository root. Discovery
records must opt out of hit-rate accounting; locked records fail validation when
any preregistration field is missing.

## Cohorts

| Cohort | Information cutoff | Eligible set | Locked terrain and trial | Selection | Status | Included in hit rate? |
|---|---|---|---|---|---|---|
| [`2026-08-19-source-sweep`](2026-08-19-source-sweep.md) | 2026-08-19; exact upstream commits in report | 7 like-for-like + 4 ecosystem candidates | No owner-supplied task portfolio, threshold, budget or deadline; archetypal terrains only | P1: 5, P2: 4, Hold: 2 | **Discovery cohort; unresolved** | **No.** It predates the trial-ready gate and its P1 order means information value, not calibrated success probability. |

## Why the inaugural sweep is not a claimed win

The sweep successfully generated source-backed hypotheses, including the
DeepSeek execution/change-path signal that mechanism coverage hid. That tests
the method's ability to produce candidates. It does not test whether those
candidates win.

Counting the sweep as a successful Bole cohort would leak the conclusion into
the definition: there is no locked real task portfolio, no primary uplift
threshold, no budget/deadline and no resolved external postcondition. It remains
valuable discovery evidence and becomes an input to future locked cohorts.

## Next cohort — not open until all fields are locked

``` text
Cohort id:
Information cutoff:
Decision owner:
Real terrain and external postconditions:
Eligible set and exclusion rule:
Baseline Harness/configuration:
Popularity baseline ranking:
Feature-coverage baseline ranking:
Random seed and shadow sample:
Exploit / explore / shadow allocation:

For every selected candidate:
  exact commit/configuration:
  evidence tripod:
  primary causal prediction:
  primary metric and minimum uplift:
  falsifier:
  repetitions and task tranche:
  budget, deadline and early-stop rule:
  pre-run probability/reference class:

Outcome adjudicator:
Status: Draft / Locked / Running / Resolved
```

Do not change `Draft` to `Locked` while any field above is missing.
