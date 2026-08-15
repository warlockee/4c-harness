# 4C Harness Landscape

4C can describe the **shape** of an execution system without forcing
every product into one category.

## Archetypes

  Archetype                   Cost          Compatibility   Continuity    Cognition
  --------------------------- ------------- --------------- ------------- -----------
  API adapter                 Low           High            Low           Low
  Model gateway               High          High            Low--Medium   Low
  Optimizer                   High          Medium--High    Low--Medium   Medium
  Agent-loop library          Low--Medium   Medium          Medium        Low
  Durable agent runtime       Medium        Medium--High    High          Medium
  Observability/eval system   Low           Low--Medium     Low           High
  Full harness platform       High          High            High          High
  Self-improving harness      High          High            High          Very High

These are archetypes, not vendor labels.

## Inference infrastructure vs. Harness

Low-level inference systems primarily optimize **computation**.
Harnesses optimize **task execution across model calls**.

A cache inside an inference engine and a cache policy inside a harness
may share a name while operating at different abstraction layers.

The useful question is:

> **What object is being optimized: computation or execution?**

## Evidence-based mapping template

For every real system, document:

1.  its primary abstraction;
2.  concrete Cost mechanisms;
3.  concrete Compatibility mechanisms;
4.  concrete Continuity mechanisms;
5.  concrete Cognition mechanisms;
6.  what it deliberately leaves to another layer;
7.  whether each claim is documented, empirically observed, or inferred.

Candidate systems for later evidence-based mapping include model
gateways, agent SDKs, durable runtimes, coding-agent harnesses,
observability/eval platforms and inference engines.

This file should remain evidence-driven: product scores should be added
only after source verification.
