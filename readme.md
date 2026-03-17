# 🧹 KeyForge Log-Scrubber

> **Privacy-first DevOps Tool**
> By Sudhir Kumar ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))

---

## ⚠️ WINDOWS USERS — PEHLE YE PADHO!

### ❌ Common Mistakes Jo Bilkul Mat Karna

---

### Mistake 1 — PowerShell Se Mat Chalao

```powershell
# ❌ GALAT — PowerShell me ye error aayega
/usr/bin/env python3 main.py
# Error: '/usr/bin/env' is not recognized
```

```cmd
# ✅ SAHI — Hamesha CMD use karo
# Start → CMD → Enter
python main.py scan logs.txt
```

---

### Mistake 2 — Drive Switch Karna Bhool Jana

```cmd
# ❌ GALAT — Sirf cd likhne se drive switch nahi hoti
cd E:\tmp\keyforge-log-scrubber-main

# Tum abhi bhi C:\Users\DELL me rahoge!
```

```cmd
# ✅ SAHI — Pehle drive switch karo
E:
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
```

---

### Mistake 3 — logs.txt Banaye Bina Tool Chalana

```cmd
# ❌ GALAT — Seedha tool chalana
python main.py scan logs.txt
# Error: [ERROR] File not found: logs.txt
```

```cmd
# ✅ SAHI — Pehle logs.txt banao
echo Test log: admin@company.com > logs.txt
python main.py scan logs.txt
```

---

### Mistake 4 — python3 Likhna Windows Me

```cmd
# ❌ GALAT — Windows me python3 nahi hota
python3 main.py scan logs.txt
# Error: 'python3' is not recognized

# ✅ SAHI — Windows me sirf python likhte hain
python main.py scan logs.txt
```

---

### Mistake 5 — Galat Folder Me Tool Chalana

```cmd
# ❌ GALAT — Kisi bhi folder se chalana
C:\Users\DELL> python main.py scan logs.txt
# Error: can't open file 'C:\\Users\\DELL\\main.py'

# ✅ SAHI — Pehle sahi folder me jao
E:
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
python main.py scan logs.txt
```

---

## ✅ SAHI TARIKA — Step by Step

### Step 1 — CMD Kholo

```
Win + R dabao
→ "cmd" likho
→ Enter dabao
```

### Step 2 — Python Check Karo

```cmd
python --version
```

```
Output aana chahiye:
Python 3.12.x  ✅
```

### Step 3 — Drive Switch Karo

```cmd
E:
```

### Step 4 — Folder Me Jao

```cmd
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
```

### Step 5 — Files Check Karo

```cmd
dir
```

```
Ye files dikhni chahiye:
main.py      ✅
patterns.py  ✅
utils.py     ✅
README.md    ✅
```

### Step 6 — Test Log File Banao

```cmd
echo 2024-01-15 User: admin@company.com IP: 192.168.1.55 > logs.txt
echo 2024-01-15 Card: 4111111111111111 >> logs.txt
echo 2024-01-15 password=SuperSecret123 >> logs.txt
echo 2024-01-15 secret=aB3xK9mNpQrStUvWxYz1234567890abcd >> logs.txt
echo 2024-01-15 AWS: AKIAIOSFODNN7EXAMPLE >> logs.txt
echo 2024-01-15 Normal log line >> logs.txt
```

### Step 7 — Tool Chalao

```cmd
python main.py scan logs.txt
```

### Step 8 — Clean File Dekho

```cmd
type logs_cleaned.txt
```

---

## 🚀 Installation

```cmd
:: Step 1 - Python Install Check Karo
python --version

:: Step 2 - Download karo agar nahi hai
:: https://www.python.org/downloads/
:: ⚠️ Install karte waqt "Add Python to PATH" ZAROOR tick karo!

:: Step 3 - Project folder me jao
E:
cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
```

---

## 💻 Usage

### Basic Scan

```cmd
python main.py scan logs.txt
```

Output saved to → `logs_cleaned.txt`

---

### Strict Mode

```cmd
python main.py scan logs.txt --strict
```

---

### Preview Mode (Dry Run)

```cmd
python main.py scan logs.txt --preview
```

---

### Custom Pattern

```cmd
python main.py scan logs.txt --custom-pattern "SSN:\d{3}-\d{2}-\d{4}"
```

### Multiple Custom Patterns

```cmd
python main.py scan logs.txt ^
  --custom-pattern "SSN:\d{3}-\d{2}-\d{4}" ^
  --custom-pattern "EMP-ID:[A-Z]{2}\d{6}"
```

### Sab Flags Ek Saath

```cmd
python main.py scan logs.txt --strict --preview ^
  --custom-pattern "INTERNAL-TOKEN:[A-Z0-9]{16}"
```

---

## 🔍 Kya Kya Redact Hota Hai

```
┌─────────────────┬──────────────────────────────────────┐
│ Pattern         │ Example                              │
├─────────────────┼──────────────────────────────────────┤
│ Email           │ user@example.com                     │
│ IPv4            │ 192.168.1.100                        │
│ IPv6            │ 2001:0db8:85a3::8a2e:0370:7334       │
│ API Key/Secret  │ secret=aB3xK9... (32-64 chars)       │
│ AWS Key         │ AKIAIOSFODNN7EXAMPLE                 │
│ JWT Token       │ eyJhbGciOiJIUzI1NiJ9.eyJ...         │
│ Credit Card     │ 4111111111111111                     │
│ Bearer Token    │ Bearer eyJhbGc...                    │
│ Password Field  │ password=SuperSecret!                │
│ Custom Patterns │ Apna rule add karo                   │
└─────────────────┴──────────────────────────────────────┘
```

---

## 📂 Output Files

```
logs.txt          ← Original (KABHI modify nahi hoti) 🔒
logs_cleaned.txt  ← Clean version with [REDACTED]    ✅
```

---

## 🔒 Security Design

```
✅ Original file read-only hai — kabhi modify nahi hoti
✅ Output alag file me save hoti hai
✅ Chunked reading (64 KB) — bade GB logs bhi handle hote hain
✅ Koi internet connection nahi chahiye
✅ Koi external library nahi chahiye
```

---

## ❓ Troubleshooting

### Problem 1

```
Error: 'python' is not recognized
Fix  : https://python.org se Python install karo
       Install me "Add Python to PATH" tick karo ✅
```

### Problem 2

```
Error: can't open file 'main.py'
Fix  : Pehle sahi folder me jao
       E:
       cd tmp\keyforge-log-scrubber-main\keyforge-log-scrubber-main
```

### Problem 3

```
Error: [ERROR] File not found: logs.txt
Fix  : Pehle logs.txt banao
       echo Test log > logs.txt
```

### Problem 4

```
Error: '/usr/bin/env' is not recognized
Fix  : PowerShell band karo
       CMD use karo
       python main.py scan logs.txt
```

---

## 📊 Sample Output

```
  🔍  Scanning  : logs.txt
  ⚡  Strict    : OFF
  👁   Preview   : OFF

──────────────────────────────────────────────────
  📊  KeyForge Scrub Report
──────────────────────────────────────────────────
  Lines scanned   : 7
  Lines modified  : 6
  Total redactions: 6

  Pattern breakdown:
    EMAIL           1 hit(s)
    IPV4            2 hit(s)
    CREDIT_CARD     1 hit(s)
    PASSWORD_FIELD  1 hit(s)
    API_KEY         1 hit(s)
    AWS_KEY         1 hit(s)
──────────────────────────────────────────────────

  ✅  Clean file saved → logs_cleaned.txt
```

---

## 🏷️ Branding

**KeyForge Log-Scrubber** — Privacy-first DevOps Tool
Built with ❤️ by Sudhir Kumar ([@SudhirDevOps1](https://twitter.com/SudhirDevOps1))
