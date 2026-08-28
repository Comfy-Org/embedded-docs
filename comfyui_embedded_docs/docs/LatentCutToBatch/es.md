# LatentCutToBatch

El nodo LatentCutToBatch divide una representación latente a lo largo de una dimensión elegida (tiempo, ancho o alto) en segmentos de un tamaño especificado y los apila en un nuevo lote. Cada segmento se convierte en un elemento separado del lote, por lo que diferentes partes de una muestra latente pueden procesarse de forma independiente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente que se dividirá y agrupará en lotes. | LATENT | Sí | - |
| `dim` | La dimensión a lo largo de la cual se cortan las muestras latentes. `"t"` se refiere a la dimensión temporal (fotogramas), `"x"` al ancho y `"y"` a la altura. | COMBO | Sí | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | El tamaño de cada segmento que se cortará de la dimensión especificada. Si el tamaño de la dimensión no es perfectamente divisible por este valor, el resto se descarta. (predeterminado: 1) | INT | Sí | 1 a 16384 (resolución máxima) |

Nota: La opción `"t"` solo tiene efecto cuando el latente incluye una dimensión temporal. Si la dimensión elegida corresponde a la posición del lote o del canal, o no existe (por ejemplo, al seleccionar `"t"` en un latente sin fotogramas), el nodo devuelve la entrada sin cambios. Si `slice_size` es mayor que el tamaño de la dimensión elegida, se utiliza toda la dimensión como un solo segmento. Cuando el tamaño de la dimensión no es divisible uniformemente entre `slice_size`, la parte sobrante al final se descarta. El tamaño del lote de salida es el tamaño del lote de entrada multiplicado por el número de segmentos, y la dimensión segmentada en sí se reduce a `slice_size`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El lote latente resultante, que contiene las muestras segmentadas y apiladas. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/es.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
