# Nano Banana 2

Este nodo genera o edita imágenes enviando un prompt de texto a la API de Vertex AI de Google a través de los modelos Gemini 3.1 Flash Image. Crea nuevas imágenes a partir de una descripción o modifica imágenes existentes utilizando imágenes de referencia opcionales.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto que describe la imagen a generar o las ediciones a aplicar. Incluya cualquier restricción, estilo o detalle que el modelo deba seguir. No debe estar vacío. | STRING | Sí | N/A |
| `model` | Selecciona el modelo Gemini que se usará para la generación de imágenes. Este parámetro incluye subparámetros adicionales para resolución, relación de aspecto, nivel de razonamiento y entradas de referencia. | COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace todo lo posible por proporcionar la misma respuesta para solicitudes repetidas. La salida determinista no está garantizada. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso si se usa el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. (valor predeterminado: 42) | INT | Sí | 0 a 18446744073709551615 |
| `response_modalities` | Determina el formato de la respuesta. IMAGE devuelve solo una imagen; IMAGE+TEXT devuelve una imagen y una respuesta de texto. (valor predeterminado: IMAGE) Parámetro avanzado. | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento de una IA. El valor predeterminado es un prompt integrado que le indica al modelo que siempre produzca una imagen. Parámetro avanzado. | STRING | No | N/A |
| `temperature` | Controla la aleatoriedad en la generación. Un valor más bajo produce resultados más enfocados o deterministas. (valor predeterminado: 1.0) Parámetro avanzado. | FLOAT | No | 0.0 a 2.0 (paso 0.01) |
| `top_p` | Umbral de muestreo por núcleo (nucleus sampling). Un valor más bajo es más enfocado; uno más alto, más diverso. (valor predeterminado: 0.95) Parámetro avanzado. | FLOAT | No | 0.0 a 1.0 (paso 0.01) |

### Entradas de Nano Banana 2 (Gemini 3.1 Flash Image)

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `aspect_ratio` | Si se establece en 'auto', coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen en formato 16:9. (valor predeterminado: auto) | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolución de salida objetivo. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Selecciona el nivel de razonamiento utilizado por el modelo. | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` |

### Entradas de Nano Banana 2 Lite

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `aspect_ratio` | Si se establece en 'auto', coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen en formato 16:9. (valor predeterminado: auto) | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolución de salida objetivo. | COMBO | Sí | `"1K"` |
| `thinking_level` | Selecciona el nivel de razonamiento utilizado por el modelo. | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `images` | Imágenes de referencia opcionales. Hasta 14 imágenes en total. Ranura ampliable: conecte `image_1` a `image_14`. | IMAGE | No | 0 a 14 imágenes |
| `files` | Archivos opcionales para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |

**Nota:** Se puede conectar un máximo de 14 imágenes de referencia a la entrada `images`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | La imagen generada o editada. | IMAGE |
| `STRING` | Una descripción de texto o leyenda generada por el modelo. | STRING |
| `thought_image` | Primera imagen del proceso de razonamiento del modelo. Solo está disponible con `thinking_level` HIGH y con la modalidad IMAGE+TEXT. | IMAGE |

**Nota:** La salida `STRING` está vacía cuando `response_modalities` se establece en `IMAGE`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/es.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
