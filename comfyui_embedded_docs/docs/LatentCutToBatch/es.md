# LatentCutToBatch

El nodo LatentCutToBatch divide una representación latente a lo largo de una dimensión seleccionada en múltiples segmentos y los apila en un nuevo lote. Esto permite procesar diferentes partes de una muestra latente de forma independiente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente que se dividirá y agrupará en lotes. | LATENT | Sí | - |
| `dim` | La dimensión a lo largo de la cual se cortarán las muestras latentes. `"t"` se refiere a la dimensión temporal, `"x"` al ancho y `"y"` a la altura. | COMBO | Sí | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | El tamaño de cada segmento a cortar de la dimensión especificada. Si el tamaño de la dimensión no es perfectamente divisible por este valor, el resto se descarta. (predeterminado: 1) | INT | Sí | 1 a 16384 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | El lote latente resultante, que contiene las muestras segmentadas y apiladas. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/es.md)

---
**Source fingerprint (SHA-256):** `38d0ace3ef91e47e3f047aa7057c61e09b6534702526b34691b4bc239c933cd3`
