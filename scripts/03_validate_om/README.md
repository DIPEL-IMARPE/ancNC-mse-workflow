# 03 - Validar los modelos operativos

> [Volver a `scripts/`](../) · [Validación científica](../../docs/16_conditioning_validation/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa comprueba si los modelos operativos construidos anteriormente son **científicamente plausibles** y adecuados para poner a prueba procedimientos de manejo.

El script `validate_om.R` puede coordinar:

- comparación de biomasa, captura, reclutamiento, tallas u otras variables con rangos históricos;
- revisión de medias, variabilidad, autocorrelación y extremos;
- reproducción de eventos históricos relevantes;
- **hindcast**: reproducir un periodo histórico conocido;
- **holdout**: evaluar datos o periodos que no se utilizaron para calibrar;
- comprobación de dinámica espacial, ambiental o ecosistémica cuando formen parte del OM;
- identificación de OMs que deben rechazarse, corregirse o pasar al Reference/Robustness Set.

La validación no busca demostrar que un OM sea “la verdad”. Busca evitar que las MPs sean evaluadas contra mundos simulados incompatibles con la evidencia o carentes de los mecanismos relevantes para la decisión.
