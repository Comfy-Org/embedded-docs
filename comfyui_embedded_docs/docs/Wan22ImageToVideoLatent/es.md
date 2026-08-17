# Wan22ImageToVideoLatent

El nodo Wan22ImageToVideoLatent prepara la entrada latente utilizada para la generación de video Wan 2.2. Crea un video latente vacío con el ancho, la altura y el número de fotogramas especificados y, cuando se proporciona una imagen inicial, codifica esa imagen en los primeros fotogramas del latente. También genera una máscara de ruido que indica qué fotogramas ya están completados por la imagen y cuáles aún deben generarse.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial en el espacio latente | VAE | Sí | - |
| `width` | El ancho del video de salida en píxeles (predeterminado: 1280, paso: 32) | INT | Sí | 32 to MAX_RESOLUTION |
| `height` | La altura del video de salida en píxeles (predeterminado: 704, paso: 32) | INT | Sí | 32 to MAX_RESOLUTION |
| `length` | El número de fotogramas del video (predeterminado: 49, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | La cantidad de videos latentes a generar en paralelo (predeterminado: 1) | INT | Sí | 1 to 4096 |
| `start_image` | Imagen o secuencia de imágenes opcional que se coloca en los primeros fotogramas del video latente. Solo se utilizan los primeros fotogramas de `length`. La imagen se redimensiona a `width` x `height` con remuestreo bilineal y recorte centrado antes de ser codificada por el VAE. | IMAGE | No | - |

**Nota:** Las dimensiones espaciales del latente son `width / 16` y `height / 16`, por lo que `width` y `height` deben ser divisibles entre 16. La dimensión temporal del latente se calcula como `((length - 1) // 4) + 1` y tiene 48 canales. Cuando se proporciona un `start_image`, la imagen codificada llena los primeros fotogramas del latente y la `noise_mask` se establece en 0 para esos fotogramas y en 1 para los restantes, lo que indica al muestreador que mantenga los fotogramas de la imagen sin cambios y genere el resto. Cuando no se proporciona `start_image`, el latente se llena con ceros y no se incluye ninguna máscara de ruido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | El video latente generado, repetido `batch_size` veces. Cuando se proporciona un `start_image`, también contiene una `noise_mask` que marca los fotogramas codificados por la imagen (0) y los fotogramas a generar (1). | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
