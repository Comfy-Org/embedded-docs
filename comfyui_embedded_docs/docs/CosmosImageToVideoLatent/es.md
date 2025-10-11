> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/es.md)

El nodo CosmosImageToVideoLatent crea representaciones latentes de video a partir de imágenes de entrada. Genera un latente de video en blanco y opcionalmente codifica imágenes de inicio y/o fin en los fotogramas iniciales y/o finales de la secuencia de video. Cuando se proporcionan imágenes, también crea máscaras de ruido correspondientes para indicar qué partes del latente deben preservarse durante la generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar imágenes en el espacio latente |
| `width` | INT | No | 16 a MAX_RESOLUTION | El ancho del video de salida en píxeles (predeterminado: 1280) |
| `height` | INT | No | 16 a MAX_RESOLUTION | La altura del video de salida en píxeles (predeterminado: 704) |
| `length` | INT | No | 1 a MAX_RESOLUTION | El número de fotogramas en la secuencia de video (predeterminado: 121) |
| `batch_size` | INT | No | 1 a 4096 | El número de lotes latentes a generar (predeterminado: 1) |
| `start_image` | IMAGE | No | - | Imagen opcional para codificar al inicio de la secuencia de video |
| `end_image` | IMAGE | No | - | Imagen opcional para codificar al final de la secuencia de video |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo devuelve un latente en blanco sin ninguna máscara de ruido. Cuando se proporciona alguna imagen, las secciones correspondientes del latente se codifican y enmascaran en consecuencia.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latent` | LATENT | La representación latente de video generada con imágenes codificadas opcionales y máscaras de ruido correspondientes |