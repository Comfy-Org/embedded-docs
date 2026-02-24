> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/es.md)

El nodo TextGenerateLTX2Prompt es una versión especializada de un nodo de generación de texto. Toma el texto de entrada del usuario y lo formatea automáticamente con instrucciones específicas del sistema antes de enviarlo a un modelo de lenguaje para su mejora o finalización. El nodo puede operar en dos modos: solo texto o con una referencia de imagen, utilizando diferentes instrucciones del sistema para cada caso.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | | El modelo CLIP utilizado para la codificación de texto. |
| `prompt` | STRING | Sí | | La entrada de texto sin procesar del usuario que será mejorada o completada. |
| `max_length` | INT | Sí | | El número máximo de tokens que el modelo de lenguaje puede generar. |
| `sampling_mode` | COMBO | Sí | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` | La estrategia de muestreo utilizada para seleccionar el siguiente token durante la generación de texto. |
| `image` | IMAGE | No | | Una imagen de entrada opcional. Cuando se proporciona, el nodo utiliza una instrucción del sistema diferente que incluye un marcador de posición para el contexto de la imagen. |

**Nota:** El comportamiento del nodo cambia según la presencia de la entrada `image`. Si se proporciona una imagen, el texto generado se formateará para una tarea de imagen a video. Si no se proporciona una imagen, el formato será para una tarea de texto a video.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | STRING | La cadena de texto mejorada o completada generada por el modelo de lenguaje. |