# 01 — Preparar los datos

> [Volver a `scripts/`](../) · [Datos](../../data/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa transforma los datos disponibles en **insumos limpios, documentados y reproducibles** para el MSE.

El script principal es `prepare_inputs.R`. Debe coordinar, según el proyecto:

- lectura de archivos originales o fuentes externas;
- estandarización de fechas, unidades, identificadores y coordenadas;
- controles de calidad y detección de valores imposibles;
- integración entre fuentes;
- construcción de datos intermedios y procesados;
- registro de cambios de protocolo o cobertura;
- escritura de productos en `data/interim/` o `data/processed/`.

Las reglas de limpieza o funciones reutilizables no deberían duplicarse dentro del script; deben vivir preferentemente en `src/io/` u otra carpeta apropiada de `src/`.

**Salida esperada:** datos listos para análisis y un inventario actualizado en `registry/data_inventory.csv`.
