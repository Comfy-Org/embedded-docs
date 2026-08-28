# OpenAI GPT Image 2

Este nodo genera imágenes mediante la API GPT Image de OpenAI. Admite varios modelos (`gpt-image-2`, `gpt-image-1.5` y `gpt-image-1`), permite proporcionar imágenes de referencia para edición y puede usar una máscara para especificar qué partes de una imagen modificar.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de imagen GPT de OpenAI que se usará. Al seleccionar un modelo, se muestran parámetros adicionales específicos de ese modelo. | DYNAMIC_COMBO | Sí | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Indicación de texto para GPT Image (por defecto: `""`). | STRING | Sí | No aplica |
| `n` | Cuántas imágenes generar (por defecto: `1`). | INT | Sí | 1 a 8 |
| `semilla` | Semilla para reproducibilidad (por defecto: `0`). Aún no implementado en el backend. | INT | Sí | 0 a 2147483647 |

### Entradas de gpt-image-2

Estas entradas aparecen cuando `model` se establece en `gpt-image-2`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tamaño` | Tamaño de la imagen. Seleccione «Custom» para usar el ancho y la altura personalizados (por defecto: `"auto"`). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `ancho_personalizado` | Se usa solo cuando `model.size` es «Custom». Debe ser múltiplo de 16 (por defecto: `1024`). | INT | No | 1024 a 3840 |
| `altura_personalizada` | Se usa solo cuando `model.size` es «Custom». Debe ser múltiplo de 16 (por defecto: `1024`). | INT | No | 1024 a 3840 |
| `fondo` | Devuelve la imagen con o sin fondo (por defecto: `"auto"`). | COMBO | Sí | `"auto"`<br>`"opaque"` |
| `calidad` | Calidad de la imagen; afecta el costo y el tiempo de generación (por defecto: `"low"`). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imágenes de referencia opcionales para la edición de imágenes. Hasta 16 imágenes. Consulte Entradas de referencia para más detalles. | IMAGE | No | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | No aplica |

### Entradas de gpt-image-1.5 y gpt-image-1

Estas entradas aparecen cuando `model` se establece en `gpt-image-1.5` o `gpt-image-1`. Ambos modelos comparten el mismo conjunto de parámetros.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `tamaño` | Tamaño de la imagen (por defecto: `"auto"`). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fondo` | Devuelve la imagen con o sin fondo (por defecto: `"auto"`). | COMBO | Sí | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `calidad` | Calidad de la imagen; afecta el costo y el tiempo de generación (por defecto: `"low"`). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imágenes de referencia opcionales para la edición de imágenes. Hasta 16 imágenes. Consulte Entradas de referencia para más detalles. | IMAGE | No | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | No aplica |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.images` | Entrada ampliable: conecte de 1 a N elementos (p. ej. `image_1`...`image_16`); hasta 16 imágenes de referencia para todos los modelos. | IMAGE | No | 1 a 16 |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | No aplica |

**Restricciones y limitaciones de los parámetros:**

- Cuando `model.size` es «Custom» (solo gpt-image-2), tanto `model.custom_width` como `model.custom_height` deben ser múltiplos de 16, el lado más largo no debe superar 3840, la relación de aspecto no debe superar 3:1 y el número total de píxeles debe estar entre 655,360 y 8,294,400.
- `model.mask` requiere exactamente una imagen de referencia en `model.images`: no puede usarse sin una imagen ni con más de una imagen.
- Cuando se usa `model.mask`, sus dimensiones deben coincidir con las de la imagen de referencia.
- Cuando se proporciona `model.images`, el nodo funciona en modo de edición de imágenes; sin `model.images`, genera imágenes únicamente a partir de la indicación.
- Las imágenes de referencia se reducen de escala antes de enviarse a la API.
- `seed` actualmente no está implementado en el backend.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen o imágenes generadas. Todas las imágenes devueltas se apilan en un solo lote; si sus dimensiones difieren, se redimensionan para que coincidan con la primera imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
