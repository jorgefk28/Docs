# UC-REC-S-01 y UCE-REC-S-01 — Buscar Paciente

## UC-REC-S-01 — Buscar Paciente (Sección 2.7.3.1)

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

## UCE-REC-S-01 — Buscar Paciente (Sección 2.8.1)

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

## Referencias actualizadas

| Lugar | Antes | Después |
|---|---|---|
| UC-REC-17 Comentarios | `<<include>>` Buscar Paciente | `<<include>>` UC-REC-S-01 (Buscar Paciente) |
| UC-REC-19 Comentarios | `<<include>>` Buscar Paciente | `<<include>>` UC-REC-S-01 (Buscar Paciente) |
| UCE-REC-17 Paso 2 | El sistema ejecuta Buscar Paciente | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente) |
| UCE-REC-19 Paso 2 | El sistema ejecuta Buscar Paciente | El sistema ejecuta UCE-REC-S-01 (Buscar Paciente) |