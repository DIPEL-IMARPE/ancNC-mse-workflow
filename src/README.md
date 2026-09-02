# Funciones y cálculos reutilizables (`src/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

`src` significa *source code*. En este proyecto contiene las **funciones reutilizables que realizan los cálculos del MSE**. Una función puede calcular reclutamiento, generar un índice observado, aplicar una HCR o calcular una métrica de riesgo.

La idea es evitar copiar la misma ecuación en varios archivos. Las funciones se escriben aquí una vez y luego los scripts de `scripts/` las utilizan cuando ejecutan cada etapa del proyecto.

| Carpeta | Qué calcula |
|---|---|
| [`om/`](om/) | Dinámica del modelo operativo: población, reclutamiento, crecimiento, mortalidad, pesca, etc. |
| [`observation/`](observation/) | Generación de datos observados simulados y sus errores. |
| [`estimation/`](estimation/) | Evaluación de stock, estimadores o indicadores utilizados por las MPs. |
| [`mp/`](mp/) | Procedimientos de manejo y reglas de decisión. |
| [`implementation/`](implementation/) | Implementación imperfecta y respuesta de la flota. |
| [`metrics/`](metrics/) | Métricas de desempeño y riesgo. |
| [`validation/`](validation/) | Diagnósticos, validación, hindcast, holdout y pruebas de plausibilidad. |
| [`io/`](io/) | Lectura, validación y escritura de datos, configuraciones y resultados. |

## Diferencia con `scripts/`

- `src/` contiene **cómo se hace un cálculo**.
- `scripts/` contiene **qué etapa se ejecuta y en qué orden**.

Por ejemplo, una función que calcula el reclutamiento pertenece en `src/om/`; el archivo que inicia el proceso completo de calibrar los modelos operativos pertenece en `scripts/02_condition_om/`.
