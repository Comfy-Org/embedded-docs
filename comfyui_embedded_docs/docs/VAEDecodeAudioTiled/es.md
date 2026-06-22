# VAE Decodificar audio (en mosaico)

Este nodo convierte una representación de audio comprimida (muestras latentes) nuevamente en una forma de onda de audio utilizando un Autoencoder Variacional (VAE). Procesa los datos en secciones más pequeñas y superpuestas (teselas) para gestionar el uso de memoria, lo que lo hace adecuado para manejar secuencias de audio más largas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente comprimida del audio que se va a decodificar. | LATENT | Sí | N/A |
| `vae` | El modelo de Autoencoder Variacional utilizado para realizar la decodificación. | VAE | Sí | N/A |
| `tamaño_de_mosaico` | El tamaño de cada tesela de procesamiento. El audio se decodifica en secciones de esta longitud para conservar memoria (predeterminado: 512). | INT | Sí | 32 a 8192 |
| `superposición` | El número de muestras en las que se superponen las teselas adyacentes. Esto ayuda a reducir los artefactos en los límites entre teselas (predeterminado: 64). | INT | Sí | 0 a 1024 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La forma de onda de audio decodificada. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/es.md)

---
**Source fingerprint (SHA-256):** `d989f0cd0e4b4bf992d6860e27c25b8e814df52763c82909a61c58f418306352`
