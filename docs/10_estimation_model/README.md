# 10 - Modelo de estimación: reproducir la información usada para decidir

> [Volver a `docs/`](../) · [Especificación mínima](../../models/estimation_model/) · [Configuración](../../config/estimation_model.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

El modelo de estimación representa **cómo el sistema de manejo transforma los datos observados en una estimación o indicador del estado del stock**.

Puede ser:

- una evaluación de stock completa;
- una evaluación simplificada;
- un modelo de producción u otro estimador reducido;
- un índice empírico utilizado directamente por una MP.

## Qué debe reproducirse

- datos que recibe el estimador;
- frecuencia con que se actualiza;
- parámetros fijos y estimados cuando corresponda;
- incertidumbre de la estimación;
- sesgo y patrones retrospectivos relevantes;
- criterios de convergencia;
- qué ocurre cuando la evaluación falla o falta información.

El procedimiento de manejo **nunca debe acceder directamente a la biomasa, reclutamiento u otros estados verdaderos del OM**. Solo puede utilizar la información que estaría disponible en el sistema real después del proceso de observación y estimación.

El procedimiento alternativo usado cuando el assessment falla debe definirse antes de ejecutar la MSE, no improvisarse después de observar los resultados.
