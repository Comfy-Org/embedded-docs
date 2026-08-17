# Recraft V4 Texto a Imagen

Este nodo genera imágenes a partir de descripciones de texto utilizando los modelos de IA Recraft V4 y V4.1. Envía el prompt y la configuración de generación al servicio de generación de imágenes de Recraft y devuelve la imagen o imágenes resultantes. Puedes elegir el modelo, el tamaño de la imagen y el número de imágenes a generar.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo a utilizar para la generación. La selección de un modelo determina las opciones de `size` disponibles. | DYNAMIC_COMBO | Sí | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para la generación de la imagen. Máximo 10.000 caracteres. | STRING | Sí | 1 a 10000 caracteres |
| `negative_prompt` | Esta entrada se ignora: Recraft V4 y V4.1 no admiten prompt negativo. | STRING | Sí | N/A |
| `n` | Número de imágenes a generar (por defecto: 1). | INT | Sí | 1 a 6 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | CUSTOM | No | N/A |

### Entradas de recraftv4_1, recraftv4_1_utility y recraftv4

Compartidas por los modelos `recraftv4_1`, `recraftv4_1_utility` y `recraftv4`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size` | El tamaño de la imagen generada (por defecto: 1024x1024). | COMBO | Sí | Múltiples opciones disponibles (tamaños estándar de Recraft V4) |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro y recraftv4_pro

Compartidas por los modelos `recraftv4_1_pro`, `recraftv4_1_utility_pro` y `recraftv4_pro`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size` | El tamaño de la imagen generada (por defecto: 2048x2048). | COMBO | Sí | Múltiples opciones disponibles (tamaños Pro de Recraft V4) |

**Notas:**

- La entrada `size` aparece cuando se selecciona un modelo, y sus opciones disponibles dependen del modelo: los modelos estándar (`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`) comparten un conjunto de tamaños, mientras que los modelos Pro (`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`) comparten otro diferente.
- La entrada `negative_prompt` se muestra en la interfaz, pero no se envía al modelo; Recraft V4 y V4.1 no admiten prompts negativos.
- El valor de `seed` solo determina si el nodo se vuelve a ejecutar cuando cambia el valor; los resultados reales de la imagen son no deterministas independientemente de la semilla.
- Si utilizas un ID de estilo de la Infinite Style Library a través de la entrada `recraft_controls`, asegúrate de que no sea un estilo de arte vectorial, ya que podría devolver datos SVG en lugar de una imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La imagen o el lote de imágenes generado. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
