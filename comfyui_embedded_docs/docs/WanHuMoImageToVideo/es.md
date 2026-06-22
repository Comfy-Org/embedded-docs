# WanHuMoImageToVideo

El nodo WanHuMoImageToVideo convierte imágenes en secuencias de video generando representaciones latentes para los fotogramas del video. Procesa entradas de condicionamiento y puede incorporar imágenes de referencia y embeddings de audio para influir en la generación del video. El nodo produce datos de condicionamiento modificados y representaciones latentes adecuadas para la síntesis de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo que guía la generación del video hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo que aleja la generación del video de contenido no deseado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes de referencia en el espacio latente | VAE | Sí | - |
| `ancho` | Ancho de los fotogramas del video de salida en píxeles (predeterminado: 832, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto de los fotogramas del video de salida en píxeles (predeterminado: 480, debe ser divisible entre 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en la secuencia de video generada (predeterminado: 97, debe cumplir que (length - 1) sea divisible entre 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de secuencias de video a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_codificador_audio` | Datos opcionales de codificación de audio que pueden influir en la generación del video según el contenido de audio | AUDIOENCODEROUTPUT | No | - |
| `imagen_referencia` | Imagen de referencia opcional utilizada para guiar el estilo y contenido de la generación del video | IMAGE | No | - |

**Nota:** Cuando se proporciona una imagen de referencia, esta se codifica y se añade tanto al condicionamiento positivo como al negativo. Cuando se proporciona la salida del codificador de audio, se procesa e incorpora a los datos de condicionamiento. Si no se proporciona ninguno, se utilizan tensores de relleno con ceros tanto para los latentes de referencia como para los embeddings de audio.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo modificado con la imagen de referencia y/o embeddings de audio incorporados | CONDITIONING |
| `latente` | Condicionamiento negativo modificado con la imagen de referencia y/o embeddings de audio incorporados | CONDITIONING |
| `latent` | Representación latente generada que contiene los datos de la secuencia de video | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `6301671d04748ce80c561a65df80c7ca146b91bcce8851872df40211af29fd39`
