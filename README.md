<<<<<<< HEAD
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
=======
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
>>>>>>> ec9b3d0727420f744473b681fbd6d2a018240acc
