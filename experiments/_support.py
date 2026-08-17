#!/usr/bin/env python3
"""Shared preconditions and evidence labelling for the reproduction suite.

Two distinctions matter here and were previously left implicit.

**Precondition versus claim.** A missing local CLI is not a falsification of a
4C claim; it means the experiment could not run. Preconditions therefore exit
with `SKIP_EXIT_CODE` and `run_all.py` reports them as skipped, while claim
checks fail the suite.

**Evidence level.** An experiment that observes an upstream system's own
behaviour is stronger evidence than one that instruments a boundary with
locally authored code. Every report states which it is, so that no reader has
to infer it from the imports.
"""

from __future__ import annotations

import sys


SKIP_EXIT_CODE = 77

#: The experiment varies a cause and observes behaviour produced by the
#: upstream system itself. The classification is supported by third-party code.
THIRD_PARTY_BEHAVIOUR = (
    "third-party behaviour: the observed policy delta is produced by the "
    "upstream system under test"
)

#: The experiment instruments a boundary with locally authored code. It shows
#: that the distinction can be stated and mechanised; it is not independent
#: evidence that any upstream system draws the boundary this way.
INSTRUMENTED_ILLUSTRATION = (
    "instrumented illustration: the policy delta is produced by locally "
    "authored code, with the upstream package supplying only the named "
    "primitive"
)

#: The experiment reads a declared interface rather than exercising it.
DECLARED_INTERFACE = (
    "declared interface: control surfaces are read from a shipped binary; "
    "enforcement is not exercised"
)


class ClaimFailure(AssertionError):
    """A checked experimental claim did not hold."""


def require(condition: object, message: str) -> None:
    """Check an experimental claim.

    Unlike `assert`, this survives `python -O`, so a suite run with
    optimisations enabled cannot silently report success.
    """
    if not condition:
        raise ClaimFailure(message)


def skip(message: str) -> None:
    """Report an unmet precondition and exit without failing the suite."""
    print(f"SKIP {message}", file=sys.stderr)
    raise SystemExit(SKIP_EXIT_CODE)
