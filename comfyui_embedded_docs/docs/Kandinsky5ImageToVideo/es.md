# Kandinsky5ImageToVideo

El nodo Kandinsky5ImageToVideo prepara los datos de condicionamiento y espacio latente para la generación de videos utilizando el modelo Kandinsky. Crea un tensor latente de video vacío y, opcionalmente, puede codificar una imagen inicial para guiar los primeros fotogramas del video generado, modificando el condicionamiento positivo y negativo en consecuencia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Las indicaciones de condicionamiento positivo que guían la generación del video. | CONDITIONING | Sí | N/A |
| `negativo` | Las indicaciones de condicionamiento negativo para alejar la generación del video de ciertos conceptos. | CONDITIONING | Sí | N/A |
| `vae` | El modelo VAE utilizado para codificar la imagen inicial opcional en el espacio latente. | VAE | Sí | N/A |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 768). | INT | Sí | 16 a 16384 (step 16) |
| `alto` | El alto del video de salida en píxeles (predeterminado: 512). | INT | Sí | 16 a 16384 (step 16) |
| `duración` | El número de fotogramas del video (predeterminado: 121). | INT | Sí | 1 a 16384 (step 4) |
| `tamaño_lote` | El número de secuencias de video a generar simultáneamente (predeterminado: 1). | INT | Sí | 1 a 4096 |
| `imagen_inicial` | Una imagen inicial opcional o un lote de fotogramas. Si se proporciona, se codifica y se utiliza para reemplazar el inicio ruidoso de los latentes de salida del modelo. | IMAGE | No | N/A |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para que coincida con las dimensiones `width` y `height` especificadas mediante interpolación bilineal. Solo los primeros `length` fotogramas del lote de imágenes se utilizan para la codificación; cualquier fotograma adicional se ignora. Si el lote de imágenes tiene menos de `length` fotogramas, solo se utilizan esos fotogramas. Solo se codifican los canales RGB de la imagen. El latente codificado se inyecta tanto en el condicionamiento `positive` como en el `negative` para guiar la apariencia inicial del video, y los fotogramas codificados limpios reemplazan el inicio ruidoso de los latentes de salida del modelo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo modificado, potencialmente actualizado con los datos de la imagen inicial codificada. | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado, potencialmente actualizado con los datos de la imagen inicial codificada. | CONDITIONING |
| `latente` | Latente de video vacío. Un tensor latente lleno de ceros, con la forma de las dimensiones especificadas. | LATENT |
| `latente_cond` | Imágenes iniciales codificadas limpias, utilizadas para reemplazar el inicio ruidoso de los latentes de salida del modelo. Vacío cuando no se proporciona una `start_image`. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
