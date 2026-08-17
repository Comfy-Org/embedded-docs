# WanTrackToVideo

El nodo WanTrackToVideo utiliza datos de seguimiento de movimiento (trayectorias de puntos) para guiar la generación de video. Procesa las trayectorias, opcionalmente las combina con una imagen inicial y produce salidas positivas y negativas condicionadas, además de un tensor latente para el modelo de video Wan. Cuando no se proporciona ninguna trayectoria válida, recurre a la conversión estándar de imagen a video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negative` | Condicionamiento negativo para la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar los fotogramas de video | VAE | Sí | - |
| `tracks` | Datos de seguimiento en formato JSON como una cadena multilínea (predeterminado: "[]") | STRING | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas del video de salida (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `temperature` | Parámetro avanzado de temperatura para el parcheado de movimiento (predeterminado: 220.0, paso: 0.1) | FLOAT | Sí | 1.0 a 1000.0 |
| `topk` | Valor avanzado de top-k para el parcheado de movimiento (predeterminado: 2) | INT | Sí | 1 a 10 |
| `start_image` | Imagen inicial utilizada para el primer fotograma de la generación de video | IMAGE | Sí | - |
| `clip_vision_output` | Salida de CLIP vision para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |

**Notas:**
- La entrada `tracks` espera una cadena JSON o una lista de cadenas JSON que contengan datos de seguimiento de puntos. Si el valor de `tracks` está vacío o no se puede parsear, el nodo recurre al comportamiento de WanImageToVideo.
- Cuando `start_image` está presente, se redimensiona para que coincida con `width` y `height` y se utiliza como primer fotograma de la secuencia de video.
- Cuando se proporciona `clip_vision_output`, se añade tanto al condicionamiento positivo como al negativo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo con la trayectoria de movimiento y la información de imagen opcional aplicadas | CONDITIONING |
| `negative` | Condicionamiento negativo con la trayectoria de movimiento y la información de imagen opcional aplicadas | CONDITIONING |
| `latent` | Tensor latente relleno de ceros, dimensionado para las dimensiones, la longitud y el tamaño de lote solicitados para el video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/es.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
