# Política de datos - `ancNC-mse-workflow`

Este repositorio GitHub es público. Por tanto, **solo debe versionarse información cuya publicación o redistribución esté autorizada**. La existencia de un conjunto de datos puede documentarse públicamente sin publicar sus observaciones.

## Clases de información

### `public`

Información que puede versionarse y redistribuirse después de comprobar su fuente y permiso de uso. Ejemplos posibles: normas públicas, literatura, indicadores publicados y datos abiertos.

### `derived_public`

Producto agregado o derivado de información no pública cuya difusión ha sido expresamente autorizada. La autorización debe quedar registrada en la documentación o en el inventario correspondiente.

### `internal`

Información para IMARPE, consultores o colaboradores autorizados que **no debe entrar a este repositorio público**. Incluye por defecto productos intermedios, datos procesados internos y resultados de trabajo no aprobados para difusión.

### `restricted`

Información que no debe entrar al historial de Git bajo ninguna circunstancia: datos primarios restringidos, credenciales, información personal, documentos confidenciales o archivos sujetos a restricciones institucionales o contractuales.

## Organización local de los datos

| Ruta | Clase por defecto | Git | Uso |
|---|---|---:|---|
| `data/examples/` | public | sí | datos sintéticos para probar el flujo |
| `data/public/` | public | sí | datos reales autorizados para redistribución |
| `data/metadata/` | public | sí | diccionarios, esquemas y metadatos no sensibles |
| `data/raw_private/` | restricted | no | datos originales restringidos |
| `data/interim/` | internal | no | productos intermedios |
| `data/processed/` | internal | no | insumos analíticos derivados no autorizados para publicación |
| `outputs/` | internal | no | resultados de corridas y análisis, salvo release aprobado |
| `local_private/` | restricted | no | documentos o archivos locales sensibles |

## Datos esperados para el MSE de anchoveta Norte-Centro

El proyecto podrá requerir, sujeto a disponibilidad y autorización, información de cruceros hidroacústicos, capturas/desembarques, esfuerzo, composiciones de talla, muestreo biológico, monitoreo de juveniles, medidas de manejo, fechas de temporadas, cuotas, cierres, evaluación de stock y variables ambientales. **La mención de estas fuentes no implica que sean públicas.**

Cada conjunto debe registrarse en `registry/data_inventory.csv` con propietario, cobertura, variables, clase de acceso y uso dentro del MSE.

## Regla para fuentes documentales restringidas

Si un informe, base o documento es restringido, registre su existencia en `registry/source_registry.csv` y su ubicación autorizada, pero no copie el archivo a GitHub. Puede almacenarse localmente bajo `local_private/references/` u otra infraestructura institucional aprobada.

## Antes de hacer `git add`

Compruebe siempre:

```bash
git status
git check-ignore data/raw_private/archivo.ext
git check-ignore data/processed/archivo.ext
```

La protección de `.gitignore` reduce errores accidentales, pero **no sustituye la responsabilidad de verificar permisos de publicación**.
