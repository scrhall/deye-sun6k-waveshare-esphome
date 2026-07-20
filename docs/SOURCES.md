# Sources and traceability

This page separates official documentation from community sources. Last checked: July 20, 2026.

## 1. Inverter and Modbus port — official Deye source

Document: **Deye User Manual `SUN-3.6/5/6/7/7.6/8/10K-SG05LP1-EU-AM2-P`**, 2025 English edition.

- [Official PDF](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf)
- [Official Deye manual download area](https://www.deyeinverter.com/download/product-manual/)

| Used fact | Manual location |
|---|---|
| `SUN-(3.6-6)K-SG05LP1-EU-AM2-P` has separate `BMS 485/CAN`, `RS 485/METER`, and `Modbus` ports | Printed page 3; PDF page 5, “2.1 Product Overview and Size” |
| `BMS 485/CAN` is for battery communication; `RS 485/METER` is for a meter; `Modbus` is marked “Reserved” | Printed page 14; PDF page 16, “3.4.2 Function port definition” |
| `Modbus SN` is each inverter's Modbus address | Printed page 44; PDF page 46, “Advanced Function / Paral. Set3” screen |
| Modbus RJ45 pinout | Printed page 53; PDF page 55, “Definition of RJ45 Port Pin for Modbus” |

Pinout transcribed from printed page 53:

| Pin | Official signal |
|---:|---|
| 1 | `sunspe-485_B` |
| 2 | `sunspe-485_A` |
| 3 | `GND_sunspe-485` |
| 4 | `--` |
| 5 | `--` |
| 6 | `GND_sunspe-485` |
| 7 | `sunspe-485_A` |
| 8 | `sunspe-485_B` |

The manual identifies the physical port and pinout while also calling it “Reserved”. This guide therefore treats proprietary-map access as an experiment dependent on firmware and hardware revision; it does not claim official Deye support for the low-address registers.

## 2. Board — official Waveshare sources

- [Official `ESP32-S3-RS485-CAN` wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN)
- [Official product page](https://www.waveshare.com/esp32-s3-rs485-can.htm)
- [Official demo archive](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip)
- [Official schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf)

| Used fact | Exact source |
|---|---|
| Model, isolated RS485, USB-C 5 V or 7–36 V DC power, reserved 120 Ω termination disabled by default | Official wiki, “Specifications”, “Onboard Resources”, and “Interfaces” |
| RS485 terminals `A+` / `B-`, with no GND on the isolated terminal block | Official wiki, “Interfaces” |
| RS485 TX `GPIO17`, RX `GPIO18` | Official demo: `Arduino/examples/MAIN_WIFI_AP/WS_GPIO.h` and `MAIN_WIFI_STA/WS_GPIO.h` |
| Automatic direction control | Official wiki, “Isolated RS485 communication Interface → Direction control”; official demo `WS_RS485.cpp` uses `UART_MODE_RS485_HALF_DUPLEX` without an external DE/RE pin |

## 3. ESPHome — official documentation

- [Modbus component](https://esphome.io/components/modbus/)
- [Modbus Controller](https://esphome.io/components/modbus_controller/)
- [Modbus Controller Sensor](https://esphome.io/components/sensor/modbus_controller/)
- [UART](https://esphome.io/components/uart/)
- [ESP32 platform](https://esphome.io/components/esp32/)

These sources support the YAML syntax for `uart`, `modbus`, `modbus_controller`, `register_type: holding`, value types, filters, and sensors.

## 4. Register map — community source, not official

Project: [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), `SG0XLP1` configuration:

- [Main `pv-inverter.Deye-SG0XLP1.yaml`](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv-inverter.Deye-SG0XLP1.yaml)
- [Battery: 70, 71, 72, 74, 182, 183, 184, 190, 191](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/battery.yaml)
- [Grid/CT: 76, 77, 81, 150, 169, 172](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/grid.yaml)
- [PV: 96, 108–112, 186, 187](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/pv.yaml)
- [Load: 84, 85, 178, 192](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/load.yaml)
- [Inverter: 90, 91, 175, 193](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/inverter.yaml)
- [Community project Apache-2.0 license](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/LICENSE)

No official Deye map for these low registers was found in the consulted official sources. Therefore:

1. The YAML does not present these registers as official.
2. Only reads are implemented.
3. Signs, scaling, and compatibility must be compared with values shown by the inverter.
4. If this revision exposes only standard SunSpec models, the community proprietary map may not work.

## 5. Purchase

- [Amazon listing](https://amzn.to/4fxuGVk) — redirected when checked to ASIN `B0FN4LWLH9`, Waveshare `ESP32-S3-RS485-CAN`.

Amazon is used only as a purchase link. Technical specifications and pinouts come from official Waveshare documentation, not seller copy.
