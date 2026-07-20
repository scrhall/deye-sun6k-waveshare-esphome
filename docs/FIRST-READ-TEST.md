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

1. Confirm on `Paral. Set3` that `Modbus SN` is exactly `01`; otherwise set `modbus_address` to the displayed value.
2. Confirm the RJ45 is labelled `Modbus`, not `BMS 485/CAN` or `RS485/METER`.
3. Watch the Waveshare TX/RX indicators during a poll. TX without RX confirms no electrical reply.
4. If `Modbus SN=01` and only TX occurs: isolate power, swap only A+ and B-, restore power, and retest. Change nothing else.
5. If RX remains absent, restore original polarity, use the shortest cable, and keep 120 Ω termination disabled.
6. Confirm no other Modbus master/client is connected.
7. If the correct address and both polarities produce TX without RX on the dedicated port, the leading hypothesis is that this firmware does not enable the manual's reserved `Modbus` port. Do not attempt writes.

Stop immediately if the inverter reports a BMS/CAN alarm. Restore the original battery cable and disconnect the ESP branch.
