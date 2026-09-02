# Archivos de configuración (`config/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Los archivos de esta carpeta son **fichas de parámetros y opciones que el código lee para saber qué escenario ejecutar**. No contienen la justificación científica completa y no deberían usarse para introducir decisiones nuevas sin documentarlas.

Piense en `config/` como el lugar donde se traduce una decisión científica ya acordada a una forma que la computadora pueda leer.

| Archivo o carpeta | Qué controla |
|---|---|
| [`operating_model.yml`](operating_model.yml) | Estructura y opciones del modelo operativo: escala temporal, reclutamiento, crecimiento, mortalidad, selectividad, espacio, ambiente, etc. |
| [`observation_model.yml`](observation_model.yml) | Errores y sesgos de índices, captura, tallas, muestreo y monitoreo. |
| [`estimation_model.yml`](estimation_model.yml) | Tipo de evaluación/estimador, frecuencia, fallas y procedimiento alternativo. |
| [`implementation_model.yml`](implementation_model.yml) | Diferencias entre medidas recomendadas y realizadas: cumplimiento, retrasos, cuota capturada, respuesta espacial, etc. |
| [`performance_metrics.yml`](performance_metrics.yml) | Métricas, restricciones de riesgo y criterios generales de comparación. |
| [`reference_set/`](reference_set/) | Configuración del conjunto principal de modelos operativos plausibles. |
| [`robustness_set/`](robustness_set/) | Escenarios adicionales para comprobar la robustez de las MPs. |
| [`management_procedures/`](management_procedures/) | MPs candidatas y parámetros que pueden ajustarse. |
| [`experiments/`](experiments/) | Número de simulaciones, horizonte, semillas y combinaciones que se ejecutarán. |
| [`publication/`](publication/) | Clasificación de archivos y reglas para productos públicos, internos o restringidos. |

## Relación con otras carpetas

- `docs/` explica **por qué** se tomó una decisión.
- `registry/` registra **de dónde salió** y quién la aprobó.
- `config/` indica **qué valores concretos se ejecutarán**.
- `src/` contiene **cómo se calcula**.
- `scripts/` coordina **cuándo se ejecuta cada etapa**.

Un cambio material en `config/` debería tener una justificación trazable en `docs/` o `registry/`.
