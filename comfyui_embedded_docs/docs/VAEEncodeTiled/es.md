# VAE Codificar (Mosaico)

El nodo VAEEncodeTiled procesa imágenes dividiéndolas en mosaicos más pequeños y codificándolas mediante un Autoencoder Variacional. Este enfoque basado en mosaicos permite manejar imágenes grandes que de otro modo superarían los límites de memoria. El nodo admite tanto VAEs de imágenes como de video, con controles de mosaico separados para las dimensiones espaciales y temporales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `píxeles` | Los datos de imagen de entrada que se codificarán | IMAGE | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para la codificación | VAE | Sí | - |
| `tamaño_mosaico` | El tamaño de cada mosaico para el procesamiento espacial (predeterminado: 512) | INT | Sí | 64-4096 (paso: 64) |
| `superposición` | La cantidad de superposición entre mosaicos adyacentes (predeterminado: 64) | INT | Sí | 0-4096 (paso: 32) |
| `tamaño_temporal` | Solo se usa para VAEs de video: Cantidad de fotogramas a codificar a la vez (predeterminado: 64) | INT | Sí | 8-4096 (paso: 4) |
| `superposición_temporal` | Solo se usa para VAEs de video: Cantidad de fotogramas a superponer (predeterminado: 8) | INT | Sí | 4-4096 (paso: 4) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se utilizan VAEs de video y no tienen efecto en los VAEs de imágenes estándar.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | La representación latente codificada de la imagen de entrada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `87420b96ef9b2d5ef18ecb0339a62b6955151e2a9d2c4390758048c00432939a`
