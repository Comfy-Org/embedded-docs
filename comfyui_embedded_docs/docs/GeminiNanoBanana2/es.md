# Nano Banana 2

El nodo GeminiNanoBanana2 genera o edita imágenes utilizando el modelo Gemini de Vertex AI de Google. Envía un prompt de texto, junto con imágenes o archivos de referencia opcionales, a la API y devuelve la imagen generada y cualquier texto adjunto. Este nodo está marcado como obsoleto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto que describe la imagen a generar o las ediciones que se deben aplicar. Incluya cualquier restricción, estilo o detalle que el modelo deba seguir. No puede estar vacío. (predeterminado: vacío) | STRING | Sí | N/A |
| `model` | El modelo Gemini específico que se utilizará para la generación de imágenes. | COMBO | Sí | "Nano Banana 2 (Gemini 3.1 Flash Image)" |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace todo lo posible por proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso si se usa el mismo valor de semilla. Por defecto, se utiliza un valor de semilla aleatorio. (predeterminado: 42) | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | Si se establece en 'auto', coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen en 16:9. (predeterminado: "auto") | COMBO | Sí | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"9:16"<br>"16:9"<br>"21:9" |
| `resolution` | Resolución de salida deseada. Para 2K/4K se utiliza el escalador nativo de Gemini. | COMBO | Sí | "1K"<br>"2K"<br>"4K" |
| `response_modalities` | Determina el tipo de contenido que devuelve el modelo: "IMAGE" devuelve solo una imagen, "IMAGE+TEXT" también devuelve texto. (avanzado) | COMBO | Sí | "IMAGE"<br>"IMAGE+TEXT" |
| `thinking_level` | Controla la profundidad del proceso de razonamiento del modelo. | COMBO | Sí | "MINIMAL"<br>"HIGH" |
| `images` | Imágenes de referencia opcionales. Para incluir varias imágenes, use el nodo Batch Images (hasta 14). | IMAGE | No | 1 a 14 imágenes |
| `files` | Archivos opcionales para usar como contexto del modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | CUSTOM | No | N/A |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento de una IA. (predeterminado: un prompt predefinido que le indica al modelo que siempre produzca una imagen) (avanzado) | STRING | No | N/A |

**Nota:** La entrada `images` admite un máximo de 14 imágenes. Si se proporcionan más, el nodo generará un error. La entrada `prompt` no debe estar vacía ni contener solo espacios en blanco.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen principal generada o editada por el modelo. | IMAGE |
| `string` | Cualquier contenido de texto devuelto por el modelo. | STRING |
| `thought_image` | Primera imagen del proceso de razonamiento del modelo. Solo disponible con thinking_level HIGH y modalidad IMAGE+TEXT. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/es.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
