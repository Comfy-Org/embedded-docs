> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/es.md)

El nodo Flux2Scheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de eliminación de ruido, específicamente adaptado para el modelo Flux. Calcula un programa basado en el número de pasos de eliminación de ruido y las dimensiones de la imagen objetivo, lo que influye en la progresión de la eliminación de ruido durante la generación de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Sí | 1 a 4096 | El número de pasos de eliminación de ruido a realizar. Un valor más alto generalmente conduce a resultados más detallados pero tarda más en procesarse (por defecto: 20). |
| `width` | INT | Sí | 16 a 16384 | El ancho de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (por defecto: 1024). |
| `height` | INT | Sí | 16 a 16384 | La altura de la imagen a generar, en píxeles. Este valor influye en el cálculo del programa de ruido (por defecto: 1024). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Una secuencia de valores de nivel de ruido (sigmas) que definen el programa de eliminación de ruido para el muestreador. |
