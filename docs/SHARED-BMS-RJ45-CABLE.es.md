# Cable breakout experimental para compartir el RJ45 BMS

[English](SHARED-BMS-RJ45-CABLE.md)

> [!CAUTION]
> Preferir el puerto dedicado **`Modbus`**. Deye documenta `BMS 485/CAN` como puerto de **comunicación con la batería**, no como puerto Modbus de telemetría. Sus pines RS485 pueden usar un protocolo BMS y no responder a los registros 183/184. Este breakout es experimental: solo usarlo si una prueba de lectura confirma Modbus sin afectar al BMS.

![Definición oficial de los puertos de comunicación Deye](assets/deye-function-port-definitions.png)

*Recorte del manual oficial Deye, página impresa 14: `BMS 485/CAN` para batería y `Modbus` reservado.*

## No usar cuando

- La batería comunica con el inversor por RS485 en vez de CAN.
- No se conoce el pinout o protocolo exacto.
- Aparecen alarmas de batería o comunicación BMS.
- Solo se dispone de un divisor Ethernet pasivo: conecta en paralelo los ocho hilos y puede unir transceptores involuntariamente.

## Pinout BMS del inversor

Manual oficial Deye, apéndice I, página impresa 52:

![Pinout oficial Deye BMS 485/CAN](assets/deye-bms-rj45-pinout.png)

*Recorte sin modificar del manual oficial: tabla completa y orientación del conector.*

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

## Construcción propuesta

El cable BMS original queda intacto. Se intercala una extensión macho–macho propia y un acoplador RJ45 hembra–hembra recto:

```text
Inversor, BMS RJ45 hembra
          │
          └── macho A ── extensión propia ── macho B
                 │                           │
                 │                           └── acoplador RJ45 hembra-hembra recto
                 │                                      │
                 │                                      └── cable BMS original ── batería PCS
                 │
                 ├── pin 1, 485_B ──→ Waveshare B-
                 └── pin 2, 485_A ──→ Waveshare A+
```

Para una SE-F16 ya comprobada comunicando por CAN mediante PCS 4/5, este es el mapeo completo. Los colores solo son referencia si ambos latiguillos son realmente T568B; manda siempre el número comprobado con multímetro.

| Pin | Color T568B | Macho A, inversor | Unión hacia macho B | Derivación lateral |
|---:|---|---|---|---|
| 1 | blanco/naranja | `485_B` | **No conectar** | Waveshare `B-` |
| 2 | naranja | `485_A` | **No conectar** | Waveshare `A+` |
| 3 | blanco/verde | `GND_485` | **No conectar** | Ninguna |
| 4 | azul | `CAN-H` | **Pin 4→pin 4, recto** | Ninguna |
| 5 | blanco/azul | `CAN-L` | **Pin 5→pin 5, recto** | Ninguna |
| 6 | verde | `GND_485` | **No conectar** | Ninguna |
| 7 | blanco/marrón | `485_A` | **No conectar** | Ninguna |
| 8 | marrón | `485_B` | **No conectar** | Ninguna |

Por tanto, **no hay cruces**. La derivación RS485 sale únicamente del macho A. Pines 1/2 no continúan al macho B, acoplador ni cable BMS original.

El acoplador hembra–hembra sí debe ser totalmente recto:

```text
1→1  2→2  3→3  4→4  5→5  6→6  7→7  8→8
```

Aunque el acoplador conserve los ocho pines, el macho B solo recibe señal útil en 4/5; 1/2/3/6/7/8 llegan abiertos desde la extensión.

- No conectar pines 3/6 del inversor a Waveshare: su borne RS485 aislado solo expone A+/B-.
- Dejar sin usar los pines RS485 duplicados 7/8. No usar ambos pares.
- El acoplador hembra–hembra debe ser recto, no cruzado; verificar 1→1, 2→2… 8→8 con continuidad.
- Conservar en la extensión cualquier referencia/masa CAN exigida por la revisión exacta de la batería y el cable original. Confirmarlo con su manual y continuidad; no adivinar.
- La extensión no es un latiguillo Ethernet completo: no llevar 1/2/7/8 hasta el lado batería. Pasar solo CAN 4/5 y cualquier referencia adicional previamente verificada.
- Mantener recto y corto el ramal CAN. Empezar también con ramal RS485 corto.

## Material

- Extensión propia con dos RJ45 macho: **macho A** hacia inversor y **macho B** hacia acoplador.
- Acoplador RJ45 hembra–hembra 8P8C recto.
- Cable BMS original, sin cortar ni modificar.
- Par trenzado A+/B- hacia Waveshare.
- Caja de derivación aislante junto al macho A, multímetro, alivio de tensión y etiquetas.

No crimpar un cable en Y definitivo hasta validar la versión con breakouts.

### Forma sencilla con un latiguillo T568B

1. Usar un cable macho–macho recto T568B y cortarlo por el centro: una mitad será macho A y otra macho B.
2. Introducir ambos extremos cortados en una caja con bornes.
3. Unir azul A↔azul B (pin 4) y blanco/azul A↔blanco/azul B (pin 5).
4. Llevar blanco/naranja del macho A (pin 1) a `B-` y naranja del macho A (pin 2) a `A+`.
5. Aislar individualmente todos los demás hilos de ambos lados. No unirlos entre sí.
6. Verificar por número de pin; si los colores no coinciden exactamente con T568B, ignorarlos y mapear con continuidad.

## Montaje y comprobación

1. Apagar y aislar inversor, batería y fuente del ESP según sus manuales.
2. Fotografiar y etiquetar conectores. Confirmar que la batería está configurada en CAN.
3. Mapear pin a pin el cable BMS original y el acoplador hembra–hembra con continuidad.
4. Construir la extensión macho A→macho B. Pasar 4→4 y 5→5; añadir solo cualquier referencia CAN confirmada.
5. En la caja del macho A, derivar pin 1→B- y pin 2→A+ de Waveshare. No llevar 1/2/7/8 al macho B.
6. Comprobar extremo a extremo: inversor 4→PCS 4, inversor 5→PCS 5, inversor 1→solo B- e inversor 2→solo A+. Los demás destinos deben quedar abiertos salvo referencias verificadas. Nunca medir continuidad con tensión.
7. Conectar la batería **sin el ESP**. Arrancar y confirmar SOC, voltaje y ausencia de alarma BMS.
8. Alimentar el ESP por separado, conectar A+/B- y ejecutar la [prueba de dos registros](FIRST-READ-TEST.es.md).
9. Si Modbus no responde, desconectar el ramal ESP. No probar escrituras ni asumir otro baud rate.

## Abortar inmediatamente

Desconectar el ESP si desaparece el SOC, aparece fallo BMS/CAN, cambia la carga, se calienta un transceptor o las lecturas son inestables. Restaurar el cable original antes de seguir diagnosticando.

## Fuentes

- [Manual oficial del inversor Deye](https://www.deyeinverter.com/deyeinverter/2025/08/12/rand/5761/%5Bb%5Dmanual_sun-3.6-10k-sg05lp1-eu-am2-p_20250812_en.pdf): finalidad del puerto en página impresa 14; pinout BMS RJ45 en página 52.
- [Manual oficial SE-F16 V06](https://deyeess.com/wp-content/uploads/2025/12/Deye-ESS-User-Manual-SE-F16-EU-EN-V06.pdf): comprobar el pinout PCS de la revisión exacta antes de montar. El servidor oficial devolvió HTTP 403 durante esta revisión, por lo que aquí no se revalidó independientemente ese pinout.
