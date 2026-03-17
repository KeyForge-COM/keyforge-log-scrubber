# 🧹 KeyForge Log-Scrubber

> **Privacy-first DevOps Tool**  
> By Sudhir Kumar ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))

---

## 🚀 What It Does

KeyForge Log-Scrubber scans log files and automatically detects
and redacts sensitive information — replacing it with `[REDACTED]`.

The **original file is never modified**. A clean copy is saved separately.

---

## 📦 Requirements

- Python 3.10+
- No external dependencies (standard library only)

---

## ⚙️ Installation

```bash
git clone https://github.com/SudhirDevOps1/keyforge-log-scrubber.git
cd keyforge-log-scrubber
chmod +x main.py
```

---

## 💻 Usage

### Basic Scan

```bash
python main.py scan logs.txt
```

Output saved to → `logs_cleaned.txt`

---

### Strict Mode

Also redacts high-entropy strings ≥ 40 chars (unknown token formats).

```bash
python main.py scan logs.txt --strict
```

---

### Preview Mode (Dry Run)

Prints only the redacted lines. No file is written.

```bash
python main.py scan logs.txt --preview
```

---

### Custom Regex Pattern

```bash
python main.py scan logs.txt --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

Multiple custom patterns:

```bash
python main.py scan logs.txt \
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" \
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}"
```

---

### Combine Flags

```bash
python main.py scan logs.txt --strict --preview \
  --custom-pattern "INTERNAL-TOKEN:[A-Z0-9]{16}"
```

---

## 🔍 What Gets Redacted

| Pattern         | Example Match                              |
|-----------------|--------------------------------------------|
| Email           | `user@example.com`                         |
| IPv4            | `192.168.1.100`                            |
| IPv6            | `2001:0db8:85a3::8a2e:0370:7334`           |
| API Key / Secret| `secret=aB3xK9...` (32–64 chars)          |
| AWS Access Key  | `AKIAIOSFODNN7EXAMPLE`                     |
| JWT Token       | `eyJhbGciOiJIUzI1NiJ9.eyJ...`             |
| Credit Card     | `4111111111111111`                         |
| Bearer Token    | `Bearer eyJhbGc...`                        |
| Password Field  | `password=SuperSecret!`                    |
| Custom Patterns | Whatever you define via `--custom-pattern` |

---

## 📂 Output

```
logs.txt          ← Original (NEVER modified)
logs_cleaned.txt  ← Clean version with [REDACTED] placeholders
```

---

## 🔒 Security Design

- ✅ Original file is read-only — never modified
- ✅ Output written to a separate file
- ✅ Chunked reading (64 KB) — safe for multi-GB logs
- ✅ No network calls — fully offline
- ✅ No external dependencies

---

## 📊 Sample Output

```
  🔍  Scanning  : logs.txt
  ⚡  Strict    : OFF
  👁   Preview   : OFF

──────────────────────────────────────────────────
  📊  KeyForge Scrub Report
──────────────────────────────────────────────────
  Lines scanned   : 10,450
  Lines modified  : 312
  Total redactions: 489
  Output file     : logs_cleaned.txt

  Pattern breakdown:
    EMAIL                   201 hit(s)
    IPV4                    145 hit(s)
    JWT                      89 hit(s)
    API_KEY                  43 hit(s)
    CREDIT_CARD              11 hit(s)
──────────────────────────────────────────────────

  ✅  Clean file saved → logs_cleaned.txt
```

---

## 🏷️ Branding

**KeyForge Log-Scrubber** — Privacy-first DevOps Tool  
Built with ❤️ by Sudhir Kumar ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))
