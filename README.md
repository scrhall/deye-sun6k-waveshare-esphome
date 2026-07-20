# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN

[Español](docs/README.es.md) · [Sources](docs/SOURCES.md)

> [!WARNING]
> **AI-generated and pending review.** The documentation and configuration have not completed human or field validation. Anyone using, modifying, wiring, flashing, or operating this project does so entirely at their own risk. No liability is accepted for damage, data loss, injury, or incorrect operation.

ESPHome Modbus RTU reader for:

- Deye `SUN-6K-SG05LP1-EU-AM2-P`
- Waveshare `ESP32-S3-RS485-CAN`
- [Buy the board on Amazon](https://amzn.to/4fxuGVk)
- [Optional 12 V DC, 1.25 A, 15 W DIN-rail power supply](https://amzn.to/4vEIxz0)

Current YAML is **read-only**: 31 holding-register sensors, no write entities or commands. Compiled with ESPHome 2026.6.5. The register map is community-sourced and requires testing on the target inverter.

## Wiring

Use only the inverter RJ45 port marked **`Modbus`**.

| Deye Modbus RJ45 | Waveshare |
|---|---|
| Pin 1 — B | B- |
| Pin 2 — A | A+ |
| Pin 3 — GND | Do not connect |

![Official Deye Modbus RJ45 pinout](docs/assets/deye-modbus-rj45-pinout.png)

*Unmodified crop from the official Deye manual, printed page 53.*

Alternative pair: pin 8 → B-, pin 7 → A+. Do not use both pairs.

Power Waveshare through USB-C 5 V or DC 7–36 V. For a DIN-rail installation, the linked 12 V supply can feed the board's DC input; observe `+`/`-` polarity. Do not power it from the inverter RJ45.

Board UART: TX `GPIO17`, RX `GPIO18`; automatic direction control, no `flow_control_pin`. Keep the 120 Ω jumper disabled for the initial short-cable test.

> **Safety:** isolate the inverter before opening it. The DIN supply has a 100–240 V AC input: mains wiring must be enclosed and performed by a qualified person. Do not use `RS485/METER` or parallel ports. Share `BMS 485/CAN` only under the [experimental breakout procedure](docs/SHARED-BMS-RJ45-CABLE.md). The Deye manual marks the dedicated Modbus port “Reserved”; firmware compatibility is not guaranteed.

## Install

1. Choose the physical connection: use the dedicated `Modbus` port when available. If the BMS RJ45 must be shared while the battery uses CAN, first follow the **[male-to-male adapter cable guide](docs/SHARED-BMS-RJ45-CABLE.md)**.
2. In Home Assistant, install/start **ESPHome Device Builder** and open its web UI.
3. Select **New Device Setup**, enter Wi-Fi details, and finish the wizard. Before replacing its YAML, copy the generated API encryption key and OTA password.
4. Open **EDIT**. Replace the generated YAML with the contents of [`deye-sun6k-waveshare.yaml`](https://raw.githubusercontent.com/scrhall/deye-sun6k-waveshare-esphome/main/deye-sun6k-waveshare.yaml), then save.
5. Open the Dashboard **SECRETS** editor. Add the five keys listed in [`secrets.example.yaml`](https://github.com/scrhall/deye-sun6k-waveshare-esphome/blob/main/secrets.example.yaml), using the Wi-Fi details and generated credentials from the wizard.
6. From the device menu, select **Validate**, then **Install**. Connect the board by USB-C for the first flash; later updates can use Wi-Fi.

ESPHome defaults: `9600 8N1`, slave `0x01`, function `03`, polling every 10 seconds. The inverter manual exposes only `Modbus SN` in the LCD menus, not baud rate or parity; set `modbus_address` to match that value. `9600 8N1` comes from the community integration and remains subject to physical verification on this model/firmware.

### Check `Modbus SN` on the inverter

1. On the main touchscreen, tap the **gear icon** at the top right.
2. Tap **`Advanced Function`**.
3. Use the right-side **↑/↓ arrows** until the page label is **`Paral. Set3`**.
4. Read **`Modbus SN`** at the top of that screen. It must be `01` for this YAML's default `0x01`; otherwise change `modbus_address` to the displayed value.

Viewing does not require saving: avoid changing fields and do not press the green confirmation button. The official manual shows no password prompt for viewing; firmware may differ.

First test: import [`deye-sun6k-waveshare-test.yaml`](deye-sun6k-waveshare-test.yaml), which reads only SOC register `184` and voltage register `183` (×0.01 V). Follow the [step-by-step test](docs/FIRST-READ-TEST.md). If the dedicated port ignores the proprietary low register map, try the read-only [`SunSpec` signature test](deye-sun6k-sunspec-test.yaml).

Signed grid/battery power values must be checked against known import/export and charge/discharge states.

## Sources

- [Official Deye manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): ports, `Modbus SN`, pinout on printed pages 3, 14, 44, 53.
- Official Waveshare: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- [Official ESPHome Modbus Controller docs](https://esphome.io/components/modbus_controller/).
- [Official ESPHome Device Builder guide](https://esphome.io/guides/getting_started_hassio/).
- [Community Deye register map](https://github.com/Lewa-Reka/esphome-deye-inverter), `SG0XLP1` configuration.
- Detailed register provenance: [docs/SOURCES.md](docs/SOURCES.md).

MIT licensed. Not affiliated with Deye, Waveshare, Amazon, or ESPHome.
