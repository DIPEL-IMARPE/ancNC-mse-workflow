# Fuentes que sustentan el MSE (`references/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Aquí se guardan —o se enlazan cuando no pueden redistribuirse— los documentos que respaldan los datos, parámetros, supuestos y decisiones del MSE. Esta carpeta funciona como la **biblioteca de evidencia** del proyecto.

| Carpeta | Qué contiene |
|---|---|
| [`regulations/`](regulations/) | Normas, resoluciones, cuotas, temporadas, vedas, cierres y otras medidas oficiales de manejo. |
| [`assessment_reports/`](assessment_reports/) | Evaluaciones de stock, benchmarks, actualizaciones, asesoramiento científico y revisiones. |
| [`survey_reports/`](survey_reports/) | Informes de cruceros, acústica, monitoreo y muestreos científicos. |
| [`literature/`](literature/) | Artículos, informes técnicos y otra literatura utilizada para sustentar hipótesis o parámetros. |

## Trazabilidad

Toda fuente importante debe tener un identificador en [`registry/source_registry.csv`](../registry/source_registry.csv). Después, los parámetros, datos o decisiones pueden apuntar a ese `source_id` en lugar de depender de notas informales.

Si un documento es restringido, registre su existencia y ubicación autorizada sin copiarlo a un repositorio público.
