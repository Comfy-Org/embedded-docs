# CosmosImageToVideoLatent

El nodo CosmosImageToVideoLatent crea un latent de video para la generación de imagen a video. Comienza con un latent vacío y, opcionalmente, puede codificar una imagen inicial y/o una imagen final en los primeros o últimos fotogramas de la secuencia de video. Cuando se proporcionan imágenes, también genera una máscara de ruido que marca los fotogramas codificados como fijos durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar las imágenes de entrada en el espacio latente | VAE | Sí | - |
| `width` | El ancho del video de salida en píxeles (predeterminado: 1280) | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `height` | La altura del video de salida en píxeles (predeterminado: 704) | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `length` | El número de fotogramas en la secuencia de video (predeterminado: 121) | INT | Sí | 1 a MAX_RESOLUTION (paso 8) |
| `batch_size` | El número de latents de video a generar en el lote de salida (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `start_image` | Imagen opcional o secuencia de imágenes a codificar al inicio de la secuencia de video | IMAGE | No | - |
| `end_image` | Imagen opcional o secuencia de imágenes a codificar al final de la secuencia de video | IMAGE | No | - |

**Nota:** Cuando no se proporciona ni `start_image` ni `end_image`, el nodo devuelve un latent vacío sin máscara de ruido. Cuando se proporciona al menos una imagen, se incluye una `noise_mask`: los fotogramas latentes codificados a partir de las imágenes suministradas tienen valor de máscara 0 (se mantienen fijos), mientras que los fotogramas restantes tienen valor de máscara 1 (se generarán). Las imágenes se redimensionan al `width` y `height` objetivo antes de codificarse, y el número de fotogramas tomados de una imagen de entrada es igual a su dimensión de lote, hasta un máximo de `length`. El latent tiene 16 canales, dimensiones espaciales `width / 8` y `height / 8`, y `((length - 1) // 8) + 1` fotogramas. Cuando se proporcionan imágenes, el latent y su máscara de ruido se repiten `batch_size` veces para formar el lote de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latent` | Un LATENT que contiene las `samples` del latent de video y, cuando se proporciona `start_image` o `end_image`, una `noise_mask` que marca los fotogramas codificados como fijos | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
