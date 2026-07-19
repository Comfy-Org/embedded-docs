# WanSoundImageToVideo

El nodo WanSoundImageToVideo genera contenido de video a partir de imágenes con condicionamiento de audio opcional. Toma indicaciones de condicionamiento positivo y negativo junto con un modelo VAE para crear latentes de video, y puede incorporar imágenes de referencia, codificación de audio, videos de control y referencias de movimiento para guiar el proceso de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Indicaciones de condicionamiento positivo que guían qué contenido debe aparecer en el video generado | CONDITIONING | Sí | - |
| `negativo` | Indicaciones de condicionamiento negativo que especifican qué contenido debe evitarse en el video generado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar y decodificar las representaciones latentes del video | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video generado (predeterminado: 77, debe ser divisible por 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_codificador_audio` | Codificación de audio opcional que puede influir en la generación de video según las características del sonido | AUDIOENCODEROUTPUT | No | - |
| `imagen_ref` | Imagen de referencia opcional que proporciona guía visual para el contenido del video | IMAGE | No | - |
| `video_control` | Video de control opcional que guía el movimiento y la estructura del video generado | IMAGE | No | - |
| `movimiento_ref` | Referencia de movimiento opcional que proporciona guía para los patrones de movimiento en el video | IMAGE | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo procesado que ha sido modificado para la generación de video | CONDITIONING |
| `negativo` | Condicionamiento negativo procesado que ha sido modificado para la generación de video | CONDITIONING |
| `latente` | Representación de video generada en el espacio latente que puede decodificarse en fotogramas de video finales | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `f80f82b8671294a14ecfecf91bc13febae0c91c5efa438467a4413d52dc82d3f`
