# WanAnimateToVideo

El nodo WanAnimateToVideo genera contenido de video combinando múltiples entradas de condicionamiento, incluyendo referencias de pose, expresiones faciales y elementos de fondo. Procesa diversas entradas de video para crear secuencias animadas coherentes, manteniendo la consistencia temporal entre fotogramas. El nodo maneja operaciones en el espacio latente y puede extender videos existentes continuando patrones de movimiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamiento positivo para guiar la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | Condicionamiento negativo para alejar la generación de contenido no deseado | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar y decodificar datos de imagen | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `duración` | Número de fotogramas a generar (predeterminado: 77, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `salida_visión_clip` | Salida opcional del modelo de visión CLIP para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `imagen_referencia` | Imagen de referencia utilizada como punto de partida para la generación | IMAGE | No | - |
| `video_rostro` | Entrada de video que proporciona guía de expresiones faciales | IMAGE | No | - |
| `video_pose` | Entrada de video que proporciona guía de pose y movimiento | IMAGE | No | - |
| `máximo_fotogramas_continuación_movimiento` | Número máximo de fotogramas a continuar desde el movimiento anterior (predeterminado: 5, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `video_fondo` | Video de fondo para componer con el contenido generado | IMAGE | No | - |
| `máscara_personaje` | Máscara que define regiones del personaje para procesamiento selectivo | MASK | No | - |
| `continuar_movimiento` | Secuencia de movimiento anterior para continuar, garantizando consistencia temporal | IMAGE | No | - |
| `desplazamiento_fotograma_video` | Cantidad de fotogramas a desplazar en todos los videos de entrada. Se utiliza para generar videos más largos por fragmentos. Conéctelo a la salida `desplazamiento_fotograma_video` del nodo anterior para extender un video. (predeterminado: 0, paso: 1) | INT | Sí | 0 a MAX_RESOLUTION |

**Restricciones de Parámetros:**

- Cuando se proporciona `pose_video`, la longitud de salida se ajustará para coincidir con la duración del video de pose si la lógica `trim_to_pose_video` está activa (actualmente configurada como `False` en el código fuente)
- `face_video` se redimensiona automáticamente a resolución 512x512 y se normaliza a un rango de -1.0 a 1.0 al procesarse
- Los fotogramas de `continue_motion` están limitados por el parámetro `continue_motion_max_frames`; solo se utilizan los últimos `continue_motion_max_frames` fotogramas de la entrada
- Los videos de entrada (`face_video`, `pose_video`, `background_video`, `character_mask`) se desplazan según `video_frame_offset` antes del procesamiento; si el desplazamiento supera la duración del video, la entrada se ignora
- Si `character_mask` contiene solo un fotograma, se repetirá en todos los fotogramas
- Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo
- Si no se proporciona `reference_image`, se utiliza una imagen negra (todos ceros) como referencia predeterminada
- Si no se proporciona `continue_motion`, los fotogramas iniciales se rellenan con ruido gris (intensidad 0.5)

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo modificado con contexto de video adicional que incluye salida de visión CLIP, latente de video de pose, píxeles de video facial, imagen latente concatenada y máscara concatenada | CONDITIONING |
| `latente` | Condicionamiento negativo modificado con contexto de video adicional que incluye salida de visión CLIP, latente de video de pose, píxeles de video facial (invertidos), imagen latente concatenada y máscara concatenada | CONDITIONING |
| `recortar_latente` | Contenido de video generado en formato de espacio latente con forma [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] | LATENT |
| `recortar_imagen` | Información de recorte en espacio latente que indica la cantidad de fotogramas latentes a recortar desde el inicio (corresponde a los fotogramas latentes de la imagen de referencia) | INT |
| `desplazamiento_fotograma_video` | Información de recorte en espacio de imagen para fotogramas de movimiento de referencia, que indica la cantidad de fotogramas de imagen a recortar desde el inicio | INT |
| `desplazamiento_fotograma_video` | Desplazamiento de fotogramas actualizado para continuar la generación de video en fragmentos, calculado como el desplazamiento anterior más la longitud generada | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/es.md)

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
