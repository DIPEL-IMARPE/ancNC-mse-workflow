# 07 — Definir el alcance y diseño del MSE

> [Volver a `docs/`](../) · [Perfil de la especie](../../species_profile.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa convierte la pregunta de manejo en un **experimento de simulación bien definido**. Antes de construir modelos complejos, el equipo debe decidir qué necesita representar para responder la pregunta.

## Decisiones principales

- **pregunta de decisión:** qué alternativas o incertidumbres debe evaluar la MSE;
- **horizonte de proyección:** cuántos años o temporadas se simularán;
- **periodo de estabilización (*warm-up*):** si el modelo necesita un periodo previo para generar estados iniciales coherentes;
- **paso temporal:** anual, estacional, mensual, semanal u otro;
- **frecuencia de evaluación y decisión:** cada cuánto se actualiza la información y se aplica la MP;
- **estructura biológica:** edad, talla, ambas o una aproximación más simple;
- **estructura espacial:** no espacial, regiones, áreas dinámicas u otra representación;
- **ambiente, ecosistema y economía:** incluirlos solo si pueden modificar la conclusión de manejo.

## Principio de parsimonia

Una MSE más compleja no es automáticamente mejor. Debe incluir los procesos que puedan cambiar el desempeño relativo de las MPs y justificar aquellos que se omiten. La complejidad debe responder a objetivos, mecanismos ecológicos, incertidumbres y disponibilidad de información, no solo a la existencia de datos.

Las decisiones de alto nivel se reflejan después en `species_profile.yml` y en los archivos de `config/`.
