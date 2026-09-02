# Informes reproducibles (`reports/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Aquí se guardan los **archivos fuente de los informes**, no copias manuales desconectadas del análisis. La meta es que tablas y figuras puedan regenerarse desde corridas identificadas del MSE.

| Carpeta | Producto principal |
|---|---|
| [`technical/`](technical/) | Informe científico completo: datos, supuestos, OMs, MPs, incertidumbre, resultados, diagnósticos y limitaciones. |
| [`management/`](management/) | Resumen orientado a la decisión: objetivos, riesgos, trade-offs, alternativas y recomendación. |
| [`stakeholder/`](stakeholder/) | Material para talleres, discusión de objetivos y comunicación con actores involucrados. |

## Principio de trazabilidad

Un número presentado en un informe debería poder vincularse con una corrida registrada en [`registry/run_registry.csv`](../registry/run_registry.csv) y, cuando sea un producto oficial, con un manifiesto en [`certification/run_manifests/`](../certification/run_manifests/).

Los informes deben comunicar incertidumbre y riesgo; no solo un ranking final de MPs.
