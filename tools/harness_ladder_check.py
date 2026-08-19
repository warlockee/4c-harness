#!/usr/bin/env python3
"""Verify that the published 4C Harness Ladder matches its scorecard data."""

from __future__ import annotations

import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "docs" / "scouts" / "fit-scores.json"
MARKET = ROOT / "docs" / "scouts" / "market-universe.json"
LADDER = ROOT / "assets" / "4c-harness-ladder.svg"
COMPARISON_ID = "interactive-coding-v1"
SVG_NS = "{http://www.w3.org/2000/svg}"
ROW_BAR_ORIGIN = 414.0
THRESHOLDS = (50, 65, 80, 100)


def elements_with_class(root: ET.Element, class_name: str) -> list[ET.Element]:
    return [
        element
        for element in root.iter()
        if class_name in element.get("class", "").split()
    ]


def one_with_class(root: ET.Element, class_name: str) -> ET.Element:
    matches = elements_with_class(root, class_name)
    if len(matches) != 1:
        raise ValueError(f"expected one {class_name!r} element, found {len(matches)}")
    return matches[0]


def display_number(value: float) -> str:
    return str(int(value)) if value.is_integer() else f"{value:g}"


def competition_ranks(candidates: list[dict]) -> list[int]:
    ranks: list[int] = []
    previous_score: float | None = None
    previous_rank = 0
    for position, candidate in enumerate(candidates, start=1):
        score = float(candidate["score"])
        if score != previous_score:
            previous_rank = position
            previous_score = score
        ranks.append(previous_rank)
    return ranks


def main() -> int:
    payload = json.loads(SCORES.read_text())
    market = json.loads(MARKET.read_text())
    comparison = next(
        item
        for item in payload["comparisons"]
        if item["comparison_id"] == COMPARISON_ID
    )
    indexed = list(enumerate(comparison["candidates"]))
    candidates = [
        candidate
        for _, candidate in sorted(indexed, key=lambda item: (-item[1]["score"], item[0]))
    ]
    ranks = competition_ranks(candidates)

    svg = ET.parse(LADDER).getroot()
    errors: list[str] = []
    if svg.get("data-comparison-id") != COMPARISON_ID:
        errors.append("SVG comparison id does not match the fixed comparison")
    if svg.get("data-market-snapshot") != market["snapshot_date"]:
        errors.append("SVG market snapshot does not match the market universe")
    pixels_per_point = float(svg.get("data-pixels-per-point", "nan"))
    global_bar_origin = float(svg.get("data-bar-origin", "nan"))

    rows = elements_with_class(svg, "candidate-row")
    if len(rows) != len(candidates):
        errors.append(f"SVG has {len(rows)} candidate rows; expected {len(candidates)}")
    else:
        for row, candidate, rank in zip(rows, candidates, ranks):
            name = candidate["candidate"]
            score = float(candidate["score"])
            prefix = f"{name}:"
            if row.get("data-candidate") != name:
                errors.append(f"{prefix} row order/name differs from scorecard")
            if row.get("data-score") != display_number(score):
                errors.append(f"{prefix} data-score differs from {display_number(score)}")
            if row.get("data-rank") != str(rank):
                errors.append(f"{prefix} rank differs from {rank}")

            try:
                candidate_label = one_with_class(row, "candidate-label").text or ""
                rank_label = one_with_class(row, "rank-label").text or ""
                score_label = one_with_class(row, "score-label").text or ""
                stage_label = one_with_class(row, "stage-label").text or ""
            except ValueError as error:
                errors.append(f"{prefix} {error}")
                continue
            if candidate_label != name:
                errors.append(f"{prefix} visible candidate label is stale")
            if rank_label != f"{rank:02d}":
                errors.append(f"{prefix} visible rank label is stale")
            if score_label != display_number(score):
                errors.append(f"{prefix} visible score label is stale")
            if stage_label != candidate["evidence_stage"].upper():
                errors.append(f"{prefix} visible evidence stage is stale")

            segments = elements_with_class(row, "score-segment")
            active_pressures = [
                pressure
                for pressure, weight in comparison["weights"].items()
                if weight > 0
            ]
            if [segment.get("data-pressure") for segment in segments] != active_pressures:
                errors.append(f"{prefix} score segments differ from active-C order")
                continue
            expected_x = ROW_BAR_ORIGIN
            contribution_sum = 0.0
            for segment, pressure in zip(segments, active_pressures):
                contribution = (
                    comparison["weights"][pressure]
                    * candidate["grades"][pressure]
                    / 5
                )
                contribution_sum += contribution
                width = contribution * pixels_per_point
                segment_x = float(segment.get("x", "nan"))
                segment_width = float(segment.get("width", "nan"))
                if abs(segment_x - expected_x) > 1e-9:
                    errors.append(f"{prefix} {pressure} segment starts at the wrong point")
                if abs(segment_width - width) > 1e-9:
                    errors.append(
                        f"{prefix} {pressure} width is {segment_width:g}; expected {width:g}"
                    )
                expected_x += width
            if abs(contribution_sum - score) > 1e-9:
                errors.append(f"{prefix} segment contributions do not sum to score")

    legend = {
        item.get("data-pressure"): item.get("data-weight")
        for item in elements_with_class(svg, "legend-item")
    }
    expected_legend = {
        pressure: str(weight) for pressure, weight in comparison["weights"].items()
    }
    if legend != expected_legend:
        errors.append("legend weights differ from the fixed comparison")

    threshold_elements = elements_with_class(svg, "score-threshold")
    if [int(item.get("data-score", "-1")) for item in threshold_elements] != list(THRESHOLDS):
        errors.append("score thresholds are incomplete or out of order")
    else:
        for threshold, element in zip(THRESHOLDS, threshold_elements):
            expected_x = global_bar_origin + threshold * pixels_per_point
            if abs(float(element.get("x1", "nan")) - expected_x) > 1e-9:
                errors.append(f"threshold {threshold} is not aligned to the score scale")

    leader = candidates[0]
    try:
        leader_name = one_with_class(svg, "leader-candidate").text or ""
        leader_score = one_with_class(svg, "leader-score").text or ""
        if leader_name != leader["candidate"]:
            errors.append("leader callout candidate is stale")
        if leader_score != display_number(float(leader["score"])):
            errors.append("leader callout score is stale")
    except ValueError as error:
        errors.append(str(error))

    products = market.get("products", [])
    product_names = [product.get("name") for product in products]
    if len(product_names) != len(set(product_names)):
        errors.append("market universe contains duplicate product names")

    allowed_statuses = {"ranked", "source-audit-queued", "runtime-evidence-needed"}
    for product in products:
        name = product.get("name", "<unnamed>")
        status = product.get("status")
        if status not in allowed_statuses:
            errors.append(f"{name}: unsupported market status {status!r}")
        if not str(product.get("official_url", "")).startswith("https://"):
            errors.append(f"{name}: official_url must be HTTPS")
        if status == "source-audit-queued":
            commit = str(product.get("pinned_commit", ""))
            if len(commit) != 40 or any(character not in "0123456789abcdef" for character in commit):
                errors.append(f"{name}: source audit queue requires a 40-character commit")
            if int(product.get("stars_at_snapshot", 0)) < 10_000:
                errors.append(f"{name}: source audit queue misses the market-presence gate")

    ranked_names = {product["name"] for product in products if product["status"] == "ranked"}
    scorecard_names = {candidate["candidate"] for candidate in candidates}
    if ranked_names != scorecard_names:
        errors.append("ranked market products differ from the fixed comparison")

    expected_unranked = [
        product for product in products if product["status"] != "ranked"
    ]
    market_rows = elements_with_class(svg, "market-candidate")
    if len(market_rows) != len(expected_unranked):
        errors.append(
            f"SVG has {len(market_rows)} unranked market products; "
            f"expected {len(expected_unranked)}"
        )
    else:
        for row, product in zip(market_rows, expected_unranked):
            name = product["name"]
            if row.get("data-candidate") != name:
                errors.append(f"{name}: market row order/name differs from universe")
            if row.get("data-status") != product["status"]:
                errors.append(f"{name}: market row status differs from universe")
            try:
                label = one_with_class(row, "market-candidate-label").text or ""
                if label != name:
                    errors.append(f"{name}: visible market label is stale")
            except ValueError as error:
                errors.append(f"{name}: {error}")

    expected_count = (
        f"{len(products)} ACTIVE PRODUCTS / {len(expected_unranked)} AWAITING EVIDENCE"
    )
    try:
        visible_count = one_with_class(svg, "market-count").text or ""
        if visible_count != expected_count:
            errors.append("visible market count is stale")
    except ValueError as error:
        errors.append(str(error))

    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    print(
        f"PASS 4C Harness Ladder: {len(candidates)} ranked, "
        f"{len(expected_unranked)} awaiting evidence, "
        f"{leader['candidate']} leads at {display_number(float(leader['score']))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
