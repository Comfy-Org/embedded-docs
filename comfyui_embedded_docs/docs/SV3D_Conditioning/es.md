# SV3D_Acondicionamiento

El nodo SV3D_Conditioning prepara los datos de condicionamiento para la generación de video 3D utilizando el modelo SV3D. Toma una imagen inicial y la procesa a través de los codificadores de visión CLIP y VAE para crear un condicionamiento positivo y negativo, junto con una representación latente. El nodo genera secuencias de elevación y azimut de cámara para la generación de video de múltiples fotogramas según el número de fotogramas de video especificado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `clip_vision` | El modelo de visión CLIP utilizado para codificar la imagen de entrada | CLIP_VISION | Sí | - |
| `init_image` | La imagen inicial que sirve como punto de partida para la generación de video 3D | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen en el espacio latente | VAE | Sí | - |
| `width` | El ancho de salida para los fotogramas de video generados (por defecto: 576, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION (paso de 8) |
| `height` | El alto de salida para los fotogramas de video generados (por defecto: 576, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION (paso de 8) |
| `video_frames` | El número de fotogramas a generar para la secuencia de video (por defecto: 21) | INT | Sí | 1 a 4096 |
| `elevation` | El ángulo de elevación de la cámara en grados para la vista 3D, aplicado a cada fotograma (por defecto: 0.0) | FLOAT | Sí | -90.0 a 90.0 (paso de 0.1) |

Nota: El azimut de la cámara comienza en 0 grados y aumenta 360 / (video_frames - 1) grados por fotograma, por lo que la cámara completa una órbita completa alrededor del objeto a lo largo de la secuencia. El mismo valor de `elevation` se aplica a todos los fotogramas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positive` | Los datos de condicionamiento positivo que contienen incrustaciones de imagen y parámetros de cámara para la generación | CONDITIONING |
| `negative` | Los datos de condicionamiento negativo con incrustaciones puestas a cero para la generación contrastiva | CONDITIONING |
| `latent` | Un tensor latente vacío con dimensiones que coinciden con los fotogramas de video y la resolución especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
