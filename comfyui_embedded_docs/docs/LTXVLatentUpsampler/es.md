El nodo LTXVLatentUpsampler aumenta la resolución espacial de una representación latente de video por un factor de dos. Utiliza un modelo de ampliación especializado para procesar los datos latentes, los cuales primero se desnormalizan y luego se renormalizan utilizando las estadísticas de canal del VAE proporcionado. Este nodo está diseñado para flujos de trabajo de video dentro del espacio latente.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente de entrada del video que se va a ampliar. | LATENT | Sí |  |
| `modelo_de_escalado` | El modelo cargado utilizado para realizar la ampliación 2x en los datos latentes. | LATENT_UPSCALE_MODEL | Sí |  |
| `vae` | El modelo VAE utilizado para desnormalizar los latentes de entrada antes de la ampliación y para normalizar los latentes de salida después. | VAE | Sí |  |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | La representación latente ampliada, con dimensiones espaciales duplicadas en comparación con la entrada. El latente de salida tiene el mismo tamaño de lote, número de canales y duración temporal que la entrada. La `noise_mask` de la entrada, si está presente, se elimina de la salida. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/es.md)

---
**Source fingerprint (SHA-256):** `b2c726d3a3e4881eee7e1d3bae8c478adf01cd87a9652be882579f4e26c1536f`
