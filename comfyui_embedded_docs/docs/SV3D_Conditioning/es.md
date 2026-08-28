# SV3D_Acondicionamiento

SV3D_Conditioning prepara los datos de condicionamiento para la generación de videos 3D utilizando el modelo SV3D. Toma una imagen inicial y la procesa a través de los codificadores CLIP vision y VAE para crear un condicionamiento positivo y negativo, junto con una representación latente. El nodo genera secuencias de elevación y acimut de cámara para la generación de videos de múltiples fotogramas según el número especificado de fotogramas de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip_vision` | El modelo de visión CLIP utilizado para codificar la imagen de entrada | CLIP_VISION | Sí | - |
| `imagen_inicial` | La imagen inicial que sirve como punto de partida para la generación de videos 3D | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | La altura de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) | INT | Sí | 16 a MAX_RESOLUTION |
| `cuadros_de_video` | El número de fotogramas a generar para la secuencia de video (predeterminado: 21) | INT | Sí | 1 a 4096 |
| `elevación` | El ángulo de elevación de la cámara en grados para la vista 3D (predeterminado: 0.0) | FLOAT | Sí | -90.0 a 90.0 |

Nota: El acimut de la cámara comienza en 0 grados y aumenta en una cantidad constante por cada fotograma, de modo que la cámara completa una órbita de 360 grados alrededor del objeto a lo largo de los fotogramas generados. El valor de `elevation` permanece constante para cada fotograma.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Los datos de condicionamiento positivo que contienen los embeddings de imagen y los parámetros de cámara para la generación | CONDITIONING |
| `negativo` | Los datos de condicionamiento negativo con los embeddings y los latentes puestos a cero para la generación contrastiva | CONDITIONING |
| `latente` | Un tensor latente vacío con dimensiones que coinciden con los fotogramas de video y la resolución especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
