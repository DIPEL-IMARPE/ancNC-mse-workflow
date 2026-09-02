# 20 — Circunstancias excepcionales

> [Volver a `docs/`](../) · [Registro de circunstancias excepcionales](../../registry/exceptional_circumstances_registry.csv) · [Mapa completo](../../REPOSITORY_MAP.md)

Una MP se evalúa dentro de un conjunto de condiciones simuladas. En la práctica puede aparecer un evento, dato o estado del stock que quede **fuera del dominio para el cual la estrategia fue probada**. El protocolo de circunstancias excepcionales define de antemano cómo detectar y manejar esa situación.

## El protocolo debería especificar

- **indicador de detección:** qué variable se vigilará;
- **umbral o condición de activación:** cuándo se considera que existe una circunstancia excepcional;
- **método de evaluación:** quién revisa la evidencia y con qué información;
- **autoridad:** quién puede tomar una decisión extraordinaria;
- **respuesta temporal:** qué medida puede aplicarse mientras se investiga;
- **posible suspensión o modificación de la MP:** bajo qué condiciones se permite apartarse temporalmente del procedimiento;
- **revisión científica:** cuándo se requiere recalibrar el OM o repetir la MSE;
- **criterio de retorno:** cuándo vuelve a aplicarse la MP normal.

## Ejemplos

- reclutamiento muy por debajo de todo lo simulado;
- índice de abundancia extremadamente fuera del rango histórico;
- cambio abrupto de distribución espacial;
- pérdida prolongada del programa de monitoreo;
- evaluación de stock que falla repetidamente;
- nueva tecnología o cambio de flota que altera la selectividad;
- cambio ambiental persistente no representado por los OMs.

El objetivo no es introducir discreción ilimitada, sino **preacordar cómo reconocer que la MSE dejó de representar adecuadamente la situación real**.
