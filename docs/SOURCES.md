# Sources

Official sources support hardware, ports, pinout, and ESPHome syntax. Register addresses are community-sourced.

## Deye — official

[SG05LP1-EU-AM2-P manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf)

| Fact | Printed page |
|---|---:|
| Separate BMS, meter, and Modbus ports | 3 |
| Port purposes; Modbus marked “Reserved” | 14 |
| `Modbus SN` is the inverter address | 44 |
| BMS 485/CAN RJ45 pinout | 52 |
| Modbus RJ45 pinout | 53 |

Pinout: `1=B`, `2=A`, `3=GND`, `6=GND`, `7=A`, `8=B`; pins 4–5 unused.

LCD route verified against printed pages 30, 34, and 44: main screen gear icon → `Advanced Function` → right-side ↑/↓ arrows → `Paral. Set3`. `Modbus SN` is shown at the top of that screen.

Image `docs/assets/deye-modbus-rj45-pinout.png` is an unmodified crop from printed page 53 of the official Deye manual.

## Waveshare — official

- [Wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN): isolated RS485, power, terminals, termination.
- [Demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip): `WS_GPIO.h` defines `TXD1=GPIO17`, `RXD1=GPIO18`, and direction enable `TXD1EN=GPIO21`; `WS_RS485.cpp` handles half-duplex direction in software.
- [Schematic](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).

The schematic shows the single RS485 indicator (`LED2`) as bi-color: green channel on `TXD1`, blue channel on `RXD1`.

## ESPHome — official

[Modbus](https://esphome.io/components/modbus/) · [Controller](https://esphome.io/components/modbus_controller/) · [Sensor](https://esphome.io/components/sensor/modbus_controller/) · [UART](https://esphome.io/components/uart/)

## Registers — community

Source: [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), `SG0XLP1`.

Its board-specific Waveshare example also sets `modbus.flow_control_pin: GPIO21`. This repository runs a pinned, audited subset of release `0.14.0`: read entities remain active while writable `number`, `select`, `switch`, and `datetime` components and the API-disconnect Safe Mode script are commented out.

- [Battery](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/battery.yaml): 70–74, 182–184, 190–191.
- [Grid/CT](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/grid.yaml): 76–77, 81, 150, 169, 172.
- [PV](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/pv.yaml): 96, 108–112, 186–187.
- [Load](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/load.yaml): 84–85, 178, 192.
- [Inverter](https://github.com/Lewa-Reka/esphome-deye-inverter/blob/main/pv_inverter/packages/deye_hybrid_1p/inverter.yaml): 90–91, 175, 193.

No official Deye map for these low addresses was found. The read map, scaling, and transport were field-validated on one `SUN-6K-SG05LP1-EU-AM2-P` installation on 2026-07-21. Signed directions should still be checked for each installation. Current YAML performs reads only.

The inverter manual documents `Modbus SN` but does not expose a baud-rate/parity setting in its LCD instructions. The project's `9600 8N1` serial parameters came from the community SG0XLP1 configuration and were physically verified on the installation above.

Amazon purchase links: [Waveshare board](https://amzn.to/4fxuGVk) and [optional 12 V DIN power supply](https://amzn.to/4vEIxz0). Amazon listings are not used as primary technical sources.
