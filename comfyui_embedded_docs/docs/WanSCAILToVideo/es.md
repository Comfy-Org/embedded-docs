# WanSCAILToVideo

El nodo WanSCAILToVideo prepara el condicionamiento y un espacio latente vacío para la generación de video con los modelos de video SCAIL y SCAIL-2. Procesa entradas opcionales como imágenes de referencia, videos de pose, salidas de CLIP Vision, máscaras de identidad coloreadas y fragmentos de fotogramas anteriores, incrustándolas en el condicionamiento positivo y negativo. El nodo devuelve el condicionamiento modificado y un tensor latente en blanco con las dimensiones de video especificadas, listo para el muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `positivo` | La entrada de condicionamiento positivo. | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar imágenes y fotogramas de video. | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (por defecto: 512). Los valores aumentan de 32 en 32. | INT | Sí | 32 a MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles (por defecto: 896). Los valores aumentan de 32 en 32. | INT | Sí | 32 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas del video (por defecto: 81). Los valores aumentan de 4 en 4. | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | El número de videos a generar en un lote (por defecto: 1). | INT | Sí | 1 a 4096 |
| `video_pose` | Video utilizado para el condicionamiento de pose. Se reducirá a la mitad de la resolución del video principal. | IMAGE | No | - |
| `pose_video_mask` | Solo SCAIL-2. Video de máscara SAM3 coloreada por identidad, a la misma resolución que `pose_video`. | IMAGE | No | - |
| `replacement_mode` | Solo SCAIL-2. False = Modo de animación (`pose_video_mask` debe tener fondo negro). True = Modo de reemplazo (`pose_video_mask` debe tener fondo blanco). (por defecto: False) | BOOLEAN | No | - |
| `fuerza_pose` | Fuerza del latente de pose. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 10.0 |
| `inicio_pose` | Paso inicial del condicionamiento de pose. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 |
| `fin_pose` | Paso final del condicionamiento de pose. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `imagen_referencia` | Imagen de referencia. La primera imagen es la referencia principal (componga todas las identidades sobre ella). SCAIL-2: las imágenes adicionales del lote se usan como vistas adicionales (vista trasera, primer plano, fondo ocluido), y cada una necesita una `reference_image_mask` correspondiente en el color de esa identidad. | IMAGE | No | - |
| `reference_image_mask` | Solo SCAIL-2. Máscara de referencia coloreada, cuyo lote coincide con `reference_image` (la primera es la máscara de referencia principal; el resto son máscaras de identidad para las `reference_image` adicionales). | IMAGE | No | - |
| `clip_vision_output` | Características de CLIP Vision para el condicionamiento. El modelo está entrenado con un redimensionamiento por estiramiento para ajustarse a la relación de aspecto. | CLIP_VISION_OUTPUT | No | - |
| `video_frame_offset` | Fotograma de salida acumulado en el que comienza este fragmento. Conéctalo desde la salida `video_frame_offset` del fragmento anterior. (por defecto: 0) | INT | Sí | 0 a MAX_RESOLUTION |
| `previous_frame_count` | Fotogramas finales de `previous_frames` que se usan como ancla. SCAIL-2 se entrenó con 5 (fragmentos de 81 fotogramas, paso de 76 fotogramas). (por defecto: 5) | INT | Sí | 1 a MAX_RESOLUTION |
| `previous_frames` | Solo SCAIL-2. Salida decodificada completa del fragmento anterior. Solo los últimos `previous_frame_count` se usan como ancla de extensión. | IMAGE | No | - |

**Nota:** Las entradas `pose_video` y `pose_video_mask` se recortan juntas hasta la más corta de las dos, y se procesan solo para los primeros `length` fotogramas. Si cualquiera de las dos entradas es más corta o igual que `video_frame_offset`, se ignora por completo. El `pose_video` se reduce a la mitad de la resolución del video principal antes de codificarse, y el latente de pose codificado se multiplica por `pose_strength` y se aplica al condicionamiento solo entre los pasos de timestep `pose_start` y `pose_end`. Si se proporciona `pose_video_mask`, el video de máscara coloreada se reduce a la mitad de la resolución y se convierte en una máscara de conducción de 28 canales, que se añade tanto al condicionamiento positivo como al negativo.

**Nota:** Cuando se proporciona `reference_image`, cada imagen del lote se codifica individualmente en un latente y se incrusta tanto en el condicionamiento positivo como en el negativo. La primera imagen es la referencia principal; las imágenes adicionales se utilizan como vistas adicionales, y cada una necesita una `reference_image_mask` correspondiente. `reference_image_mask` solo se usa cuando también se proporciona `reference_image`; cuando se proporcionan ambas, también se crea una máscara de referencia de 28 canales que vincula los fotogramas de referencia con las identidades, y se añade al condicionamiento. En el modo de reemplazo (`replacement_mode=True`), la imagen de referencia se compone sobre un fondo negro usando la máscara de imagen de referencia como matte alfa. Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo.

**Nota:** Cuando se proporciona `previous_frames`, solo los últimos `previous_frame_count` fotogramas se usan como ancla de extensión, y `video_frame_offset` se ajusta en consecuencia (se reduce en el número de fotogramas anclados, limitado a 0). Los fotogramas anclados se codifican y se escriben al inicio del latente de salida, y se incluye una máscara de ruido para que esos fotogramas se mantengan sin cambios durante la generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | El condicionamiento positivo modificado, que puede contener latentes de imagen de referencia incrustados, salida de CLIP Vision, latentes de pose del video, máscaras de conducción, máscaras de referencia o latentes de fotogramas anteriores. | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado, que puede contener latentes de imagen de referencia incrustados, salida de CLIP Vision, latentes de pose del video, máscaras de conducción, máscaras de referencia o latentes de fotogramas anteriores. | CONDITIONING |
| `latente` | Un tensor latente vacío con forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Cuando se proporciona `previous_frames`, el latente se rellena parcialmente con fotogramas anteriores codificados y se incluye una máscara de ruido. | LATENT |
| `video_frame_offset` | Offset ajustado + longitud. Conéctalo al siguiente fragmento para la generación secuencial de video. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/es.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
