# 🧹 KeyForge Log-Scrubber

<div align="center">

```
 _  __          _____                     
| |/ /___ _   _|  ___|__  _ __ __ _  ___ 
| ' // _ \ | | | |_ / _ \| '__/ _` |/ _ \
| . \  __/ |_| |  _| (_) | | | (_| |  __/
|_|\_\___|\__, |_|  \___/|_|  \__, |\___|
          |___/  Log-Scrubber  |___/      
```

**Privacy-first DevOps Tool**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Mac-green?style=flat-square)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Author](https://img.shields.io/badge/Author-Sudhir%20Kumar-red?style=flat-square)](https://twitter.com/SudhirDevOps1)

> **Automatically detect and redact sensitive data from log files.**
> Original file is NEVER modified. Privacy guaranteed. 🔒

By **Sudhir Kumar** ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))

</div>

---

## 📑 Table of Contents

- [What is KeyForge Log-Scrubber?](#-what-is-keyforge-log-scrubber)
- [Why Use This Tool?](#-why-use-this-tool)
- [How It Works?](#-how-it-works)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage & Commands](#-usage--commands)
- [What Gets Redacted?](#-what-gets-redacted)
- [CLI Flags](#-cli-flags)
- [Real Examples](#-real-examples)
- [Sample Report Output](#-sample-report-output)
- [Windows Users Guide](#-windows-users-guide)
- [Common Mistakes & Fixes](#-common-mistakes--fixes)
- [Troubleshooting](#-troubleshooting)
- [Security Design](#-security-design)
- [Architecture](#-architecture)
- [Who Should Use This?](#-who-should-use-this)
- [Output Files](#-output-files)
- [Future Features](#-future-features-coming-soon)
- [License](#-license)
- [Contributing](#-contributing)
- [Contact & Support](#-contact--support)

---

## 🤔 What is KeyForge Log-Scrubber?

**KeyForge Log-Scrubber** is a powerful, privacy-first command-line tool
designed to automatically scan log files, detect sensitive information,
and replace it with `[REDACTED]` — keeping your data safe before sharing,
storing, or pushing logs anywhere.

```
✅ Scans log files automatically
✅ Detects sensitive data using smart regex patterns
✅ Replaces all sensitive data with [REDACTED]
✅ Saves a clean, safe copy of your log file
✅ NEVER modifies or touches the original file
✅ Works completely offline — no data ever leaves your machine
✅ Handles files of any size safely (chunked processing)
```

---

### 💡 Simple Before & After Example

```
BEFORE (logs.txt) — Dangerous ❌
────────────────────────────────────────────────────────────
2024-01-15 10:00:01  User login:    admin@company.com
2024-01-15 10:00:02  Client IP:     192.168.1.55
2024-01-15 10:00:03  Card charged:  4111111111111111
2024-01-15 10:00:04  password=SuperSecret123
2024-01-15 10:00:05  API secret=aB3xK9mNpQrStUvWxYz123456
2024-01-15 10:00:06  Token: Bearer eyJhbGciOiJIUzI1NiJ9...
2024-01-15 10:00:07  AWS Key: AKIAIOSFODNN7EXAMPLE
2024-01-15 10:00:08  Normal log entry — nothing sensitive here


AFTER (logs_cleaned.txt) — Safe ✅
────────────────────────────────────────────────────────────
2024-01-15 10:00:01  User login:    [REDACTED]
2024-01-15 10:00:02  Client IP:     [REDACTED]
2024-01-15 10:00:03  Card charged:  [REDACTED]
2024-01-15 10:00:04  [REDACTED]
2024-01-15 10:00:05  API secret=[REDACTED]
2024-01-15 10:00:06  Token: [REDACTED]
2024-01-15 10:00:07  AWS Key: [REDACTED]
2024-01-15 10:00:08  Normal log entry — nothing sensitive here
```

---

## 🎯 Why Use This Tool?

### The Real-World Problem

Every day, developers and DevOps engineers share log files for debugging,
auditing, or support — and accidentally expose sensitive information.

```
😱 Scenario 1 — Developer shares debug logs with team:
   ─────────────────────────────────────────────────────
   Log contained → customer emails, session tokens
   Result        → Data breach! GDPR violation!
                   Company fined thousands of dollars.

😱 Scenario 2 — DevOps pushes logs to GitHub accidentally:
   ─────────────────────────────────────────────────────
   Log contained → AWS API keys, database passwords
   Result        → Hacker scraped keys within minutes.
                   Cloud bill: $50,000 overnight!

😱 Scenario 3 — Support team receives raw payment logs:
   ─────────────────────────────────────────────────────
   Log contained → Credit card numbers, CVVs
   Result        → PCI-DSS violation!
                   Payment processor account suspended.

😱 Scenario 4 — Log file attached to Jira ticket:
   ─────────────────────────────────────────────────────
   Log contained → Internal IP addresses, JWT tokens
   Result        → Internal network exposed.
                   Active tokens hijacked.
```

### The KeyForge Solution

```
✅ Scrub logs BEFORE sharing with anyone
✅ Scrub logs BEFORE pushing to GitHub / GitLab
✅ Scrub logs BEFORE attaching to tickets
✅ Scrub logs BEFORE storing in S3 / cloud storage
✅ Stay compliant with GDPR, PCI-DSS, HIPAA, SOC2
✅ Build a culture of privacy-first DevOps
```

---

## ⚙️ How It Works?

KeyForge Log-Scrubber uses a **multi-layer regex scanning engine**
that processes your log file line by line, applying all detection
patterns simultaneously, then writes a clean version to a new file.

```
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   📄 logs.txt  (Your Original Log File)                  │
│   ──────────────────────────────────────                 │
│   Line 1: admin@company.com  ← Sensitive!               │
│   Line 2: 192.168.1.55       ← Sensitive!               │
│   Line 3: 4111111111111111   ← Sensitive!               │
│   Line 4: Normal log line    ← Safe                     │
│                                                          │
└─────────────────────┬────────────────────────────────────┘
                      │
                      │  Read in 64KB chunks
                      │  (memory safe for large files)
                      ▼
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   🔍 KeyForge Multi-Layer Scanner Engine                 │
│   ───────────────────────────────────────               │
│                                                          │
│   Layer 1 — Built-in Patterns:                          │
│   ┌─────────────────────────────────────────────┐       │
│   │  Pattern 1:  EMAIL          → Regex scan    │       │
│   │  Pattern 2:  IPv4 Address   → Regex scan    │       │
│   │  Pattern 3:  IPv6 Address   → Regex scan    │       │
│   │  Pattern 4:  API Key/Secret → Regex scan    │       │
│   │  Pattern 5:  AWS Access Key → Regex scan    │       │
│   │  Pattern 6:  JWT Token      → Regex scan    │       │
│   │  Pattern 7:  Credit Card    → Regex scan    │       │
│   │  Pattern 8:  Bearer Token   → Regex scan    │       │
│   │  Pattern 9:  Password Field → Regex scan    │       │
│   └─────────────────────────────────────────────┘       │
│                                                          │
│   Layer 2 — Custom Patterns (--custom-pattern):         │
│   ┌─────────────────────────────────────────────┐       │
│   │  Custom 1:   Your own regex  → Regex scan   │       │
│   │  Custom 2:   Your own regex  → Regex scan   │       │
│   │  Custom N:   Your own regex  → Regex scan   │       │
│   └─────────────────────────────────────────────┘       │
│                                                          │
│   Layer 3 — Strict Mode (--strict):                     │
│   ┌─────────────────────────────────────────────┐       │
│   │  High-entropy strings ≥ 40 chars → Redact   │       │
│   │  Catches unknown / future token formats     │       │
│   └─────────────────────────────────────────────┘       │
│                                                          │
└─────────────────────┬────────────────────────────────────┘
                      │
                      │  Replace matches with [REDACTED]
                      │  Count hits per pattern
                      ▼
┌──────────────────────────────────────────────────────────┐
│                                                          │
│   🔄 Redaction Engine                                    │
│   ──────────────────                                     │
│                                                          │
│   Sensitive match found  →  Replace with [REDACTED]     │
│   Non-sensitive content  →  Keep exactly as-is          │
│   Track stats per line   →  Build report data           │
│                                                          │
└──────────┬────────────────────────────┬─────────────────┘
           │                            │
           ▼                            ▼
┌──────────────────┐        ┌───────────────────────┐
│                  │        │                       │
│   logs.txt       │        │   logs_cleaned.txt    │
│   (ORIGINAL)     │        │   (SAFE CLEAN COPY)   │
│                  │        │                       │
│   Untouched 🔒   │        │   [REDACTED] ✅        │
│   Never modified │        │   Ready to share      │
│                  │        │                       │
└──────────────────┘        └───────────────────────┘
```

---

## 📁 Project Structure

```
keyforge-log-scrubber/
│
├── main.py         →  CLI entry point — commands, flags, banner, stats
├── patterns.py     →  All regex detection rules (built-in + custom loader)
├── utils.py        →  Core scrubbing engine — file I/O, line processing
├── README.md       →  Full documentation (this file)
└── LICENSE         →  MIT License
```

### Detailed File Roles

```
┌──────────────┬───────────────────────────────────────────────────────────┐
│ File         │ Responsibility                                            │
├──────────────┼───────────────────────────────────────────────────────────┤
│              │ • Parses all CLI arguments using argparse                 │
│ main.py      │ • Displays the ASCII banner                               │
│              │ • Calls scan_and_scrub() from utils.py                    │
│              │ • Displays final stats report                             │
│              │ • Handles --strict, --preview, --custom-pattern flags     │
├──────────────┼───────────────────────────────────────────────────────────┤
│              │ • Defines all built-in regex patterns                     │
│ patterns.py  │ • EMAIL, IPV4, IPV6, API_KEY, AWS_KEY, JWT               │
│              │ • CREDIT_CARD, BEARER_TOKEN, PASSWORD_FIELD              │
│              │ • Loads and validates user-supplied custom patterns       │
│              │ • Returns combined pattern dictionary                     │
├──────────────┼───────────────────────────────────────────────────────────┤
│              │ • Reads input file in 64KB chunks (memory safe)           │
│ utils.py     │ • Applies all patterns to each line                       │
│              │ • Handles group-based redaction (key=value → key=[REDACTED])│
│              │ • Writes clean output file                                │
│              │ • Collects and returns statistics                         │
└──────────────┴───────────────────────────────────────────────────────────┘
```

---

## 📦 Requirements

```
✅ Python 3.10 or higher
✅ No external pip packages required
✅ Uses Python standard library only
✅ Works on Windows, Linux, and macOS
✅ No internet connection needed
✅ No configuration files needed to get started
```

### Verify Your Python Version

```cmd
python --version
```

Expected output:

```
Python 3.12.10  ✅
```

If Python is not installed:

```
1. Visit → https://www.python.org/downloads/
2. Download Python 3.10 or higher
3. During installation:
   ☑️ Check "Add Python to PATH"  ← CRITICAL STEP!
4. Restart your terminal
5. Run: python --version
```

---

## 🔧 Installation

### Windows

```cmd
:: Option 1 — Download ZIP from GitHub
:: Go to: https://github.com/SudhirDevOps1/keyforge-log-scrubber
:: Click "Code" → "Download ZIP"
:: Extract the ZIP file to your desired location

:: Option 2 — Git Clone
git clone https://github.com/SudhirDevOps1/keyforge-log-scrubber.git

:: Navigate to the project folder
:: First switch to the correct drive (if not on C:)
E:

:: Then go into the folder
cd keyforge-log-scrubber

:: Verify all files are present
dir
```

Expected output of `dir`:

```
Directory of E:\keyforge-log-scrubber

17-03-2026  12:43    <DIR>   .
17-03-2026  12:43    <DIR>   ..
17-03-2026  12:43         LICENSE
17-03-2026  12:55         main.py       ✅
17-03-2026  12:43         patterns.py   ✅
17-03-2026  12:43         README.md     ✅
17-03-2026  12:43         utils.py      ✅
```

### Linux / macOS

```bash
# Clone the repository
git clone https://github.com/SudhirDevOps1/keyforge-log-scrubber.git

# Navigate into the project folder
cd keyforge-log-scrubber

# Make main.py executable (optional)
chmod +x main.py

# Verify all files are present
ls -la
```

---

## ⚡ Quick Start

### Windows (CMD) — Step by Step

```cmd
:: ── Step 1: Open CMD ──────────────────────────────────────────
:: Press Win + R → type "cmd" → press Enter

:: ── Step 2: Verify Python is installed ───────────────────────
python --version
:: Expected: Python 3.12.10

:: ── Step 3: Switch to correct drive ──────────────────────────
E:
:: (Replace E: with whatever drive your project is on)

:: ── Step 4: Navigate to project folder ───────────────────────
cd keyforge-log-scrubber

:: ── Step 5: Verify files are present ─────────────────────────
dir
:: You should see: main.py, patterns.py, utils.py, README.md

:: ── Step 6: Create a test log file ───────────────────────────
echo 2024-01-15 User login: admin@company.com from 192.168.1.55 > logs.txt
echo 2024-01-15 Card Number: 4111111111111111 >> logs.txt
echo 2024-01-15 password=SuperSecret123 >> logs.txt
echo 2024-01-15 secret=aB3xK9mNpQrStUvWxYz1234567890abcd >> logs.txt
echo 2024-01-15 AWS Key: AKIAIOSFODNN7EXAMPLE >> logs.txt
echo 2024-01-15 Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.abc >> logs.txt
echo 2024-01-15 Normal log line — nothing sensitive here >> logs.txt

:: ── Step 7: Run the scrubber ──────────────────────────────────
python main.py scan logs.txt

:: ── Step 8: View the cleaned output file ─────────────────────
type logs_cleaned.txt
```

### Linux / macOS (Terminal) — Step by Step

```bash
# Step 1: Navigate to project folder
cd keyforge-log-scrubber

# Step 2: Create a test log file
cat > logs.txt << 'EOF'
2024-01-15 User login: admin@company.com from 192.168.1.55
2024-01-15 Card Number: 4111111111111111
2024-01-15 password=SuperSecret123
2024-01-15 secret=aB3xK9mNpQrStUvWxYz1234567890abcd
2024-01-15 AWS Key: AKIAIOSFODNN7EXAMPLE
2024-01-15 Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.abc
2024-01-15 Normal log line — nothing sensitive here
EOF

# Step 3: Run the scrubber
python main.py scan logs.txt

# Step 4: View the cleaned output
cat logs_cleaned.txt
```

---

## 💻 Usage & Commands

### Basic Syntax

```
python main.py scan <FILE> [OPTIONS]
```

---

### 1️⃣ Basic Scan

```cmd
python main.py scan logs.txt
```

```
What it does:
─────────────────────────────────────────────────────────
→ Reads logs.txt line by line
→ Applies all 9 built-in detection patterns
→ Replaces all sensitive data with [REDACTED]
→ Saves the clean result to logs_cleaned.txt
→ Prints a full statistics report
→ Original logs.txt is never touched or modified
```

---

### 2️⃣ Preview Mode (Dry Run)

```cmd
python main.py scan logs.txt --preview
```

```
What it does:
─────────────────────────────────────────────────────────
→ Scans the file exactly like a normal scan
→ Prints ONLY the affected (redacted) lines to screen
→ Does NOT save any output file
→ Perfect for: testing, reviewing before committing
→ Use this first to see what will be redacted
```

---

### 3️⃣ Strict Mode

```cmd
python main.py scan logs.txt --strict
```

```
What it does:
─────────────────────────────────────────────────────────
→ Runs all 9 built-in pattern checks
→ ADDITIONALLY scans for any string ≥ 40 characters
  that looks high-entropy (random / encoded)
→ Catches unknown token formats, custom secrets,
  future API key formats not yet in patterns
→ Recommended for: security audits, production logs
→ May occasionally redact long non-sensitive strings
```

---

### 4️⃣ Custom Pattern

```cmd
python main.py scan logs.txt --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

```
What it does:
─────────────────────────────────────────────────────────
→ Adds your own regex pattern to the detection engine
→ Runs alongside all built-in patterns
→ Useful for: company-specific IDs, internal tokens,
  healthcare data, government IDs, etc.
→ The regex follows Python re module syntax
```

---

### 5️⃣ Multiple Custom Patterns

```cmd
:: Windows CMD (use ^ for line continuation)
python main.py scan logs.txt ^
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" ^
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}" ^
  --custom-pattern "PAN:[A-Z]{5}\d{4}[A-Z]" ^
  --custom-pattern "AADHAAR:\d{4}\s\d{4}\s\d{4}"
```

```bash
# Linux / macOS (use \ for line continuation)
python main.py scan logs.txt \
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" \
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}" \
  --custom-pattern "PAN:[A-Z]{5}\d{4}[A-Z]" \
  --custom-pattern "AADHAAR:\d{4}\s\d{4}\s\d{4}"
```

---

### 6️⃣ Combine All Flags

```cmd
python main.py scan logs.txt --strict --preview --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

```
What it does:
─────────────────────────────────────────────────────────
→ Strict mode ON (catches high-entropy strings too)
→ Preview mode ON (no file saved, just shows output)
→ Custom pattern active alongside built-ins
→ Best for: full audit dry-run before cleanup
```

---

## 🔍 What Gets Redacted?

### Built-in Detection Patterns

```
┌──────────────────────┬──────────────────────────────────────────┬──────────────────────┐
│ Pattern Name         │ Example — Before                         │ After                │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ EMAIL                │ admin@company.com                        │ [REDACTED]           │
│                      │ user.name+tag@sub.domain.co.uk           │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ IPv4 ADDRESS         │ 192.168.1.100                            │ [REDACTED]           │
│                      │ 10.0.0.1                                 │ [REDACTED]           │
│                      │ 255.255.255.0                            │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ IPv6 ADDRESS         │ 2001:0db8:85a3::8a2e:0370:7334           │ [REDACTED]           │
│                      │ fe80::1                                  │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ API KEY / SECRET     │ secret=aB3xK9mNpQrStUvWxYz123456        │ secret=[REDACTED]    │
│                      │ api_key="xK9mNpQrStUvWxYz12345678"      │ api_key="[REDACTED]" │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ AWS ACCESS KEY       │ AKIAIOSFODNN7EXAMPLE                     │ [REDACTED]           │
│                      │ AKIAI44QH8DHBEXAMPLE                     │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ JWT TOKEN            │ eyJhbGciOiJIUzI1NiJ9.eyJzdWIi.SflKxw   │ [REDACTED]           │
│                      │ (header.payload.signature format)        │                      │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ CREDIT CARD          │ 4111111111111111   (Visa)                │ [REDACTED]           │
│                      │ 5500005555555559   (MasterCard)          │ [REDACTED]           │
│                      │ 371449635398431    (Amex)                │ [REDACTED]           │
│                      │ 6011111111111117   (Discover)            │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ BEARER TOKEN         │ Bearer eyJhbGciOiJIUzI1NiJ9...          │ [REDACTED]           │
│                      │ Authorization: Bearer abc123xyz...       │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ PASSWORD FIELD       │ password=SuperSecret123                  │ [REDACTED]           │
│                      │ passwd=MyP@ssw0rd                        │ [REDACTED]           │
│                      │ pwd=hunter2                              │ [REDACTED]           │
├──────────────────────┼──────────────────────────────────────────┼──────────────────────┤
│ CUSTOM PATTERNS      │ SSN:123-45-6789    (your rule)           │ [REDACTED]           │
│                      │ EMP-ID:AB123456    (your rule)           │ [REDACTED]           │
└──────────────────────┴──────────────────────────────────────────┴──────────────────────┘
```

### Credit Card Networks Supported

```
┌─────────────────────┬────────────────────────────┬──────────────────────────┐
│ Network             │ Pattern                    │ Example                  │
├─────────────────────┼────────────────────────────┼──────────────────────────┤
│ Visa                │ 4xxx xxxx xxxx xxxx        │ 4111 1111 1111 1111      │
│ MasterCard          │ 5x xx xxxx xxxx xxxx       │ 5500 0055 5555 5559      │
│ American Express    │ 3x xx xxxx xxxx xxx        │ 3714 496353 98431        │
│ Discover            │ 6011 xxxx xxxx xxxx        │ 6011 1111 1111 1117      │
└─────────────────────┴────────────────────────────┴──────────────────────────┘
```

---

## 🚩 CLI Flags Reference

```
┌──────────────────────────┬──────────┬───────────┬──────────────────────────────────────────────┐
│ Flag                     │ Type     │ Default   │ Description                                  │
├──────────────────────────┼──────────┼───────────┼──────────────────────────────────────────────┤
│ scan <file>              │ Required │ —         │ Path to the log file to scan                 │
│                          │          │           │ Example: scan logs.txt                       │
├──────────────────────────┼──────────┼───────────┼──────────────────────────────────────────────┤
│ --strict                 │ Optional │ OFF       │ Enable strict mode                           │
│                          │          │           │ Also redacts high-entropy strings ≥ 40 chars │
│                          │          │           │ Catches unknown/future token formats          │
├──────────────────────────┼──────────┼───────────┼──────────────────────────────────────────────┤
│ --preview                │ Optional │ OFF       │ Dry-run mode                                 │
│                          │          │           │ Prints affected lines to screen only         │
│                          │          │           │ No output file is written                    │
├──────────────────────────┼──────────┼───────────┼──────────────────────────────────────────────┤
│ --custom-pattern <REGEX> │ Optional │ None      │ Add a custom regex detection pattern         │
│                          │          │           │ Can be used multiple times                   │
│                          │          │           │ Follows Python re module syntax              │
└──────────────────────────┴──────────┴───────────┴──────────────────────────────────────────────┘
```

---

## 🎯 Real Examples

### Example 1 — Apache / Nginx Web Server Log

```
Input:
192.168.1.1 - admin@site.com [15/Jan/2024:10:00:01] "GET /api?key=abc123xyz789def456ghi012jkl345mn HTTP/1.1" 200

Output:
[REDACTED] - [REDACTED] [15/Jan/2024:10:00:01] "GET /api?key=[REDACTED] HTTP/1.1" 200
```

---

### Example 2 — Application / Backend Log

```
Input:
2024-01-15 ERROR  Database connection failed. User: john@example.com password=MyPass123 host=10.0.0.5

Output:
2024-01-15 ERROR  Database connection failed. User: [REDACTED] [REDACTED] host=[REDACTED]
```

---

### Example 3 — AWS CloudWatch / IAM Log

```
Input:
AccessKeyId: AKIAIOSFODNN7EXAMPLE SecretAccessKey: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY Region: us-east-1

Output:
AccessKeyId: [REDACTED] SecretAccessKey: [REDACTED] Region: us-east-1
```

---

### Example 4 — Payment / E-commerce Log

```
Input:
2024-01-15 INFO  Payment processed. Card: 4111-1111-1111-1111 Amount: $500.00 Customer: billing@store.com

Output:
2024-01-15 INFO  Payment processed. Card: [REDACTED] Amount: $500.00 Customer: [REDACTED]
```

---

### Example 5 — Authentication / OAuth Log

```
Input:
2024-01-15 DEBUG  Auth header received: Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Output:
2024-01-15 DEBUG  Auth header received: [REDACTED]
```

---

### Example 6 — Custom Pattern (Indian PAN Card)

```cmd
python main.py scan logs.txt --custom-pattern "PAN:[A-Z]{5}\d{4}[A-Z]"
```

```
Input:
2024-01-15 KYC verified for PAN:ABCDE1234F customer: user@bank.com

Output:
2024-01-15 KYC verified for [REDACTED] customer: [REDACTED]
```

---

### Example 7 — Full Strict Mode (Unknown Tokens)

```cmd
python main.py scan logs.txt --strict
```

```
Input:
2024-01-15 Internal-Token: xK9mNpQrStUvWxYz1234567890abcdef0987654321ABCDEF

Output:
2024-01-15 Internal-Token: [REDACTED]
(Caught by strict mode — 48 char high-entropy string)
```

---

## 📊 Sample Report Output

```
 _  __          _____
| |/ /___ _   _|  ___|__  _ __ __ _  ___
| ' // _ \ | | | |_ / _ \| '__/ _` |/ _ \
| . \  __/ |_| |  _| (_) | | | (_| |  __/
|_|\_\___|\__, |_|  \___/|_|  \__, |\___|
          |___/  Log-Scrubber  |___/

  Privacy-first DevOps Tool
  By Sudhir Kumar (@SudhirDevOps1)

  🔍  Scanning  : logs.txt
  ⚡  Strict    : OFF
  👁   Preview   : OFF

──────────────────────────────────────────────────
  📊  KeyForge Scrub Report
──────────────────────────────────────────────────
  Lines scanned   : 10,450
  Lines modified  :    312
  Total redactions:    489
  Output file     : logs_cleaned.txt

  Pattern breakdown:
    EMAIL                  201 hit(s)
    IPV4                   145 hit(s)
    JWT                     89 hit(s)
    API_KEY                 43 hit(s)
    CREDIT_CARD             11 hit(s)
──────────────────────────────────────────────────

  ✅  Clean file saved → logs_cleaned.txt
```

---

## 🖥️ Windows Users Guide

### How to Open CMD

```
Method 1 → Press Win + R → type "cmd" → press Enter
Method 2 → Click Start Menu → search "Command Prompt" → Enter
Method 3 → Press Win + X → select "Command Prompt" or "Terminal"
Method 4 → In File Explorer address bar → type "cmd" → Enter
```

### ⚠️ CRITICAL — How to Switch Drives in Windows CMD

This is the most common mistake Windows users make.
`cd` alone does NOT switch drives in CMD.

```cmd
── Correct way to navigate to another drive ──────────────

Step 1: Type the drive letter and press Enter
E:

Step 2: Then use cd to go into the folder
cd keyforge-log-scrubber

── You should now see this prompt ────────────────────────
E:\keyforge-log-scrubber>

── Full example for different drives ─────────────────────
If project is on D: drive:
  D:
  cd keyforge-log-scrubber

If project is on C: drive:
  cd C:\Users\YourName\keyforge-log-scrubber
```

### Useful CMD Navigation Commands

```cmd
:: See where you currently are
cd

:: See all files in current folder
dir

:: Go up one folder level
cd ..

:: Go to a specific folder
cd FolderName

:: Clear the screen
cls

:: Check Python version
python --version

:: Check if a file exists
dir logs.txt
```

---

## ❌ Common Mistakes & Fixes

### Mistake 1 — Running from PowerShell Instead of CMD

```powershell
# ❌ WRONG — PowerShell does not support Linux shebang lines
PS C:\Users\DELL> /usr/bin/env python3 main.py
# Error: '/usr/bin/env' is not recognized as a name of a cmdlet...
```

```cmd
# ✅ CORRECT — Always use CMD on Windows
C:\> python main.py scan logs.txt
```

**Why:** The `#!/usr/bin/env python3` line at the top of `main.py` is a
Linux/macOS "shebang" line. Windows CMD ignores it safely.
PowerShell tries to execute it and fails.

---

### Mistake 2 — Forgetting to Switch Drive Before cd

```cmd
# ❌ WRONG — cd with a different drive letter does NOT switch drives
C:\Users\DELL> cd E:\keyforge-log-scrubber
C:\Users\DELL>                              ← Still on C: drive!

# ❌ WRONG — Running tool from wrong location
C:\Users\DELL> python main.py scan logs.txt
# Error: can't open file 'C:\Users\DELL\main.py': No such file or directory
```

```cmd
# ✅ CORRECT — Switch drive first, then cd
C:\Users\DELL> E:
E:\> cd keyforge-log-scrubber
E:\keyforge-log-scrubber> python main.py scan logs.txt  ✅
```

---

### Mistake 3 — Running Tool Without Creating logs.txt First

```cmd
# ❌ WRONG — No log file exists yet
E:\keyforge-log-scrubber> python main.py scan logs.txt
# [ERROR] File not found: logs.txt
```

```cmd
# ✅ CORRECT — Create the file first, then scan
E:\keyforge-log-scrubber> echo 2024-01-15 admin@test.com > logs.txt
E:\keyforge-log-scrubber> python main.py scan logs.txt  ✅
```

---

### Mistake 4 — Using python3 Instead of python on Windows

```cmd
# ❌ WRONG — python3 is a Linux/macOS command
C:\> python3 main.py scan logs.txt
# Error: 'python3' is not recognized as an internal or external command
```

```cmd
# ✅ CORRECT — Windows uses "python" not "python3"
C:\> python main.py scan logs.txt  ✅
```

---

### Mistake 5 — Python Not Added to PATH During Install

```cmd
# ❌ WRONG — Python installed but not in PATH
C:\> python --version
# 'python' is not recognized as an internal or external command
```

```
# ✅ CORRECT FIX:
1. Go to: https://www.python.org/downloads/
2. Download the latest Python installer
3. Run the installer
4. On the FIRST screen:
   ───────────────────────────────────────
   ☑️  Add Python to PATH   ← TICK THIS!
   ───────────────────────────────────────
5. Click "Install Now"
6. Close ALL CMD windows
7. Open a fresh CMD window
8. Run: python --version
```

---

### Mistake 6 — Using Relative Path When Not in Project Folder

```cmd
# ❌ WRONG — Trying to use path without being in the folder
C:\Users\DELL> python E:\keyforge-log-scrubber\main.py scan logs.txt
# Error: [ERROR] File not found: logs.txt
# (logs.txt is being looked for in C:\Users\DELL, not the project folder)
```

```cmd
# ✅ CORRECT — Navigate INTO the folder first
C:\Users\DELL> E:
E:\> cd keyforge-log-scrubber
E:\keyforge-log-scrubber> python main.py scan logs.txt  ✅
```

---

## 🔧 Troubleshooting

```
┌─────────────────────────────────────────┬────────────────────────────────────────────────┐
│ Error Message                           │ Solution                                       │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ 'python' is not recognized              │ Install Python from python.org/downloads       │
│                                         │ During install: check "Add Python to PATH" ✅  │
│                                         │ Restart CMD after installing                   │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ 'python3' is not recognized             │ On Windows, use "python" not "python3"         │
│                                         │ python main.py scan logs.txt                   │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ can't open file 'C:\Users\...\main.py'  │ You are in the wrong folder                    │
│                                         │ Switch drive: E:                               │
│                                         │ Navigate: cd keyforge-log-scrubber             │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ [ERROR] File not found: logs.txt        │ The log file does not exist yet                │
│                                         │ Create it: echo test log > logs.txt            │
│                                         │ Or point to your real log file path            │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ '/usr/bin/env' is not recognized        │ Do not use PowerShell on Windows               │
│                                         │ Use CMD (Command Prompt) instead               │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ The system cannot find the path         │ You forgot to switch drives                    │
│                                         │ Type: E: (then press Enter)                    │
│                                         │ Then: cd keyforge-log-scrubber                 │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ Permission denied                       │ Run CMD as Administrator                       │
│                                         │ Right-click CMD → "Run as administrator"       │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ SyntaxError / IndentationError          │ Python version too old                         │
│                                         │ Upgrade to Python 3.10+                        │
│                                         │ Check: python --version                        │
├─────────────────────────────────────────┼────────────────────────────────────────────────┤
│ Invalid regex for custom pattern        │ Your --custom-pattern regex has a syntax error │
│                                         │ Test your regex at: regex101.com               │
└─────────────────────────────────────────┴────────────────────────────────────────────────┘
```

---

## 🔒 Security Design

```
┌───────────────────────────────────────────────────────────────┐
│                    Security Principles                        │
├───────────────────────────────────────────────────────────────┤
│                                                               │
│  🔒 Original File is READ-ONLY                                │
│     The input file is opened in read mode only.              │
│     It is NEVER opened for writing.                          │
│     Even a crash cannot corrupt your original file.          │
│                                                               │
│  📄 Separate Output File                                      │
│     Clean output is always written to a NEW file.            │
│     Naming: logs.txt → logs_cleaned.txt                      │
│     Your original stays safe no matter what.                 │
│                                                               │
│  🧠 Memory-Safe Chunked Processing                            │
│     Files are read in 64KB chunks, not loaded fully.         │
│     Handles log files of any size safely.                    │
│     Will not crash or slow down on multi-GB files.           │
│                                                               │
│  🌐 Fully Offline — Zero Network Calls                        │
│     This tool never connects to the internet.                │
│     Your sensitive log data never leaves your machine.       │
│     No telemetry, no analytics, no callbacks.                │
│                                                               │
│  📦 Zero External Dependencies                                │
│     Only Python's built-in standard library is used.        │
│     No pip packages to install. No supply-chain risk.        │
│     Nothing can be injected via a third-party package.       │
│                                                               │
│  🙈 No Secret Storage                                         │
│     The tool does not store, log, or cache any              │
│     sensitive data it finds. It only counts hits.            │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         main.py                              │
│                     (CLI Entry Point)                        │
│                                                              │
│  • argparse — parses scan, --strict, --preview,             │
│               --custom-pattern flags                         │
│  • Displays ASCII banner                                     │
│  • Calls scan_and_scrub() with parsed arguments             │
│  • Calls print_stats() with returned stats dict             │
└─────────────────────────┬────────────────────────────────────┘
                          │  calls scan_and_scrub()
                          ▼
┌──────────────────────────────────────────────────────────────┐
│                         utils.py                             │
│                    (Core Scrub Engine)                       │
│                                                              │
│  scan_and_scrub()                                            │
│    → Orchestrates the full scan workflow                     │
│    → Calls _iter_lines_chunked() for safe file reading       │
│    → Calls _scrub_line() for each line                       │
│    → Writes output to logs_cleaned.txt                       │
│    → Returns statistics dictionary                           │
│                                                              │
│  _iter_lines_chunked()                                       │
│    → Reads file in 64KB chunks                               │
│    → Yields complete lines one at a time                     │
│    → Safe for very large files (GB+)                         │
│                                                              │
│  _scrub_line()                                               │
│    → Applies all patterns to a single line                   │
│    → Handles group-based redaction (key=[REDACTED])         │
│    → Applies strict mode high-entropy sweep                  │
│    → Returns (scrubbed_line, list_of_hit_pattern_names)     │
│                                                              │
│  print_stats()                                               │
│    → Pretty-prints the final scan report                     │
│                                                              │
└──────────┬────────────────────────────┬─────────────────────┘
           │  get_all_patterns()        │  reads / writes
           ▼                            ▼
┌──────────────────────┐  ┌─────────────────────────────────────┐
│     patterns.py      │  │             Files                   │
│    (Regex Library)   │  │                                     │
│                      │  │  logs.txt          (input)  🔒      │
│  BUILT_IN_PATTERNS:  │  │  ↑ read-only, never modified        │
│  ├─ EMAIL            │  │                                     │
│  ├─ IPV4             │  │  logs_cleaned.txt  (output) ✅      │
│  ├─ IPV6             │  │  ↑ new file, safe to share          │
│  ├─ API_KEY          │  │                                     │
│  ├─ AWS_KEY          │  └─────────────────────────────────────┘
│  ├─ JWT              │
│  ├─ CREDIT_CARD      │
│  ├─ BEARER_TOKEN     │
│  ├─ PASSWORD_FIELD   │
│  └─ CUSTOM_1..N      │
│                      │
│  get_all_patterns()  │
│  → merges built-in   │
│    + custom patterns │
│  → validates custom  │
│    regex syntax      │
└──────────────────────┘
```

---

## 👥 Who Should Use This?

```
┌──────────────────────────┬──────────────────────────────────────────────────┐
│ Role                     │ Use Case                                         │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 👨‍💻 Software Developers   │ Scrub debug/error logs before sharing with team  │
│                          │ Clean logs before attaching to GitHub issues     │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 🔐 Security Engineers    │ Audit production logs for data exposure          │
│                          │ Verify no secrets are leaking into log outputs   │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 🏢 DevOps / SRE Teams    │ Anonymize logs before storing in cloud           │
│                          │ Clean logs before shipping to log aggregators    │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 📋 Compliance Teams      │ Ensure GDPR compliance — no PII in logs          │
│                          │ PCI-DSS — no card data in payment logs           │
│                          │ HIPAA — no patient data in healthcare logs       │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 🧪 QA / Test Engineers   │ Sanitize test environment logs                   │
│                          │ Share test logs without exposing test credentials│
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 📊 Data / ML Engineers   │ Anonymize log datasets before ML training        │
│                          │ Remove PII before data analysis pipelines        │
├──────────────────────────┼──────────────────────────────────────────────────┤
│ 🎓 Students / Learners   │ Practice safe log handling habits early          │
│                          │ Learn regex-based data detection patterns        │
└──────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 📄 Output Files

```
Input  → logs.txt            (Original — NEVER modified) 🔒
Output → logs_cleaned.txt    (Safe, clean, shareable)    ✅

File Naming Convention:
────────────────────────────────────────────
  logs.txt          →  logs_cleaned.txt
  app_logs.txt      →  app_logs_cleaned.txt
  server.log        →  server_cleaned.log
  access.log        →  access_cleaned.log
  2024-01-15.log    →  2024-01-15_cleaned.log
────────────────────────────────────────────

Location:
  Output file is always saved in the SAME folder
  as the input file — easy to find.
```

---

## 🌟 Future Features (Coming Soon)

```
🔜 Scan multiple files at once
   python main.py scan *.log

🔜 Scan entire folders recursively
   python main.py scan /var/logs/ --recursive

🔜 JSON / structured log support
   Proper key-value aware redaction

🔜 HTML scan report
   Beautiful visual report with highlighted findings

🔜 YAML config file support
   .keyforge.yaml — define all rules in one place

🔜 Git pre-commit hook integration
   Auto-scan before every git commit

🔜 Audit mode
   Only report findings — do not redact

🔜 Multiple output formats
   logs_cleaned.json, logs_cleaned.csv
```

---

## 📜 License

```
MIT License
Copyright (c) 2026 Sudhir Kumar (@SudhirDevOps1)

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
```

---

## 🤝 Contributing

```
We welcome contributions of all kinds!

1. Fork the repository on GitHub

2. Create your feature branch
   git checkout -b feature/your-feature-name

3. Make your changes and commit
   git commit -m "feat: add your feature description"

4. Push to your fork
   git push origin feature/your-feature-name

5. Open a Pull Request on GitHub
   → Describe what you changed and why
   → Reference any related issues

Ideas for contributions:
  ✅ New detection patterns (phone numbers, SSN, etc.)
  ✅ Support for more log formats
  ✅ Performance improvements
  ✅ New CLI features
  ✅ Tests and documentation
```

---

## 📞 Contact & Support

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   👤  Author   :  Sudhir Kumar                          │
│   🐦  Twitter  :  @SudhirDevOps1                        │
│   💼  GitHub   :  github.com/SudhirDevOps1              │
│                                                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   🐛  Found a bug?                                      │
│       Open an issue on GitHub Issues                    │
│       Include: OS, Python version, error message        │
│                                                         │
│   💡  Have a feature idea?                              │
│       Start a discussion in GitHub Discussions          │
│                                                         │
│   ⭐  Found it useful?                                   │
│       Star the repo — it helps others discover it!      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

<div align="center">

**Built with ❤️ by Sudhir Kumar ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))**

*Privacy-first DevOps Tool — Protecting your logs, one file at a time.*

---

⭐ **If KeyForge Log-Scrubber helped you, please star the repository!** ⭐

</div>
