# OpenAI GPT Image 2

Este nodo genera imágenes mediante la API de OpenAI GPT Image. Admite varios modelos GPT Image, imágenes de referencia opcionales para edición y una máscara opcional para inpainting. Cuando se proporcionan imágenes de referencia, el nodo envía una solicitud de edición a la API; de lo contrario, envía una solicitud de generación simple.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo OpenAI GPT Image a utilizar. Al seleccionar un modelo, se revelan parámetros adicionales específicos de dicho modelo. | DYNAMIC_COMBO | Sí | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt de texto para GPT Image (por defecto: `""`). | STRING | Sí | N/A |
| `n` | Cuántas imágenes generar (por defecto: 1). | INT | Sí | 1 a 8 |
| `seed` | Semilla para reproducibilidad (por defecto: 0). Aún no implementada en el backend. | INT | Sí | 0 a 2147483647 |

### Entradas de gpt-image-2

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.size` | Tamaño de la imagen. Seleccione "Custom" para usar el ancho y alto personalizados (por defecto: "auto"). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (por defecto: 1024). | INT | No | 1024 a 3840 |
| `model.custom_height` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (por defecto: 1024). | INT | No | 1024 a 3840 |
| `model.background` | Devuelve la imagen con o sin fondo (por defecto: "auto"). | COMBO | Sí | `"auto"`<br>`"opaque"` |
| `model.quality` | Calidad de imagen, afecta el costo y el tiempo de generación (por defecto: "low"). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas de gpt-image-1.5 y gpt-image-1

Estos dos modelos comparten el mismo conjunto de parámetros específicos del modelo.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.size` | Tamaño de imagen (por defecto: "auto"). | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Devuelve la imagen con o sin fondo (por defecto: "auto"). | COMBO | Sí | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Calidad de imagen, afecta el costo y el tiempo de generación (por defecto: "low"). | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas de referencia

Estas entradas están disponibles para todos los modelos.

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.images` | Imagen(es) de referencia opcional(es) para la edición de imágenes. Ranura ampliable: conecta hasta 16 imágenes (`image_1` a `image_16`). | IMAGE | No | 0 a 16 imágenes |
| `model.mask` | Máscara opcional para inpainting (las áreas blancas se reemplazarán). Requiere exactamente una imagen de referencia. | MASK | No | N/A |

**Restricciones y limitaciones de los parámetros:**

- Cuando `model.size` es "Custom" (solo gpt-image-2), `model.custom_width` y `model.custom_height` deben ser múltiplos de 16, el borde más largo no debe superar los 3840 píxeles, la relación de aspecto no debe superar 3:1, y el número total de píxeles debe estar entre 655,360 y 8,294,400.
- Una máscara requiere exactamente una imagen de referencia. Una máscara no se puede usar sin una imagen de entrada, ni con múltiples imágenes de entrada.
- Cuando se proporciona una máscara, la altura y el ancho de la máscara deben coincidir con la altura y el ancho de la imagen de entrada.
- Las imágenes de referencia se reducen a un máximo de 2048 x 2048 píxeles en total antes de enviarse a la API.
- El parámetro `seed` aún no está implementado en el backend.
- Si la API devuelve imágenes con dimensiones diferentes en una sola respuesta, todas las imágenes se redimensionan para que coincidan con las dimensiones de la primera imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `image` | La imagen o imágenes generadas, apiladas en un tensor de lote único de forma (N, H, W, C). | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
