# Nano Banana Pro (Google Gemini Image)

Nano Banana Pro (Google Gemini Image) genera o edita imágenes utilizando los modelos de imagen Gemini de Google Vertex AI. Envía un prompt de texto junto con imágenes o archivos de referencia opcionales a la API de Gemini, y devuelve la imagen generada junto con una respuesta de texto opcional.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. Valor por defecto: cadena vacía. | STRING | Sí | N/A |
| `model` | El modelo de imagen Gemini a utilizar. La opción «Nano Banana 2 (Gemini 3.1 Flash Image)» se envía a la API como `gemini-3.1-flash-image`; «gemini-3-pro-image-preview» se envía como `gemini-3-pro-image`. | COMBO | Sí | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace todo lo posible por proporcionar la misma respuesta en solicitudes repetidas. La salida determinista no está garantizada. Cambiar el modelo u otros ajustes de parámetros puede provocar variaciones en la respuesta incluso con el mismo valor de semilla. Valor por defecto: 42. | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | La relación de aspecto deseada de la imagen de salida. Si se establece en «auto», coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen 16:9. Valor por defecto: «auto». | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolución de salida objetivo. Para 2K/4K se utiliza el escalador nativo de Gemini. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Seleccione «IMAGE» para salida solo de imagen, o «IMAGE+TEXT» para devolver tanto la imagen generada como una respuesta de texto. | COMBO | Sí | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Imagen(es) de referencia opcionales utilizadas como contexto visual. Para incluir varias imágenes, use el nodo Batch Images (hasta 14). | IMAGE | No | N/A |
| `files` | Archivo(s) opcionales para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. Valor por defecto: un prompt de sistema predefinido que indica al modelo que siempre genere una imagen. | STRING | No | N/A |

**Restricciones:**

* El `prompt` no debe quedar vacío después de eliminar los espacios en blanco al principio y al final; de lo contrario, se produce un error.
* La entrada `images` acepta un máximo de 14 imágenes. Si se proporcionan más de 14, se genera un error.
* La entrada `files` debe estar conectada a un nodo que emita el tipo de datos `GEMINI_INPUT_FILES`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | La imagen generada o editada por el modelo Gemini. | IMAGE |
| `string` | La respuesta de texto del modelo. Esta salida está vacía cuando `response_modalities` está configurado en «IMAGE». | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/es.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
