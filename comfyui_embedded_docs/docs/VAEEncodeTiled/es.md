# VAE Codificar (Mosaico)

El nodo VAEEncodeTiled procesa imágenes dividiéndolas en teselas más pequeñas y codificándolas mediante un Autoencoder Variacional. Este enfoque por teselas permite manejar imágenes grandes que de otro modo podrían superar las limitaciones de memoria. El nodo admite tanto VAE de imagen como de video, con controles de teselado separados para las dimensiones espaciales y temporales.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `pixels` | Los datos de imagen de entrada que se van a codificar | IMAGE | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para la codificación | VAE | Sí | - |
| `tile_size` | El tamaño de cada tesela para el procesamiento espacial (por defecto: 512) | INT | Sí | 64-4096 (step: 64) |
| `overlap` | La cantidad de superposición entre teselas adyacentes (por defecto: 64) | INT | Sí | 0-4096 (step: 32) |
| `temporal_size` | Solo se usa para VAE de video: cantidad de fotogramas a codificar a la vez (por defecto: 64) | INT | Sí | 8-4096 (step: 4) |
| `temporal_overlap` | Solo se usa para VAE de video: cantidad de fotogramas que se superponen (por defecto: 8) | INT | Sí | 4-4096 (step: 4) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se utilizan VAE de video y no tienen efecto en los VAE de imagen estándar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | La representación latente codificada de la imagen de entrada | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
