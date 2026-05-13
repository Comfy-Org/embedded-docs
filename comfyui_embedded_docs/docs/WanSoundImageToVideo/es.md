> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/es.md)

El nodo WanSoundImageToVideo genera contenido de video a partir de imágenes con condicionamiento de audio opcional. Toma indicaciones de condicionamiento positivo y negativo junto con un modelo VAE para crear latentes de video, y puede incorporar imágenes de referencia, codificación de audio, videos de control y referencias de movimiento para guiar el proceso de generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento positivo que guían qué contenido debe aparecer en el video generado |
| `negativo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento negativo que especifican qué contenido debe evitarse en el video generado |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar y decodificar las representaciones latentes del video |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, debe ser divisible por 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video generado (predeterminado: 77, debe ser divisible por 4) |
| `tamaño_lote` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `salida_codificador_audio` | AUDIOENCODEROUTPUT | No | - | Codificación de audio opcional que puede influir en la generación de video según las características del sonido |
| `imagen_ref` | IMAGE | No | - | Imagen de referencia opcional que proporciona guía visual para el contenido del video |
| `video_control` | IMAGE | No | - | Video de control opcional que guía el movimiento y la estructura del video generado |
| `movimiento_ref` | IMAGE | No | - | Referencia de movimiento opcional que proporciona guía para los patrones de movimiento en el video |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo procesado que ha sido modificado para la generación de video |
| `latente` | CONDITIONING | Condicionamiento negativo procesado que ha sido modificado para la generación de video |
| `latent` | LATENT | Representación de video generada en el espacio latente que puede decodificarse en fotogramas de video finales |

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
