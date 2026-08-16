#!/usr/bin/env python3
"""Observe provider-semantic translation in LiteLLM without making API calls."""

from __future__ import annotations

import importlib.metadata
import json
import platform
from copy import deepcopy

import litellm


CANONICAL_TOOL = {
    "type": "function",
    "function": {
        "name": "lookup",
        "description": "Look up a fixed record",
        "parameters": {"type": "object", "properties": {}},
    },
}

TARGETS = {
    "openai": "gpt-4o",
    "anthropic": "claude-3-5-sonnet-20241022",
    "bedrock": "anthropic.claude-3-5-sonnet-20241022-v2:0",
    "gemini": "gemini-2.0-flash",
}


def translate(provider: str, model: str) -> dict[str, object]:
    return litellm.get_optional_params(
        model=model,
        custom_llm_provider=provider,
        max_tokens=128,
        stop=["END"],
        tools=[deepcopy(CANONICAL_TOOL)],
        tool_choice="auto",
        messages=[{"role": "user", "content": "fixed request"}],
    )


def main() -> None:
    translated = {
        provider: translate(provider, model) for provider, model in TARGETS.items()
    }
    assert CANONICAL_TOOL["function"]["parameters"] == {
        "type": "object",
        "properties": {},
    }

    # Same semantic request, provider-specific representations.
    assert translated["openai"]["stop"] == ["END"]
    assert translated["anthropic"]["stop_sequences"] == ["END"]
    assert translated["bedrock"]["stopSequences"] == ["END"]
    assert translated["gemini"]["stop_sequences"] == ["END"]

    assert translated["openai"]["tools"][0]["function"]["parameters"] == {
        "type": "object",
        "properties": {},
    }
    assert translated["anthropic"]["tools"][0]["input_schema"] == {
        "type": "object",
        "properties": {},
    }
    assert "function_declarations" in translated["gemini"]["tools"][0]

    # Translation is deterministic when the target semantics are fixed.
    assert translated["anthropic"] == translate("anthropic", TARGETS["anthropic"])
    serialized = {json.dumps(value, sort_keys=True) for value in translated.values()}
    assert len(serialized) == len(TARGETS)

    report = {
        "experiment": "litellm-provider-compatibility",
        "runtime": platform.python_version(),
        "litellm": importlib.metadata.version("litellm"),
        "controlled_variables": [
            "canonical messages",
            "max token value",
            "stop sequence",
            "tool name and schema",
            "tool-choice intent",
            "no network request",
        ],
        "independent_variable": "target provider semantics",
        "targets": TARGETS,
        "translated_parameters": translated,
        "result": {
            "compatibility_residual": True,
            "claim": (
                "Holding task intent and canonical parameters fixed, target "
                "provider semantics change the required request representation."
            ),
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
