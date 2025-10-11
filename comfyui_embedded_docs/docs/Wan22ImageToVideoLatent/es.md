> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/es.md)

El nodo Wan22ImageToVideoLatent crea representaciones latentes de video a partir de imágenes. Genera un espacio latente de video en blanco con dimensiones específicas y puede opcionalmente codificar una secuencia de imagen inicial en los fotogramas iniciales. Cuando se proporciona una imagen de inicio, codifica la imagen en el espacio latente y crea una máscara de ruido correspondiente para las regiones inpaintadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar imágenes en el espacio latente |
| `width` | INT | No | 32 a MAX_RESOLUTION | El ancho del video de salida en píxeles (valor por defecto: 1280, paso: 32) |
| `height` | INT | No | 32 a MAX_RESOLUTION | La altura del video de salida en píxeles (valor por defecto: 704, paso: 32) |
| `length` | INT | No | 1 a MAX_RESOLUTION | El número de fotogramas en la secuencia de video (valor por defecto: 49, paso: 4) |
| `batch_size` | INT | No | 1 a 4096 | El número de lotes a generar (valor por defecto: 1) |
| `start_image` | IMAGE | No | - | Secuencia de imagen inicial opcional para codificar en el video latente |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imagen en los fotogramas iniciales del espacio latente y genera una máscara de ruido correspondiente. Los parámetros de ancho y altura deben ser divisibles por 16 para las dimensiones adecuadas del espacio latente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | La representación latente de video generada |
| `noise_mask` | LATENT | La máscara de ruido que indica qué regiones deben ser desruidas durante la generación |