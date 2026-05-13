> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/es.md)

Este nodo genera imágenes de forma síncrona utilizando el modelo Stable Diffusion 3.5 de Stability AI. Crea imágenes basadas en indicaciones de texto y también puede modificar imágenes existentes cuando se proporcionan como entrada. El nodo admite varias relaciones de aspecto y ajustes preestablecidos de estilo para personalizar el resultado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Una indicación sólida y descriptiva que defina claramente elementos, colores y sujetos generará mejores resultados. (predeterminado: cadena vacía) |
| `model` | COMBO | Sí | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` | El modelo Stable Diffusion 3.5 a utilizar para la generación. |
| `aspect_ratio` | COMBO | Sí | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` | Relación de aspecto de la imagen generada. (predeterminado: 1:1) |
| `style_preset` | COMBO | No | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` | Estilo deseado opcional de la imagen generada. Selecciona "None" para no usar un ajuste preestablecido de estilo. |
| `cfg_scale` | FLOAT | Sí | 1.0 a 10.0 | Qué estrictamente se adhiere el proceso de difusión al texto de la indicación (valores más altos mantienen tu imagen más cercana a tu indicación). (predeterminado: 4.0) |
| `seed` | INT | Sí | 0 a 4294967294 | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) |
| `image` | IMAGE | No | - | Imagen de entrada opcional para generación de imagen a imagen. Cuando se proporciona, el nodo cambia al modo de imagen a imagen y el parámetro `aspect_ratio` se ignora. |
| `negative_prompt` | STRING | No | - | Palabras clave de lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. (predeterminado: cadena vacía) |
| `image_denoise` | FLOAT | No | 0.0 a 1.0 | Reducción de ruido de la imagen de entrada; 0.0 produce una imagen idéntica a la entrada, 1.0 es como si no se hubiera proporcionado ninguna imagen. (predeterminado: 0.5) Este parámetro solo se utiliza cuando se proporciona una `image`. |

**Nota:** Cuando se proporciona una `image`, el nodo cambia al modo de generación de imagen a imagen y el parámetro `aspect_ratio` se determina automáticamente a partir de la imagen de entrada. Cuando no se proporciona ninguna `image`, el parámetro `image_denoise` se ignora.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | La imagen generada o modificada. |

---
**Source fingerprint (SHA-256):** `80dbb27f19bb3286ee988f020f7f65623a73d7cac77ca0cdfc7a428254102aa3`
