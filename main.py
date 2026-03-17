#!/usr/bin/env python3
# ============================================================
# KeyForge Log-Scrubber — CLI Entry Point
# Privacy-first DevOps Tool
# By Sudhir Kumar (@SudhirDevOps1)
# ============================================================

from __future__ import annotations

import argparse
import sys
import textwrap
from pathlib import Path

from utils import print_stats, scan_and_scrub

# ── Banner ───────────────────────────────────────────────────
BANNER = r"""
 _  __          _____                     
| |/ /___ _   _|  ___|__  _ __ __ _  ___ 
| ' // _ \ | | | |_ / _ \| '__/ _` |/ _ \
| . \  __/ |_| |  _| (_) | | | (_| |  __/
|_|\_\___|\__, |_|  \___/|_|  \__, |\___|
          |___/  Log-Scrubber  |___/      

  Privacy-first DevOps Tool
  By Sudhir Kumar (@SudhirDevOps1)
"""


# ── CLI Definition ───────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="keyforge-scrubber",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
            KeyForge Log-Scrubber
            ---------------------
            Detect and redact sensitive data from log files.
            Sensitive data is replaced with [REDACTED].
            Original file is NEVER modified.
        """),
        epilog=textwrap.dedent("""\
            Examples:
              keyforge-scrubber scan logs.txt
              keyforge-scrubber scan logs.txt --strict
              keyforge-scrubber scan logs.txt --preview
              keyforge-scrubber scan logs.txt --custom-pattern "SSN:\\d{3}-\\d{2}-\\d{4}"
              keyforge-scrubber scan logs.txt --custom-pattern "TOKEN=[A-Z0-9]+" --strict
        """),
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # ── scan subcommand ──────────────────────────────────────
    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a log file and redact sensitive data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    scan_parser.add_argument(
        "file",
        metavar="FILE",
        help="Path to the log file to scan (e.g. logs.txt)",
    )

    scan_parser.add_argument(
        "--strict",
        action="store_true",
        default=False,
        help=(
            "Enable strict mode: also redact high-entropy strings "
            "≥ 40 chars (catches unknown token formats)"
        ),
    )

    scan_parser.add_argument(
        "--preview",
        action="store_true",
        default=False,
        help=(
            "Dry-run: print only the redacted lines to stdout. "
            "No output file is written."
        ),
    )

    scan_parser.add_argument(
        "--custom-pattern",
        metavar="REGEX",
        dest="custom_patterns",
        action="append",
        default=None,
        help=(
            "Add a custom regex pattern (can be used multiple times). "
            'Example: --custom-pattern "SSN:\\d{3}-\\d{2}-\\d{4}"'
        ),
    )

    return parser


# ── Entry Point ──────────────────────────────────────────────

def main() -> None:
    print(BANNER)

    parser = build_parser()
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    if args.command == "scan":
        input_path = Path(args.file)

        print(f"  🔍  Scanning  : {input_path}")
        print(f"  ⚡  Strict    : {'ON' if args.strict else 'OFF'}")
        print(f"  👁   Preview   : {'ON' if args.preview else 'OFF'}")

        if args.custom_patterns:
            print(f"  🔧  Custom rules: {len(args.custom_patterns)}")

        print()

        if args.preview:
            print("  ── Preview: Redacted Lines Only ──\n")

        stats = scan_and_scrub(
            input_path=input_path,
            custom_patterns=args.custom_patterns,
            strict=args.strict,
            preview=args.preview,
        )

        print_stats(stats)

        if not args.preview and stats["lines_modified"] > 0:
            print(f"\n  ✅  Clean file saved → {stats['output_file']}\n")
        elif stats["lines_modified"] == 0:
            print("\n  ✅  No sensitive data detected.\n")


if __name__ == "__main__":
    main()
