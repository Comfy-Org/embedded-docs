> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/es.md)

El nodo EmptyCosmosLatentVideo crea un tensor de video latente vacío con dimensiones especificadas. Genera una representación latente rellena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video, con parámetros configurables de ancho, alto, longitud y tamaño de lote.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `width` | INT | Sí | 16 a MAX_RESOLUTION | El ancho del video latente en píxeles (predeterminado: 1280, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | La altura del video latente en píxeles (predeterminado: 704, debe ser divisible por 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | El número de fotogramas en el video latente (predeterminado: 121, debe ser divisible por 8) |
| `batch_size` | INT | No | 1 a 4096 | La cantidad de videos latentes a generar en un lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `samples` | LATENT | El tensor de video latente vacío generado con valores cero |

---
**Source fingerprint (SHA-256):** `f473820af3faf7cb6992ff1959089801e333df395b4007abeb9b504962bfc73b`
