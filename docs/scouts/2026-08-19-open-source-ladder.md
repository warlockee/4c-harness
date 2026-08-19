# 4C open-source Harness ladder — 2026-08-19

This report is the audit trail behind the opening ladder. It compares every
active general-purpose open-source coding Harness in the dated market universe
with at least 10,000 GitHub stars. Each repository is pinned to an exact commit.

## Locked comparison contract

- Terrain: latency- and quota-sensitive interactive coding with on-demand local extension.
- Weights: Dollar Efficiency (Cost) 45%, Compatibility 35%, Continuity 20%, Cognition 0%.
- Formula: `sum(weight × grade / 5)`; grades use the published 0–5 rubric.
- Ceiling: source evidence can reach grade 4, never grade 5. Grade 3+ requires
  implementation, executable invariant, shipped-path reachability, and a falsifier.
- Claim boundary: these are source-fit predictions, not measured speed, price,
  task-success, or universal product-quality claims. Runtime trials can overturn them.

## Result

| Rank | Harness | D / K / N | 4C Fit | Pinned commit |
|---:|---|---:|---:|---|
| 1 | DeepSeek Harness | 4 / 4 / 4 | 80 | `141eb6f` |
| 1 | OpenCode | 4 / 4 / 4 | 80 | `e2505d4` |
| 1 | Goose | 4 / 4 / 4 | 80 | `af016f0` |
| 1 | Pi | 4 / 4 / 4 | 80 | `b7bb00b` |
| 1 | Zed Agent | 4 / 4 / 4 | 80 | `6e0a083` |
| 6 | Aider | 4 / 3 / 4 | 73 | `5dc9490` |
| 7 | Gemini CLI | 3 / 4 / 4 | 71 | `eaa3042` |
| 7 | Qwen Code | 3 / 4 / 4 | 71 | `39fc769` |
| 7 | Kilo Code | 3 / 4 / 4 | 71 | `9a6e081` |
| 10 | Continue | 3 / 4 / 3 | 67 | `5522c6f` |
| 10 | Crush | 3 / 4 / 3 | 67 | `7d78d74` |
| 12 | Codex | 3 / 3 / 4 | 64 | `3b45c29` |
| 13 | SWE-agent | 3 / 3 / 2 | 56 | `3ea751c` |
| 14 | Cline | 2 / 3 / 3 | 51 | `d9bb228` |
| 14 | OpenHands | 2 / 3 / 3 | 51 | `f2dd330` |

`D / K / N` means Dollar Efficiency / Compatibility / Continuity. Cognition is
inactive for this comparison, so it contributes no points and is not displayed
as a grade.

## What was read

The compact index below names the decisive mechanisms. The machine-readable
[evidence ledger](fit-score-evidence.json) contains, for every C and every
Harness, exact commit-pinned links to implementation, invariant, reachability,
the bounded claim, and the observation that would falsify it.

| Harness | Dollar Efficiency | Compatibility | Continuity |
|---|---|---|---|
| DeepSeek Harness | direct SSE adapter and cache accounting | native translation and Cordis extension seam | write-behind JSONL persistence |
| OpenCode | token-budgeted compaction | provider-specific semantic adapters | snapshot-backed reverse patches |
| Goose | provider-aware cache-prefix invariance | native MCP extension manager | SQLite sessions and non-destructive fork |
| Pi | tested automatic compaction | cross-provider handoff transforms | atomic JSONL repair and torn-tail recovery |
| Zed Agent | threshold compaction tests | live context-server registry | database flush/reopen roundtrip |
| Aider | token-budgeted repository map | model/edit-format configuration | guarded Git undo and verification |
| Gemini CLI | routing and context compression | live extension loading | checkpoint recovery |
| Qwen Code | bounded concurrent dispatch | live extension refresh | interrupted-history repair |
| Kilo Code | threshold compaction | provider plugins | ordered projection and staged revert |
| Continue | token-budget message pruning | four MCP transports | JSON session lifecycle |
| Crush | parallel tool calls and summarization | single-flight MCP renewal | database-backed sessions |
| Codex | parallel-safe tool dispatch | first-class MCP sessions | rollout reconstruction |
| SWE-agent | configurable history processors | LiteLLM model mediation | trajectory replay; no safe resume proof |
| Cline | context-management path | provider/tool mediation | task checkpoints and persistence |
| OpenHands | bounded event/context paths | runtime/tool mediation | session persistence and replay |

## Interpretation

An 80 means “excellent source fit for this terrain,” not “best Harness in every
situation.” The five-way tie is intentional: the evidence does not justify
inventing precision between equal grade vectors. DeepSeek Harness scores highly
for explainable reasons—its direct provider path, extension seam, and
write-behind persistence all satisfy the same grade-4 rule applied to peers.

Closed-source and runtime-only products remain in the dated
[market universe](../validation/market-universe.md) but cannot be placed on a
source-code ladder without fabricating evidence.
