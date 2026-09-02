# Especificación del modelo de implementación

> [Volver a `models/`](../) · [Documentación científica](../../docs/12_implementation_model/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define cómo representar la diferencia entre una **medida recomendada** y lo que **realmente ocurre en la pesquería**.

`specification.yml` exige distinguir la acción recomendada, la acción realizada y el error de implementación. Según el sistema también puede ser necesario representar:

- cumplimiento imperfecto;
- retrasos entre decisión y aplicación;
- cuota no capturada o sobrepasada;
- respuesta de la flota a cierres o cambios de cuota;
- redistribución espacial del esfuerzo.

Este componente evita asumir que una cuota, cierre o restricción se implementa de forma instantánea y perfecta. Los valores concretos se declaran en `config/implementation_model.yml` y su fundamento debe documentarse en `docs/12_implementation_model/`.
