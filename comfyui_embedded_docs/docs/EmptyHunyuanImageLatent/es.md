El nodo EmptyHunyuanImageLatent crea un tensor latente vacío con dimensiones específicas para su uso con modelos de generación de imágenes Hunyuan. Genera un punto de partida en blanco que puede procesarse a través de nodos posteriores en el flujo de trabajo. El nodo permite especificar el ancho, alto y tamaño de lote del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente generada en píxeles (predeterminado: 2048, incremento: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `alto` | El alto de la imagen latente generada en píxeles (predeterminado: 2048, incremento: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `tamaño_lote` | El número de muestras latentes a generar en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | Un tensor latente vacío con las dimensiones especificadas para el procesamiento de imágenes Hunyuan | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/es.md)

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`
