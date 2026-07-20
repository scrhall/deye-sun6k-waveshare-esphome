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

`Stop waiting for response from 1` significa que el ESP envió una petición al esclavo 1 y no recibió una trama válida. `Duplicate modbus command ... address=183 count=2` es una consecuencia: ESPHome agrupa los registros contiguos 183/184 en una lectura y vuelve a programarla mientras la anterior sigue sin respuesta; no indica sensores duplicados.

Con el YAML de prueba actualizado, el log `VERY_VERBOSE` debe mostrar la petición `01 03 00 B7 00 02 74 2D`. Buscar después una línea RX. Si solo aparece TX, el fallo está antes de interpretar registros: puerto, dirección, polaridad, cableado o puerto deshabilitado por firmware.

Cambiar una sola cosa cada vez:

1. Confirmar en `Paral. Set3` que `Modbus SN` muestra exactamente `01`; si no, cambiar `modbus_address` al valor real.
2. Confirmar que el RJ45 es el puerto rotulado `Modbus`, no `BMS 485/CAN` ni `RS485/METER`.
3. Revisar LED TX/RX de Waveshare durante una consulta. TX sin RX confirma ausencia eléctrica de respuesta.
4. Si `Modbus SN=01` y solo hay TX: aislar alimentación, intercambiar únicamente A+ y B-, restaurar alimentación y repetir. No cambiar nada más en esta prueba.
5. Si sigue sin RX, restaurar la polaridad original, usar cable mínimo y dejar desactivada la terminación de 120 Ω.
6. Confirmar que no existe otro maestro/cliente Modbus conectado.
7. Si dirección y ambas polaridades producen TX sin RX en el puerto dedicado, la hipótesis principal pasa a ser que el puerto `Modbus` marcado como reservado no está habilitado por ese firmware. No probar escrituras.

Parar inmediatamente ante alarma BMS/CAN. Restaurar el cable original y desconectar el ramal ESP.
