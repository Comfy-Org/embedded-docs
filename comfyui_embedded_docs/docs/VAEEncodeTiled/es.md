> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

El nodo VAEEncodeTiled procesa imágenes dividiéndolas en mosaicos más pequeños y codificándolas mediante un Autoencoder Variacional. Este enfoque basado en mosaicos permite manejar imágenes grandes que de otro modo superarían los límites de memoria. El nodo admite tanto VAEs de imágenes como de video, con controles de mosaico separados para las dimensiones espaciales y temporales.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-------------|-------------|-------|-------------|
| `pixels` | IMAGE | Sí | - | Los datos de imagen de entrada que se codificarán |
| `vae` | VAE | Sí | - | El modelo de Autoencoder Variacional utilizado para la codificación |
| `tile_size` | INT | Sí | 64-4096 (paso: 64) | El tamaño de cada mosaico para el procesamiento espacial (predeterminado: 512) |
| `overlap` | INT | Sí | 0-4096 (paso: 32) | La cantidad de superposición entre mosaicos adyacentes (predeterminado: 64) |
| `temporal_size` | INT | Sí | 8-4096 (paso: 4) | Solo se usa para VAEs de video: Cantidad de fotogramas a codificar a la vez (predeterminado: 64) |
| `temporal_overlap` | INT | Sí | 4-4096 (paso: 4) | Solo se usa para VAEs de video: Cantidad de fotogramas a superponer (predeterminado: 8) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se utilizan VAEs de video y no tienen efecto en los VAEs de imágenes estándar.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|-------------|-------------|
| `LATENT` | LATENT | La representación latente codificada de la imagen de entrada |

---
**Source fingerprint (SHA-256):** `87420b96ef9b2d5ef18ecb0339a62b6955151e2a9d2c4390758048c00432939a`
