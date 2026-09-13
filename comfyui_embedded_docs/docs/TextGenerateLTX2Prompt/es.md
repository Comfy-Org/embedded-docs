# TextGenerateLTX2Prompt

El nodo TextGenerateLTX2Prompt expande un prompt breve del usuario a una descripción audiovisual detallada, adecuada para generar video con la serie LTX-2 de modelos de video. Agrega automáticamente instrucciones de sistema específicas de la tarea, envía el prompt formateado a un modelo de lenguaje y devuelve el texto mejorado. Cuando se proporciona una imagen de referencia opcional, el nodo cambia al modo imagen a video y expande el prompt a partir del contenido de esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la codificación de texto. El nodo comprueba el nombre del tokenizador del modelo para seleccionar las instrucciones correspondientes: los modelos basados en Gemma 4 usan el formato LTX-2.4, mientras que los demás modelos usan el formato LTX-2 (Gemma 3). | CLIP | Sí |  |
| `prompt` | La entrada de texto sin procesar que describe la escena o el concepto que se expandirá en un prompt detallado para generación de video. | STRING | Sí |  |
| `max_length` | El número máximo de tokens que el modelo de lenguaje puede generar. | INT | Sí |  |
| `sampling_mode` | La estrategia de muestreo utilizada para seleccionar el siguiente token durante la generación de texto. | COMBO | Sí | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `image` | Una imagen de entrada opcional utilizada como primer fotograma del video. Cuando se proporciona, el nodo cambia al modo imagen a video y usa un prompt de sistema que expande el prompt del usuario a partir del contenido de la imagen. | IMAGE | No |  |
| `thinking` | Cuando está habilitado, se indica al modelo que razone antes de responder. Cualquier bloque de razonamiento se elimina de la salida devuelta (predeterminado: False). | BOOLEAN | No |  |
| `use_default_template` | Cuando está habilitado, el nodo usa la plantilla de chat predeterminada para el formateo (predeterminado: True). | BOOLEAN | No |  |
| `video` | Una entrada de video opcional que se puede usar como contexto adicional para la generación. | VIDEO | No |  |
| `audio` | Una entrada de audio opcional que se puede usar como contexto adicional para la generación. | AUDIO | No |  |

**Nota:** El comportamiento del nodo cambia según sus entradas:

- Si se proporciona una `image`, el prompt generado se formatea para una tarea de imagen a video usando un prompt de sistema que describe cómo expandir el prompt a partir del contenido de la imagen. Si no se proporciona una imagen, el formato es para una tarea de texto a video usando un prompt de sistema que expande el prompt en una descripción detallada para generación de video.
- Si el nombre del tokenizador de CLIP contiene "gemma4", el nodo usa los prompts de sistema de LTX-2.4 y el formato de chat de Gemma 4. De lo contrario, usa los prompts de sistema y el formato de chat de LTX-2 (Gemma 3).
- Cuando `thinking` está habilitado con un modelo Gemma 4, el modelo se abre en su canal de razonamiento; cuando está deshabilitado, el modelo se abre directamente en el canal de respuesta final. Para los modelos que no son Gemma 4, `thinking` se pasa al paso de generación subyacente.
- Si el modelo de lenguaje no produce texto utilizable después de eliminar los bloques de razonamiento, el nodo devuelve el `prompt` original en su lugar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El prompt mejorado para generación de video producido por el modelo de lenguaje, con cualquier bloque de razonamiento eliminado. Si el resultado está vacío, se devuelve el prompt original del usuario. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/es.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
