# OpenAI GPT Image 2

## Descripción general

Este nodo genera imágenes mediante la API GPT Image de OpenAI. Admite múltiples modelos, permite proporcionar imágenes de entrada para edición y puede utilizar una máscara para especificar qué partes de una imagen modificar.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Texto de solicitud (prompt) para GPT Image (por defecto: ""). | STRING | Sí | N/A |
| `modelo` | El modelo GPT Image de OpenAI a utilizar. Al seleccionar un modelo, se muestran parámetros adicionales específicos de ese modelo. | COMBO | Sí | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `tamaño` | Tamaño de la imagen. Seleccione 'Custom' para usar el ancho y alto personalizados (por defecto: "auto"). Solo disponible para `gpt-image-2`. | COMBO | Sí | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `ancho_personalizado` | Se usa solo cuando `size` es 'Custom'. Debe ser múltiplo de 16 (por defecto: 1024). Solo disponible para `gpt-image-2`. | INT | No | 1024 a 3840 |
| `altura_personalizada` | Se usa solo cuando `size` es 'Custom'. Debe ser múltiplo de 16 (por defecto: 1024). Solo disponible para `gpt-image-2`. | INT | No | 1024 a 3840 |
| `fondo` | Devuelve la imagen con o sin fondo (por defecto: "auto"). Solo disponible para `gpt-image-2`. | COMBO | Sí | `"auto"`<br>`"opaque"` |
| `calidad` | La calidad de la imagen generada. Solo disponible para `gpt-image-2`. | COMBO | Sí | `"standard"`<br>`"hd"` |
| `model.images` | Imágenes de entrada para edición. Solo disponible para `gpt-image-2`. | IMAGE | No | N/A |
| `model.mask` | Una máscara para especificar qué partes de la imagen de entrada se van a editar. Solo disponible para `gpt-image-2`. | MASK | No | N/A |
| `n` | Cuántas imágenes generar (por defecto: 1). | INT | Sí | 1 a 8 |
| `semilla` | Semilla para reproducibilidad (por defecto: 0). Nota: aún no está implementada en el backend. | INT | Sí | 0 a 2147483647 |

**Restricciones y limitaciones de los parámetros:**

- Al usar `gpt-image-2` con un `model.size` de "Custom", `custom_width` y `custom_height` deben ser múltiplos de 16, el lado máximo debe ser `<= 3840`, la relación de aspecto no debe superar 3:1, y el número total de píxeles debe estar entre 655,360 y 8,294,400.
- Si se proporciona una `mask`, se requiere una imagen de entrada (`model.images`). No se puede usar una máscara sin una imagen de entrada.
- Una máscara no se puede usar con múltiples imágenes de entrada.
- Cuando se proporciona una máscara, las dimensiones de la máscara deben coincidir con las dimensiones de la imagen de entrada.
- El parámetro `seed` actualmente no es funcional.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen o las imágenes generadas. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `d0544a2d0f9e9cdd4b121bbf18eb6e43d508b2230e44dfa814649f6a4999e543`
