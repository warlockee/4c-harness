# The 4C Bole Challenge

**Find the winning AI Harness before the leaderboard makes it obvious.**

The rule is deliberately small:

``` text
CALL IT → RACE IT → PUBLISH IT
```

1. **Call it.** Before the measured run, publish one candidate, one real task,
   one source-level reason it should win, and one observation that would prove
   the call wrong.
2. **Race it.** Run the current and candidate Harness against the same external
   finish line, budget and authority boundary.
3. **Publish it.** Close the call as `Hit`, `Miss` or `Censored`. Misses stay
   visible. A randomly sampled Hold runs in the shadow lane so missed winners
   cannot disappear.

[**Open a public Bole bet →**](https://github.com/warlockee/4c-harness/issues/new?template=bole-challenge.yml)

When the race ends, add this comment without editing the opening bet, then close
the issue:

``` text
RESULT: HIT / MISS / CENSORED
PRIMARY METRIC: <baseline> → <candidate>; locked minimum: <threshold>
EXTERNAL FINISH LINE: PASS / FAIL
EVIDENCE: <trace, artifact or reproducible command>
DEVIATIONS: <none, or what changed>
```

## The only scoreboard that matters

| Score | Meaning |
|---|---|
| **Hit rate** | Resolved pre-run calls whose candidate cleared the locked finish line |
| **Missed-winner rate** | Shadow Holds that would have cleared it |

4C earns the name “Bole” only when its locked calls beat popularity, feature
coverage and random choice at the same trial budget. Stars, testimonials and a
post-hoc explanation do not count.

## Live record

**Counted calls: 0. Proven hits: 0.** The challenge is open; the repository does
not claim a Bole success rate yet.

The [2026-08-19 source sweep](scouts/2026-08-19-source-sweep.md) produced a
trial queue, but it was performed after the products and public reactions were
visible. It is discovery evidence, not a prediction.

DeepSeek Harness is the reference case: its source exposes a thin streaming
path, off-path persistence and an unusually short extension loop—the mechanisms
that could explain why users report it as fast, cheap and fun. 4C found a sharp
testable explanation, but found it too late to claim the call. The next winner
must be named before the experience is known.

## What counts as a hit

A candidate is a hit only when it beats the current Harness by the locked
minimum uplift, completes the external task, stays inside the budget and effect
scope, and resolves before the deadline. Everything else is a miss or a named
censoring event.

That is the complete public game. The detailed evidence and anti-leakage rules
live in [Scout Calibration](scout-calibration.md); they are an audit appendix,
not extra work required to understand the challenge.
