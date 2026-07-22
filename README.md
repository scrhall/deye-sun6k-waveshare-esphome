# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN

[Español](docs/README.es.md) · [Sources](docs/SOURCES.md)

Read-only ESPHome Modbus RTU integration for:

- Deye `SUN-6K-SG05LP1-EU-AM2-P`
- Waveshare `ESP32-S3-RS485-CAN`
- [Buy the board on Amazon](https://amzn.to/4fxuGVk)
- [Optional 12 V DC DIN-rail power supply](https://amzn.to/4vEIxz0)

## Field-verified happy path

Use this exact topology:

1. Inverter's dedicated RJ45 port labelled **`Modbus`**.
2. One uninterrupted CAT/Ethernet cable; no splitter, coupler, BMS branch, meter branch, or parallel master.
3. Only RJ45 pins **1 and 2** connected:

| Deye Modbus RJ45 | Waveshare RS485 terminal |
|---|---|
| Pin 1 — `B` | `B-` |
| Pin 2 — `A` | `A+` |
| Pins 3–8 | Not connected |

RJ45 refers only to the connector; this is RS485/Modbus RTU, not Ethernet networking.

![Official Deye Modbus RJ45 pinout](docs/assets/deye-modbus-rj45-pinout.png)

*Unmodified crop from the official Deye manual, printed page 53.*

Waveshare UART and direction control:

```yaml
uart:
  tx_pin: GPIO17
  rx_pin: GPIO18

modbus:
  flow_control_pin: GPIO21
```

`GPIO21` is required: without it the board transmitted but did not correctly switch the RS485 transceiver for reception.

Power Waveshare separately through USB-C 5 V or its 7–36 V DC terminal. Do not take power from the Modbus RJ45. If using a DIN supply from the inverter's Backup/Load AC output, feed it from a protected branch rather than directly from raw inverter terminals.

## Firmware

The repository intentionally provides one firmware:

[`deye-sun6k-waveshare-upstream-readonly.yaml`](deye-sun6k-waveshare-upstream-readonly.yaml)

It pins an audited snapshot derived from [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter). This project activates only its read-only subset. The upstream project also provides writable inverter controls; they are intentionally not exposed here. Their definitions remain only as `READONLY-DISABLED` comments for audit.

- [Per-file write-entity audit](docs/UPSTREAM-WRITE-ENTITY-AUDIT.es.md)
- [Vendored package notes](pv_inverter/README.md)
- CI rejects active `number`, `select`, `switch`, `button`, `datetime`, scripts, or Modbus write primitives.

## Install with ESPHome Device Builder

1. Create the device and keep the generated API encryption key and OTA password.
2. Replace its YAML with the [raw read-only YAML](https://raw.githubusercontent.com/scrhall/deye-sun6k-waveshare-esphome/main/deye-sun6k-waveshare-upstream-readonly.yaml).
3. Add the keys from [`secrets.example.yaml`](secrets.example.yaml) to the Dashboard **SECRETS** editor.
4. Set inverter `Modbus SN` to `01`, or change `modbus_inverter_address` to match it.
5. Select **Validate**, then **Install**. Use USB-C for the first flash; later updates can use OTA.

Serial settings physically validated on this installation: `9600 8N1`, slave `0x01`, function `03`. Screen route: gear → `Advanced Function` → arrows to `Paral. Set3` → `Modbus SN`.

## Home Assistant verification

Live verification on 2026-07-21 returned:

- 86 `sensor` entities and 2 `binary_sensor` entities reporting data.
- Battery, PV, grid, load, temperatures, energy totals, device metadata, alarms, and ESP diagnostics.
- `Running Status = normal`, `Device Alarm = OK`, `Device Fault = OK`.
- Zero `number`, `select`, `switch`, `button`, or `datetime` entities for this device.

The exact entity count may change if ESPHome or the read-only package is updated, but writable control domains must remain zero.

## Sources

- [Official Deye manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf)
- Official Waveshare [product page](https://www.waveshare.com/esp32-s3-rs485-can.htm), [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), and [schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf)
- [ESPHome Modbus Controller](https://esphome.io/components/modbus_controller/)
- [Detailed provenance](docs/SOURCES.md)

MIT licensed. Upstream vendored files retain their Apache-2.0 license. Not affiliated with Deye, Waveshare, Amazon, ESPHome, or Lewa-Reka.
