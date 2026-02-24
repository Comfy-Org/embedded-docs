> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/es.md)

El nodo Kandinsky5ImageToVideo prepara los datos de condicionamiento y del espacio latente para la generación de vídeo utilizando el modelo Kandinsky. Crea un tensor latente de vídeo vacío y, opcionalmente, puede codificar una imagen inicial para guiar los primeros fotogramas del vídeo generado, modificando el condicionamiento positivo y negativo en consecuencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | N/A | Los prompts de condicionamiento positivo para guiar la generación del vídeo. |
| `negative` | CONDITIONING | Sí | N/A | Los prompts de condicionamiento negativo para alejar la generación del vídeo de ciertos conceptos. |
| `vae` | VAE | Sí | N/A | El modelo VAE utilizado para codificar la imagen inicial opcional en el espacio latente. |
| `width` | INT | No | 16 a 8192 (paso 16) | El ancho del vídeo de salida en píxeles (por defecto: 768). |
| `height` | INT | No | 16 a 8192 (paso 16) | La altura del vídeo de salida en píxeles (por defecto: 512). |
| `length` | INT | No | 1 a 8192 (paso 4) | El número de fotogramas en el vídeo (por defecto: 121). |
| `batch_size` | INT | No | 1 a 4096 | El número de secuencias de vídeo a generar simultáneamente (por defecto: 1). |
| `start_image` | IMAGE | No | N/A | Una imagen inicial opcional. Si se proporciona, se codifica y se utiliza para reemplazar el inicio ruidoso de los latentes de salida del modelo. |

**Nota:** Cuando se proporciona una `start_image`, se redimensiona automáticamente para que coincida con el `width` y `height` especificados utilizando interpolación bilineal. Se utilizan los primeros `length` fotogramas del lote de imágenes para la codificación. El latente codificado se inyecta luego tanto en el condicionamiento `positive` como en el `negative` para guiar la apariencia inicial del vídeo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado, potencialmente actualizado con los datos de la imagen inicial codificada. |
| `negative` | CONDITIONING | El condicionamiento negativo modificado, potencialmente actualizado con los datos de la imagen inicial codificada. |
| `latent` | LATENT | Un tensor latente de vídeo vacío con ceros, configurado para las dimensiones especificadas. |
| `cond_latent` | LATENT | La representación latente limpia y codificada de las imágenes iniciales proporcionadas. Se utiliza internamente para reemplazar el inicio ruidoso de los latentes de vídeo generados. |
