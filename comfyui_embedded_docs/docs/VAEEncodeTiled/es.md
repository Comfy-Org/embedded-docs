# VAE Codificar (Mosaico)

VAEEncodeTiled procesa imágenes dividiéndolas en mosaicos más pequeños y codificándolas mediante un Autoencoder Variacional. Este enfoque por mosaicos permite manejar imágenes grandes que, de otro modo, podrían exceder las limitaciones de memoria. El nodo admite VAE tanto de imagen como de video, con controles de mosaico separados para las dimensiones espacial y temporal.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `pixels` | Los datos de imagen de entrada que se van a codificar. | IMAGE | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para la codificación. | VAE | Sí | - |
| `tile_size` | El tamaño de cada mosaico para el procesamiento espacial (predeterminado: 512). Ajuste avanzado. | INT | Sí | 64-4096 (paso: 64) |
| `overlap` | La cantidad de superposición entre mosaicos adyacentes (predeterminado: 64). Ajuste avanzado. | INT | Sí | 0-4096 (paso: 32) |
| `temporal_size` | Solo se usa para VAE de video: cantidad de fotogramas a codificar a la vez (predeterminado: 64). Ajuste avanzado. | INT | Sí | 8-4096 (paso: 4) |
| `temporal_overlap` | Solo se usa para VAE de video: cantidad de fotogramas a superponer (predeterminado: 8). Ajuste avanzado. | INT | Sí | 4-4096 (paso: 4) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se usan VAE de video y no tienen efecto en los VAE de imágenes estándar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | La representación latente codificada de la imagen de entrada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
