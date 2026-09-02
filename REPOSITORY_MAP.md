# Mapa del repositorio

> **Idioma principal:** español · [English version](REPOSITORY_MAP.en.md)

Este documento es el **índice navegable** de `ancNC-mse-workflow`. Cada enlace abre la carpeta correspondiente en GitHub; al entrar, el `README.md` de esa carpeta explica qué debe contener, qué archivos se esperan y cómo se relaciona con el resto del MSE.

## Raíz del proyecto

- [`.github/`](.github/ABOUT.md) - herramientas propias de GitHub: revisión de cambios, plantillas de incidencias y comprobaciones automáticas. No contiene ciencia del MSE.
- [`docs/`](docs/) - documentación científica e institucional; explica qué sistema se está modelando y por qué.
  - [`00_getting_started/`](docs/00_getting_started/) - guía de entrada para nuevos colaboradores o consultores.
  - [`01_governance_objectives/`](docs/01_governance_objectives/) - objetivos de manejo, prioridades y tolerancias de riesgo.
  - [`02_stock_ecology/`](docs/02_stock_ecology/) - biología, ecología, estructura del stock y papel como pez forraje.
  - [`03_fishery/`](docs/03_fishery/) - flotas, esfuerzo, selectividad, tecnología y comportamiento pesquero.
  - [`04_management_system/`](docs/04_management_system/) - cómo funciona realmente el sistema de manejo, incluido el statu quo.
  - [`05_monitoring_data/`](docs/05_monitoring_data/) - cruceros, muestreos, datos pesqueros, cobertura, calidad y cambios de protocolo.
  - [`06_stock_assessment/`](docs/06_stock_assessment/) - evaluación de stock, supuestos, diagnósticos y puntos de referencia.
  - [`07_mse_scope_design/`](docs/07_mse_scope_design/) - pregunta del MSE, horizonte, escala temporal, espacialidad y nivel de complejidad.
  - [`08_operating_model/`](docs/08_operating_model/) - especificación y calibración del modelo que representa el sistema verdadero simulado.
  - [`09_observation_model/`](docs/09_observation_model/) - cómo se simulan errores y sesgos de los datos observados.
  - [`10_estimation_model/`](docs/10_estimation_model/) - cómo se reproduce la evaluación o indicador que recibe el procedimiento de manejo.
  - [`11_management_procedures/`](docs/11_management_procedures/) - procedimientos de manejo candidatos y sus reglas de decisión.
  - [`12_implementation_model/`](docs/12_implementation_model/) - diferencias entre una decisión de manejo y lo que realmente ocurre en la pesquería.
  - [`13_performance_metrics/`](docs/13_performance_metrics/) - indicadores usados para juzgar conservación, captura, estabilidad y otros objetivos.
  - [`14_uncertainty_scenarios/`](docs/14_uncertainty_scenarios/) - hipótesis principales y pruebas de robustez.
  - [`15_experimental_design/`](docs/15_experimental_design/) - número de simulaciones, semillas aleatorias y diseño de escenarios.
  - [`16_conditioning_validation/`](docs/16_conditioning_validation/) - comprobación de que el modelo operativo reproduce comportamientos plausibles.
  - [`17_tuning_selection/`](docs/17_tuning_selection/) - ajuste de parámetros de las reglas y comparación de alternativas.
  - [`18_ecosystem_climate/`](docs/18_ecosystem_climate/) - clima, no estacionariedad, depredadores y función de pez forraje.
  - [`19_economics_social/`](docs/19_economics_social/) - costos, ingresos, estabilidad y objetivos sociales cuando sean relevantes.
  - [`20_exceptional_circumstances/`](docs/20_exceptional_circumstances/) - qué hacer cuando el sistema entra en condiciones no representadas adecuadamente por el MSE.
  - [`21_adoption_monitoring_review/`](docs/21_adoption_monitoring_review/) - seguimiento después de adoptar una MP y calendario de revisión.
  - [`22_reporting_communication/`](docs/22_reporting_communication/) - informes técnicos, productos para decisión y comunicación de incertidumbre.
  - [`23_quality_assurance/`](docs/23_quality_assurance/) - control de calidad, reproducibilidad y revisión independiente.
- [`data/`](data/) - datos, separados por nivel de acceso y etapa de procesamiento.
  - [`examples/`](data/examples/) - datos ficticios pequeños para probar que el repositorio funciona.
  - [`public/`](data/public/) - datos que pueden redistribuirse públicamente.
  - [`raw_private/`](data/raw_private/) - datos originales restringidos; Git los ignora.
  - [`interim/`](data/interim/) - productos intermedios internos; su contenido no se versiona.
  - [`processed/`](data/processed/) - datos procesados internos; su contenido no se versiona salvo autorización explícita.
  - [`metadata/`](data/metadata/) - diccionarios, unidades, cobertura y reglas de calidad.
- [`references/`](references/) - documentos que sustentan el MSE.
  - [`regulations/`](references/regulations/) - normas y medidas oficiales de manejo.
  - [`assessment_reports/`](references/assessment_reports/) - informes de evaluación y asesoramiento.
  - [`survey_reports/`](references/survey_reports/) - informes de cruceros y monitoreo.
  - [`literature/`](references/literature/) - literatura científica utilizada.
- [`registry/`](registry/) - “libro de trazabilidad” del proyecto: tablas que permiten saber de dónde salió cada dato, parámetro, decisión, escenario o resultado.
- [`config/`](config/) - archivos de configuración que el código lee para saber **qué escenario ejecutar**; son equivalentes a fichas de parámetros, no a código científico.
  - [`reference_set/`](config/reference_set/) - conjunto principal de modelos operativos plausibles.
  - [`robustness_set/`](config/robustness_set/) - escenarios adicionales para someter las MPs a condiciones difíciles o alternativas.
  - [`management_procedures/`](config/management_procedures/) - parámetros y variantes de los procedimientos de manejo.
  - [`experiments/`](config/experiments/) - diseño de las corridas de simulación.
  - [`publication/`](config/publication/) - reglas para material público, interno o restringido.
- [`models/`](models/) - especificaciones científicas mínimas que debe cumplir cada componente del ciclo cerrado.
  - [`operating_model/`](models/operating_model/) - qué debe representar el modelo operativo.
  - [`observation_model/`](models/observation_model/) - qué errores de observación deben poder simularse.
  - [`estimation_model/`](models/estimation_model/) - qué debe recibir y producir la evaluación o estimador.
  - [`implementation_model/`](models/implementation_model/) - cómo representar errores y retrasos de implementación.
  - [`management_procedures/`](models/management_procedures/) - elementos obligatorios de una MP completa.
  - [`reference_points/`](models/reference_points/) - definiciones de puntos objetivo, disparadores y límites.
- [`src/`](src/) - funciones reutilizables: cálculos que pueden ser llamados por varias etapas del MSE.
  - [`om/`](src/om/) - funciones del modelo operativo.
  - [`observation/`](src/observation/) - funciones para generar datos observados simulados.
  - [`estimation/`](src/estimation/) - funciones de evaluación o estimación.
  - [`mp/`](src/mp/) - funciones de procedimientos y reglas de manejo.
  - [`implementation/`](src/implementation/) - funciones de implementación y respuesta de flota.
  - [`metrics/`](src/metrics/) - funciones que calculan métricas de desempeño.
  - [`validation/`](src/validation/) - diagnósticos y comprobaciones científicas.
  - [`io/`](src/io/) - funciones para leer, validar y guardar archivos.
- [`scripts/`](scripts/) - archivos que **inician y coordinan una etapa completa del flujo de trabajo**; llaman a las funciones de `src/`.
  - [`00_setup/`](scripts/00_setup/) - comprobar y mantener la estructura del repositorio.
  - [`01_data/`](scripts/01_data/) - preparar y validar datos.
  - [`02_condition_om/`](scripts/02_condition_om/) - calibrar/condicionar el modelo operativo.
  - [`03_validate_om/`](scripts/03_validate_om/) - comprobar que el OM produce dinámicas plausibles.
  - [`04_run_mse/`](scripts/04_run_mse/) - ejecutar la simulación de ciclo cerrado.
  - [`05_summarize/`](scripts/05_summarize/) - calcular y resumir métricas de desempeño.
  - [`06_reports/`](scripts/06_reports/) - generar informes reproducibles.
  - [`07_release/`](scripts/07_release/) - preparar entregas públicas, internas o privadas.
- [`tests/`](tests/) - comprobaciones automáticas para detectar errores de código o resultados científicamente imposibles.
  - [`unit/`](tests/unit/) - prueba cálculos individuales.
  - [`scientific/`](tests/scientific/) - prueba reglas científicas, unidades e invariantes.
  - [`integration/`](tests/integration/) - prueba que todos los componentes se conecten correctamente.
  - [`regression/`](tests/regression/) - detecta cambios involuntarios en resultados previamente aceptados.
- [`reports/`](reports/) - fuentes de los informes reproducibles.
  - [`technical/`](reports/technical/) - informe científico completo.
  - [`management/`](reports/management/) - resumen orientado a la decisión de manejo.
  - [`stakeholder/`](reports/stakeholder/) - material de talleres y comunicación.
- [`outputs/`](outputs/) - resultados generados por las corridas; son internos por defecto y deben poder regenerarse a partir de datos, código y configuración.
  - [`runs/`](outputs/runs/) - resultados por corrida identificada.
  - [`figures/`](outputs/figures/) - figuras derivadas.
  - [`tables/`](outputs/tables/) - tablas derivadas.
- [`certification/`](certification/) - copias congeladas de la versión que respalda un análisis o recomendación oficial.
  - [`reference_sets/`](certification/reference_sets/) - Reference Sets aprobados.
  - [`robustness_sets/`](certification/robustness_sets/) - Robustness Sets aprobados.
  - [`management_procedures/`](certification/management_procedures/) - MPs y parámetros aprobados.
  - [`run_manifests/`](certification/run_manifests/) - identidad exacta de cada corrida oficial.
  - [`review/`](certification/review/) - revisión independiente y respuestas.
  - [`software/`](certification/software/) - versiones del software usado.

## Archivos principales de la raíz

- [`README.md`](README.md) - explicación general y punto de entrada humano.
- [`species_profile.yml`](species_profile.yml) - ficha de identidad del stock/pesquería que se está estudiando.
- [`publication.yml`](publication.yml) - nivel de visibilidad del proyecto y reglas básicas de publicación.
- [`DATA_POLICY.md`](DATA_POLICY.md) - reglas para proteger datos institucionales.
- [`GOVERNANCE.md`](GOVERNANCE.md) - roles y responsabilidades.
- [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) - alcance y principios del proyecto.
- [`TREE.txt`](TREE.txt) - árbol técnico generado automáticamente; a diferencia de este documento, no contiene enlaces ni explicaciones.

## Regla práctica de navegación

No es necesario leer todos los README. Empiece por el [`README.md`](README.md), use este mapa para entrar a la carpeta relacionada con su tarea y lea **solo el README local de esa carpeta** antes de modificar sus archivos.
