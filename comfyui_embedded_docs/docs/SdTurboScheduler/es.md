> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/es.md)

SDTurboScheduler está diseñado para generar una secuencia de valores sigma para el muestreo de imágenes, ajustando la secuencia según el nivel de eliminación de ruido y el número de pasos especificados. Aprovecha las capacidades de muestreo de un modelo específico para producir estos valores sigma, que son cruciales para controlar el proceso de eliminación de ruido durante la generación de imágenes.

## Entradas

| Parámetro | Tipo de datos | Descripción |
| --- | --- | --- |
| `modelo` | `MODEL` | El parámetro model especifica el modelo generativo que se utilizará para la generación de valores sigma. Es crucial para determinar el comportamiento de muestreo específico y las capacidades del programador. |
| `pasos` | `INT` | El parámetro steps determina la longitud de la secuencia sigma que se generará, influyendo directamente en la granularidad del proceso de eliminación de ruido. |
| `reducir_ruido` | `FLOAT` | El parámetro denoise ajusta el punto de inicio de la secuencia sigma, permitiendo un control más preciso sobre el nivel de eliminación de ruido aplicado durante la generación de imágenes. |

## Salidas

| Parámetro | Tipo de datos | Descripción |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Una secuencia de valores sigma generados según el modelo, los pasos y el nivel de eliminación de ruido especificados. Estos valores son esenciales para controlar el proceso de eliminación de ruido en la generación de imágenes. |