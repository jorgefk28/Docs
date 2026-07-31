# Artifact: Cambios Aplicados — COMPLETITUD_DIAG_LAB.md

**Fecha:** 31/07/2026
**Documento destino:** `TF_2026_Requerimientos_KLUKA_JORGE.md`

---

## Resumen de Cambios Aplicados

### 1. Eliminación de UC-DIAG-05 "Notificación de Resultados"
- **UC-DIAG-05** reemplazado por "Descargar Informe" (contenido del antiguo UC-DIAG-06)
- **UC-DIAG-06** eliminado (fusionado en DIAG-05)
- **UC-DIAG-04**: Postcondiciones actualizadas → ahora genera OTP y envía WhatsApp directamente (sin referenciar DIAG-05)
- **UC-DIAG-04**: Requisitos asociados: se agregó RF-08

### 2. Exclusión de Flujos DIAG (F3, F4, F7, F8, F9)
No se crearon los siguientes UC propuestos en el análisis:
| Flujo | UC Propuesto | Estado |
|-------|-------------|--------|
| F3: Reabrir Análisis Validado | UC-DIAG-10 | ❌ No creado |
| F4: Reenviar OTP / Notificación | UC-DIAG-11 | ❌ No creado |
| F7: Registrar Observaciones de Cultivo | UC-DIAG-14 | ❌ No creado |
| F8: Asignar Análisis a Bioquímico | UC-DIAG-15 | ❌ No creado |
| F9: Derivar Muestra a Laboratorio Externo | UC-DIAG-16 | ❌ No creado |

### 3. Nuevos UC-DIAG Creados (renumerados)
| UC | Nombre | Flujo Origen |
|----|--------|-------------|
| UC-DIAG-08 | Modificar Ficha Clínica | F1 |
| UC-DIAG-09 | Cancelar Análisis | F2 |
| UC-DIAG-10 | Consultar Panel de Análisis | F5 |
| UC-DIAG-11 | Gestionar Tipos de Análisis y Muestra | F6 |

### 4. Exclusión de Flujos LAB (F13, F19, F20, F23)
Estos flujos se incorporaron como parte del UC **LAB-02 "Registrar Retiro de Insumos"** en lugar de crear UC separados:

| Flujo | Descripción | Incorporado en LAB-02 |
|-------|-------------|----------------------|
| F13 | Gestionar Lotes y Vencimientos | ✅ FIFO/FEFO, lote consumido |
| F19 | Registrar Disposición Final de Residuos | ✅ Vinculado al retiro |
| F20 | Registrar Ubicación de Almacenamiento | ✅ Ubicación de origen |
| F23 | Vincular Retiro con Análisis/Práctica | ✅ Trazabilidad análisis/práctica |

### 5. Nuevos UC-LAB Creados
| UC | Nombre | Flujo Origen |
|----|--------|-------------|
| UC-LAB-06 | Gestionar Catálogo de Insumos | F10 |
| UC-LAB-07 | Consultar Trazabilidad de Movimientos | F14 |
| UC-LAB-08 | Configurar Umbrales de Alerta | F15 |
| UC-LAB-09 | Registrar Devolución de Insumos | F16 |
| UC-LAB-10 | Gestionar Categorías de Residuos | F17 |
| UC-LAB-11 | Consultar y Modificar Registro de Residuos | F18 |
| UC-LAB-12 | Gestionar Categorías de Insumos | F21 |
| UC-LAB-13 | Generar Reporte de Inventario | F22 |

### 6. Actualizaciones a UC Existentes
- **UC-DIAG-01**: Agregado `<<extend>>` a UC-DIAG-08 (Modificar Ficha Clínica)
- **UC-DIAG-02**: Precondición relajada: "no necesariamente en la sesión actual"
- **UC-DIAG-07**: Renombrado a "Consultar Historial de Paciente"
- **UC-LAB-04**: Precondición cambiada a rol de Administrador

### 7. IRQ Actualizados
- **IRQ-02**: Agregados estados "Cancelado, Derivado"
- **IRQ-03**: Agregados campos: Número de Lote, Unidad de Medida, Categoría, Ubicación de Almacenamiento, Fecha de Ingreso
- **IRQ-04**: **NO MODIFICADO** (por instrucción expresa)
- **IRQ-05 (nuevo)**: Catálogo de Tipos de Análisis/Muestra
- **IRQ-06 (nuevo)**: Movimiento de Inventario
- **IRQ-07 (nuevo)**: Categoría de Residuo

### 8. RF Nuevos (RF-16 a RF-21)
| RF | Nombre | Objetivo |
|----|--------|----------|
| RF-16 | Gestión de Catálogos Clínicos | OBJ-02 |
| RF-17 | Gestión de Catálogos de Inventario | OBJ-04, OBJ-05 |
| RF-18 | Trazabilidad de Lotes y Vencimientos | OBJ-04 |
| RF-19 | Registro de Disposición Final de Residuos | OBJ-05 |
| RF-20 | Modificación de Ficha Clínica | OBJ-02 |
| RF-21 | Cancelación de Análisis | OBJ-02 |

### 9. Actores Actualizados
- **ACT-01 (Bioquímico/Doctor)**: Agregado "modificar, cancelar" al ciclo de vida
- **ACT-02 (Profesor)**: Agregado registro de residuos y consulta de inventario/trazabilidad
- **ACT-03 (Administrador)**: Agregada gestión de catálogos del sistema

### 10. Descripciones de Módulos Actualizadas
- **Registro de Análisis**: Agregada gestión de tipos, cancelación, panel
- **Stock de Insumos Reactivos**: Agregados lotes, ubicaciones, devoluciones
- **Control de Residuos**: Agregada disposición final y categorías

### 11. Correcciones de Consistencia
- **UCE-DIAG-01 paso 9**: "interfaz" → "La interfaz" (tipografía)
- **UCE-DIAG-01 pasos 3, 7, 8**: "Backend" → "El sistema" (normalización)
- **Nota UC-REC-09**: Agregada explicación de salto intencional en numeración
- **Sección 2.8.3 LAB**: Actualizada con lista de UC pendientes

---

## Deuda Técnica (No Implementado)

### Pendiente de Desarrollo — UCE
| Subsistema | UCE Pendientes |
|-----------|---------------|
| Gestión de Pacientes | UCE-REC-06 a UCE-REC-08, UCE-REC-10 a UCE-REC-22, UCE-REC-S-01 |
| Laboratorio Bioquímico | UCE-DIAG-01 a UCE-DIAG-05, UCE-DIAG-07 a UCE-DIAG-11 |
| Recursos de Laboratorio | UCE-LAB-01 a UCE-LAB-13 (todos pendientes) |
| Acceso y Seguridad | UCE-SEG-01 a UCE-SEG-03 |
| Reportes y Estadísticas | UCE-REP-01 |

### No Implementado por Exclusión Expresa
| Ítem | Motivo |
|------|--------|
| UC-DIAG-10 (Reabrir Análisis) — F3 | Excluido por usuario |
| UC-DIAG-11 (Reenviar Notificación) — F4 | Excluido por usuario |
| UC-DIAG-14 (Registrar Observación de Cultivo) — F7 | Excluido por usuario |
| UC-DIAG-15 (Asignar Análisis) — F8 | Excluido por usuario |
| UC-DIAG-16 (Derivar Muestra) — F9 | Excluido por usuario |
| UC-LAB-07 como "Gestionar Lotes" (F13) | Fusionado en LAB-02 |
| UC-LAB-13 como "Disposición Final" (F19) | Fusionado en LAB-02 |
| UC-LAB-14 como "Ubicaciones" (F20) | Fusionado en LAB-02 |
| F23 (Vincular retiro con análisis/práctica) | Fusionado en LAB-02 |
| IRQ-04 (agregar campos) | No modificado por instrucción expresa |

### Inconsistencias Residuales (No Intervenidas)
| Ubicación | Detalle | Nota |
|-----------|---------|------|
| UCE-DIAG-02 pasos 5, 6 | "Backend" con mayúscula | Preexistente, no solicitado en el cambio |
| UCE-SEG-01 pasos 4, 5, 6 | "Backend" con mayúscula | Preexistente, no solicitado en el cambio |
| UCE-REP-01 pasos 4, 5, 8 | "Backend" con mayúscula | Preexistente, no solicitado en el cambio |
| UCE-DIAG-01 Comentarios | "Backend" con mayúscula | Preexistente, no solicitado en el cambio |
| UCE-DIAG-02 paso 1 | "UC-DIAG-01" (guion simple) | Preexistente, variación menor de nomenclatura |

---

*Fin del artifact. Todos los cambios aprobados han sido aplicados.*