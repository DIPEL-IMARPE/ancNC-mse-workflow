# Glosario breve de `ancNC-mse-workflow`

> Este glosario complementa el [`README.md`](README.md). Incluye términos científicos y computacionales que aparecen con frecuencia en el repositorio.

| Término | Explicación breve |
|---|---|
| MSE | Evaluación por simulación de procedimientos de manejo bajo incertidumbre. |
| OM / Operating Model | Modelo que representa un sistema verdadero plausible dentro de la simulación. |
| Conditioning | Calibración del OM para que sea compatible con evidencia histórica y rangos plausibles. |
| Observation Model | Modelo que convierte el estado verdadero simulado en datos imperfectos. |
| Estimation Model | Evaluación, estimador o indicador utilizado por la MP. |
| MP / Management Procedure | Procedimiento preacordado que transforma información observada en una acción de manejo. |
| HCR / Harvest Control Rule | Regla de decisión dentro de una MP. |
| Implementation Model | Modelo de diferencias entre la acción recomendada y la realizada. |
| Closed loop / ciclo cerrado | Simulación iterativa OM → datos → evaluación → MP → implementación → OM. |
| Reference Set | Conjunto principal de OMs plausibles usado para la evaluación central. |
| Robustness Set | Escenarios alternativos o difíciles usados para comprobar robustez. |
| Tuning | Ajuste de parámetros de una MP con objetivos definidos previamente. |
| Monte Carlo | Repetición de simulaciones con variación aleatoria para estimar riesgos y distribuciones. |
| Hindcast | Evaluación usando un periodo histórico conocido. |
| Holdout | Datos reservados para validación y no utilizados para calibrar. |
| Registry | Tabla de trazabilidad del proyecto. |
| Config | Archivo de parámetros y opciones que el código lee para ejecutar un escenario. |
| `src/` | Funciones reutilizables que contienen cálculos. |
| `scripts/` | Archivos que inician y coordinan etapas completas del flujo de trabajo. |
| Test | Comprobación automática de código o coherencia científica. |
| Run | Una ejecución identificada del experimento de simulación. |
| Seed / semilla | Número que permite reproducir exactamente una secuencia pseudoaleatoria. |
| Checksum | Huella digital de un archivo para comprobar que no cambió. |
| Certificación | Congelamiento documentado de una versión usada para un análisis formal. |
| CI / Continuous Integration | Comprobaciones automáticas que GitHub ejecuta cuando cambia el repositorio. |
| Pull Request | Propuesta de cambio que puede revisarse antes de incorporarse a la rama principal. |
