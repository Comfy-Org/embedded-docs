# EmptyMochiLatentVideo

EmptyMochiLatentVideo crea un tensor de video latente vacío con las dimensiones que especifiques. Genera una representación latente rellena de ceros que puede utilizarse como punto de partida en flujos de trabajo de generación de video. El nodo permite definir el ancho, la altura, la longitud y el tamaño de lote del tensor de video latente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del video latente en píxeles (predeterminado: 848, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | La altura del video latente en píxeles (predeterminado: 480, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas del video latente (predeterminado: 25, debe cumplir que `(length - 1)` sea divisible entre 6) | INT | Sí | 7 a MAX_RESOLUTION |
| `tamaño_del_lote` | El número de videos latentes a generar en un lote (predeterminado: 1) | INT | No | 1 a 4096 |

**Nota:** Las dimensiones latentes reales se calculan como ancho/8 y alto/8, la dimensión temporal se calcula como `((length - 1) // 6) + 1`, y el tensor tiene 12 canales. El parámetro `length` debe cumplir que `(length - 1)` sea divisible entre 6, por lo que los valores válidos son 7, 13, 19, 25, etc.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | Un tensor de video latente vacío con las dimensiones especificadas, que contiene todos los valores en cero | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
