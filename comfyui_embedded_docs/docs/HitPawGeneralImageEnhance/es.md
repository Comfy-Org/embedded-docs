# HitPaw General Image Enhance

Este nodo mejora imágenes de baja resolución ampliándolas a superresolución, eliminando artefactos y ruido. Utiliza una API externa para procesar la imagen y puede ajustar automáticamente el tamaño de entrada para mantenerse dentro de los límites de procesamiento. El tamaño máximo de salida permitido es de 32 megapíxeles.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo de mejora a utilizar. El modelo `generative_portrait` está optimizado para retratos, mientras que `generative` es un modelo de uso general. | COMBO | Sí | `"generative_portrait"`<br>`"generative"` |
| `imagen` | La imagen de entrada que se va a mejorar. | IMAGE | Sí | - |
| `factor de escalado` | El factor por el cual se amplían las dimensiones de la imagen. Un factor de 1 significa que no se amplía, 2 duplica las dimensiones y 4 las cuadruplica. | COMBO | Sí | `1`<br>`2`<br>`4` |
| `reducción automática` | Reduce automáticamente la escala de la imagen de entrada si la salida excediera el límite. (predeterminado: `False`) | BOOLEAN | No | - |

**Nota:** El nodo genera un error si el tamaño de salida calculado (ancho de entrada × upscale_factor × alto de entrada × upscale_factor) supera los 32 000 000 de píxeles (32 MP) y `auto_downscale` está deshabilitado. Cuando `auto_downscale` está habilitado, el nodo reduce automáticamente el tamaño de la imagen de entrada o el factor de ampliación (o ambos) para que la salida se ajuste al límite de 32 MP.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen de salida mejorada y ampliada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/es.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
