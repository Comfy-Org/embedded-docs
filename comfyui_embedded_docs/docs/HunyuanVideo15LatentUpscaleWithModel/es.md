# Hunyuan Video 15 Latent Upscale With Model

El nodo Hunyuan Video 15 Latent Upscale With Model aumenta la resolución de una representación de imagen latente. Primero amplía las muestras latentes a un tamaño específico usando un método de interpolación elegido y, a continuación, refina el resultado ampliado mediante un modelo de aumento de escala Hunyuan Video 1.5 especializado para mejorar la calidad.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de aumento de escala latente Hunyuan Video 1.5 utilizado para refinar las muestras ampliadas. | LATENT_UPSCALE_MODEL | Sí | N/A |
| `samples` | La representación de imagen latente que se va a ampliar. | LATENT | Sí | N/A |
| `upscale_method` | El algoritmo de interpolación utilizado para el paso inicial de aumento de escala (predeterminado: `"bilinear"`). | COMBO | No | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | El ancho objetivo de la representación latente ampliada, en píxeles. Un valor de 0 calculará el ancho automáticamente a partir de la altura objetivo y la relación de aspecto original. El ancho final de salida será múltiplo de 16 (predeterminado: 1280). | INT | No | 0 a 16384 (paso 8) |
| `height` | La altura objetivo de la representación latente ampliada, en píxeles. Un valor de 0 calculará la altura automáticamente a partir del ancho objetivo y la relación de aspecto original. La altura final de salida será múltiplo de 16 (predeterminado: 720). | INT | No | 0 a 16384 (paso 8) |
| `crop` | Determina cómo se recorta la representación latente ampliada para ajustarse a las dimensiones objetivo. | COMBO | No | `"disabled"`<br>`"center"` |

**Nota sobre las dimensiones:** Si tanto `width` como `height` se establecen en 0, el nodo devuelve los `samples` de entrada sin cambios. Si solo una dimensión se establece en 0, la otra se calcula para conservar la relación de aspecto original. Las dimensiones finales siempre se ajustan para que tengan al menos 64 píxeles y sean divisibles por 16.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | La representación de imagen latente ampliada y refinada por el modelo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/es.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
