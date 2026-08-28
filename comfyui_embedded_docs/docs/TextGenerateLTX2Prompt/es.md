# TextGenerateLTX2Prompt

El nodo TextGenerateLTX2Prompt expande una breve indicación del usuario en una descripción audiovisual detallada, adecuada para generar videos con la serie de modelos de video LTX-2. Agrega automáticamente instrucciones del sistema específicas para la tarea, envía la indicación formateada a un modelo de lenguaje y devuelve el texto mejorado. Cuando se proporciona una imagen de referencia opcional, el nodo cambia al modo de imagen a video y expande la indicación a partir del contenido de esa imagen.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP utilizado para la codificación de texto. El nodo verifica el nombre del tokenizador del modelo para seleccionar las instrucciones correspondientes: los modelos basados en Gemma 4 usan el formato LTX-2.4, mientras que otros modelos usan el formato LTX-2 (Gemma 3). | CLIP | Sí |  |
| `mensaje` | La entrada de texto sin procesar que describe la escena o el concepto que se expandirá para generar una indicación de video detallada. | STRING | Sí |  |
| `longitud_máxima` | El número máximo de tokens que se le permite generar al modelo de lenguaje. | INT | Sí |  |
| `modo_de_muestreo` | La estrategia de muestreo utilizada para seleccionar el siguiente token durante la generación de texto. | COMBO | Sí | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` |
| `imagen` | Una imagen de entrada opcional utilizada como primer fotograma del video. Cuando se proporciona, el nodo cambia al modo de imagen a video y utiliza un mensaje del sistema que expande la indicación del usuario basándose en el contenido de la imagen. | IMAGE | No |  |
| `pensando` | Cuando está habilitado, se le indica al modelo que razone antes de responder. Cualquier bloque de razonamiento se elimina de la salida devuelta (predeterminado: False). | BOOLEAN | No |  |
| `use_default_template` | Cuando está habilitado, el nodo utiliza la plantilla de chat predeterminada para el formateo (predeterminado: True). | BOOLEAN | No |  |
| `video` | Una entrada de video opcional que se puede utilizar como contexto adicional para la generación. | VIDEO | No |  |
| `audio` | Una entrada de audio opcional que se puede utilizar como contexto adicional para la generación. | AUDIO | No |  |

**Nota:** El comportamiento del nodo cambia según sus entradas:

- Si se proporciona una `image`, la indicación generada se formatea para una tarea de imagen a video utilizando un mensaje del sistema que describe cómo expandir la indicación basándose en el contenido de la imagen. Si no se proporciona ninguna imagen, el formateo es para una tarea de texto a video utilizando un mensaje del sistema que expande la indicación en una descripción detallada para la generación de video.
- Si el nombre del tokenizador del CLIP contiene "gemma4", el nodo utiliza los mensajes del sistema LTX-2.4 y el formato de chat Gemma 4. De lo contrario, utiliza los mensajes del sistema LTX-2 (Gemma 3) y su formato de chat.
- Si el modelo de lenguaje no produce texto utilizable después de eliminar los bloques de razonamiento, el nodo devuelve la `prompt` original en su lugar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `texto_generado` | La indicación mejorada para generación de video producida por el modelo de lenguaje, con cualquier bloque de razonamiento eliminado. Si el resultado está vacío, se devuelve la indicación original del usuario. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/es.md)

---
**Source fingerprint (SHA-256):** `8f524ea60a247217dde8a1edaf7a689e253ae05acc9eb52ad47b91e879dba1df`
