> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/es.md)

El nodo EmptyMochiLatentVideo crea un tensor de video latente vacío con dimensiones específicas. Genera una representación latente rellena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video. El nodo permite definir el ancho, alto, duración y tamaño de lote para el tensor de video latente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho del video latente en píxeles (valor predeterminado: 848, debe ser divisible entre 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | El alto del video latente en píxeles (valor predeterminado: 480, debe ser divisible entre 16) |
| `length` | INT | Sí | 7 a MAX_RESOLUTION | El número de fotogramas en el video latente (valor predeterminado: 25, debe ser divisible entre 6 después de restar 1) |
| `batch_size` | INT | No | 1 a 4096 | La cantidad de videos latentes a generar en un lote (valor predeterminado: 1) |

**Nota:** Las dimensiones latentes reales se calculan como ancho/8 y alto/8, y la dimensión temporal se calcula como ((duración - 1) // 6) + 1. El parámetro `length` debe cumplir que `(length - 1)` sea divisible entre 6, lo que significa que los valores válidos son 7, 13, 19, 25, etc.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tensor de video latente vacío con las dimensiones especificadas, que contiene todos ceros |

---
**Source fingerprint (SHA-256):** `6876a739355b2dcde42f8c02eb67405678798b818865ec1a73e19076b738554b`
