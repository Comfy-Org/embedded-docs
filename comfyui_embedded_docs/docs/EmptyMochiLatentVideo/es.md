# EmptyMochiLatentVideo

El nodo EmptyMochiLatentVideo crea un tensor de video latente vacío con dimensiones específicas. Genera una representación latente rellenada con ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video. El nodo permite definir el ancho, alto, longitud y tamaño de lote para el tensor de video latente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho del video latente en píxeles (valor predeterminado: 848, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | El alto del video latente en píxeles (valor predeterminado: 480, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | El número de fotogramas en el video latente (valor predeterminado: 25, debe cumplir que `(length - 1)` sea divisible entre 6) | INT | Sí | 7 a MAX_RESOLUTION |
| `batch_size` | El número de videos latentes a generar en un lote (valor predeterminado: 1) | INT | No | 1 a 4096 |

**Nota:** El nodo comprime las dimensiones espaciales y temporales de la entrada. El ancho y el alto latentes se calculan como `width / 8` y `height / 8`, y la dimensión temporal se calcula como `((length - 1) // 6) + 1`. El parámetro `length` debe cumplir que `(length - 1)` sea divisible entre 6, lo que significa que los valores válidos son 7, 13, 19, 25, etc. El tensor latente resultante tiene 12 canales y una forma final de `(batch_size, 12, ((length - 1) // 6) + 1, height // 8, width // 8)`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | Un tensor de video latente vacío con las dimensiones especificadas, que contiene todos ceros | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
