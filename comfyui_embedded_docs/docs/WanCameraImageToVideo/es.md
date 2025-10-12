> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/es.md)

El nodo WanCameraImageToVideo convierte imágenes en secuencias de video generando representaciones latentes para la generación de video. Procesa entradas de condicionamiento e imágenes iniciales opcionales para crear latentes de video que pueden utilizarse con modelos de video. El nodo admite condiciones de cámara y salidas de visión CLIP para un control mejorado de la generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Prompts de condicionamiento positivo para la generación de video |
| `negative` | CONDITIONING | Sí | - | Prompts de condicionamiento negativo a evitar en la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para codificar imágenes al espacio latente |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (valor por defecto: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (valor por defecto: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (valor por defecto: 81, paso: 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (valor por defecto: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para condicionamiento adicional |
| `start_image` | IMAGE | No | - | Imagen inicial opcional para inicializar la secuencia de video |
| `camera_conditions` | WAN_CAMERA_EMBEDDING | No | - | Condiciones de embedding de cámara opcionales para la generación de video |

**Nota:** Cuando se proporciona `start_image`, el nodo la utiliza para inicializar la secuencia de video y aplica enmascaramiento para fusionar los fotogramas iniciales con el contenido generado. Los parámetros `camera_conditions` y `clip_vision_output` son opcionales, pero cuando se proporcionan, modifican el condicionamiento tanto para los prompts positivos como negativos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con las condiciones de cámara y salidas de visión CLIP aplicadas |
| `negative` | CONDITIONING | Condicionamiento negativo modificado con las condiciones de cámara y salidas de visión CLIP aplicadas |
| `latent` | LATENT | Representación latente de video generada para usar con modelos de video |
