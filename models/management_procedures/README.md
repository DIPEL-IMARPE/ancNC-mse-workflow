# Especificación de los procedimientos de manejo

> [Volver a `models/`](../) · [Documentación científica](../../docs/11_management_procedures/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define los elementos que debe tener un **procedimiento de manejo (MP) completo** antes de ser evaluado en la MSE.

`specification.yml` exige documentar como mínimo:

1. **datos de entrada:** qué información observa la MP;
2. **indicador o estimador:** cómo se resume esa información;
3. **regla de decisión:** cómo se transforma el indicador en una decisión;
4. **acción de manejo:** cuota, esfuerzo, cierre, restricción espacial u otra medida;
5. **momento de aplicación:** cuándo y con qué frecuencia se decide;
6. **restricciones:** límites de cambio, pisos, techos u otras condiciones;
7. **procedimiento alternativo:** qué hacer si faltan datos, falla la evaluación o no puede calcularse la regla.

Una HCR puede ser una parte central de la MP, pero no necesariamente representa por sí sola todo el procedimiento de manejo.
