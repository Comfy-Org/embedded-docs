# Hunyuan Video 15 Latent Upscale With Model

El nodo Hunyuan Video 15 Latent Upscale With Model aumenta la resolución de una representación de imagen latente. Primero amplía las muestras latentes a un tamaño específico usando un método de interpolación elegido, luego refina el resultado ampliado usando un modelo de ampliación especializado Hunyuan Video 1.5 para mejorar la calidad.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de ampliación latente Hunyuan Video 1.5 utilizado para refinar las muestras ampliadas. | LATENT_UPSCALE_MODEL | Sí | N/D |
| `muestras` | La representación de imagen latente que se va a ampliar. | LATENT | Sí | N/D |
| `método_de_escalado` | El algoritmo de interpolación utilizado para el paso de ampliación inicial (predeterminado: `"bilinear"`). | COMBO | No | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `ancho` | El ancho objetivo para el latente ampliado, en píxeles. Un valor de 0 calcula el ancho automáticamente según la altura objetivo y la relación de aspecto original. El ancho final de salida será un múltiplo de 16 (predeterminado: 1280). | INT | No | 0 a 16384 (paso: 8) |
| `alto` | La altura objetivo para el latente ampliado, en píxeles. Un valor de 0 calcula la altura automáticamente según el ancho objetivo y la relación de aspecto original. La altura final de salida será un múltiplo de 16 (predeterminado: 720). | INT | No | 0 a 16384 (paso: 8) |
| `recorte` | Determina cómo se recorta el latente ampliado para ajustarse a las dimensiones objetivo. | COMBO | No | `"disabled"`<br>`"center"` |

**Nota sobre las dimensiones:** Si tanto `width` como `height` se establecen en 0, el nodo devuelve las `samples` de entrada sin cambios. Si solo una dimensión se establece en 0, la otra se calcula para preservar la relación de aspecto original. Las dimensiones finales siempre se ajustan para ser al menos 64 píxeles y divisibles por 16.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `LATENT` | La representación de imagen latente ampliada y refinada por el modelo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/es.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
