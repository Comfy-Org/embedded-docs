> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/es.md)

El nodo Kandinsky5ImageToVideo prepara los datos de condicionamiento y espacio latente para la generación de video utilizando el modelo Kandinsky. Crea un tensor latente de video vacío y puede codificar opcionalmente una imagen de inicio para guiar los fotogramas iniciales del video generado, modificando el condicionamiento positivo y negativo en consecuencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | N/D | Los mensajes de condicionamiento positivo para guiar la generación del video. |
| `negative` | CONDITIONING | Sí | N/D | Los mensajes de condicionamiento negativo para alejar la generación del video de ciertos conceptos. |
| `vae` | VAE | Sí | N/D | El modelo VAE utilizado para codificar la imagen de inicio opcional en el espacio latente. |
| `width` | INT | No | 16 a 8192 (paso 16) | El ancho del video de salida en píxeles (predeterminado: 768). |
| `height` | INT | No | 16 a 8192 (paso 16) | La altura del video de salida en píxeles (predeterminado: 512). |
| `length` | INT | No | 1 a 8192 (paso 4) | El número de fotogramas en el video (predeterminado: 121). |
| `batch_size` | INT | No | 1 a 4096 | El número de secuencias de video a generar simultáneamente (predeterminado: 1). |
| `start_image` | IMAGE | No | N/D | Una imagen de inicio opcional. Si se proporciona, se codifica y se utiliza para reemplazar el inicio ruidoso de los latentes de salida del modelo. |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para que coincida con el `width` y `height` especificados mediante interpolación bilineal. Los primeros `length` fotogramas del lote de imágenes se utilizan para la codificación. El latente codificado se inyecta luego en el condicionamiento tanto `positive` como `negative` para guiar la apariencia inicial del video.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado, potencialmente actualizado con los datos de la imagen de inicio codificada. |
| `negative` | CONDITIONING | El condicionamiento negativo modificado, potencialmente actualizado con los datos de la imagen de inicio codificada. |
| `latent` | LATENT | Un tensor latente de video vacío con ceros, con forma para las dimensiones especificadas. |
| `cond_latent` | LATENT | La representación latente codificada y limpia de las imágenes de inicio proporcionadas. Se utiliza internamente para reemplazar el inicio ruidoso de los latentes del video generado. |

---
**Source fingerprint (SHA-256):** `19d3b60be18f5adcd659563329988bce2511a1b27b33fd0ab3a9d93e265557f2`
