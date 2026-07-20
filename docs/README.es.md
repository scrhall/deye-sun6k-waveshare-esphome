# Deye SUN-6K + Waveshare ESP32-S3-RS485-CAN — ESPHome solo lectura

[English version](../README.md)

Configuración ESPHome específica para leer por **Modbus RTU/RS485** un inversor híbrido monofásico **Deye `SUN-6K-SG05LP1-EU-AM2-P`** usando la placa industrial aislada **Waveshare `ESP32-S3-RS485-CAN`**.

> Estado: compilación correcta con ESPHome 2026.6.5. Los pinouts de placa e inversor están respaldados por documentación oficial. El mapa de registros bajos es comunitario y debe verificarse físicamente en esta revisión concreta.

## Fuentes

Toda afirmación técnica relevante está trazada por documento y sección en **[Sources and traceability](SOURCES.md)**. Resumen:

- Deye oficial: [manual SG05LP1-EU-AM2-P 2025](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf), especialmente páginas impresas 3, 14, 44 y 53.
- Waveshare oficial: [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN), [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip) y [esquema](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf).
- ESPHome oficial: [Modbus Controller](https://esphome.io/components/modbus_controller/).
- Registros: [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), fuente comunitaria separada de la documentación oficial.

## Hardware

- Inversor: Deye `SUN-6K-SG05LP1-EU-AM2-P`.
- Interfaz: Waveshare `ESP32-S3-RS485-CAN`, ESP32-S3R8, RS485 aislado y conmutación automática.
- [Comprar la placa en Amazon](https://amzn.to/4fxuGVk).
- [Wiki oficial Waveshare](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN).
- [Producto oficial Waveshare](https://www.waveshare.com/esp32-s3-rs485-can.htm).
- [Manual oficial Deye](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf); pinout Modbus en página impresa 53.

## Seguridad y alcance

Configuración **solo lectura a nivel ESPHome**:

- Solo define sensores `modbus_controller` sobre `holding registers`.
- No define `number`, `select`, `switch`, `button` ni acciones de escritura.
- No reutiliza el paquete comunitario completo porque incluye controles que escriben registros.

ESPHome sigue actuando como cliente Modbus y transmite peticiones de lectura función `03`. “Solo lectura” no significa silencio eléctrico.

**Riesgo eléctrico:** apagar y aislar el inversor según su manual antes de abrir el compartimento inferior. Usar instalador cualificado cuando corresponda. No conectar al puerto `BMS 485/CAN`, `RS485/METER`, `Parallel 1` ni `Parallel 2`.

## Cableado

Usar el RJ45 interior marcado **`Modbus`**. Fuente: [manual oficial Deye, páginas impresas 3, 14 y 53](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf). El mismo manual llama al puerto “Reserved”; la compatibilidad real depende del firmware.

| Inversor, RJ45 Modbus | Waveshare RS485 |
|---|---|
| Pin 1 — `sunspe-485_B` | B- |
| Pin 2 — `sunspe-485_A` | A+ |
| Pin 3 — `GND_sunspe-485` | **No conectar**; el borne RS485 aislado no expone GND |

Par duplicado del inversor: pin 8 a B-, pin 7 a A+. No conectar ambos pares simultáneamente.

Alimentar la Waveshare por USB-C 5 V o bornes DC 7–36 V. **No alimentarla desde el RJ45 del inversor.**

La terminación de 120 Ω viene desactivada. Dejarla así para una prueba inicial con cable corto. En bus largo o ruidoso, evaluar terminación en extremos sin duplicarla si el inversor ya termina la línea.

## Parámetros Waveshare confirmados

- TX RS485: `GPIO17`.
- RX RS485: `GPIO18`.
- Dirección: automática por hardware; sin `flow_control_pin`.
- RS485 aislado con protección TVS, sobretensión y ESD.

Fuentes oficiales Waveshare: [demo](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Demo.zip), [esquema](https://files.waveshare.com/wiki/ESP32-S3-RS485-CAN/ESP32-S3-RS485-CAN-Schematic.pdf) y [wiki](https://www.waveshare.com/wiki/ESP32-S3-RS485-CAN).

## Instalación

1. Instalar ESPHome o usar su add-on en Home Assistant.
2. Clonar este repositorio.
3. Copiar secretos: `cp secrets.example.yaml secrets.yaml`.
4. Completar Wi-Fi y generar credenciales con `openssl rand -base64 32` y `openssl rand -hex 32`.
5. Validar: `esphome config deye-sun6k-waveshare.yaml`.
6. Compilar: `esphome compile deye-sun6k-waveshare.yaml`.
7. Primera carga USB-C: `esphome run deye-sun6k-waveshare.yaml`.
8. Añadirlo a Home Assistant y asignarlo al área adecuada.

## Primera prueba

Valores predeterminados: Modbus RTU `9600 8N1`, esclavo `0x01`, intervalo 10 s, holding registers y función `03`.

Comprobar primero `Battery SOC` (184) y `Battery Voltage` (183, ×0,01 V).

Sin respuesta: confirmar puerto `Modbus`, `Modbus SN`, cableado A/B, logs y LED RS485, ausencia de otro maestro, cable corto y compatibilidad del firmware.

## Signos y limitaciones

Los registros de potencia de red y batería son `S_WORD`. Verificar signos observando importación/exportación y carga/descarga. El YAML no invierte signos sin prueba.

El mapa procede de [Lewa-Reka/esphome-deye-inverter](https://github.com/Lewa-Reka/esphome-deye-inverter), configuración comunitaria `SG0XLP1`; enlaces por grupo en [SOURCES.md](SOURCES.md). No se ha localizado mapa oficial Deye para estos registros bajos.

Proyecto no afiliado a Deye, Waveshare, Amazon ni ESPHome. Pendiente de prueba física en la unidad concreta. No escribir registros sin mapa oficial exacto y copia de ajustes.

## Licencia

MIT. Consulta [LICENSE](../LICENSE).
