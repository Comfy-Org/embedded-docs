> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/es.md)

El nodo EmptyMochiLatentVideo crea un tensor de video latente vacío con dimensiones específicas. Genera una representación latente llena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video. El nodo permite definir el ancho, alto, longitud y tamaño de lote para el tensor de video latente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho del video latente en píxeles (por defecto: 848, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | El alto del video latente en píxeles (por defecto: 480, debe ser divisible por 16) |
| `length` | INT | Sí | 7 a MAX_RESOLUTION | El número de fotogramas en el video latente (por defecto: 25) |
| `batch_size` | INT | No | 1 a 4096 | El número de videos latentes a generar en un lote (por defecto: 1) |

**Nota:** Las dimensiones latentes reales se calculan como ancho/8 y alto/8, y la dimensión temporal se calcula como ((longitud - 1) // 6) + 1.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | Un tensor de video latente vacío con las dimensiones especificadas, que contiene todos ceros |