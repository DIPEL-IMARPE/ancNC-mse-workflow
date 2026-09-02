# Datos del MSE de anchoveta Norte-Centro (`data/`)

> **Idioma principal:** español - [English version](README.en.md) - [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta organiza los datos del proyecto por **nivel de acceso** y por **etapa de procesamiento**. El repositorio GitHub es público, pero la mayoría de los datos institucionales necesarios para el MSE pueden no serlo.

| Carpeta | Clase por defecto | Qué contiene | ¿Se versiona? |
|---|---|---|---:|
| [`examples/`](examples/) | public | datos sintéticos pequeños para comprobar el flujo | sí |
| [`public/`](public/) | public | datos reales expresamente autorizados para redistribución | sí |
| [`metadata/`](metadata/) | public | diccionarios, unidades, cobertura, esquemas y QC no sensibles | sí |
| [`raw_private/`](raw_private/) | restricted | datos originales restringidos | no |
| [`interim/`](interim/) | internal | productos intermedios derivados durante limpieza/integración | no |
| [`processed/`](processed/) | internal | insumos limpios listos para análisis o MSE | no, salvo autorización explícita |

## Flujo recomendado

```text
dato original restringido
        |
        v
data/raw_private/       (local, no Git)
        |
        v
procesamiento reproducible
        |
        +--> data/interim/      (local, no Git)
        |
        +--> data/processed/    (local, no Git)
        |
        +--> producto autorizado
                 |
                 v
             data/public/       (Git permitido)
```

## Inventario inicial esperado

Para este MSE se debe evaluar la disponibilidad de, al menos:

- cruceros y observaciones hidroacústicas;
- series de biomasa/abundancia e incertidumbre asociada;
- capturas y desembarques;
- esfuerzo y características de la flota;
- composiciones de talla;
- muestreo biológico y reproductivo;
- monitoreo de juveniles y distribución espacial;
- historia de temporadas, cuotas, cierres y otras medidas de manejo;
- inputs, outputs y diagnósticos de la evaluación de stock;
- información ambiental relevante para hipótesis del OM o escenarios de robustez.

La inclusión en esta lista **no determina que el dato sea público ni que deba entrar al OM**. Cada fuente se evaluará individualmente.

Registre todo conjunto de datos en [`registry/data_inventory.csv`](../registry/data_inventory.csv), incluso si su contenido es privado.
