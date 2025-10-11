> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/es.md)

Este nodo permite a los usuarios interactuar con los modelos de IA Gemini de Google para generar respuestas de texto. Puedes proporcionar múltiples tipos de entradas, incluyendo texto, imágenes, audio, video y archivos como contexto para que el modelo genere respuestas más relevantes y significativas. El nodo maneja automáticamente toda la comunicación con la API y el análisis de las respuestas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Entradas de texto para el modelo, utilizadas para generar una respuesta. Puedes incluir instrucciones detalladas, preguntas o contexto para el modelo. Por defecto: cadena vacía. |
| `model` | COMBO | Sí | `gemini-2.0-flash-exp`<br>`gemini-2.0-flash-thinking-exp`<br>`gemini-2.5-pro-exp`<br>`gemini-2.0-flash`<br>`gemini-2.0-flash-thinking`<br>`gemini-2.5-pro`<br>`gemini-2.0-flash-lite`<br>`gemini-1.5-flash`<br>`gemini-1.5-flash-8b`<br>`gemini-1.5-pro`<br>`gemini-1.0-pro` | El modelo Gemini que se utilizará para generar las respuestas. Por defecto: gemini-2.5-pro. |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Cuando la semilla se fija a un valor específico, el modelo hace un esfuerzo por proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se utiliza el mismo valor de semilla. Por defecto, se utiliza un valor de semilla aleatorio. Por defecto: 42. |
| `images` | IMAGE | No | - | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puedes usar el nodo Batch Images. Por defecto: Ninguno. |
| `audio` | AUDIO | No | - | Audio opcional para usar como contexto para el modelo. Por defecto: Ninguno. |
| `video` | VIDEO | No | - | Video opcional para usar como contexto para el modelo. Por defecto: Ninguno. |
| `files` | GEMINI_INPUT_FILES | No | - | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. Por defecto: Ninguno. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `STRING` | STRING | La respuesta de texto generada por el modelo Gemini. |