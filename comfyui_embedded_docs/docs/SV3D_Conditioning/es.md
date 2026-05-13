> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/es.md)

El nodo SV3D_Conditioning prepara datos de condicionamiento para la generación de video 3D utilizando el modelo SV3D. Toma una imagen inicial y la procesa a través de los codificadores CLIP vision y VAE para crear condicionamiento positivo y negativo, junto con una representación latente. El nodo genera secuencias de elevación y acimut de cámara para la generación de video de múltiples fotogramas según el número especificado de fotogramas de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip_vision` | CLIP_VISION | Sí | - | El modelo de visión CLIP utilizado para codificar la imagen de entrada |
| `init_image` | IMAGE | Sí | - | La imagen inicial que sirve como punto de partida para la generación de video 3D |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar la imagen en el espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) |
| `video_frames` | INT | No | 1 a 4096 | El número de fotogramas a generar para la secuencia de video (predeterminado: 21) |
| `elevation` | FLOAT | No | -90.0 a 90.0 | El ángulo de elevación de la cámara en grados para la vista 3D (predeterminado: 0.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | Los datos de condicionamiento positivo que contienen embeddings de imagen y parámetros de cámara para la generación |
| `negative` | CONDITIONING | Los datos de condicionamiento negativo con embeddings puestos a cero para generación contrastiva |
| `latent` | LATENT | Un tensor latente vacío con dimensiones que coinciden con los fotogramas de video y la resolución especificados |

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
