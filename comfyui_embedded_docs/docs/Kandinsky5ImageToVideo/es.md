# Kandinsky5ImageToVideo

El nodo Kandinsky5ImageToVideo prepara los datos de condicionamiento y del espacio latente para la generación de video con el modelo Kandinsky. Crea un tensor latente de video vacío y, opcionalmente, puede codificar una imagen inicial para guiar los primeros fotogramas del video generado, modificando el condicionamiento positivo y negativo en consecuencia.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Las indicaciones de condicionamiento positivo que guían la generación de video. | CONDITIONING | Sí | N/A |
| `negative` | Las indicaciones de condicionamiento negativo que alejan la generación de video de ciertos conceptos. | CONDITIONING | Sí | N/A |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial opcional en el espacio latente. | VAE | Sí | N/A |
| `width` | El ancho del video de salida en píxeles (predeterminado: 768). | INT | Sí | 16 a 8192 (paso 16) |
| `height` | La altura del video de salida en píxeles (predeterminado: 512). | INT | Sí | 16 a 8192 (paso 16) |
| `length` | El número de fotogramas del video (predeterminado: 121). | INT | Sí | 1 a 8192 (paso 4) |
| `batch_size` | El número de secuencias de video a generar simultáneamente (predeterminado: 1). | INT | Sí | 1 a 4096 |
| `start_image` | Una imagen inicial opcional. Si se proporciona, se codifica y se utiliza para reemplazar el inicio ruidoso de los latentes de salida del modelo. | IMAGE | No | N/A |

**Nota:** cuando se proporciona una `start_image`, se redimensiona para que coincida con el `width` y `height` especificados mediante interpolación bilineal. Solo se utilizan los primeros `length` fotogramas de la imagen para la codificación. El latente codificado se inyecta luego en el condicionamiento `positive` y `negative`, junto con una máscara que marca los fotogramas iniciales, de modo que la imagen codificada limpia reemplaza el comienzo ruidoso del video generado.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado, posiblemente actualizado con los datos de la imagen inicial codificada. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, posiblemente actualizado con los datos de la imagen inicial codificada. | CONDITIONING |
| `latent` | Un tensor latente de video vacío relleno de ceros, con la forma especificada por `batch_size`, `length`, `height` y `width`. | LATENT |
| `cond_latent` | La representación latente codificada y limpia de las imágenes iniciales proporcionadas. Se utiliza para reemplazar el inicio ruidoso de los latentes de salida del modelo. Vacía cuando no se proporciona `start_image`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
