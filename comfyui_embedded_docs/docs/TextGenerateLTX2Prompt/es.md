# TextGenerateLTX2Prompt

El nodo `TextGenerateLTX2Prompt` es una versión especializada de un nodo de generación de texto. Toma el mensaje de texto del usuario y lo formatea automáticamente con instrucciones de sistema específicas antes de enviarlo a un modelo de lenguaje para su mejora o finalización. El nodo puede operar en dos modos: solo texto o con una referencia de imagen, utilizando diferentes mensajes de sistema para cada caso.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la codificación de texto. | CLIP | Sí |  |
| `mensaje` | La entrada de texto sin procesar del usuario que será mejorada o completada. | STRING | Sí |  |
| `longitud_máxima` | El número máximo de tokens que el modelo de lenguaje puede generar. | INT | Sí |  |
| `modo_de_muestreo` | La estrategia de muestreo utilizada para seleccionar el siguiente token durante la generación de texto. | COMBO | Sí | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `imagen` | Una imagen de entrada opcional. Cuando se proporciona, el nodo utiliza un mensaje de sistema diferente que incluye un marcador de posición para el contexto de la imagen. | IMAGE | No |  |
| `pensando` | Cuando está habilitado, el modelo mostrará su proceso de razonamiento antes de la respuesta final. | BOOLEAN | No |  |
| `use_default_template` | Cuando está habilitado, el nodo utilizará la plantilla de chat predeterminada para el formateo. | BOOLEAN | No |  |
| `video` | Una entrada de video opcional que puede usarse como contexto adicional para la generación. | VIDEO | No |  |
| `audio` | Una entrada de audio opcional que puede usarse como contexto adicional para la generación. | AUDIO | No |  |

**Nota:** El comportamiento del nodo cambia según la presencia de la entrada `image`. Si se proporciona una imagen, el mensaje generado se formateará para una tarea de imagen a video. Si no se proporciona ninguna imagen, el formateo será para una tarea de texto a video.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `texto_generado` | La cadena de texto mejorada o completada generada por el modelo de lenguaje. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/es.md)

---
**Source fingerprint (SHA-256):** `a3daa0a376a53b9c5613238092cc1289d4c358c7c74b12a6e311681de550d1f8`
