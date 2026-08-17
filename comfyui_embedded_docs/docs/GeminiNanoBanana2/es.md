# Nano Banana 2

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto que describe la imagen a generar o las ediciones a aplicar. Incluye cualquier restricción, estilo o detalle que el modelo deba seguir. Debe contener al menos un carácter que no sea espacio en blanco. | STRING | Sí | N/A |
| `model` | El modelo Gemini específico que se usará para la generación de imágenes. La única opción disponible corresponde al modelo `gemini-3.1-flash-image-preview`. | COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace su mejor esfuerzo para proporcionar la misma respuesta en solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. Por defecto, se usa un valor de semilla aleatorio. (por defecto: 42) | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | Si se establece en 'auto', coincide con la relación de aspecto de tu imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen con relación de aspecto 16:9. (por defecto: "auto") | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Resolución de salida objetivo. Para 2K/4K se utiliza el escalador nativo de Gemini. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Determina el tipo de contenido que devuelve el modelo: `IMAGE` devuelve solo la imagen, `IMAGE+TEXT` también devuelve el texto de razonamiento del modelo. (avanzado) | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Controla la profundidad del proceso de razonamiento del modelo. | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` |
| `images` | Imagen(es) de referencia opcional(es). Para incluir múltiples imágenes, usa el nodo Batch Images (hasta 14). | IMAGE | No | Hasta 14 imágenes |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento de una IA. (por defecto: instrucciones integradas que requieren que el modelo siempre produzca una imagen) (avanzado) | STRING | No | N/A |

**Nota:** La entrada `images` acepta un máximo de 14 imágenes; proporcionar más genera un error. Cuando se proporcionan más de 10 imágenes de referencia, las primeras 10 se envían como URLs de archivo y las restantes se envían como datos integrados. El `prompt` no debe estar vacío después de eliminar los espacios en blanco. Este nodo está marcado como obsoleto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen principal generada o editada por el modelo. | IMAGE |
| `string` | Cualquier contenido de texto devuelto por el modelo. | STRING |
| `thought_image` | Primera imagen del proceso de pensamiento del modelo. Solo disponible con `thinking_level` HIGH y modalidad `IMAGE+TEXT`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/es.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
