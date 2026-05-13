> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

El nodo EmptyLTXVLatentVideo crea un tensor latente vacío para procesamiento de video. Genera un punto de partida en blanco con dimensiones específicas que puede utilizarse como entrada para flujos de trabajo de generación de video. El nodo produce una representación latente rellena de ceros con el ancho, alto, duración y tamaño de lote configurados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `width` | INT | Sí | 64 a MAX_RESOLUTION | El ancho del tensor latente de video (predeterminado: 768, incremento: 32) |
| `height` | INT | Sí | 64 a MAX_RESOLUTION | La altura del tensor latente de video (predeterminado: 512, incremento: 32) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | El número de fotogramas en el video latente (predeterminado: 97, incremento: 8) |
| `batch_size` | INT | No | 1 a 4096 | La cantidad de videos latentes a generar en un lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `samples` | LATENT | El tensor latente vacío generado con valores cero en las dimensiones especificadas |

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`
