# Modelo de Dominio - SIGEMI (Detallado)

## Sistema Integral de Gestion Micologica

---

# 1. Introduccion

El modelo de dominio de SIGEMI esta compuesto por **22 entidades** que cubren cuatro grandes areas funcionales:

| Area | Entidades | Flujos asociados |
|---|---|---|
| **Recepcion y Agenda** | Paciente, Turno, IndicacionMedica, ConfiguracionAgenda, BloqueoAgenda | UC-REC-01 a UC-REC-22 |
| **Diagnostico Clinico** | FichaClinica, VersionFichaClinica, AnalisisMicologico, TipoAnalisis, Otp, InformeResultados | UC-DIAG-01 a UC-DIAG-11 |
| **Laboratorio (Insumos y Residuos)** | Insumo, Lote, MovimientoInventario, CategoriaInsumo, UbicacionAlmacenamiento, ResiduoQuimico, DisposicionFinal, CategoriaResiduo | UC-LAB-01 a UC-LAB-13 |
| **Seguridad y Reportes** | Usuario, Rol, Auditoria, Reporte | UC-SEG-01, UC-SEG-02, UC-REP-01 |

---
# 2. Entidades Transaccionales por Area

---

## 2.1 Area de Recepcion y Agenda

### 2.1.1 Paciente

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| numero_registro | string | Numero de registro clinico interno |
| dni | string | Documento Nacional de Identidad (unico) |
| nombre | string | Nombre/s del paciente |
| apellido | string | Apellido/s del paciente |
| fecha_nacimiento | date | Fecha de nacimiento |
| sexo | string | Sexo del paciente |
| domicilio | string | Direccion de residencia |
| telefono | string | Telefono de contacto (WhatsApp) |
| correo_electronico | string | Correo electronico |
| obra_social | string | Obra social o cobertura medica |
| estado | string | Activo / Inactivo (baja logica) |
| fecha_ingreso | datetime | Fecha de creacion del registro |

**Descripcion:** Persona atendida en el laboratorio de Micologia. Es el eje central del historial clinico. Soporta **Alta Temprana**: el agente IA crea el registro solo con DNI y nombre; el resto se completa durante la consulta. El paciente **no** es un Usuario del sistema (ACT-04): interactua de forma anonima via WhatsApp y portal OTP.

**Relaciones:**
- 1 -> 0..N **FichaClinica**: un paciente puede tener multiples consultas a lo largo del tiempo.
- 1 -> 0..N **Turno**: un paciente agenda uno o mas turnos.
- N < - 1 **Usuario**: solo un Administrador puede ejecutar su baja logica (UC-REC-19).

**Flujos donde interviene:**
- **UC-REC-01** - Registro de paciente (Alta Temprana por IA via WhatsApp).
- **UC-REC-04** - Busqueda de paciente para agendar turno.
- **UC-REC-14** - Modificacion de datos demograficos del paciente.
- **UC-REC-15** (paso 6) - Completar datos demograficos al registrar asistencia.
- **UC-REC-16** - Consulta de historial de turnos y analisis del paciente.
- **UC-REC-19** - Baja logica de paciente (solo Administrador).
- **UC-DIAG-01** - El paciente asiste a la consulta donde se completa su ficha clinica.
- **UC-DIAG-05** - El paciente descarga su informe de resultados via OTP.

---
### 2.1.2 Turno

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| paciente_id | integer | FK a Paciente |
| tipo_analisis_id | integer | FK a TipoAnalisis |
| indicacion_medica_id | integer | FK a IndicacionMedica enviada |
| fecha_hora | datetime | Fecha y hora programada del turno |
| estado | string | Confirmado / Pendiente / Atendido / Cancelado / No Asistio |
| reprogramaciones | integer | Contador de reprogramaciones (max. 2) |
| motivo_cancelacion | string | Motivo de cancelacion (si aplica) |
| fecha_creacion | datetime | Fecha de creacion del turno |
| fecha_atencion | datetime | Fecha/hora real de atencion (si asistio) |

**Descripcion:** Cita programada para un paciente en una fecha y hora especificas. Recorre un ciclo de estados: Pendiente, Confirmado, Atendido, Cancelado o No Asistio.

**Relaciones:**
- N < - 1 **Paciente**: cada turno esta asignado a un unico paciente (UC-REC-01).
- N < - 1 **TipoAnalisis**: se agenda para un tipo de analisis micologico especifico (UC-REC-20 paso 6).
- N < - 1 **IndicacionMedica**: al agendar se envia una indicacion medica predefinida (RF-02).

**Flujos donde interviene:**
- **UC-REC-01** - Creacion del turno (via WhatsApp con Agente IA).
- **UC-REC-02** - Confirmacion del turno por parte del paciente.
- **UC-REC-03** - Cancelacion del turno.
- **UC-REC-04** - Reprogramacion del turno (max. 2 veces).
- **UC-REC-05** - Registro de asistencia (marcar como Atendido / No Asistio).
- **UC-REC-06** - Notificacion de recordatorio automatico al paciente.
- **UC-REC-14** - Visualizacion de agenda del dia.
- **UC-REC-15** - Registro de asistencia y completar datos del paciente.
- **UC-REC-20** a **UC-REC-22** - Agendado desde el panel interno de Administracion.

---
### 2.1.3 IndicacionMedica

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| titulo | string | Titulo de la indicacion |
| contenido | text | Cuerpo de la indicacion medica |
| tipo_analisis_id | integer | FK a TipoAnalisis asociado |
| estado | string | Activo / Inactivo (baja logica) |
| fecha_creacion | datetime | Fecha de creacion |
| fecha_modificacion | datetime | Fecha de ultima modificacion |

**Descripcion:** Instruccion medica predefinida que se envia al paciente al agendar un turno. Cada indicacion esta vinculada a un tipo de analisis especifico.

**Relaciones:**
- N < - 1 **TipoAnalisis**: cada indicacion se vincula obligatoriamente a un tipo de analisis (UC-REC-10 paso 2).

**Flujos donde interviene:**
- **UC-REC-10 a UC-REC-13** - ABM de indicaciones (Alta, Baja, Modificacion).
- **UC-REC-20** (paso 5) - Seleccion de la indicacion medica asociada al crear el turno.

---
### 2.1.4 ConfiguracionAgenda

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| dias_habiles | string | Dias de atencion (ej. "L,M,X,J,V") |
| horario_inicio_manana | time | Inicio franja matutina |
| horario_fin_manana | time | Fin franja matutina |
| horario_inicio_tarde | time | Inicio franja vespertina |
| horario_fin_tarde | time | Fin franja vespertina |
| duracion_turno | integer | Duracion en minutos de cada turno |
| intervalo_entre_turnos | integer | Minutos de separacion entre turnos consecutivos |
| max_turnos_por_franja | integer | Cantidad maxima de turnos por bloque horario |
| periodos_inhabiles | text | Feriados y recesos en formato JSON |
| usuario_modificacion_id | integer | FK a Usuario que modifico la configuracion |
| fecha_modificacion | datetime | Fecha del ultimo cambio |

**Descripcion:** Conjunto unico de parametros que definen la disponibilidad horaria del laboratorio (dias habiles, duracion de turnos, franjas, recesos). Solo existe una configuracion vigente a la vez.

**Relaciones:**
- 0..1 < - 1 **Usuario**: el Administrador define los parametros de la agenda.

**Flujos donde interviene:**
- **UC-REC-07** - Gestion de la agenda: definicion de disponibilidad y parametros operativos.

---
### 2.1.5 BloqueoAgenda

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| fecha_inicio | date | Inicio del periodo bloqueado |
| fecha_fin | date | Fin del periodo (mismo dia si es dia unico) |
| hora_inicio | time | Inicio de franja bloqueada (nulo si dia completo) |
| hora_fin | time | Fin de franja bloqueada (nulo si dia completo) |
| tipo_bloqueo | string | Dia Completo / Franja Horaria |
| motivo | string | Razon del bloqueo |
| usuario_id | integer | FK a Usuario (Administrador) que ejecuto el bloqueo |
| fecha_bloqueo | datetime | Fecha de creacion del bloqueo |
| estado | string | Activo / Inactivo (desbloqueado) |

**Descripcion:** Restriccion temporal de un dia completo o franja horaria que impide la asignacion de turnos en ese periodo.

**Relaciones:**
- N < - 1 **Usuario**: el Administrador puede crear multiples bloqueos de dias o franjas horarias (UC-REC-08).

**Flujos donde interviene:**
- **UC-REC-08** - Bloqueo y desbloqueo de la agenda.

---
## 2.2 Area de Diagnostico Clinico

### 2.2.1 FichaClinica

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| paciente_id | integer | FK a Paciente |
| bioquimico_id | integer | FK a Usuario que registro la ficha |
| fecha_consulta | datetime | Fecha y hora de la consulta presencial |
| datos_clinicos | text | Informacion clinica estructurada (JSON) |
| version_actual | integer | Numero de version vigente |
| estado | string | Activo / Modificado / Historico |

**Descripcion:** Documento clinico estructurado que registra la informacion medica recolectada durante una consulta presencial. Se genera por cada visita del paciente al laboratorio.

**Relaciones:**
- N < - 1 **Paciente**: cada ficha pertenece a un unico paciente; un paciente puede tener multiples fichas.
- 1 -> 0..N **AnalisisMicologico**: una ficha clinica puede originar multiples analisis (UC-DIAG-02).
- 1 -> 0..N **VersionFichaClinica**: cada modificacion de la ficha genera una version historica (RF-20, UC-DIAG-08).
- N < - 1 **Usuario**: un Bioquimico/Doctor completa y registra la ficha durante la consulta (UC-DIAG-01).

**Flujos donde interviene:**
- **UC-DIAG-01** - Registro de ficha clinica durante la consulta presencial.
- **UC-DIAG-08** - Modificacion de ficha clinica existente (genera una nueva version).

---
### 2.2.2 VersionFichaClinica

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| ficha_clinica_id | integer | FK a FichaClinica |
| numero_version | integer | Numero secuencial de version |
| datos_previos | text | Contenido de la ficha antes del cambio (JSON) |
| datos_nuevos | text | Contenido de la ficha despues del cambio (JSON) |
| usuario_id | integer | FK a Usuario que realizo la modificacion |
| fecha_modificacion | datetime | Fecha y hora de la modificacion |
| motivo | string | Razon del cambio |

**Descripcion:** Historial de cambios de una ficha clinica. Almacena la version previa ante cada modificacion. Materializa el requisito RF-20: cada modificacion de ficha preserva el contenido anterior como respaldo de auditoria clinica.

**Relaciones:**
- N < - 1 **FichaClinica**: cada version pertenece a una unica ficha clinica.
- N < - 1 **Usuario**: el Bioquimico/Doctor que modifica la ficha queda registrado como autor de la version.

**Flujos donde interviene:**
- **UC-DIAG-08** - Al modificar una ficha clinica, el sistema genera automaticamente una nueva version preservando los datos previos.

---
### 2.2.3 AnalisisMicologico

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| ficha_clinica_id | integer | FK a FichaClinica |
| tipo_analisis_id | integer | FK a TipoAnalisis |
| bioquimico_validador_id | integer | FK a Usuario que valida (nulo hasta validacion) |
| tipo_muestra | string | Tipo de muestra biologica (ej. unas, piel, cabello) |
| estado | string | Pendiente / En Proceso / Terminado / Validado / Cancelado / Derivado |
| observaciones | text | Observaciones y resultados parciales |
| resultado_final | text | Diagnostico y resultado definitivo |
| fecha_creacion | datetime | Fecha de ingreso de la muestra |
| fecha_validacion | datetime | Fecha de validacion final (nulo hasta ese momento) |
| motivo_cancelacion | string | Motivo obligatorio si estado = Cancelado |

**Descripcion:** Traza el ciclo de vida completo de una muestra microbiologica, desde su ingreso hasta su validacion o cancelacion. Es la entidad central del flujo de diagnostico.

**Relaciones:**
- N < - 1 **FichaClinica**: el analisis se crea a partir de una ficha clinica registrada (UC-DIAG-02 paso 6).
- N < - 1 **TipoAnalisis**: cada analisis corresponde a un tipo del catalogo clinico.
- N < - 0..1 **Usuario**: solo un Bioquimico puede validar el analisis (estado "Validado") (UC-DIAG-04).
- 1 -> 0..1 **Otp**: al validar el analisis se genera un token OTP unico para descarga segura (UC-DIAG-04).
- 1 -> 0..1 **InformeResultados**: al validar se compila y almacena el PDF del informe (UC-DIAG-04).
- 1 -> 0..N **MovimientoInventario**: los retiros de insumos pueden asociarse a un analisis (IRQ-06, UC-LAB-02).
- 1 -> 0..N **ResiduoQuimico**: un analisis clinico puede generar residuos quimicos registrados (UC-LAB-03).

**Flujos donde interviene:**
- **UC-DIAG-02** - Registro de ingreso de la muestra y creacion del analisis.
- **UC-DIAG-03** - Procesamiento del analisis (carga de observaciones y resultados parciales).
- **UC-DIAG-04** - Validacion del analisis (genera OTP e InformeResultados).
- **UC-DIAG-09** - Cancelacion del analisis (requiere motivo).
- **UC-LAB-02** - Asociacion de consumo de insumos al analisis.
- **UC-LAB-03** - Registro de residuos quimicos generados por el analisis.

---
### 2.2.4 TipoAnalisis

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| nombre | string | Nombre del tipo de analisis |
| descripcion | text | Descripcion del analisis o tipo de muestra |
| indicaciones_asociadas | text | Indicaciones medicas estandar asociadas |
| estado | string | Activo / Inactivo (baja logica) |

**Descripcion:** Catalogo de tipos de analisis micologicos y tipos de muestra disponibles. Es un catalogo base referenciado por Turno, IndicacionMedica y AnalisisMicologico.

**Relaciones:**
- 1 < - N **Turno**: un turno se agenda para un tipo de analisis.
- 1 < - N **IndicacionMedica**: cada indicacion se asocia a un tipo de analisis.
- 1 < - N **AnalisisMicologico**: cada analisis pertenece a un tipo.

**Flujos donde interviene:**
- **UC-DIAG-11** - Mantenimiento del catalogo de tipos de analisis (ABM).
- **UC-REC-20** (paso 6) - Seleccion del tipo de analisis al agendar turno.
- **UC-REC-10** (paso 2) - Asociacion de indicacion medica a tipo de analisis.
- **UC-DIAG-02** - Especificacion del tipo de analisis al registrar una muestra.

---
### 2.2.5 Otp

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| analisis_id | integer | FK a AnalisisMicologico |
| token | string | Codigo OTP generado criptograficamente |
| fecha_generacion | datetime | Fecha y hora de generacion |
| fecha_expiracion | datetime | Fecha de expiracion (TTL = 7 dias) |
| usado | boolean | Indica si ya fue consumido |
| fecha_uso | datetime | Fecha de consumo (nulo si no usado) |

**Descripcion:** Token criptografico de un solo uso generado al validar un analisis. Habilita la descarga segura del informe de resultados por parte del paciente, con un TTL de 7 dias.

**Relaciones:**
- N < - 1 **AnalisisMicologico**: cada OTP se genera para un analisis especifico al momento de su validacion.
- 1 < -> 1 **InformeResultados**: el OTP habilita la descarga del informe asociado. La relacion es bidireccional 1 a 1.

**Flujos donde interviene:**
- **UC-DIAG-04** - Generacion del OTP al validar el analisis.
- **UC-DIAG-05** - Verificacion del OTP para habilitar descarga del informe (portal web del paciente).

---
### 2.2.6 InformeResultados

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| analisis_id | integer | FK a AnalisisMicologico |
| ruta_archivo | string | Ruta del PDF en servidor local |
| fecha_generacion | datetime | Fecha de generacion automatica |
| hash_archivo | string | Hash de integridad del archivo |

**Descripcion:** Documento PDF generado automaticamente al validar un analisis, almacenado en el servidor local del laboratorio. Incluye un hash criptografico para verificar la integridad del archivo.

**Relaciones:**
- N < - 1 **AnalisisMicologico**: el informe pertenece al analisis que lo origino.
- 1 < -> 1 **Otp**: el OTP valido permite la descarga del informe asociado. Es una relacion 1 a 1 bidireccional.

**Flujos donde interviene:**
- **UC-DIAG-04** - El sistema genera automaticamente el informe al validar el analisis (UC-DIAG-04 paso 11).
- **UC-DIAG-05** - Descarga del informe por parte del paciente mediante OTP valido.

---
### 2.3.2 Lote

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| insumo_id | integer | FK a Insumo |
| numero_lote | string | Numero de lote del fabricante |
| fecha_ingreso | date | Fecha de recepcion en el laboratorio |
| fecha_vencimiento | date | Fecha de vencimiento |
| cantidad_inicial | real | Cantidad recibida originalmente |
| cantidad_actual | real | Cantidad remanente disponible |
| estado | string | Activo / Agotado / Vencido |

**Descripcion:** Grupo especifico de un mismo insumo con numero de lote y fecha de vencimiento particulares. Implementa la politica **FEFO** (First Expiry, First Out): al retirar, el sistema consume primero el lote con fecha de vencimiento mas proxima (RF-18).

**Relaciones:**
- N < - 1 **Insumo**: cada lote corresponde a un unico insumo.
- 1 -> 0..N **MovimientoInventario**: cada operacion sobre el inventario (ingreso, retiro, devolucion) afecta un lote especifico.

**Flujos donde interviene:**
- **UC-LAB-01** - Recepcion de nuevos lotes en el laboratorio.
- **UC-LAB-02** - Retiro de insumos (consumo FEFO: selecciona lote mas proximo a vencer).
- **UC-LAB-06** - Recepcion y validacion de lotes.
- **UC-LAB-07** - Devolucion de insumos (revierte cantidad a un lote especifico).
- **UC-LAB-08** - Dashboard de alertas de vencimiento (basado en dias_alerta_vencimiento del Insumo).

---
### 2.3.3 MovimientoInventario

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| insumo_id | integer | FK a Insumo |
| lote_id | integer | FK a Lote afectado |
| usuario_id | integer | FK a Usuario responsable |
| ubicacion_id | integer | FK a UbicacionAlmacenamiento de origen/destino |
| analisis_id | integer | FK a AnalisisMicologico asociado (nulo si es practica) |
| devolucion_referencia_id | integer | FK al MovimientoInventario original (si es devolucion) |
| tipo_movimiento | string | Ingreso / Retiro / Devolucion |
| cantidad | real | Cantidad movida |
| practica_educativa | string | Descripcion de practica si no es para analisis clinico |
| fecha | datetime | Fecha y hora del movimiento |

**Descripcion:** Registro individual de cada operacion sobre el inventario: ingreso, retiro o devolucion. Cada movimiento queda trazado con usuario responsable, ubicacion, lote afectado y opcionalmente el analisis clinico o practica educativa que lo motivo.

**Relaciones:**
- N < - 1 **Lote**: cada movimiento (ingreso/retiro/devolucion) impacta un lote concreto (IRQ-06).
- N < - 1 **Usuario**: Profesor, Bioquimico o Administrador registra cada movimiento (IRQ-06).
- N < - 1 **UbicacionAlmacenamiento**: cada movimiento registra la ubicacion de origen o destino (UC-LAB-02).
- N < - 0..1 **AnalisisMicologico**: opcionalmente vinculado a un analisis clinico para trazabilidad del consumo.
- N < - 0..1 **MovimientoInventario** (autoreferencia): una devolucion referencia al movimiento de retiro original que esta revirtiendo (UC-LAB-09).

**Flujos donde interviene:**
- **UC-LAB-01** - Registro de ingreso de insumos al inventario.
- **UC-LAB-02** - Registro de retiro de insumos (asociado a un analisis o practica educativa).
- **UC-LAB-07** - Devolucion de insumos al inventario.
- **UC-LAB-09** - Autoreferencia: una devolucion revierte un retiro previo.

---
### 2.3.4 CategoriaInsumo

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| nombre | string | Nombre de la categoria |
| descripcion | text | Descripcion (ej. "Reactivos quimicos", "Medios de cultivo") |
| estado | string | Activo / Inactivo |

**Descripcion:** Clasificacion de insumos (reactivos, medios de cultivo, materiales descartables, equipos). Catalogo base referenciado por Insumo.

**Relaciones:**
- 1 < - N **Insumo**: cada insumo pertenece a una categoria.

**Flujos donde interviene:**
- **UC-LAB-12** - Gestion del catalogo de categorias de insumos (ABM).
- **UC-LAB-06** - Al dar de alta un insumo, se asigna a una categoria existente.

---
### 2.3.5 UbicacionAlmacenamiento

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| nombre | string | Nombre de la ubicacion (ej. "Estante A-3", "Heladera 2") |
| descripcion | text | Detalle de la ubicacion |
| estado | string | Activo / Inactivo |

**Descripcion:** Lugar fisico donde se almacena un insumo dentro del laboratorio. Catalogo base referenciado por Insumo (ubicacion por defecto) y MovimientoInventario (origen/destino).

**Relaciones:**
- 1 < - N **Insumo**: cada insumo tiene una ubicacion de almacenamiento por defecto.
- 1 < - N **MovimientoInventario**: cada movimiento registra la ubicacion de origen o destino.

**Flujos donde interviene:**
- **IRQ-03** - Requisito de almacenamiento fisico trazable.
- **UC-LAB-02** - Al registrar movimientos de retiro/ingreso se especifica la ubicacion.

---
## 2.4 Area de Laboratorio: Residuos

### 2.4.1 ResiduoQuimico

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| categoria_residuo_id | integer | FK a CategoriaResiduo |
| usuario_id | integer | FK a Usuario responsable del registro |
| analisis_id | integer | FK a AnalisisMicologico (nulo si es de practica educativa) |
| disposicion_final_id | integer | FK a DisposicionFinal (nulo hasta disposicion) |
| fecha_hora | datetime | Fecha y hora de generacion del residuo |
| volumen | real | Volumen exacto generado (ml) |
| peso | real | Peso exacto generado (g) |
| descripcion | text | Observaciones adicionales |
| reporte_mensual_id | integer | FK a Reporte que lo consolido (nulo si no consolidado) |

**Descripcion:** Registro de desechos quimicos generados por actividades del laboratorio, con volumen y peso exactos. Puede originarse de un analisis clinico o de una practica educativa.

**Relaciones:**
- N < - 1 **CategoriaResiduo**: cada residuo se clasifica segun su categoria de peligrosidad (IRQ-04).
- N < - 1 **Usuario**: Profesor o Bioquimico registra la generacion del residuo (UC-LAB-03).
- N < - 0..1 **AnalisisMicologico**: opcionalmente vinculado a un analisis clinico que lo genero.
- N < - 0..1 **DisposicionFinal**: un residuo eventualmente recibe tratamiento final (RF-19).
- N < - 0..1 **Reporte**: al generar el reporte mensual, el residuo queda vinculado al reporte (UC-LAB-04).

**Flujos donde interviene:**
- **UC-LAB-03** - Registro de residuo quimico generado (por analisis o practica educativa).
- **UC-LAB-11** - Consulta del historial de residuos generados.
- **UC-LAB-04** - Consolidacion en reporte mensual de residuos.

---
### 2.4.2 DisposicionFinal

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| usuario_id | integer | FK a Usuario responsable |
| fecha | datetime | Fecha de disposicion final |
| metodo_tratamiento | string | Metodo de tratamiento aplicado |
| descripcion | text | Detalles de la disposicion |

**Descripcion:** Registro de la salida y tratamiento definitivo de los residuos acumulados. Varios residuos pueden consolidarse en una unica disposicion final.

**Relaciones:**
- N < - 1 **Usuario**: un usuario autorizado registra la disposicion final (RF-19).
- 1 -> 0..N **ResiduoQuimico**: una disposicion puede consolidar multiples residuos.

**Flujos donde interviene:**
- **RF-19** - Registro de disposicion final y tratamiento de residuos acumulados.

---
### 2.4.3 CategoriaResiduo

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| nombre | string | Nombre de la categoria |
| clase_peligrosidad | string | Clase I / Clase II / Clase III |
| descripcion | text | Descripcion de la categoria |
| instrucciones_almacenamiento | text | Instrucciones de resguardo y manejo |
| estado | string | Activo / Inactivo |

**Descripcion:** Clasificacion de peligrosidad para residuos quimicos (Clase I, II, III). Catalogo base referenciado por ResiduoQuimico.

**Relaciones:**
- 1 < - N **ResiduoQuimico**: cada residuo pertenece a una categoria de peligrosidad.

**Flujos donde interviene:**
- **UC-LAB-10** - Gestion del catalogo de categorias de residuos (ABM).
- **UC-LAB-03** - Al registrar un residuo, se selecciona su categoria correspondiente.

---
## 2.5 Area de Seguridad y Acceso

### 2.5.1 Usuario

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| rol_id | integer | FK a Rol |
| nombre | string | Nombre/s del usuario |
| apellido | string | Apellido/s del usuario |
| correo_electronico | string | Correo institucional (login) |
| contrasena_hash | string | Hash de contrasena |
| estado | string | Activo / Inactivo (baja logica) / Bloqueado Temporal |
| intentos_fallidos | integer | Contador de intentos fallidos de login |
| bloqueado_hasta | datetime | Fecha/hora de desbloqueo automatico |
| fecha_registro | datetime | Fecha de creacion de la cuenta |

**Descripcion:** Cuenta de acceso al sistema para personal interno autenticado. Incluye credenciales (hash de contrasena), control de bloqueo por intentos fallidos y referencia a su rol. Todo usuario pertenece a uno de los tres perfiles: Administrador, Bioquimico-Doctor o Profesor.

**Relaciones:**
- N < - 1 **Rol**: cada usuario tiene asignado un unico rol que determina sus permisos (UC-SEG-02).
- 1 -> 0..N **Auditoria**: toda accion critica del usuario queda registrada automaticamente (RF-14).
- 1 -> 0..N **Reporte**: un usuario autorizado puede emitir multiples reportes.
- 1 -> 0..1 **ConfiguracionAgenda**: el Administrador define los parametros de la agenda.
- 1 -> 0..N **BloqueoAgenda**: el Administrador puede crear multiples bloqueos.
- 1 -> 0..N **FichaClinica**: un Bioquimico/Doctor registra fichas clinicas.
- 1 -> 0..N **MovimientoInventario**: un usuario registra movimientos de inventario.
- 1 -> 0..N **Paciente**: un Administrador puede desactivar pacientes.

**Flujos donde interviene:**
- **UC-SEG-01** - Autenticacion y control de acceso al sistema.
- **UC-SEG-02** - Gestion de usuarios y roles (ABM).
- **Transversal** - Toda operacion sensible requiere un usuario autenticado.

---
### 2.5.2 Rol

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| nombre | string | Administrador / Bioquimico-Doctor / Profesor |
| descripcion | text | Descripcion del rol y sus permisos |

**Descripcion:** Perfil de autorizacion que define los permisos operativos dentro del sistema. Los tres roles definidos son: Administrador (gestion completa del sistema), Bioquimico-Doctor (operaciones clinicas y de laboratorio) y Profesor (operaciones academicas y de inventario).

**Relaciones:**
- 1 < - N **Usuario**: cada usuario tiene exactamente un rol asignado.

**Flujos donde interviene:**
- **UC-SEG-02** - Gestion de roles y asignacion a usuarios.
- **Transversal** - Toda operacion verifica el rol del usuario contra los permisos requeridos.

---
## 2.6 Area de Auditoria y Reportes

### 2.6.1 Auditoria

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| usuario_id | integer | FK a Usuario responsable |
| fecha_hora | datetime | Fecha y hora precisa del evento |
| direccion_ip | string | Direccion IP de origen |
| modulo | string | Modulo del sistema donde ocurrio |
| accion | string | Accion ejecutada (CREAR, MODIFICAR, ELIMINAR, VALIDAR, etc.) |
| entidad_afectada | string | Nombre de la entidad afectada |
| entidad_id | integer | ID del registro afectado |
| cambio_realizado | text | Detalle del cambio en formato JSON |

**Descripcion:** Registro inmutable y cronologico de cada evento critico ejecutado en la plataforma. Es una entidad transversal que registra toda accion sensible conforme a RF-14: configuracion de agenda, bloqueos, validacion de analisis, modificaciones de pacientes, etc.

**Relaciones:**
- N < - 1 **Usuario**: cada registro de auditoria esta asociado a un usuario responsable.

**Flujos donde interviene:**
- **UC-SEG-01** - Auditoria de eventos de autenticacion y seguridad.
- **Transversal** - Se genera automaticamente ante acciones sensibles en cualquier modulo del sistema (RF-14).

---
### 2.6.2 Reporte

| Atributo | Tipo | Descripcion |
|---|---|---|
| id | integer | Identificador unico |
| usuario_id | integer | FK a Usuario que genero el reporte |
| tipo_reporte | string | Residuos / Inventario / Operativo (Clinico) |
| rango_fecha_inicio | date | Inicio del periodo reportado |
| rango_fecha_fin | date | Fin del periodo reportado |
| ruta_archivo | string | Ruta del archivo generado en servidor |
| formato_archivo | string | PDF / CSV / XLSX |
| fecha_generacion | datetime | Fecha de emision del reporte |
| mes_anio | string | Mes/anio consolidado (para reporte mensual de residuos) |

**Descripcion:** Documento consolidado generado a partir de datos transaccionales para cumplimiento normativo o investigacion. Soporta tres tipos: residuos (reporte mensual obligatorio), inventario (estado de stock y movimientos) y operativo (datos clinicos y estadisticas del laboratorio).

**Relaciones:**
- N < - 1 **Usuario**: un usuario autorizado puede emitir multiples reportes (UC-LAB-04, UC-REP-01).
- 1 -> 0..N **ResiduoQuimico**: el reporte mensual consolida los residuos generados en el periodo.

**Flujos donde interviene:**
- **UC-LAB-04** - Generacion de reporte mensual de residuos quimicos.
- **UC-LAB-13** - Generacion de reporte de inventario.
- **UC-REP-01** - Generacion de reportes operativos y estadisticos.

---
---
# 3. Mapa de Entidades por Flujo de Trabajo

## 3.1 Recepcion y Agenda (UC-REC)

| Flujo | Entidades participantes |
|---|---|
| UC-REC-01 - Creacion de turno (WhatsApp) | Paciente, Turno, TipoAnalisis, IndicacionMedica |
| UC-REC-02 - Confirmacion de turno | Turno |
| UC-REC-03 - Cancelacion de turno | Turno |
| UC-REC-04 - Reprogramacion de turno | Turno, Paciente |
| UC-REC-05 - Registro de asistencia | Turno |
| UC-REC-06 - Recordatorio automatico | Turno, IndicacionMedica |
| UC-REC-07 - Configurar agenda | ConfiguracionAgenda, Usuario |
| UC-REC-08 - Bloquear agenda | BloqueoAgenda, Usuario |
| UC-REC-10 a UC-REC-13 - ABM Indicaciones | IndicacionMedica, TipoAnalisis |
| UC-REC-14 - Modificar paciente | Paciente, Usuario |
| UC-REC-15 - Registrar asistencia + datos | Turno, Paciente |
| UC-REC-16 - Historial del paciente | Paciente, Turno, FichaClinica, AnalisisMicologico |
| UC-REC-19 - Baja logica de paciente | Paciente, Usuario |
| UC-REC-20 a UC-REC-22 - Agendado interno | Turno, Paciente, TipoAnalisis, IndicacionMedica |

## 3.2 Diagnostico Clinico (UC-DIAG)

| Flujo | Entidades participantes |
|---|---|
| UC-DIAG-01 - Registro de ficha clinica | FichaClinica, Paciente, Usuario |
| UC-DIAG-02 - Ingreso de muestra | AnalisisMicologico, FichaClinica, TipoAnalisis |
| UC-DIAG-03 - Procesar analisis | AnalisisMicologico |
| UC-DIAG-04 - Validar analisis | AnalisisMicologico, Otp, InformeResultados, Usuario |
| UC-DIAG-05 - Descargar informe (portal OTP) | Otp, InformeResultados, Paciente |
| UC-DIAG-08 - Modificar ficha clinica | FichaClinica, VersionFichaClinica, Usuario |
| UC-DIAG-09 - Cancelar analisis | AnalisisMicologico |
| UC-DIAG-11 - Gestionar tipo de analisis | TipoAnalisis |

## 3.3 Laboratorio - Insumos (UC-LAB)

| Flujo | Entidades participantes |
|---|---|
| UC-LAB-01 - Recepcion de insumos | Insumo, Lote, MovimientoInventario, UbicacionAlmacenamiento, Usuario |
| UC-LAB-02 - Retiro de insumos | MovimientoInventario, Lote, Insumo, AnalisisMicologico, Usuario, UbicacionAlmacenamiento |
| UC-LAB-06 - ABM de insumos | Insumo, CategoriaInsumo, UbicacionAlmacenamiento |
| UC-LAB-07 - Devolucion de insumos | MovimientoInventario, Lote, Insumo, Usuario |
| UC-LAB-08 - Dashboard alertas stock | Insumo, Lote |
| UC-LAB-09 - Devolucion con referencia | MovimientoInventario (autoreferencia) |
| UC-LAB-12 - Gestionar categorias | CategoriaInsumo |

## 3.4 Laboratorio - Residuos (UC-LAB)

| Flujo | Entidades participantes |
|---|---|
| UC-LAB-03 - Registrar residuo quimico | ResiduoQuimico, CategoriaResiduo, AnalisisMicologico, Usuario |
| UC-LAB-04 - Reporte mensual residuos | ResiduoQuimico, Reporte, Usuario |
| UC-LAB-10 - Gestionar categorias residuos | CategoriaResiduo |
| UC-LAB-11 - Historial de residuos | ResiduoQuimico |
| RF-19 - Disposicion final | DisposicionFinal, ResiduoQuimico, Usuario |

## 3.5 Seguridad y Reportes

| Flujo | Entidades participantes |
|---|---|
| UC-SEG-01 - Autenticacion | Usuario, Auditoria |
| UC-SEG-02 - Gestion de usuarios/roles | Usuario, Rol |
| UC-REP-01 - Reportes operativos | Reporte, Usuario |

---
# 4. Notas de Diseno Clave

- **Alta Temprana de Paciente**: el agente IA crea el registro solo con DNI y nombre; el resto de atributos se completan durante la consulta (UC-DIAG-01) o al registrar asistencia (UC-REC-15 paso 6). Esto permite agilizar el agendado sin exigir carga completa de datos.

- **Politica FEFO en Lote**: al retirar insumos, el sistema consume primero el lote con fecha de vencimiento mas proxima. El atributo dias_alerta_vencimiento en Insumo permite configurar la anticipacion de las alertas (UC-LAB-08).

- **Versionado de Fichas Clinicas (RF-20)**: cada modificacion de una ficha clinica preserva el contenido anterior como VersionFichaClinica, permitiendo auditoria clinica retroactiva.

- **Auditoria Transversal (RF-14)**: la entidad Auditoria registra automaticamente toda accion sensible (configuracion de agenda, bloqueos, validacion de analisis, modificaciones de pacientes, etc.) sin intervencion del usuario.

- **El Paciente no es Usuario (ACT-04)**: el paciente interactua de forma anonima via WhatsApp y portal OTP, sin credenciales de acceso a la plataforma interna. No existe una entidad de autenticacion para pacientes.

- **OTP con TTL de 7 dias**: el token de un solo uso expira a los 7 dias de generado. Una vez usado (descargado el informe), no puede reutilizarse. Esto cumple con el requisito de seguridad RNF-02.

- **Relacion 1 a 1 entre OTP e InformeResultados**: cada analisis validado genera exactamente un OTP y un InformeResultados. El OTP habilita exclusivamente la descarga de su informe asociado.
---
# 5. Explicaciones Conceptuales de Entidades Clave

## 5.1 ConfiguracionAgenda y BloqueoAgenda

Son dos cosas distintas que trabajan juntas para controlar la disponibilidad de turnos.

### ConfiguracionAgenda - la "plantilla" de horarios

Es un unico registro (tabla de configuracion) que define como se genera la agenda normal del laboratorio:

| Atributo | Que define |
|---|---|
| dias_habiles | Que dias se atiende ("L,M,X,J,V") |
| horario_inicio/fin_manana | Franja matutina (ej. 08:00-12:00) |
| horario_inicio/fin_tarde | Franja vespertina (ej. 14:00-18:00) |
| duracion_turno | Cada turno dura 20 min |
| intervalo_entre_turnos | 5 min entre turnos |
| max_turnos_por_franja | Max. turnos por bloque |
| periodos_inhabiles | Feriados/recesos fijos en JSON |

La clave: es la regla general. Solo hay una fila vigente. Cuando el sistema agenda un turno, mira esta config para saber que horarios existen. Si hay que cambiar horarios, se modifica este unico registro (queda registrado quien y cuando).

### BloqueoAgenda - la "excepcion" puntual

Es una restriccion temporal especifica que se superpone a la config para tapar un dia o una franja concreta, sin tocar la plantilla general.

Casos reales de uso:
- Mantenimiento de un equipo - bloqueo de dia completo.
- Feriado imprevisto (no estaba en periodos_inhabiles) - bloqueo de dia completo.
- Reunion de 11:00 a 12:00 - bloqueo de franja horaria.
- Vacaciones del bioquimico - bloqueo de varios dias (fecha_inicio a fecha_fin).

Atributos clave:
- tipo_bloqueo = Dia Completo (hora_inicio/hora_fin son nulas) o Franja Horaria (se indican horas).
- estado = Activo / Inactivo - permite "desbloquear" cuando termina la restriccion.
- motivo y usuario_id - trazabilidad de quien y por que lo bloqueo.

### Como funcionan juntos

ConfiguracionAgenda genera los turnos disponibles (plantilla); BloqueoAgenda descarta turnos en periodos puntuales (excepcion). Al validar un turno, el sistema pregunta: "este horario, esta dentro de la plantilla (Config) y NO esta bloqueado?". Si configura la mantiene la opcion; el bloqueo la elimina temporalmente.

---

## 5.2 FichaClinica y VersionFichaClinica - el historial

No existe una sola ficha por paciente para siempre. Hay que distinguir dos niveles:

1. Entre consultas: varias FichaClinica por paciente (cronologia de visitas). Un paciente con 5 consultas tendra 5 fichas clinicas, cada una con su fecha_consulta.
2. Dentro de una consulta: varias VersionFichaClinica por ficha (cronologia de ediciones de esa ficha).

FichaClinica = un registro por cada consulta/visita presencial.
VersionFichaClinica = el historial de cambios de UNA ficha en particular.

### El mecanismo de "version actual"

La idea es nunca perder lo que escribio el bioquimico, aunque despues lo corrija:

Estado inicial de una FichaClinica:
`
FichaClinica
  datos_clinicos = "{...v1...}"
  version_actual = 1   estado = Activo
`

El bioquimico modifica la ficha (UC-DIAG-08):

PASO 1 - Se COPIA el contenido anterior a VersionFichaClinica:
`
VersionFichaClinica n.1
  datos_previos = "{...v1...}"   (lo que habia)
  datos_nuevos  = "{...v2...}"   (lo nuevo)
  usuario_id, motivo, fecha
`

PASO 2 - Se actualiza la FichaClinica:
`
FichaClinica
  datos_clinicos = "{...v2...}"
  version_actual = 2   estado = Activo
`

Despues de N ediciones:
- FichaClinica apunta siempre al contenido vigente (datos_clinicos actual + version_actual = el numero mas alto).
- VersionFichaClinica guarda cada snapshot anterior, permitiendo reconstruir como estaba la ficha en la version 1, 2, 3... (auditoria clinica, RF-20).

estado de la ficha: Activo (la vigente), Modificado (transicion), Historico (cuando ya no es la que se usa).

Analogia: es como el historial de cambios de un documento. El documento (FichaClinica) siempre muestra la ultima version editada, pero en la lista de revisiones (VersionFichaClinica) queda guardada cada copia anterior por si hay que consultarla o deshacer.

---

## 5.3 Lote - que es y como funciona

### Por que existe

Un mismo Insumo (ej. el reactivo "Azul de Lactofenol") puede llegar al laboratorio en entregas distintas, cada una con diferente numero de lote del fabricante y diferente fecha de vencimiento. Si guardaramos solo el insumo con un stock total, no sabriamos cual vence primero. Por eso se separa en Lote.

### La relacion

`
Insumo (catalogo)  --1--  N--  Lote (instancias con fecha de vencimiento)
`

- Insumo = "que es" (definicion, unidad, categoria, ubicacion por defecto).
- Lote = "una partida concreta que llego" (numero de lote + vencimiento).

Ejemplo:
`
INSUMO "Azul de Lactofenol" (stock_actual = 200 ml)
|
|-- Lote A: num_lote="LP-2301"  vence 2026-03-10   cantidad_actual = 80 ml
|-- Lote B: num_lote="LP-2304"  vence 2026-08-22   cantidad_actual = 120 ml
`

### Ciclo de vida de un Lote

1. Ingreso (UC-LAB-01): llega una partida nueva - se crea un Lote con cantidad_inicial = lo recibido, fecha_vencimiento, numero_lote, cantidad_actual = cantidad_inicial, estado = Activo.

2. Retiro (UC-LAB-02): cuando se usa el insumo, se descuenta de un lote especifico. Aqui entra la politica FEFO (First Expiry, First Out): se consume primero el lote que vence antes. En el ejemplo se usaria el Lote A (vence 03-10) antes que el B (vence 08-22), evitando que caduque producto sin usar.

3. Movimiento (MovimientoInventario): cada ingreso/retiro/devolucion queda registrado y apunta al lote afectado, dando trazabilidad total ("de que partida salio lo usado?").

4. Estados del lote:
   - Activo: hay stock y no vencio.
   - Agotado: cantidad_actual llego a 0.
   - Vencido: paso su fecha_vencimiento sin agotarse (ya no se puede usar).

### El stock del Insumo

Insumo.stock_actual no se guarda a mano: es un calculo = suma de cantidad_actual de todos sus lotes activos. Cuando se consume o agrega un lote, el stock total del insumo se recalcula.

### Alerta de vencimiento

Insumo.dias_alerta_vencimiento (ej. 30) + Lote.fecha_vencimiento - el dashboard avisa con anticipacion los lotes que vencen dentro de 30 dias, para usarlos primero o gestionarlos (UC-LAB-08).

Analogia: el Insumo es "la leche larga vida" y el Lote es "la caja con tal fecha de vencimiento". Si tienes varias cajas con vencimientos distintos, necesitas saber cual abrir primero - eso es exactamente lo que resuelve el Lote + FEFO.
