# Mini Security Tool

A small Python tool that reads scan data, finds risky open ports,
and suggests a fix for each one.

## What it checks

| Port | Service | Fix |
|------|---------|-----|
| 3389 | RDP | Close RDP to the internet, use VPN instead |
| 23 | Telnet | Disable Telnet, use SSH instead |
| 21 | FTP | Disable FTP, use SFTP instead |

## How to run

```
python cli.py
python cli.py path/to/scan_data.txt
python cli.py scan/sample_data.txt -o my_report.txt
python cli.py --help
```

By default the tool reads `scan/sample_data.txt` and writes `report.txt`.
```
Risky ports found: ['3389']
Port 3389: Close RDP to the internet, use VPN instead.
Report saved to report.txt
```
## Roadmap

- [x] Choose the input file from the command line
- [ ] Show the host for each risky port
- [ ] Add more risky ports
- [ ] Add tests
- [ ] Severity levels
- [ ] JSON and HTML reports