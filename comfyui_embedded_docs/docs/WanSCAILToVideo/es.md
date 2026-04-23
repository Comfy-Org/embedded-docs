> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/es.md)

El nodo WanSCAILToVideo prepara el acondicionamiento y un espacio latente vacío para la generación de video. Procesa entradas opcionales como imágenes de referencia, videos de pose y salidas de visión CLIP, integrándolas en el acondicionamiento positivo y negativo para un modelo de video. El nodo devuelve el acondicionamiento modificado y un tensor latente en blanco con las dimensiones de video especificadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de acondicionamiento positivo. |
| `negative` | CONDITIONING | Sí | - | La entrada de acondicionamiento negativo. |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar imágenes y fotogramas de video. |
| `width` | INT | Sí | 32 a MAX_RESOLUTION | El ancho del video de salida en píxeles (por defecto: 512). Debe ser divisible por 8. |
| `height` | INT | Sí | 32 a MAX_RESOLUTION | La altura del video de salida en píxeles (por defecto: 896). Debe ser divisible por 8. |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | El número de fotogramas en el video (por defecto: 81). |
| `batch_size` | INT | Sí | 1 a 4096 | El número de videos a generar en un lote (por defecto: 1). |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para el acondicionamiento. |
| `reference_image` | IMAGE | No | - | Una imagen de referencia opcional para el acondicionamiento. |
| `pose_video` | IMAGE | No | - | Video utilizado para el acondicionamiento de pose. Se reducirá a la mitad de la resolución del video principal. |
| `pose_strength` | FLOAT | Sí | 0.0 a 10.0 | Intensidad del latente de pose (por defecto: 1.0). |
| `pose_start` | FLOAT | Sí | 0.0 a 1.0 | Paso inicial para usar el acondicionamiento de pose (por defecto: 0.0). |
| `pose_end` | FLOAT | Sí | 0.0 a 1.0 | Paso final para usar el acondicionamiento de pose (por defecto: 1.0). |

**Nota:** La entrada `pose_video` se procesa solo para los primeros `length` fotogramas. La `reference_image` se procesa solo para la primera imagen del lote.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El acondicionamiento positivo modificado, que potencialmente contiene latentes de imagen de referencia, salida de visión CLIP o latentes de video de pose incrustados. |
| `negative` | CONDITIONING | El acondicionamiento negativo modificado, que potencialmente contiene latentes de imagen de referencia, salida de visión CLIP o latentes de video de pose incrustados. |
| `latent` | LATENT | Un tensor latente vacío con la forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. |