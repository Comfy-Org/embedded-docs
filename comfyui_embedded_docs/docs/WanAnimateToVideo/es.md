# WanAnimateToVideo

Este nodo experimental prepara la generación de video de Wan combinando una imagen de referencia con videos opcionales de pose, rostro y fondo. Construye datos de condicionamiento y un tensor de video latente vacío para la generación posterior, y devuelve información de desplazamiento de fotogramas que ayuda a extender videos existentes por segmentos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Condicionamiento positivo para guiar la generación hacia el contenido deseado. | CONDITIONING | Sí | - |
| `negative` | Condicionamiento negativo para alejar la generación del contenido no deseado. | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar y decodificar datos de imagen. | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16). | INT | Sí | 16 a MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16). | INT | Sí | 16 a MAX_RESOLUTION |
| `length` | Número de fotogramas a generar (predeterminado: 77, paso: 4). | INT | Sí | 1 a MAX_RESOLUTION |
| `batch_size` | Número de videos a generar en un solo lote (predeterminado: 1). | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida opcional del modelo de visión CLIP utilizada como condicionamiento adicional tanto para el condicionamiento positivo como para el negativo. | CLIP_VISION_OUTPUT | No | - |
| `reference_image` | Imagen de referencia utilizada como punto de partida para la generación. Si no se proporciona, se usa una imagen negra (todos los ceros). | IMAGE | No | - |
| `face_video` | Video que proporciona guía de expresiones faciales. Al procesarse, se redimensiona a 512x512 y se normaliza al rango de -1.0 a 1.0. | IMAGE | No | - |
| `pose_video` | Video que proporciona guía de pose y movimiento. Si es más corto que `length`, se rellena con su último fotograma. | IMAGE | No | - |
| `continue_motion_max_frames` | Número máximo de fotogramas para continuar desde un movimiento anterior. Solo se utilizan los últimos esta cantidad de fotogramas de `continue_motion` (predeterminado: 5, paso: 4). | INT | Sí | 1 a MAX_RESOLUTION |
| `background_video` | Video de fondo para componer con el contenido generado. | IMAGE | No | - |
| `character_mask` | Máscara que define regiones de personajes para procesamiento selectivo. Si la máscara tiene un solo fotograma, se repite en todos los fotogramas. | MASK | No | - |
| `continue_motion` | Secuencia de movimiento anterior utilizada para mantener la consistencia temporal al extender un video. Solo se utilizan los últimos `continue_motion_max_frames` fotogramas. | IMAGE | No | - |
| `video_frame_offset` | Cantidad de fotogramas a desplazar en todos los videos de entrada. Se usa para generar videos más largos por segmentos. Conéctalo a la salida `video_frame_offset` del nodo anterior para extender un video. (predeterminado: 0, paso: 1) | INT | Sí | 0 a MAX_RESOLUTION |

**Restricciones de parámetros:**

- Cuando se proporciona `pose_video`, un video de pose más corto se rellena con su último fotograma para igualar `length`. El código fuente contiene una marca `trim_to_pose_video`, actualmente deshabilitada, que acortaría la salida para que coincidiera con la longitud del video de pose.
- `face_video` se redimensiona a 512x512 y se normaliza al rango de -1.0 a 1.0.
- `continue_motion` se limita a los últimos `continue_motion_max_frames` fotogramas. Cuando se usa `continue_motion`, `video_frame_offset` se reduce por el número de fotogramas tomados, pero nunca por debajo de 0.
- Los videos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) se desplazan según `video_frame_offset`. Si el desplazamiento es mayor o igual que su longitud, la entrada se ignora, excepto para una `character_mask` de un solo fotograma, que siempre se repite.
- Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo.
- Si no se proporciona `reference_image`, se usa una imagen negra (todos los ceros) como referencia.
- Si no se proporciona `continue_motion`, se usan fotogramas grises con valor de píxel 0.5 para la porción de movimiento.
- `width` y `height` usan un paso de 16; las dimensiones latentes correspondientes son `width / 8` y `height / 8`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado que siempre incluye la imagen latente concatenada y la máscara concatenada. Si se proporcionan `clip_vision_output`, `pose_video` o `face_video`, también se añaden sus valores. | CONDITIONING |
| `negative` | Condicionamiento negativo modificado que siempre incluye la imagen latente concatenada y la máscara concatenada. Si se proporcionan `clip_vision_output`, `pose_video` o `face_video`, también se añaden sus valores; los píxeles del video de rostro se establecen en -1.0. | CONDITIONING |
| `latent` | Tensor latente vacío inicializado con ceros, con forma `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Número de fotogramas latentes a recortar del inicio, correspondiente a los fotogramas latentes de la imagen de referencia. | INT |
| `trim_image` | Número de fotogramas de imagen a recortar del inicio, correspondiente a los fotogramas de movimiento de referencia. | INT |
| `video_frame_offset` | Desplazamiento de fotogramas actualizado para la generación de video por segmentos, igual al desplazamiento de entrada ajustado más la longitud generada. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/es.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
