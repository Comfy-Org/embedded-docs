> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/es.md)

Este nodo mejora imágenes de baja resolución ampliándolas a superresolución, eliminando artefactos y ruido. Utiliza una API externa para procesar la imagen y puede ajustar automáticamente el tamaño de entrada para mantenerse dentro de los límites de procesamiento. El tamaño máximo de salida permitido es de 4 megapíxeles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | STRING | Sí | `"generative_portrait"`<br>`"generative"` | El modelo de mejora a utilizar. El modelo `generative_portrait` está optimizado para retratos, mientras que `generative` es un modelo de propósito general. |
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a mejorar. |
| `upscale_factor` | INT | Sí | `1`<br>`2`<br>`4` | El factor por el cual se ampliarán las dimensiones de la imagen. Un factor de 1 significa sin ampliación, 2 duplica las dimensiones y 4 las cuadruplica. |
| `auto_downscale` | BOOLEAN | No | - | Reduce automáticamente la escala de la imagen de entrada si la salida supera el límite. Cuando está habilitado, el nodo intentará reducir el tamaño de la imagen de entrada para que se ajuste al límite de salida de 4 megapíxeles antes de aplicar el factor de ampliación solicitado. (predeterminado: `False`) |

**Nota:** El nodo generará un error si el tamaño de salida calculado (alto de entrada × factor de ampliación × ancho de entrada × factor de ampliación) supera los 4,000,000 de píxeles (4MP) y `auto_downscale` está deshabilitado. Cuando `auto_downscale` está habilitado, el nodo intentará reducir la escala de la imagen de entrada para que se ajuste al límite antes de aplicar el factor de ampliación solicitado. Si se requiriera una reducción de escala de más de 2x, el nodo reducirá el factor de ampliación en su lugar.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen de salida mejorada y ampliada. |

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
