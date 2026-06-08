El nodo **Hunyuan Video 15 Latent Upscale With Model** aumenta la resolución de una representación de imagen latente. Primero, escala las muestras latentes a un tamaño específico utilizando un método de interpolación seleccionado, luego refina el resultado escalado usando un modelo de escalado especializado Hunyuan Video 1.5 para mejorar la calidad.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de escalado latente Hunyuan Video 1.5 utilizado para refinar las muestras escaladas. | LATENT_UPSCALE_MODEL | Sí | N/A |
| `muestras` | La representación de imagen latente que se va a escalar. | LATENT | Sí | N/A |
| `método_de_escalado` | El algoritmo de interpolación utilizado para el paso de escalado inicial (predeterminado: `"bilinear"`). | COMBO | No | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `ancho` | El ancho objetivo para el latente escalado, en píxeles. Un valor de 0 calculará el ancho automáticamente según la altura objetivo y la relación de aspecto original. El ancho final de salida será un múltiplo de 16 (predeterminado: 1280). | INT | No | 0 a 16384 |
| `alto` | La altura objetivo para el latente escalado, en píxeles. Un valor de 0 calculará la altura automáticamente según el ancho objetivo y la relación de aspecto original. La altura final de salida será un múltiplo de 16 (predeterminado: 720). | INT | No | 0 a 16384 |
| `recorte` | Determina cómo se recorta el latente escalado para ajustarse a las dimensiones objetivo. | COMBO | No | `"disabled"`<br>`"center"` |

**Nota sobre Dimensiones:** Si tanto `width` como `height` se establecen en 0, el nodo devuelve las `samples` de entrada sin cambios. Si solo una dimensión se establece en 0, la otra dimensión se calcula para preservar la relación de aspecto original. Las dimensiones finales siempre se ajustan para tener al menos 64 píxeles y ser divisibles entre 16.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | La representación de imagen latente escalada y refinada por el modelo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/es.md)

---
**Source fingerprint (SHA-256):** `1de9e157c1a0433f1b3d5ff4d428a1aa392fd65da5e314e6e818ce66495d5ef4`
