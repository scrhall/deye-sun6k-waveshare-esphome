# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN

[English](../README.md) · [Fuentes](SOURCES.md)

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

> **Seguridad:** aislar el inversor antes de abrirlo. La fuente DIN recibe 100–240 V AC: el cableado de red debe quedar protegido y realizarlo personal cualificado. No usar `BMS 485/CAN`, `RS485/METER` ni puertos paralelos. El manual Deye marca Modbus como “Reserved”; la compatibilidad depende del firmware.

## Instalación

```bash
git clone https://github.com/scrhall/deye-sun6k-waveshare-esphome.git
cd deye-sun6k-waveshare-esphome
cp secrets.example.yaml secrets.yaml
```

Editar `secrets.yaml` y ejecutar:

```bash
esphome config deye-sun6k-waveshare.yaml
esphome run deye-sun6k-waveshare.yaml
```

Valores predeterminados: `9600 8N1`, esclavo `0x01`, función `03`, consulta cada 10 segundos. Cambiar `modbus_address` si no coincide con `Modbus SN`.

Probar primero:

- `Battery SOC`: registro `184`
- `Battery Voltage`: registro `183`, ×0,01 V

Sin respuesta: revisar puerto, `Modbus SN`, polaridad A/B, logs, LED RS485, cable corto y ausencia de otro cliente Modbus.

Verificar experimentalmente los signos de potencia de red y batería.

## Fuentes

- [Manual oficial Deye](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): puertos, `Modbus SN` y pinout en páginas impresas 3, 14, 44 y 53.
- Waveshare oficial: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [esquema](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- [Documentación oficial ESPHome](https://esphome.io/components/modbus_controller/).
- [Mapa comunitario Deye](https://github.com/Lewa-Reka/esphome-deye-inverter), configuración `SG0XLP1`.
- Procedencia detallada: [SOURCES.md](SOURCES.md).

Licencia MIT. Proyecto no afiliado a Deye, Waveshare, Amazon ni ESPHome.
