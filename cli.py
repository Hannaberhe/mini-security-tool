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

data = load_data("scan/sample_data.txt")
risky = find_risky_ports(data)
print("Risky ports found:", risky)

for port in risky:
    print(f"Port {port}: {suggest_fix(port)}")

with open("report.txt", "w") as f:
    for port in risky:
        f.write(f"Port {port}: {suggest_fix(port)}\n")

print("Report saved to report.txt")
