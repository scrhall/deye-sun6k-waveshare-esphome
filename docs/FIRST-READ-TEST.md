# First read test: registers 184 and 183

[Español](FIRST-READ-TEST.es.md)

Use [`deye-sun6k-waveshare-test.yaml`](../deye-sun6k-waveshare-test.yaml). It contains only two function-03 holding-register sensors and no writes.

## Prepare

1. Confirm inverter `Modbus SN` and set `modbus_address` to the same value; default is `01` / `0x01`.
2. Prefer the dedicated inverter `Modbus` port. If using the experimental BMS breakout, first verify normal battery communication with the ESP branch disconnected.
3. Use a short A+/B- cable. Ensure no other Modbus client is connected.
4. In ESPHome Device Builder, create a test device, open **EDIT**, paste the test YAML, complete **SECRETS**, then **Validate** and **Install** over USB-C.

## Read

1. Open the device's **LOGS** in ESPHome Dashboard.
2. Connect A+ and B- with equipment safely isolated, then restore power.
3. Wait 20–30 seconds: the controller polls every 10 seconds.
4. Check Home Assistant or logs for:
   - `Battery SOC Test` — register `184`, expected to match the inverter SOC display.
   - `Battery Voltage Test` — register `183`, raw value multiplied by `0.01 V`, expected to be close to the inverter/BMS voltage display.
5. Observe at least three updates. Values should be stable and plausible, not `unknown`, unavailable, zero unexpectedly, or rapidly changing.

## No response

`Stop waiting for response from 1` means the ESP sent a request to slave 1 and received no valid frame. `Duplicate modbus command ... address=183 count=2` is a consequence: ESPHome combines adjacent registers 183/184 into one read and schedules it again while the prior request remains unanswered; it does not indicate duplicate sensors.

With the updated test YAML, `VERY_VERBOSE` logs should show request `01 03 00 B7 00 02 74 2D`. Look for an RX line immediately after it. TX without RX isolates the failure before register decoding: port, address, polarity, wiring, or a firmware-disabled port.

Change one thing at a time:

1. Confirm `modbus.flow_control_pin` is `GPIO21`. Without it, the board logs TX but does not correctly switch the RS485 transceiver for reception.
2. Confirm on `Paral. Set3` that `Modbus SN` is exactly `01`; otherwise set `modbus_address` to the displayed value.
3. Confirm the RJ45 is labelled `Modbus`, not `BMS 485/CAN` or `RS485/METER`.
4. Watch the Waveshare's single bi-color RS485 LED during a poll. The official schematic maps **green=TX** and **blue=RX**. Periodic green without blue confirms transmission with no electrical reply.
5. If `Modbus SN=01` and only TX occurs: isolate power, swap only A+ and B-, restore power, and retest. Change nothing else.
6. If RX remains absent, restore original polarity, use the shortest cable, and keep 120 Ω termination disabled.
7. Confirm no other Modbus master/client is connected.
8. Only after confirming GPIO21, address, and both polarities should a disabled port be considered. Do not attempt writes.

Stop immediately if the inverter reports a BMS/CAN alarm. Restore the original battery cable and disconnect the ESP branch.

## Dedicated-port SunSpec test

The official pinout labels this port `SunSpec`. Firmware may ignore proprietary registers 183/184 while answering only the standard map.

1. Install [`deye-sun6k-sunspec-test.yaml`](../deye-sun6k-sunspec-test.yaml), keeping address `0x01` and the verified wiring. The YAML preserves `device_name: deye-sun6k-rs485`; do not change the hostname between tests because Dashboard/API discovery may lose the node after reboot.
2. The first request must be `01 03 9C 40 00 02 EB 8F`: function 03, two registers from 40000.
3. A valid signature returns `0x5375 0x6E53`, displayed as `21365` and `28243`: ASCII `SunS`.
4. Any reply, including a Modbus exception or different values, proves the port, address, baud rate, and polarity work.
5. If 40000 does not reply, edit only `sunspec_base_address`: test `0`, then `50000`, the alternative bases scanned by the official SunSpec client.
6. If no base produces RX, stop changing registers: the fault remains transport, firmware, or a disabled port.
