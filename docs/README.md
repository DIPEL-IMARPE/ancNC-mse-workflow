# Documentación científica del MSE (`docs/`)

> **Idioma principal:** español · [English version](README.en.md) · [Mapa completo](../REPOSITORY_MAP.md)

Esta carpeta contiene la **explicación científica e institucional** del proyecto. Aquí se documenta qué se está modelando, por qué se eligieron determinados supuestos y cómo funciona el sistema de manejo. No debería utilizarse para guardar resultados generados ni para introducir parámetros sin justificación.

Las subcarpetas están numeradas para sugerir un orden de trabajo. Una MSE real es iterativa: varias etapas se revisan a medida que aparecen nueva evidencia, diagnósticos o decisiones de manejo.

| Etapa | Carpeta | Pregunta principal |
|---:|---|---|
| 00 | [`00_getting_started/`](00_getting_started/) | ¿Cómo se incorpora una persona nueva al proyecto? |
| 01 | [`01_governance_objectives/`](01_governance_objectives/) | ¿Qué queremos lograr con el manejo y qué nivel de riesgo aceptamos? |
| 02 | [`02_stock_ecology/`](02_stock_ecology/) | ¿Cómo funciona biológica y ecológicamente el stock? |
| 03 | [`03_fishery/`](03_fishery/) | ¿Cómo opera la pesquería y cómo responde la flota? |
| 04 | [`04_management_system/`](04_management_system/) | ¿Cómo se toman e implementan actualmente las decisiones de manejo? |
| 05 | [`05_monitoring_data/`](05_monitoring_data/) | ¿Qué se observa, cómo se muestrea y con qué errores? |
| 06 | [`06_stock_assessment/`](06_stock_assessment/) | ¿Cómo se evalúa el stock y qué incertidumbres tiene la evaluación? |
| 07 | [`07_mse_scope_design/`](07_mse_scope_design/) | ¿Qué pregunta responderá la MSE y qué complejidad necesita? |
| 08 | [`08_operating_model/`](08_operating_model/) | ¿Qué modelos plausibles representan el sistema verdadero simulado? |
| 09 | [`09_observation_model/`](09_observation_model/) | ¿Cómo se simulan los datos imperfectos que observaría el sistema real? |
| 10 | [`10_estimation_model/`](10_estimation_model/) | ¿Qué evaluación o indicador recibe el procedimiento de manejo? |
| 11 | [`11_management_procedures/`](11_management_procedures/) | ¿Qué procedimientos de manejo se compararán? |
| 12 | [`12_implementation_model/`](12_implementation_model/) | ¿Qué diferencias existen entre la recomendación y la acción realizada? |
| 13 | [`13_performance_metrics/`](13_performance_metrics/) | ¿Cómo mediremos conservación, captura, estabilidad y otros objetivos? |
| 14 | [`14_uncertainty_scenarios/`](14_uncertainty_scenarios/) | ¿Qué incertidumbres principales y pruebas de robustez se evaluarán? |
| 15 | [`15_experimental_design/`](15_experimental_design/) | ¿Cuántas simulaciones y qué diseño experimental necesitamos? |
| 16 | [`16_conditioning_validation/`](16_conditioning_validation/) | ¿Los modelos operativos producen dinámicas compatibles con la evidencia? |
| 17 | [`17_tuning_selection/`](17_tuning_selection/) | ¿Cómo se ajustan y comparan las MPs sin sobreajustarlas? |
| 18 | [`18_ecosystem_climate/`](18_ecosystem_climate/) | ¿El clima o las interacciones ecosistémicas pueden cambiar la decisión? |
| 19 | [`19_economics_social/`](19_economics_social/) | ¿Qué objetivos económicos o sociales deben incluirse? |
| 20 | [`20_exceptional_circumstances/`](20_exceptional_circumstances/) | ¿Qué hacemos si ocurre algo fuera del dominio probado por la MSE? |
| 21 | [`21_adoption_monitoring_review/`](21_adoption_monitoring_review/) | ¿Cómo se vigila y revisa una MP después de adoptarla? |
| 22 | [`22_reporting_communication/`](22_reporting_communication/) | ¿Cómo comunicamos métodos, riesgos y compromisos entre objetivos? |
| 23 | [`23_quality_assurance/`](23_quality_assurance/) | ¿Cómo aseguramos calidad, reproducibilidad y revisión independiente? |

**Regla práctica:** antes de modificar el código de un componente, su justificación científica debería poder encontrarse en la carpeta `docs/` correspondiente.
