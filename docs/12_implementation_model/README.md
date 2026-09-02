# 12 — Modelo de implementación: de la recomendación a lo que realmente ocurre

> [Volver a `docs/`](../) · [Especificación mínima](../../models/implementation_model/) · [Configuración](../../config/implementation_model.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

Una MSE no debería asumir que toda medida recomendada se aplica de manera instantánea y perfecta. El **modelo de implementación** representa la diferencia entre la decisión formal y el resultado real en la pesquería.

## Procesos que pueden ser relevantes

- **cuota no capturada:** la pesquería termina por debajo de la cuota autorizada;
- **sobrepaso de cuota:** la captura supera la recomendación o límite previsto;
- **cumplimiento imperfecto:** parte de la flota no responde exactamente a la medida;
- **retrasos:** existe tiempo entre detección, decisión y aplicación de una medida;
- **cierres tardíos o incompletos:** una medida espacial/temporal no se implementa inmediatamente;
- **redistribución de flota:** el esfuerzo se desplaza hacia otras áreas, temporadas o componentes del stock;
- **cambios de duración de temporada:** la acción de manejo modifica cuándo y cuánto tiempo opera la pesquería.

Estos procesos deben incorporarse cuando puedan modificar el desempeño relativo de las MPs. Si se asume implementación perfecta, esa decisión debe quedar explícitamente justificada.
