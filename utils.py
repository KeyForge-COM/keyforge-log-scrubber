# ============================================================
# KeyForge Log-Scrubber — Core Utilities
# Privacy-first DevOps Tool
# By Sudhir Kumar (@SudhirDevOps1)
# ============================================================

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterator

from patterns import REDACT_PLACEHOLDER, get_all_patterns

# ── Constants ────────────────────────────────────────────────
CHUNK_SIZE = 1024 * 64  # 64 KB per chunk — safe for large files
OUTPUT_SUFFIX = "_cleaned"


# ── Helpers ──────────────────────────────────────────────────

def _build_output_path(input_path: Path) -> Path:
    """
    Derive the cleaned file path.

    Example:
        logs.txt  →  logs_cleaned.txt
    """
    return input_path.with_name(
        f"{input_path.stem}{OUTPUT_SUFFIX}{input_path.suffix}"
    )


def _scrub_line(
    line: str,
    patterns: dict[str, re.Pattern],
    strict: bool = False,
) -> tuple[str, list[str]]:
    """
    Apply all patterns to a single log line.

    Args:
        line:     Raw log line.
        patterns: Compiled regex patterns.
        strict:   If True, also redact any token ≥ 20 consecutive
                  non-whitespace chars that looks high-entropy.

    Returns:
        (scrubbed_line, list_of_matched_pattern_names)
    """
    hits: list[str] = []

    for name, pattern in patterns.items():
        # Groups present? Redact only the captured group, not the key name
        if pattern.groups:
            def _replace_group(m: re.Match) -> str:
                full = m.group(0)
                for g in m.groups():
                    if g:
                        full = full.replace(g, REDACT_PLACEHOLDER, 1)
                return full

            new_line, count = pattern.subn(_replace_group, line)
        else:
            new_line, count = pattern.subn(REDACT_PLACEHOLDER, line)

        if count:
            hits.append(name)
            line = new_line

    # ── Strict mode extra sweep ──────────────────────────────
    if strict:
        high_entropy = re.compile(r"[A-Za-z0-9+/=_\-]{40,}")
        new_line, count = high_entropy.subn(REDACT_PLACEHOLDER, line)
        if count:
            hits.append("HIGH_ENTROPY")
            line = new_line

    return line, hits


def _iter_lines_chunked(file_path: Path) -> Iterator[str]:
    """
    Memory-efficient line iterator using buffered reads.
    Handles files of any size without loading all into RAM.
    """
    with file_path.open("r", encoding="utf-8", errors="replace") as fh:
        buffer = ""
        while True:
            chunk = fh.read(CHUNK_SIZE)
            if not chunk:
                if buffer:
                    yield buffer   # last line without newline
                break
            buffer += chunk
            lines = buffer.split("\n")
            # Keep last partial line in the buffer
            buffer = lines.pop()
            yield from (line + "\n" for line in lines)


# ── Public API ───────────────────────────────────────────────

def scan_and_scrub(
    input_path: Path,
    custom_patterns: list[str] | None = None,
    strict: bool = False,
    preview: bool = False,
) -> dict:
    """
    Main scrubbing routine.

    Args:
        input_path:      Source log file.
        custom_patterns: Extra regex strings from --custom-pattern.
        strict:          Enable high-entropy sweep.
        preview:         Dry-run; print to stdout, no file written.

    Returns:
        Stats dictionary.
    """
    if not input_path.exists():
        print(f"[ERROR] File not found: {input_path}")
        sys.exit(1)

    if not input_path.is_file():
        print(f"[ERROR] Path is not a file: {input_path}")
        sys.exit(1)

    patterns = get_all_patterns(custom_patterns)
    output_path = _build_output_path(input_path)

    stats: dict = {
        "lines_scanned": 0,
        "lines_modified": 0,
        "total_redactions": 0,
        "pattern_hits": {},
        "output_file": str(output_path) if not preview else "PREVIEW (no file written)",
    }

    # ── Open output (or stdout for preview) ─────────────────
    out_fh = sys.stdout if preview else output_path.open(
        "w", encoding="utf-8"
    )

    try:
        for line in _iter_lines_chunked(input_path):
            scrubbed, hits = _scrub_line(line, patterns, strict)
            stats["lines_scanned"] += 1

            if hits:
                stats["lines_modified"] += 1
                stats["total_redactions"] += len(hits)
                for h in hits:
                    stats["pattern_hits"][h] = stats["pattern_hits"].get(h, 0) + 1

            if preview:
                # Only print lines that were changed
                if hits:
                    out_fh.write(scrubbed)
            else:
                out_fh.write(scrubbed)

    finally:
        if not preview:
            out_fh.close()

    return stats


def print_stats(stats: dict) -> None:
    """Pretty-print the scrubbing summary."""
    sep = "─" * 50
    print(f"\n{sep}")
    print("  📊  KeyForge Scrub Report")
    print(sep)
    print(f"  Lines scanned   : {stats['lines_scanned']:,}")
    print(f"  Lines modified  : {stats['lines_modified']:,}")
    print(f"  Total redactions: {stats['total_redactions']:,}")
    print(f"  Output file     : {stats['output_file']}")
    if stats["pattern_hits"]:
        print(f"\n  Pattern breakdown:")
        for name, count in sorted(
            stats["pattern_hits"].items(), key=lambda x: -x[1]
        ):
            print(f"    {name:<20} {count:>6} hit(s)")
    print(sep)
