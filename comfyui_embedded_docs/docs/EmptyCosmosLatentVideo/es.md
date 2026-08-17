# EmptyCosmosLatentVideo

El nodo EmptyCosmosLatentVideo crea un tensor de video latente vacío con las dimensiones especificadas. Genera una representación latente rellena de ceros que puede utilizarse como punto de partida para flujos de trabajo de generación de video, con parámetros configurables de ancho, alto, longitud y tamaño de lote. Las dimensiones espaciales del latente se submuestrean por un factor de 8.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho del video latente en píxeles (por defecto: 1280, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | El alto del video latente en píxeles (por defecto: 704, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | El número de fotogramas del video latente (por defecto: 121, debe ser divisible por 8) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | El número de videos latentes a generar en un lote (por defecto: 1) | INT | Sí | 1 a 4096 |

El tensor latente utiliza 16 canales. Las dimensiones espaciales se dividen por 8 en comparación con las dimensiones en píxeles (height // 8, width // 8), y el número de fotogramas se comprime a ((length - 1) // 8) + 1 fotogramas latentes.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | El tensor de video latente vacío generado, con valores de cero. Forma: (batch_size, 16, ((length - 1) // 8) + 1, height // 8, width // 8) | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
