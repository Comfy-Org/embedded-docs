# LatentCutToBatch

El nodo **LatentCutToBatch** divide una representación latente a lo largo de una dimensión elegida en múltiples segmentos y los apila en un nuevo lote. Esto permite procesar diferentes partes de una muestra latente de forma independiente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente que se va a dividir y agrupar en lotes. | LATENT | Sí | - |
| `dim` | La dimensión a lo largo de la cual se cortan las muestras latentes. `"t"` se refiere a la dimensión temporal, `"x"` a la anchura y `"y"` a la altura. | COMBO | Sí | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | El tamaño de cada segmento que se corta de la dimensión especificada. Si el tamaño de la dimensión no es perfectamente divisible por este valor, el resto se descarta. (por defecto: 1) | INT | Sí | 1 a 16384 (resolución máxima) |

Nota: Si la dimensión seleccionada es el eje de lote o de canal, la entrada se devuelve sin cambios. Si `slice_size` es mayor que el tamaño de la dimensión, se usa toda la dimensión como un único segmento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El lote latente resultante, que contiene las muestras segmentadas y apiladas. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/es.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
