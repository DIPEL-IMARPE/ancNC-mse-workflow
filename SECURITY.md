# Seguridad

Este repositorio es público. Nunca suba credenciales, datos personales, datos primarios restringidos, informes confidenciales ni información institucional no autorizada.

Las rutas `local_private/`, `data/raw_private/`, `data/interim/`, `data/processed/` y `outputs/` están protegidas por `.gitignore` según su clase de acceso por defecto. Antes de cada commit revise `git status` y confirme que los archivos agregados están autorizados para publicación.

Si un archivo sensible fue agregado alguna vez al historial de Git, eliminarlo en un commit posterior **no lo retira del historial**. En ese caso debe tratarse como un incidente de seguridad y limpiarse el historial con el procedimiento correspondiente.
