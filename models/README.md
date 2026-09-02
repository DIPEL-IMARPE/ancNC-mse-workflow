# Especificaciones de los componentes del MSE (`models/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta contiene **listas de requisitos científicos mínimos** para cada componente del ciclo de simulación. Su función es evitar que la implementación dependa únicamente de decisiones escondidas dentro del código.

Los archivos `.yml` de esta carpeta no son el modelo ejecutándose; describen **qué debe poder representar cada componente**. Son útiles para revisar el diseño con especialistas antes de programarlo o cambiarlo.

| Carpeta | Qué especifica |
|---|---|
| [`operating_model/`](operating_model/) | Procesos que debe representar el sistema verdadero simulado: población, reclutamiento, crecimiento, mortalidad, pesca y otros procesos justificados. |
| [`observation_model/`](observation_model/) | Qué datos se simulan y qué fuentes de error o sesgo deben poder representarse. |
| [`estimation_model/`](estimation_model/) | Qué información recibe la evaluación/estimador, qué produce y cómo se manejan fallas. |
| [`implementation_model/`](implementation_model/) | Cómo representar diferencias entre la medida recomendada y la realizada. |
| [`management_procedures/`](management_procedures/) | Elementos mínimos de una MP completa: datos de entrada, indicador/estimador, regla, acción, momento de aplicación, restricciones y procedimiento alternativo. |
| [`reference_points/`](reference_points/) | Definiciones de puntos objetivo, disparadores y límites utilizados por la evaluación o el manejo. |

## Por qué separar esto del código

Un ecólogo, evaluador de stock o gestor debería poder revisar la arquitectura científica del MSE sin tener que leer funciones en R, Python o C++. `models/` cumple esa función de especificación; `src/` contiene después la implementación computacional.
