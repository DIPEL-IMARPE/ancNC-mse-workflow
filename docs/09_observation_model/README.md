# 09 — Modelo de observación: simular datos imperfectos

> [Volver a `docs/`](../) · [Especificación mínima](../../models/observation_model/) · [Configuración](../../config/observation_model.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

En la naturaleza no observamos directamente la biomasa, el reclutamiento o la mortalidad por pesca verdaderos. Observamos **datos producidos por métodos de muestreo y monitoreo imperfectos**. El modelo de observación reproduce ese proceso dentro de la MSE.

## Ejemplos de incertidumbre observacional

- error y posible sesgo en índices de abundancia;
- disponibilidad y capturabilidad de un crucero acústico;
- cobertura espacial incompleta;
- error de reporte en captura o esfuerzo;
- muestreo limitado de tallas o edades;
- tamaño efectivo de muestra de composiciones;
- error en proporción de juveniles u otras variables biológicas;
- ausencia de un crucero o pérdida de datos;
- cambios históricos en diseño de muestreo o protocolo.

### Precisión y sesgo no son lo mismo

- **Precisión** describe cuánto varía una observación alrededor de su valor esperado.
- **Sesgo** significa que, en promedio, la observación se desplaza sistemáticamente respecto al valor que pretende medir.

Una MP que funciona solo cuando los datos son perfectos probablemente no será robusta en la práctica. Por eso el modelo de observación debe reflejar los errores que realmente puede enfrentar el sistema de manejo.
