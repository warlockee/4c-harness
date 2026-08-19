# Scout Card: DeepSeek Harness

Promotion stage: **Nominated**  
Candidate snapshot:
[`141eb6f`](https://github.com/deepseek-ai/deepseek-harness/tree/141eb6fef83422698aef7a981029e843e8161534)
(2026-08-19)  
Evidence ceiling: **Source-predicted**; no comparative runtime distribution is
claimed by this repository.

Calibration status: **Discovery-only / not trial-ready.** This card was written
before an owner supplied a real task portfolio, primary uplift threshold,
budget and deadline. It does not enter the Bole hit-rate denominator. When those
fields are locked, append a cohort record to the [calibration
ledger](calibration-ledger.md) rather than backfilling them after a run.

## Terrain

DeepSeek deserves a bounded trial when one or more of these conditions changes
human or application policy:

- interactive coding waits cause the person to context-switch;
- quota or marginal price causes useful small tasks to be rejected;
- missing local integrations are frequent enough that time-to-extension
  matters;
- a single local session benefits from rapid correction more than from broad
  routing or distributed workflow machinery.

This card does not nominate it universally for consequential production
automation, long-running distributed workflows or tasks whose dominant limit is
model capability rather than Harness realization.

## 4C activation hypothesis

| Pressure | Conditional activation |
|---|---|
| **Cost** | Strong when latency, price, tokens or quota changes task selection, interaction cadence or parallelism. |
| **Compatibility** | Strong when the task adds providers, modalities, messaging channels, local UI or bespoke tools. |
| **Continuity** | Active for multi-step local work and persisted preferences; durable recovery claims require a separate failure trial. |
| **Cognition** | Not demonstrated merely by stored skills, presets, traces or agent-written plugins. |

Required boundaries: externally checked task postconditions; scoped filesystem,
process, network and credential Authority; explicit evidence provenance for any
added modality or service.

## Nomination signals

| Signal | Prediction | Falsifier |
|---|---|---|
| Direct native DeepSeek SSE stream and exactly one provider request per stream | Low Harness-added time and request amplification | Same-model trace exposes hidden calls or comparable Harness overhead |
| Native thinking, tool, reasoning-replay, cache-usage and provider-error mapping | Strong Model–Harness fit | Same-model comparison shows lost capability or no outcome benefit |
| Session write-behind and non-blocking telemetry contract | Continuity/observation stay off the response hot path | Storage, projection or event-loop work dominates useful-output latency |
| Bounded parallel-safe tool scheduler with model-order commit | Independent tool work reduces wall time without history nondeterminism | Target tasks have no overlap, or concurrency worsens limits/failures |
| Per-package Model Experience, token and KV-cache-effect contract | Prompt/cache tax can be localized before running the product | Default composition still produces unstable prefixes or unaccounted context |
| Live Cordis inspection plus define/run/stop and reversible plugin effects | Short, inspectable change path | A representative extension requires core patching, restart, manual cleanup or unsafe authority |

Primary source links and line-level limits are maintained in the [Execution
Yield case](../execution-yield.md#7-deepseek-harness-what-source-inspection-should-have-surfaced).

## Five realization paths

| Path | Current reading |
|---|---|
| **Onboarding** | Unknown. Run from a clean supported machine through credentials and first verified edit. |
| **Execution** | Source predicts a thin streaming path, off-path secondary writes and safe tool overlap. |
| **Model fit** | Source predicts strong preservation of DeepSeek-native semantics and cache accounting. |
| **Human control** | Immediate chunk events and agent inbox/control seams exist; comprehension, correction flow and UI delay remain unmeasured. |
| **Change** | Source predicts unusually short inspect → define → run → diagnose → stop/rollback extension cycles; restart/upgrade survival remains unmeasured. |

## Qualification trial

Use a current Harness baseline and this candidate on three portfolios:

1. representative interactive coding tasks already delegated;
2. real small tasks rejected today because of waiting or quota;
3. one missing integration requiring a reversible extension.

Where available, run both same-model/different-Harness and
same-Harness/different-model controls. Pin commit, model id, endpoint, region,
preset, tool set, permissions, cache state and input repository revision.

Before the first measured run, additionally lock one primary causal claim, its
minimum meaningful uplift, the external postcondition, repetitions, total trial
budget, resolution deadline and early-stop rule. Without those fields this
section is a proposed experiment, not a forecast.

Measure:

- clean-install time and failed actions to first verified task;
- cold/warm and cache-hit/miss p50/p95/p99 time to first useful output;
- time, model requests, tool calls, tokens and money per externally verified
  outcome;
- correction-loop time and the human context-switch threshold;
- success, retry and recovery tails over short and long sessions;
- time and touchpoints to implement, validate, restart, upgrade and roll back
  the extension;
- rejected task classes newly completed within the user's limits.

## Promotion rules

- Advance to **Qualified** only if traces confirm the predicted execution,
  Model-fit and change paths.
- Advance to **Task-proven** only if representative outcomes beat the baseline
  under equal Validity and Authority.
- Advance to **Frontier-proven** only if previously rejected work succeeds
  repeatedly and is worth its total human/economic cost.
- Advance to **Adoptable** only if tails, recovery, upgrade and migration remain
  acceptable.
- Advance to **Switch-worthy** only if the advantage covers the target portfolio
  and exceeds the seven-line-item migration bill.

Current verdict: **run the bounded qualification trial; do not dismiss it from
`Cost: Partial`, and do not promote it from testimonials alone.**
