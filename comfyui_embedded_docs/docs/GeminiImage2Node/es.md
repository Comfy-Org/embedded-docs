# Nano Banana Pro (Google Gemini Image)

El nodo GeminiImage2Node genera o edita imágenes utilizando el modelo Gemini de Google Vertex AI. Usted proporciona un mensaje de texto y, opcionalmente, imágenes o archivos de referencia; el nodo los envía a la API y devuelve la imagen generada, además de una respuesta de texto cuando se solicita.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluya cualquier restricción, estilo o detalle que el modelo deba seguir. El mensaje debe contener al menos un carácter después de eliminar los espacios en blanco. | STRING | Sí | N/A |
| `model` | El modelo Gemini específico que se usará para la generación. La opción «Nano Banana 2 (Gemini 3.1 Flash Image)» se asigna internamente al modelo `gemini-3.1-flash-image`, y «gemini-3-pro-image-preview» se asigna a `gemini-3-pro-image`. | COMBO | Sí | `"gemini-3-pro-image-preview"`<br>`"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace su mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso si se usa el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. Valor predeterminado: 42. | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | Si se establece en 'auto', coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, generalmente se genera un cuadrado 16:9. Valor predeterminado: 'auto'. | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolución de salida deseada. Para 2K/4K se utiliza el escalador nativo de Gemini. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Elija 'IMAGE' para salida solo de imagen, o 'IMAGE+TEXT' para devolver tanto la imagen generada como una respuesta de texto. | COMBO | Sí | `"IMAGE+TEXT"`<br>`"IMAGE"` |
| `images` | Imagen o imágenes de referencia opcionales. Para incluir múltiples imágenes, use el nodo Batch Images (hasta 14). | IMAGE | No | N/A |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento de una IA. Valor predeterminado: un mensaje de sistema predefinido para la generación de imágenes. | STRING | No | N/A |

**Restricciones:**

* La entrada `images` admite un máximo de 14 imágenes. Si se proporcionan más, se genera un error.
* Cuando se proporcionan más de 10 imágenes, las primeras 10 se cargan como referencias URL y las imágenes restantes se envían en línea en la solicitud.
* La entrada `files` debe estar conectada a un nodo que genere el tipo de datos `GEMINI_INPUT_FILES`.
* Cuando `response_modalities` se establece en «IMAGE», solo se devuelve la imagen y la salida de texto está vacía.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen generada o editada por el modelo Gemini. | IMAGE |
| `string` | La respuesta de texto del modelo. Esta salida estará vacía si `response_modalities` se establece en «IMAGE». | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage2Node/es.md)

---
**Source fingerprint (SHA-256):** `02293dad786d4b441da3174fa76f6c5847f122d294bd7e1f765ffd72420034a4`
