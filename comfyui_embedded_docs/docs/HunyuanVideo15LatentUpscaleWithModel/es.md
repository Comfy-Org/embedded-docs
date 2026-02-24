> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/es.md)

El nodo Hunyuan Video 15 Latent Upscale With Model aumenta la resolución de una representación de imagen latente. Primero, escala las muestras latentes a un tamaño especificado utilizando un método de interpolación elegido, y luego refina el resultado escalado utilizando un modelo especializado de escala superior Hunyuan Video 1.5 para mejorar la calidad.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | LATENT_UPSCALE_MODEL | Sí | N/A | El modelo de escala superior latente Hunyuan Video 1.5 utilizado para refinar las muestras escaladas. |
| `samples` | LATENT | Sí | N/A | La representación de imagen latente que se va a escalar. |
| `upscale_method` | COMBO | No | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` | El algoritmo de interpolación utilizado para el paso inicial de escala superior (por defecto: `"bilinear"`). |
| `width` | INT | No | 0 a 16384 | El ancho objetivo para el latente escalado, en píxeles. Un valor de 0 calculará el ancho automáticamente basándose en la altura objetivo y la relación de aspecto original. El ancho final de salida será un múltiplo de 16 (por defecto: 1280). |
| `height` | INT | No | 0 a 16384 | La altura objetivo para el latente escalado, en píxeles. Un valor de 0 calculará la altura automáticamente basándose en el ancho objetivo y la relación de aspecto original. La altura final de salida será un múltiplo de 16 (por defecto: 720). |
| `crop` | COMBO | No | `"disabled"`<br>`"center"` | Determina cómo se recorta el latente escalado para ajustarse a las dimensiones objetivo. |

**Nota sobre las dimensiones:** Si tanto `width` como `height` se establecen en 0, el nodo devuelve las `samples` de entrada sin cambios. Si solo una dimensión se establece en 0, la otra dimensión se calcula para preservar la relación de aspecto original. Las dimensiones finales siempre se ajustan para tener al menos 64 píxeles y ser divisibles por 16.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La representación de imagen latente escalada y refinada por el modelo. |
