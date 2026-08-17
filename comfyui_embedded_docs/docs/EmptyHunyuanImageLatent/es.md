# ImagenLatenteHunyuanVacía

El nodo EmptyHunyuanImageLatent crea un tensor latente vacío con dimensiones específicas para su uso con modelos de generación de imágenes Hunyuan. Genera un punto de partida en blanco que puede procesarse mediante nodos posteriores en el flujo de trabajo. El nodo permite especificar el ancho, el alto y el tamaño de lote del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `width` | El ancho de la imagen latente generada en píxeles (predeterminado: 2048, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `height` | El alto de la imagen latente generada en píxeles (predeterminado: 2048, paso: 32) | INT | Sí | 64 a MAX_RESOLUTION |
| `batch_size` | El número de muestras latentes a generar en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `LATENT` | Un tensor latente vacío con las dimensiones especificadas para el procesamiento de imágenes Hunyuan. El tensor tiene 64 canales y sus dimensiones espaciales son una treintaidosava parte (1/32) del ancho y alto solicitados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/es.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
