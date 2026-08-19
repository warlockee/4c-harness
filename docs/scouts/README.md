# Harness Scout Board

Want to turn one nomination into evidence? [Open a public Bole
bet](https://github.com/warlockee/4c-harness/issues/new?template=bole-challenge.yml),
lock the prediction before the run, and publish the hit or miss.

This board tracks evidence stage, not product rank. `Mapped` means the
repository has classified documented mechanisms. It does not mean the candidate
failed a source audit. `Nominated` means a task terrain, source edge, prediction
and falsifier exist. Later stages follow the [Harness Scout promotion
ladder](../harness-scout.md#4-the-promotion-ladder).

## Like-for-like candidates

| Candidate | Stage | Trial queue and terrain |
|---|---|---|
| [DeepSeek Harness](deepseek-harness.md) | **Nominated** | **P1:** interactive latency, quota and on-demand extension. |
| [Aider](2026-08-19-source-sweep.md#aider-p1-nominated) | **Nominated** | **P1:** low-amplification repository editing with Git-native correction. |
| [browser-use](2026-08-19-source-sweep.md#browser-use-p1-nominated) | **Nominated** | **P1:** stateful browser execution and recovery. |
| [Codex](2026-08-19-source-sweep.md#codex-p2-nominated) | **Nominated** | **P2:** high-authority, resumable and parallel coding work. |
| [Gemini CLI](2026-08-19-source-sweep.md#gemini-cli-p2-nominated) | **Nominated** | **P2:** long governed sessions with routing, hooks and extensions. |
| [OpenHands](2026-08-19-source-sweep.md#openhands-p2-nominated) | **Nominated** | **P2:** supervision of isolated local/remote autonomous runs. |
| [Cline](2026-08-19-source-sweep.md#cline-p2-nominated) | **Nominated** | **P2:** reversible sessions spanning IDE, CLI, SDK and hub clients. |

## Ecosystem candidates

These rows are substrates or adjacent control planes, not drop-in replacements
for an end-user coding Harness.

| Candidate | Stage | Trial queue and terrain |
|---|---|---|
| [LangGraph](2026-08-19-source-sweep.md#langgraph-p1-substrate-trial-nominated) | **Nominated** | **P1:** durable stateful workflows and failure recovery. |
| [LiteLLM](2026-08-19-source-sweep.md#litellm-p1-infrastructure-trial-nominated) | **Nominated** | **P1:** multi-provider quota, cost and availability policy. |
| [CrewAI](2026-08-19-source-sweep.md#crewai-hold-mapped) | Mapped | Hold until role separation predicts net yield after handoff amplification. |
| [Langflow](2026-08-19-source-sweep.md#langflow-hold-mapped) | Mapped | Hold until visual composition shortens a measured idea-to-deployment path. |

No candidate is currently `Qualified`, `Task-proven`, `Frontier-proven`,
`Adoptable` or `Switch-worthy` in this repository.

The exact commits, source signals, predictions and falsifiers are recorded in
the [2026-08-19 source sweep](2026-08-19-source-sweep.md).

All current nominations are **discovery-only**. Their P1/P2 labels order source
trial information value, not calibrated success probability, because no real
owner-supplied terrain, uplift threshold, budget and deadline were locked before
the audit. The sweep is therefore excluded from hit-rate claims in the
[calibration ledger](calibration-ledger.md). Future trial-ready cohorts must
start as a public [Bole Challenge](../bole-challenge.md); the seven detailed
[calibration gates](../scout-calibration.md#2-a-nomination-must-pass-seven-hard-gates)
apply before 4C aggregates success-rate claims.

## Board rules

- A missing nomination is unknown, not negative evidence.
- Every nomination names a terrain; there is no global winner column.
- Source predictions link exact commits and include falsifiers.
- Promotion requires the evidence for every prior stage.
- A failed claim is rejected only for its named terrain and prediction.
- Updates preserve the old card or record its superseding commit so evidence
  does not silently drift with `main`.
- Every locked trial, including misses, expired trials and randomly sampled
  Holds, remains in the calibration ledger.
