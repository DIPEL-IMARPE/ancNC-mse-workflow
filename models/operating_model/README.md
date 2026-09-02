# Especificación del modelo operativo

> [Volver a `models/`](../) · [Documentación científica del OM](../../docs/08_operating_model/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define **qué procesos debe poder representar el modelo operativo**, independientemente del lenguaje o motor utilizado para implementarlo.

El archivo `specification.yml` funciona como una lista mínima de requisitos. Por defecto exige dinámica poblacional, reclutamiento, crecimiento, mortalidad, madurez, selectividad, pesca y variación estocástica. También recuerda que espacialidad, ambiente, ecosistema y economía deben incluirse cuando sean relevantes para la decisión o justificarse si se excluyen.

Esta especificación no sustituye la documentación científica en `docs/08_operating_model/` ni los valores concretos de `config/operating_model.yml`.
