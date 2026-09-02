<img align="right" src="assets/logo_hex_mse.svg" alt="Logo de Evaluación de Estrategias de Manejo" width="110">

# Evaluación de Estrategias de Manejo (MSE) para pesquerías

<br clear="right">

> **Idioma principal:** español. [English version](README.en.md) - [Mapa completo del repositorio](REPOSITORY_MAP.md)

Este repositorio es una **plantilla reutilizable para desarrollar una Evaluación de Estrategias de Manejo (Management Strategy Evaluation, MSE) de una especie, stock o pesquería**. Está orientado a ecólogos, biólogos pesqueros, evaluadores de stock, especialistas en manejo, consultores y modeladores que necesitan trabajar sobre una estructura común, trazable y reproducible.

No es una MSE ya resuelta y no contiene parámetros verdaderos de una especie real. El perfil inicial utiliza campos genéricos de ejemplo. Al crear un proyecto nuevo, esos campos deben reemplazarse por la especie, stock, pesquería, área de manejo e instituciones correspondientes.

## Qué representa una MSE en este template

Una MSE no consiste únicamente en elegir una cuota o una regla de control de captura. Evalúa si un procedimiento de manejo sigue cumpliendo los objetivos acordados cuando existen incertidumbres sobre la dinámica del recurso, la pesquería, los datos, la evaluación y la implementación de las medidas.

El ciclo general es:

`objetivos de manejo -> sistema biológico y pesquero -> modelo operativo -> observaciones simuladas -> evaluación o indicador -> procedimiento de manejo -> implementación -> respuesta del sistema -> métricas de desempeño -> comparación de alternativas`.

Después de seleccionar una estrategia, el proceso continúa con seguimiento, revisión periódica y un protocolo para circunstancias excepcionales.

## Archivos principales de la raíz

Los archivos visibles en la pantalla principal de GitHub cumplen funciones diferentes:

| Archivo | Para qué sirve |
|---|---|
| [`README.md`](README.md) | Portada y guía principal del repositorio. |
| [`README.en.md`](README.en.md) | Versión en inglés de la documentación principal. |
| [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md) | Mapa navegable de carpetas y subcarpetas. |
| [`GLOSSARY.md`](GLOSSARY.md) | Glosario de términos de MSE y del repositorio. |
| [`TEMPLATE_USAGE.md`](TEMPLATE_USAGE.md) | Guía práctica para crear un proyecto a partir de este template. |
| [`species_profile.yml`](species_profile.yml) | Ficha general del caso: especie, stock, región, instituciones y decisiones básicas de escala. |
| [`publication.yml`](publication.yml) | Define niveles de visibilidad y ayuda a distinguir contenido público, interno y restringido. |
| [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) | Resume el propósito, alcance y principios generales del proyecto. |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Define roles, responsabilidades y reglas para registrar decisiones. |
| [`DATA_POLICY.md`](DATA_POLICY.md) | Establece cómo manejar datos públicos, internos y restringidos. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Indica cómo realizar cambios sin perder trazabilidad ni reproducibilidad. |
| [`SECURITY.md`](SECURITY.md) | Resume las reglas para proteger credenciales e información sensible. |
| [`CHANGELOG.md`](CHANGELOG.md) | Registra los cambios relevantes entre versiones del template. |
| [`CITATION.cff`](CITATION.cff) | Metadatos para facilitar la citación del repositorio. |
| [`VERSION`](VERSION) | Indica la versión actual del template. |
| [`Makefile`](Makefile) | Contiene atajos opcionales para ejecutar verificaciones y tareas repetitivas. |

Cada carpeta tiene además su propio `README.md`, que explica qué debe guardarse allí y cómo se relaciona con el resto del proyecto. No es necesario leerlos todos: consulte el README de la carpeta en la que esté trabajando.

## Carpetas principales

| Carpeta | Para qué sirve |
|---|---|
| [`.github/`](.github/ABOUT.md) | Automatización y revisión dentro de GitHub; no contiene componentes científicos del MSE. |
| [`assets/`](assets/) | Recursos gráficos del repositorio, incluido el logo. |
| [`docs/`](docs/) | Documentación científica e institucional del proyecto. |
| [`data/`](data/) | Datos organizados según nivel de acceso y etapa de procesamiento. |
| [`references/`](references/) | Normas, informes técnicos y literatura que respaldan el proyecto. |
| [`registry/`](registry/) | Tablas maestras de trazabilidad de fuentes, datos, parámetros, escenarios, decisiones y corridas. |
| [`config/`](config/) | Archivos de configuración que indican qué valores, escenarios, modelos o procedimientos se ejecutan. |
| [`models/`](models/) | Especificaciones conceptuales de los componentes del MSE. |
| [`src/`](src/) | Funciones reutilizables que realizan cálculos y operaciones del proyecto. |
| [`scripts/`](scripts/) | Archivos que inician y coordinan cada etapa del trabajo. |
| [`tests/`](tests/) | Pruebas automáticas de código, integración y coherencia científica. |
| [`reports/`](reports/) | Fuentes reproducibles de informes técnicos, resúmenes para gestión y materiales de comunicación. |
| [`outputs/`](outputs/) | Resultados generados por las simulaciones y análisis. |
| [`certification/`](certification/) | Versiones congeladas y auditables de configuraciones, procedimientos, software y corridas. |

### [Ver el mapa completo de carpetas y subcarpetas](REPOSITORY_MAP.md)

## Cómo se relacionan `docs`, `config`, `models`, `src` y `scripts`

- **`docs/`** explica por qué se toma una decisión y qué significa científicamente.
- **`models/`** define qué elementos mínimos debe representar cada componente del MSE.
- **`config/`** guarda los valores y opciones concretos que se usarán en una corrida.
- **`src/`** contiene las funciones que realizan los cálculos.
- **`scripts/`** organiza el orden de ejecución y llama a las funciones necesarias para completar una etapa.

Por ejemplo, una decisión sobre reclutamiento puede estar justificada en `docs/08_operating_model/`, descrita como requisito en `models/operating_model/`, parametrizada en `config/operating_model.yml`, implementada mediante funciones en `src/om/` y ejecutada desde `scripts/02_condition_om/`.

## Flujo científico recomendado

1. Definir el caso de estudio en [`species_profile.yml`](species_profile.yml).
2. Definir objetivos de manejo, prioridades y tolerancias de riesgo en [`docs/01_governance_objectives/`](docs/01_governance_objectives/).
3. Documentar biología, ecología, pesquería, manejo, monitoreo y evaluación de stock en [`docs/02_stock_ecology/`](docs/02_stock_ecology/) a [`docs/06_stock_assessment/`](docs/06_stock_assessment/).
4. Registrar fuentes, datos, parámetros y decisiones en [`references/`](references/) y [`registry/`](registry/).
5. Definir la pregunta de manejo, horizonte temporal y complejidad necesaria en [`docs/07_mse_scope_design/`](docs/07_mse_scope_design/).
6. Construir, condicionar y validar los modelos operativos.
7. Definir el modelo de observación, el modelo de estimación y los procedimientos de manejo candidatos.
8. Definir las métricas de desempeño antes de comparar alternativas.
9. Ejecutar la simulación de ciclo cerrado y evaluar riesgos y compromisos entre objetivos.
10. Documentar circunstancias excepcionales, seguimiento y revisión periódica.
11. Congelar en [`certification/`](certification/) la versión utilizada para un análisis oficial.

## El ejemplo del template es genérico

[`species_profile.yml`](species_profile.yml) contiene campos como `Example species`, `Example stock` y `Example management area`. Son marcadores de posición y no corresponden a una especie, institución o pesquería real.

Los campos `TBD` significan **por definir con evidencia o mediante una decisión científica documentada**. No deben completarse arbitrariamente solo para llenar el archivo.

## Datos públicos, internos y restringidos

El template distingue información `public`, `derived_public`, `internal` y `restricted`. `data/raw_private/` y `local_private/` están destinados a información que no debe entrar al historial de Git. Consulte [`DATA_POLICY.md`](DATA_POLICY.md) y [`publication.yml`](publication.yml).
