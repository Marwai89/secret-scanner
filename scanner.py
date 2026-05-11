import os
import re
import argparse
import logging

# Create logs directory if it does not exist
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Regex patterns for detecting secrets
SECRET_PATTERNS = {

    "AWS Access Key":
        r"AKIA[0-9A-Z]{16}",

    "Google API Key":
        r"AIza[0-9A-Za-z\-_]{35}",

    "Stripe Secret Key":
        r"sk_live_[0-9a-zA-Z]{24}",

    "JWT Token":
        r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9._-]+\.[a-zA-Z0-9._-]+",

    "Private Key":
        r"-----BEGIN PRIVATE KEY-----",

    "Password":
        r'(?i)password\s*=\s*["\'][^"\']+["\']',

    "Bearer Token":
        r"Bearer\s+[A-Za-z0-9\-._~+/]+=*"
}


def scan_file(file_path):

    findings = []

    try:

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:

            for line_num, line in enumerate(file, start=1):

                for secret_type, pattern in SECRET_PATTERNS.items():

                    matches = re.findall(pattern, line)

                    for match in matches:

                        finding = {
                            "type": secret_type,
                            "file": file_path,
                            "line": line_num,
                            "match": match
                        }

                        findings.append(finding)

                        logging.warning(
                            f"{secret_type} found in "
                            f"{file_path} line {line_num}"
                        )

    except Exception as e:

        logging.error(f"Error scanning {file_path}: {e}")

    return findings


def scan_directory(directory):

    all_findings = []

    for root, dirs, files in os.walk(directory):

        # Ignore Git directories
        if ".git" in root:
            continue

        for file in files:

            file_path = os.path.join(root, file)

            findings = scan_file(file_path)

            all_findings.extend(findings)

    return all_findings


def print_report(findings):

    print("\n===== SECRET SCAN REPORT =====\n")

    print(f"Total Findings: {len(findings)}\n")

    if not findings:

        print("No secrets found.")
        return

    for finding in findings:

        print(f"Type : {finding['type']}")
        print(f"File : {finding['file']}")
        print(f"Line : {finding['line']}")
        print(f"Match: {finding['match']}")
        print("-" * 50)


def main():

    parser = argparse.ArgumentParser(
        description="Secret Scanner CLI Tool"
    )

    parser.add_argument(
        "path",
        help="File or directory to scan"
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    target = args.path

    if not os.path.exists(target):

        print("Path does not exist.")
        return

    logging.info(f"Starting scan: {target}")

    print(f"\nScanning: {target}")

    if os.path.isfile(target):

        findings = scan_file(target)

    else:

        findings = scan_directory(target)

    print_report(findings)

    logging.info("Scan completed.")

    print("\nScan completed.")
    print("Log file saved in logs/scanner.log")


if __name__ == "__main__":
    main()