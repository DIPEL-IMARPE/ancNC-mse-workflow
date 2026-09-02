# 17 - Ajustar y seleccionar procedimientos de manejo

> [Volver a `docs/`](../) · [Métricas](../13_performance_metrics/) · [Reference/Robustness Sets](../14_uncertainty_scenarios/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa tiene dos tareas diferentes: **ajustar los parámetros de una MP** y **seleccionar entre alternativas**.

## Ajuste o *tuning*

El tuning modifica parámetros previamente identificados -por ejemplo un nivel objetivo de explotación, un umbral o un límite de cambio anual- para que la MP cumpla objetivos acordados.

Los objetivos y tolerancias de riesgo deben existir antes del tuning. No se deberían cambiar los criterios para favorecer una MP después de observar los resultados.

## Evitar el sobreajuste

Una MP puede parecer excelente si se ajusta específicamente a cada escenario que después se utiliza para evaluarla. Para reducir ese problema:

- use principalmente el Reference Set para el ajuste central;
- mantenga escenarios adicionales como pruebas independientes de robustez cuando sea posible;
- documente cualquier uso del Robustness Set durante el tuning;
- utilice holdouts o escenarios no usados en el ajuste cuando el diseño lo permita.

## Selección

La selección debe comenzar eliminando alternativas que violan restricciones de riesgo. Entre las restantes, compare compromisos entre objetivos mediante tablas, gráficos y, cuando sea útil, fronteras de Pareto.

La recomendación final debe explicar **qué se gana y qué se sacrifica** con cada alternativa, no solo presentar un ranking.
