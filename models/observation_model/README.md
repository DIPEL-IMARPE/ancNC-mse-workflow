# Especificación del modelo de observación

> [Volver a `models/`](../) · [Documentación científica](../../docs/09_observation_model/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define qué debe poder representar el modelo que transforma el **estado verdadero simulado** en los **datos imperfectos que observaría el sistema real**.

`specification.yml` recuerda los componentes mínimos: observación de capturas, índices de abundancia y muestreo de composiciones. También señala procesos que deben evaluarse cuando sean relevantes, como disponibilidad acústica, cobertura espacial, muestreo biológico o cruceros faltantes.

La precisión, sesgo y demás valores concretos se especifican en `config/observation_model.yml`; la justificación científica se documenta en `docs/09_observation_model/`.
