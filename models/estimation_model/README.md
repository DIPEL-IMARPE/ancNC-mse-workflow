# Especificación del modelo de estimación

> [Volver a `models/`](../) · [Documentación científica](../../docs/10_estimation_model/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define los requisitos del **método que transforma datos observados en la información usada por el procedimiento de manejo**. Puede ser una evaluación de stock completa, un modelo reducido o un indicador empírico.

`specification.yml` exige que el proyecto documente como mínimo:

- qué evaluación o indicador se utiliza;
- con qué frecuencia se actualiza;
- cómo se representa su incertidumbre;
- qué ocurre si la evaluación no converge, faltan datos o el indicador no puede calcularse.

La MP nunca debe recibir directamente los estados verdaderos del modelo operativo. Debe trabajar con la misma clase de información imperfecta que estaría disponible en el sistema real.
