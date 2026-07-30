# Inserción de UC-REC-S-01 y UCE-REC-S-01 — Buscar Paciente

## Resumen del problema

En el documento `TF_2026_Requerimientos_KLUKA_JORGE.md`:

1. **UC-REC-17 (Modificar Paciente)** y **UC-REC-19 (Desactivar Paciente)** referencian `<<include>> Buscar Paciente` sin especificar un ID de caso de uso formal.
2. **UCE-REC-17** y **UCE-REC-19** tienen pasos que dicen "El sistema ejecuta Buscar Paciente" sin referenciar un UCE formal.
3. No existe una definición de caso de uso ni extendido para **Buscar Paciente** en las secciones 2.7.3.1 y 2.8.1.

## Cambios requeridos (4 modificaciones + 2 inserciones)

---

## A. Insertar UC-REC-S-01 en sección 2.7.3.1

**Lugar de inserción:** Después de UC-REC-22 (línea 477), antes del inicio de la sección 2.7.3.2 (línea 478).

**Contenido a insertar:**

```
|**UC–REC-S-01**|**Buscar Paciente**|
|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico y Registro de Análisis |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |
|**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre o Apellido) y retorna el/los paciente(s) coincidente(s) al caso de uso invocante. |
|**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |
|**Postcondiciones**| Los datos del paciente seleccionado son retornados al caso de uso invocante para continuar su flujo. |
|**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. |
```

---

## B. Insertar UCE-REC-S-01 en sección 2.8.1

**Lugar de inserción:** Después de UCE-REC-22 (línea 1134), antes del inicio de la sección 2.8.2 (línea 1135).

**Contenido a insertar:**

```
|**UCE–REC-S-01**|**Buscar Paciente**|  |
|---|---|---|
|**Objetivos asociados**| OBJ-02 Digitalización del Historial Clínico |  |
|**Requisitos asociados**| RF-05 Registro de Ficha Clínica |  |
|**Descripción**| Subproceso reutilizable de búsqueda de pacientes. Recibe un criterio de búsqueda (DNI, Nombre, Apellido) y retorna el/los pacientes coincidentes al caso de uso invocante. |  |
|**Precondición**| El caso de uso invocante debe proveer al menos un criterio de búsqueda. |  |
|**Secuencia normal**|**Paso**|  |
|  | 1 | El sistema solicita al usuario el criterio de búsqueda (DNI, Nombre o Apellido). |
|  | 2 | El usuario ingresa el criterio de búsqueda. |
|  | 3 | El sistema consulta la base de datos con el criterio ingresado. |
|  | 4a | Si hay una sola coincidencia exacta: el sistema retorna los datos del paciente al caso de uso invocante. |
|  | 4b | Si hay múltiples coincidencias: el sistema muestra un listado paginado para que el usuario seleccione. Al seleccionar, retorna los datos. |
|**Postcondición**| Los datos del paciente seleccionado son retornados al caso de uso invocante. |  |
|**Excepciones**|**Paso**|  |
|  | 3 | Si ningún paciente coincide con el criterio ingresado, el sistema informa "Paciente no encontrado" al caso de uso invocante para que maneje la situación (ofrecer crear uno nuevo, buscar de nuevo, etc.). |
|  | 3 | Si ocurre un error de conexión con la base de datos, se retorna un error al caso de uso invocante. |
|**Rendimiento**|**Paso**|  |
|  | 3 | Menos de 1 segundo |
|**Frecuencia**| Alta (invocado por Modificar y Desactivar Paciente) |  |
|**Estabilidad**| Alta |  |
|**Comentarios**| Caso de uso puramente estructural (include-only). No tiene actor directo ni produce valor por sí mismo. Solo existe como subflujo `<<include>>` de UC-REC-17 y UC-REC-19. La búsqueda es flexible: DNI (coincidencia exacta), Nombre o Apellido (coincidencia parcial). |  |
```

---

## C. Actualizar referencias en UC-REC-17 (línea 434)

**Línea actual:**
```
|**Comentarios**| Incluye `<<include>>` Buscar Paciente. |
```

**Debe quedar:**
```
|**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). |
```

---

## D. Actualizar referencias en UC-REC-19 (línea 451)

**Línea actual:**
```
|**Comentarios**| Incluye `<<include>>` Buscar Paciente. Se realiza baja lógica para mantener integridad referencial. |
```

**Debe quedar:**
```
|**Comentarios**| Incluye `<<include>>` UC-REC-S-01 (Buscar Paciente). Se realiza baja lógica para mantener integridad referencial. |
```

---

## E. Actualizar referencias en UCE-REC-17 (línea 972)

**Línea actual:**
```
|  | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido como criterio de búsqueda. |
```

**Debe quedar:**
```
|  | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido como criterio de búsqueda. |
```

---

## F. Actualizar referencias en UCE-REC-19 (línea 1026)

**Línea actual:**
```
|  | 2 | El sistema ejecuta Buscar Paciente: solicita DNI, Nombre o Apellido. |
```

**Debe quedar:**
```
|  | 2 | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente): solicita DNI, Nombre o Apellido. |
```

---

## Resumen visual de cambios

### Antes:
```
Sección 2.7.3.1 (UC):
  UC-REC-17 → Comentarios: Incluye <<include>> Buscar Paciente.         ← Sin ID
  UC-REC-19 → Comentarios: Incluye <<include>> Buscar Paciente.         ← Sin ID
  [NO EXISTE UC-REC-S-01]

Sección 2.8.1 (UCE):
  UCE-REC-17 → Paso 2: El sistema ejecuta Buscar Paciente: solicita...  ← Sin ID
  UCE-REC-19 → Paso 2: El sistema ejecuta Buscar Paciente: solicita...  ← Sin ID
  [NO EXISTE UCE-REC-S-01]
```

### Después:
```
Sección 2.7.3.1 (UC):
  UC-REC-17 → Comentarios: Incluye <<include>> UC-REC-S-01 (Buscar Paciente).  ← Con ID
  UC-REC-19 → Comentarios: Incluye <<include>> UC-REC-S-01 (Buscar Paciente).  ← Con ID
  UC-REC-S-01 → [NUEVO] Buscar Paciente (include-only)

Sección 2.8.1 (UCE):
  UCE-REC-17 → Paso 2: El sistema ejecuta UCE-REC-S-01 (Buscar Paciente):...   ← Con ID
  UCE-REC-19 → Paso 2: El sistema ejecuta UCE-REC-S-01 (Buscar Paciente):...   ← Con ID
  UCE-REC-S-01 → [NUEVO] Buscar Paciente (include-only)
```