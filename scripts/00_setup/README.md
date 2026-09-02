# 00 - Preparar y comprobar el repositorio

> [Volver a `scripts/`](../) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta contiene herramientas de mantenimiento del repositorio. **No ejecuta el MSE científico.** Sirve para comprobar que la estructura esté completa y que la documentación técnica acompañe a los archivos.

| Archivo | Qué hace |
|---|---|
| `repo_check.py` | Comprueba que existan los archivos y README mínimos esperados. |
| `refresh_manifest.py` | Actualiza `registry/file_manifest.csv`, el inventario técnico de archivos. |
| `build_tree.py` | Genera `TREE.txt`, una representación técnica del árbol de carpetas. |

Para navegar por el proyecto use [`REPOSITORY_MAP.md`](../../REPOSITORY_MAP.md); `TREE.txt` está pensado principalmente como inventario técnico.
