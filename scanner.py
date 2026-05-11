import re
import argparse

# Secret patterns
SECRET_PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Password": r'(?i)password\s*=\s*["\'][^"\']+["\']',
}

def scan_file(file_path):

    findings = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:

        for line_num, line in enumerate(file, start=1):

            for secret_type, pattern in SECRET_PATTERNS.items():

                matches = re.findall(pattern, line)

                for match in matches:

                    findings.append({
                        "type": secret_type,
                        "line": line_num,
                        "match": match
                    })

    return findings


def main():

    parser = argparse.ArgumentParser(
        description="Simple Secret Scanner"
    )

    parser.add_argument("file", help="File to scan")

    args = parser.parse_args()

    results = scan_file(args.file)

    if not results:
        print("No secrets found.")

    else:

        print("\nSecrets Detected:\n")

        for result in results:

            print(f"Type : {result['type']}")
            print(f"Line : {result['line']}")
            print(f"Match: {result['match']}")
            print("-" * 40)


if __name__ == "__main__":
    main()
    