> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/es.md)

El nodo GeminiImage2Node genera o edita imágenes utilizando el modelo Gemini de Vertex AI de Google. Envía un mensaje de texto y, opcionalmente, imágenes o archivos de referencia a la API y devuelve la imagen generada y/o una descripción de texto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. |
| `model` | COMBO | Sí | `"gemini-3-pro-image-preview"` | El modelo específico de Gemini a utilizar para la generación. |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Cuando se fija a un valor específico, el modelo hace un esfuerzo por proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Cambiar el modelo u otras configuraciones puede causar variaciones incluso con la misma semilla. Por defecto: 42. |
| `aspect_ratio` | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | La relación de aspecto deseada para la imagen de salida. Si se establece en 'auto', coincide con la relación de aspecto de tu imagen de entrada; si no se proporciona ninguna imagen, generalmente se genera un cuadrado 16:9. Por defecto: "auto". |
| `resolution` | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` | Resolución objetivo de salida. Para 2K/4K se utiliza el escalador nativo de Gemini. |
| `response_modalities` | COMBO | Sí | `"IMAGE+TEXT"`<br>`"IMAGE"` | Elige 'IMAGE' para una salida solo de imagen, o 'IMAGE+TEXT' para devolver tanto la imagen generada como una respuesta de texto. |
| `images` | IMAGE | No | N/A | Imagen(es) de referencia opcional(es). Para incluir múltiples imágenes, utiliza el nodo Batch Images (hasta 14). |
| `files` | CUSTOM | No | N/A | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas desde el nodo Gemini Generate Content Input Files. |
| `system_prompt` | STRING | No | N/A | Instrucciones fundamentales que dictan el comportamiento de una IA. Por defecto: Un mensaje de sistema predefinido para generación de imágenes. |

**Restricciones:**

* La entrada `images` admite un máximo de 14 imágenes. Si se proporcionan más, se generará un error.
* La entrada `files` debe estar conectada a un nodo que emita el tipo de dato `GEMINI_INPUT_FILES`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen generada o editada por el modelo Gemini. |
| `string` | STRING | La respuesta de texto del modelo. Esta salida estará vacía si `response_modalities` está configurado como "IMAGE". |
