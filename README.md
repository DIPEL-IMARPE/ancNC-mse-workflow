<img align="right" src="assets/logo_hex_mse.svg" alt="Logo de Evaluación de Estrategias de Manejo" width="110">

# Evaluación de Estrategias de Manejo (MSE) de la anchoveta peruana - stock Norte-Centro

<br clear="right">

> **Idioma principal:** español. [English version](README.en.md) - [Mapa completo del repositorio](REPOSITORY_MAP.md)

Este repositorio desarrolla un flujo analítico reproducible para la **Evaluación de Estrategias de Manejo (Management Strategy Evaluation, MSE) del stock Norte-Centro de anchoveta peruana (*Engraulis ringens*)**.

El proyecto está orientado a evaluar, mediante simulación de ciclo cerrado, el desempeño de procedimientos de manejo alternativos frente a incertidumbre en la dinámica poblacional, el reclutamiento, la observación del recurso, la evaluación de stock, la respuesta de la pesquería y la implementación de las medidas de manejo.

El repositorio está diseñado para el trabajo científico de **DIPEL-IMARPE** y para la colaboración con especialistas y consultores autorizados. La documentación debe permitir que una persona externa al desarrollo comprenda la biología del recurso, la pesquería, el sistema de monitoreo, la evaluación de stock, el marco de manejo, los supuestos del modelo operativo y la evidencia utilizada para cada decisión del MSE.

Este repositorio **no representa todavía una estrategia de manejo adoptada** ni presupone que una regla de control específica sea adecuada. Los componentes del MSE se incorporarán progresivamente y toda decisión importante deberá quedar respaldada por evidencia trazable o por una decisión científica documentada.

## Qué representa una MSE en este proyecto

Una MSE no consiste únicamente en elegir una cuota o una regla de control de captura. Evalúa si un procedimiento de manejo sigue cumpliendo los objetivos acordados cuando existen incertidumbres sobre la dinámica del recurso, la pesquería, los datos, la evaluación y la implementación de las medidas.

El ciclo general es:

`objetivos de manejo -> sistema biológico y pesquero -> modelo operativo -> observaciones simuladas -> evaluación o indicador -> procedimiento de manejo -> implementación -> respuesta del sistema -> métricas de desempeño -> comparación de alternativas`.

Después de seleccionar una estrategia, el proceso continúa con seguimiento, revisión periódica y un protocolo para circunstancias excepcionales.

## Estado actual

El proyecto se encuentra en **fase de inicialización científica**. Antes de programar procedimientos de manejo se deben completar, como mínimo:

1. objetivos de manejo y tolerancias de riesgo;
2. síntesis de biología y ecología del stock;
3. descripción de la pesquería y sus flotas;
4. reconstrucción del sistema histórico y actual de manejo;
5. inventario y caracterización de los sistemas de monitoreo;
6. documentación de la evaluación de stock;
7. inventario de datos, fuentes, parámetros e incertidumbres;
8. definición justificada del alcance y complejidad del MSE.

Los campos `TBD` significan **por definir con evidencia o mediante una decisión científica documentada**. No deben completarse arbitrariamente.

## Archivos principales de la raíz

| Archivo | Para qué sirve |
|---|---|
| [`README.md`](README.md) | Portada y guía principal del proyecto. |
| [`README.en.md`](README.en.md) | Versión resumida en inglés. |
| [`REPOSITORY_MAP.md`](REPOSITORY_MAP.md) | Mapa navegable de carpetas y subcarpetas. |
| [`GLOSSARY.md`](GLOSSARY.md) | Glosario de términos de MSE y del repositorio. |
| [`species_profile.yml`](species_profile.yml) | Ficha del caso: especie, stock, instituciones y decisiones básicas de escala. |
| [`publication.yml`](publication.yml) | Clasifica qué contenido puede ser público, interno o restringido. |
| [`PROJECT_CHARTER.md`](PROJECT_CHARTER.md) | Propósito, alcance y principios científicos del proyecto. |
| [`GOVERNANCE.md`](GOVERNANCE.md) | Roles y reglas para registrar decisiones. |
| [`DATA_POLICY.md`](DATA_POLICY.md) | Política para datos públicos, derivados, internos y restringidos. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Reglas para realizar cambios sin perder trazabilidad. |
| [`SECURITY.md`](SECURITY.md) | Protección de credenciales e información sensible. |
| [`CHANGELOG.md`](CHANGELOG.md) | Historial de versiones del proyecto. |
| [`CITATION.cff`](CITATION.cff) | Metadatos para citar el repositorio. |
| [`VERSION`](VERSION) | Versión actual de `ancNC-mse-workflow`. |

Cada carpeta tiene su propio `README.md`. No es necesario leerlos todos: use el [mapa del repositorio](REPOSITORY_MAP.md), entre a la carpeta relacionada con la tarea actual y lea su README local.

## Carpetas principales

| Carpeta | Para qué sirve |
|---|---|
| [`.github/`](.github/ABOUT.md) | Automatización y revisión dentro de GitHub. |
| [`assets/`](assets/) | Recursos gráficos. |
| [`docs/`](docs/) | Documentación científica e institucional del MSE. |
| [`data/`](data/) | Datos según nivel de acceso y etapa de procesamiento. |
| [`references/`](references/) | Normas, informes y literatura autorizados para versionarse; las fuentes restringidas se registran sin copiarse. |
| [`registry/`](registry/) | Trazabilidad de fuentes, datos, parámetros, escenarios, decisiones y corridas. |
| [`config/`](config/) | Configuraciones de modelos, escenarios y experimentos. |
| [`models/`](models/) | Especificaciones conceptuales de los componentes del MSE. |
| [`src/`](src/) | Funciones reutilizables. |
| [`scripts/`](scripts/) | Scripts que coordinan cada etapa del trabajo. |
| [`tests/`](tests/) | Pruebas de código, integración y coherencia científica. |
| [`reports/`](reports/) | Fuentes reproducibles de informes. |
| [`outputs/`](outputs/) | Resultados generados; son internos por defecto y no se versionan. |
| [`certification/`](certification/) | Versiones congeladas y auditables de análisis oficiales. |

### [Ver el mapa completo de carpetas y subcarpetas](REPOSITORY_MAP.md)

## Cómo se relacionan `docs`, `config`, `models`, `src` y `scripts`

- **`docs/`** explica por qué se toma una decisión y qué significa científicamente.
- **`models/`** define qué elementos mínimos debe representar cada componente del MSE.
- **`config/`** guarda los valores y opciones concretos utilizados en una corrida.
- **`src/`** contiene las funciones que realizan los cálculos.
- **`scripts/`** organiza el orden de ejecución y llama a las funciones necesarias para completar una etapa.

Por ejemplo, una hipótesis sobre reclutamiento puede estar justificada en `docs/08_operating_model/`, descrita como requisito en `models/operating_model/`, parametrizada en `config/operating_model.yml`, implementada mediante funciones en `src/om/` y ejecutada desde `scripts/02_condition_om/`.

## Datos públicos, internos y restringidos

Este repositorio GitHub es público, pero **los datos institucionales no se vuelven públicos por estar asociados al proyecto**. La política distingue cuatro clases:

- `public`: puede versionarse y redistribuirse después de verificar fuente y permiso;
- `derived_public`: producto derivado de información no pública, pero expresamente autorizado para difusión;
- `internal`: solo para colaboradores autorizados; no se versiona en este repositorio público;
- `restricted`: no debe entrar al historial de Git.

Por seguridad, `.gitignore` excluye `data/raw_private/`, `data/interim/`, `data/processed/`, `outputs/` y `local_private/`, preservando únicamente sus README. Los conjuntos de datos pueden describirse públicamente en `registry/data_inventory.csv` sin publicar sus observaciones.

Consulte [`DATA_POLICY.md`](DATA_POLICY.md) y [`data/README.md`](data/README.md) antes de incorporar cualquier archivo de datos.
