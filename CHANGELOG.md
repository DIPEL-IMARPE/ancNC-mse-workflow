# Historial de cambios

## 0.1.0 - 2026-09-02

### Inicialización del caso

- Creación de `ancNC-mse-workflow` a partir de `.template-fisheries-mse` v1.0.3.
- Definición del caso para la anchoveta peruana (*Engraulis ringens*), stock Norte-Centro.
- Institución científica principal: IMARPE; unidad científica: DIPEL.
- Autoridad de manejo: PRODUCE.
- Se mantienen como `TBD` las decisiones aún no sustentadas sobre dominio exacto, estructura del OM, escala temporal, estructura espacial, modelo de estimación y procedimientos de manejo candidatos.

### Protección de datos

- El proyecto se configura como repositorio público con separación explícita entre `public`, `derived_public`, `internal` y `restricted`.
- `data/raw_private/` y `local_private/` se clasifican como restringidos.
- `data/interim/`, `data/processed/` y `outputs/` se clasifican como internos por defecto y se excluyen de Git.
- Se amplió la documentación de política de datos y fuentes restringidas.
