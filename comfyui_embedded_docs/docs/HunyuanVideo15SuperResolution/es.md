> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/es.md)

El nodo `HunyuanVideo15SuperResolution` prepara datos de condicionamiento para un proceso de superresolución de video. Toma una representación latente de un video y, opcionalmente, una imagen inicial, y los empaqueta junto con aumento de ruido y datos de visión CLIP en un formato que puede ser utilizado por un modelo para generar una salida de mayor resolución.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | N/A | La entrada de condicionamiento positivo que se modificará con datos latentes y de aumento. |
| `negativo` | CONDITIONING | Sí | N/A | La entrada de condicionamiento negativo que se modificará con datos latentes y de aumento. |
| `vae` | VAE | No | N/A | El VAE utilizado para codificar la `imagen_inicial` opcional. Es obligatorio si se proporciona `imagen_inicial`. |
| `imagen_inicial` | IMAGE | No | N/A | Una imagen inicial opcional para guiar la superresolución. Si se proporciona, se ampliará y codificará en el latente de condicionamiento. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | N/A | Incrustaciones de visión CLIP opcionales para agregar al condicionamiento. |
| `latente` | LATENT | Sí | N/A | La representación latente de video de entrada que se incorporará al condicionamiento. |
| `aumento_de_ruido` | FLOAT | No | 0.0 - 1.0 | La intensidad del aumento de ruido que se aplicará al condicionamiento (valor predeterminado: 0.70). |

**Nota:** Si proporcionas una `start_image`, también debes conectar un `vae` para que pueda ser codificada. La `start_image` se ampliará automáticamente para que coincida con las dimensiones implícitas del `latent` de entrada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | El condicionamiento positivo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos de visión CLIP opcionales. |
| `latente` | CONDITIONING | El condicionamiento negativo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos de visión CLIP opcionales. |
| `latente` | LATENT | El latente de entrada se transmite sin cambios. |

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
