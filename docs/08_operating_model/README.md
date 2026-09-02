# 08 — Modelo operativo: representar sistemas verdaderos plausibles

> [Volver a `docs/`](../) · [Especificación mínima](../../models/operating_model/) · [Configuración](../../config/operating_model.yml) · [Mapa completo](../../REPOSITORY_MAP.md)

El **modelo operativo (OM)** representa el “sistema verdadero” dentro de la simulación. No afirma conocer la verdad real del stock; describe una o varias hipótesis plausibles sobre cómo funcionan la población y la pesquería.

## Componentes que normalmente deben evaluarse

- dinámica de abundancia o números por edad/talla;
- reclutamiento y su variabilidad;
- crecimiento y relación talla–peso;
- mortalidad natural;
- madurez y reproducción;
- selectividad y mortalidad por pesca;
- flotas o componentes pesqueros cuando sean relevantes;
- variación aleatoria de procesos.

Según la pregunta también pueden ser materiales:

- movimiento y distribución espacial;
- disponibilidad al crucero o a la pesquería;
- ambiente y cambios de productividad;
- depredación o función de pez forraje;
- respuesta económica o de la flota.

## Incertidumbre paramétrica y estructural

La incertidumbre **paramétrica** se refiere a no conocer exactamente el valor de un parámetro. La incertidumbre **estructural** se refiere a no saber cuál mecanismo o forma de modelo es correcta. Una MSE robusta puede necesitar varios OMs para representar ambas.

No seleccione un único OM solo porque tenga el mejor ajuste estadístico si existen hipótesis alternativas científicamente plausibles que podrían cambiar el desempeño relativo de las MPs.

Después de construir los OMs deben calibrarse y validarse antes de utilizarlos para seleccionar una estrategia de manejo.
