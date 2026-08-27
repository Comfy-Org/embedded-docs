# Google Gemini

Este nodo permite a los usuarios interactuar con los modelos de IA Gemini de Google para generar respuestas de texto. Puede proporcionar múltiples tipos de entradas, incluyendo texto, imágenes, audio, video y archivos como contexto para que el modelo genere respuestas más relevantes y significativas. El nodo maneja automáticamente toda la comunicación con la API y el procesamiento de las respuestas.

**Nota:** Este nodo está marcado como obsoleto en el código fuente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Entradas de texto para el modelo, utilizadas para generar una respuesta. Puede incluir instrucciones detalladas, preguntas o contexto para el modelo. Por defecto: cadena vacía. | STRING | Sí | - |
| `modelo` | El modelo Gemini a utilizar para generar respuestas. Por defecto: gemini-3-1-pro. | COMBO | Sí | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `semilla` | Cuando la semilla se fija a un valor específico, el modelo hace un mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. La salida determinista no está garantizada. Además, cambiar el modelo o los ajustes de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. Por defecto, se usa un valor de semilla aleatorio. Por defecto: 42. | INT | Sí | 0 a 18446744073709551615 |
| `imágenes` | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puede usar el nodo Batch Images. Por defecto: Ninguna. | IMAGE | No | - |
| `audio` | Audio opcional para usar como contexto para el modelo. Por defecto: Ninguno. | AUDIO | No | - |
| `video` | Video opcional para usar como contexto para el modelo. Por defecto: Ninguno. | VIDEO | No | - |
| `archivos` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. Por defecto: Ninguno. | GEMINI_INPUT_FILES | No | - |
| `system_prompt` | Instrucciones fundamentales que dictan el comportamiento de una IA. Por defecto: cadena vacía. Este es un parámetro avanzado. | STRING | No | - |

Todas las imágenes conectadas se utilizan como contexto. Cuando se proporcionan más de 10 imágenes, las primeras 10 se cargan como referencias de archivo y las imágenes restantes se envían en línea a la API.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `STRING` | La respuesta de texto generada por el modelo Gemini. Si el modelo no produce texto, el nodo devuelve "Empty response from Gemini model...". | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/es.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
