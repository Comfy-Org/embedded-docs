> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/es.md)

El nodo WanAnimateToVideo genera contenido de video combinando múltiples entradas de condicionamiento, incluyendo referencias de pose, expresiones faciales y elementos de fondo. Procesa diversas entradas de video para crear secuencias animadas coherentes, manteniendo la consistencia temporal entre fotogramas. El nodo maneja operaciones en el espacio latente y puede extender videos existentes continuando patrones de movimiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Condicionamiento positivo para guiar la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | Condicionamiento negativo para alejar la generación de contenido no deseado |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar y decodificar datos de imagen |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) |
| `duración` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas a generar (predeterminado: 77, paso: 4) |
| `tamaño_lote` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `salida_visión_clip` | CLIP_VISION_OUTPUT | No | - | Salida opcional del modelo de visión CLIP para condicionamiento adicional |
| `imagen_referencia` | IMAGE | No | - | Imagen de referencia utilizada como punto de partida para la generación |
| `video_rostro` | IMAGE | No | - | Entrada de video que proporciona guía de expresiones faciales |
| `video_pose` | IMAGE | No | - | Entrada de video que proporciona guía de pose y movimiento |
| `máximo_fotogramas_continuación_movimiento` | INT | Sí | 1 a MAX_RESOLUTION | Número máximo de fotogramas a continuar desde el movimiento anterior (predeterminado: 5, paso: 4) |
| `video_fondo` | IMAGE | No | - | Video de fondo para componer con el contenido generado |
| `máscara_personaje` | MASK | No | - | Máscara que define regiones del personaje para procesamiento selectivo |
| `continuar_movimiento` | IMAGE | No | - | Secuencia de movimiento anterior para continuar, garantizando consistencia temporal |
| `desplazamiento_fotograma_video` | INT | Sí | 0 a MAX_RESOLUTION | Cantidad de fotogramas a desplazar en todos los videos de entrada. Se utiliza para generar videos más largos por fragmentos. Conéctelo a la salida `desplazamiento_fotograma_video` del nodo anterior para extender un video. (predeterminado: 0, paso: 1) |

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

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | Condicionamiento positivo modificado con contexto de video adicional que incluye salida de visión CLIP, latente de video de pose, píxeles de video facial, imagen latente concatenada y máscara concatenada |
| `latente` | CONDITIONING | Condicionamiento negativo modificado con contexto de video adicional que incluye salida de visión CLIP, latente de video de pose, píxeles de video facial (invertidos), imagen latente concatenada y máscara concatenada |
| `recortar_latente` | LATENT | Contenido de video generado en formato de espacio latente con forma [batch_size, 16, latent_length + trim_latent, latent_height, latent_width] |
| `recortar_imagen` | INT | Información de recorte en espacio latente que indica la cantidad de fotogramas latentes a recortar desde el inicio (corresponde a los fotogramas latentes de la imagen de referencia) |
| `desplazamiento_fotograma_video` | INT | Información de recorte en espacio de imagen para fotogramas de movimiento de referencia, que indica la cantidad de fotogramas de imagen a recortar desde el inicio |
| `desplazamiento_fotograma_video` | INT | Desplazamiento de fotogramas actualizado para continuar la generación de video en fragmentos, calculado como el desplazamiento anterior más la longitud generada |

---
**Source fingerprint (SHA-256):** `c2ca90f4963f629d51cdd7f4bdb67e01c32ce5ca7d916b1f992ccd220f57566c`
