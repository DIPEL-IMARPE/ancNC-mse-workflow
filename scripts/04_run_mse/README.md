# 04 - Ejecutar la MSE en ciclo cerrado

> [Volver a `scripts/`](../) · [Diseño del MSE](../../docs/07_mse_scope_design/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta es la etapa en la que se ejecuta la **simulación de ciclo cerrado**. En cada paso temporal se repite la cadena:

**estado verdadero del OM → datos observados con error → evaluación/estimador → procedimiento de manejo → implementación real → nuevo estado del OM**.

La separación entre esos componentes es fundamental. El procedimiento de manejo solo puede utilizar la información que estaría disponible en el sistema real; no debe acceder directamente a la biomasa, reclutamiento u otros estados verdaderos del OM.

El script principal debe:

- leer las configuraciones del experimento, OMs y MPs;
- asignar semillas aleatorias reproducibles;
- ejecutar todas las réplicas y escenarios requeridos;
- aplicar el modelo de observación, estimación e implementación en el orden correcto;
- guardar resultados con un `run_id` único;
- registrar la corrida en `registry/run_registry.csv`.

`run_demo.R` es solamente una **prueba mínima heredada de la plantilla de origen**. No representa una MSE científica ni una especie real y debe reemplazarse por la implementación científica del MSE de anchoveta Norte-Centro.
