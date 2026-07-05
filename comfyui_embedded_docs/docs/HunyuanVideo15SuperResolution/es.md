# HunyuanVideo15SuperResolution

El nodo `HunyuanVideo15SuperResolution` prepara datos de condicionamiento para un proceso de superresolución de video. Toma una representación latente de un video y, opcionalmente, una imagen inicial, y los empaqueta junto con aumento de ruido y datos de visión CLIP en un formato que puede ser utilizado por un modelo para generar una salida de mayor resolución.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo que se modificará con datos latentes y de aumento. | CONDITIONING | Sí | N/A |
| `negativo` | La entrada de condicionamiento negativo que se modificará con datos latentes y de aumento. | CONDITIONING | Sí | N/A |
| `vae` | El VAE utilizado para codificar la `imagen_inicial` opcional. Es obligatorio si se proporciona `imagen_inicial`. | VAE | No | N/A |
| `imagen_inicial` | Una imagen inicial opcional para guiar la superresolución. Si se proporciona, se ampliará y codificará en el latente de condicionamiento. | IMAGE | No | N/A |
| `clip_vision_output` | Incrustaciones de visión CLIP opcionales para agregar al condicionamiento. | CLIP_VISION_OUTPUT | No | N/A |
| `latente` | La representación latente de video de entrada que se incorporará al condicionamiento. | LATENT | Sí | N/A |
| `aumento_de_ruido` | La intensidad del aumento de ruido que se aplicará al condicionamiento (valor predeterminado: 0.70). | FLOAT | No | 0.0 - 1.0 |

**Nota:** Si proporcionas una `start_image`, también debes conectar un `vae` para que pueda ser codificada. La `start_image` se ampliará automáticamente para que coincida con las dimensiones implícitas del `latent` de entrada.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos de visión CLIP opcionales. | CONDITIONING |
| `negative` | El condicionamiento negativo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos de visión CLIP opcionales. | CONDITIONING |
| `latent` | El latente de entrada se transmite sin cambios. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/es.md)

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
