#!/usr/bin/env python3
"""Observe provider-semantic translation in LiteLLM without making API calls.

Evidence level: third-party behaviour. Every observed difference is produced by
LiteLLM's own parameter mapping; this file only holds the canonical request
fixed and reads what the library emits per provider.
"""

from __future__ import annotations

import importlib.metadata
import json
import platform
from copy import deepcopy

import litellm

from _support import THIRD_PARTY_BEHAVIOUR, require


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
    require(
        CANONICAL_TOOL["function"]["parameters"] == {"type": "object", "properties": {}},
        "the canonical request was mutated during translation",
    )

    # Same semantic request, provider-specific representations.
    require(translated["openai"]["stop"] == ["END"], "openai stop sequence changed shape")
    require(
        translated["anthropic"]["stop_sequences"] == ["END"],
        "anthropic stop sequence changed shape",
    )
    require(
        translated["bedrock"]["stopSequences"] == ["END"],
        "bedrock stop sequence changed shape",
    )
    require(
        translated["gemini"]["stop_sequences"] == ["END"],
        "gemini stop sequence changed shape",
    )

    require(
        translated["openai"]["tools"][0]["function"]["parameters"]
        == {"type": "object", "properties": {}},
        "openai tool schema is no longer nested under function.parameters",
    )
    require(
        translated["anthropic"]["tools"][0]["input_schema"]
        == {"type": "object", "properties": {}},
        "anthropic tool schema is no longer expressed as input_schema",
    )
    require(
        "function_declarations" in translated["gemini"]["tools"][0],
        "gemini tool schema is no longer expressed as function_declarations",
    )

    # Translation is deterministic when the target semantics are fixed.
    require(
        translated["anthropic"] == translate("anthropic", TARGETS["anthropic"]),
        "translation is not deterministic for a fixed target",
    )
    serialized = {json.dumps(value, sort_keys=True) for value in translated.values()}
    require(
        len(serialized) == len(TARGETS),
        "two providers produced an identical representation",
    )

    report = {
        "experiment": "litellm-provider-compatibility",
        "evidence_level": THIRD_PARTY_BEHAVIOUR,
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
