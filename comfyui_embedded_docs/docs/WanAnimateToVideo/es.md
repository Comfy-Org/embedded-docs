> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/es.md)

El nodo WanAnimateToVideo genera contenido de video combinando múltiples entradas de condicionamiento que incluyen referencias de pose, expresiones faciales y elementos de fondo. Procesa varias entradas de video para crear secuencias animadas coherentes mientras mantiene la consistencia temporal entre fotogramas. El nodo maneja operaciones en el espacio latente y puede extender videos existentes continuando patrones de movimiento.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Condicionamiento positivo para guiar la generación hacia el contenido deseado |
| `negative` | CONDITIONING | Sí | - | Condicionamiento negativo para dirigir la generación lejos del contenido no deseado |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar y decodificar datos de imagen |
| `width` | INT | No | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (valor por defecto: 832, paso: 16) |
| `height` | INT | No | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (valor por defecto: 480, paso: 16) |
| `length` | INT | No | 1 a MAX_RESOLUTION | Número de fotogramas a generar (valor por defecto: 77, paso: 4) |
| `batch_size` | INT | No | 1 a 4096 | Número de videos a generar simultáneamente (valor por defecto: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida opcional del modelo de visión CLIP para condicionamiento adicional |
| `reference_image` | IMAGE | No | - | Imagen de referencia utilizada como punto de partida para la generación |
| `face_video` | IMAGE | No | - | Entrada de video que proporciona guía de expresiones faciales |
| `pose_video` | IMAGE | No | - | Entrada de video que proporciona guía de pose y movimiento |
| `continue_motion_max_frames` | INT | No | 1 a MAX_RESOLUTION | Número máximo de fotogramas para continuar desde el movimiento anterior (valor por defecto: 5, paso: 4) |
| `background_video` | IMAGE | No | - | Video de fondo para componer con el contenido generado |
| `character_mask` | MASK | No | - | Máscara que define regiones de personajes para procesamiento selectivo |
| `continue_motion` | IMAGE | No | - | Secuencia de movimiento anterior desde la cual continuar para consistencia temporal |
| `video_frame_offset` | INT | No | 0 a MAX_RESOLUTION | La cantidad de fotogramas a buscar en todos los videos de entrada. Se utiliza para generar videos más largos por fragmentos. Conectar a la salida video_frame_offset del nodo anterior para extender un video. (valor por defecto: 0, paso: 1) |

**Restricciones de Parámetros:**
- Cuando se proporciona `pose_video` y la lógica `trim_to_pose_video` está activa, la longitud de salida se ajustará para coincidir con la duración del video de pose
- `face_video` se redimensiona automáticamente a una resolución de 512x512 cuando se procesa
- Los fotogramas de `continue_motion` están limitados por el parámetro `continue_motion_max_frames`
- Los videos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) se desplazan por `video_frame_offset` antes del procesamiento
- Si `character_mask` contiene solo un fotograma, se repetirá en todos los fotogramas
- Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con contexto de video adicional |
| `negative` | CONDITIONING | Condicionamiento negativo modificado con contexto de video adicional |
| `latent` | LATENT | Contenido de video generado en formato de espacio latente |
| `trim_latent` | INT | Información de recorte del espacio latente para procesamiento posterior |
| `trim_image` | INT | Información de recorte del espacio de imagen para fotogramas de movimiento de referencia |
| `video_frame_offset` | INT | Desplazamiento de fotograma actualizado para continuar la generación de video en fragmentos |