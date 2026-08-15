# The 4C Theory of AI Harness

> **Models create intelligence. Infrastructure creates computation.
> Harnesses create execution. Applications create user value.**

As models commoditize, complexity does not disappear. **It moves into
the harness.**

The 4C Theory defines the Harness as the engineering layer that turns
bounded, mostly stateless model calls into production execution. It
exists to solve four persistent constraints:

  -----------------------------------------------------------------------
  4C                      Reality                 Question
  ----------------------- ----------------------- -----------------------
  **Cost**                Resources are finite    How should execution
                                                  change because
                                                  resources are not free?

  **Compatibility**       The world is            How should execution
                          heterogeneous           change because models,
                                                  tools and environments
                                                  differ?

  **Continuity**          Tasks unfold through    How should execution
                          time                    persist and remain
                                                  controlled across
                                                  inference boundaries?

  **Cognition**           Experience should       How should future
                          compound                execution improve
                                                  because of what
                                                  happened before?
  -----------------------------------------------------------------------

## The stack

``` text
APPLICATION      → optimizes user value
HARNESS          → optimizes execution
INFRASTRUCTURE   → optimizes computation
MODEL            → creates intelligence
```

**4C is not a feature taxonomy. It is a constraint taxonomy.** A
mechanism may solve several constraints: compression can serve Cost +
Continuity; routing can serve Cost + Compatibility + Cognition.

## Reinterpreting the buzzwords

-   **Cost:** caching, compression, routing, batching, token/latency
    budgeting
-   **Compatibility:** adapters, tool calling, structured output, MCP,
    A2A
-   **Continuity:** agent loops, loop engineering, memory,
    checkpoint/resume, durable execution, human-in-the-loop
-   **Cognition:** tracing, replay, evals, diagnosis, self-debugging,
    learning and adaptation

> **Loop Engineering is Continuity Engineering.**\
> **Observability records experience. Cognition compounds it.**

## Repository

-   [Theory](docs/theory.md) --- canonical definitions and boundaries
-   [Landscape](docs/landscape.md) --- mapping real systems into 4C
-   [Case studies](docs/case-studies.md) --- concrete provider/harness
    cases
-   [Counterarguments](docs/counterarguments.md) --- attacks and
    falsification tests
-   [Predictions](docs/predictions.md) --- falsifiable predictions

Diagram sources are available in [`assets/diagrams`](assets/diagrams).

The previous generation of harnesses made agents stateful.

> **The next generation will make harnesses self-improving.**
