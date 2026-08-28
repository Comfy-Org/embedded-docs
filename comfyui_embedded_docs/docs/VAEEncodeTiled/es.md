# VAE Codificar (Mosaico)

VAEEncodeTiled procesa imágenes dividiéndolas en tiles más pequeños y codificándolas mediante un Autoencoder Variacional. Este enfoque por tiles permite manejar imágenes grandes que de otro modo podrían superar los límites de memoria. El nodo admite tanto VAEs de imágenes como de vídeo, con controles de tiles separados para las dimensiones espacial y temporal.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `píxeles` | Los datos de imagen de entrada que se van a codificar | IMAGE | Sí | - |
| `vae` | El modelo de Autoencoder Variacional utilizado para la codificación | VAE | Sí | - |
| `tamaño_mosaico` | El tamaño de cada tile para el procesamiento espacial (predeterminado: 512) | INT | Sí | 64-4096 (step: 64) |
| `superposición` | La cantidad de superposición entre tiles adyacentes (predeterminado: 64) | INT | Sí | 0-4096 (step: 32) |
| `tamaño_temporal` | Solo se usa para VAEs de vídeo: cantidad de fotogramas a codificar a la vez (predeterminado: 64) | INT | Sí | 8-4096 (step: 4) |
| `superposición_temporal` | Solo se usa para VAEs de vídeo: cantidad de fotogramas a superponer (predeterminado: 8) | INT | Sí | 4-4096 (step: 4) |

**Nota:** Los parámetros `temporal_size` y `temporal_overlap` solo son relevantes cuando se utilizan VAEs de vídeo y no tienen efecto en los VAEs de imagen estándar.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `LATENT` | La representación latente codificada de la imagen de entrada. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/es.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
