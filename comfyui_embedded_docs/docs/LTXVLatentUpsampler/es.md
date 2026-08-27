# LTXVLatentUpsampler

El nodo LTXVLatentUpsampler aumenta la resolución espacial de una representación latente de video por un factor de dos. Utiliza un modelo de escalado especializado para procesar los datos latentes, que primero se desnormalizan y luego se renormalizan utilizando las estadísticas de canal del VAE proporcionado. Este nodo está diseñado para flujos de trabajo de video dentro del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente de entrada del video que se va a ampliar. | LATENT | Sí |  |
| `modelo_de_escalado` | El modelo cargado utilizado para realizar el escalado 2x en los datos latentes. | LATENT_UPSCALE_MODEL | Sí |  |
| `vae` | El modelo VAE utilizado para desnormalizar los latentes de entrada antes del escalado y para normalizar los latentes de salida después. | VAE | Sí |  |

Nota: Este nodo está marcado como experimental en ComfyUI.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `LATENT` | La representación latente escalada, con dimensiones espaciales duplicadas en comparación con la entrada. El latente de salida tiene el mismo tamaño de lote, número de canales y longitud temporal que la entrada. El `noise_mask` de la entrada, si está presente, se elimina de la salida. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/es.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
