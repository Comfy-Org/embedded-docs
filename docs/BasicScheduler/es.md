El nodo BasicScheduler está diseñado para calcular una secuencia de valores sigma para modelos de difusión basados en el programador, modelo y parámetros de reducción de ruido proporcionados. Ajusta dinámicamente el número total de pasos según el factor de reducción de ruido para afinar el proceso de difusión.

## Tipos de entrada

| Parámetro  | Comfy dtype | Descripción |
|------------|-------------|-------------|
| `model`    | `MODEL`     | El parámetro model especifica el modelo de difusión para el cual se calcularán los valores sigma. Juega un papel crucial en la determinación de los valores sigma apropiados para el proceso de difusión. |
| `scheduler`| `COMBO[STRING]` | El parámetro scheduler determina el algoritmo de programación que se utilizará para calcular los valores sigma. Influye directamente en la progresión y características del proceso de difusión. |
| `steps`    | `INT`       | El parámetro steps indica el número total de pasos en el proceso de difusión. Afecta la granularidad y duración del proceso. |
| `denoise`  | `FLOAT`     | El parámetro denoise permite ajustar el número efectivo de pasos escalando los pasos totales, permitiendo un control más fino sobre el proceso de difusión. |

## Tipos de salida

| Parámetro | Comfy dtype | Descripción |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | La salida sigmas representa la secuencia calculada de valores sigma para el proceso de difusión, esencial para controlar el nivel de ruido en cada paso. |