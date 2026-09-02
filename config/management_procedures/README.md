# Configuración de procedimientos de manejo

> [Volver a `config/`](../) · [Documentación de MPs](../../docs/11_management_procedures/) · [Mapa completo](../../REPOSITORY_MAP.md)

Aquí se declaran las **MPs candidatas y los valores de sus parámetros** para una corrida determinada.

`mp_candidates.yml` incluye familias de ejemplo, pero ninguna debe asumirse automáticamente como adecuada para un caso real. Primero debe reconstruirse el procedimiento vigente (*status quo*) y luego definir qué alternativas responden a los objetivos de manejo.

Para cada MP el proyecto debe especificar claramente:

- qué datos observa;
- qué indicador o evaluación utiliza;
- qué regla de decisión aplica;
- qué acción produce;
- cuándo se toma la decisión;
- qué pisos, techos o restricciones de cambio existen;
- qué ocurre si faltan datos o falla la evaluación.

Los parámetros que se ajustan durante el **tuning** deben estar identificados por separado de aquellos fijados por regulación, biología o decisión de manejo. La justificación científica pertenece en `docs/11_management_procedures/`; este archivo solo contiene la configuración concreta que se ejecutará.
