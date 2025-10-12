> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/es.md)

El nodo EmptyCosmosLatentVideo crea un tensor de video latente vacío con dimensiones específicas. Genera una representación latente llena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video, con parámetros configurables de ancho, alto, longitud y tamaño de lote.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | El ancho del video latente en píxeles (por defecto: 1280, debe ser divisible por 16) |
| `altura` | INT | Sí | 16 a MAX_RESOLUTION | La altura del video latente en píxeles (por defecto: 704, debe ser divisible por 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | El número de fotogramas en el video latente (por defecto: 121) |
| `tamaño_del_lote` | INT | No | 1 a 4096 | El número de videos latentes a generar en un lote (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | El tensor de video latente vacío generado con valores cero |