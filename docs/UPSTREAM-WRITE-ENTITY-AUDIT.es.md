# Auditoría de entidades de escritura del paquete Lewa-Reka 1P LV

> Snapshot: `Lewa-Reka/esphome-deye-inverter` `0.14.0`, commit `c0adb5c275a7d2be127e8fffe8c3c4711ea6e475`.
> Esta lista contiene solo entidades, scripts y callbacks capaces de provocar escrituras. Los sensores de lectura no aparecen.

**Criterio:** para firmware estrictamente de solo lectura, recomendación inicial para todas las filas: **COMENTAR**. `internal: true` o `disabled_by_default: true` no elimina la capacidad de escribir; solo cambia visibilidad.

## Resumen

- Rutas de escritura auditadas: **104**.
- Función Modbus de escritura observada en controles upstream: registros Holding mediante componentes `modbus_controller` y `use_write_multiple`.
- Riesgo `CRÍTICO`: puede alterar operación, seguridad eléctrica, batería, red o límites principales.
- Riesgo `ALTO`: cambia programación, umbrales o funciones auxiliares.

## `deye_hybrid_1p_lv.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Safe Mode: aplicar cuatro valores por defecto<br>`set_safe_modbus_registers` | `script` | — | Ejecuta la acción «Safe Mode: aplicar cuatro valores por defecto». | Visible/activa | **CRÍTICO** | **COMENTAR** |

## `packages/init.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Safe Mode tras desconexión API<br>`on_client_disconnected` | `callback API` | — | Espera 600 s tras perder Home Assistant y ejecuta set_safe_modbus_registers. | Visible/activa | **CRÍTICO** | **COMENTAR** |

## `packages/deye_hybrid_1p/battery.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Battery Operation Mode<br>`battery_operation_mode` | `select` | HR 213 | Selecciona el modo operativo de la batería. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery BMS Type | `select` | HR 325 | Selecciona el perfil/protocolo BMS de la batería. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Type<br>`battery_type` | `select` | HR 200 | Selecciona el tipo y estrategia de control de batería. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Wake Up | `switch` | HR 214 | Envía la orden de despertar la batería. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Generator Charging | `switch` | HR 231 | Activa o desactiva la carga de batería desde generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Grid Charging | `switch` | HR 232 | Activa o desactiva la carga de batería desde red. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Generator Charging Start Voltage | `number` | HR 225 | Fija la tensión que inicia carga desde generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Generator Charging Start SOC | `number` | HR 226 | Fija el SOC que inicia carga desde generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Generator Charging Current | `number` | HR 227 | Fija la corriente de carga desde generador. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Grid Charging Start Voltage | `number` | HR 228 | Fija la tensión que inicia carga desde red. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Grid Charging Start SOC | `number` | HR 229 | Fija el SOC que inicia carga desde red. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Equalization Cycle | `number` | HR 207 | Fija el ciclo de ecualización de batería. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Equalization Time | `number` | HR 208 | Fija la duración de ecualización de batería. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Temperature Compensation | `number` | HR 209 | Fija la compensación de tensión por temperatura. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Resistance | `number` | HR 215 | Fija la resistencia interna configurada de batería. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Charging Efficiency | `number` | HR 216 | Fija la eficiencia de carga usada por el inversor. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Shutdown SOC | `number` | HR 217 | Fija el SOC de apagado por batería baja. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Restart SOC | `number` | HR 218 | Fija el SOC de reinicio. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Low SOC | `number` | HR 219 | Fija el umbral de SOC bajo. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Shutdown Voltage | `number` | HR 220 | Fija la tensión de apagado. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Restart Voltage | `number` | HR 221 | Fija la tensión de reinicio. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Battery Low Voltage | `number` | HR 222 | Fija el umbral de tensión baja. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Equalization Voltage | `number` | HR 201 | Fija la tensión de ecualización de batería. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Absorption Voltage | `number` | HR 202 | Fija la tensión de absorción. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Float Voltage | `number` | HR 203 | Fija la tensión de flotación. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Capacity | `number` | HR 204 | Fija la capacidad nominal configurada. | Visible/activa | **ALTO** | **COMENTAR** |
| Battery Empty Voltage | `number` | HR 205 | Fija la tensión considerada batería vacía. | Visible/activa | **ALTO** | **COMENTAR** |
| Maximum Battery Charge Current<br>`maximum_battery_charge_current` | `number` | HR 210 | Fija la corriente máxima de carga de batería. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Maximum Battery Discharge Current<br>`maximum_battery_discharge_current` | `number` | HR 211 | Fija la corriente máxima de descarga de batería. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Maximum Battery Grid Charge Current | `number` | HR 230 | Fija la corriente máxima de carga desde red. | Visible/activa | **CRÍTICO** | **COMENTAR** |

## `packages/deye_hybrid_1p/device.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Power Switch<br>`switch_power` | `switch` | HR 43 | Enciende o apaga la función principal del inversor. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Self Check Time<br>`self_check_time` | `number` | HR 61 | Fija la duración del autocontrol del inversor. | Visible/activa | **ALTO** | **COMENTAR** |
| Meter | `select` | HR 326 | Selecciona el tipo/configuración de contador. | Visible/activa | **CRÍTICO** | **COMENTAR** |

## `packages/deye_hybrid_1p/gen.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Generator Port Use | `select` | HR 235 | Selecciona la función del puerto GEN. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator<br>`switch_generator` | `switch` | HR 234 | Activa o desactiva la configuración «Generator». | Visible/activa | **ALTO** | **COMENTAR** |
| SmartLoad Off Voltage | `number` | HR 236 | Fija tensión para desconectar Smart Load. | Visible/activa | **ALTO** | **COMENTAR** |
| SmartLoad Off SOC | `number` | HR 237 | Fija SOC para desconectar Smart Load. | Visible/activa | **ALTO** | **COMENTAR** |
| SmartLoad On Voltage | `number` | HR 238 | Fija tensión para conectar Smart Load. | Visible/activa | **ALTO** | **COMENTAR** |
| SmartLoad On SOC | `number` | HR 239 | Fija SOC para conectar Smart Load. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator Operating Time<br>`generator_operating_time` | `number` | HR 223 | Fija tiempo de funcionamiento del generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator Cooling Time<br>`generator_cooling_time` | `number` | HR 224 | Fija tiempo de enfriamiento del generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator Min PV Power<br>`generator_min_pv_power` | `number` | HR 241 | Fija potencia FV mínima vinculada a generador. | Visible/activa | **ALTO** | **COMENTAR** |

## `packages/deye_hybrid_1p/grid.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Grid Frequency | `select` | HR 285 | Selecciona frecuencia nominal de red. | Visible/activa | **ALTO** | **COMENTAR** |
| Charging Signal | `select` | HR 242 | Selecciona comportamiento de la señal de carga. | Visible/activa | **ALTO** | **COMENTAR** |
| Force Off Grid<br>`switch_off_grid` | `switch` | HR 281 | Fuerza funcionamiento desconectado de red. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Generator Grid Side | `switch` | HR 280 | Configura generador en el lado de red. | Visible/activa | **ALTO** | **COMENTAR** |
| Grid voltage protection - high<br>`grid_voltage_protection_high` | `number` | HR 287 | Fija disparo por sobretensión de red. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Grid voltage protection - low<br>`grid_voltage_protection_low` | `number` | HR 288 | Fija disparo por subtensión de red. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Grid Frequency Protection - high<br>`grid_requency_protection_high` | `number` | HR 289 | Fija disparo por frecuencia de red alta. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Grid Frequency Protection - low<br>`grid_requency_protection_low` | `number` | HR 290 | Fija disparo por frecuencia de red baja. | Visible/activa | **CRÍTICO** | **COMENTAR** |

## `packages/deye_hybrid_1p/tou.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Time of Use 1 Start<br>`time_of_use_1_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 2 Start<br>`time_of_use_2_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 3 Start<br>`time_of_use_3_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 4 Start<br>`time_of_use_4_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 5 Start<br>`time_of_use_5_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 6 Start<br>`time_of_use_6_start` | `datetime` | — | Define la hora de inicio de un tramo Time of Use; su cambio termina escribiendo el registro horario asociado. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use<br>`switch_time_of_use` | `switch` | HR 248 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 1 Charge Enable<br>`switch_time_point_1_charge_enable` | `switch` | HR 274 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 2 Charge Enable<br>`switch_time_point_2_charge_enable` | `switch` | HR 275 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 3 Charge Enable<br>`switch_time_point_3_charge_enable` | `switch` | HR 276 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 4 Charge Enable<br>`switch_time_point_4_charge_enable` | `switch` | HR 277 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 5 Charge Enable<br>`switch_time_point_5_charge_enable` | `switch` | HR 278 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 6 Charge Enable<br>`switch_time_point_6_charge_enable` | `switch` | HR 279 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use All Charge Enable<br>`switch_time_of_use_all_charge_enable` | `switch` | — | Activa/desactiva o configura la programación horaria Time of Use. | Desactivada por defecto | **ALTO** | **COMENTAR** |
| Time of Use 1 Start Raw<br>`time_of_use_1_start_raw` | `number` | HR 250 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 2 Start Raw<br>`time_of_use_2_start_raw` | `number` | HR 251 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 3 Start Raw<br>`time_of_use_3_start_raw` | `number` | HR 252 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 4 Start Raw<br>`time_of_use_4_start_raw` | `number` | HR 253 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 5 Start Raw<br>`time_of_use_5_start_raw` | `number` | HR 254 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 6 Start Raw<br>`time_of_use_6_start_raw` | `number` | HR 255 | Activa/desactiva o configura la programación horaria Time of Use. | Interna | **ALTO** | **COMENTAR** |
| Time of Use 1 Voltage<br>`time_of_use_1_voltage` | `number` | HR 262 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 2 Voltage<br>`time_of_use_2_voltage` | `number` | HR 263 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 3 Voltage<br>`time_of_use_3_voltage` | `number` | HR 264 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 4 Voltage<br>`time_of_use_4_voltage` | `number` | HR 265 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 5 Voltage<br>`time_of_use_5_voltage` | `number` | HR 266 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 6 Voltage<br>`time_of_use_6_voltage` | `number` | HR 267 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 1 Out Power<br>`time_of_use_1_out_power` | `number` | HR 256 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 2 Out Power<br>`time_of_use_2_out_power` | `number` | HR 257 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 3 Out Power<br>`time_of_use_3_out_power` | `number` | HR 258 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 4 Out Power<br>`time_of_use_4_out_power` | `number` | HR 259 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 5 Out Power<br>`time_of_use_5_out_power` | `number` | HR 260 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 6 Out Power<br>`time_of_use_6_out_power` | `number` | HR 261 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 1 SoC<br>`time_of_use_1_soc` | `number` | HR 268 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 2 SoC<br>`time_of_use_2_soc` | `number` | HR 269 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 3 SoC<br>`time_of_use_3_soc` | `number` | HR 270 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 4 SoC<br>`time_of_use_4_soc` | `number` | HR 271 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 5 SoC<br>`time_of_use_5_soc` | `number` | HR 272 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use 6 SoC<br>`time_of_use_6_soc` | `number` | HR 273 | Activa/desactiva o configura la programación horaria Time of Use. | Visible/activa | **ALTO** | **COMENTAR** |
| Time of Use All Voltage<br>`time_of_use_all_voltage` | `number` | — | Activa/desactiva o configura la programación horaria Time of Use. | Desactivada por defecto | **ALTO** | **COMENTAR** |
| Time of Use All Out Power<br>`time_of_use_all_out_power` | `number` | — | Activa/desactiva o configura la programación horaria Time of Use. | Desactivada por defecto | **ALTO** | **COMENTAR** |
| Time of Use All SoC<br>`time_of_use_all_soc` | `number` | — | Activa/desactiva o configura la programación horaria Time of Use. | Desactivada por defecto | **ALTO** | **COMENTAR** |

## `packages/deye_hybrid_1p/work_mode.yaml`

| Entidad / ID | Tipo | Registro | Qué hace | Exposición | Riesgo | Recomendación |
|---|---|---:|---|---|---|---|
| Energy Management Priority<br>`energy_management_priority` | `select` | HR 243 | Selecciona prioridad energética, por ejemplo carga o batería. | Visible/activa | **ALTO** | **COMENTAR** |
| System Work Mode<br>`system_work_mode` | `select` | HR 244 | Selecciona el modo global de trabajo del inversor. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Solar Sell<br>`switch_solar_sell` | `switch` | HR 247 | Permite o impide venta de excedente solar. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Microinverter Export cut-off | `switch` | HR 280 | Activa el corte de exportación del microinversor. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator Peak Shaving Enable | `switch` | HR 280 | Activa peak shaving usando generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Grid Peak Shaving Enable | `switch` | HR 280 | Activa peak shaving de red. | Visible/activa | **ALTO** | **COMENTAR** |
| Max Sell Power<br>`max_sell_power` | `number` | HR 245 | Fija potencia máxima exportable. | Visible/activa | **CRÍTICO** | **COMENTAR** |
| Max Solar Power<br>`max_solar_power` | `number` | HR 53 | Fija potencia solar máxima admitida/configurada. | Visible/activa | **ALTO** | **COMENTAR** |
| Zero Export Power<br>`zero_export_power` | `number` | HR 206 | Fija margen/objetivo de potencia para vertido cero. | Visible/activa | **ALTO** | **COMENTAR** |
| Generator Peak shaving<br>`generator_peak_shaving_power` | `number` | HR 292 | Fija potencia de peak shaving del generador. | Visible/activa | **ALTO** | **COMENTAR** |
| Grid Peak Shaving Power<br>`grid_peak_shaving_power` | `number` | HR 293 | Fija potencia de peak shaving de red. | Visible/activa | **ALTO** | **COMENTAR** |

## Decisión propuesta

1. Comentar `api.on_client_disconnected` y `script.set_safe_modbus_registers` primero.
2. Comentar todos los bloques `select`, `switch`, `number` y `datetime` de estos ficheros.
3. Mantener sensores y text sensors de lectura.
4. Si algún sensor de plantilla depende de un control eliminado, comentarlo solo por dependencia y documentarlo por separado.
5. Verificar configuración expandida y código fuente generado para confirmar cero funciones Modbus de escritura.

## Entidad de lectura comentada por dependencia

| Fichero | Entidad | Motivo |
|---|---|---|
| `packages/deye_hybrid_1p/work_mode.yaml` | `Load Priority` (`binary_sensor.template`) | Su lambda depende del select escribible `energy_management_priority`. Mantenerla exigiría conservar un control Modbus; se comenta para garantizar solo lectura. |
