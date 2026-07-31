# CORRECCIONES DE INCONSISTENCIAS — SIGEMI

**Documento:** TF_2026_Requerimientos_KLUKA_JORGE.md  
**Fecha de corrección:** 31/07/2026  
**Auditoría de origen:** RESUMEN_EJECUTIVO_DOCUMENTACION_SIGEMI.md (29/07/2026)  
**Líneas finales:** 1,284 (eran 1,272)

---

## 1. CAMBIOS REALIZADOS

### 🔴 Críticas (resueltas: 1, 2, 3, 7)

| # | Inconsistencia | Acción | Ubicación |
|---|---|---|---|
| 1 | RF-03 con dos nombres distintos | Unificado a **"Gestión de Reagendación automática"** en UC-REC-03, UC-REC-04, UCE-REC-03, UCE-REC-04 | 2.7.3.1, 2.8.1 |
| 2 | Sección 2.8.1 titulada "Subsistema Gestión Clínica" | Renombrado a **"Subsistema Gestión de Pacientes"** | 2.8.1 |
| 3 | UCE-DIAG-01 y UCE-DIAG-02 en sección equivocada (2.8.2 "Recursos de Laboratorio") | 2.8.2 renombrado a **"Subsistema Laboratorio Bioquímico"**; insertada nueva sección **2.8.3 "Subsistema Recursos de Laboratorio"** (placeholder); 2.8.3→2.8.4 "Acceso y Seguridad"; 2.8.4→2.8.5 "Reportes y Estadísticas" | 2.8.2–2.8.5 |
| 7 | Campos IRQ-01 no coinciden con UCE-REC-16 | **Agregados:** Correo Electrónico, Obra Social. **Eliminados:** Médico derivante, Institución, Diagnóstico presuntivo. Actualizado paso 5 de UCE-DIAG-01 para eliminar referencias a campos removidos. | 2.4, 2.8.2 |

### 🟡 Altas (resueltas: 8, 9, 10, 14)

| # | Inconsistencia | Acción | Ubicación |
|---|---|---|---|
| 8 | `<<include>>` a "Enviar Recordatorio de Turno" no definido | Eliminada la referencia `<<include>>` en UCE-REC-01 paso 8. El texto ahora describe el envío como proceso interno del sistema sin calificarlo como caso de uso. | 2.8.1 |
| 9 | Referencias a "antiguo UC-REC-09" | Eliminadas las tres referencias en UCE-REC-20, UCE-REC-21 y UCE-REC-22 | 2.8.1 |
| 10 | Glosario de Términos vacío | Completado con **9 términos:** Agente IA, OTP, Token, Alta Temprana, Baja lógica, Ficha Clínica, Muestra, Micología, JWT | Glosario |
| 14 | "Cultivo" en IRQ-02 sin presencia en UCE-DIAG-02 | Eliminado "Cultivo" de los datos específicos de IRQ-02 | 2.4 |

### 🟠 Medias (resueltas: 15, 16, 17, 18)

| # | Inconsistencia | Acción | Ubicación |
|---|---|---|---|
| 15 | "Bíoquímico" vs "Bioquímico" | Corregido a **"Laboratorio Bioquímico"** (sin tilde en la i) | 2.7.3.2 |
| 16 | "Acceso y Seguridades" vs "Acceso y Seguridad" | Corregido a **"Acceso y Seguridad"** | 2.2 |
| 17 | "Recepción y Administración de Pacientes" vs "Gestión de Pacientes" | Corregido a **"Gestión de Pacientes"** | 2.2 |
| 18 | "Diagnóstico y Laboratorio Bioquímico" vs "Laboratorio Bioquímico" | Corregido a **"Laboratorio Bioquímico"** | 2.2 |

### 🟢 Bajas (resueltas: 19, 20, 21, 22)

| # | Inconsistencia | Acción | Ubicación |
|---|---|---|---|
| 19 | UCE-REC-06: métrica de rendimiento referencia "Paso 6" inexistente | Corregido a **"Paso 3"** | 2.8.1 |
| 20 | UCE-REC-15: numeración duplicada (5 y 5.1) | Renumerado: 5.1→6, 6→7, 7→8 | 2.8.1 |
| 21 | Typo "Registro deInformación" | Corregido a **"Registro de Información"** (espacio agregado) | 2.2 |
| 22 | UC-REC-16 asociado a OBJ-02 | Corregido a **OBJ-01** (Automatización de la Gestión de Turnos y Atención) | 2.7.3.1 |

---

## 2. DEUDA TÉCNICA DOCUMENTAL PENDIENTE

### 🔴 Críticas no resueltas (por instrucción del autor)

| # | Problema | Justificación de no resolución |
|---|---|---|
| 4 | Recursividad sin caso base en UC-REC-04 | Pendiente de análisis de arquitectura |
| 5 | Políticas contradictorias de cancelación (<24h paciente vs. administrativo) | Pendiente de definición de negocio |
| 6 | Políticas contradictorias de reprogramación (>2 veces paciente vs. administrativo) | Pendiente de definición de negocio |

### 🟡 Altas no resueltas

| # | Problema | Justificación |
|---|---|---|
| 11 | Figuras 1-5 (DCU) son placeholders | Requiere trabajo de diagramación (Mermaid o similar) |
| 12 | Anonimización en UCE-REP-01 sin RF/RNF que la respalde | Requiere definición de nuevo requisito funcional o no funcional |
| 13 | Módulo "Roles y Permisos" sin UC/UCE | Requiere definición de nuevos casos de uso |

### 🟢 Bajas no resueltas

| # | Problema | Justificación |
|---|---|---|
| 23 | UCE-REC-05 y UCE-REC-06: postcondiciones vacías | Pendiente — el autor debe definir las postcondiciones |
| 24 | UC-REP-01: postcondiciones vacías | Pendiente — el autor debe definir las postcondiciones |

### UCEs faltantes (12)

| Código | Nombre | Subsistema |
|---|---|---|
| UCE-DIAG-03 | Actualizar Estado de Análisis | Laboratorio Bioquímico |
| UCE-DIAG-04 | Validar Análisis | Laboratorio Bioquímico |
| UCE-DIAG-05 | Notificación de Resultados | Laboratorio Bioquímico |
| UCE-DIAG-06 | Descargar Informe | Laboratorio Bioquímico |
| UCE-DIAG-07 | Consultar Ficha Clínica | Laboratorio Bioquímico |
| UCE-LAB-01 | Registrar Ingreso de Insumos | Recursos de Laboratorio |
| UCE-LAB-02 | Registrar Retiro de Insumos | Recursos de Laboratorio |
| UCE-LAB-03 | Registrar Generación de Residuos | Recursos de Laboratorio |
| UCE-LAB-04 | Generar Reporte de Residuos | Recursos de Laboratorio |
| UCE-LAB-05 | Consultar Inventario | Recursos de Laboratorio |
| UCE-SEG-02 | Administrar Usuario y Roles | Acceso y Seguridad |
| UCE-SEG-03 | Cerrar Sesión | Acceso y Seguridad |

---

## 3. RESUMEN DE IMPACTO

| Métrica | Antes | Después |
|---|---|---|
| Defectos críticos | 7 | 3 (pendientes: 4, 5, 6) |
| Defectos altos | 7 | 3 (pendientes: 11, 12, 13) |
| Defectos medios | 4 | 0 |
| Defectos bajos | 6 | 2 (pendientes: 23, 24) |
| Glosario de términos | 0 definiciones | 9 definiciones |
| Inconsistencias de nomenclatura | 4 variantes | 0 (unificadas) |
| UCEs pendientes | 12 | 12 (sin cambios) |

---

*Documento generado el 31/07/2026.*