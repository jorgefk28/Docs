# RESUMEN EJECUTIVO — Estado de Avance del Proyecto SIGEMI

**Sistema Integral de Gestión Micológica — Módulo de Bioquímica y Farmacia (UNaM)**
**Documento:** `TF_2026_Requerimientos_KLUKA_JORGE.md` (v0.0.0.1, 1.463 líneas)
**Fecha del informe:** 31/08/2026

---

## 1. ESTADO GLOBAL

| Componente documental | Completitud |
|---|---|
| Objetivos del sistema (OBJ) | 5/5 (100%) |
| Requisitos de Información (IRQ) | 7/7 (100%) |
| Requisitos Funcionales (RF) | 21/21 (100%) |
| Requisitos No Funcionales (RNF) | 5/5 (100%) |
| Identificación de Actores | 4/4 (100%) |
| Definición de Casos de Uso (UC) | 49/49 (100%) |
| Casos de Uso Extendidos (UCE) | 26/49 (53%) |
| Diagramas de Casos de Uso | Terminado (.drawio) |
| Modelo de Dominio | Terminado (detallado + Mermaid) |
| Modelo de Datos | En Revisión |
| Glosario de Términos | Completado (9 términos) |

**Conclusión:** La base de requisitos (OBJ, IRQ, RF, RNF, actores) está completa, los 49 UC están definidos y los artefactos de modelado visual (diagrama de casos, modelo de dominio) ya están terminados. El frente pendiente es la **escritura de los UCE de los subsistemas Laboratorio Bioquímico (DIAG) y Recursos de Laboratorio (LAB)** y la **revisión final del Modelo de Datos**.

---

## 2. COMPLETITUD POR SUBSISTEMA

### 2.1 Gestión de Pacientes (REC)

| Indicador | Valor |
|---|---|
| UC definidos | 22/22 ✅ |
| UCE definidos | 22/22 ✅ |
| **Completitud** | **100%** |

Cubre turnos (WhatsApp + manual), reprogramación/cancelación, reasignación automática, agenda, indicaciones médicas, asistencia, CRUD de pacientes y búsqueda (UC-REC-S-01).

### 2.2 Laboratorio Bioquímico (DIAG)

| Indicador | Valor |
|---|---|
| UC definidos | 10/10 ✅ |
| UCE definidos | 2/10 ❌ |
| **Completitud** | **60%** |

**UCE faltantes (8):** DIAG-03 (Actualizar Estado), DIAG-04 (Validar), DIAG-05 (Descargar), DIAG-06 (Historial), DIAG-07 (Modificar Ficha), DIAG-08 (Cancelar Análisis), DIAG-09 (Panel de Análisis), DIAG-10 (Tipos de Análisis).

### 2.3 Recursos de Laboratorio (LAB)

| Indicador | Valor |
|---|---|
| UC definidos | 13/13 ✅ |
| UCE definidos | 0/13 ❌ |
| **Completitud** | **50%** |

Sección declarada como "UCEs pendientes de desarrollo" (LAB-01 a LAB-13). Es el subsistema de mayor deuda documental.

### 2.4 Acceso y Seguridad (SEG)

| Indicador | Valor |
|---|---|
| UC definidos | 3/3 ✅ |
| UCE definidos | 1/3 ❌ |
| **Completitud** | **66%** |

Faltan UCE-SEG-02 (Administrar Usuario y Roles) y UCE-SEG-03 (Cerrar Sesión).

### 2.5 Reportes y Estadísticas (REP)

| Indicador | Valor |
|---|---|
| UC definidos | 1/1 ✅ |
| UCE definidos | 1/1 ✅ |
| **Completitud** | **100%** |

---

## 3. MÉTRICAS GLOBALES

| Métrica | Valor |
|---|---|
| Total UC | 49 |
| Total UCE escritos | 26 |
| UCE pendientes | 23 |
| Completitud global UCE | 73% |


---
