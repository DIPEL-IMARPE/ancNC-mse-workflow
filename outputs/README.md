# Resultados generados (`outputs/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta contiene los resultados producidos por las corridas del MSE. **No es una fuente primaria de información**: cualquier resultado importante debería poder regenerarse a partir de datos, código, configuración y semillas registradas.

| Carpeta | Qué contiene |
|---|---|
| [`runs/`](runs/) | Resultados completos organizados por identificador de corrida (`run_id`). |
| [`figures/`](figures/) | Figuras derivadas de corridas identificadas. |
| [`tables/`](tables/) | Tablas derivadas de corridas identificadas. |

## Regla práctica

No guarde aquí archivos manuales sin origen conocido. Cada corrida importante debe aparecer en [`registry/run_registry.csv`](../registry/run_registry.csv). Para análisis usados formalmente en asesoramiento, conserve además un manifiesto en [`certification/run_manifests/`](../certification/run_manifests/).

En muchos proyectos los resultados voluminosos no se versionan en Git; se conserva en Git la configuración, trazabilidad y documentación necesarias para reproducirlos.
