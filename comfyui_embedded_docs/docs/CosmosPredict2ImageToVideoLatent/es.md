El nodo CosmosPredict2ImageToVideoLatent crea representaciones latentes de video a partir de imágenes para la generación de video. Puede generar un video latente en blanco o incorporar imágenes de inicio y final para crear secuencias de video con dimensiones y duración específicas. El nodo maneja la codificación de imágenes al formato de espacio latente adecuado para el procesamiento de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 848, debe ser divisible por 16) | INT | No | 16 a MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) | INT | No | 16 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas en la secuencia de video (predeterminado: 93, paso: 4) | INT | No | 1 a MAX_RESOLUTION |
| `tamaño_del_lote` | El número de secuencias de video a generar (predeterminado: 1) | INT | No | 1 a 4096 |
| `imagen_inicial` | Imagen de inicio opcional para la secuencia de video | IMAGE | No | - |
| `imagen_final` | Imagen final opcional para la secuencia de video | IMAGE | No | - |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo genera un video latente en blanco. Cuando se proporcionan imágenes, estas se codifican y se posicionan al inicio y/o al final de la secuencia de video con el enmascaramiento adecuado.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | La representación latente del video generado que contiene la secuencia de video codificada | LATENT |
| `noise_mask` | Una máscara que indica qué partes del latente deben conservarse durante la generación | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `55fab16180c0e3fa254bcc77694dbc666810b28522e61b9c613f720fae66bd0c`
