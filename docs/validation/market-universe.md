# 4C Harness market universe

Snapshot: **2026-08-19**  
Scope: `active-general-purpose-coding-harness-v1`

The market universe tracks **31 active Harness products**. The opening ladder
ranks all **15 open-source products** that pass the public-implementation and
10,000-star gates on the frozen candidate-blind `interactive-coding-v2` exam. The remaining
16 need runtime evidence and are not given fabricated source scores.

## Inclusion rule

A product enters this snapshot only when all of these are true:

1. It can inspect an existing repository, change code, and run commands, tests,
   or a pull-request workflow.
2. Its official repository or first-party product documentation is active on
   the snapshot date. Archived products and public repositories without
   activity in the preceding 180 days are excluded.
3. It has either a public implementation with at least 10,000 GitHub stars or
   a maintained, first-party commercial product page.
4. One named product counts once. IDE, CLI, web, mobile, and cloud surfaces do
   not become separate entries unless they expose materially different
   Harnesses.

This excludes model APIs without a Harness, autocomplete-only assistants,
greenfield app builders that cannot work on arbitrary existing repositories,
libraries/frameworks, archived products, and duplicate surfaces.

The machine-readable source of truth is
[`market-universe.json`](../scouts/market-universe.json). Missing candidates can
be proposed with the
[market-coverage issue](https://github.com/warlockee/4c-harness/issues/new?template=market-coverage.yml)
or a pull request; the same published rule must admit or reject them.

## Why 16 products have no score

`Unranked` means **unknown, not worse**.

- **Runtime evidence needed** means the product is closed-source or its public
  repository is too thin to support source scoring. It needs a controlled,
  same-terrain task trial.

Publishing placeholder scores would turn market coverage into fabrication.
The market universe exposes that evidence gap separately from the source ladder.

## Transition notes

- Gemini CLI remains active for enterprise and API-key users. Google moved the
  individual subscription terminal path to Antigravity CLI in June 2026, so
  both are tracked and their product scopes are not silently conflated.
- The official Antigravity CLI and GitHub Copilot CLI repositories expose
  documentation, installers, examples, or changelogs, but not enough public
  implementation to earn source grades. They remain runtime-evidence entries.
- Roo Code is archived and Plandex failed the 180-day activity gate; both stay
  in the exclusion ledger rather than disappearing without explanation.
