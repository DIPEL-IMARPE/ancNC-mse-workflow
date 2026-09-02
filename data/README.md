# Datos del proyecto (`data/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta organiza los datos por **nivel de acceso** y por **etapa de procesamiento**. La idea es evitar mezclar archivos originales, productos intermedios y datos listos para el MSE.

| Carpeta | Qué contiene |
|---|---|
| [`examples/`](examples/) | Datos ficticios y pequeños usados únicamente para comprobar que el template funciona. |
| [`public/`](public/) | Datos que pueden redistribuirse públicamente, con su fuente y licencia registradas. |
| [`raw_private/`](raw_private/) | Datos originales restringidos. Git ignora su contenido para evitar subirlo accidentalmente. |
| [`interim/`](interim/) | Productos intermedios reproducibles generados durante limpieza, integración o transformación. |
| [`processed/`](processed/) | Datos limpios, validados y listos para análisis, condicionamiento del OM o simulación. |
| [`metadata/`](metadata/) | Diccionarios de variables, unidades, cobertura temporal/espacial, cambios de protocolo y reglas de control de calidad. |

## Regla básica

Los datos originales restringidos **no deben entrar al historial de Git**, aunque el repositorio sea privado. Registre cada conjunto de datos en [`registry/data_inventory.csv`](../registry/data_inventory.csv) e indique propietario, periodo, resolución, variables, nivel de acceso y uso dentro del MSE.

Consulte también [`DATA_POLICY.md`](../DATA_POLICY.md).
