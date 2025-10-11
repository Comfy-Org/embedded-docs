> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/es.md)

El nodo SVD_img2vid_Conditioning prepara los datos de condicionamiento para la generación de videos utilizando Stable Video Diffusion. Toma una imagen inicial y la procesa a través de codificadores CLIP vision y VAE para crear pares de condicionamiento positivo y negativo, junto con un espacio latente vacío para la generación de video. Este nodo configura los parámetros necesarios para controlar el movimiento, la tasa de cuadros y los niveles de aumento en el video generado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sí | - | Modelo CLIP vision para codificar la imagen de entrada |
| `init_image` | IMAGE | Sí | - | Imagen inicial que se utilizará como punto de partida para la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para codificar la imagen en el espacio latente |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida (predeterminado: 1024, paso: 8) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Altura del video de salida (predeterminado: 576, paso: 8) |
| `video_frames` | INT | Sí | 1 a 4096 | Número de cuadros a generar en el video (predeterminado: 14) |
| `motion_bucket_id` | INT | Sí | 1 a 1023 | Controla la cantidad de movimiento en el video generado (predeterminado: 127) |
| `fps` | INT | Sí | 1 a 1024 | Cuadros por segundo para el video generado (predeterminado: 6) |
| `augmentation_level` | FLOAT | Sí | 0.0 a 10.0 | Nivel de aumento de ruido a aplicar a la imagen de entrada (predeterminado: 0.0, paso: 0.01) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Datos de condicionamiento positivo que contienen incrustaciones de imagen y parámetros de video |
| `negative` | CONDITIONING | Datos de condicionamiento negativo con incrustaciones anuladas y parámetros de video |
| `latent` | LATENT | Tensor de espacio latente vacío listo para la generación de video |