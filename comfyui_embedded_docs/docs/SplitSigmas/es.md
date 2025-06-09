
El nodo SplitSigmas está diseñado para dividir una secuencia de valores sigma en dos partes basándose en un paso especificado. Esta funcionalidad es crucial para operaciones que requieren un manejo o procesamiento diferente de las partes inicial y subsecuente de la secuencia de sigma, permitiendo una manipulación más flexible y dirigida de estos valores.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | El parámetro 'sigmas' representa la secuencia de valores sigma que se va a dividir. Es esencial para determinar el punto de división y las dos secuencias resultantes de valores sigma, impactando la ejecución y los resultados del nodo. |
| `step`    | `INT`       | El parámetro 'step' especifica el índice en el que la secuencia de sigma debe dividirse. Juega un papel crítico en la definición del límite entre las dos secuencias de sigma resultantes, influyendo en la funcionalidad del nodo y las características de la salida. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | El nodo produce dos secuencias de valores sigma, cada una representando una parte de la secuencia original dividida en el paso especificado. Estas salidas son cruciales para operaciones posteriores que requieren un manejo diferenciado de los valores sigma. |
