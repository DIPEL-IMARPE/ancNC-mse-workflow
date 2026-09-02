# 05 — Resumir y comparar el desempeño

> [Volver a `scripts/`](../) · [Métricas de desempeño](../../docs/13_performance_metrics/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa transforma miles de trayectorias simuladas en información útil para comparar procedimientos de manejo.

El script `summarize_results.R` debería coordinar:

- cálculo de métricas de conservación, captura, estabilidad y otros objetivos;
- estimación de probabilidades de riesgo y distribuciones, no solo promedios;
- comparación entre MPs bajo el Reference Set y el Robustness Set;
- análisis de compromisos entre objetivos (*trade-offs*), por ejemplo más captura frente a mayor riesgo;
- identificación de alternativas que cumplen restricciones mínimas de desempeño;
- producción de tablas y figuras trazables a un `run_id`.

### Dos términos frecuentes

- **Trade-off:** mejorar un objetivo puede empeorar otro. Por ejemplo, aumentar la captura media puede aumentar el riesgo de baja biomasa.
- **Frontera de Pareto:** conjunto de alternativas para las que no es posible mejorar un objetivo sin empeorar al menos otro.

La selección final de una MP no debería basarse únicamente en un ranking numérico: debe respetar objetivos, tolerancias de riesgo y prioridades previamente acordadas.
