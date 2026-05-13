> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmas/es.md)

El nodo SplitSigmas está diseñado para dividir una secuencia de valores sigma en dos partes basándose en un paso especificado. Esta funcionalidad es crucial para operaciones que requieren un manejo o procesamiento diferente de las partes inicial y posterior de la secuencia sigma, permitiendo una manipulación más flexible y dirigida de estos valores.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | El parámetro 'sigmas' representa la secuencia de valores sigma que se va a dividir. Es esencial para determinar el punto de división y las dos secuencias resultantes de valores sigma, afectando la ejecución y los resultados del nodo. |
| `paso`    | `INT`       | El parámetro 'step' especifica el índice en el cual se debe dividir la secuencia sigma. Desempeña un papel crítico en la definición del límite entre las dos secuencias sigma resultantes, influyendo en la funcionalidad del nodo y las características de la salida. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `sigmas_bajos`  | `SIGMAS`    | El nodo genera dos secuencias de valores sigma, cada una representando una parte de la secuencia original dividida en el paso especificado. Estas salidas son cruciales para operaciones posteriores que requieren un manejo diferenciado de los valores sigma. |