import unittest

from cli import find_risky_ports, suggest_fix


class FindRiskyPortsTests(unittest.TestCase):
    def test_finds_rdp(self):
        lines = ["open_ports: 3389,80\n"]
        self.assertEqual(find_risky_ports(lines), ["3389"])

    def test_finds_several_risky_ports(self):
        lines = ["open_ports: 21,22,23\n"]
        self.assertEqual(find_risky_ports(lines), ["21", "23"])

    def test_safe_ports_are_ignored(self):
        lines = ["open_ports: 22,80,443\n"]
        self.assertEqual(find_risky_ports(lines), [])

    def test_lines_without_open_ports_are_ignored(self):
        lines = ["host: 10.0.0.5\n", "os: windows\n"]
        self.assertEqual(find_risky_ports(lines), [])

    def test_empty_input(self):
        self.assertEqual(find_risky_ports([]), [])


class SuggestFixTests(unittest.TestCase):
    def test_rdp_fix_mentions_vpn(self):
        self.assertIn("VPN", suggest_fix("3389"))

    def test_telnet_fix_mentions_ssh(self):
        self.assertIn("SSH", suggest_fix("23"))

    def test_unknown_port(self):
        self.assertEqual(suggest_fix("9999"), "No known fix.")