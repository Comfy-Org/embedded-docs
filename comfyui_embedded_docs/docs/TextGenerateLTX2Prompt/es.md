# TextGenerateLTX2Prompt

El nodo `TextGenerateLTX2Prompt` es una versión especializada de un nodo de generación de texto. Toma el prompt de texto del usuario y lo formatea automáticamente con instrucciones de sistema específicas de LTX2 antes de enviarlo a un modelo de lenguaje para mejorarlo o completarlo. El nodo puede funcionar en modo solo texto o en modo con referencia de imagen, y adapta automáticamente su formato al modelo CLIP conectado, utilizando el formato de prompt LTX 2.4 para modelos Gemma 4 y el formato LTX 2.0 para modelos Gemma 3.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la codificación de texto. El modelo determina el formato del prompt: los modelos Gemma 4 usan el formato LTX 2.4 y los modelos Gemma 3 usan el formato LTX 2.0. | CLIP | Sí |  |
| `prompt` | La entrada de texto sin procesar del usuario que será mejorada o completada. | STRING | Sí |  |
| `max_length` | El número máximo de tokens que el modelo de lenguaje puede generar. | INT | Sí |  |
| `sampling_mode` | La estrategia de muestreo utilizada para seleccionar el siguiente token durante la generación de texto. | COMBO | Sí | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Una imagen de entrada opcional. Cuando se proporciona, el nodo utiliza un prompt de sistema diferente que incluye contexto de imagen para la generación de imagen a video. | IMAGE | No |  |
| `thinking` | Cuando está habilitado, el modelo mostrará su proceso de razonamiento antes de la respuesta final. El bloque de razonamiento se elimina del resultado final. | BOOLEAN | No |  |
| `use_default_template` | Cuando está habilitado, el nodo utilizará la plantilla de chat predeterminada para el formateo. | BOOLEAN | No |  |
| `video` | Una entrada de video opcional que puede usarse como contexto adicional para la generación. | VIDEO | No |  |
| `audio` | Una entrada de audio opcional que puede usarse como contexto adicional para la generación. | AUDIO | No |  |

**Notas:** El comportamiento del nodo cambia según la presencia de la entrada `image`. Si se proporciona una imagen, el prompt se formatea para una tarea de imagen a video utilizando un prompt de sistema que expande el prompt basándose en el contenido de la imagen. Si no se proporciona ninguna imagen, el formato corresponde a una tarea de texto a video utilizando un prompt de sistema que expande el prompt hasta convertirlo en una descripción detallada de generación de video.

El modelo `clip` conectado también afecta al formateo: cuando el tokenizador CLIP es un modelo Gemma 4, el nodo utiliza el formato de chat y los prompts de sistema de LTX 2.4; de lo contrario, utiliza el formato de chat de Gemma 3 / LTX 2.0. Después de la generación, cualquier bloque de razonamiento (por ejemplo, `<think>...</think>`) se elimina de la salida y, si el texto resultante está vacío, se devuelve el `prompt` original.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | La cadena de texto mejorada o completada generada por el modelo de lenguaje, con cualquier contenido de razonamiento eliminado. Si el modelo no produce texto, se devuelve el `prompt` original. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/es.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
