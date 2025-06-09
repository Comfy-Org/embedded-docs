
El SDTurboScheduler está diseñado para generar una secuencia de valores sigma para el muestreo de imágenes, ajustando la secuencia según el nivel de reducción de ruido y el número de pasos especificados. Aprovecha las capacidades de muestreo de un modelo específico para producir estos valores sigma, que son cruciales para controlar el proceso de reducción de ruido durante la generación de imágenes.

## Entradas

| Parámetro | Data Type | Descripción |
| --- | --- | --- |
| `model` | `MODEL` | El parámetro model especifica el modelo generativo que se utilizará para la generación de valores sigma. Es crucial para determinar el comportamiento de muestreo específico y las capacidades del programador. |
| `steps` | `INT` | El parámetro steps determina la longitud de la secuencia de sigma a generar, influyendo directamente en la granularidad del proceso de reducción de ruido. |
| `denoise` | `FLOAT` | El parámetro denoise ajusta el punto de inicio de la secuencia de sigma, permitiendo un control más fino sobre el nivel de reducción de ruido aplicado durante la generación de imágenes. |

## Salidas

| Parámetro | Data Type | Descripción |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Una secuencia de valores sigma generada en base al modelo especificado, los pasos y el nivel de reducción de ruido. Estos valores son esenciales para controlar el proceso de reducción de ruido en la generación de imágenes. |
