# 15 - Diseño del experimento de simulación

> [Volver a `docs/`](../) · [Configuración de experimentos](../../config/experiments/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta etapa define **cómo se ejecutarán las simulaciones para que las comparaciones entre MPs sean estadísticamente estables y reproducibles**.

## Elementos principales

- horizonte de proyección;
- periodo de estabilización si es necesario;
- número de réplicas de Monte Carlo;
- semillas aleatorias y forma de registrarlas;
- escenarios/OMs y MPs que se cruzarán;
- uso de las mismas realizaciones aleatorias para comparar MPs cuando sea apropiado;
- precisión Monte Carlo requerida para las métricas clave;
- diseño factorial o muestreo de escenarios cuando el número de combinaciones sea grande;
- experimentos de valor de información.

### ¿Cuántas réplicas son suficientes?

No existe un número universal. Debe aumentarse el número de simulaciones hasta que el error Monte Carlo sea pequeño respecto de las diferencias de desempeño que sustentan la decisión. Una comparación inestable por falta de réplicas puede producir rankings que cambian solo por azar.

### Valor de información

La MSE también puede comparar sistemas de monitoreo: por ejemplo, uno versus dos cruceros, diferente frecuencia de muestreo, precisión de índices o cobertura espacial. Así puede estimarse cuánto mejora el manejo al invertir en determinada información.
