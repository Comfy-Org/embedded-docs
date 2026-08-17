# WanSCAILToVideo

El nodo WanSCAILToVideo prepara el condicionamiento y un espacio latente vacío para la generación de video. Procesa entradas opcionales como imágenes de referencia, videos de pose, salidas de CLIP vision y fragmentos de fotogramas anteriores, incrustándolas en el condicionamiento positivo y negativo para un modelo de video. El nodo genera el condicionamiento modificado y un tensor latente vacío con las dimensiones de video especificadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `positive` | La entrada de condicionamiento positivo. | CONDITIONING | Sí | - |
| `negative` | La entrada de condicionamiento negativo. | CONDITIONING | Sí | - |
| `vae` | El modelo VAE utilizado para codificar imágenes y fotogramas de video. | VAE | Sí | - |
| `width` | El ancho del video de salida en píxeles (por defecto: 512). Ajustable en incrementos de 32. | INT | Sí | 32 to MAX_RESOLUTION |
| `height` | La altura del video de salida en píxeles (por defecto: 896). Ajustable en incrementos de 32. | INT | Sí | 32 to MAX_RESOLUTION |
| `length` | El número de fotogramas del video (por defecto: 81). Ajustable en incrementos de 4 a partir de 1. | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | El número de videos a generar en un lote (por defecto: 1). | INT | Sí | 1 to 4096 |
| `pose_strength` | Fuerza del latente de pose (por defecto: 1.0). | FLOAT | Sí | 0.0 to 10.0 |
| `pose_start` | Paso inicial del condicionamiento de pose (por defecto: 0.0). | FLOAT | Sí | 0.0 to 1.0 |
| `pose_end` | Paso final del condicionamiento de pose (por defecto: 1.0). | FLOAT | Sí | 0.0 to 1.0 |
| `video_frame_offset` | Fotograma de salida acumulado en el que comienza este fragmento. Conéctelo desde la salida `video_frame_offset` del fragmento anterior (por defecto: 0). | INT | Sí | 0 to MAX_RESOLUTION |
| `previous_frame_count` | Fotogramas finales de `previous_frames` para anclar. SCAIL-2 se entrenó con 5 (fragmentos de 81 fotogramas, paso de 76 fotogramas) (por defecto: 5). | INT | Sí | 1 to MAX_RESOLUTION |
| `pose_video` | Video utilizado para el condicionamiento de pose. Se reducirá a la mitad de la resolución del video principal. | IMAGE | No | - |
| `pose_video_mask` | Solo SCAIL-2. Video de máscara SAM3 coloreado por identidad, a la misma resolución que `pose_video`. | IMAGE | No | - |
| `replacement_mode` | Solo SCAIL-2. False = Modo de animación (`pose_video_mask` debe tener fondo negro). True = Modo de reemplazo (`pose_video_mask` debe tener fondo blanco). Por defecto: False. | BOOLEAN | No | - |
| `reference_image` | Imagen de referencia. La primera imagen es la referencia principal (componga todas las identidades sobre ella). SCAIL-2: las imágenes adicionales del lote se utilizan como vistas adicionales (vista trasera, primer plano, fondo ocluido), y cada una necesita una `reference_image_mask` correspondiente en el color de esa identidad. | IMAGE | No | - |
| `reference_image_mask` | Solo SCAIL-2. Máscara de referencia coloreada, cuyo lote coincide con `reference_image` (la primera = máscara de referencia principal; el resto = máscaras de identidad para las `reference_image` adicionales). | IMAGE | No | - |
| `clip_vision_output` | Características de CLIP vision para el condicionamiento. El modelo se entrena con un redimensionamiento por estiramiento hasta la relación de aspecto. | CLIP_VISION_OUTPUT | No | - |
| `previous_frames` | Solo SCAIL-2. Salida decodificada completa del fragmento anterior. Solo los últimos `previous_frame_count` fotogramas se utilizan como ancla de extensión. | IMAGE | No | - |

**Nota:**

- Las entradas `pose_video` y `pose_video_mask` se cortan a partir de `video_frame_offset`; si el video no tiene fotogramas más allá de ese desplazamiento, dicha entrada se ignora. Luego se truncan juntas hasta la más corta de las dos y se limitan a `length` fotogramas. `pose_video` se reduce a la mitad de la resolución del video principal antes de codificarse.
- La entrada `reference_image_mask` solo se aplica cuando también se proporciona `reference_image`. Cada imagen del lote de `reference_image` se codifica individualmente como una referencia latente de un solo fotograma. En el modo de reemplazo (`replacement_mode=True`), las imágenes de referencia se componen sobre un fondo negro utilizando la máscara de imagen de referencia como matte alfa.
- Cuando se proporciona `clip_vision_output`, se aplica tanto al condicionamiento positivo como al negativo.
- Cuando se proporciona `previous_frames`, solo los últimos `previous_frame_count` fotogramas se utilizan como ancla de extensión. El latente de salida se rellena parcialmente con la codificación de estos fotogramas, se incluye una máscara de ruido en el latente de salida y `video_frame_offset` se ajusta restando el número de fotogramas conservados (nunca por debajo de 0).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | El condicionamiento positivo modificado, que potencialmente contiene latentes de imagen de referencia incrustados, salida de CLIP vision, latentes de video de pose, máscaras de conducción, máscaras de referencia o latentes de fotogramas anteriores. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, que potencialmente contiene latentes de imagen de referencia incrustados, salida de CLIP vision, latentes de video de pose, máscaras de conducción, máscaras de referencia o latentes de fotogramas anteriores. | CONDITIONING |
| `latent` | Un tensor latente vacío con forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Cuando se proporciona `previous_frames`, el latente se rellena parcialmente con fotogramas anteriores codificados y se incluye una máscara de ruido. | LATENT |
| `video_frame_offset` | Desplazamiento ajustado + `length`. Conéctelo al siguiente fragmento para la generación secuencial de video. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/es.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
