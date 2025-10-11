> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/es.md)

El nodo WanSoundImageToVideo genera contenido de video a partir de imágenes con condicionamiento de audio opcional. Toma prompts de condicionamiento positivo y negativo junto con un modelo VAE para crear latentes de video, y puede incorporar imágenes de referencia, codificación de audio, videos de control y referencias de movimiento para guiar el proceso de generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Prompts de condicionamiento positivo que guían qué contenido debe aparecer en el video generado |
| `negative` | CONDITIONING | Sí | - | Prompts de condicionamiento negativo que especifican qué contenido debe evitarse en el video generado |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar y decodificar las representaciones latentes del video |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (por defecto: 832, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (por defecto: 480, debe ser divisible por 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de frames en el video generado (por defecto: 77, debe ser divisible por 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (por defecto: 1) |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | No | - | Codificación de audio opcional que puede influir en la generación del video basándose en características del sonido |
| `ref_image` | IMAGE | No | - | Imagen de referencia opcional que proporciona guía visual para el contenido del video |
| `control_video` | IMAGE | No | - | Video de control opcional que guía el movimiento y la estructura del video generado |
| `ref_motion` | IMAGE | No | - | Referencia de movimiento opcional que proporciona guía para los patrones de movimiento en el video |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo procesado que ha sido modificado para la generación de video |
| `negative` | CONDITIONING | Condicionamiento negativo procesado que ha sido modificado para la generación de video |
| `latent` | LATENT | Representación de video generada en el espacio latente que puede decodificarse en frames de video finales |