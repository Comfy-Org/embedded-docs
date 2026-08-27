# WanHuMoImageToVideo

El nodo WanHuImageToVideo convierte imágenes en secuencias de video generando representaciones latentes para los fotogramas. Procesa entradas de condicionamiento y puede incorporar imágenes de referencia y embeddings de audio para influir en la generación del video. El nodo genera datos de condicionamiento modificados y representaciones latentes adecuados para la síntesis de video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo que guía la generación de video hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo que aleja la generación de video del contenido no deseado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar las imágenes de referencia en el espacio latente | VAE | Sí | - |
| `ancho` | Ancho de los fotogramas del video de salida en píxeles (predeterminado: 832, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto de los fotogramas del video de salida en píxeles (predeterminado: 480, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en la secuencia de video generada (predeterminado: 97, debe cumplir que (length - 1) sea divisible entre 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de secuencias de video a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_codificador_audio` | Datos de codificación de audio opcionales que pueden influir en la generación de video según el contenido de audio | AUDIOENCODEROUTPUT | No | - |
| `imagen_referencia` | Imagen de referencia opcional utilizada para guiar el estilo y el contenido de la generación de video | IMAGE | No | - |

**Nota:** Cuando se proporciona una imagen de referencia, esta se codifica en un latente que se adjunta al condicionamiento positivo, mientras que un latente relleno de ceros con la misma forma se adjunta al condicionamiento negativo. Cuando se proporciona la salida del codificador de audio, los embeddings de audio se interpolan y se adjuntan al condicionamiento positivo, mientras que un embedding de audio relleno de ceros se adjunta al condicionamiento negativo. Si se omiten las entradas opcionales, se utilizan tensores de relleno con ceros tanto para los latentes de referencia como para los embeddings de audio.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo modificado con la imagen de referencia y/o los embeddings de audio incorporados | CONDITIONING |
| `negativo` | Condicionamiento negativo modificado con la imagen de referencia y/o los embeddings de audio incorporados | CONDITIONING |
| `latente` | Representación latente de la secuencia de video, inicializada en cero y dimensionada según los ajustes de `width`, `height` y `length` | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
