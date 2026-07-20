# Primera prueba: registros 184 y 183

[English](FIRST-READ-TEST.md)

Usar [`deye-sun6k-waveshare-test.yaml`](../deye-sun6k-waveshare-test.yaml). Solo contiene dos sensores holding register por función 03 y ninguna escritura.

## Preparación

1. Comprobar `Modbus SN` y poner el mismo valor en `modbus_address`; por defecto `01` / `0x01`.
2. Preferir el puerto dedicado `Modbus`. Con breakout BMS experimental, comprobar primero la comunicación normal de batería con el ramal ESP desconectado.
3. Usar cable A+/B- corto y sin otro cliente Modbus conectado.
4. En ESPHome Device Builder, crear un dispositivo de prueba, abrir **EDIT**, pegar el YAML de prueba, completar **SECRETS**, pulsar **Validate** e **Install** por USB-C.

## Lectura

1. Abrir **LOGS** del dispositivo en ESPHome Dashboard.
2. Con el equipo aislado, conectar A+ y B-; después restaurar alimentación.
3. Esperar 20–30 segundos: consulta cada 10 segundos.
4. Revisar en Home Assistant o logs:
   - `Battery SOC Test`: registro `184`; debe coincidir con el SOC mostrado por el inversor.
   - `Battery Voltage Test`: registro `183`, multiplicado por `0,01 V`; debe aproximarse al voltaje mostrado por inversor/BMS.
5. Observar al menos tres actualizaciones. Deben ser estables y razonables, no `unknown`, no disponible, cero inesperado ni cambios bruscos.

## Sin respuesta

Cambiar una sola cosa cada vez:

1. Confirmar otra vez `Modbus SN`.
2. Revisar LED TX/RX de Waveshare. TX sin RX suele indicar ausencia de respuesta.
3. Aislar alimentación, intercambiar A+ y B- y repetir.
4. Usar cable mínimo y dejar inicialmente desactivada la terminación de 120 Ω.
5. Confirmar que solo existe un cliente Modbus.
6. Volver al puerto dedicado `Modbus`. Si el breakout BMS falla pero CAN sigue correcto, asumir que ese RS485 BMS no expone la telemetría requerida.

Parar inmediatamente ante alarma BMS/CAN. Restaurar el cable original y desconectar el ramal ESP.
