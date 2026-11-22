import argparse
import sys


def load_data(path):
    with open(path) as f:
        return f.readlines()


def find_risky_ports(lines):
    risky_ports = ["3389", "23", "21"]
    found = []
    for line in lines:
        if "open_ports" in line:
            ports = line.split(":")[1].strip().split(",")
            for p in ports:
                if p in risky_ports:
                    found.append(p)
    return found


def suggest_fix(port):
    fixes = {
        "3389": "Close RDP to the internet, use VPN instead.",
        "23": "Disable Telnet, use SSH instead.",
        "21": "Disable FTP, use SFTP instead.",
    }
    return fixes.get(port, "No known fix.")


def main():
    parser = argparse.ArgumentParser(
        description="Find risky open ports and suggest fixes."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="scan/sample_data.txt",
        help="path to the scan data file (default: scan/sample_data.txt)",
    )
    parser.add_argument(
        "-o", "--output",
        default="report.txt",
        help="path for the report file (default: report.txt)",
    )
    args = parser.parse_args()

    try:
        data = load_data(args.input)
    except FileNotFoundError:
        print(f"Error: file not found: {args.input}")
        return 1

    risky = find_risky_ports(data)
    print("Risky ports found:", risky)
    for port in risky:
        print(f"Port {port}: {suggest_fix(port)}")

    with open(args.output, "w") as f:
        for port in risky:
            f.write(f"Port {port}: {suggest_fix(port)}\n")

    print(f"Report saved to {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())