# 14 - Incertidumbres y escenarios

> [Volver a `docs/`](../) - [Reference Set](../../config/reference_set/) - [Robustness Set](../../config/robustness_set/) - [Mapa completo](../../REPOSITORY_MAP.md)

Una MSE es útil precisamente porque el sistema real es incierto. Esta etapa identifica **qué no sabemos con suficiente certeza y qué hipótesis alternativas podrían cambiar una decisión de manejo**.

## Dos conjuntos con funciones diferentes

### Reference Set
Conjunto principal de modelos operativos considerados suficientemente plausibles para representar la incertidumbre central. Suele utilizarse para la evaluación principal y el ajuste de parámetros de las MPs.

### Robustness Set
Escenarios adicionales que someten las MPs a condiciones difíciles, menos probables o alternativas. Su función principal es comprobar resistencia, no ampliar indiscriminadamente el conjunto utilizado para ajustar la MP.

## Ejemplos de incertidumbres que pueden ser relevantes

- magnitud y variabilidad del reclutamiento;
- cambios de régimen o fallas persistentes de reclutamiento;
- mortalidad natural, crecimiento o madurez variables;
- selectividad variable entre flotas, temporadas o periodos históricos;
- sesgo o variación en índices de abundancia;
- campañas, cruceros o periodos de monitoreo faltantes;
- cambios espaciales de distribución;
- errores o retrasos de implementación;
- cambios ambientales o no estacionariedad climática;
- debilitamiento o ruptura de relaciones ambiente-reclutamiento;
- cambios de productividad o interacciones ecosistémicas;
- cambios tecnológicos, económicos o de comportamiento de la flota.

No todas estas incertidumbres deben incluirse en todos los proyectos. Deben seleccionarse según la biología de la especie, la pesquería, los datos disponibles y la pregunta de manejo.

Cada incertidumbre debe registrarse en `registry/uncertainty_registry.csv` con su mecanismo, evidencia y tratamiento. Un escenario debe existir porque representa una pregunta científica o de manejo, no solamente para aumentar el número de sensibilidades.
