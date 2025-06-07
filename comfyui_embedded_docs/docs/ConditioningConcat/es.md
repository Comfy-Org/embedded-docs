El nodo ConditioningConcat está diseñado para concatenar vectores de condicionamiento, fusionando específicamente el vector 'conditioning_from' en el vector 'conditioning_to'. Esta operación es fundamental en escenarios donde la información de condicionamiento de dos fuentes necesita combinarse en una representación única y unificada.

## Entradas

| Parámetro             | Comfy dtype        | Descripción |
|-----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Representa el conjunto principal de vectores de condicionamiento al que se concatenarán los vectores 'conditioning_from'. Sirve como base para el proceso de concatenación. |
| `conditioning_from`   | `CONDITIONING`     | Consiste en vectores de condicionamiento que se concatenarán a los vectores 'conditioning_to'. Este parámetro permite integrar información de condicionamiento adicional en el conjunto existente. |

## Salidas

| Parámetro            | Comfy dtype        | Descripción |
|----------------------|--------------------|-------------|
| `conditioning`       | `CONDITIONING`     | La salida es un conjunto unificado de vectores de condicionamiento, resultante de la concatenación de los vectores 'conditioning_from' en los vectores 'conditioning_to'. |
