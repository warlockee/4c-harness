# 4C Case Studies

This document is for concrete examples showing how the same underlying
constraint produces different harness behavior.

## Case Study Template

For each provider or system:

### 1. Constraint

What economic, compatibility, temporal or experiential constraint
exists?

### 2. Documented semantics

What does the provider officially specify?

### 3. Empirical findings

What behavior has been discovered through experiments but is not
guaranteed by documentation?

### 4. Harness policy

What execution strategy follows from those facts?

### 5. Outcome

What changes in cost, reliability, task lifetime or learning?

## Provider Economics → Cost Policy

A core Cost thesis is:

> **Pricing semantics become execution semantics.**

Different billing functions can rationally produce different harnesses:

``` text
pricing / limits / cache behavior
              ↓
      provider-specific policy
              ↓
cache | compress | route | summarize | batch
              ↓
        actual task economics
```

The important asset may be less the implementation than the **empirical
findings** behind it.

A few hundred lines of policy code can be rewritten. Hundreds of trials
that discover cache boundaries, latency cliffs, undocumented
incompatibilities or context-price transitions may be substantially
harder to reproduce.

## Planned provider studies

The initial research queue should include:

-   DeepSeek: caching economics and prefix reuse
-   Anthropic: prompt caching and long-context economics
-   OpenAI: cached input, tool-loop semantics and model routing
-   Kimi: context-window economics and truncation/summarization policy
-   Qwen: context tiers and execution-policy implications

**Publication rule:** exact prices, cache rules and provider behaviors
must be verified against current primary sources before being stated as
facts.

## Cross-C study: Context Compression

Compression illustrates why 4C is a constraint taxonomy.

-   Compress to reduce paid tokens → **Cost**
-   Compress to keep a long-running task alive → **Continuity**
-   Learn when compression is safe from historical outcomes →
    **Cognition**

The implementation may be one function; the reasons for its existence
span three constraints.
