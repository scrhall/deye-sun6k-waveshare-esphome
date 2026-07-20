# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN — read-only ESPHome

[Versión en español](docs/README.es.md)

ESPHome configuration for reading a **Deye `SUN-6K-SG05LP1-EU-AM2-P`** single-phase hybrid inverter over **Modbus RTU/RS485**, using the isolated industrial **Waveshare `ESP32-S3-RS485-CAN`** board.

> Status: successfully compiled with ESPHome 2026.6.5. Board and inverter pinouts are backed by official documentation. The low-address register map is community-sourced and must be verified on the specific inverter revision.

## Sources

Every relevant technical claim is mapped to a document and section in **[Sources and traceability](docs/SOURCES.md)**. Summary:

- Official Deye source: [2025 SG05LP1-EU-AM2-P manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf), especially printed pages 3, 14, 44, and 53.
- Official Waveshare sources: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), and [schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- Official ESPHome source: [Modbus Controller documentation](https://esphome.io/components/modbus_controller/).
- Register map: [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), clearly identified as a community source rather than official Deye documentation.

## Hardware

- Inverter: Deye `SUN-6K-SG05LP1-EU-AM2-P`.
- Interface: Waveshare `ESP32-S3-RS485-CAN`, ESP32-S3R8, isolated RS485 with automatic direction control.
- [Buy the board on Amazon](https://amzn.to/4fxuGVk).
- [Official Waveshare wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN).
- [Official Waveshare product page](https://www.waveshare.com/esp32-s3-rs485-can.htm).
- [Official Deye manual for the SG05LP1-EU-AM2-P family](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf); Modbus pinout is on printed page 53.

## Safety and scope

This is **read-only at the ESPHome configuration level**:

- It defines only `modbus_controller` sensors over holding registers.
- It defines no `number`, `select`, `switch`, `button`, or write action.
- It does not reuse the complete community package because that package includes controls that write registers.

ESPHome still acts as a Modbus client and transmits function `03` read requests. “Read-only” does not mean electrically silent.

**Electrical hazard:** shut down and isolate the inverter according to its manual before opening the lower connection compartment. Use a qualified installer where required. Do not connect this reader to `BMS 485/CAN`, `RS485/METER`, `Parallel 1`, or `Parallel 2`.

## Wiring

Use the internal RJ45 connector marked **`Modbus`**. Source: [official Deye manual, printed pages 3, 14, and 53](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf). The same manual calls this port “Reserved”, so actual compatibility depends on firmware.

| Inverter Modbus RJ45 | Waveshare RS485 |
|---|---|
| Pin 1 — `sunspe-485_B` | B- |
| Pin 2 — `sunspe-485_A` | A+ |
| Pin 3 — `GND_sunspe-485` | **Do not connect**; the board's isolated RS485 terminal exposes no GND |

Duplicated inverter pair: pin 8 to B-, pin 7 to A+. Do not wire both pairs simultaneously.

Power the Waveshare through USB-C 5 V or its 7–36 V DC input terminals. **Do not power it from the inverter RJ45.**

The board's 120 Ω termination is disabled by default. Leave it disabled for an initial short-cable test. For a long or noisy bus, evaluate end termination; do not add it blindly if the inverter already terminates the line.

## Confirmed Waveshare parameters

- RS485 UART TX: `GPIO17`.
- RS485 UART RX: `GPIO18`.
- Direction control: automatic in hardware; no `flow_control_pin`.
- Isolated RS485 with TVS, surge, and ESD protection.

Sources: official Waveshare [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf), and [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN). Exact traceability: [docs/SOURCES.md](docs/SOURCES.md).

## Installation

1. Install ESPHome, or use the ESPHome add-on in Home Assistant.
2. Clone this repository.
3. Copy the secrets template:

   ```bash
   cp secrets.example.yaml secrets.yaml
   ```

4. Enter Wi-Fi details and generate credentials:

   ```bash
   openssl rand -base64 32  # api_encryption_key
   openssl rand -hex 32     # ota_password
   ```

5. Validate and compile:

   ```bash
   esphome config deye-sun6k-waveshare.yaml
   esphome compile deye-sun6k-waveshare.yaml
   ```

6. Perform the first flash over USB-C:

   ```bash
   esphome run deye-sun6k-waveshare.yaml
   ```

7. Add the discovered device to Home Assistant and assign it to the appropriate area.

## Initial test

Defaults:

- Modbus RTU, `9600 8N1`.
- Slave address `0x01`.
- 10-second polling interval.
- Holding registers, function `03`.

Check these first:

- `Battery SOC`, register `184`.
- `Battery Voltage`, register `183`, scale ×0.01 V.

If there is no response:

1. Confirm the physical `Modbus` port.
2. Confirm the inverter's `Modbus SN`; change `modbus_address` if it is not `1`.
3. Swap A+ and B- if the installation uses opposite line naming.
4. Inspect ESPHome logs and the Waveshare RS485 LED.
5. Confirm that no other Modbus client shares the bus.
6. Test with a 10–20 second interval and a short cable.
7. Confirm that the inverter firmware/revision enables the port and proprietary map.

## Signed values

Grid and battery power registers use `S_WORD`. Verify the sign convention while observing known operating states:

- Grid import versus export.
- Battery charging versus discharging.

The YAML does not invert signs, avoiding an unverified assumption.

## Included registers

Battery, PV1/PV2, grid, external CT, output, load, temperatures, frequencies, and daily/total energy. Addresses are passed directly to ESPHome; do not add `40001`.

The map comes from the community project [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), `SG0XLP1` configuration. This repository keeps only read sensors. Per-group source links are listed in [docs/SOURCES.md](docs/SOURCES.md). The community project is Apache-2.0 licensed; this independent YAML was authored from the documented map.

## Limitations

- Not affiliated with Deye, Waveshare, Amazon, or ESPHome.
- Physical testing on the specific `SUN-6K-SG05LP1-EU-AM2-P` unit is still required.
- Do not write registers without the exact official map and a backup of original settings.
- Amazon may change seller, price, or listing behind the short URL.

## License

MIT. See [LICENSE](LICENSE).
