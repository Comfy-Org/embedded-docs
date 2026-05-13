> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/es.md)

El nodo WanTrackToVideo convierte datos de seguimiento de movimiento en secuencias de video procesando puntos de seguimiento y generando los fotogramas de video correspondientes. Toma coordenadas de seguimiento como entrada y produce acondicionamiento de video y representaciones latentes que pueden utilizarse para la generación de video. Cuando no se proporcionan seguimientos, recurre a la conversión estándar de imagen a video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Acondicionamiento positivo para la generación de video |
| `negative` | CONDITIONING | Sí | - | Acondicionamiento negativo para la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para codificación y decodificación |
| `tracks` | STRING | Sí | - | Datos de seguimiento en formato JSON como cadena multilínea (predeterminado: "[]") |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video de salida (predeterminado: 81, paso: 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `temperature` | FLOAT | Sí | 1.0 a 1000.0 | Parámetro de temperatura para el parcheo de movimiento (predeterminado: 220.0, paso: 0.1) |
| `topk` | INT | Sí | 1 a 10 | Valor top-k para el parcheo de movimiento (predeterminado: 2) |
| `start_image` | IMAGE | No | - | Imagen inicial para la generación de video |
| `clip_vision_output` | CLIPVISIONOUTPUT | No | - | Salida de visión CLIP para acondicionamiento adicional |

**Nota:** Cuando `tracks` contiene datos de seguimiento válidos, el nodo procesa los seguimientos de movimiento para generar video. Cuando `tracks` está vacío, cambia al modo estándar de imagen a video. Si se proporciona `start_image`, inicializa el primer fotograma de la secuencia de video.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | Acondicionamiento positivo con información de seguimiento de movimiento aplicada |
| `negative` | CONDITIONING | Acondicionamiento negativo con información de seguimiento de movimiento aplicada |
| `latent` | LATENT | Representación latente del video generado |

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
