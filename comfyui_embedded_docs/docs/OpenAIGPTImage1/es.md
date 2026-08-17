# OpenAI GPT Image 2

Genera imágenes de forma sincrónica a través del endpoint de GPT Image de OpenAI. Este nodo puede crear nuevas imágenes a partir de indicaciones de texto o editar imágenes existentes cuando se proporciona una imagen de entrada y una máscara opcional. Admite múltiples modelos de GPT Image, incluidos gpt-image-1, gpt-image-1.5 y gpt-image-2. Este nodo está obsoleto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Indicación de texto para GPT Image (predeterminado: "") | STRING | Sí | - |
| `seed` | Semilla aleatoria para la generación (predeterminado: 0) - aún no implementada en el backend | INT | No | 0 a 2147483647 |
| `quality` | Calidad de imagen; afecta el costo y el tiempo de generación (predeterminado: "low") | COMBO | No | "low"<br>"medium"<br>"high" |
| `background` | Devuelve la imagen con o sin fondo (predeterminado: "auto") | COMBO | No | "auto"<br>"opaque"<br>"transparent" |
| `size` | Tamaño de imagen. Seleccione "Custom" para usar el ancho y alto personalizados (solo GPT Image 2) (predeterminado: "auto") | COMBO | No | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Cuántas imágenes generar (predeterminado: 1) | INT | No | 1 a 8 |
| `image` | Imagen de referencia opcional para edición de imágenes | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) | MASK | No | - |
| `model` | Modelo de GPT Image a utilizar (predeterminado: "gpt-image-2") | COMBO | No | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840 |
| `custom_height` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840 |

**Restricciones de parámetros:**

- Cuando se proporciona `image`, el nodo cambia al modo de edición de imágenes.
- `mask` solo se puede usar cuando se proporciona `image`.
- Al usar `mask`, solo se admiten imágenes individuales (el tamaño del lote debe ser 1).
- `mask` e `image` deben tener el mismo tamaño.
- La resolución personalizada (`size` = "Custom") solo es compatible con el modelo gpt-image-2.
- El ancho y el alto personalizados deben ser múltiplos de 16.
- La relación de aspecto de la resolución personalizada no debe exceder 3:1.
- Los píxeles totales de la resolución personalizada deben estar entre 655,360 y 8,294,400.
- El fondo transparente no es compatible con el modelo gpt-image-2.
- Los tamaños superiores a 1536x1024 (por ejemplo, 2048x2048, 3840x2160) solo son compatibles con el modelo gpt-image-2.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | Imagen(es) generada(s) o editada(s) | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/es.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
