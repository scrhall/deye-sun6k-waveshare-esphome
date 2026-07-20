# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN

[English](../README.md) · [Fuentes](SOURCES.md)

> [!WARNING]
> **Contenido generado por una IA y pendiente de revisión.** La documentación y la configuración aún no han completado revisión humana ni prueba física. Quien use, modifique, cablee, flashee u opere este proyecto lo hace bajo su exclusiva responsabilidad. No se acepta responsabilidad por daños, pérdida de datos, lesiones o funcionamiento incorrecto.

Lector ESPHome Modbus RTU para:

- Deye `SUN-6K-SG05LP1-EU-AM2-P`
- Waveshare `ESP32-S3-RS485-CAN`
- [Comprar la placa en Amazon](https://amzn.to/4fxuGVk)
- [Fuente opcional DIN 12 V DC, 1,25 A y 15 W](https://amzn.to/4vEIxz0)

El YAML actual es **solo lectura**: 31 sensores, sin entidades ni comandos de escritura. Compilado con ESPHome 2026.6.5. El mapa de registros es comunitario y requiere prueba física.

## Cableado

Usar solo el RJ45 del inversor marcado **`Modbus`**.

| RJ45 Modbus Deye | Waveshare |
|---|---|
| Pin 1 — B | B- |
| Pin 2 — A | A+ |
| Pin 3 — GND | No conectar |

Par alternativo: pin 8 → B-, pin 7 → A+. No usar ambos pares.

Alimentar Waveshare por USB-C 5 V o DC 7–36 V. Para montaje DIN, la fuente enlazada puede alimentar la entrada DC de la placa respetando polaridad `+`/`-`. No alimentarla desde el RJ45.

UART: TX `GPIO17`, RX `GPIO18`; dirección automática, sin `flow_control_pin`. Mantener desactivado el jumper de 120 Ω en la prueba inicial con cable corto.

> **Seguridad:** aislar el inversor antes de abrirlo. La fuente DIN recibe 100–240 V AC: el cableado de red debe quedar protegido y realizarlo personal cualificado. No usar `RS485/METER` ni puertos paralelos. Compartir `BMS 485/CAN` solo siguiendo el [procedimiento experimental](SHARED-BMS-RJ45-CABLE.es.md). El manual Deye marca el puerto Modbus dedicado como “Reserved”; la compatibilidad depende del firmware.

## Instalación

1. En Home Assistant, instalar/iniciar **ESPHome Device Builder** y abrir su interfaz web.
2. Elegir **New Device Setup**, introducir el Wi-Fi y terminar el asistente. Antes de sustituir su YAML, copiar la clave de cifrado API y la contraseña OTA generadas.
3. Abrir **EDIT**. Sustituir el YAML por el contenido de [`deye-sun6k-waveshare.yaml`](https://raw.githubusercontent.com/scrhall/deye-sun6k-waveshare-esphome/main/deye-sun6k-waveshare.yaml) y guardar.
4. Abrir el editor **SECRETS** del Dashboard. Añadir las cinco claves de [`secrets.example.yaml`](https://github.com/scrhall/deye-sun6k-waveshare-esphome/blob/main/secrets.example.yaml), usando el Wi-Fi y las credenciales generadas por el asistente.
5. En el menú del dispositivo, pulsar **Validate** y después **Install**. Conectar la placa por USB-C para la primera carga; las siguientes pueden hacerse por Wi-Fi.

Valores predeterminados: `9600 8N1`, esclavo `0x01`, función `03`, consulta cada 10 segundos. Cambiar `modbus_address` si no coincide con `Modbus SN`.

### Comprobar `Modbus SN` en el inversor

1. En la pantalla principal, pulsar el **engranaje** superior derecho.
2. Pulsar **`Advanced Function`**.
3. Usar las flechas laterales **↑/↓** hasta ver **`Paral. Set3`**.
4. Leer **`Modbus SN`** en la parte superior. Debe mostrar `01` para el valor predeterminado `0x01`; si muestra otro número, cambiar `modbus_address` al valor mostrado.

Para consultar no hay que guardar: no cambiar campos ni pulsar la confirmación verde. El manual oficial no muestra contraseña para visualizar esta pantalla; el firmware puede variar.

Primera prueba: importar [`deye-sun6k-waveshare-test.yaml`](../deye-sun6k-waveshare-test.yaml), que solo lee SOC `184` y voltaje `183` (×0,01 V). Seguir la [prueba paso a paso](FIRST-READ-TEST.es.md).

Verificar experimentalmente los signos de potencia de red y batería.

## Fuentes

- [Manual oficial Deye](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): puertos, `Modbus SN` y pinout en páginas impresas 3, 14, 44 y 53.
- Waveshare oficial: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [esquema](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- [Documentación oficial ESPHome](https://esphome.io/components/modbus_controller/).
- [Guía oficial ESPHome Device Builder](https://esphome.io/guides/getting_started_hassio/).
- [Mapa comunitario Deye](https://github.com/Lewa-Reka/esphome-deye-inverter), configuración `SG0XLP1`.
- Procedencia detallada: [SOURCES.md](SOURCES.md).

Licencia MIT. Proyecto no afiliado a Deye, Waveshare, Amazon ni ESPHome.
