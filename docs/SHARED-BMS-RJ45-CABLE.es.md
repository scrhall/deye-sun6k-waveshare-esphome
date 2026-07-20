# Cable breakout experimental para compartir el RJ45 BMS

[English](SHARED-BMS-RJ45-CABLE.md)

> [!CAUTION]
> Preferir el puerto dedicado **`Modbus`**. Deye documenta `BMS 485/CAN` como puerto de **comunicación con la batería**, no como puerto Modbus de telemetría. Sus pines RS485 pueden usar un protocolo BMS y no responder a los registros 183/184. Este breakout es experimental: solo usarlo si una prueba de lectura confirma Modbus sin afectar al BMS.

## No usar cuando

- La batería comunica con el inversor por RS485 en vez de CAN.
- No se conoce el pinout o protocolo exacto.
- Aparecen alarmas de batería o comunicación BMS.
- Solo se dispone de un divisor Ethernet pasivo: conecta en paralelo los ocho hilos y puede unir transceptores involuntariamente.

## Pinout BMS del inversor

Manual oficial Deye, apéndice I, página impresa 52:

| Pin | Señal |
|---:|---|
| 1 | `485_B` |
| 2 | `485_A` |
| 3 | `GND_485` |
| 4 | `CAN-H` |
| 5 | `CAN-L` |
| 6 | `GND_485` |
| 7 | `485_A` |
| 8 | `485_B` |

El manual muestra el conector hembra de frente, pestaña abajo y contactos arriba: los pines 1→8 van de izquierda a derecha. No confiar en colores Ethernet; usar breakouts RJ45 numerados y comprobar cada pin con multímetro.

## Reparto previsto

Solo para una SE-F16 ya comprobada comunicando por CAN mediante PCS 4/5:

```text
RJ45 BMS del inversor                PCS de batería SE-F16
pin 4  CAN-H  --------------------  pin 4  CAN-H
pin 5  CAN-L  --------------------  pin 5  CAN-L

RJ45 BMS del inversor                RS485 aislado Waveshare
pin 1  485_B  --------------------  B-
pin 2  485_A  --------------------  A+
```

- No conectar pines 3/6 del inversor a Waveshare: su borne RS485 aislado solo expone A+/B-.
- Dejar sin usar los pines RS485 duplicados 7/8. No usar ambos pares.
- Conservar cualquier referencia/masa CAN exigida por la revisión exacta de la batería y el cable original. Confirmarlo con su manual y continuidad; no adivinar.
- Mantener recto y corto el ramal CAN. Empezar también con ramal RS485 corto.

## Material

- Breakout RJ45 macho etiquetado o latiguillo corto hacia el inversor.
- Breakout RJ45 hembra etiquetado para el cable de batería.
- Par trenzado A+/B- hacia Waveshare.
- Multímetro con continuidad, caja aislante, alivio de tensión y etiquetas.

No crimpar un cable en Y definitivo hasta validar la versión con breakouts.

## Montaje y comprobación

1. Apagar y aislar inversor, batería y fuente del ESP según sus manuales.
2. Fotografiar y etiquetar conectores. Confirmar que la batería está configurada en CAN.
3. Mapear pin a pin el cable original funcional con continuidad.
4. Montar primero CAN: comprobar 4→4 y 5→5, sin cortos entre ellos ni con otros pines.
5. Añadir únicamente pin 1 del inversor→B- y pin 2→A+ de Waveshare.
6. Comprobar los ocho pines contra todas las salidas. Los pines no relacionados deben quedar abiertos. Nunca medir continuidad con tensión.
7. Conectar la batería **sin el ESP**. Arrancar y confirmar SOC, voltaje y ausencia de alarma BMS.
8. Alimentar el ESP por separado, conectar A+/B- y ejecutar la [prueba de dos registros](FIRST-READ-TEST.es.md).
9. Si Modbus no responde, desconectar el ramal ESP. No probar escrituras ni asumir otro baud rate.

## Abortar inmediatamente

Desconectar el ESP si desaparece el SOC, aparece fallo BMS/CAN, cambia la carga, se calienta un transceptor o las lecturas son inestables. Restaurar el cable original antes de seguir diagnosticando.

## Fuentes

- [Manual oficial del inversor Deye](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): finalidad del puerto en página impresa 14; pinout BMS RJ45 en página 52.
- [Manual oficial SE-F16 V06](https://deyeess.com/wp-content/uploads/2025/12/Deye-ESS-User-Manual-SE-F16-EU-EN-V06.pdf): comprobar el pinout PCS de la revisión exacta antes de montar. El servidor oficial devolvió HTTP 403 durante esta revisión, por lo que aquí no se revalidó independientemente ese pinout.
