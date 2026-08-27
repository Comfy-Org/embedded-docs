# CosmosPredict2ImageToVideoLatent

CosmosPredict2ImageToVideoLatent crea representaciones latentes de video a partir de imágenes para la generación de video. Puede generar un latente de video en blanco o incorporar imágenes de inicio y fin para crear secuencias de video con dimensiones y duración específicas. El nodo se encarga de codificar las imágenes en el formato de espacio latente adecuado para el procesamiento de video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 848, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas en la secuencia de video (predeterminado: 93, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | El número de secuencias de video a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imagen_inicial` | Imagen inicial opcional para la secuencia de video | IMAGE | No | - |
| `imagen_final` | Imagen final opcional para la secuencia de video | IMAGE | No | - |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo genera un latente de video en blanco. Cuando se proporciona una o ambas imágenes, se redimensionan a `width` y `height`, se codifican en el espacio latente y se colocan al inicio y/o al final de la secuencia de video, marcando las regiones correspondientes en la máscara de ruido para que se conserven durante la generación. El latente y la máscara resultantes se repiten `batch_size` veces.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | La representación latente de video generada que contiene la secuencia de video codificada | LATENT |
| `noise_mask` | Una máscara que indica qué partes del latente deben conservarse durante la generación. Solo está presente cuando se proporciona al menos una de `start_image` o `end_image`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
