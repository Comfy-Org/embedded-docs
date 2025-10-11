> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/es.md)

El nodo CosmosPredict2ImageToVideoLatent crea representaciones latentes de video a partir de imágenes para la generación de videos. Puede generar un video latente en blanco o incorporar imágenes de inicio y fin para crear secuencias de video con dimensiones y duración especificadas. El nodo maneja la codificación de imágenes al formato de espacio latente apropiado para el procesamiento de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar imágenes en el espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho del video de salida en píxeles (por defecto: 848, debe ser divisible por 16) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura del video de salida en píxeles (por defecto: 480, debe ser divisible por 16) |
| `length` | INT | No | 1 a MAX_RESOLUTION | El número de fotogramas en la secuencia de video (por defecto: 93, paso: 4) |
| `batch_size` | INT | No | 1 a 4096 | El número de secuencias de video a generar (por defecto: 1) |
| `start_image` | IMAGE | No | - | Imagen inicial opcional para la secuencia de video |
| `end_image` | IMAGE | No | - | Imagen final opcional para la secuencia de video |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo genera un video latente en blanco. Cuando se proporcionan imágenes, estas se codifican y posicionan al principio y/o final de la secuencia de video con el enmascaramiento apropiado.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | La representación latente de video generada que contiene la secuencia de video codificada |
| `noise_mask` | LATENT | Una máscara que indica qué partes del latente deben preservarse durante la generación |