# Diseño de las simulaciones (`experiments/`)

> [Volver a `config/`](../) · [Diseño experimental](../../docs/15_experimental_design/) · [Mapa completo](../../REPOSITORY_MAP.md)

Esta carpeta define **cuántas simulaciones se harán, durante cuánto tiempo y bajo qué combinaciones de escenarios y MPs**.

`base_experiment.yml` puede especificar:

- horizonte de proyección;
- número de réplicas de Monte Carlo;
- bloque de semillas aleatorias;
- Reference Set y Robustness Set utilizados;
- MPs que se compararán;
- uso de **common random numbers**.

### ¿Qué son los *common random numbers*?

Significa comparar distintas MPs utilizando, cuando sea posible, las mismas realizaciones aleatorias de reclutamiento, observación y otros procesos. Así, una diferencia entre MPs se debe en mayor medida a la estrategia de manejo y menos al azar de haber enfrentado trayectorias distintas.

El número de réplicas no debe fijarse por costumbre. Debe comprobarse que el error Monte Carlo sea suficientemente pequeño para las métricas y diferencias que sustentan la decisión.

También pueden definirse aquí experimentos de **valor de información**, por ejemplo comparar el desempeño con uno versus dos cruceros, diferente precisión del monitoreo o distintas frecuencias de evaluación.
