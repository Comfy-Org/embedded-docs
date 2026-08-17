# HunyuanVideo15SuperResolution

El nodo HunyuanVideo15SuperResolution prepara datos de condicionamiento para un proceso de superresolución de video. Toma una representación latente de un video y, opcionalmente, una imagen inicial, y los empaqueta junto con un valor de aumento de ruido y datos opcionales de visión CLIP en un formato que un modelo puede usar para generar una salida de mayor resolución.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | La entrada de condicionamiento positivo que se modificará con los datos concatenados de latente y aumento de ruido. | CONDITIONING | Sí | N/A |
| `negative` | La entrada de condicionamiento negativo que se modificará con los datos concatenados de latente y aumento de ruido. | CONDITIONING | Sí | N/A |
| `vae` | El VAE utilizado para codificar la `start_image` opcional. Es necesario si se proporciona `start_image`. | VAE | No | N/A |
| `start_image` | Una imagen inicial opcional que guía el proceso de superresolución. Si se proporciona, se amplía, se codifica con el `vae` y se coloca al inicio del latente de condicionamiento. | IMAGE | No | N/A |
| `clip_vision_output` | Incrustaciones opcionales de visión CLIP. Cuando se proporcionan, se añaden tanto al condicionamiento positivo como al negativo. | CLIP_VISION_OUTPUT | No | N/A |
| `latent` | La representación latente de video que se incorporará al condicionamiento. | LATENT | Sí | N/A |
| `noise_augmentation` | La intensidad del aumento de ruido que se aplicará al condicionamiento (predeterminado: 0.70). Este es un parámetro avanzado. | FLOAT | Sí | 0.0 - 1.0 (step 0.01) |

**Nota:** Si proporcionas una `start_image`, también debes conectar un `vae` para que se codifique. La `start_image` se amplía automáticamente para coincidir con las dimensiones implícitas del `latent` de entrada, y solo se utilizan sus primeros tres canales de color (RGB) por el VAE.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP. | CONDITIONING |
| `latent` | El latente de entrada, transmitido sin cambios. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/es.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
