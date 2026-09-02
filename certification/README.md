# Versiones congeladas y auditables (`certification/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta se utiliza cuando una versión del MSE deja de ser solamente material de desarrollo y pasa a respaldar una comparación formal, revisión independiente o recomendación de manejo.

“Certificar” aquí significa **congelar y documentar exactamente qué versión se utilizó**: código, configuraciones, conjuntos de modelos operativos, MPs, semillas aleatorias, software y resultados. No implica una certificación legal automática.

| Carpeta | Qué conserva |
|---|---|
| [`reference_sets/`](reference_sets/) | Versiones aprobadas del conjunto principal de modelos operativos. |
| [`robustness_sets/`](robustness_sets/) | Versiones aprobadas de los escenarios de robustez. |
| [`management_procedures/`](management_procedures/) | MPs, HCRs y parámetros de ajuste utilizados en el análisis formal. |
| [`run_manifests/`](run_manifests/) | Ficha exacta de cada corrida oficial: commit, configuración, semillas, software y huellas digitales de archivos. |
| [`review/`](review/) | Observaciones de revisión independiente y respuestas del equipo. |
| [`software/`](software/) | Versiones de R, Python, Stock Synthesis, OpenMSE, FLR u otros motores utilizados. |

## Por qué existe

El código continúa evolucionando después de una recomendación. Sin una copia congelada sería difícil reproducir, meses después, exactamente los resultados utilizados en una decisión. Esta carpeta separa claramente **desarrollo activo** de **versiones formalmente utilizadas**.

Nunca modifique en sitio una versión ya aprobada; cree una nueva versión con nueva identificación.
