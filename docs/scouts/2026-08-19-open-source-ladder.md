# 4C open-source Harness ladder — 2026-08-19

This report is the audit trail behind the opening ladder. It compares every
active general-purpose open-source coding Harness in the dated market universe
with at least 10,000 GitHub stars. Each repository is pinned to an exact commit.
Every candidate row also carries its official GitHub URL and a star-count
snapshot captured at **2026-08-20T00:14:37Z**. Stars are market context only:
they contribute **0 points** to the 4C score.

## Locked comparison contract

- Terrain: latency- and quota-sensitive interactive coding with on-demand local extension.
- Weights: Cost Efficiency 45%, Compatibility 35%, Continuity 20%, Cognition 0%.
- Frozen exam: 12 candidate-blind questions in
  [`interactive-coding-v2-exam.json`](interactive-coding-v2-exam.json).
- Formula: `sum(question weight × answer level)`, where answer level is exactly
  `0`, `0.5`, or `1`. Missing qualifying evidence scores zero.
- Contract: the exam is separate from candidate
  [answer sheets](interactive-coding-v2-results.json) and bound by SHA-256.
  Candidate names and candidate-specific weights are rejected by CI.
- Claim boundary: these are source-fit predictions, not measured speed, price,
  task-success, or universal product-quality claims. Runtime trials can overturn them.

## Result

| Rank | Harness | Official GitHub | Stars | CE / K / N | Source exam | Pinned commit |
|---:|---|---|---:|---:|---:|---|
| 1 | DeepSeek Harness | [github.com/deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 167,152 | 40 / 30.5 / 15.5 | **86** | `141eb6f` |
| 2 | Pi | [github.com/earendil-works/pi](https://github.com/earendil-works/pi) | 93,784 | 33.5 / 30.5 / 20 | **84** | `b7bb00b` |
| 3 | Qwen Code | [github.com/QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 27,200 | 33 / 31.5 / 18 | **82.5** | `39fc769` |
| 4 | Gemini CLI | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) | 106,586 | 23 / 35 / 20 | **78** | `eaa3042` |
| 5 | Codex | [github.com/openai/codex](https://github.com/openai/codex) | 106,859 | 28 / 30.5 / 18 | **76.5** | `3b45c29` |
| 6 | Zed Agent | [github.com/zed-industries/zed](https://github.com/zed-industries/zed) | 88,895 | 33.5 / 26.5 / 15.5 | **75.5** | `6e0a083` |
| 7 | Goose | [github.com/aaif-goose/goose](https://github.com/aaif-goose/goose) | 53,011 | 28.5 / 26.5 / 20 | **75** | `af016f0` |
| 8 | Kilo Code | [github.com/Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) | 26,937 | 28 / 26 / 17.5 | **71.5** | `9a6e081` |
| 9 | Continue | [github.com/continuedev/continue](https://github.com/continuedev/continue) | 35,546 | 28 / 30 / 11 | **69** | `5522c6f` |
| 9 | Crush | [github.com/charmbracelet/crush](https://github.com/charmbracelet/crush) | 27,504 | 28 / 30 / 11 | **69** | `7d78d74` |
| 11 | OpenCode | [github.com/anomalyco/opencode](https://github.com/anomalyco/opencode) | 199,235 | 23 / 27 / 15 | **65** | `e2505d4` |
| 12 | Aider | [github.com/Aider-AI/aider](https://github.com/Aider-AI/aider) | 48,333 | 28 / 18 / 17.5 | **63.5** | `5dc9490` |
| 13 | OpenHands | [github.com/OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 84,508 | 16.5 / 22 / 17.5 | **56** | `f2dd330` |
| 14 | Cline | [github.com/cline/cline](https://github.com/cline/cline) | 66,499 | 11 / 22 / 17.5 | **50.5** | `d9bb228` |
| 15 | SWE-agent | [github.com/SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) | 20,080 | 22 / 13 / 5.5 | **40.5** | `3ea751c` |

`CE / K / N` means Cost Efficiency / Compatibility / Continuity point
contributions. Cognition is inactive for this comparison.

Star counts come from the official GitHub repository API at the single timestamp
above. They make project attention visible without turning popularity into a
quality grade.

## The fixed exam

| Pressure | Frozen questions | Points |
|---|---|---:|
| Cost Efficiency | default hot path; context/cache economy; safe parallelism; budget/stop enforcement | 45 |
| Compatibility | model semantics; tool protocol; live extension; failure fidelity | 35 |
| Continuity | durable state; crash integrity; safe resume; rollback/fork | 20 |

Full credit requires the question's complete pinned shipped path and executable
invariant. Half credit means a reachable mechanism covers only part of the
question or leaves defaultness/completeness open. Zero means this audit found no
qualifying pinned evidence; it does not assert that the feature can never exist.

### Answer matrix

`1` = full, `½` = partial, `0` = no qualifying evidence. HP/CC/SP/BS are Cost
Efficiency; MS/TP/LE/FF are Compatibility; DS/CI/SR/RF are Continuity.

| Harness | HP | CC | SP | BS | MS | TP | LE | FF | DS | CI | SR | RF | Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| DeepSeek Harness | 1 | 1 | 1 | ½ | 1 | ½ | 1 | 1 | 1 | ½ | 1 | ½ | **86** |
| Pi | ½ | 1 | ½ | 1 | 1 | ½ | 1 | 1 | 1 | 1 | 1 | 1 | **84** |
| Qwen Code | ½ | ½ | 1 | 1 | 1 | 1 | 1 | ½ | 1 | 1 | 1 | ½ | **82.5** |
| Gemini CLI | ½ | 1 | 0 | ½ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **78** |
| Codex | ½ | ½ | 1 | ½ | 1 | 1 | ½ | 1 | 1 | 1 | 1 | ½ | **76.5** |
| Zed Agent | ½ | 1 | ½ | 1 | ½ | 1 | 1 | ½ | 1 | ½ | 1 | ½ | **75.5** |
| Goose | ½ | 1 | ½ | ½ | ½ | 1 | 1 | ½ | 1 | 1 | 1 | 1 | **75** |
| Kilo Code | ½ | 1 | 0 | 1 | 1 | ½ | ½ | 1 | 1 | ½ | 1 | 1 | **71.5** |
| Continue | ½ | 1 | 0 | 1 | ½ | 1 | 1 | 1 | 1 | ½ | ½ | 0 | **69** |
| Crush | ½ | ½ | 1 | ½ | ½ | 1 | 1 | 1 | 1 | ½ | ½ | 0 | **69** |
| OpenCode | ½ | 1 | 0 | ½ | 1 | 1 | ½ | ½ | 1 | ½ | ½ | 1 | **65** |
| Aider | ½ | 1 | 0 | 1 | 1 | ½ | 0 | ½ | 1 | 1 | ½ | 1 | **63.5** |
| OpenHands | 0 | ½ | ½ | ½ | ½ | 1 | ½ | ½ | 1 | ½ | 1 | 1 | **56** |
| Cline | 0 | ½ | 0 | ½ | ½ | 1 | ½ | ½ | 1 | ½ | 1 | 1 | **50.5** |
| SWE-agent | ½ | ½ | 0 | 1 | ½ | ½ | 0 | ½ | ½ | 0 | ½ | 0 | **40.5** |

Question definitions, weights and each answer sheet are machine-readable; the
matrix is a human-readable projection, not a second scoring source.

## What was read

The compact index below names the decisive mechanisms. The machine-readable
[evidence ledger](fit-score-evidence.json) contains, for every C and every
Harness, exact commit-pinned links to implementation, invariant, reachability,
the bounded claim, and the observation that would falsify it.

| Harness | Cost Efficiency | Compatibility | Continuity |
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

The previous whole-C method produced five identical 80s because one strong
causal path promoted an entire C to grade 4. That was useful for nomination but
too coarse for a leaderboard.

The v2 result does not add arbitrary decimal opinions. It replaces three broad
grades with 12 frozen questions. DeepSeek leads because it earns full credit on
the default hot path, context/cache handling, deterministic safe parallelism,
model semantics, live extension, failure fidelity, durable state and safe
resume. It still loses 14 points: hard budget enforcement, general
tool-protocol coverage, crash-tail integrity and session rollback are only
partial in the pinned source evidence.

The exam contract contains no candidate names. Results cannot redefine a
question or weight, and CI rejects arithmetic drift or a full-credit answer
without an executable invariant. This is the anti-fit boundary: **4C writes the
exam; every Harness sits the same exam.**

Closed-source and runtime-only products remain in the dated
[market universe](../validation/market-universe.md) but cannot be placed on a
source-code ladder without fabricating evidence.
