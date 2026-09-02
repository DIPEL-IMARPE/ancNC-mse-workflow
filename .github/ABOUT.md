# Carpeta `.github`

Esta carpeta contiene archivos que GitHub interpreta automáticamente para gobernanza y automatización del repositorio.

## Qué contiene

| Elemento | Función |
|---|---|
| `ISSUE_TEMPLATE/` | Plantillas para registrar decisiones científicas, incidencias y cambios. |
| `workflows/` | GitHub Actions para ejecutar controles automáticos del repositorio. |
| `pull_request_template.md` | Checklist que aparece al crear un Pull Request. |

## Por qué este archivo se llama `ABOUT.md` y no `README.md`

GitHub puede dar prioridad a un `README.md` situado dentro de `.github/` al decidir qué documento mostrar como portada del repositorio. Para que la portada sea siempre el `README.md` de la raíz —la presentación del MSE—, esta carpeta se documenta mediante `ABOUT.md`.

## Regla

No crear `.github/README.md` ni `.github/README.en.md`. La documentación bilingüe de esta carpeta debe mantenerse como `ABOUT.md` y `ABOUT.en.md`.
