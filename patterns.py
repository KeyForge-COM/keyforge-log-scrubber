# ============================================================
# KeyForge Log-Scrubber — Pattern Definitions
# Privacy-first DevOps Tool
# By Sudhir Kumar (@SudhirDevOps1)
# ============================================================

import re

# ── Built-in detection patterns ──────────────────────────────
BUILT_IN_PATTERNS: dict[str, re.Pattern] = {

    "EMAIL": re.compile(
        r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
        re.IGNORECASE,
    ),

    "IPV4": re.compile(
        r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}"
        r"(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    ),

    "IPV6": re.compile(
        r"\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b"
        r"|\b(?:[0-9a-fA-F]{1,4}:){1,7}:\b"
        r"|\b::(?:[0-9a-fA-F]{1,4}:){0,6}[0-9a-fA-F]{1,4}\b",
        re.IGNORECASE,
    ),

    # Generic high-entropy API key / secret (32–64 hex/base64 chars)
    "API_KEY": re.compile(
        r"(?i)(?:api[_\-]?key|secret|token|auth|passwd|password)"
        r"[\s:=\"']*"
        r"([A-Za-z0-9\-_/+]{32,64})"
    ),

    # AWS-style access key
    "AWS_KEY": re.compile(
        r"\b(AKIA[0-9A-Z]{16})\b"
    ),

    # JWT  (header.payload.signature)
    "JWT": re.compile(
        r"\beyJ[A-Za-z0-9\-_]+\."     # header  (starts with eyJ)
        r"[A-Za-z0-9\-_]+\."          # payload
        r"[A-Za-z0-9\-_+/=]+\b"       # signature
    ),

    # Credit card — Visa / MC / Amex / Discover (with optional separators)
    "CREDIT_CARD": re.compile(
        r"\b(?:"
        r"4[0-9]{12}(?:[0-9]{3})?"            # Visa
        r"|5[1-5][0-9]{14}"                   # MasterCard
        r"|3[47][0-9]{13}"                    # Amex
        r"|6(?:011|5[0-9]{2})[0-9]{12}"       # Discover
        r")(?:[\s\-]?[0-9]{4})?\b"
    ),

    # Bearer / OAuth tokens
    "BEARER_TOKEN": re.compile(
        r"(?i)Bearer\s+[A-Za-z0-9\-_=.+/]{20,}"
    ),

    # Generic password field in logs
    "PASSWORD_FIELD": re.compile(
        r'(?i)(?:password|passwd|pwd)\s*[=:]\s*\S+'
    ),
}

# Replacement placeholder
REDACT_PLACEHOLDER = "[REDACTED]"


def get_all_patterns(custom: list[str] | None = None) -> dict[str, re.Pattern]:
    """
    Return all active patterns, optionally appending user-supplied regex strings.

    Args:
        custom: List of raw regex strings passed via --custom-pattern.

    Returns:
        Combined pattern dictionary.
    """
    patterns = dict(BUILT_IN_PATTERNS)  # copy; never mutate the original

    if custom:
        for idx, raw in enumerate(custom, start=1):
            key = f"CUSTOM_{idx}"
            try:
                patterns[key] = re.compile(raw)
                print(f"  [+] Custom pattern #{idx} loaded: {raw}")
            except re.error as exc:
                print(f"  [!] Invalid regex for custom pattern #{idx}: {exc}")

    return patterns
