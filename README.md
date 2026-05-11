# Secret Scanner CLI Tool

A Python-based CLI tool that scans files and directories for hardcoded secrets using regex patterns.

## Features

- Scan files or directories
- Detect common secrets:
  - AWS Access Keys
  - Google API Keys
  - Stripe Secret Keys
  - JWT Tokens
  - Passwords
  - Private Keys
  - Bearer Tokens
- Logging support
- Displays:
  - File name
  - Line number
  - Matched secret

---

## Installation

```bash
git clone https://github.com/Marwai89/secret-scanner.git

cd secret-scanner
```

---

## Usage

### Scan a file

```bash
python scanner.py sample.txt
```

### Scan a directory

```bash
python scanner.py my_folder/
```

---

## Detection Logic

The scanner reads files line by line and uses regular expressions (regex) to identify common secret patterns such as API keys, passwords, tokens, and private keys.

---

## Example Output

```text
===== SECRET SCAN REPORT =====

Total Findings: 2

Type : AWS Access Key
File : sample.txt
Line : 4
Match: AKIAIOSFODNN7EXAMPLE
```

---

## Logging

Logs are saved in:

```text
logs/scanner.log
```

---

## Technologies Used

- Python
- Regex
- argparse
- logging
- os