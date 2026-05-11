# Secret Scanner CLI Tool

## Overview

This project is a Python command-line tool that scans files and directories for hardcoded secrets using Regular Expressions (Regex).

The tool helps detect sensitive information such as:

- Passwords
- API Keys
- Tokens
- Private Keys

---

## Features

- Scan a single file
- Scan entire directories
- Recursive scanning
- Regex-based secret detection
- Logging support
- CLI interface using argparse

---

## Secret Patterns Included

The scanner detects:

1. AWS Access Keys
2. Google API Keys
3. Stripe Secret Keys
4. JWT Tokens
5. Passwords
6. Bearer Tokens
7. Private Keys

---

## Detection Logic

The application uses Python Regular Expressions (`re`) to search for patterns commonly associated with secrets.

Example:

```python
r"AKIA[0-9A-Z]{16}"
```

This detects AWS Access Keys.

---

## Usage

### Scan a File

```bash
python scanner.py sample_secrets.txt
```

### Scan a Directory

```bash
python scanner.py .
```

---

## Logging

Logs are stored in:

```text
logs/scanner.log
```

---

## Example Output

```text
===== SECRET SCAN REPORT =====

Type : Password
File : sample_secrets.txt
Line : 1
Match: password = "mypassword123"
```