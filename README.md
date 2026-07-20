# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN

[Español](docs/README.es.md) · [Sources](docs/SOURCES.md)

ESPHome Modbus RTU reader for:

- Deye `SUN-6K-SG05LP1-EU-AM2-P`
- Waveshare `ESP32-S3-RS485-CAN`
- [Buy the board on Amazon](https://amzn.to/4fxuGVk)

Current YAML is **read-only**: 31 holding-register sensors, no write entities or commands. Compiled with ESPHome 2026.6.5. The register map is community-sourced and requires testing on the target inverter.

## Wiring

Use only the inverter RJ45 port marked **`Modbus`**.

| Deye Modbus RJ45 | Waveshare |
|---|---|
| Pin 1 — B | B- |
| Pin 2 — A | A+ |
| Pin 3 — GND | Do not connect |

Alternative pair: pin 8 → B-, pin 7 → A+. Do not use both pairs.

Power Waveshare through USB-C 5 V or DC 7–36 V. Do not power it from the inverter RJ45.

Board UART: TX `GPIO17`, RX `GPIO18`; automatic direction control, no `flow_control_pin`. Keep the 120 Ω jumper disabled for the initial short-cable test.

> **Safety:** isolate the inverter before opening it. Do not use `BMS 485/CAN`, `RS485/METER`, or parallel ports. The Deye manual marks the Modbus port “Reserved”; firmware compatibility is not guaranteed.

## Install

```bash
git clone https://github.com/scrhall/deye-sun6k-waveshare-esphome.git
cd deye-sun6k-waveshare-esphome
cp secrets.example.yaml secrets.yaml
```

Edit `secrets.yaml`, then:

```bash
esphome config deye-sun6k-waveshare.yaml
esphome run deye-sun6k-waveshare.yaml
```

Defaults: `9600 8N1`, slave `0x01`, function `03`, polling every 10 seconds. If needed, change `modbus_address` to match the inverter's `Modbus SN`.

Test first:

- `Battery SOC`: register `184`
- `Battery Voltage`: register `183`, ×0.01 V

No response: verify port, `Modbus SN`, A/B polarity, logs, RS485 LED, short cable, and absence of another Modbus client.

Signed grid/battery power values must be checked against known import/export and charge/discharge states.

## Sources

- [Official Deye manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): ports, `Modbus SN`, pinout on printed pages 3, 14, 44, 53.
- Official Waveshare: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- [Official ESPHome Modbus Controller docs](https://esphome.io/components/modbus_controller/).
- [Community Deye register map](https://github.com/Lewa-Reka/esphome-deye-inverter), `SG0XLP1` configuration.
- Detailed register provenance: [docs/SOURCES.md](docs/SOURCES.md).

MIT licensed. Not affiliated with Deye, Waveshare, Amazon, or ESPHome.
