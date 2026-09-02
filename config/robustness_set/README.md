# Robustness Set - pruebas adicionales de robustez

> [Volver a `config/`](../) · [Incertidumbre y escenarios](../../docs/14_uncertainty_scenarios/) · [Mapa completo](../../REPOSITORY_MAP.md)

El **Robustness Set** contiene escenarios adicionales utilizados para preguntar: **¿la MP sigue siendo aceptable si el sistema funciona de una manera difícil, menos probable o diferente a la incertidumbre central?**

Puede incluir, por ejemplo:

- fallas persistentes de reclutamiento;
- cambios de régimen;
- sesgo de disponibilidad acústica;
- pérdida de un crucero;
- selectividad, crecimiento o mortalidad mal especificados;
- retrasos de implementación;
- no estacionariedad climática;
- ruptura de una relación ambiente-reclutamiento utilizada históricamente.

Estos escenarios no deben mezclarse sin criterio con el Reference Set. En general, el Reference Set representa la incertidumbre central utilizada para el análisis principal y ajuste de MPs, mientras que el Robustness Set funciona como una **prueba de resistencia**.

Cada escenario debe tener una justificación en `registry/uncertainty_registry.csv` y `registry/scenario_registry.csv`; no agregue escenarios solo para producir una lista extensa de sensibilidades.
