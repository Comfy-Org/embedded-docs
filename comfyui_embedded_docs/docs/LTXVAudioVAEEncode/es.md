El nodo LTXV Audio VAE Encode toma una entrada de audio y la comprime en una representación latente más pequeña utilizando un modelo Audio VAE específico. Este proceso es esencial para generar o manipular audio dentro de un flujo de trabajo de espacio latente, ya que convierte los datos de audio sin procesar en un formato que otros nodos en el pipeline pueden entender y procesar.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `audio` | El audio que se va a codificar. | AUDIO | Sí | - |
| `audio_vae` | El modelo Audio VAE que se utilizará para la codificación. | VAE | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `Audio Latent` | La representación latente comprimida del audio de entrada. La salida incluye las muestras latentes, la frecuencia de muestreo del modelo VAE y un identificador de tipo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/es.md)

---
**Source fingerprint (SHA-256):** `fc10d8bbdca5150b7c87adb52960b8690397c3d003c89f9ec6a8410c541a347f`
