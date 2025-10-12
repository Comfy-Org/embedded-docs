> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/es.md)

El nodo WanSoundImageToVideoExtend amplía la generación de imagen a video incorporando condicionamiento de audio e imágenes de referencia. Toma condicionamientos positivo y negativo junto con datos latentes de video y opcionales incrustaciones de audio para generar secuencias de video extendidas. El nodo procesa estas entradas para crear salidas de video coherentes que pueden sincronizarse con señales de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Prompts de condicionamiento positivo que guían lo que el video debe incluir |
| `negative` | CONDITIONING | Sí | - | Prompts de condicionamiento negativo que especifican lo que el video debe evitar |
| `vae` | VAE | Sí | - | Autoencoder variacional utilizado para codificar y decodificar los fotogramas del video |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas a generar para la secuencia de video (valor por defecto: 77, paso: 4) |
| `video_latent` | LATENT | Sí | - | Representación latente de video inicial que sirve como punto de partida para la extensión |
| `audio_encoder_output` | AUDIOENCODEROUTPUT | No | - | Incrustaciones de audio opcionales que pueden influir en la generación del video basándose en características del sonido |
| `ref_image` | IMAGE | No | - | Imagen de referencia opcional que proporciona guía visual para la generación del video |
| `control_video` | IMAGE | No | - | Video de control opcional que puede guiar el movimiento y el estilo del video generado |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo procesado con contexto de video aplicado |
| `negative` | CONDITIONING | Condicionamiento negativo procesado con contexto de video aplicado |
| `latent` | LATENT | Representación latente de video generada que contiene la secuencia de video extendida |
