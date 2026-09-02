# Reference Set - conjunto principal de modelos operativos

> [Volver a `config/`](../) · [Incertidumbre y escenarios](../../docs/14_uncertainty_scenarios/) · [Mapa completo](../../REPOSITORY_MAP.md)

El **Reference Set** es el conjunto principal de modelos operativos que el equipo considera suficientemente plausibles para representar la incertidumbre central del sistema.

No es “el mejor modelo” ni un único escenario base. Puede contener varios OMs que difieren, por ejemplo, en reclutamiento, mortalidad, crecimiento, selectividad o productividad, siempre que esas diferencias estén respaldadas por evidencia o decisiones científicas explícitas.

`reference_set.yml` debe identificar:

- qué OMs forman parte del conjunto;
- cómo se relacionan con `registry/scenario_registry.csv`;
- si todos tienen el mismo peso o existe un esquema de ponderación;
- qué versión del conjunto se utiliza en cada experimento.

Este conjunto suele ser la base principal para evaluar y ajustar (*tuning*) las MPs. Los escenarios más extremos, secundarios o de prueba se mantienen separados en `robustness_set/` para evitar mezclar incertidumbre central con pruebas de estrés.
