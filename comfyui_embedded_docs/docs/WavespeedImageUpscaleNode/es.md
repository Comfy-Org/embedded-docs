> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/es.md)

El nodo WaveSpeed Image Upscale utiliza un servicio de IA externo para aumentar la resolución y calidad de una imagen. Toma una sola foto de entrada y la amplía a una resolución objetivo superior, como 2K, 4K u 8K, produciendo un resultado más nítido y detallado.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | STRING | Sí | `"SeedVR2"`<br>`"Ultimate"` | El modelo de IA a utilizar para la ampliación. "SeedVR2" y "Ultimate" ofrecen diferentes niveles de calidad y precios. |
| `image` | IMAGE | Sí | | La imagen de entrada que se va a ampliar. |
| `target_resolution` | STRING | Sí | `"2K"`<br>`"4K"`<br>`"8K"` | La resolución de salida deseada para la imagen ampliada. |

**Nota:** Este nodo requiere exactamente una imagen de entrada. Proporcionar un lote de imágenes generará un error.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen de salida ampliada y de alta resolución. |

---
**Source fingerprint (SHA-256):** `b14056f981f6e34c67d8126391acc11878f92f5f406559afbac803c86da42bcc`
