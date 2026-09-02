# Configuración de publicación y visibilidad

> [Volver a `config/`](../) · [Política de datos](../../DATA_POLICY.md) · [Mapa completo](../../REPOSITORY_MAP.md)

La configuración principal de visibilidad está en [`publication.yml`](../../publication.yml), en la raíz del repositorio. **Ese es el único archivo autoritativo** para clasificar material como público, interno, derivado-publicable o restringido.

Esta subcarpeta se conserva únicamente para documentación y, si un proyecto real lo necesita, para configuraciones adicionales de construcción de entregas. No debe crearse aquí una segunda copia de las reglas de `publication.yml`, porque dos archivos equivalentes podrían divergir y causar errores.

Consulte también `scripts/07_release/` para preparar entregas versionadas.
