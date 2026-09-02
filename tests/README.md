# Comprobaciones automáticas (`tests/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta contiene pruebas automáticas para detectar errores antes de confiar en los resultados del MSE. No todas las pruebas son informáticas: algunas verifican reglas científicas básicas.

| Carpeta | Qué comprueba |
|---|---|
| [`unit/`](unit/) | Que una función individual produzca el resultado esperado para casos simples y conocidos. |
| [`scientific/`](scientific/) | Que se respeten reglas científicas: biomasa no negativa, proporciones entre 0 y 1, unidades coherentes, selectividad válida, etc. |
| [`integration/`](integration/) | Que los componentes se conecten correctamente: OM → observación → estimación → MP → implementación → OM. |
| [`regression/`](regression/) | Que cambios de código no modifiquen resultados previamente aceptados sin que el equipo lo detecte. |

## Por qué son importantes en un MSE

Una simulación puede ejecutarse sin mostrar mensajes de error y aun así ser científicamente incorrecta. Por eso deben comprobarse tanto el funcionamiento del software como propiedades biológicas, pesqueras y estadísticas del sistema.

Una versión utilizada para asesoramiento debería pasar los tests relevantes y dejar constancia de ello en `certification/`.
