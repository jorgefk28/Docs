# Análisis de Completitud — Subsistema Laboratorio Bioquímico (DIAG) y Subsistema Recursos de Laboratorio (LAB)

**Propósito:** Validar antes de editar el documento principal `TF_2026_Requerimientos_KLUKA_JORGE.md`.
**Fecha:** 31/07/2026

---

## 1. DIAG: Flujos de Trabajo Cubiertos por UC

| UC Actual | Flujo Cubierto | ¿Tiene UCE? |
|---|---|---|
| UC–DIAG-01 | Registrar Ficha Clínica (durante la consulta presencial) | Sí (UCE–DIAG-01) |
| UC–DIAG-02 | Registrar Ingreso de Muestra (inicio de trazabilidad del análisis) | Sí (UCE–DIAG-02) |
| UC–DIAG-03 | Actualizar Estado de Análisis (cargar resultados parciales y avanzar estado) | **NO** |
| UC–DIAG-04 | Validar Análisis (diagnóstico final, cierre clínico, dispara generación de PDF y notificación) | **NO** |
| UC–DIAG-05 | Notificación de Resultados (generación de OTP, envío de WhatsApp al paciente) | **NO** |
| UC–DIAG-06 | Descargar Informe (paciente ingresa OTP en portal web, descarga PDF) | **NO** |
| UC–DIAG-07 | Consultar Ficha Clínica (listar pacientes, filtrar, ver historial acumulado) | **NO** |

**Resumen DIAG:** 7 UC definidos, 2 UCE desarrollados, 5 UCE pendientes de escritura.

---

## 2. DIAG: Flujos de Trabajo Faltantes (No Documentados)

### 2.1 Nivel Estratégico — ¿Qué falta para que el subsistema sea completo?

| # | Flujo Faltante | Justificación |
|---|---|---|
| F1 | **Modificar Ficha Clínica** | El médico puede cometer errores al registrar la ficha o necesitar agregar información posterior (ej. resultados de anamnesis que llegan después). No hay UC para editar una ficha ya guardada. |
| F2 | **Cancelar / Anular Análisis** | Una muestra puede contaminarse, perderse, o el paciente puede desistir. No existe forma de cancelar un análisis en curso. |
| F3 | **Reabrir Análisis Validado** | Si tras la validación se detecta un error en el diagnóstico, debe existir un mecanismo controlado para revertir el estado «Validado» y corregir. |
| F4 | **Reenviar OTP / Notificación** | El paciente puede perder el mensaje de WhatsApp, cambiar de teléfono, o el OTP puede expirar sin uso. El personal debe poder reenviar la notificación. |
| F5 | **Consultar Análisis (Panel de Trabajo)** | DIAG-07 lista fichas clínicas de pacientes, pero el bioquímico necesita un panel de trabajo donde vea todos los análisis por estado (pendientes, en proceso, etc.) sin navegar paciente por paciente. |
| F6 | **Gestionar Tipos de Análisis / Tipos de Muestra** | El sistema referencia «Tipo de Muestra» y «Tipo de Análisis» en DIAG-02, pero no existe UC para administrar ese catálogo (crear, modificar, desactivar tipos). |
| F7 | **Registrar Observaciones de Cultivo (Seguimiento Periódico)** | En micología, los cultivos pueden tardar semanas. El sistema debe permitir registrar observaciones periódicas (día 7, día 14, día 21) sin cambiar el estado del análisis cada vez. |
| F8 | **Asignar Análisis a Bioquímico** | En un laboratorio con múltiples profesionales, los análisis deben poder asignarse a un bioquímico responsable. |
| F9 | **Derivar Muestra a Laboratorio Externo** | Puede ser necesario enviar una muestra a otro laboratorio para análisis complementarios. El sistema debe registrar la derivación y su resultado. |

---

## 3. DIAG: Propuesta de Nuevos Casos de Uso

### UC–DIAG-08 — Modificar Ficha Clínica

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-05 |
| **Descripción** | El Bioquímico/Doctor modifica una ficha clínica previamente registrada, corrigiendo errores o agregando información complementaria. |
| **Actor** | Bioquímico/Doctor, Administrador |
| **Precondición** | La ficha clínica debe existir y no estar asociada a un análisis en estado «Validado». |
| **Postcondiciones** | Los cambios quedan registrados. Se almacena una versión histórica de la ficha original (audit trail de modificaciones). |
| **Comentarios** | Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Cuando el análisis ya fue validado, la modificación se restringe a campos no clínicos (ej. observaciones administrativas). |

### UC–DIAG-09 — Cancelar Análisis

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Bioquímico/Doctor cancela un análisis micológico en curso, registrando el motivo. |
| **Actor** | Bioquímico/Doctor, Administrador |
| **Precondición** | El análisis debe existir y estar en estado «Pendiente» o «En Proceso» (no «Validado»). |
| **Postcondiciones** | El estado del análisis cambia a «Cancelado». Se registra el motivo obligatorio de cancelación. El análisis cancelado permanece en el historial del paciente. |
| **Comentarios** | Un análisis «Validado» no puede cancelarse; debe usarse UC–DIAG-10 (Reabrir Análisis) primero. |

### UC–DIAG-10 — Reabrir Análisis

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Administrador (o Bioquímico con permiso especial) revierte el estado de un análisis «Validado» a «En Proceso» para permitir correcciones. |
| **Actor** | Administrador |
| **Precondición** | El análisis debe estar en estado «Validado». |
| **Postcondiciones** | El estado del análisis cambia a «En Proceso». El PDF previamente generado se marca como «Obsoleto». El OTP asociado se invalida. Se registra en auditoría con motivo obligatorio. |
| **Comentarios** | Operación de alta criticidad. Solo el Administrador puede ejecutarla. Requiere doble confirmación. |

### UC–DIAG-11 — Reenviar Notificación de Resultados

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-03 |
| **Requisitos asociados** | RF-07 |
| **Descripción** | El personal autorizado reenvía al paciente el mensaje de WhatsApp con el enlace al portal y un nuevo OTP para la descarga de resultados. |
| **Actor** | Bioquímico/Doctor, Administrador |
| **Precondición** | El análisis debe estar en estado «Validado». El OTP anterior debe estar expirado o ya utilizado. |
| **Postcondiciones** | Se genera un nuevo OTP criptográfico. Se envía un nuevo mensaje de WhatsApp al paciente. El OTP anterior queda invalidado. |
| **Comentarios** | Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). El nuevo OTP tiene un TTL de 7 días (RNF-02). |

### UC–DIAG-12 — Consultar Panel de Análisis

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Bioquímico/Doctor accede a un panel de trabajo que lista todos los análisis micológicos, filtrables por estado, tipo de análisis, fecha y bioquímico asignado, sin necesidad de navegar paciente por paciente. |
| **Actor** | Bioquímico/Doctor, Administrador |
| **Precondición** | Sesión activa con rol autorizado. |
| **Postcondiciones** | El sistema presenta una tabla paginada y filtrable de análisis. Operación de solo lectura. Desde este panel se puede acceder al detalle de cada análisis y ejecutar acciones (actualizar estado, validar, cancelar). |
| **Comentarios** | Diferente de DIAG-07 (que muestra el historial de un paciente). Este UC muestra el volumen de trabajo del laboratorio. |

### UC–DIAG-13 — Gestionar Tipos de Análisis y Muestra

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Administrador gestiona el catálogo de tipos de análisis micológicos y tipos de muestra disponibles en el sistema (crear, modificar, desactivar). |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. |
| **Postcondiciones** | El catálogo queda actualizado. Los tipos desactivados no pueden seleccionarse en nuevos análisis, pero se preservan en registros históricos. |
| **Comentarios** | Incluye sub-flujos: Crear Tipo, Modificar Tipo, Desactivar Tipo (baja lógica). |

### UC–DIAG-14 — Registrar Observación de Cultivo

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Bioquímico/Doctor registra una observación periódica sobre el progreso de un cultivo micológico sin modificar el estado del análisis. |
| **Actor** | Bioquímico/Doctor |
| **Precondición** | El análisis debe existir y estar en estado «En Proceso». |
| **Postcondiciones** | La observación (texto, fecha, hora, usuario) se adjunta al análisis como entrada de bitácora. El estado del análisis no cambia. |
| **Comentarios** | Permite documentar hallazgos intermedios (crecimiento de colonias, cambios macroscópicos, contaminación) durante las semanas que dura un cultivo. |

### UC–DIAG-15 — Asignar Análisis a Bioquímico

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Administrador o el propio Bioquímico asigna un análisis micológico a un profesional responsable específico. |
| **Actor** | Administrador, Bioquímico/Doctor |
| **Precondición** | El análisis debe existir y no estar en estado «Validado» ni «Cancelado». |
| **Postcondiciones** | El análisis queda vinculado al bioquímico seleccionado. El panel de trabajo (DIAG-12) refleja la asignación. |
| **Comentarios** | Un análisis sin asignación explícita se considera «sin responsable» y aparece destacado en el panel. |

### UC–DIAG-16 — Derivar Muestra a Laboratorio Externo

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-02 |
| **Requisitos asociados** | RF-06 |
| **Descripción** | El Bioquímico/Doctor registra la derivación de una muestra a un laboratorio externo para análisis complementarios, incluyendo el destino y el motivo. |
| **Actor** | Bioquímico/Doctor, Administrador |
| **Precondición** | El análisis debe existir y estar en estado «Pendiente» o «En Proceso». |
| **Postcondiciones** | El análisis se marca como «Derivado». Se registra: laboratorio destino, fecha de envío, motivo de derivación, y un campo para el resultado externo cuando se reciba. |
| **Comentarios** | El análisis derivado puede volver a «En Proceso» cuando se reciba el resultado externo. |

---

## 4. LAB: Flujos de Trabajo Cubiertos por UC

| UC Actual | Flujo Cubierto | ¿Tiene UCE? |
|---|---|---|
| UC–LAB-01 | Registrar Ingreso de Insumos (entrada de reactivos al inventario) | **NO** |
| UC–LAB-02 | Registrar Retiro de Insumos (consumo por prácticas o análisis) | **NO** |
| UC–LAB-03 | Registrar Generación de Residuos (volumen y peso de desechos) | **NO** |
| UC–LAB-04 | Generar Reporte de Residuos (consolidación mensual automática) | **NO** |
| UC–LAB-05 | Consultar Inventario (vista del stock actual con filtros) | **NO** |

**Resumen LAB:** 5 UC definidos, **0 UCE desarrollados** (el documento dice «UCEs pendientes de desarrollo»).

---

## 5. LAB: Flujos de Trabajo Faltantes (No Documentados)

### 5.1 Nivel Estratégico — ¿Qué falta para que el subsistema sea completo?

| # | Flujo Faltante | Justificación |
|---|---|---|
| F10 | **Gestionar Catálogo de Insumos/Reactivos** | LAB-01 registra ingreso de stock, pero no existe UC para crear un nuevo tipo de insumo en el catálogo. La primera vez que se usa un reactivo, alguien debe darlo de alta con nombre, umbral, unidad de medida. |
| F11 | **Modificar Insumo/Reactivo** | Actualizar nombre, umbral mínimo, o cualquier otro atributo de un insumo ya registrado. |
| F12 | **Desactivar Insumo/Reactivo** | Cuando un reactivo se descontinúa, debe desactivarse del catálogo activo sin perder trazabilidad histórica. |
| F13 | **Gestionar Lotes y Vencimientos** | El IRQ-03 menciona «Fecha de vencimiento», pero no hay UC para registrar lotes. Un mismo reactivo puede tener múltiples lotes con distintas fechas de vencimiento. Falta: ingreso de lote, consulta de lotes próximos a vencer, marcado de lote vencido. |
| F14 | **Consultar Trazabilidad de Movimientos** | LAB-05 muestra el stock actual, pero no existe UC para consultar el historial de movimientos de un insumo (quién retiró, cuándo, para qué práctica/análisis). |
| F15 | **Configurar Umbrales de Alerta por Insumo** | RF-09 menciona alertas visuales cuando el stock alcanza un umbral mínimo, pero no hay UC para definir cuál es ese umbral por insumo. |
| F16 | **Registrar Devolución de Insumos** | Si un profesor retira más reactivo del necesario, debe poder devolver el excedente al inventario. |
| F17 | **Gestionar Categorías de Residuos** | El IRQ-04 menciona «Categoría/Clase de peligrosidad», pero no hay UC para administrar ese catálogo. |
| F18 | **Consultar / Modificar Registro de Residuos** | LAB-03 registra el residuo, pero no hay UC para consultar el historial de residuos de un período ni para corregir un registro erróneo. |
| F19 | **Registrar Disposición Final de Residuos** | El ciclo de vida del residuo no termina al generarse. Falta registrar cuándo y cómo se dispuso finalmente (retiro por empresa de tratamiento, fecha de eliminación). |
| F20 | **Registrar Ubicación de Almacenamiento** | En un laboratorio físico, los insumos están en estanterías, heladeras, armarios. El sistema debe permitir registrar y consultar la ubicación. |
| F21 | **Gestionar Categorías de Insumos** | Agrupar insumos por categoría (reactivos, medios de cultivo, materiales descartables, equipos) facilita la consulta y los reportes. |
| F22 | **Generar Reporte de Inventario** | Así como existe reporte de residuos (LAB-04), debería existir un reporte de inventario (stock actual, movimientos del período, insumos próximos a vencer). |
| F23 | **Vincular Retiro de Insumo con Análisis/Práctica** | LAB-02 registra el retiro, pero no lo vincula con un análisis micológico o una práctica educativa específica. Esta trazabilidad es clave para calcular costos y para investigación. |

---

## 6. LAB: Propuesta de Nuevos Casos de Uso

### UC–LAB-06 — Gestionar Catálogo de Insumos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10 |
| **Descripción** | El Administrador gestiona el catálogo de tipos de insumos y reactivos: crear, modificar y desactivar (baja lógica). |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. |
| **Postcondiciones** | El catálogo queda actualizado. Los insumos desactivados no pueden recibir nuevos ingresos o retiros, pero sus movimientos históricos se preservan. |
| **Comentarios** | Datos del insumo: nombre, descripción, unidad de medida (ml, g, unidades), categoría, umbral mínimo de alerta, ubicación de almacenamiento. |

### UC–LAB-07 — Gestionar Lotes de Insumo

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10, RF-09 |
| **Descripción** | El Administrador registra un nuevo lote de un insumo al momento del ingreso, indicando número de lote, fecha de vencimiento y cantidad. El sistema debe alertar sobre lotes próximos a vencer. |
| **Actor** | Administrador |
| **Precondición** | El insumo debe existir en el catálogo (LAB-06). |
| **Postcondiciones** | El lote queda registrado y asociado al ingreso. El stock del insumo se incrementa. El sistema programa alerta automática de vencimiento (ej. 30 días antes). |
| **Comentarios** | Un mismo insumo puede tener múltiples lotes activos. Al retirar (LAB-02), el sistema debe consumir primero del lote más próximo a vencer (FIFO/FEFO). |

### UC–LAB-08 — Consultar Trazabilidad de Movimientos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10 |
| **Descripción** | El usuario autorizado consulta el historial completo de movimientos (ingresos, retiros, devoluciones) de un insumo o de todos los insumos en un rango de fechas. |
| **Actor** | Administrador, Bioquímico/Doctor, Profesor |
| **Precondición** | Sesión activa con rol autorizado. |
| **Postcondiciones** | El sistema presenta una tabla cronológica de movimientos con: fecha, tipo de movimiento, usuario, cantidad, lote afectado, y análisis/práctica asociada. Operación de solo lectura. |
| **Comentarios** | Filtrable por insumo, tipo de movimiento, rango de fechas, usuario. |

### UC–LAB-09 — Configurar Umbrales de Alerta

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-09 |
| **Descripción** | El Administrador configura los umbrales mínimos de stock y los días de anticipación para alertas de vencimiento de cada insumo. |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. El insumo debe existir en el catálogo. |
| **Postcondiciones** | Los umbrales quedan configurados. El dashboard reflejará alertas cuando el stock esté por debajo del umbral o un lote esté dentro del período de pre-vencimiento. |
| **Comentarios** | Umbrales por defecto: stock mínimo = 1 unidad, alerta de vencimiento = 30 días. El Administrador puede sobrescribirlos por insumo. |

### UC–LAB-10 — Registrar Devolución de Insumos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10 |
| **Descripción** | El Profesor o Bioquímico registra la devolución de insumos no utilizados al inventario, revirtiendo total o parcialmente un retiro previo. |
| **Actor** | Profesor, Bioquímico/Doctor, Administrador |
| **Precondición** | Debe existir un retiro previo registrado. La cantidad a devolver no puede superar la cantidad retirada. |
| **Postcondiciones** | El stock del insumo se incrementa en la cantidad devuelta. Se registra el movimiento como «Devolución» vinculado al retiro original. |
| **Comentarios** | Si el lote original ya venció, el sistema advierte y la devolución se registra como «Vencido — no utilizable». |

### UC–LAB-11 — Gestionar Categorías de Residuos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-05 |
| **Requisitos asociados** | RF-11 |
| **Descripción** | El Administrador gestiona el catálogo de categorías/clases de peligrosidad de residuos químicos (crear, modificar, desactivar). |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. |
| **Postcondiciones** | El catálogo queda actualizado. Las categorías desactivadas no pueden seleccionarse en nuevos registros de residuos. |
| **Comentarios** | Datos de la categoría: nombre, clase de peligrosidad (ej. Clase I, II, III), descripción, instrucciones de almacenamiento. |

### UC–LAB-12 — Consultar y Modificar Registro de Residuos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-05 |
| **Requisitos asociados** | RF-11 |
| **Descripción** | El usuario autorizado consulta el historial de residuos generados en un período y, si es necesario, corrige un registro erróneo (antes de que se consolide en el reporte mensual). |
| **Actor** | Administrador, Bioquímico/Doctor, Profesor |
| **Precondición** | Sesión activa con rol autorizado. El registro a modificar no debe haber sido incluido en un reporte mensual ya emitido. |
| **Postcondiciones** | Los datos del residuo quedan actualizados. Se registra la modificación en auditoría. |
| **Comentarios** | Sub-flujos: Consultar (listado filtrable por fecha, categoría, usuario), Modificar (solo el autor o Administrador). |

### UC–LAB-13 — Registrar Disposición Final de Residuos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-05 |
| **Requisitos asociados** | RF-11 |
| **Descripción** | El Administrador registra la salida y disposición final de los residuos acumulados, indicando fecha de retiro, empresa/personal responsable del tratamiento y método de eliminación. |
| **Actor** | Administrador |
| **Precondición** | Deben existir residuos registrados y no dispuestos. |
| **Postcondiciones** | Los residuos seleccionados se marcan como «Dispuestos». Se registra: fecha de disposición, responsable del retiro, método de tratamiento. |
| **Comentarios** | Este UC cierra el ciclo de vida del residuo. La información es crítica para el cumplimiento normativo. |

### UC–LAB-14 — Gestionar Ubicaciones de Almacenamiento

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10 |
| **Descripción** | El Administrador gestiona el catálogo de ubicaciones físicas de almacenamiento (estantería, heladera, armario) donde se guardan los insumos. |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. |
| **Postcondiciones** | El catálogo de ubicaciones queda actualizado. Cada insumo puede tener asignada una ubicación. |
| **Comentarios** | Datos de ubicación: código/nombre, descripción (ej. «Heladera 2 — Estante superior»), temperatura (si aplica). |

### UC–LAB-15 — Gestionar Categorías de Insumos

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10 |
| **Descripción** | El Administrador gestiona el catálogo de categorías de insumos (reactivos, medios de cultivo, materiales descartables, equipos). |
| **Actor** | Administrador |
| **Precondición** | Sesión activa con rol de Administrador. |
| **Postcondiciones** | El catálogo queda actualizado. Los insumos pueden clasificarse por categoría. |
| **Comentarios** | Facilita filtros en consultas de inventario (LAB-05) y reportes (LAB-16). |

### UC–LAB-16 — Generar Reporte de Inventario

| Campo | Valor |
|---|---|
| **Objetivos asociados** | OBJ-04 |
| **Requisitos asociados** | RF-10, RF-09 |
| **Descripción** | El Administrador genera un reporte del estado del inventario en un momento dado, incluyendo stock actual, movimientos del período, insumos bajo umbral y próximos a vencer. |
| **Actor** | Administrador, Bioquímico/Doctor |
| **Precondición** | Sesión activa con rol autorizado. |
| **Postcondiciones** | El sistema emite un reporte en formato PDF o CSV con el resumen del inventario. |
| **Comentarios** | Complementa a LAB-05 (consulta en pantalla) con una versión exportable para auditorías o planificación de compras. |

---

## 7. Cambios de Repercusión

### 7.1 IRQ (Requisitos de Información) — Ampliaciones

| IRQ | Cambio Propuesto | Motivo |
|---|---|---|
| **IRQ-03** (Insumo/Reactivo) | Agregar campos: `Número de Lote`, `Unidad de Medida`, `Categoría`, `Ubicación de Almacenamiento`, `Fecha de Ingreso` | Soporta UC–LAB-07 (lotes), LAB-14 (ubicaciones), LAB-15 (categorías). |
| **IRQ-04** (Registro de Residuo) | Agregar campos: `Fecha de Disposición Final`, `Método de Tratamiento`, `Empresa/Responsable de Retiro`, `Estado` (Generado / Dispuesto) | Soporta UC–LAB-13 (disposición final). |
| **IRQ-02** (Análisis Micológico) | Agregar campos: `Bioquímico Asignado`, `Estado de Derivación`, `Laboratorio Destino`, `Fecha de Derivación`, `Resultado Externo` | Soporta UC–DIAG-15 (asignación) y DIAG-16 (derivación). |
| **IRQ-02** (Análisis Micológico) | Agregar entidad: `Bitácora de Cultivo` (fecha, observación, usuario) | Soporta UC–DIAG-14 (observaciones periódicas). |
| **Nuevo IRQ-05** | **Catálogo de Tipos de Análisis/Muestra** (nombre, descripción, estado, indicaciones asociadas) | Soporta UC–DIAG-13. |
| **Nuevo IRQ-06** | **Movimiento de Inventario** (tipo: ingreso/retiro/devolución, fecha, cantidad, lote, usuario, análisis/práctica asociada) | Soporta UC–LAB-08 (trazabilidad). |
| **Nuevo IRQ-07** | **Categoría de Residuo** (nombre, clase de peligrosidad, descripción, instrucciones de almacenamiento) | Soporta UC–LAB-11. |

### 7.2 RF (Requisitos Funcionales) — Nuevos

| RF | Descripción | Objetivo |
|---|---|---|
| **RF-16** | **Gestión de Catálogos Clínicos** — El sistema debe permitir al Administrador gestionar los tipos de análisis micológicos y tipos de muestra (crear, modificar, desactivar). | OBJ-02 |
| **RF-17** | **Gestión de Catálogos de Inventario** — El sistema debe permitir al Administrador gestionar las categorías de insumos, ubicaciones de almacenamiento y categorías de residuos. | OBJ-04, OBJ-05 |
| **RF-18** | **Trazabilidad de Lotes y Vencimientos** — El sistema debe permitir registrar lotes al ingresar insumos, con número de lote y fecha de vencimiento, y alertar sobre proximidad de vencimiento. | OBJ-04 |
| **RF-19** | **Registro de Disposición Final de Residuos** — El sistema debe permitir registrar la salida y disposición final de los residuos acumulados, con fecha, responsable y método de tratamiento. | OBJ-05 |
| **RF-20** | **Modificación de Ficha Clínica** — El sistema debe permitir al Bioquímico/Doctor modificar una ficha clínica registrada, manteniendo un historial de versiones. | OBJ-02 |
| **RF-21** | **Cancelación y Reapertura de Análisis** — El sistema debe permitir cancelar un análisis en curso (con motivo) y reabrir un análisis validado (solo Administrador, con auditoría). | OBJ-02 |

### 7.3 Actores — Ajustes

| Actor | Cambio Propuesto | Motivo |
|---|---|---|
| **ACT-02 (Profesor)** | Agregar a la descripción: «También registra la generación de residuos químicos producto de las prácticas educativas y puede consultar el inventario y la trazabilidad de movimientos.» | Ya está implícito en LAB-03 y LAB-05 pero no en la definición del actor. |
| **ACT-03 (Administrador)** | Agregar a la descripción: «Gestiona catálogos del sistema (tipos de análisis, insumos, categorías, ubicaciones) y registra la disposición final de residuos.» | Cubre los nuevos UC de administración de catálogos. |
| **ACT-01 (Bioquímico/Doctor)** | Agregar a la descripción: «Puede asignar análisis a un bioquímico responsable, derivar muestras a laboratorios externos y reenviar notificaciones de resultados.» | Cubre DIAG-11, DIAG-15, DIAG-16. |

### 7.4 UC Existentes — Ajustes

| UC | Cambio Propuesto | Motivo |
|---|---|---|
| **UC–DIAG-01** | Agregar `<<extend>>` a UC–DIAG-08 (Modificar Ficha Clínica). | Flujo natural: después de registrar, puede necesitar modificar. |
| **UC–DIAG-02** | La precondición «El paciente debe contar con una Ficha Clínica registrada en la sesión actual» es demasiado restrictiva. Debería permitir registrar una muestra aunque la ficha se haya creado en una sesión anterior. | Escenario real: el paciente llega otro día para la toma de muestra. |
| **UC–DIAG-04** | Agregar a postcondiciones: «Si el análisis tenía un OTP previo (por reenvío), se invalida. Solo se genera el OTP en la primera validación, no en reaperturas.» | Para evitar conflicto con DIAG-10 (Reabrir) y DIAG-11 (Reenviar). |
| **UC–DIAG-07** | Considerar renombrar a «Consultar Historial de Paciente» para diferenciarlo de DIAG-12 (Consultar Panel de Análisis). | Evita ambigüedad entre «consultar ficha de un paciente» y «consultar el panel de trabajo». |
| **UC–LAB-02** | Agregar a la descripción: «El sistema debe registrar el análisis micológico o la práctica educativa a la que se destina el retiro.» | Soporta trazabilidad fina (F23). |
| **UC–LAB-04** | Cambiar actor de «privilegios administrativos o directivos necesarios» a «Administrador» para ser consistente con el resto del documento. | Consistencia. |

### 7.5 Consistencia Interna — Hallazgos

| Hallazgo | Ubicación | Acción |
|---|---|---|
| **UC–REC-09 no existe** | Sección 2.7.3.1: después de UC–REC-08 (Bloquear/Desbloquear) salta a UC–REC-10 (Crear Indicación Médica). | Verificar si es un hueco intencional o si falta un UC. Si es intencional, documentarlo. |
| **UCE–DIAG-01 paso 9** | Dice «interfaz muestra…» (falta «La» al inicio). | Corrección tipográfica. |
| **UCE–REC-01 postcondición** | Dice «El sistema programa automáticamente en cola el envío de un mensaje recordatorio» pero no existe un UC para gestionar recordatorios. | Podría ser un UC implícito o requerir un UC–REC-23 (Gestionar Recordatorios). |
| **UCE–DIAG-01 paso 3** | «Backend» con mayúscula inconsistente. En otros UCE aparece como «backend» o «El sistema». | Normalizar terminología. |
| **Sección 2.8.3 LAB** | Dice «UCEs pendientes de desarrollo» sin listar siquiera los encabezados. | Completar con los 5 UCE de LAB-01 a LAB-05 más los nuevos. |

### 7.6 Módulos — Ajustes

| Módulo | Cambio Propuesto |
|---|---|
| **Stock de Insumos Reactivos** | Ampliar descripción para incluir trazabilidad por lotes, ubicaciones de almacenamiento y devoluciones. |
| **Control de Residuos** | Ampliar descripción para incluir el registro de disposición final y la gestión de categorías de peligrosidad. |
| **Registro de Análisis** | Ampliar descripción para incluir bitácora de cultivo, asignación a bioquímico y derivación a laboratorios externos. |

---

## 8. Resumen Cuantitativo

### DIAG

| Concepto | Actual | Propuesto | Total |
|---|---|---|---|
| UC definidos | 7 | +9 | 16 |
| UCE desarrollados | 2 | +14 (pendientes) | 16 |
| Flujos cubiertos | 7 | +9 | 16 |

### LAB

| Concepto | Actual | Propuesto | Total |
|---|---|---|---|
| UC definidos | 5 | +11 | 16 |
| UCE desarrollados | 0 | +16 (pendientes) | 16 |
| Flujos cubiertos | 5 | +11 | 16 |

### Totales del Documento

| Concepto | Actual | Propuesto | Total |
|---|---|---|---|
| IRQ | 4 | +3 | 7 |
| RF | 15 | +6 | 21 |
| UC totales | 28 | +20 | 48 |
| UCE totales | 19 | +30 | 49 |

---

## 9. Criterio de Priorización para Desarrollo de UCE

Si se desea avanzar por orden de importancia, se sugiere:

1. **Prioridad Alta (esenciales para operación clínica diaria):** DIAG-03, DIAG-04, DIAG-05, DIAG-06, DIAG-07, LAB-01, LAB-02, LAB-03, LAB-05
2. **Prioridad Media (completan integridad del sistema):** DIAG-08, DIAG-09, DIAG-12, DIAG-14, LAB-04, LAB-06, LAB-07, LAB-08, LAB-10, LAB-13, LAB-16
3. **Prioridad Baja (administración y casos extremos):** DIAG-10, DIAG-11, DIAG-13, DIAG-15, DIAG-16, LAB-09, LAB-11, LAB-12, LAB-14, LAB-15

---

*Fin del análisis. Queda a disposición para validación antes de modificar el documento principal.*