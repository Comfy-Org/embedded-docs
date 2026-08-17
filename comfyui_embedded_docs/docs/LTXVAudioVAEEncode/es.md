# Codificar LTXV Audio VAE

El nodo **LTXV Audio VAE Encode** toma una entrada de audio y la comprime en una representación latente más pequeña utilizando un modelo Audio VAE específico. Este proceso es esencial para generar o manipular audio dentro de un flujo de trabajo de espacio latente, ya que convierte los datos de audio sin procesar en un formato que otros nodos del pipeline pueden comprender y procesar.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `audio` | El audio que se va a codificar. | AUDIO | Sí | - |
| `audio_vae` | El modelo Audio VAE que se usará para la codificación. | VAE | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `Audio Latent` | La representación latente comprimida del audio de entrada. La salida incluye las muestras latentes, la frecuencia de muestreo del modelo VAE y un identificador de tipo. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/es.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`
