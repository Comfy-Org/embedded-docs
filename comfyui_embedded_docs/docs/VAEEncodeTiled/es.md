> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

El nodo VAEEncodeTiled procesa imágenes dividiéndolas en mosaicos más pequeños y codificándolos mediante un Autoencoder Variacional. Este enfoque basado en mosaicos permite manejar imágenes grandes que de otro modo podrían exceder las limitaciones de memoria. El nodo admite tanto VAEs de imagen como de video, con controles de mosaico separados para dimensiones espaciales y temporales.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `pixels` | IMAGE | Sí | - | Los datos de imagen de entrada a codificar |
| `vae` | VAE | Sí | - | El modelo de Autoencoder Variacional utilizado para la codificación |
| `tile_size` | INT | Sí | 64-4096 (paso: 64) | El tamaño de cada mosaico para el procesamiento espacial (por defecto: 512) |
| `overlap` | INT | Sí | 0-4096 (paso: 32) | La cantidad de superposición entre mosaicos adyacentes (por defecto: 64) |
| `temporal_size` | INT | Sí | 8-4096 (paso: 4) | Solo para VAEs de video: Cantidad de fotogramas a codificar a la vez (por defecto: 64) |
| `temporal_overlap` | INT | Sí | 4-4096 (paso: 4) | Solo para VAEs de video: Cantidad de fotogramas a superponer (por defecto: 8) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se utilizan VAEs de video y no tienen efecto en VAEs de imagen estándar.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La representación latente codificada de la imagen de entrada |