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

Change one thing at a time:

1. Confirm `Modbus SN` again.
2. Check Waveshare TX/RX indicators. TX activity without RX suggests no reply.
3. Isolate power, swap A+ and B-, then retest.
4. Use the shortest practical cable and keep 120 Ω termination disabled initially.
5. Confirm only one Modbus client is connected.
6. Return to the dedicated `Modbus` port. If the BMS-port breakout fails but battery CAN remains healthy, assume that BMS RS485 does not expose the required telemetry protocol.

Stop immediately if the inverter reports a BMS/CAN alarm. Restore the original battery cable and disconnect the ESP branch.
