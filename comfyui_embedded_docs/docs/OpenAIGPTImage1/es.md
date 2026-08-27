# OpenAI GPT Image 2

Genera imágenes de forma síncrona a través del endpoint GPT Image de OpenAI. El nodo puede crear imágenes nuevas a partir de indicaciones de texto o editar imágenes existentes cuando se le proporciona una imagen de entrada y una máscara opcional. Es compatible con los modelos gpt-image-1, gpt-image-1.5 y gpt-image-2 y está marcado como obsoleto.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `prompt` | Indicación de texto para GPT Image (predeterminado: "") | STRING | Sí | - |
| `seed` | Semilla aleatoria para la generación (predeterminado: 0) - aún no implementada en el backend | INT | No | 0 a 2147483647 |
| `quality` | Calidad de imagen, afecta al costo y al tiempo de generación (predeterminado: "low") | COMBO | No | "low"<br>"medium"<br>"high" |
| `background` | Devuelve la imagen con o sin fondo (predeterminado: "auto") | COMBO | No | "auto"<br>"opaque"<br>"transparent" |
| `size` | Tamaño de imagen. Seleccione "Custom" para usar el ancho y alto personalizados (solo GPT Image 2) (predeterminado: "auto") | COMBO | No | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | Cuántas imágenes generar (predeterminado: 1) | INT | No | 1 a 8 |
| `image` | Imagen de referencia opcional para la edición de imágenes | IMAGE | No | - |
| `mask` | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) | MASK | No | - |
| `model` | Modelo GPT Image a utilizar (predeterminado: "gpt-image-2") | COMBO | No | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840, step 16 |
| `custom_height` | Se usa solo cuando `size` es "Custom". Debe ser múltiplo de 16 (solo GPT Image 2) (predeterminado: 1024) | INT | No | 1024 a 3840, step 16 |

**Restricciones de parámetros:**

- Cuando se proporciona `image`, el nodo cambia al modo de edición de imágenes.
- `mask` solo se puede usar cuando se proporciona `image`.
- Al usar `mask`, solo se admiten imágenes individuales (el tamaño del lote debe ser 1).
- `mask` e `image` deben tener el mismo tamaño.
- La resolución personalizada (`size` = "Custom") solo es compatible con el modelo gpt-image-2.
- El ancho y alto personalizados deben ser múltiplos de 16.
- La relación de aspecto de la resolución personalizada no debe superar 3:1.
- El total de píxeles de la resolución personalizada debe estar entre 655 360 y 8 294 400.
- El fondo transparente no es compatible con el modelo gpt-image-2.
- Los tamaños mayores que 1536x1024 (por ejemplo, 2048x2048, 3840x2160) solo son compatibles con el modelo gpt-image-2.
- Los modelos `gpt-image-1` y `gpt-image-1.5` solo admiten los tamaños `auto`, `1024x1024`, `1024x1536` y `1536x1024`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `IMAGE` | Imagen(es) generada(s) o editada(s) | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/es.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
