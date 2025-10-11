> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/es.md)

El nodo SV3D_Conditioning prepara datos de condicionamiento para la generación de video 3D utilizando el modelo SV3D. Toma una imagen inicial y la procesa a través de codificadores CLIP vision y VAE para crear condicionamiento positivo y negativo, junto con una representación latente. El nodo genera secuencias de elevación y azimut de cámara para la generación de video multiframe según el número especificado de fotogramas de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sí | - | El modelo CLIP vision utilizado para codificar la imagen de entrada |
| `init_image` | IMAGE | Sí | - | La imagen inicial que sirve como punto de partida para la generación de video 3D |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen en el espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho de salida para los fotogramas de video generados (por defecto: 576, debe ser divisible por 8) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura de salida para los fotogramas de video generados (por defecto: 576, debe ser divisible por 8) |
| `video_frames` | INT | No | 1 a 4096 | El número de fotogramas a generar para la secuencia de video (por defecto: 21) |
| `elevation` | FLOAT | No | -90.0 a 90.0 | El ángulo de elevación de la cámara en grados para la vista 3D (por defecto: 0.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Los datos de condicionamiento positivo que contienen incrustaciones de imagen y parámetros de cámara para la generación |
| `negative` | CONDITIONING | Los datos de condicionamiento negativo con incrustaciones puestas a cero para generación contrastiva |
| `latent` | LATENT | Un tensor latente vacío con dimensiones que coinciden con los fotogramas de video y resolución especificados |