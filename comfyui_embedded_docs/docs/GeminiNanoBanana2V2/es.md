# Nano Banana 2

Este nodo genera o edita imágenes enviando un prompt de texto a la API de Vertex AI de Google mediante los modelos de imagen Gemini. Crea imágenes nuevas a partir de una descripción o modifica imágenes existentes usando imágenes de referencia opcionales.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Selecciona el modelo de imagen Gemini que se utilizará. El modelo elegido determina las opciones de resolución disponibles y las entradas específicas del modelo. | DYNAMIC_COMBO | Sí | `"Nano Banana 2 (Gemini 3.1 Flash Image)"`<br>`"Nano Banana 2 Lite"` |
| `prompt` | Prompt de texto que describe la imagen a generar o las ediciones a aplicar. Incluya las restricciones, estilos o detalles que el modelo debe seguir. No debe estar vacío. (predeterminado: vacío) | STRING | Sí | N/A |
| `seed` | Cuando la semilla se fija a un valor específico, el modelo hace todo lo posible por proporcionar la misma respuesta ante solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso si se usa el mismo valor de semilla. De forma predeterminada, se usa un valor de semilla aleatorio. (predeterminado: 42) | INT | Sí | 0 a 18446744073709551615 |
| `response_modalities` | Determina el formato de la respuesta. IMAGE devuelve solo una imagen; IMAGE+TEXT devuelve una imagen y una respuesta de texto. (predeterminado: IMAGE) Parámetro avanzado. | COMBO | Sí | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `system_prompt` | Instrucciones fundamentales que rigen el comportamiento de una IA. Si se deja vacío, se utiliza un prompt integrado que indica al modelo que siempre produzca una imagen. Parámetro avanzado. | STRING | No | N/A |
| `temperature` | Controla la aleatoriedad en la generación. Cuanto más bajo, más centrado y determinista. (predeterminado: 1.0) Parámetro avanzado. | FLOAT | No | 0.0 a 2.0 (paso 0.01) |
| `top_p` | Umbral de muestreo de núcleo (nucleus sampling). Cuanto más bajo, más enfocado; cuanto más alto, más diverso. (predeterminado: 0.95) Parámetro avanzado. | FLOAT | No | 0.0 a 1.0 (paso 0.01) |

### Entradas de Nano Banana 2 (Gemini 3.1 Flash Image)

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `aspect_ratio` | Si se establece en `'auto'`, coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen 16:9. (predeterminado: auto) | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolución de salida objetivo. | COMBO | Sí | `"1K"`<br>`"2K"`<br>`"4K"` |
| `thinking_level` | Selecciona el nivel de pensamiento utilizado por el modelo. | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` |

### Entradas de Nano Banana 2 Lite

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `aspect_ratio` | Si se establece en `'auto'`, coincide con la relación de aspecto de la imagen de entrada; si no se proporciona ninguna imagen, normalmente se genera una imagen 16:9. (predeterminado: auto) | COMBO | Sí | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"`<br>`"1:4"`<br>`"4:1"`<br>`"8:1"`<br>`"1:8"` |
| `resolution` | Resolución de salida objetivo. | COMBO | Sí | `"1K"` |
| `thinking_level` | Selecciona el nivel de pensamiento utilizado por el modelo. | COMBO | Sí | `"MINIMAL"`<br>`"HIGH"` |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Imagen(es) de referencia opcional(es). Hasta 14 imágenes en total. Ranura ampliable: conecte desde `image_1` hasta `image_14`. | IMAGE | No | 0 a 14 imágenes |
| `files` | Archivo(s) opcional(es) para usar como contexto del modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | No | N/A |

**Nota:** Se puede conectar un máximo de 14 imágenes de referencia a la entrada `images`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La imagen generada o editada. | IMAGE |
| `STRING` | Una descripción de texto o leyenda generada por el modelo. Vacía cuando no se devuelve texto, como cuando `response_modalities` está configurado en `IMAGE`. | STRING |
| `thought_image` | Primera imagen del proceso de pensamiento del modelo. Solo disponible con `thinking_level` HIGH y la modalidad IMAGE+TEXT. | IMAGE |

**Nota:** La salida `STRING` está vacía cuando `response_modalities` se establece en `IMAGE`.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/es.md)

---
**Source fingerprint (SHA-256):** `347d28aeb46aa91f7515a31c385a3e3f805a1861116a21dd2ef6575ab7fd4f3e`
