El nodo EmptyLTXVLatentVideo crea un tensor latente vacío para procesamiento de video. Genera un punto de partida en blanco con dimensiones específicas que puede utilizarse como entrada para flujos de trabajo de generación de video. El nodo produce una representación latente rellena de ceros con el ancho, alto, duración y tamaño de lote configurados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho del tensor latente de video (predeterminado: 768, incremento: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `altura` | La altura del tensor latente de video (predeterminado: 512, incremento: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas en el video latente (predeterminado: 97, incremento: 8) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | La cantidad de videos latentes a generar en un lote (predeterminado: 1) | INT | No | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | El tensor latente vacío generado con valores cero en las dimensiones especificadas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/es.md)

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`
