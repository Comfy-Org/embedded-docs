El nodo WanTrackToVideo convierte datos de seguimiento de movimiento en secuencias de video procesando puntos de seguimiento y generando los fotogramas de video correspondientes. Toma coordenadas de seguimiento como entrada y produce acondicionamiento de video y representaciones latentes que pueden utilizarse para la generación de video. Cuando no se proporcionan seguimientos, recurre a la conversión estándar de imagen a video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Acondicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negativo` | Acondicionamiento negativo para la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificación y decodificación | VAE | Sí | - |
| `pistas` | Datos de seguimiento en formato JSON como cadena multilínea (predeterminado: "[]") | STRING | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video de salida (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `temperatura` | Parámetro de temperatura para el parcheo de movimiento (predeterminado: 220.0, paso: 0.1) | FLOAT | Sí | 1.0 a 1000.0 |
| `topk` | Valor top-k para el parcheo de movimiento (predeterminado: 2) | INT | Sí | 1 a 10 |
| `imagen_inicial` | Imagen inicial para la generación de video | IMAGE | No | - |
| `salida_vision_clip` | Salida de visión CLIP para acondicionamiento adicional | CLIPVISIONOUTPUT | No | - |

**Nota:** Cuando `tracks` contiene datos de seguimiento válidos, el nodo procesa los seguimientos de movimiento para generar video. Cuando `tracks` está vacío, cambia al modo estándar de imagen a video. Si se proporciona `start_image`, inicializa el primer fotograma de la secuencia de video.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Acondicionamiento positivo con información de seguimiento de movimiento aplicada | CONDITIONING |
| `latente` | Acondicionamiento negativo con información de seguimiento de movimiento aplicada | CONDITIONING |
| `latent` | Representación latente del video generado | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/es.md)

---
**Source fingerprint (SHA-256):** `b3e12492d3dafa100266f6be8fe05e4d62b827f1a2bdb4029f804b107dc691ed`
