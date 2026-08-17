# CosmosPredict2ImageToVideoLatent

El nodo CosmosPredict2ImageToVideoLatent crea representaciones latentes de video a partir de imágenes para la generación de video. Puede generar un latente de video en blanco o incorporar imágenes de inicio y fin para crear secuencias de video con dimensiones y duración especificadas. El nodo maneja la codificación de imágenes al formato de espacio latente apropiado para el procesamiento de video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `width` | El ancho del video de salida en píxeles (predeterminado: 848, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION (step 16) |
| `height` | El alto del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION (step 16) |
| `length` | El número de fotogramas en la secuencia de video (predeterminado: 93) | INT | Sí | 1 to MAX_RESOLUTION (step 4) |
| `batch_size` | El número de secuencias de video a generar (predeterminado: 1) | INT | Sí | 1 to 4096 |
| `start_image` | Imagen opcional de inicio para la secuencia de video | IMAGE | No | - |
| `end_image` | Imagen opcional de fin para la secuencia de video | IMAGE | No | - |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo genera un latente de video en blanco. Cuando se proporcionan imágenes, estas se codifican y se posicionan al principio y/o al final de la secuencia de video con el enmascaramiento adecuado.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | La representación latente de video generada que contiene la secuencia de video codificada | LATENT |
| `noise_mask` | Una máscara que indica qué partes del latente deben conservarse durante la generación | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
