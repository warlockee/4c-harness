#!/usr/bin/env python3
"""Render the README ladder from the fixed comparison scorecard."""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "docs/scouts/fit-scores.json"
MARKET = ROOT / "docs/scouts/market-universe.json"
OUTPUT = ROOT / "assets/4c-harness-ladder.svg"
COMPARISON_ID = "interactive-coding-v1"
COLORS = {"Cost": "#FDBD2E", "Compatibility": "#2CC6B7", "Continuity": "#8B7CFF"}
LABELS = {"Cost": "DOLLAR EFFICIENCY", "Compatibility": "COMPATIBILITY", "Continuity": "CONTINUITY"}
PX = 9
ROW_X = 56
BAR_X = 414
GLOBAL_BAR_X = ROW_X + BAR_X


def competition_ranks(items: list[dict]) -> list[int]:
    out, last_score, last_rank = [], None, 0
    for position, item in enumerate(items, 1):
        if item["score"] != last_score:
            last_score, last_rank = item["score"], position
        out.append(last_rank)
    return out


def main() -> None:
    data = json.loads(SCORES.read_text())
    market = json.loads(MARKET.read_text())
    comparison = next(x for x in data["comparisons"] if x["comparison_id"] == COMPARISON_ID)
    indexed = list(enumerate(comparison["candidates"]))
    candidates = [x for _, x in sorted(indexed, key=lambda pair: (-pair[1]["score"], pair[0]))]
    ranks = competition_ranks(candidates)
    top = candidates[0]["score"]
    leaders = [x for x in candidates if x["score"] == top]
    row_start, row_step, row_height = 318, 66, 56
    row_end = row_start + row_step * (len(candidates) - 1) + row_height
    footer_y = row_end + 52
    height = footer_y + 178
    esc = html.escape
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="1792" height="{height}" viewBox="0 0 1792 {height}" role="img" aria-labelledby="title desc" data-comparison-id="{COMPARISON_ID}" data-market-snapshot="{market["snapshot_date"]}" data-bar-origin="{GLOBAL_BAR_X}" data-pixels-per-point="{PX}">',
        '<title id="title">4C open-source Harness ladder for interactive coding</title>',
        f'<desc id="desc">Fifteen active open-source coding Harnesses ranked from pinned code evidence. Five source-fit leaders tie at {top}. Longer bars mean better fit, not higher price.</desc>',
        '<defs><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#B8C5D6" stroke-width="1" opacity=".28"/></pattern></defs>',
        f'<rect width="1792" height="{height}" fill="#EEF3F9"/><rect width="1792" height="{height}" fill="url(#grid)"/>',
        '<rect width="1792" height="44" fill="#101826"/>',
        '<text x="52" y="29" fill="#fff" font-family="SFMono-Regular,Menlo,monospace" font-size="15" font-weight="700" letter-spacing="3">4C // THE HARNESS EVALUATION STANDARD</text>',
        '<rect x="1480" y="8" width="260" height="28" fill="#FF5A36"/><text x="1610" y="28" text-anchor="middle" fill="#fff" font-family="SFMono-Regular,Menlo,monospace" font-size="14" font-weight="700" letter-spacing="2">PINNED · AUDITABLE</text>',
        '<text x="56" y="105" fill="#2457FF" font-family="SFMono-Regular,Menlo,monospace" font-size="18" font-weight="700" letter-spacing="3">4C OPEN-SOURCE HARNESS LADDER / 2026-08-19</text>',
        '<text x="52" y="163" fill="#101826" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="62" font-weight="900" letter-spacing="-2">SEE A HARNESS. THINK 4C.</text>',
        '<text x="56" y="198" fill="#53657A" font-family="Helvetica Neue,Arial,sans-serif" font-size="19">One terrain · One formula · Exact commits · Source-fit predictions, not runtime claims</text>',
        f'<text class="coverage-count" x="56" y="232" fill="#101826" font-family="SFMono-Regular,Menlo,monospace" font-size="14" font-weight="700">{len(candidates)} OPEN-SOURCE PRODUCTS · {len(candidates)} PINNED CODE AUDITS</text>',
        '<g transform="translate(1160 70)"><rect width="576" height="174" fill="#101826"/>',
        '<text x="24" y="29" fill="#8FA3BC" font-family="SFMono-Regular,Menlo,monospace" font-size="12" letter-spacing="2">SOURCE-FIT LEADERS · TIED BY EVIDENCE</text>',
    ]
    for i, leader in enumerate(leaders):
        lines.append(f'<text class="leader-candidate" x="24" y="{61+i*21}" fill="#fff" font-family="Helvetica Neue,Arial,sans-serif" font-size="18" font-weight="800">{esc(leader["candidate"])}</text>')
    lines += [
        f'<text class="leader-score" x="546" y="144" text-anchor="end" fill="#FDBD2E" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="58" font-weight="900">{top}</text>',
        '<text x="546" y="163" text-anchor="end" fill="#8FA3BC" font-family="SFMono-Regular,Menlo,monospace" font-size="11">4C FIT / 100</text></g>',
        '<text x="56" y="284" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">RANK</text><text x="158" y="284" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">HARNESS / EVIDENCE</text>',
    ]
    for threshold, label in ((50, "CONDITIONAL"), (65, "STRONG"), (80, "EXCELLENT"), (100, "100")):
        x = GLOBAL_BAR_X + threshold * PX
        lines.append(f'<text x="{x}" y="272" text-anchor="middle" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="11">{threshold}</text>')
        lines.append(f'<text x="{x}" y="289" text-anchor="middle" fill="#6D7E92" font-family="SFMono-Regular,Menlo,monospace" font-size="10">{label}</text>')
        lines.append(f'<line class="score-threshold" data-score="{threshold}" x1="{x}" y1="298" x2="{x}" y2="{row_end}" stroke="#8393A7" stroke-width="1" stroke-dasharray="4 6" opacity=".5"/>')

    for idx, (item, rank) in enumerate(zip(candidates, ranks)):
        y = row_start + idx * row_step
        leader = item["score"] == top
        bg, fg, sub, stroke = ("#101826", "#FFFFFF", "#8FA3BC", "#2457FF") if leader else ("#FFFFFF", "#101826", "#718196", "#C7D2E0")
        lines += [
            f'<!-- {esc(item["candidate"])} -->',
            f'<g class="candidate-row" data-candidate="{esc(item["candidate"])}" data-score="{item["score"]}" data-rank="{rank}" transform="translate({ROW_X} {y})">',
            f'<rect width="1680" height="{row_height}" fill="{bg}" stroke="{stroke}" stroke-width="{2 if leader else 1}"/>',
            f'<text class="rank-label" x="18" y="38" fill="{fg}" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="31" font-weight="900">{rank:02d}</text>',
            f'<text class="candidate-label" x="98" y="25" fill="{fg}" font-family="Helvetica Neue,Arial,sans-serif" font-size="21" font-weight="800">{esc(item["candidate"])}</text>',
            f'<text class="stage-label" x="98" y="44" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="9">{item["evidence_stage"].upper()}</text>',
            f'<rect x="{BAR_X}" y="15" width="900" height="27" fill="{("#27354A" if leader else "#D9E1EB")}"/>',
        ]
        cursor = BAR_X
        for pressure, weight in comparison["weights"].items():
            if weight == 0:
                continue
            contribution = weight * item["grades"][pressure] / 5
            width = contribution * PX
            lines.append(f'<rect class="score-segment" data-pressure="{pressure}" x="{cursor:g}" y="15" width="{width:g}" height="27" fill="{COLORS[pressure]}"/>')
            cursor += width
        grade_text = f'D{item["grades"]["Cost"]} · K{item["grades"]["Compatibility"]} · N{item["grades"]["Continuity"]}'
        lines += [
            f'<text x="1360" y="23" fill="{sub}" font-family="SFMono-Regular,Menlo,monospace" font-size="9">{grade_text}</text>',
            f'<text x="1360" y="41" fill="{fg}" font-family="SFMono-Regular,Menlo,monospace" font-size="11" font-weight="700">{item["exact_commit"][:7]}</text>',
            f'<text class="score-label" x="1632" y="41" text-anchor="end" fill="{fg}" font-family="Arial Narrow,Helvetica Neue,Arial,sans-serif" font-size="37" font-weight="900">{item["score"]}</text>',
            '</g>',
        ]

    lines.append(f'<g transform="translate(56 {footer_y})" font-family="SFMono-Regular,Menlo,monospace">')
    lx = 0
    for pressure, weight in comparison["weights"].items():
        if pressure == "Cognition":
            lines.append(f'<g class="legend-item" data-pressure="{pressure}" data-weight="{weight}"><text x="1120" y="17" fill="#718196" font-size="12">COGNITION 0% / INACTIVE</text></g>')
        else:
            lines.append(f'<g class="legend-item" data-pressure="{pressure}" data-weight="{weight}"><rect x="{lx}" width="18" height="18" fill="{COLORS[pressure]}"/><text x="{lx+28}" y="15" fill="#101826" font-size="13" font-weight="700">{LABELS[pressure]} {weight}%</text></g>')
            lx += {"Cost": 340, "Compatibility": 300, "Continuity": 270}[pressure]
    lines += [
        '<text x="0" y="52" fill="#2457FF" font-size="13" font-weight="700">LONGER BAR = MORE VERIFIED OUTPUT PER LIMIT. DOLLAR EFFICIENCY IS BETTER WHEN LONGER.</text>',
        '<line x1="0" y1="74" x2="1680" y2="74" stroke="#C7D2E0"/>',
        '<text x="0" y="102" fill="#101826" font-size="12">SCOPE  Active general-purpose open-source coding Harnesses with ≥10k GitHub stars</text>',
        '<text x="0" y="126" fill="#53657A" font-size="11">GRADE  Source ceiling = 4/5 · Every 3+ requires implementation + executable invariant + reachability + falsifier</text>',
        '<text x="0" y="150" fill="#53657A" font-size="11">BOUNDARY  Source-fit prediction only. Paired runtime trials may overturn this order. Equal evidence stays tied.</text>',
        '</g></svg>',
    ]
    OUTPUT.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
