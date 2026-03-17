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
- [Windows Guide](#-windows-users-guide)
- [Common Mistakes](#-common-mistakes--fixes)
- [Troubleshooting](#-troubleshooting)
- [Security Design](#-security-design)
- [Architecture](#-architecture)

---

## 🤔 What is KeyForge Log-Scrubber?

**KeyForge Log-Scrubber** ek powerful CLI tool hai jo:

```
✅ Log files scan karta hai
✅ Sensitive data automatically dhundhta hai
✅ Use [REDACTED] se replace karta hai
✅ Clean safe file save karta hai
✅ Original file kabhi touch nahi karta
```

### Simple Example:

```
BEFORE (logs.txt) — Dangerous ❌
─────────────────────────────────────────────────
2024-01-15 User login: admin@company.com
2024-01-15 IP Address: 192.168.1.55
2024-01-15 Card Number: 4111111111111111
2024-01-15 password=SuperSecret123
2024-01-15 API: secret=aB3xK9mNpQrStUvWxYz123456
2024-01-15 Token: Bearer eyJhbGciOiJIUzI1NiJ9...


AFTER (logs_cleaned.txt) — Safe ✅
─────────────────────────────────────────────────
2024-01-15 User login: [REDACTED]
2024-01-15 IP Address: [REDACTED]
2024-01-15 Card Number: [REDACTED]
2024-01-15 [REDACTED]
2024-01-15 API: secret=[REDACTED]
2024-01-15 Token: [REDACTED]
```

---

## 🎯 Why Use This Tool?

### Real Life Problem:

```
😱 Scenario 1:
   Developer ne production logs share kiye
   Us log me customer emails the
   → Data breach! Legal problem!

😱 Scenario 2:
   DevOps engineer ne logs GitHub pe push kiye
   Us log me API keys the
   → Hacker ne keys use karke server hack kiya!

😱 Scenario 3:
   Support team ko logs bheje debugging ke liye
   Us log me credit card numbers the
   → PCI-DSS violation! Huge fine!
```

### KeyForge Solution:

```
✅ Logs share karne se PEHLE scrub karo
✅ Koi sensitive data leak nahi hoga
✅ Team ke saath safely share karo
✅ GitHub pe safely push karo
✅ Compliance maintain karo (GDPR, PCI-DSS)
```

---

## ⚙️ How It Works?

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   logs.txt (Original File)                         │
│   ───────────────────────                          │
│   admin@company.com  ← Email detected!             │
│   192.168.1.55       ← IP detected!                │
│   4111111111111111   ← Credit card detected!       │
│                                                     │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│                                                     │
│   🔍 KeyForge Scanner Engine                        │
│   ──────────────────────────                        │
│   Pattern 1: Email Regex      → ✅ Found & Flag     │
│   Pattern 2: IP Regex         → ✅ Found & Flag     │
│   Pattern 3: Credit Card      → ✅ Found & Flag     │
│   Pattern 4: API Key          → ✅ Found & Flag     │
│   Pattern 5: JWT Token        → ✅ Found & Flag     │
│   Pattern 6: Password Field   → ✅ Found & Flag     │
│   Pattern 7: AWS Key          → ✅ Found & Flag     │
│   Pattern 8: Bearer Token     → ✅ Found & Flag     │
│   Custom  9: Your Pattern     → ✅ Found & Flag     │
│                                                     │
└──────────────────┬──────────────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────────────┐
│                                                     │
│   🔄 Redaction Engine                               │
│   ───────────────────                               │
│   Sensitive data → [REDACTED]                       │
│   Non-sensitive  → Unchanged                        │
│   64KB chunks    → RAM safe for large files         │
│                                                     │
└──────────────────┬──────────────────────────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
┌──────────────┐   ┌──────────────────┐
│  logs.txt    │   │ logs_cleaned.txt │
│  (original)  │   │ (safe & clean)   │
│  UNCHANGED🔒 │   │  [REDACTED] ✅   │
└──────────────┘   └──────────────────┘
```

---

## 📁 Project Structure

```
keyforge-log-scrubber/
│
├── main.py         → CLI entry point, commands & flags
├── patterns.py     → All regex detection rules
├── utils.py        → Core scrubbing engine & file handling
├── README.md       → Documentation (ye file!)
└── LICENSE         → MIT License
```

### File Roles:

```
┌─────────────┬────────────────────────────────────────┐
│ File        │ Kya Karta Hai                          │
├─────────────┼────────────────────────────────────────┤
│ main.py     │ CLI commands handle karta hai          │
│             │ --strict, --preview, --custom-pattern  │
├─────────────┼────────────────────────────────────────┤
│ patterns.py │ Saare regex patterns define hain       │
│             │ Email, IP, JWT, Card, API key etc.     │
├─────────────┼────────────────────────────────────────┤
│ utils.py    │ Actual scrubbing logic hai             │
│             │ File read/write, line by line scan     │
└─────────────┴────────────────────────────────────────┘
```

---

## 📦 Requirements

```
✅ Python 3.10 or higher
✅ No external libraries needed!
✅ Standard library only
✅ Works on Windows, Linux, Mac
```

### Check Your Python:

```cmd
python --version
```

```
Output: Python 3.12.10  ✅
```

---

## 🔧 Installation

### Windows:

```cmd
:: Step 1 - Project download karo (ZIP se)
:: Ya Git clone karo:
git clone https://github.com/SudhirDevOps1/keyforge-log-scrubber.git

:: Step 2 - Drive switch karo jahan project hai
E:

:: Step 3 - Folder me jao
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main

:: Step 4 - Files check karo
dir
```

### Linux / Mac:

```bash
# Clone karo
git clone https://github.com/SudhirDevOps1/keyforge-log-scrubber.git

# Folder me jao
cd keyforge-log-scrubber

# Permission do
chmod +x main.py

# Files check karo
ls -la
```

---

## ⚡ Quick Start

### Windows (CMD):

```cmd
:: Step 1 - Drive switch karo
E:

:: Step 2 - Folder me jao
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main

:: Step 3 - Test log file banao
echo 2024-01-15 User: admin@company.com IP: 192.168.1.55 > logs.txt
echo 2024-01-15 Card: 4111111111111111 >> logs.txt
echo 2024-01-15 password=SuperSecret123 >> logs.txt
echo 2024-01-15 secret=aB3xK9mNpQrStUvWxYz1234567890abcd >> logs.txt
echo 2024-01-15 AWS: AKIAIOSFODNN7EXAMPLE >> logs.txt
echo 2024-01-15 Normal log line nothing sensitive >> logs.txt

:: Step 4 - Tool chalao
python main.py scan logs.txt

:: Step 5 - Clean file dekho
type logs_cleaned.txt
```

### Linux / Mac (Terminal):

```bash
# Test log file banao
cat > logs.txt << 'EOF'
2024-01-15 User: admin@company.com IP: 192.168.1.55
2024-01-15 Card: 4111111111111111
2024-01-15 password=SuperSecret123
2024-01-15 secret=aB3xK9mNpQrStUvWxYz1234567890abcd
2024-01-15 AWS: AKIAIOSFODNN7EXAMPLE
2024-01-15 Normal log line nothing sensitive
EOF

# Tool chalao
python main.py scan logs.txt

# Clean file dekho
cat logs_cleaned.txt
```

---

## 💻 Usage & Commands

### Basic Syntax:

```
python main.py scan <FILE> [OPTIONS]
```

---

### 1️⃣ Basic Scan

```cmd
python main.py scan logs.txt
```

```
Kya karta hai:
→ logs.txt scan karta hai
→ Sensitive data [REDACTED] se replace karta hai
→ logs_cleaned.txt save karta hai
→ Original logs.txt unchanged rehta hai
```

---

### 2️⃣ Preview Mode

```cmd
python main.py scan logs.txt --preview
```

```
Kya karta hai:
→ Sirf screen pe dikhata hai
→ Koi file save NAHI hoti
→ Pehle dekho phir decide karo
→ Dry run / test ke liye perfect
```

---

### 3️⃣ Strict Mode

```cmd
python main.py scan logs.txt --strict
```

```
Kya karta hai:
→ Normal patterns + extra sweep
→ 40+ character high-entropy strings bhi pakadta hai
→ Unknown token formats bhi redact hote hain
→ Maximum security ke liye use karo
```

---

### 4️⃣ Custom Pattern

```cmd
python main.py scan logs.txt --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

```
Kya karta hai:
→ Apna khud ka regex pattern add karo
→ Built-in patterns ke saath kaam karta hai
→ Multiple patterns add kar sakte ho
```

---

### 5️⃣ Multiple Custom Patterns

```cmd
:: Windows CMD
python main.py scan logs.txt ^
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" ^
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}" ^
  --custom-pattern "PAN:[A-Z]{5}\d{4}[A-Z]"
```

```bash
# Linux / Mac
python main.py scan logs.txt \
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" \
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}" \
  --custom-pattern "PAN:[A-Z]{5}\d{4}[A-Z]"
```

---

### 6️⃣ Combine All Flags

```cmd
python main.py scan logs.txt --strict --preview --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

---

## 🔍 What Gets Redacted?

```
┌──────────────────┬─────────────────────────────────────┬──────────────────┐
│ Pattern Name     │ Example (Before)                    │ After            │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ Email            │ admin@company.com                   │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ IPv4 Address     │ 192.168.1.100                       │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ IPv6 Address     │ 2001:0db8:85a3::8a2e:0370:7334      │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ API Key/Secret   │ secret=aB3xK9mNpQrStUvWxYz123456    │ secret=[REDACTED]│
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ AWS Access Key   │ AKIAIOSFODNN7EXAMPLE                │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ JWT Token        │ eyJhbGciOiJIUzI1NiJ9.eyJ...        │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ Credit Card      │ 4111111111111111                    │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ Bearer Token     │ Bearer eyJhbGc...                   │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ Password Field   │ password=SuperSecret!               │ [REDACTED]       │
├──────────────────┼─────────────────────────────────────┼──────────────────┤
│ Custom Patterns  │ SSN:123-45-6789                     │ [REDACTED]       │
└──────────────────┴─────────────────────────────────────┴──────────────────┘
```

### Credit Cards Supported:

```
✅ Visa              → 4xxx xxxx xxxx xxxx
✅ MasterCard        → 5xxx xxxx xxxx xxxx
✅ American Express  → 3xxx xxxx xxxx xxx
✅ Discover          → 6011 xxxx xxxx xxxx
```

---

## 🚩 CLI Flags

```
┌──────────────────────┬──────────┬──────────────────────────────────────────┐
│ Flag                 │ Type     │ Description                              │
├──────────────────────┼──────────┼──────────────────────────────────────────┤
│ scan <file>          │ Required │ Scan karne ke liye file ka naam          │
├──────────────────────┼──────────┼──────────────────────────────────────────┤
│ --strict             │ Optional │ High-entropy strings bhi pakadta hai     │
├──────────────────────┼──────────┼──────────────────────────────────────────┤
│ --preview            │ Optional │ Dry run - koi file save nahi hoti        │
├──────────────────────┼──────────┼──────────────────────────────────────────┤
│ --custom-pattern     │ Optional │ Apna regex pattern add karo              │
│                      │          │ Multiple baar use kar sakte ho           │
└──────────────────────┴──────────┴──────────────────────────────────────────┘
```

---

## 🎯 Real Examples

### Example 1 — Web Server Log

```
Input (apache_access.log):
192.168.1.1 - admin@site.com [15/Jan/2024] "GET /api?key=abc123xyz789def456ghi012jkl345mn"

Output:
[REDACTED] - [REDACTED] [15/Jan/2024] "GET /api?key=[REDACTED]"
```

### Example 2 — Application Log

```
Input:
2024-01-15 ERROR DB connection failed for user: john@example.com password=MyPass123

Output:
2024-01-15 ERROR DB connection failed for user: [REDACTED] [REDACTED]
```

### Example 3 — AWS CloudWatch Log

```
Input:
AccessKeyId: AKIAIOSFODNN7EXAMPLE SecretKey: wJalrXUtnFEMI/K7MDENG/bPxRfi

Output:
AccessKeyId: [REDACTED] SecretKey: [REDACTED]
```

### Example 4 — Payment Gateway Log

```
Input:
Transaction processed for card 4111-1111-1111-1111 amount $500

Output:
Transaction processed for card [REDACTED] amount $500
```

### Example 5 — Auth Service Log

```
Input:
Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

Output:
[REDACTED]
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
  Lines modified  : 312
  Total redactions: 489
  Output file     : logs_cleaned.txt

  Pattern breakdown:
    EMAIL                201 hit(s)
    IPV4                 145 hit(s)
    JWT                   89 hit(s)
    API_KEY               43 hit(s)
    CREDIT_CARD           11 hit(s)
──────────────────────────────────────────────────

  ✅  Clean file saved → logs_cleaned.txt
```

---

## 🖥️ Windows Users Guide

### CMD Kaise Kholein:

```
Method 1: Win + R → "cmd" → Enter
Method 2: Start Menu → "Command Prompt"
Method 3: Search bar → "cmd" → Enter
```

### ⚠️ IMPORTANT — Drive Switch Karna:

```cmd
:: Agar project E: drive pe hai toh:
E:                                          ← Pehle drive switch karo
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main

:: Agar project D: drive pe hai toh:
D:
cd path\to\keyforge-log-scrubber

:: Agar project C: drive pe hai toh:
cd C:\path\to\keyforge-log-scrubber
```

### Kahan Hoon Check Karo:

```cmd
:: Current location dekho
cd

:: Files dekho
dir

:: Python check karo
python --version
```

---

## ❌ Common Mistakes & Fixes

### Mistake 1 — PowerShell Use Karna

```powershell
# ❌ GALAT
/usr/bin/env python3 main.py
# Error: '/usr/bin/env' is not recognized
```

```cmd
# ✅ SAHI — CMD use karo
python main.py scan logs.txt
```

---

### Mistake 2 — Drive Switch Bhoolna

```cmd
# ❌ GALAT
C:\Users\DELL> cd E:\tmp\keyforge
C:\Users\DELL>          ← Abhi bhi C: pe ho!
```

```cmd
# ✅ SAHI
C:\Users\DELL> E:
E:\> cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
E:\tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main>
```

---

### Mistake 3 — Galat Folder Se Chalana

```cmd
# ❌ GALAT
C:\Users\DELL> python main.py scan logs.txt
# Error: can't open file 'C:\Users\DELL\main.py'
```

```cmd
# ✅ SAHI — Pehle sahi folder me jao
E:
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
python main.py scan logs.txt
```

---

### Mistake 4 — logs.txt Banaye Bina Chalana

```cmd
# ❌ GALAT
python main.py scan logs.txt
# Error: [ERROR] File not found: logs.txt
```

```cmd
# ✅ SAHI — Pehle file banao
echo Test log admin@test.com > logs.txt
python main.py scan logs.txt
```

---

### Mistake 5 — python3 Likhna

```cmd
# ❌ GALAT (Linux command hai)
python3 main.py scan logs.txt
# Error: 'python3' is not recognized

# ✅ SAHI (Windows command)
python main.py scan logs.txt
```

---

### Mistake 6 — python PATH me nahi hai

```cmd
# ❌ Error
'python' is not recognized as an internal or external command
```

```
# ✅ Fix:
1. https://python.org/downloads pe jao
2. Python download karo
3. Install karte waqt:
   ☑️ "Add Python to PATH"  ← YE ZAROOR TICK KARO!
4. CMD band karo
5. Naya CMD kholo
6. python --version check karo
```

---

## 🔧 Troubleshooting

### Problem → Solution Table:

```
┌────────────────────────────────────┬──────────────────────────────────────┐
│ Error Message                      │ Fix                                  │
├────────────────────────────────────┼──────────────────────────────────────┤
│ 'python' is not recognized         │ Python install karo                  │
│                                    │ python.org/downloads                 │
│                                    │ "Add to PATH" tick karo              │
├────────────────────────────────────┼──────────────────────────────────────┤
│ can't open file 'main.py'          │ Sahi folder me jao                   │
│                                    │ E: → cd tmp\keyforge...              │
├────────────────────────────────────┼──────────────────────────────────────┤
│ [ERROR] File not found: logs.txt   │ logs.txt banao pehle                 │
│                                    │ echo test > logs.txt                 │
├────────────────────────────────────┼──────────────────────────────────────┤
│ '/usr/bin/env' is not recognized   │ CMD use karo PowerShell nahi         │
├────────────────────────────────────┼──────────────────────────────────────┤
│ 'python3' is not recognized        │ python likho python3 nahi            │
├────────────────────────────────────┼──────────────────────────────────────┤
│ The system cannot find the path    │ Drive switch karo pehle              │
│                                    │ E: likho phir cd karo                │
├────────────────────────────────────┼──────────────────────────────────────┤
│ Permission denied                  │ CMD admin mode me kholo              │
│                                    │ Right click → Run as Administrator   │
└────────────────────────────────────┴──────────────────────────────────────┘
```

---

## 🔒 Security Design

```
┌─────────────────────────────────────────────────────┐
│              Security Principles                    │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ✅ Original file READ-ONLY                         │
│     Kabhi modify nahi hoti                         │
│                                                     │
│  ✅ Separate Output File                            │
│     logs_cleaned.txt alag save hoti hai            │
│                                                     │
│  ✅ Chunked Processing                              │
│     64KB chunks — GB files bhi safe                │
│                                                     │
│  ✅ Offline Tool                                    │
│     Koi internet connection nahi chahiye           │
│     Data bahar nahi jata                           │
│                                                     │
│  ✅ Zero Dependencies                               │
│     Sirf Python standard library                   │
│     Koi third party package nahi                   │
│                                                     │
│  ✅ No Logging of Sensitive Data                    │
│     Tool khud koi data store nahi karta            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    main.py                          │
│              (CLI Entry Point)                      │
│                                                     │
│  argparse → Commands & Flags handle karta hai       │
│  Banner display karta hai                           │
│  Stats print karta hai                              │
└──────────────────────┬──────────────────────────────┘
                       │ calls
                       ▼
┌─────────────────────────────────────────────────────┐
│                    utils.py                         │
│              (Core Scrub Engine)                    │
│                                                     │
│  scan_and_scrub() → Main function                   │
│  _scrub_line()    → Line by line processing         │
│  _iter_lines_chunked() → Memory safe reading        │
│  print_stats()    → Report generate karta hai       │
└──────────┬──────────────────────┬───────────────────┘
           │ uses                 │ reads/writes
           ▼                     ▼
┌──────────────────┐   ┌──────────────────────────────┐
│   patterns.py    │   │         Files                │
│  (Regex Rules)   │   │                              │
│                  │   │  logs.txt      (input)  🔒   │
│  EMAIL           │   │  logs_cleaned.txt (output)✅  │
│  IPV4 / IPV6     │   │                              │
│  API_KEY         │   └──────────────────────────────┘
│  AWS_KEY         │
│  JWT             │
│  CREDIT_CARD     │
│  BEARER_TOKEN    │
│  PASSWORD_FIELD  │
│  CUSTOM_*        │
└──────────────────┘
```

---

## 👥 Who Should Use This?

```
┌──────────────────────┬───────────────────────────────────────┐
│ User                 │ Use Case                              │
├──────────────────────┼───────────────────────────────────────┤
│ 👨‍💻 Developers        │ Debug logs share karne se pehle       │
├──────────────────────┼───────────────────────────────────────┤
│ 🔐 Security Engineer │ Audit ke liye log cleanup             │
├──────────────────────┼───────────────────────────────────────┤
│ 🏢 DevOps Teams      │ Production logs anonymize karna       │
├──────────────────────┼───────────────────────────────────────┤
│ 📋 Compliance Teams  │ GDPR / PCI-DSS compliance             │
├──────────────────────┼───────────────────────────────────────┤
│ 🧪 QA Engineers      │ Test logs me se data clean karna      │
├──────────────────────┼───────────────────────────────────────┤
│ 📊 Data Analysts     │ Log data anonymize karke analyze karna│
└──────────────────────┴───────────────────────────────────────┘
```

---

## 📄 Output Files

```
Input  → logs.txt           (Original — NEVER modified) 🔒
Output → logs_cleaned.txt   (Safe clean version)        ✅

Naming Convention:
  logs.txt          → logs_cleaned.txt
  app_logs.txt      → app_logs_cleaned.txt
  server.log        → server_cleaned.log
  access.log        → access_cleaned.log
```

---

## 🌟 Future Features (Coming Soon)

```
🔜 Multiple file scan  → python main.py scan *.log
🔜 Folder scan         → python main.py scan /var/logs/
🔜 JSON log support    → Structured log handling
🔜 HTML Report         → Beautiful report generate karna
🔜 Config file         → .keyforge.yaml se rules load karna
🔜 Git hook            → Commit se pehle auto scan
```

---

## 📜 License

```
MIT License
Copyright (c) 2024 Sudhir Kumar (@SudhirDevOps1)

Free to use, modify and distribute.
Credit dena mat bhoolna! 😊
```

---

## 🤝 Contributing

```
1. Fork karo repository
2. Feature branch banao
   git checkout -b feature/amazing-feature
3. Changes karo aur commit karo
   git commit -m "Add amazing feature"
4. Push karo
   git push origin feature/amazing-feature
5. Pull Request kholo
```

---

## 📞 Contact & Support

```
👤 Author  : Sudhir Kumar
🐦 Twitter : @SudhirDevOps1
💼 GitHub  : github.com/SudhirDevOps1

🐛 Bug mila? → GitHub Issues me report karo
💡 Idea hai? → Discussions me share karo
⭐ Useful laga? → Star dena mat bhoolna!
```

---

<div align="center">

**Built with ❤️ by Sudhir Kumar (@SudhirDevOps1)**

*Privacy-first DevOps Tool*

⭐ **Star this repo if it helped you!** ⭐

</div>
