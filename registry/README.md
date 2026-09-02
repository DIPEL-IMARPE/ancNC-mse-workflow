# Tablas de trazabilidad (`registry/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

`registry/` es el **libro de registro del proyecto**. Su función es que, meses o años después, una persona pueda responder preguntas como: “¿de dónde salió este parámetro?”, “¿qué norma respalda esta medida?”, “¿qué versión de la MP produjo este resultado?” o “¿por qué se incluyó este escenario?”.

No contiene el modelo en sí. Contiene tablas simples (`.csv`) que conectan evidencia, decisiones y resultados.

| Archivo | Qué registra |
|---|---|
| [`source_registry.csv`](source_registry.csv) | Documentos y fuentes utilizados por el proyecto. |
| [`data_inventory.csv`](data_inventory.csv) | Conjuntos de datos disponibles, propietarios, cobertura, acceso y uso dentro del MSE. |
| [`parameter_registry.csv`](parameter_registry.csv) | Parámetros, definición, unidades, valor/distribución, fuente y tratamiento de incertidumbre. |
| [`management_history.csv`](management_history.csv) | Historia de medidas de manejo por fecha, temporada, área y fundamento. |
| [`regulation_registry.csv`](regulation_registry.csv) | Normas y documentos regulatorios. |
| [`objective_registry.csv`](objective_registry.csv) | Objetivos operacionales, métricas, horizonte temporal, prioridad y tolerancia de riesgo. |
| [`uncertainty_registry.csv`](uncertainty_registry.csv) | Incertidumbres biológicas, observacionales, de evaluación, implementación, clima u otras. |
| [`scenario_registry.csv`](scenario_registry.csv) | Escenarios del Reference Set y Robustness Set. |
| [`mp_registry.csv`](mp_registry.csv) | Procedimientos de manejo candidatos, versiones y estado de ajuste/certificación. |
| [`performance_metric_registry.csv`](performance_metric_registry.csv) | Definición formal de cada métrica de desempeño y su vínculo con objetivos. |
| [`run_registry.csv`](run_registry.csv) | Corridas de simulación: fecha, versión del código, configuración, semillas y resultados. |
| [`decision_log.csv`](decision_log.csv) | Decisiones científicas materiales, alternativas consideradas y evidencia utilizada. |
| [`exceptional_circumstances_registry.csv`](exceptional_circumstances_registry.csv) | Indicadores y respuestas preacordadas para circunstancias excepcionales. |
| [`software_registry.csv`](software_registry.csv) | Versiones del software y motores utilizados. |
| [`file_manifest.csv`](file_manifest.csv) | Inventario técnico de archivos del repositorio. |

## Regla práctica

Si un número, supuesto o decisión puede afectar la conclusión del MSE, debería poder rastrearse desde el resultado hacia una fila de `registry/` y desde allí hacia una fuente o una decisión documentada.
