# Vendored Deye 1P LV package

This directory preserves the transitive YAML package tree used by
`pv_inverter/deye_hybrid_1p_lv.yaml` from:

- Source: <https://github.com/Lewa-Reka/esphome-deye-inverter>
- Release: `0.14.0`
- Commit: `c0adb5c275a7d2be127e8fffe8c3c4711ea6e475`
- Upstream license: Apache-2.0, copied to
  [`THIRD_PARTY_LICENSES/Lewa-Reka-esphome-deye-inverter-Apache-2.0.txt`](../THIRD_PARTY_LICENSES/Lewa-Reka-esphome-deye-inverter-Apache-2.0.txt)

## Local read-only changes

The original text is retained inside reversible comment blocks marked:

```text
READONLY-DISABLED-BEGIN
READONLY-DISABLED-END
```

Disabled active configuration:

- all top-level `select`, `switch`, `number`, `datetime`, `button`, and
  `script` blocks;
- `api.on_client_disconnected`, because it ran the four-setting Safe Mode
  Modbus write script after 600 seconds;
- read-only template binary sensor `Load Priority`, because it depended on
  the removed writable `energy_management_priority` select.

Active result: 76 `modbus_controller` read entities and zero active write
components. The complete Spanish per-file explanation of every disabled write
entity is in
[`docs/UPSTREAM-WRITE-ENTITY-AUDIT.es.md`](../docs/UPSTREAM-WRITE-ENTITY-AUDIT.es.md).

## Update policy

Do not point the main YAML at the live upstream Git package. Review each future
upstream release as a new snapshot, regenerate the write audit, disable all
write paths, expand with `esphome config`, compile, and run the static read-only
check before publishing.
