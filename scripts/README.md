# Scripts que ejecutan las etapas del MSE (`scripts/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta contiene los archivos que **inician y coordinan cada gran etapa del flujo de trabajo**. En programación a veces se les llama *entrypoints*, pero aquí usaremos una expresión más clara: **scripts de ejecución**.

Un script de ejecución no debería contener todas las ecuaciones del MSE. Su función es indicar el orden de las tareas, leer configuraciones, llamar a las funciones de `src/`, guardar resultados y registrar qué se ejecutó.

| Etapa | Carpeta | Qué hace |
|---:|---|---|
| 00 | [`00_setup/`](00_setup/) | Comprueba que el repositorio tenga la estructura esperada y actualiza inventarios técnicos. |
| 01 | [`01_data/`](01_data/) | Lee, limpia, integra y valida los datos necesarios para el proyecto. |
| 02 | [`02_condition_om/`](02_condition_om/) | Calibra o condiciona los modelos operativos usando la evidencia disponible. |
| 03 | [`03_validate_om/`](03_validate_om/) | Comprueba que los modelos operativos produzcan dinámicas científicamente plausibles. |
| 04 | [`04_run_mse/`](04_run_mse/) | Ejecuta la simulación de ciclo cerrado: OM → observación → evaluación → MP → implementación → OM. |
| 05 | [`05_summarize/`](05_summarize/) | Calcula métricas de desempeño y resume riesgos, distribuciones y comparaciones entre MPs. |
| 06 | [`06_reports/`](06_reports/) | Genera los informes reproducibles a partir de resultados identificados. |
| 07 | [`07_release/`](07_release/) | Prepara productos para entrega pública, interna o privada según las reglas de visibilidad. |

## Diferencia con `src/`

- En [`src/`](../src/) están las **funciones y ecuaciones reutilizables**.
- En `scripts/` están los **archivos que organizan cuándo y en qué orden se usan esas funciones**.

Ejemplo: `src/metrics/` puede contener una función que calcula el riesgo de caer bajo un punto límite; `scripts/05_summarize/` llama a esa función para todas las simulaciones y construye la tabla final de desempeño.

Los scripts deben poder ejecutarse de forma reproducible, sin depender de pasos manuales no documentados.
