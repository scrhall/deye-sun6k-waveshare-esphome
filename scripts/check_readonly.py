#!/usr/bin/env python3
"""Fail when the vendored full profile contains an active write path."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
YAMLS = [ROOT / "deye-sun6k-waveshare-upstream-readonly.yaml"]
YAMLS += sorted((ROOT / "pv_inverter").rglob("*.yaml"))

active_lines: list[str] = []
for path in YAMLS:
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.lstrip().startswith("#"):
            active_lines.append(f"{path.relative_to(ROOT)}:{line_number}:{line}")

active = "\n".join(active_lines)
checks = {
    "active write-capable component domain": r"(?m):\d+:(number|select|switch|button|datetime|script):\s*$",
    "Modbus write lambda": r"\bwrite_lambda\b",
    "multiple-register write": r"\buse_write_multiple\b",
    "explicit Modbus write command": r"\b(write_register|ModbusCommandItem)\b",
    "API-disconnect write automation": r"\b(on_client_disconnected|set_safe_modbus_registers)\b",
}

failures = []
for description, pattern in checks.items():
    matches = re.findall(pattern, active)
    if matches:
        failures.append(f"{description}: {len(matches)} match(es)")

main = (ROOT / "deye-sun6k-waveshare-upstream-readonly.yaml").read_text(encoding="utf-8")
if "flow_control_pin: GPIO21" not in main:
    failures.append("required Waveshare RS485 direction control GPIO21 is missing")

if failures:
    print("readonly_static_check=FAIL", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    raise SystemExit(1)

print("readonly_static_check=PASS")
print(f"yaml_files_checked={len(YAMLS)}")
