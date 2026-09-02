# 02 — Calibrar los modelos operativos

> [Volver a `scripts/`](../) · [Documentación del OM](../../docs/08_operating_model/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa construye el conjunto de **modelos operativos (OMs) plausibles** que representarán distintos posibles “sistemas verdaderos” dentro de la simulación.

En este contexto, **condicionar o calibrar** significa elegir o estimar parámetros y estados iniciales de forma que los OMs sean compatibles con la evidencia histórica y con rangos biológicos/pesqueros razonables.

El script `condition_om.R` debería coordinar, según el caso:

- lectura de parámetros y distribuciones desde `config/`;
- estimación o muestreo de incertidumbre paramétrica;
- ajuste a historia de biomasa, captura, composiciones u otros datos cuando corresponda;
- generación de múltiples OMs si existen hipótesis estructurales alternativas;
- almacenamiento de diagnósticos necesarios para la etapa de validación;
- registro de cada escenario en `registry/scenario_registry.csv` y `registry/parameter_registry.csv`.

**Importante:** que un OM pueda ajustarse numéricamente no significa que sea científicamente plausible. La siguiente etapa, `03_validate_om/`, debe comprobarlo explícitamente.
