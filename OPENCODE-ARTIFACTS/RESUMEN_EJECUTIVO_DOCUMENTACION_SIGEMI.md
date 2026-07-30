# RESUMEN EJECUTIVO — Estado de Avance de Documentación SIGEMI

**Documento:** TF_2026_Requerimientos_KLUKA_JORGE.md (v0.0.0.1, 17/04/2026)  
**Fecha de auditoría:** 29/07/2026  
**Total de líneas:** 1,272

---

## 1. ESTADO GLOBAL

| Componente documental | Completitud |
|---|---|
| Objetivos del sistema (OBJ) | ✅ 5/5 (100%) |
| Requisitos de Información (IRQ) | ✅ 4/4 (100%) |
| Requisitos Funcionales (RF) | ✅ 15/15 (100%) |
| Requisitos No Funcionales (RNF) | ✅ 5/5 (100%) |
| Definición de Actores | ✅ 4/4 (100%) |
| Definiciones de Casos de Uso (UC) | ✅ 39/39 (100%) |
| Casos de Uso Extendidos (UCE) | ⚠️ 27/39 (69%) |
| Diagramas de Casos de Uso | ❌ 0/5 (0%) — solo placeholders |
| Glosario de Términos | ❌ Vacío |

**Conclusión:** La fase de requisitos (OBJ, RF, RNF, IRQ) está completa. Las definiciones de UC están completas. El déficit principal está en los **Casos de Uso Extendidos (31% faltante)** y en los **artefactos visuales y de soporte**.

---

## 2. EVALUACIÓN POR SUBSISTEMA

### 2.1 Subsistema Gestión de Pacientes (REC)

| Indicador | Valor |
|---|---|
| UC definidos | 23/23 ✅ |
| UCE definidos | 23/23 ✅ |
| **Completitud** | **100%** |

**Flujos de trabajo cubiertos:**
- Agendamiento de turnos (WhatsApp + manual) ✅
- Cancelación y reprogramación (WhatsApp + manual) ✅
- Reasignación automática de turnos liberados ✅
- Consulta de turnos y agenda ✅
- Configuración de parámetros de agenda ✅
- Bloqueo/desbloqueo de días y franjas ✅
- CRUD de indicaciones médicas ✅
- Cancelación por vencimiento (job automático) ✅
- Registro de asistencia ✅
- CRUD de pacientes + búsqueda ✅

**Defectos detectados:**
- 🔴 UC-REC-09 ausente (refactorizado en REC-20/21/22 pero no documentado)
- 🟡 UCE-REC-06: métrica de rendimiento referencia "Paso 6" inexistente (solo hay 4 pasos)
- 🟡 UCE-REC-05 y UCE-REC-06: postcondiciones vacías ("-")
- 🟡 UCE-REC-01: `<<include>>` a "Enviar Recordatorio de Turno" que no está definido en ningún UC/UCE
- 🟡 UCE-REC-15: numeración de pasos duplicada (5 y 5.1)

### 2.2 Subsistema Laboratorio Bioquímico (DIAG)

| Indicador | Valor |
|---|---|
| UC definidos | 7/7 ✅ |
| UCE definidos | 2/7 ❌ |
| **Completitud** | **29%** |

**UCEs FALTANTES (5):**
| Código | Nombre | Impacto |
|---|---|---|
| UCE-DIAG-03 | Actualizar Estado de Análisis | 🔴 Flujo clínico roto — no se puede avanzar un análisis de "Pendiente" a "En Proceso" o "Terminado" |
| UCE-DIAG-04 | Validar Análisis | 🔴 Sin este UCE no se puede cerrar el ciclo clínico ni disparar la notificación |
| UCE-DIAG-05 | Notificación de Resultados | 🔴 Sin este UCE no se describe la generación del OTP ni el envío por WhatsApp |
| UCE-DIAG-06 | Descargar Informe | 🔴 Sin este UCE no se describe el portal web de descarga con validación OTP |
| UCE-DIAG-07 | Consultar Ficha Clínica | 🟡 Operación de consulta del historial — menor criticidad |

**Defectos adicionales:**
- 🔴 **Error de clasificación:** UCE-DIAG-01 y UCE-DIAG-02 están ubicados en la sección 2.8.2 "Subsistema Recursos de Laboratorio", cuando pertenecen al "Subsistema Laboratorio Bioquímico". No existe sección 2.8 para Laboratorio Bioquímico.
- 🟢 UCE-DIAG-02: tabla de excepciones vacía ("- | -")

### 2.3 Subsistema Recursos de Laboratorio (LAB)

| Indicador | Valor |
|---|---|
| UC definidos | 5/5 ✅ |
| UCE definidos | 0/5 ❌ |
| **Completitud** | **0%** |

**UCEs FALTANTES (5):**
| Código | Nombre | Impacto |
|---|---|---|
| UCE-LAB-01 | Registrar Ingreso de Insumos | 🔴 Sin este UCE no se describe el flujo de entrada al inventario |
| UCE-LAB-02 | Registrar Retiro de Insumos | 🔴 Sin este UCE no se describe el flujo de egreso ni las alertas de stock |
| UCE-LAB-03 | Registrar Generación de Residuos | 🔴 Sin este UCE no se describe el registro de volumen/peso de residuos |
| UCE-LAB-04 | Generar Reporte de Residuos | 🔴 Sin este UCE no se describe la consolidación mensual normativa |
| UCE-LAB-05 | Consultar Inventario | 🟡 Operación de consulta — menor criticidad |

**Nota:** La sección 2.8.2 está titulada "Subsistema Recursos de Laboratorio" pero contiene UCE-DIAG-01 y UCE-DIAG-02 (que pertenecen a Laboratorio Bioquímico). Esto debe corregirse: crear una sección 2.8.2 para Laboratorio Bioquímico con los DIAG, y una 2.8.3 para Recursos de Laboratorio con los LAB.

### 2.4 Subsistema Acceso y Seguridad (SEG)

| Indicador | Valor |
|---|---|
| UC definidos | 3/3 ✅ |
| UCE definidos | 1/3 ❌ |
| **Completitud** | **33%** |

**UCEs FALTANTES (2):**
| Código | Nombre | Impacto |
|---|---|---|
| UCE-SEG-02 | Administrar Usuario y Roles | 🔴 Sin este UCE no se describe el CRUD de usuarios ni la asignación de roles |
| UCE-SEG-03 | Cerrar Sesión | 🟢 Flujo simple — baja criticidad |

**Defecto adicional:**
- 🟡 El módulo "Roles y Permisos" está declarado en 2.3.2.2 pero no tiene ningún UC ni UCE específico. UC-SEG-02 lo cubre parcialmente.

### 2.5 Subsistema Reportes y Estadísticas (REP)

| Indicador | Valor |
|---|---|
| UC definidos | 1/1 ✅ |
| UCE definidos | 1/1 ✅ |
| **Completitud** | **100%** |

**Defecto detectado:**
- 🟡 UCE-REP-01 menciona "anonimización estricta" en el paso 5, pero no existe ningún RF ni RNF que defina este requisito de anonimización.

---

## 3. INCONSISTENCIAS Y CONTRADICCIONES DETECTADAS

### 🔴 Críticas (deben resolverse antes de avanzar)

| # | Problema | Ubicación |
|---|---|---|
| 1 | **RF-03 tiene dos nombres distintos:** "Gestión de Reagendación automática" (línea 162) vs "Gestión de Lista de Espera por Turnos Liberados" (líneas 325, 333, 673, 698). Son conceptos semánticamente diferentes. | 2.5, 2.7, 2.8 |
| 2 | **Sección 2.8.1 titulada "Subsistema Gestión Clínica":** Este nombre no existe en los 5 subsistemas definidos en 2.2. Debería llamarse "Subsistema Gestión de Pacientes". | 2.8.1 |
| 3 | **UCE-DIAG-01 y UCE-DIAG-02 en sección equivocada:** Están en 2.8.2 "Recursos de Laboratorio" pero pertenecen a "Laboratorio Bioquímico". | 2.8.2 |
| 4 | **Recursividad sin caso base en UC-REC-04:** La reasignación automática se dispara a sí misma sin condición de parada explícita ni límite de iteraciones. UCE-REC-14 dispara UC-REC-04 "por cada bloque liberado", lo que podría generar decenas de ejecuciones simultáneas. | 2.7.3.1, 2.8.1 |
| 5 | **Políticas contradictorias de cancelación:** El paciente NO puede cancelar en las últimas 24h (UCE-REC-02), pero el administrativo SÍ puede con advertencia (UCE-REC-21). Si es intencional, debe justificarse. | 2.8.1 |
| 6 | **Políticas contradictorias de reprogramación:** El paciente NO puede reprogramar más de 2 veces (UCE-REC-03), pero el administrativo SÍ puede con confirmación (UCE-REC-22). | 2.8.1 |
| 7 | **Campos IRQ-01 no coinciden con UCE-REC-16:** Faltan en el formulario: Sexo, Médico derivante, Institución, Diagnóstico presuntivo. Sobran: Correo Electrónico, Obra Social (no declarados en IRQ-01). | 2.4, 2.8.1 |

### 🟡 Altas (deben resolverse pronto)

| # | Problema |
|---|---|
| 8 | `<<include>>` a "Enviar Recordatorio de Turno" en UCE-REC-01 — caso de uso no definido en el documento |
| 9 | Referencias a "antiguo UC-REC-09" en UCE-REC-20/21/22 — UC nunca definido, el lector no puede verificar la transición |
| 10 | Glosario de Términos completamente vacío |
| 11 | Figuras 1-5 (diagramas DCU) son solo placeholders sin contenido |
| 12 | Anonimización en UCE-REP-01 sin requisito funcional o no funcional que la respalde |
| 13 | Módulo "Roles y Permisos" declarado en 2.3.2.2 pero sin UC/UCE que lo modele |
| 14 | IRQ-02 declara "Cultivo" como dato específico pero no aparece en UCE-DIAG-02 |

### 🟠 Medias

| # | Problema |
|---|---|
| 15 | "Bioquímico" vs "Bíoquímico" — inconsistencia de acentuación entre secciones |
| 16 | "Acceso y Seguridad" vs "Acceso y Seguridades" — singular/plural inconsistente |
| 17 | "Recepción y Administración de Pacientes" vs "Gestión de Pacientes" — nombres alternativos no unificados |
| 18 | "Diagnóstico y Laboratorio Bioquímico" vs "Laboratorio Bioquímico" — nombres alternativos |

### 🟢 Bajas

| # | Problema |
|---|---|
| 19 | UCE-REC-06: métrica de rendimiento referencia "Paso 6" (inexistente, solo hay 4 pasos) |
| 20 | UCE-REC-15: numeración de pasos duplicada (5 y 5.1) |
| 21 | Typo "Registro deInformación" (falta espacio) en línea 73 |
| 22 | UC-REC-16 asociado a OBJ-02 cuando probablemente corresponde a OBJ-01 |
| 23 | UCE-REC-05 y UCE-REC-06: postcondiciones vacías |
| 24 | UC-REP-01: postcondiciones vacías |

---

## 4. FLUJOS DE TRABAJO — ANÁLISIS DE INTEGRIDAD

### Flujo principal: Atención completa al paciente

```
Agendar Turno → Asistencia → Ficha Clínica → Ingreso Muestra → Análisis → Validación → Notificación → Descarga
```

| Paso | UC | UCE | Estado |
|---|---|---|---|
| Agendar Turno | UC-REC-01 / UC-REC-20 | UCE-REC-01 / UCE-REC-20 | ✅ Completo |
| Registrar Asistencia | UC-REC-15 | UCE-REC-15 | ✅ Completo |
| Registrar Ficha Clínica | UC-DIAG-01 | UCE-DIAG-01 | ✅ Completo |
| Ingresar Muestra | UC-DIAG-02 | UCE-DIAG-02 | ✅ Completo |
| Actualizar Estado Análisis | UC-DIAG-03 | ❌ **FALTANTE** | 🔴 ROTO |
| Validar Análisis | UC-DIAG-04 | ❌ **FALTANTE** | 🔴 ROTO |
| Notificar Resultados | UC-DIAG-05 | ❌ **FALTANTE** | 🔴 ROTO |
| Descargar Informe | UC-DIAG-06 | ❌ **FALTANTE** | 🔴 ROTO |

**Conclusión:** El flujo clínico está roto a partir del paso "Actualizar Estado de Análisis". Los 4 UCEs críticos del núcleo clínico están sin documentar.

### Flujo secundario: Gestión de inventario

```
Ingreso Insumo → [Stock] → Retiro Insumo → Generación Residuo → Reporte Mensual
```

| Paso | UC | UCE | Estado |
|---|---|---|---|
| Registrar Ingreso | UC-LAB-01 | ❌ **FALTANTE** | 🔴 ROTO |
| Registrar Retiro | UC-LAB-02 | ❌ **FALTANTE** | 🔴 ROTO |
| Registrar Residuo | UC-LAB-03 | ❌ **FALTANTE** | 🔴 ROTO |
| Generar Reporte | UC-LAB-04 | ❌ **FALTANTE** | 🔴 ROTO |
| Consultar Inventario | UC-LAB-05 | ❌ **FALTANTE** | 🔴 ROTO |

**Conclusión:** El subsistema de Recursos de Laboratorio no tiene ningún UCE documentado. Está completamente pendiente.

### Flujo secundario: Seguridad

```
Iniciar Sesión → [Operaciones] → Cerrar Sesión
                 → Administrar Usuarios
```

| Paso | UC | UCE | Estado |
|---|---|---|---|
| Iniciar Sesión | UC-SEG-01 | UCE-SEG-01 | ✅ Completo |
| Administrar Usuarios | UC-SEG-02 | ❌ **FALTANTE** | 🔴 ROTO |
| Cerrar Sesión | UC-SEG-03 | ❌ **FALTANTE** | 🟡 Pendiente |

---

## 5. PRÓXIMOS PASOS RECOMENDADOS

### Fase 1: Corrección de defectos críticos (prioridad inmediata)

1. **Unificar nombre de RF-03:** Decidir entre "Gestión de Reagendación automática" o "Gestión de Lista de Espera por Turnos Liberados" y aplicarlo consistentemente.
2. **Corregir encabezado 2.8.1:** Cambiar "Subsistema Gestión Clínica" → "Subsistema Gestión de Pacientes".
3. **Reubicar UCE-DIAG-01 y UCE-DIAG-02:** Crear sección 2.8.2 "Subsistema Laboratorio Bioquímico" y moverlos allí.
4. **Definir caso base para UC-REC-04:** Agregar condición de parada explícita y límite de iteraciones.
5. **Resolver políticas contradictorias:** Definir si la cancelación/reprogramación en <24h o >2 veces es permitida para administrativos y documentar la justificación.
6. **Alinear IRQ-01 con UCE-REC-16:** Agregar campos faltantes (Sexo, Médico derivante, Institución, Diagnóstico presuntivo) o justificar su omisión.

### Fase 2: Completar UCEs faltantes (12 pendientes)

**Por orden de criticidad:**

1. **UCE-DIAG-03, 04, 05, 06** — Núcleo del flujo clínico (Actualizar, Validar, Notificar, Descargar)
2. **UCE-LAB-01, 02, 03, 04** — Flujo completo de recursos de laboratorio
3. **UCE-SEG-02** — Administración de usuarios y roles
4. **UCE-DIAG-07** — Consulta de ficha clínica
5. **UCE-LAB-05** — Consulta de inventario
6. **UCE-SEG-03** — Cerrar sesión

### Fase 3: Artefactos de soporte

7. **Crear/embeber diagramas DCU** (Figuras 1-5) — preferiblemente en Mermaid para mantenibilidad
8. **Completar Glosario de Términos** con al menos: Agente IA, OTP, Token, Alta Temprana, Baja lógica, Ficha Clínica, Muestra, Cultivo, Micología, JWT
9. **Definir UC "Enviar Recordatorio de Turno"** o eliminar la referencia `<<include>>` en UCE-REC-01
10. **Documentar la transición UC-REC-09** → UC-REC-20/21/22 en la lista de cambios

### Fase 4: Próximos artefactos de documentación (en orden metodológico)

Una vez corregidos los defectos y completados los UCEs:

11. **Modelo de Dominio:** Diagrama de clases conceptual con entidades, atributos y relaciones derivadas de los IRQ y UCEs. Identificar agregados, value objects y entidades.
12. **Diagrama de Clases de Diseño:** Refinamiento del modelo de dominio con tipos de datos, navegabilidad y patrones.
13. **Diagramas de Secuencia:** Para los flujos principales (agendamiento, ciclo de análisis, gestión de inventario).
14. **Modelo de Datos / DER:** Esquema relacional normalizado con claves, índices y restricciones.
15. **Arquitectura del Sistema:** Diagrama de componentes, decisión de stack tecnológico, definición de APIs.
16. **Prototipado de Interfaces:** Wireframes o mockups de las pantallas principales.

---

## 6. MÉTRICAS RESUMEN

| Métrica | Valor |
|---|---|
| Total UC definidos | 39 |
| Total UCE definidos | 27 |
| UCEs faltantes | **12** |
| Completitud global UCE | **69%** |
| Defectos críticos | 7 |
| Defectos altos | 7 |
| Defectos medios | 4 |
| Defectos bajos | 6 |
| Flujos de trabajo rotos | 2 (flujo clínico, flujo inventario) |
| Subsistemas al 100% | 2 de 5 (Gestión de Pacientes, Reportes) |

---

*Documento generado por el agente Analyst el 29/07/2026.*
*Fuentes: deep_diver (completitud UC/UCE) + deep_diver (inconsistencias y contradicciones).*