# EmptySD3LatentImage

El nodo EmptySD3LatentImage crea un tensor de imagen latente en blanco específicamente formateado para los modelos Stable Diffusion 3. Genera un tensor relleno de ceros con las dimensiones y la estructura correctas que esperan los pipelines de SD3. Se utiliza comúnmente como punto de partida para flujos de trabajo de generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho de la imagen latente de salida en píxeles (predeterminado: 1024) | INT | Sí | 16 to MAX_RESOLUTION (step: 16) |
| `height` | La altura de la imagen latente de salida en píxeles (predeterminado: 1024) | INT | Sí | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | El número de imágenes latentes a generar en un lote (predeterminado: 1) | INT | Sí | 1 to 4096 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | Un tensor latente que contiene muestras en blanco con dimensiones compatibles con SD3. El tensor tiene 16 canales y está reducido espacialmente por un factor de 8 en comparación con el ancho y alto de entrada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/es.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
