# Experimental shared BMS RJ45 breakout cable

[Español](SHARED-BMS-RJ45-CABLE.es.md)

> [!CAUTION]
> Prefer the dedicated inverter **`Modbus`** port. Deye documents `BMS 485/CAN` as a **battery communication** port, not as a telemetry Modbus port. Its RS485 pins may use a battery protocol and may not answer registers 183/184. This breakout is experimental and must not be used unless a read-only test confirms the expected Modbus response without affecting BMS communication.

## Never use this when

- The battery communicates with the inverter over RS485 instead of CAN.
- The exact inverter/battery pinout or active protocol is unknown.
- Battery alarms or BMS communication errors appear.
- A generic passive Ethernet splitter is the only available part. It parallels all eight conductors and can join two transceivers unintentionally.

## Inverter BMS port pinout

Official Deye manual, Appendix I, printed page 52:

| Pin | Signal |
|---:|---|
| 1 | `485_B` |
| 2 | `485_A` |
| 3 | `GND_485` |
| 4 | `CAN-H` |
| 5 | `CAN-L` |
| 6 | `GND_485` |
| 7 | `485_A` |
| 8 | `485_B` |

The manual shows the socket face-on, latch notch down, contacts at the top: pins 1→8 run left to right. Avoid relying on Ethernet wire colors; use numbered RJ45 breakout boards and verify every pin with a continuity tester.

## Intended breakout

Only for a SE-F16 already verified to communicate over CAN on PCS pins 4/5:

```text
Inverter BMS RJ45                   Battery SE-F16 PCS
pin 4  CAN-H  --------------------  pin 4  CAN-H
pin 5  CAN-L  --------------------  pin 5  CAN-L

Inverter BMS RJ45                   Waveshare isolated RS485
pin 1  485_B  --------------------  B-
pin 2  485_A  --------------------  A+
```

- Do not connect inverter pins 3/6 to Waveshare: its isolated RS485 terminal exposes only A+/B-.
- Leave duplicate RS485 pins 7/8 unused. Do not use both RS485 pairs.
- Preserve any CAN reference/ground conductor required by the exact battery revision and original cable. Confirm against that battery's manual and a continuity test; do not guess.
- Keep the battery CAN branch straight-through and short. Keep the RS485 branch short for the first test.

## Parts

- One labelled RJ45 male breakout or short patch lead to the inverter.
- One labelled RJ45 female breakout for the battery cable.
- A+/B- twisted pair to Waveshare.
- Multimeter with continuity mode, insulated enclosure, strain relief, and labels.

Do not use a crimped Y cable until the breakout version has passed every test.

## Build and verify

1. Shut down and isolate inverter, battery, and ESP supply according to their manuals.
2. Photograph and label every connector. Confirm the battery is configured for CAN.
3. Map the original working battery cable pin by pin with continuity mode.
4. Build the CAN path first. Check pin 4→4 and 5→5; confirm no short between them or to any other pin.
5. Add only inverter pin 1→Waveshare B- and pin 2→Waveshare A+.
6. Check all eight inverter pins against every output. Resistance between unrelated pins must be open; never use continuity mode on energized equipment.
7. Reconnect the battery branch **without ESP connected**. Start the system and confirm normal battery SOC, voltage, and no BMS alarm.
8. Power the ESP separately, then connect A+/B-. Run the [two-register read test](FIRST-READ-TEST.md).
9. If Modbus does not answer, disconnect the ESP branch. Do not assume another baud rate or write registers.

## Abort immediately

Disconnect the ESP branch if SOC disappears, the inverter reports BMS/CAN faults, charging behavior changes, either transceiver becomes hot, or readings are unstable. Restore the original battery cable before further diagnosis.

## Sources

- [Official Deye inverter manual](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): port purpose on printed page 14; BMS RJ45 pinout on printed page 52.
- [Official SE-F16 manual V06](https://deyeess.com/wp-content/uploads/2025/12/Deye-ESS-User-Manual-SE-F16-EU-EN-V06.pdf): verify the PCS pinout for the exact battery revision before building. The official server returned HTTP 403 during this document's review, so its pinout was not independently revalidated here.
