# Sistema de Laboratorio — Brief de Diseño UX/UI

**Sistema:** SIGEMI — Sistema Integral de Gestión Micológica
**Fuentes:** Documento de Requisitos v0.0.0.1 (17/04/2026), Modelo Conceptual/Dominio/Datos, Presentación del proyecto.

## 1. Contexto del negocio

- **Tipo de laboratorio:** Laboratorio de **Micología** (diagnóstico de infecciones fúngicas / micosis) perteneciente al Módulo de Bioquímica y Farmacia de la **UNaM** — uso académico, prácticas con alumnos, investigación y diagnóstico a la comunidad.
- **Tamaño (usuarios, muestras/día):** ⚠️ FALTA DEFINIR. Referencias conocidas: turnos con análisis de hasta **1 mes** de espera; rutina diaria de cierre de agenda; no hay volumen registrado en los documentos.
- **Regulaciones aplicables:**
  - **Ley 25.326** (Protección de Datos Personales) — emisión de resultados vía portal seguro + OTP, descarga forzada solo tras doble validación.
  - **Reglamento nacional de residuos químicos 2026** — registro exacto de volumen (ml) y peso (g), reporte mensual consolidado.
  - **Resguardo legal de historias clínicas** — retención mínima **10 años**, backup diario, inmutabilidad de análisis validados (RNF-04).
  - Despliegue **local en servidores UNaM** (sin nube de terceros) — RNF-05.
- **Objetivo principal del sistema:** Digitalizar el flujo 100% manual del laboratorio de micología (turnos, ficha clínica, análisis, stock de reactivos y residuos) garantizando trazabilidad clínica, cumplimiento normativo y datos estructurados para investigación.
- **Métricas de éxito:** ⚠️ FALTA DEFINIR (ninguna declarada). Candidatas derivadas de los objetivos: % de espacios de agenda reutilizados tras cancelación, % de retiros sin lote vencido, % de registros de residuos completos (volumen+peso), tiempo de consulta con ficha digital vs. papel, n.º de resultados entregados sin retiro presencial.

## 2. Usuarios y roles

### Rol: Bioquímico / Doctor (ACT-01)
- **Descripción:** Núcleo clínico. Atiende la consulta, registra ficha clínica, ingresa muestras, ejecuta el análisis y **valida** resultados. También registra retiros de insumos y generación de residuos.
- **Frecuencia de uso:** ⚠️ FALTA DEFINIR (alto, es el rol operativo principal — todos los días de atención).
- **Tareas principales (top 5):**
  1. Registrar ficha clínica en consulta (UC-DIAG-01)
  2. Actualizar estado del análisis y cargar observaciones/hallazgos (UC-DIAG-03)
  3. Registrar ingreso de muestra (UC-DIAG-02)
  4. Validar análisis (UC-DIAG-04)
  5. Consultar panel de análisis / historial de paciente (UC-DIAG-09, UC-DIAG-06)
- **Tareas críticas (error grave):** **Validación de resultados** (firma del diagnóstico → genera informe PDF + OTP + notificación al paciente; irreversible), cancelación de análisis, modificación de ficha clínica.
- **Dispositivos y contexto físico:** ⚠️ FALTA DEFINIR. Contexto inferido: PC de escritorio en consultorio/recepción; posible tablet al lado del microscopio. Validar.
- **Nivel técnico:** ⚠️ FALTA DEFINIR (dominio clínico alto; informático desconocido).
- **Frustraciones actuales:** registro en papel durante la consulta, historiales extraviables/deteriorables, seguimiento manual de muestras con esperas de hasta 1 mes, datos ilegibles.

### Rol: Profesor (ACT-02)
- **Descripción:** Ámbito académico. Registra **retiros de insumos** para prácticas, **devoluciones** y la **generación de residuos químicos** de las prácticas. Consulta inventario y trazabilidad.
- **Frecuencia de uso:** ⚠️ FALTA DEFINIR (media; por práctica).
- **Tareas principales (top 5):**
  1. Registrar retiro de insumos para práctica (UC-LAB-02)
  2. Registrar generación de residuos (UC-LAB-03)
  3. Registrar devolución de insumos (UC-LAB-09)
  4. Consultar inventario (UC-LAB-05)
  5. Consultar trazabilidad de movimientos (UC-LAB-07)
- **Tareas críticas:** retiro correcto del lote FEFO (no usar reactivos vencidos), registro exacto de residuos (volumen/peso) por normativa.
- **Dispositivos y contexto físico:** ⚠️ FALTA DEFINIR (probablemente PC del laboratorio o estación de banco).
- **Nivel técnico:** ⚠️ FALTA DEFINIR.
- **Frustraciones actuales:** anotar residuos en **listas de papel**, verificar stock "de manera informal", encontrarse con reactivos **vencidos** en las prácticas.

### Rol: Administrador (ACT-03)
- **Descripción:** Gestión administrativa, logística y de seguridad. Registra **ingresos** de insumos, gestiona todos los catálogos, administra usuarios/roles, configura la agenda y genera reportes. Puede además operar como Bioquímico.
- **Frecuencia de uso:** Alta.
- **Tareas principales (top 5):**
  1. Registrar ingreso de insumos con lote (UC-LAB-01)
  2. Gestión de usuarios, roles y permisos (UC-SEG-02)
  3. Gestión de catálogos (tipos de análisis/muestra, insumos, categorías, ubicaciones, residuos) (RF-16/RF-17)
  4. Configuración de agenda y bloqueos (UC-REC-07/08)
  5. Generar reporte mensual de residuos y de inventario (UC-LAB-04, UC-LAB-13)
- **Tareas críticas:** configuración de agenda (impacta disponibilidad del Agente IA), bloqueos con turnos afectados, reporte mensual de residuos (consolida y cierra datos).
- **Dispositivos y contexto físico:** ⚠️ FALTA DEFINIR (PC de escritorio).
- **Nivel técnico:** ⚠️ FALTA DEFINIR.
- **Frustraciones actuales:** control de stock en **hojas sueltas**, escasez de materiales, uso ineficiente y uso de reactivos vencidos.

### Rol: Paciente (ACT-04)
- **Descripción:** Actor **externo**, sin cuenta en la plataforma. Dos superficies: **WhatsApp (Agente IA)** para autogestión de turnos, y **portal web seguro** (mobile-first, RNF-03) para descargar su informe con OTP.
- **Frecuencia de uso:** Baja por visita (estacional).
- **Tareas principales (top 5):**
  1. Agendar turno vía WhatsApp (UC-REC-01)
  2. Cancelar / reprogramar turno vía WhatsApp (UC-REC-02/03)
  3. Consultar turnos e indicaciones médicas (UC-REC-05)
  4. Ingresar OTP en el portal (UC-DIAG-05)
  5. Descargar informe PDF (UC-DIAG-05)
- **Tareas críticas:** descarga del resultado con doble verificación (DNI + OTP, TTL 7 días). No tiene credenciales internas.
- **Dispositivos y contexto físico:** **Móvil** (el portal es mobile-first obligatorio). WhatsApp en cualquier dispositivo.
- **Nivel técnico:** Bajo / heterogéneo (incluye adultos mayores; por eso el Agente IA es conversacional).
- **Frustraciones actuales:** reservar turno solo presencialmente/por teléfono, no poder reprogramar, retiro presencial del resultado (se elimina con SIGEMI).

## 3. Arquitectura de información

### Módulos principales
1. Panel de Control (dashboard) — incluye alertas de stock (RF-09)
2. Agenda y Turnos
3. Pacientes
4. Ficha Clínica (Registro de Información Clínica)
5. Análisis (Registro de Análisis)
6. Resultados (Emisión)
7. Stock de Insumos Reactivos
8. Control de Residuos
9. Reportes y Estadísticas
10. Catálogos (tipo de análisis, insumos, categorías, ubicaciones, residuos, indicaciones, equipos) — transversal
11. Usuarios / Roles y Permisos
12. Auditoría

### Jerarquía de navegación (árbol)
```
SIGEMI (web interna — Bioquímico/Profesor/Admin)
├── Panel de Control
├── Agenda y Turnos
│   ├── Agenda (día / semana / mes)
│   ├── Nuevo Turno (manual)
│   └── Configuración
│       ├── Parámetros de agenda
│       ├── Bloqueos (día completo / franja; global / recurso / grupo)
│       └── Indicaciones Médicas
├── Pacientes
│   ├── Listado / Búsqueda (DNI, nombre, apellido, estado)
│   ├── Nuevo / Editar Paciente
│   └── Perfil de Paciente
│       ├── Fichas clínicas (con versiones)
│       └── Análisis asociados
├── Análisis
│   ├── Panel de Análisis (worklist por estado)
│   ├── Nueva Consulta (Ficha Clínica)
│   ├── Ingreso de Muestra
│   └── Detalle de Análisis (hallazgos, estados, validación)
├── Resultados
│   ├── Informes emitidos (estado OTP)
│   └── [Portal paciente — externo, no navega aquí]
├── Insumos y Stock
│   ├── Inventario
│   ├── Ingreso de Insumos (lote)
│   ├── Retiro de Insumos (FEFO)
│   ├── Devolución
│   └── Trazabilidad de Movimientos
├── Residuos
│   ├── Registrar Residuo
│   ├── Disposición Final
│   ├── Historial de Residuos
│   └── Reporte Mensual
├── Reportes y Estadísticas
├── Equipos ⚠️ FALTA DEFINIR ALCANCE
├── Seguridad
│   ├── Usuarios
│   └── Roles y Permisos
└── Auditoría
```

### Entidades del dominio (catálogo compacto para UI)
> Los campos listados salen literal de `modelo_datos_sigemi.md`.

**Paciente** — núcleo del historial. No es usuario del sistema.
- Campos: `numero_registro` (string único, interno) · `dni` (string único) · `nombre` · `apellido` · `fecha_nacimiento` (date) · `edad` (calculada) · `sexo` (string) · `domicilio` · `telefono` (WhatsApp) · `correo_electronico` · `obra_social` · `estado` (Activo/Inactivo) · `fecha_ingreso` (datetime).
- Estado inicial posible: **Alta Temprana** (solo DNI + nombre, creado por el Agente IA); se completa en la consulta.

**Turno** (cita) — `fecha_hora` · `estado` (ver §6) · `reprogramaciones` (int, máx. 2) · `motivo_cancelacion` · `fecha_creacion` · `fecha_atencion`. Relaciones: → Paciente, → TipoAnalisis, → IndicacionMedica (0..1), → Recurso (sala/consultorio/laboratorio). En base de datos con `recurso_id` y `tipo_analisis_id`.

**FichaClinica** — `fecha_consulta` (datetime) · `version_actual` (int) · `estado` (Activo/Modificado/Histórico). Descompone sus campos clínicos en `DatoClinico` (`campo`, `valor`, `tipo_dato`: texto/selección/número). Todo cambio genera `VersionFichaClinica` (snapshots previo/nuevo + `motivo` obligatorio). → Paciente, → Usuario (registró), → 0..N AnalisisMicologico.

**AnalisisMicologico** — entidad central. `tipo_muestra` (plantilla de valores reales: **uñas, piel, cabello**) · `tipo_analisis_id` (catálogo) · `estado` (ver §6) · `fecha_creacion` · `fecha_validacion` · `motivo_cancelacion` (obligatorio si cancelado) · `bioquimico_validador_id`. Resultados estructurados en `HallazgoAnalisis` (`tipo_hallazgo`: **Observación / Resultado** + `dato` + `fecha`). Relaciones: nace de FichaClinica, se valida por Usuario, genera 1 Otp + 1 InformeResultados, consume MovimientoInventario, produce ResiduoQuimico.

**TipoAnalisis** (catálogo) — `nombre` · `descripcion` · `estado` (Activo/Inactivo). ⚠️ FALTA DEFINIR: los documentos no modelan **valores de referencia**, parámetros cuantitativos ni plantilla de campos por tipo de análisis. Confirmar si son necesarios para la UI.

**IndicacionMedica** — `titulo` · `contenido` (texto libre) · `tipo_analisis_id` (obligatorio) · `estado`. Se envía al agregar turno.

**Insumo** — `nombre` · `descripcion` · `unidad_medida` (**ml / g / unidades**) · `categoria_id` · `ubicacion_id` (default) · `stock_actual` (real, calculado de lotes activos) · `umbral_minimo` (real, default 1) · `dias_alerta_vencimiento` (int, default 30) · `estado`. → 0..N `Lote`.

**Lote** — `numero_lote` (string fabricante) · `fecha_ingreso` · `fecha_vencimiento` · `cantidad_inicial` · `cantidad_actual` (real) · `estado` (Activo/Agotado/Vencido). Regla **FEFO**: al retirar se consume primero el lote con vencimiento más próximo.

**MovimientoInventario** — `tipo_movimiento` (**Ingreso / Retiro / Devolución**) · `cantidad` · `lote_id` · `usuario_id` · `ubicacion_id` · `analisis_id` (0..1) · `practica_educativa` (si no es clínico) · `devolucion_referencia_id` (0..1) · `fecha`. Devolución de lote ya vencido se registra como "Vencido — no utilizable" (UC-LAB-09).

**ResiduoQuimico** — `categoria_residuo_id` (Clase I/II/III de peligrosidad) · `volumen` (ml, real) · `peso` (g, real) · `fecha_hora` · `usuario_id` · `analisis_id` (0..1) · `disposicion_final_id` (0..1) · `reporte_mensual_id` (0..1). Editable solo **antes** de consolidarse en reporte mensual.

**CategoriaResiduo** — `nombre` · `clase_peligrosidad` (I/II/III) · `descripcion` · pasos de `InstruccionAlmacenamiento` (secuenciales).

**Otp** — `codigo` (único) · `fecha_generacion` · `fecha_expiracion` (**TTL 7 días**) · `usado` (bool) · `fecha_uso`. 1:1 con InformeResultados (`ruta_archivo`, `hash_archivo`, `fecha_generacion`).

**Usuario** — `nombre` · `apellido` · `correo_electronico` (login, único) · `contrasena_hash` · `estado` (Activo/Inactivo/Bloqueado Temporal) · `intentos_fallidos` (bloqueo a 5) · `bloqueado_hasta`. **1 rol por usuario** (Administrador / Bioquímico-Doctor / Profesor).

**Auditoria** — `fecha_hora` · `direccion_ip` · `modulo` · `accion` (CREAR/MODIFICAR/ELIMINAR/VALIDAR…) · `entidad_afectada` · `entidad_id` + detalle por campo en `CambioAuditoria` (`campo`, `valor_anterior`, `valor_nuevo`).

**Equipo** (activo fijo, desacoplado de agenda) — `numero_serie` (único) · `nombre` · `marca` · `proveedor` · `fecha_adquisicion` · `garantia_hasta` · `estado` (Operativo/En Mantenimiento/Inhabilitado) · `requisitos_uso` + historial de `MantenimientoEquipo` (Preventivo/Correctivo, próximo control). ⚠️ Sin UC dedicado en requisitos → **FALTA DEFINIR** si entra en la versión UI.

## 4. Flujos críticos (paso a paso)

### Flujo complementario de mayor frecuencia — Gestión de turno (WhatsApp + agenda)
**Actores:** Paciente (WhatsApp/Agente IA), Bioquímico/Admin (web).
1. Paciente pide turno; el Agente IA pide DNI + nombre → **Alta Temprana**.
2. IA consulta agenda, muestra bloques y los **bloquea 10 min**.
3. Paciente elige → turno **Confirmado**; se envían indicaciones + recordatorio programado.
4. En la consulta: Bioquímico localiza turno en agenda → "Registrar Asistencia" → **Atendido** / **No Asistió** (libera bloque y dispara UC-REC-04).
5. **Edge cases:** DNI inválido (reingreso); timeout 10 min (libera); sin disponibilidad (ofrece alerta de cancelación); cancelación < 24 h (bloqueada para paciente); cancelación libera hueco → reasignación automática recursiva (mensaje nocturno 22:00–08:00 se difiere a 08:00; plazo de respuesta 2 h); turnos vencidos sin atender → job diario marca **No Asistió**.

### 1. Flujo: Recepción de muestra
**Actores:** Bioquímico/Doctor.
1. Desde el turno **Atendido**, se habilita "Nueva Consulta" (o desde Pacientes → buscar DNI).
2. Se registra la **Ficha Clínica** (datos demográficos pre-cargados del alta temprana + campos clínicos estructurados).
3. Se presiona **"Ingresar Muestra"**: se selecciona tipo de muestra (uñas/piel/cabello…) y tipo de análisis; observaciones iniciales.
4. El sistema crea `AnalisisMicologico` en **Pendiente**, ligado a la ficha. Redirige al panel.
- **Edge:** DNI inexistente → alta manual de emergencia; ficha no guardada → no permite ingresar muestra (paso secuencial).
- **Errores:** error 500 → aborta transacción sin datos parciales; "Paciente no encontrado" → formulario de registro manual.

### 2. Flujo: Asignación y ejecución del estudio
**Actores:** Bioquímico/Doctor.
1. Abre **Panel de Análisis** (worklist filtrable: estado, tipo, fecha, bioquímico).
2. Abre el análisis → ve cronograma de muestra, hallazgos y línea de tiempo de estados.
3. Carga **Observación** o **Resultado parcial** (HallazgoAnalisis) y avanza estado: Pendiente → **En Proceso** → **Terminado**.
4. Si la muestra no es viable: **Cancelar** con `motivo_cancelacion` **obligatorio** (solo desde Pendiente/En Proceso).
- **Edge:** cancelar un análisis Validado está bloqueado; estado actual se mantiene si no se registra hallazgo; el consumo de insumos del análisis puede asociarse a un `MovimientoInventario` (trazabilidad clínica).

### 3. Flujo: Validación de resultados (control de calidad clínico)
**Actores:** Bioquímico/Doctor (único rol que firma).
1. Análisis debe estar **Terminado**.
2. El Bioquímico revisa hallazgos y emite diagnóstico final → **"Validar"**.
3. El sistema: estado → **Validado** (permanente) · compila **PDF** (hash de integridad) · genera **OTP** (TTL 7 días) · envía WhatsApp con enlace + instrucciones + token (sin datos clínicos en el mensaje).
4. Paciente en portal (mobile): ingresa **DNI + OTP** → descarga el PDF → OTP se invalida (1 solo uso).
- **Edge:** OTP usado/expirado → acceso denegado con mensaje claro; PDF no generado → no se notifica (fallo de sistema visible en auditoría).
- **Decisiones UI:** ⚠️ confirmar si la validación exige confirmación reforzada (teclear DNI del validador / motivo) — los documentos no lo establecen.

### 4. Flujo: Gestión de QC del inventario (reactivos: FEFO, vencimientos, umbrales)
> ⚠️ NOTA: no existe un módulo de QC formal (sueros control, Levey-Jennings) en los requisitos. El "control de calidad" del inventario se expresa como FEFO + alertas. Si el laboratorio necesita QC estadístico real, es **FALTA DEFINIR**.
1. **Ingreso** (Admin): registra insumo/lote con `numero_lote` + `fecha_vencimiento` + cantidad → stock se incrementa.
2. **Retiro** (Bioquímico/Profesor/Admin): selecciona insumo; el sistema proponer consumir el **lote FEFO** (vto. más próximo); obliga a asociar análisis o práctica educativa.
3. El sistema deduce stock; si cae bajo `umbral_minimo` o un lote entra en `dias_alerta_vencimiento` → **alerta en dashboard**.
4. **Devolución**: revierte total/parcial un retiro (referencia al movimiento original). Si el lote venció → "Vencido — no utilizable".
- **Edge:** stock insuficiente bloquea el retiro; devolución > retiro rechazada; retiro de insumo inactivo bloqueado.

### 5. Flujo: Auditoría / trazabilidad
**Actores:** Admin (consulta), el sistema (registra todo, silenciosamente).
1. Toda acción crítica genera `Auditoria` automática: usuario, fecha/hora, IP, módulo, acción, entidad, y por-campo en `CambioAuditoria`.
2. Eventos mínimos documentados: login/fallos de login, config de agenda, bloqueos, validación de análisis, modificación de pacientes, modificación de residuos, movimientos de inventario, cancelaciones.
3. El Admin consulta el log filtrable (módulo, usuario, rango, entidad) — **solo lectura, inmutable**.
- **Edge:** el log no es editable ni borrable por ningún rol; la consulta debe soportar exportación para auditorías externas.

## 5. Pantallas necesarias

> Cada screen lista: objetivo · usuario principal · datos · acciones · estados especiales.

### Acceso y global
- **Login** — Autenticar con correo institucional + contraseña. · Bioquímico/Profesor/Admin · Datos: correo, contraseña · Acciones: Ingresar, recuperar (⚠️ sin flujo definido) · Estados: error genérico "Credenciales inválidas", cuenta **Bloqueada Temporal** (indica tiempo restante, bloqueo a 5 fallos).
- **Panel de Control (Dashboard)** — Resumen operativo + alertas de stock. · Todos · Datos: alertas de stock bajo y vencimientos próximos (RF-09), conteo de análisis por estado, turnos del día, residuos del mes ⚠️ (contenido exacto FALTA DEFINIR) · Acciones: navegar a módulos, atender alertas · Estados: sin alertas (vacío OK), loading.
- **Auditoría** — Consultar log inmutable. · Admin · Datos: fecha/hora, IP, usuario, módulo, acción, entidad, valores previo/nuevo por campo · Acciones: filtrar (módulo, usuario, rango, entidad), exportar · Estados: empty "sin eventos en el rango".

### Agenda y Turnos
- **Agenda (día/semana/mes)** — Visualizar y gestionar grilla de turnos y bloqueos. · Bioquímico/Admin · Datos: franjas por Recurso (sala/consultorio/laboratorio), turno (hora, paciente, tipo de análisis, estado), bloqueos (NO DISPONIBLES) · Acciones: filtrar (DNI, estado), nuevo turno, marcar asistencia, cancelar/reprogramar, bloquear franja · Estados: día sin turnos, franja ocupada entre consulta y confirmación, vista < 2 s.
- **Nuevo Turno** — Agendar manualmente. · Bioquímico/Admin · Datos: DNI paciente, fecha, horario disponible, tipo de análisis, (indicación automática) · Acciones: buscar paciente (si no existe → alta), confirmar, cancelar · Estados: DNI inexistente → extensión a alta; horario ya ocupado.
- **Detalle/Acciones de Turno** — Marcar Presente/Ausente, cancelar, reprogramar. · Bioquímico/Admin · Datos: paciente, fecha/hora, análisis, recurso, contador de reprogramaciones, motivo · Acciones: Presente/Ausente (motivo opcional), Cancelar (confirmación; <24 h requiere confirmación explícita extra), Reprogramar (máx. 2; requiere aval del Admin en el 3.º) · Estados: ya marcado → acción bloqueada.
- **Configuración de Agenda** — Definir días hábiles, franjas, duración, intervalo, máx. por franja. · Admin · Acciones: guardar (valida consistencia horaria) · Estados: error de validación (hora fin < inicio) sin persistir.
- **Bloqueos de Agenda** — Bloquear/desbloquear día completo o franja (global / por recurso / por grupo). · Admin · Datos: período, tipo, motivo, alcance, precedencia · Estados: turnos activos en el rango → aviso y opción de cancelar/reprogramar antes de aplicar.
- **Indicaciones Médicas** — CRUD de indicaciones por tipo de análisis. · Bioquímico/Admin · Datos: título, contenido, tipo de análisis (obligatorio), estado · Acciones: crear, modificar, eliminar (baja lógica con confirmación) · Estados: vacío → CTA "crear primera indicación".

### Pacientes y Ficha Clínica
- **Listado de Pacientes** — Buscar y paginar. · Bioquímico/Admin · Datos: n.º de registro, DNI, nombre, apellido, estado, edad calculada · Acciones: filtros (DNI exacto, nombre/apellido parcial, estado), nuevo, ver perfil · Estados: 0 resultados → "No se encontraron pacientes" + CTA crear; carga > 2 s.
- **Perfil de Paciente** — Historial clínico acumulado. · Bioquímico/Admin · Datos: demográficos, fichas clínicas (con versión), análisis con estado, resultados · Acciones (solo lectura salvo edición/desactivación) · Estados: paciente Inactivo (banner), sin fichas aún.
- **Registro/Edición de Paciente** — Datos demográficos. · Bioquímico/Admin/⚠️ recepción · Datos: los campos de §3 · Acciones: guardar, desactivar (con motivo obligatorio; bloqueado si hay turnos futuros vigentes) · Estados: DNI duplicado → muestra el existente y ofrece editar; fecha de nacimiento **no editable** si el paciente ya tiene análisis.
- **Nueva Consulta (Ficha Clínica)** — Carga estructurada en la consulta. · Bioquímico · Datos: demográficos pre-cargados + campos clínicos (DatoClinico, dinámicos según tipo de dato) · Acciones: guardar ficha → habilita "Ingresar Muestra" · Estados: campos obligatorios vacíos, error 500 sin persistencia.
- **Historial de Versiones de Ficha** — Ver diff previo/nuevo + motivo. · Bioquímico/Admin · Solo lectura.

### Análisis
- **Panel de Análisis (worklist)** — Volumen de trabajo del laboratorio. · Bioquímico (Admin) · Datos: tabla paginada: n.º/lote de análisis, paciente, tipo de muestra, tipo de análisis, estado (color), fecha de ingreso, bioquímico asignado, días en estado ⚠️ (FALTA DEFINIR si se muestra SLA) · Acciones: filtrar por estado/tipo/fecha/bioquímico, abrir detalle, avanzar estado, cancelar, validar · Estados: columnas por estado, vacío "no hay análisis en este filtro".
- **Detalle de Análisis** — Ciclo de vida de la muestra. · Bioquímico · Datos: datos de muestra y ficha, hallazgos (Observación/Resultado) con fecha, línea de tiempo de estados, validador y fecha de validación, vínculos a movimientos de inventario y residuos · Acciones: agregar hallazgo, avanzar/cancelar/validar · Estados: deshabilitar acciones no permitidas según estado.
- **Ingreso de Muestra** — Alta del análisis. · Bioquímico · Datos: tipo de muestra, tipo de análisis, observaciones iniciales · Acciones: registrar → Pendiente · Estados: paso bloqueado si no hay ficha guardada.
- **Catálogo de Tipos de Análisis/Muestra** — CRUD admin. · Admin · Datos: nombre, descripción, estado · Acciones: crear, modificar, desactivar (baja lógica preserva históricos).

### Resultados
- **Informes Emitidos** — Estado de entrega. · Bioquímico/Admin ⚠️ (ver quién lo consulta) · Datos: informe (PDF, hash, fecha), OTP (estado: vigente/usado/expirado), paciente, fecha de expiración, confirmación de envío WhatsApp · Acciones: reenviar ⚠️ (no definido), ver registro de auditoría de descarga · Estados: OTP expirado → opción de regeneración ⚠️ (no definida en requisitos).
- **Portal de Resultados (paciente, mobile-first)** — Descarga segura. · Paciente · Datos: campos de verificación (DNI + OTP) · Acciones: validar y descargar · Estados: OTP inválido, usado, expirado (TTL 7 d), éxito con descarga; sin datos clínicos en pantalla previa a validar · ⚠️ Doble verificación "DNI + OTP" exigida por RF-08 y presentación.

### Stock de Insumos
- **Inventario** — Estado del stock. · Los 3 roles · Datos: insumo, categoría, ubicación, unidad (ml/g/unid.), stock actual vs. umbral, lote en uso, vencimiento más próximo · Acciones: filtros (nombre, categoría, próximos a vencer/agotar), abrir detalle, ingresar/retirar/devolver · Estados: alertas visuales por umbral y vencimiento; insumo inactivo.
- **Ingreso de Insumos** — Alta de lote. · Admin · Datos: insumo, n.º lote, cantidad, fecha de vencimiento, ubicación · Acciones: guardar → incrementa stock, registra movimiento · Estados: validación de fecha vencimiento > hoy.
- **Retiro de Insumos** — Consumo. · Profesor/Bioquímico/Admin · Datos: insumo, cantidad, lote (propuesto **FEFO**), destino (análisis o práctica educativa), ubicación · Acciones: confirmar, cancelar · Estados: stock insuficiente → bloqueo; alerta post-retiro si cae bajo umbral.
- **Devolución de Insumos** — Reversión parcial/total. · Profesor/Bioquímico/Admin · Datos: retiro original (referencia), cantidad a devolver, estado del lote · Estados: lote vencido → "Vencido — no utilizable".
- **Trazabilidad de Movimientos** — Historial cronológico. · 3 roles · Datos: fecha, tipo (Ingreso/Retiro/Devolución), usuario, cantidad, lote, análisis/práctica, ubicación · Acciones: filtros (insumo, tipo, rango, usuario), exportar · Estados: vacío por filtro.
- **Catálogos de Inventario** — Categorías de insumo, ubicaciones, insumos (umbrales y días de alerta). · Admin.

### Residuos
- **Registro de Residuo** — Carga de volumen y peso exactos. · Profesor/Bioquímico/Admin · Datos: categoría (Clase I/II/III, con instrucciones de almacenamiento visibles), volumen (ml), peso (g), fecha/hora, análisis o práctica origen, descripción · Acciones: registrar, guardar borrador ⚠️ (no definido) · Estados: validación de valores numéricos > 0.
- **Historial de Residuos** — Listado y corrección. · 3 roles · Datos: fecha, categoría, volumen, peso, usuario, estado de consolidación · Acciones: filtrar (fecha, categoría, usuario), editar **solo antes de consolidación en reporte mensual** · Estados: registro consolidado → solo lectura.
- **Disposición Final** — Cierre del ciclo. · Admin/Bioquímico ⚠️ · Datos: responsable, fecha, método de tratamiento, residuos incluidos · Acciones: registrar disposición · Estados: sin residuos pendientes de disposición.
- **Reporte Mensual de Residuos** — Documento normativo. · Admin · Datos: mes/año, consolidado por categoría (volumen/peso), generados vs. dispuestos · Acciones: generar PDF, descargar · Estados: mes vacío → aviso de "sin registros".

### Reportes
- **Reportes y Estadísticas** — Consolidación y exportación. · Bioquímico/Admin · Datos: selector tipo (Clínico/Inventario/Residuos), rango de fechas, previsualización en tabla · Acciones: generar previsualización, exportar CSV/XLSX/PDF · Estados: sin datos en el rango ("No existen registros transaccionales para los parámetros indicados"); **reporte clínico → anonimización estricta** (remoción de datos sensibles) antes de exportar.

### Seguridad
- **Usuarios** — CRUD de cuentas. · Admin · Datos: nombre, apellido, correo (login), rol, estado, intentos fallidos/bloqueo · Acciones: alta, edición, baja lógica, asignación de rol · Estados: cuenta bloqueada temporalmente.
- **Roles y Permisos** — Ver/definir matrices por rol. · Admin · Datos: permisos por pantalla/acción según Rol (Administrador / Bioquímico-Doctor / Profesor).

### ⚠️ FALTA DEFINIR
- **Equipos** (activo fijo: microscopio, autoclave, centrífuga): listado, ficha (serie, marca, garantía, estado, requisitos de uso), mantenimientos preventivos/correctivos y próximo control — modelados en la BD pero **sin caso de uso** en requisitos. Confirmar si se diseña en esta iteración.

## 6. Sistema de estados

| Estado | Significado | Color sugerido | Transiciones permitidas |
|---|---|---|---|
| **Turno — Pendiente** | Agendado vía Agente IA, sin confirmación plena/registrado | `gris` | → Confirmado, Cancelado |
| **Turno — Confirmado** | Reservado con fecha/hora fijada | `azul` | → Atendido, No Asistió, Cancelado, Reprogramar (≤2 veces) |
| **Turno — Atendido** | Paciente asistió y se inició la consulta | `verde` | — (terminal; habilita Ficha → Muestra) |
| **Turno — No Asistió** | No vino; bloque liberado; dispara reasignación | `rojo suave` | — (terminal) |
| **Turno — Cancelado** | Anulado (paciente o personal); bloque liberado | `rojo` | — (terminal; dispara UC-REC-04) |
| **Análisis — Pendiente** | Muestra ingresada, sin procesamiento | `gris` | → En Proceso, Cancelado |
| **Análisis — En Proceso** | Muestra en cultivo/procesamiento, con hallazgos parciales | `ámbar` | → Terminado, Cancelado |
| **Análisis — Terminado** | Procesamiento concluido, pendiente de firma | `azul` | → Validado (solo Bioquímico) |
| **Análisis — Validado** | Firma del bioquímico; **permanente e inmutable**; genera PDF + OTP | `verde` | — (terminal; sin transiciones) |
| **Análisis — Cancelado** | Baja con `motivo_cancelacion` **obligatorio** (solo desde Pendiente/En Proceso) | `rojo` | — (terminal; queda en historial) |
| **Análisis — Derivado** | Muestra derivada ⚠️ (sin UC que describa el flujo de derivación) | `violeta` | ⚠️ FALTA DEFINIR |
| **Lote — Activo** | Disponible para consumo (FEFO: se consume primero el que vence antes) | `verde` | → Agotado el consumirse; → Vencido al pasar la fecha |
| **Lote — Agotado** | Cantidad remanente = 0 | `gris` | — |
| **Lote — Vencido** | Pasó `fecha_vencimiento`; no consumible | `rojo` | — |
| **OTP — Vigente** | Generado, sin usar, dentro de TTL 7 días | `verde` | → Usado / Expirado |
| **OTP — Usado / Expirado** | Consumido o TTL vencido; descarga denegada | `gris/rojo` | — (regeneración ⚠️ no definida) |
| **Paciente — Activo / Inactivo** | Activo: recibe turnos · Inactivo: baja lógica, historial intacto | `verde / gris` | Activo ↔ Inactivo (solo Admin, con motivo) |
| **Usuario — Activo / Inactivo / Bloqueado Temporal** | Acceso habilitado / baja lógica / 5 fallos de login (desbloqueo automático) | `verde / gris / rojo` | Bloqueado Temporal → Activo (automático por tiempo) |
| **Insumo — Activo / Inactivo** | Catálogo habilitado / deshabilitado (preserva movimientos) | `verde / gris` | — |
| **FichaClínica — Activo / Modificado / Histórico** | Versión vigente / tiene versionado / versión previa | `azul / ámbar / gris` | Activo → Modificado al editar (se genera versión) |

**Reglas transversales:** color + icono/etiqueta de texto siempre juntos (accesibilidad); estados terminales (Validado, Cancelado) sin acción destructiva; toda transición crítica (validación, cancelación, bloqueo, modificación) se audita automáticamente (RF-14).

## 7. Design Tokens sugeridos

- **Paleta semántica** (mapeo por estado clínico/normativo, no decorativo):
  - `primary/azul` — acción y navegación principal (el laboratorio es contextos de lectura de datos; el azul no compite con los estados).
  - `éxito/verde` — Validado, Atendido, Activo, OTP vigente, stock OK.
  - `aviso/ámbar` — En Proceso, stock bajo umbral, vencimiento próximo (dentro de `dias_alerta_vencimiento`), Modificado.
  - `peligro/rojo` — Cancelado, No Asistió, Vencido, Bloqueado, deshabilitado.
  - `neutral/gris` — Pendiente, Inactivo, Histórico, registros de solo lectura.
  - `info/derivado*` — violeta para Derivado. (*Estado sin flujo definido; ajustar.)
  - La escala neutra: fondos claros (escala de grises azulados), texto de máximo contraste en paneles de trabajo por iluminación del laboratorio.
  - Justificación de dominio: el personal escanea worklists rápidamente; el código de color debe seguir el ciclo de vida clínico (semáforo), **no la marca institucional**. Para residuos, la clase de peligrosidad (I/II/III) debe tener etiquetado propio (⚠️ validar con normativa local si se asigna color por clase).
- **Tipografía:** UI sans (Inter o similar), 13–14 px para tablas/forms. **Monoespaciada** (JetBrains Mono / IBM Plex) reservada a: número de registro, **DNI**, **número de lote**, **código OTP**, **número de serie** y hashes — IDs que el personal copia/verifica contra etiquetas físicas.
- **Densidad:** alta. Tablas paginadas (no scroll infinito) con celdas de altura 32–40 px; worklist de análisis como vista principal, no tarjetas. Formularios de una sola columna en flujos de consulta (entrada rápida).
- **Modo:** **claro como principal** (luz del laboratorio, lectura de etiquetas y PDFs); **oscuro opcional** solo para sesiones prolongadas si el equipo lo confirma. El **portal paciente (OTP) claro y mobile-first** obligatorio por RNF-03. ⚠️ Confirmar contraste exigido por accesibilidad institucional.

## 8. Anti-patrones a evitar

1. **Animaciones largas o transiciones tipo "marketing"** en el worklist de análisis: el bioquímico escanea decenas de filas; cualquier transición > 150 ms entorpece.
2. **Modales para confirmar la validación de resultados**: la firma de un diagnóstico debe ser **un gesto explícito en contexto** (panel de validación con resumen del informe + confirmación reforzada), no un alert que se cierre con Enter.
3. **Borrar físicamente cualquier registro**: todo es baja lógica (pacientes, análisis, insumos, usuarios) — la UI nunca debe ofrecer "eliminar" permanente.
4. **Perder el número de lote en el retiro**: el retiro debe mostrar el **lote FEFO sugerido**, no una cifra agregada sin lote; la trazabilidad es el corazón de RF-18.
5. **Confirmación destructiva sin motivo**: cancelación de análisis y desactivación de paciente exigen campo de motivo **obligatorio** — no usar "¿Está seguro?" genérico.
6. **Toast efímero como única respuesta de error**: errores de validación que bloquean un guardado deben ser **inline y persistentes** (el flujo de consulta no puede fallar en silencio).
7. **Color como único codificador de estado**: siempre estado escrito + icono; no solo píldora de color (daltonismo y fotos en investigación).
8. **Dashboards de métricas decorativas**: el panel de control debe mostrar **alertas operativas** (stock, vencimientos, análisis a validar), no KPIs de marketing.
9. **Carga masiva al abrir inventario**: listados paginados/filtrables desde el inicio; sin render de 50.000 movimientos.
10. **Drag & drop como única forma de reprogramar turnos** en la agenda: ofrecer también diálogo accesible (móvil/tablet, pantallas táctiles).
11. **Cerrar la sesión sin aviso en puestos compartidos**: al ser laboratorio universitario, la sesión debe expirar y avisar, sin perder trabajo no guardado.
12. **Ocultar la expiración del OTP**: el portal del paciente debe comunicar claramente vigencia/consumo del token; un "token inválido" seco genera reclamos.

## 9. Preguntas abiertas para el stakeholder

1. **Volumen operativo:** ⚠️ ¿Cuántos usuarios por rol, turnos/día y análisis activos espera el sistema en producción? (condiciona densidad y paginación).
2. **Dispositivos:** ⚠️ ¿Qué hardware real usarán Bioquímicos/Profesores en banco (PC, tablet, pantalla táctil)? ¿Hay acceso a la web desde el banco de cultivo o solo desde consultorio/recepción?
3. **Qué es "Derivado":** ⚠️ El estado `Derivado` del análisis no tiene caso de uso. ¿A qué corresponde (derivar a otro laboratorio, otro profesional) y quién lo ejecuta?
4. **Valores de referencia:** ⚠️ ¿Los tipos de análisis necesitan valores de referencia o unidades por parámetro, o los resultados son cualitativos (Observación/Resultado libre) como modela SIGEMI?
5. **QC formal:** ⚠️ ¿El laboratorio requiere control de calidad estadístico (sueros control, gráficos de Levey-Jennings) o el "QC" queda cubierto por validación del bioquímico + FEFO/alertas de reactivos?
6. **Resultado crítico:** ⚠️ ¿Debe existir un flujo/alerta especial cuando un hallazgo es un resultado crítico, o todos los resultados siguen el mismo camino hasta la validación?
7. **Reenvío de resultados:** ⚠️ Si el OTP expira (7 días) o el paciente pierde el mensaje, ¿el laboratorio puede regenerar/re-notificar? (RF/RNF no lo definen).
8. **Regeneración y tipo de informe:** ⚠️ ¿El PDF del informe tiene plantilla/logo UNaM definida? ¿Quiénes aparecen como firmantes (bioquímico validador, director)? ¿Se conserva PDF/A para 10 años?
9. **Notificaciones internas:** ⚠️ ¿Los Bioquímicos quieren avisos in-app/correo cuando una muestra está próxima a vencerse en su etapa, o solo el panel basta?
10. **Equipos:** ⚠️ ¿La gestión de equipos (microscopios, autoclaves, mantenimiento) entra en la versión UI o queda fuera del alcance v1?
11. **Roles y matiz de permisos:** ⚠️ ¿El rol Profesor ve datos clínicos de pacientes, o solo inventario/residuos? ¿El Administrador ve resultados clínicos completos?
12. **Accesibilidad/idioma:** ⚠️ ¿Español como único idioma de interfaz? ¿Nivel de accesibilidad exigido (WCAG)? ¿DPI/monitores físicos (4K en recepción, o 1366×768 antiguos)?
13. **Sesiones:** ⚠️ ¿Timeout de inactividad y política de contraseñas definidos? (el modelo soporta intentos fallidos y bloqueo temporal, pero no el prefijo temporal).
14. **Nomenclatura visual institucional:** ⚠️ ¿Hay manual de identidad UNaM (colores/logo) que deba convivir con la paleta semántica clínica?

## 10. Prompts sugeridos para Figma AI

**1) Panel de Análisis (worklist)**
> Pantalla de trabajo tipo back-office para laboratorio de micología: tabla densa de análisis con columnas N.º análisis, paciente, tipo de muestra (uñas/piel/cabello), tipo de análisis, estado en píldora de color (Pendiente=gris, En Proceso=ámbar, Terminado=azul, Validado=verde, Cancelado=rojo, Derivado=violeta), fecha ingreso y bioquímico. Filtros arriba: estado, tipo, fecha, bioquímico. Botón "Nueva Consulta". Sin animaciones, filas de 36px, monoespaciada para IDs. Estilo limpio, sidebar izquierda con módulos.

**2) Agenda de Turnos**
> Pantalla de agenda de laboratorio con vista semanal de calendario: columnas por recurso (Sala 3, Laboratorio B), bloques de turno con nombre de paciente, hora, tipo de análisis y estado de turno con color; franjas bloqueadas en gris rayado estilo "no disponible". Barra superior con selector de día/semana/mes, filtro por DNI y botón "Nuevo Turno". Diálogo al hacer clic en bloque para marcar Presente/Ausente, cancelar o reprogramar. Estilo denso y legible, fuente 13px.

**3) Ficha Clínica + Ingreso de Muestra**
> Pantalla de consulta clínica en un paso fluido: encabezado con datos del paciente (DNI, edad calculada, obra social), formulario de una columna con campos clínicos estructurados, y al pie botón "Guardar Ficha" que habilita "Ingresar Muestra" con selector de tipo de muestra y tipo de análisis y observaciones iniciales. Avisos de validación inline en rojo. Estilo médico-limpio, alto contraste, sin degradados.

**4) Detalle de Análisis (ejecución y validación)**
> Pantalla de detalle de un análisis micológico: línea de tiempo vertical de estados (pendiente → en proceso → terminado → validado), campos de muestra y ficha asociada, panel de hallazgos con botones "Nueva Observación" y "Nuevo Resultado", y panel lateral fijo "Validar estudio" con resumen del diagnóstico, validador y botón de confirmación reforzada. Botón "Cancelar análisis" solo visible en Pendiente/En Proceso pidiendo motivo obligatorio. Tipografía monoespaciada para el código de análisis.

**5) Inventario de Insumos (stock + alertas)**
> Pantalla de inventario de reactivos de laboratorio: tabla con insumo, categoría, ubicación (Estante A-3), unidad de medida (ml/g/unid.), stock actual vs umbral mínimo, lote en uso y vencimiento más próximo; filas con alerta ámbar si stock bajo umbral o vence pronto y rojo si vencido. Filtros por nombre, categoría y "próximos a vencer/agotar". Botones "Ingreso", "Retiro" y "Devolución" que abren formularios laterales mostrando el lote FEFO sugerido.

---

**Nota:** brief extraído exclusivamente de los documentos de SIGEMI. Todo hueco real de información está marcado como `⚠️ FALTA DEFINIR`, concentrado en §9. Al validar las respuestas del stakeholder, refinar §5, §6 y §10.