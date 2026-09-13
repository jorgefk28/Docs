<!-- Header/Footer -->
> **Trabajo Final (ASC) - Proyecto Software (LSI) - FCEQyN - UNaM**  |  SIGEMI - Kluka, Jorge Favio

Apóstoles (Misiones), 9 de Septiembre de 2026
Al Prof. Adjunto de las cátedras
Trabajo Final (ASC) | Proyecto Software (LSI)
FCEQyN - UNaM
Lic. Sergio Daniel Caballero
S/D
De mi mayor consideración:
Me dirijo a Ud. a efectos de presentar la propuesta para el desarrollo de un producto software como tema para las cátedras “Proyecto Software” de la carrera Licenciatura en Sistemas de Información (plan de estudios 2013) y “Trabajo Final” de la carrera Analista en Sistemas de Computación (plan de estudios 2010).
El producto software a desarrollar se denomina: Sistema Integral de Gestión Micológica.
Sin otro particular, y quedando a la espera de la evaluación de la propuesta, me despido atte.
__________________________
Kluka, Jorge Favio
46.303.522 ASC - LSI 
[46.303.522]
Reservado para el equipo de cátedra
Evaluación de la propuesta
| Nombre del proyecto |  |
|---|---|
| Alumno/a | Kluka Jorge Favio |
| Fecha de la evaluación |  |

| **Aspecto** | **Evaluación** |
|---|---|
| Presentación en general |  |
| Objetivos |  |
| Requisitos funcionales |  |
| Requisitos no funcionales |  |
| Procesos automáticos | 1.<br>2.<br>3. |
| Planificación |  |
| Estrategia de validación / verificación |  |
| Metodología |  |

| **Resultado final** | APROBADO - DEBE CORREGIR |
|---|---|

Firma por el equipo de cátedra:
Contenidos
**Evaluación de la propuesta1**
**Contenidos2**
**Introducción y objetivos3**
**Alcance y limitaciones3**
**Especificación de módulos3**
Funcionales3
No funcionales3
**Descripción de los módulos3**
**Procesos automatizados4**
**Estimación de tamaño por módulo4**
**Entorno tecnológico y metodológico5**
**Planificación de actividades5**
Planteo del problema
[¿Qué problema se plantea resolver mediante el desarrollo del proyecto?.]
El Módulo de Bioquímica y Farmacia de la Universidad Nacional de Misiones realiza estudios de laboratorio con fines académicos y para brindar servicios de diagnóstico a la comunidad. Actualmente, la gestión de turnos, el control de stock de insumos reactivos, el registro de residuos químicos y el archivado de los historiales clínicos se lleva adelante de forma completamente manual. Esta operatoria traslada al propio personal del módulo las tareas propias de recepción y administración, lo que la vuelve laboriosa y propensa a errores.

**Gestión de turnos deficiente:** la recepción de pacientes, la asignación de turnos y la confección de las historias clínicas se realizan exclusivamente en papel, sin una agenda centralizada ni mecanismos de recordatorio o reprogramación. Como los análisis micológicos tienen tiempos de espera que pueden extenderse hasta un mes, las cancelaciones e inasistencias generan espacios ociosos que hoy no pueden reutilizarse, prolongando innecesariamente los tiempos de atención.

**Falta de trazabilidad de los insumos:** el stock de insumos reactivos se controla en hojas sueltas o de manera informal, sin conocer las cantidades exactas disponibles. Esto provoca escasez de materiales, un uso ineficiente de los mismos y, en ocasiones, la utilización de reactivos con fechas de vencimiento expiradas en las prácticas de la facultad.

**Nueva reglamentación nacional para residuos:** desde 2026 un nuevo reglamento exige registrar de manera exacta el volumen y peso de los residuos químicos generados para su posterior tratamiento y eliminación. Hoy los profesores asientan estos datos manualmente en listas de papel, comprometiendo la confiabilidad de la información y el cumplimiento normativo.

**Digitalización de los historiales clínicos:** el registro en papel expone la información clínica a pérdidas y deterioro, y dificulta el resguardo legal exigido. Además, se busca facilitar el acceso a los historiales clínicos para los trabajos de investigación que la facultad desarrolla sobre datos reales del laboratorio.
Introducción y objetivos
[Describir el escenario sobre el que se desarrollará el producto y los objetivos a cubrir con el mismo. Podría plantearse como la solución propuesta al problema del punto anterior.]
El Módulo de Bioquímica y Farmacia de la Universidad Nacional de Misiones cuenta con un laboratorio de Micología destinado al uso académico de la Universidad y a brindar servicios de diagnóstico a la comunidad. En el laboratorio se atienden pacientes y se procesan muestras micológicas con tiempos de espera prolongados, además de desarrollarse prácticas académicas y actividades de investigación.

Actualmente todo el ciclo operativo del laboratorio se registra en papel: la asignación de turnos, la confección de las fichas clínicas, el control de los insumos reactivos, el registro de los residuos químicos y el resguardo del historial de los pacientes. Esta dependencia del soporte físico sobrecarga al personal del módulo con tareas administrativas, dificulta la trazabilidad de las muestras y los reactivos, y pone en riesgo el cumplimiento de las normativas legales y ambientales vigentes.

Frente a este escenario se propone el desarrollo de **SIGEMI (Sistema Integral de Gestión Micológica)**, un producto software que digitaliza el registro de la información clínica, automatiza la gestión de turnos mediante un Agente IA que interactúa con el paciente vía WhatsApp, sistematiza la administración del stock de insumos reactivos y del control de residuos químicos, y garantiza la emisión segura y remota de los resultados. Con este sistema se busca eliminar el registro manual, mejorar la experiencia del paciente, asegurar el resguardo legal de la información y proveer datos estructurados para los trabajos de investigación de la facultad. Para ello se definen los siguientes objetivos:

| **Objetivo** | **Descripción** |
|---|---|
| **OBJ–01** Automatización de la Gestión de Turnos y Atención | Digitalizar y automatizar integralmente el proceso de atención de pacientes, desde la recepción y el agendamiento del turno hasta el envío de indicaciones, recordatorios, reprogramaciones y la gestión de una lista de espera. |
| **OBJ–02** Digitalización del Historial Clínico y Registro de Análisis | Centralizar en un sistema digital los datos médicos de los pacientes, su historial clínico y el estado de sus análisis (pendiente, en proceso, terminado, validado), eliminando la dependencia del papel. |
| **OBJ–03** Emisión Segura y Descarga de Resultados | Proveer un módulo automatizado y asíncrono para la entrega de resultados mediante un portal web seguro y un token de un solo uso (OTP), garantizando el cumplimiento de la Ley de Protección de los Datos Personales (Ley 25.326). |
| **OBJ–04** Trazabilidad y Control de Stock de Insumos Reactivos | Implementar un control formal de inventario que gestione cantidades, lotes y vencimientos de los insumos y reactivos químicos, previniendo el uso de materiales vencidos y la escasez. |
| **OBJ–05** Sistematización del Registro de Residuos Químicos | Registrar de manera exacta el volumen y peso de los residuos químicos generados, automatizando la generación de la documentación exigida por la normativa vigente. |
Alcance y limitaciones
[Del problema descrito en el apartado anterior, qué aspectos se van a considerar para el producto software a desarrollar. Qué cuestiones no serán abarcadas en, al menos, una versión inicial.]

**Alcance:**

El producto software a desarrollar (SIGEMI) considera los siguientes aspectos del problema planteado:

- **Gestión de Turnos y Atención:** agenda de turnos, agendamiento por Agente IA (WhatsApp) y manual, envío de indicaciones médicas, recordatorios, cancelación, reprogramación, reasignación automática de turnos liberados y lista de espera.
- **Registro de Información Clínica:** ficha clínica del paciente con sus datos demográficos e información clínica estructurada al momento de la consulta, con historial de versiones.
- **Gestión de Pacientes:** repositorio centralizado del historial clínico acumulado y de los resultados previos de las personas atendidas.
- **Registro de Análisis:** trazabilidad del ciclo de vida de la muestra (pendiente, en proceso, terminado, validado, cancelado), panel de trabajo y gestión de catálogos clínicos.
- **Emisión de Resultados:** entrega remota y segura del informe en formato PDF mediante un portal web con token OTP de un solo uso.
- **Stock de Insumos Reactivos:** registro de ingresos, retiros y devoluciones, trazabilidad por lotes y vencimientos, alertas de stock y gestión de catálogos de insumos.
- **Control de Residuos:** registro del volumen y peso de los residuos químicos, categorías de peligrosidad y generación del reporte mensual.
- **Usuarios, Roles y Permisos, Auditoría y Estadísticas:** gestión de accesos con roles, trazabilidad inmutable de las operaciones críticas y consolidación de datos para reportes e investigación.

**Limitaciones:**

- No se integrará con RISMI ni AlegraMed.
- Los pacientes no serán actores del sistema (no tendrán usuario ni credenciales de acceso); interactuarán únicamente vía WhatsApp con el Agente IA y de forma anónima en el portal de resultados mediante el token OTP.
- No se abarcará el apartado de facturación ni contabilidad para la gestión de stock (no se gestionan compras, órdenes de compra ni pagos a proveedores).
- La entrega de resultados se realizará exclusivamente de forma digital mediante el portal seguro; no se contempla el retiro presencial ni la impresión de informes en el laboratorio.
- En la versión inicial no se contempla la importación masiva ni la digitalización retroactiva de historiales clínicos históricos en papel; los registros se cargarán a partir de la puesta en marcha del sistema.
Especificación de módulos
Funcionales
Módulo de Gestión de Turnos y Atención
Módulo de Registro de Información Clínica
Módulo de Gestión de Pacientes
Módulo de Registro de Análisis
Módulo de Emisión de Resultados
Módulo de Stock de Insumos Reactivos
Módulo de Control de Residuos
No funcionales
Módulo de Usuarios
Módulo de Roles y permisos
Módulo de Estadísticas y Reportes
Módulo de Auditoría
Descripción de los módulos
[Por **cada módulo** definido en la sección anterior se debe adjuntar una descripción de la operatoria que involucra, las tareas específicas a cubrir y las salidas a generar (en caso de corresponder). Esto puede ser realizado en formato narrativo,]
Módulo de Gestión de Turnos y Atención
Este módulo se encarga de automatizar y optimizar todo el proceso inicial de atención al paciente. Sus funciones abarcan la agenda del turno, el otorgamiento de indicaciones para los análisis, el envío de recordatorios de asistencia, la gestión de reprogramaciones y la administración de una lista de espera que notifica liberaciones de fechas. Su implementación busca brindar un mejor servicio integral al paciente y eliminar la carga de trabajo completamente manual que existe en la recepción en la actualidad. 
Módulo de Registro de Información Clínica
Su propósito es sistematizar la recolección de los datos médicos iniciales del paciente al momento de su consulta. Opera permitiendo que el doctor ingrese en el sistema una ficha clínica detallada durante el transcurso del turno. Esto garantiza que el laboratorio cuente con la información médica exacta, estructurada y legible con la que posteriormente se realizarán los análisis de micosis. 
Módulo de Gestión de Pacientes
Su función principal es actuar como el repositorio centralizado del historial de las personas atendidas en el laboratorio. Gestiona el almacenamiento permanente tanto de los datos personales del paciente como de su historial clínico acumulado y resultados previos. Este almacenamiento organizado es crítico para dar respuesta a exigencias legales de resguardo de información y para facilitar la consulta ágil de datos en futuros trabajos de investigación de la facultad.
Módulo de Registro de Análisis
Este módulo traza el ciclo de vida completo de las muestras microbiológicas dentro del laboratorio. Registra el tipo de análisis, los parámetros o resultados obtenidos, y permite actualizar los estados del estudio secuencialmente (pendiente, en proceso, terminado y validado por un bioquímico). Su valor reside en asegurar un control riguroso de cada etapa clínica, consolidando toda la información relevante al análisis en un único lugar.  Incluye la gestión de tipos de análisis, la cancelación de estudios y un panel de trabajo para visualizar el volumen de análisis por estado.
Módulo de Emisión de Resultados
Se encarga de automatizar la entrega final y remota de los diagnósticos a los pacientes. Funciona mediante un flujo de notificación asíncrona que envía un enlace y genera criptográficamente un Token (OTP) de un solo uso, permitiendo al paciente descargar su archivo PDF desde un portal web seguro mediante una doble validación de identidad. Este proceso asegura el cumplimiento estricto de la Ley de Protección de los Datos Personales (Ley 25.326) sin forzar el retiro presencial. 
Módulo de Stock de Insumos Reactivos
Su objetivo es digitalizar la administración del inventario de recursos físicos y químicos. Registra los ingresos y los retiros de insumos realizados por los profesores y bioquímicos para las prácticas de los alumnos y estudios de laboratorio. Su implementación busca clarificar la trazabilidad operativa para solucionar la actual mala gestión y escasez, evitando problemáticas como el vencimiento de reactivos, el uso ineficiente de materiales nuevos y el desconocimiento de las cantidades exactas. incluyendo trazabilidad por lotes, ubicaciones de almacenamiento y devoluciones.
Módulo de Control de Residuos
Su función es sistematizar la recolección de datos sobre los desechos generados en las prácticas de laboratorio. Permite registrar de manera exacta la cantidad (volumen y peso) de los residuos químicos producidos por cada actividad. Esto es vital para garantizar el cumplimiento del nuevo reglamento que entró en vigencia en el año 2026, facilitando la generación de reportes mensuales y el adecuado resguardo de los residuos para su tratamiento 
Módulo de Usuarios
Su propósito es administrar la identidad y las credenciales de todas las personas que interactúan con la plataforma. Gestiona el registro, la modificación y la baja de cuentas, centralizando el proceso de autenticación en el sistema . Representa el pilar inicial de la seguridad de la aplicación, asegurando que únicamente los individuos debidamente identificados puedan ingresar a la plataforma. 
Módulo de Roles y permisos
Su función es controlar y delimitar el nivel de autorización y los privilegios operativos dentro de la aplicación. Opera definiendo qué pantallas, acciones y datos específicos están disponibles para cada tipo de cuenta. Su implementación es fundamental para garantizar la confidencialidad de la información clínica y prevenir alteraciones no autorizadas, forzando a que cada actor opere estrictamente dentro de sus responsabilidades.
Módulo de Estadísticas y Reportes
Este módulo se encarga de procesar y consolidar los datos transaccionales generados por el resto del sistema para su visualización y exportación. Extrae y cruza datos clínicos, de inventario y de desechos para automatizar la emisión de reportes periódicos y proveer la base de información estructurada que alimentará investigaciones académicas.
Módulo de Auditoría
Su objetivo es proveer un mecanismo de trazabilidad profundo e inmutable sobre las operaciones críticas que ocurren en el software. Funciona registrando de manera automática, silenciosa y cronológica cada evento significativo, guardando detalles precisos como el usuario responsable, la fecha, la hora, la dirección IP y el cambio específico realizado 
Procesos automatizados
[Completar la tabla con el siguiente formato]
| **Denominación** | **Módulos que intervienen** | **Descripción del proceso** |
|---|---|---|
| Agente IA de gestión de turnos | Módulo de Gestión de Turnos y Atención.<br>Módulo de Emisión de Resultados. | **Descripción**: Asistente virtual inteligente encargado de ser el primer punto de contacto con el paciente, automatizando de principio a fin la recepción, el agendamiento y la logística de entrega de estudios.<br>**Disparadores**: Mensaje entrante del paciente vía WhatsApp o disponibilidad de un resultado de laboratorio emitido.<br>**Funcionalidad**: Interactúa e interpreta mensajes para asignar turnos y enviar indicaciones o facturas. Gestiona recordatorios, reprogramaciones y coordina citas múltiples considerando dependencias temporales (ej. seguimientos de un mes). Finalmente, entrega los resultados al paciente (con tiempos de 48 hs a 20 días).<br>**Impacto**: Refleja los cambios en la agenda del sistema central en tiempo real y administra la lista de espera de forma automatizada. |
| Flujo de Reagendado Automático por Cancelación | Módulo de Gestión de Turnos y Atención | **Descripción**: Proceso autónomo diseñado para optimizar la ocupación de la agenda del laboratorio, cubriendo huecos generados por cancelaciones de manera inmediata y sin requerir intervención administrativa.<br>**Disparador**: Notificación de cancelación de turno por parte de un paciente al asistente virtual.<br>**Funcionalidad**: Libera el espacio en el sistema e inicia una búsqueda secuencial inteligente de candidatos (pacientes en lista de espera o con turnos posteriores). Envía invitaciones con vigencia de tiempo (ej. 1 hora) y, si es aceptada, confirma la reasignación recalculando citas múltiples si corresponde. Si expira o se rechaza, itera al siguiente candidato.<br>**Impacto**: Mantiene la agenda optimizada, reduce los tiempos muertos de los profesionales y acelera la atención de los pacientes en espera. |
| Motor de Emisión Segura y Descarga Criptográfica | Módulo de Emisión de Resultados, Módulo de Registro de Análisis, Módulo de Auditoría | **Descripción**: Mecanismo de seguridad y encriptación creado para resolver la problemática legal de la entrega de estudios sensibles, asegurando la privacidad del paciente sin forzar su asistencia presencial.<br>**Disparador**: Actualización del estado del análisis a "Validado" por parte del bioquímico. <br>**Funcionalidad**: Genera un Token (OTP) único y lo asocia de forma invisible al PDF del diagnóstico. Envía una notificación asíncrona (SMS/email) con el enlace y el Token, omitiendo cualquier dato clínico. Efectúa la descarga autenticada forzada vía HTTP únicamente tras validar un doble factor (DNI del paciente y Token).<br>**Impacto**: Garantiza el cumplimiento de la Ley 25.326 y genera un registro inmutable de fecha, hora e IP en la base de datos para la trazabilidad de auditoría. |

Estimación de tamaño por módulo
[Se expresa en porcentaje con respecto al total del producto. Completar la siguiente tabla.]
| **Módulo** | **Porcentaje de participación / Producto** |
|---|---|
| Módulo de Gestión de Turnos y Atención | 15% |
| Módulo de Registro de Análisis | 15% |
| Módulo de Emisión de Resultados | 12% |
| Módulo de Stock de Insumos Reactivos | 10% |
| Módulo de Gestión de Pacientes | 10% |
| Módulo de Estadísticas y Reportes | 10% |
| Módulo de Registro de Información Clínica | 8% |
| Módulo de Usuarios | 5% |
| Módulo de Roles y permisos | 5% |
| Módulo de Auditoría | 5% |
| Módulo de Control de Residuos | 5% |
| **Total** | **100%** |

Entorno tecnológico y metodológico
[Completar la siguiente tabla]
| **Lenguajes de programación:** | Python, TypeScript, SQL |
|---|---|
| **Framework:** | FastAPI (Backend) / React (Frontend) |
| **Arquitectura:** | Modelo Vista Controlador |
| **Motor de Base de Datos:** | PostgreSQL |
| **Metodología seleccionada:** | Proceso Unificado (UP) |
| **Tipo de proyecto:** | Con cliente final |

Planificación de actividades
[En función de la metodología seleccionada estimar los tiempos para cada una de sus fases, considerando el inicio del proyecto al momento de presentar la propuesta y su finalización para el mes de noviembre. Adjuntar las capturas que crea conveniente (ej: gantt). Se provee una tabla a modo de modelo orientativo.]
| **Actividad** | **Fecha de inicio** | **Fecha de finalización** |
|---|---|---|
| **Planificación y relevamiento ** | 31/08/2026 | 09/09/2026 |
| Relevar el contexto de trabajo manual del laboratorio de Micología. | 31/08/2026 | 04/09/2026 |
| Definición de Objetivos, alcance, módulos, actores y limitaciones de la solución. | 05/09/2026 | 09/09/2026 |
| **Estudio de factibilidad** | 10/09/2026 | 16/09/2026 |
| Estudio de Factibilidad | 10/09/2026 | 13/09/2026 |
| Análisis de Riesgos | 14/09/2026 | 16/09/2026 |
| **Requisitos** | 17/09/2026 | 30/09/2026 |
| Requisitos Funcionales y No Funcionales | 17/09/2026 | 19/09/2026 |
| Casos de Uso | 20/09/2026 | 26/09/2026 |
| Requisitos de Información | 27/09/2026 | 30/09/2026 |
| **Análisis.** | 01/10/2026 | 14/10/2026 |
| Modelo de Domino | 01/10/2026 | 05/10/2026 |
| Modelo de Base de Datos | 06/10/2026 | 09/10/2026 |
| Diagramas de Secuencia de Sistema | 10/10/2026 | 14/10/2026 |
| **Diseño** | 15/10/2026 | 28/10/2026 |
| Casos de uso Extendidos | 15/10/2026 | 20/10/2026 |
| Casos de uso Reales | 21/10/2026 | 25/10/2026 |
| Diseño de UX/UI | 26/10/2026 | 28/10/2026 |
| **Programación ** | 29/10/2026 | 13/11/2026 |
| Desarrollo del Software | 29/10/2026 | 13/11/2026 |
| **Testing ** | 14/11/2026 | 20/11/2026 |
| Pruebas unitarias y de integración | 14/11/2026 | 17/11/2026 |
| Pruebas de validación y corrección de errores | 18/11/2026 | 20/11/2026 |
