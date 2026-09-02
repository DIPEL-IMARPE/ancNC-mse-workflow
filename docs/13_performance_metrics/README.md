# 13 — Métricas de desempeño: cómo juzgar una estrategia

> [Volver a `docs/`](../) · [Registro de métricas](../../registry/performance_metric_registry.csv) · [Configuración](../../config/performance_metrics.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

Las métricas de desempeño traducen los objetivos de manejo a cantidades que pueden calcularse en las simulaciones.

## Ejemplos

**Conservación**
- probabilidad de caer por debajo de un punto límite;
- biomasa media o mediana;
- tiempo necesario para recuperarse de un estado bajo.

**Pesquería y estabilidad**
- captura media o mediana;
- variabilidad interanual o entre temporadas;
- probabilidad de cierre;
- duración de temporada;
- esfuerzo requerido.

**Estructura del stock y juveniles**
- captura o mortalidad de juveniles;
- proporción de temporadas con alta incidencia juvenil;
- cambios en estructura de tallas cuando sean un objetivo explícito.

**Ecosistema, economía e información**
- biomasa disponible como forraje;
- indicadores económicos o sociales acordados;
- costo o beneficio de aumentar frecuencia/precisión del monitoreo.

## Reportar riesgo, no solo promedios

Dos MPs pueden tener la misma captura promedio y riesgos muy diferentes. Por eso las comparaciones deberían mostrar distribuciones, probabilidades de exceder umbrales, cuantiles y horizontes temporales relevantes.

Cada métrica debe estar vinculada con un objetivo en `registry/objective_registry.csv`, tener una definición inequívoca y especificar si valores altos o bajos representan mejor desempeño.
