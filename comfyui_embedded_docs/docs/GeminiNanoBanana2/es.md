> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/es.md)

El nodo GeminiNanoBanana2 genera o edita imágenes utilizando el modelo Gemini de Google Vertex AI. Funciona enviando un mensaje de texto, junto con imágenes de referencia o archivos opcionales, a la API y devuelve la imagen generada y cualquier texto adjunto.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/D | Mensaje de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. |
| `model` | COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | El modelo Gemini específico a utilizar para la generación de imágenes. |
| `seed` | INT | Sí | 0 a 18446744073709551615 | Cuando la semilla se fija a un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. Por defecto, se utiliza un valor de semilla aleatorio. (predeterminado: 42) |
| `aspect_ratio` | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` | Si se establece en 'auto', coincide con la relación de aspecto de tu imagen de entrada; si no se proporciona ninguna imagen, generalmente se genera un cuadrado 16:9. (predeterminado: "auto") |
| `resolution` | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` | Resolución de salida objetivo. Para 2K/4K se utiliza el escalador nativo de Gemini. |
| `response_modalities` | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` | Determina el tipo de contenido que devolverá el modelo. (avanzado) |
| `thinking_level` | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` | Controla la profundidad del proceso de razonamiento del modelo. |
| `images` | IMAGE | No | N/D | Imagen(es) de referencia opcional(es). Para incluir múltiples imágenes, usa el nodo Agrupar Imágenes (hasta 14). |
| `files` | CUSTOM | No | N/D | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Archivos de Entrada de Contenido Generado de Gemini. |
| `system_prompt` | STRING | No | N/D | Instrucciones fundamentales que dictan el comportamiento de una IA. (avanzado) |

**Nota:** La entrada `images` admite un máximo de 14 imágenes. Si se proporcionan más, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen principal generada o editada por el modelo. |
| `thought_image` | STRING | Cualquier contenido de texto devuelto por el modelo. |
| `thought_image` | IMAGE | Primera imagen del proceso de pensamiento del modelo. Solo disponible con `thinking_level` HIGH y modalidad IMAGE+TEXT. |

---
**Source fingerprint (SHA-256):** `bd53363da73ff0db66a872fc04f1af8ce4dfee1191ca01bd813701b5ad5e4f17`
