# Harness Scout: Finding the Candidate Others Miss

The purpose of 4C selection is not to reward the most features or ratify the
most famous benchmark winner. It is to find a Harness whose task-relevant
advantage is still easier to see in its code than in the market consensus, then
promote that candidate only as evidence accumulates.

A “best Harness” without a task terrain is meaningless. A **breakout Harness**
is one that, for a named current or latent task portfolio:

1. addresses an activated pressure or expands the feasible task frontier;
2. has a source-visible causal reason to outperform the current path;
3. produces more externally verified value per limiting resource;
4. preserves the required evidence, Validity and Authority boundaries;
5. keeps its advantage across tails, failures, restarts and representative
   inputs;
6. remains net-positive after migration and re-verification cost.

This is a promotion standard, not a universal numerical ranking.

## 1. Scouting has two error budgets

**Nomination should favor recall.** A source-predicted advantage with a precise
falsifier is enough to earn a cheap trial. Requiring published product-level
proof at this stage guarantees that the scout discovers only established
leaders.

**Promotion should favor precision.** Architecture, testimonials and one fast
demo cannot justify adoption. Promotion requires a pinned trace, external
postconditions, comparable boundaries and a representative distribution.

Keeping these budgets separate lets 4C notice an underappreciated design
without laundering potential into proof.

There is a second separation inside nomination: **source prospecting** can use a
plausible terrain, but **trial-ready selection** requires a real task portfolio,
a complete causal chain and a locked success rule. P1/P2 without that contract
orders information value only; it is not a calibrated probability of winning.
The seven hard gates, exploit/explore/shadow allocation and hit-rate accounting
are defined in [Scout Calibration](scout-calibration.md).

## 2. Name the terrain before the horse

One scouting terrain contains:

``` text
current delegated tasks
+ rejected backlog: real work avoided because of latency, cost or friction
+ bounded adjacent probes: new affordances worth a reversible experiment
+ limits: time, money, tokens, effects, evidence and human attention
```

Run the 4C activation test per task class. The same Harness can be a breakout
candidate for fast interactive extension work and a poor choice for a durable,
high-authority production workflow. The verdict must carry that scope.

## 3. Source signals that deserve nomination

These are leading indicators, never automatic points:

| Source signal | Candidate advantage it predicts | Required falsifier |
|---|---|---|
| Few serial awaits, provider hops and model calls on the default path | Lower Harness-added latency and amplification | Trace shows the supposedly avoided work still blocks useful output |
| Native preservation of reasoning, tools, images, cache usage and provider errors | Stronger Model–Harness fit than a lowest-common-denominator adapter | Same-model comparison shows no retained capability or yield advantage |
| Stable prompt/tool prefix with package-owned token and invalidation accounting | Lower token tax and better cache economics | Pinned runs show unstable prefixes, low hits or no billed-token benefit |
| Persistence, telemetry and secondary projections off the response hot path | Continuity/observation without interactive delay | Event-loop or storage work dominates first-useful-output latency |
| Explicit safe concurrency with deterministic model-visible ordering | Better wall-clock yield for independent work | Representative tasks expose no parallel work or trigger rate-limit/recovery loss |
| Live interface inspection, documented seams and reversible effects | Shorter missing-capability → validated-extension path | Extension still requires privileged-core edits, restart or manual repair |
| Agent-operable define/run/diagnose/rollback workflow | Frontier expansion through on-demand self-extension | Human intervention, failure or Authority cost erases the time advantage |
| Trace events sufficient to reconstruct TTFT, completion, cost and failures | Faster falsification and improvement slope | Important waits or outcomes remain unattributable |
| Working defaults and actionable first-run failures | Short onboarding path | Clean-install trial stalls before a verified task |
| External postcondition and scoped-effect enforcement | Credible yield rather than speed obtained by skipping checks | Advantage disappears when compared under equal Validity and Authority |

The corresponding anti-signals are hidden auxiliary model calls, synchronous
logging on every chunk, demo-only configurations, provider semantics flattened
without evidence, plugins that still patch a central loop, self-reported
completion, averages without tails and speed achieved by removing a required
boundary.

## 4. The promotion ladder

| Stage | Required evidence | Allowed conclusion |
|---|---|---|
| **Mapped** | Mechanism inventory and 4C classification | “This system contains these controls.” |
| **Nominated** | Task terrain + source edge + user-visible prediction + falsifier | “This candidate deserves a bounded trial.” |
| **Qualified** | Pinned runtime trace confirms the predicted path behavior | “The source advantage is realized in this configuration.” |
| **Task-proven** | Representative distribution reaches external postconditions under equal limits and boundaries | “It wins this current task class.” |
| **Frontier-proven** | A rejected or adjacent task class becomes worth doing and succeeds repeatedly | “It expands what this user can economically delegate.” |
| **Adoptable** | Tail/failure behavior and migration-adjusted value remain acceptable | “Adopt for this scoped terrain.” |
| **Switch-worthy** | The advantage spans the target portfolio and exceeds full migration/re-verification cost | “Replace the current default for this terrain.” |

Stages cannot be skipped. A candidate can remain `Nominated` for lack of access,
credentials or repetitions without being rejected. A failed falsifier moves it
to `Rejected` for the named claim, not necessarily for every terrain.

## 5. The scout card

Every public recommendation should fit this record:

``` text
Candidate and exact commit:
Information cutoff and cohort id:
Terrain:
Current tasks:
Rejected backlog:
Adjacent probes:

Activated 4C:
Boundary requirements:

Source nomination signals:
Evidence tripod: implementation / executable invariant / shipped reachability
Predicted user-visible edges:
Falsifiers:
Five realization paths:
  onboarding / execution / Model-fit / human-control / change

Primary locked causal prediction:
Primary metric, minimum uplift and external postcondition:
Baseline and attribution controls:
Trial repetitions, budget, deadline and early-stop rule:
Lane: exploit / explore / shadow
Pre-run probability and reference class: Uncalibrated until evidence exists

Runtime configuration and attribution controls:
Yield distribution:
External postconditions:
Frontier movement:
Failure, tail and upgrade evidence:
Migration and re-verification cost:

Promotion stage:
Resolution: task hit / breakout hit / adoption hit / miss / censored
Verdict scope:
Unknowns:
```

The card makes uncertainty useful. It tells a reader whether the candidate is
an architectural prospect, a measured task winner or a migration-ready default
instead of compressing all three into “Strong.”

A card with no owner-supplied task portfolio, uplift threshold, budget or
deadline can still publish a source nomination, but it must say `Discovery-only`
and cannot enter the Bole hit-rate denominator. Every locked outcome, including
misses and expired trials, goes into the [calibration
ledger](scouts/calibration-ledger.md).

## 6. DeepSeek Harness nomination

At upstream commit
[`141eb6f`](https://github.com/deepseek-ai/deepseek-harness/tree/141eb6fef83422698aef7a981029e843e8161534),
DeepSeek Harness qualifies for **Nominated**, not yet `Task-proven`, in a terrain
where interactive latency, quota and time-to-extension change human work
policy.

The nomination is based on its direct native stream, non-blocking persistence
and telemetry contracts, bounded parallel tool scheduler, per-package model
experience/cache accounting, and agent-operable reversible Cordis extension
loop. The detailed source evidence and falsifiers are in [Execution
Yield](execution-yield.md#7-deepseek-harness-what-source-inspection-should-have-surfaced).

The next promotion test is not “does it have more plugins?” It is a controlled
trial over current tasks plus a rejected backlog, measuring cold/warm latency,
verified completion, cost, correction loop and extension time. Until that run
exists, 4C should actively surface DeepSeek as a high-potential candidate and
refuse to call it a proven winner. The reusable record is published as the
[DeepSeek Harness Scout Card](scouts/deepseek-harness.md).
