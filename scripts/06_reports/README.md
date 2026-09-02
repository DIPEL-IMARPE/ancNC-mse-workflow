# 06 — Generar los informes

> [Volver a `scripts/`](../) · [Fuentes de informes](../../reports/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa genera de forma reproducible los informes del MSE a partir de resultados ya identificados.

El script `render_reports.R` debe coordinar la construcción de:

- informe técnico completo;
- resumen para gestores y toma de decisiones;
- material para talleres o actores involucrados cuando corresponda;
- tablas y figuras vinculadas a corridas específicas.

“Generar de forma reproducible” significa que el informe puede volver a construirse desde los mismos datos, resultados y archivos de configuración, sin copiar manualmente números entre documentos.

Los archivos fuente de los informes están en [`reports/`](../../reports/). Las cifras utilizadas para asesoramiento formal deberían corresponder a corridas registradas y, cuando proceda, certificadas.
