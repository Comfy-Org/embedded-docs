# SV3D_Acondicionamiento

El nodo SV3D_Conditioning prepara datos de condicionamiento para la generación de video 3D utilizando el modelo SV3D. Toma una imagen inicial y la procesa a través de los codificadores CLIP vision y VAE para crear condicionamiento positivo y negativo, junto con una representación latente. El nodo genera secuencias de elevación y acimut de cámara para la generación de video de múltiples fotogramas según el número especificado de fotogramas de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip_vision` | El modelo de visión CLIP utilizado para codificar la imagen de entrada | CLIP_VISION | Sí | - |
| `imagen_inicial` | La imagen inicial que sirve como punto de partida para la generación de video 3D | IMAGE | Sí | - |
| `vae` | El modelo VAE utilizado para codificar la imagen en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) | INT | No | 16 a MAX_RESOLUTION |
| `altura` | La altura de salida para los fotogramas de video generados (predeterminado: 576, debe ser divisible por 8) | INT | No | 16 a MAX_RESOLUTION |
| `cuadros_de_video` | El número de fotogramas a generar para la secuencia de video (predeterminado: 21) | INT | No | 1 a 4096 |
| `elevación` | El ángulo de elevación de la cámara en grados para la vista 3D (predeterminado: 0.0) | FLOAT | No | -90.0 a 90.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | Los datos de condicionamiento positivo que contienen embeddings de imagen y parámetros de cámara para la generación | CONDITIONING |
| `negativo` | Los datos de condicionamiento negativo con embeddings puestos a cero para generación contrastiva | CONDITIONING |
| `latente` | Un tensor latente vacío con dimensiones que coinciden con los fotogramas de video y la resolución especificados | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `be02939aa4cdd1785eb445034a27d08a90e390a497fa9697fb769f0ce26e6d2f`
