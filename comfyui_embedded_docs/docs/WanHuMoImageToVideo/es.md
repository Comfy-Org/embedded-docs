> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/es.md)

El nodo WanHuMoImageToVideo convierte imágenes en secuencias de video generando representaciones latentes para los fotogramas de video. Procesa entradas de condicionamiento y puede incorporar imágenes de referencia y incrustaciones de audio para influir en la generación del video. El nodo genera datos de condicionamiento modificados y representaciones latentes adecuadas para la síntesis de video.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo que guía la generación del video hacia el contenido deseado |
| `negative` | CONDITIONING | Sí | - | Entrada de condicionamiento negativo que aleja la generación del video de contenido no deseado |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar imágenes de referencia en el espacio latente |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho de los fotogramas de video de salida en píxeles (por defecto: 832, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto de los fotogramas de video de salida en píxeles (por defecto: 480, debe ser divisible por 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video generada (por defecto: 97) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de secuencias de video a generar simultáneamente (por defecto: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | No | - | Datos de codificación de audio opcionales que pueden influir en la generación del video basándose en el contenido de audio |
| `ref_image` | IMAGE | No | - | Imagen de referencia opcional utilizada para guiar el estilo y contenido de la generación del video |

**Nota:** Cuando se proporciona una imagen de referencia, esta se codifica y se añade tanto al condicionamiento positivo como al negativo. Cuando se proporciona una salida del codificador de audio, esta se procesa e incorpora en los datos de condicionamiento.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con la imagen de referencia y/o las incrustaciones de audio incorporadas |
| `negative` | CONDITIONING | Condicionamiento negativo modificado con la imagen de referencia y/o las incrustaciones de audio incorporadas |
| `latent` | LATENT | Representación latente generada que contiene los datos de la secuencia de video |