# WanHuMoImageToVideo

El nodo WanHuMoImageToVideo prepara los datos de condicionamiento y el espacio latente para la generación de video a partir de imágenes. Crea un tensor de video latente vacío, opcionalmente codifica una imagen de referencia con el VAE y, de forma opcional, convierte la salida del codificador de audio en condicionamiento sincronizado con el video. El nodo genera flujos de condicionamiento positivo y negativo, además de un tensor latente para el muestreo de video posterior.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positivo que guía la generación de video hacia el contenido deseado. | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativo que aleja la generación de video del contenido no deseado. | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar la imagen de referencia en el espacio latente. | VAE | Sí | - |
| `width` | Ancho de los fotogramas del video de salida en píxeles (por defecto: 832; debe ser divisible por 16). | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `height` | Alto de los fotogramas del video de salida en píxeles (por defecto: 480; debe ser divisible por 16). | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `length` | Número de fotogramas en la secuencia de video generada (por defecto: 97; debe cumplir que `(length - 1)` sea divisible por 4). | INT | Sí | 1 a MAX_RESOLUTION (paso 4) |
| `batch_size` | Número de secuencias de video a generar simultáneamente (por defecto: 1). | INT | Sí | 1 a 4096 |
| `audio_encoder_output` | Salida opcional del codificador de audio utilizada para influir en la generación de video según el contenido de audio. | AUDIO_ENCODER_OUTPUT | No | - |
| `ref_image` | Imagen de referencia opcional utilizada para guiar el estilo y el contenido de la generación de video. | IMAGE | No | - |

**Nota:** Cuando se proporciona `ref_image`, se redimensiona a `width` x `height`, se codifica con el `vae` y se añade tanto al condicionamiento positivo como al negativo como un latente de referencia. Cuando no se proporciona imagen de referencia, se utilizan latentes de referencia cero. Cuando se proporciona `audio_encoder_output`, sus embeddings de audio se procesan y se añaden a ambas corrientes de condicionamiento como un embedding de audio; de lo contrario, se utiliza un embedding de audio cero.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo con el latente de referencia y la información del embedding de audio añadidos. | CONDITIONING |
| `negative` | Condicionamiento negativo con el latente de referencia y la información del embedding de audio añadidos. | CONDITIONING |
| `latent` | Tensor latente que representa la secuencia de video, inicializado con ceros según `batch_size`, `length`, `height` y `width`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
