> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/es.md)

El nodo HunyuanVideo15SuperResolution prepara datos de condicionamiento para un proceso de superresolución de video. Toma una representación latente de un video y, opcionalmente, una imagen inicial, y los empaqueta junto con datos de aumento de ruido y visión CLIP en un formato que puede ser utilizado por un modelo para generar una salida de mayor resolución.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | N/A | La entrada de condicionamiento positivo que se modificará con datos latentes y de aumento. |
| `negative` | CONDITIONING | Sí | N/A | La entrada de condicionamiento negativo que se modificará con datos latentes y de aumento. |
| `vae` | VAE | No | N/A | El VAE utilizado para codificar la `start_image` opcional. Requerido si se proporciona `start_image`. |
| `start_image` | IMAGE | No | N/A | Una imagen inicial opcional para guiar la superresolución. Si se proporciona, se escalará y codificará en el latente de condicionamiento. |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | N/A | Incrustaciones de visión CLIP opcionales para agregar al condicionamiento. |
| `latent` | LATENT | Sí | N/A | La representación latente del video de entrada que se incorporará al condicionamiento. |
| `noise_augmentation` | FLOAT | No | 0.0 - 1.0 | La intensidad del aumento de ruido a aplicar al condicionamiento (por defecto: 0.70). |

**Nota:** Si proporciona una `start_image`, también debe conectar un `vae` para que pueda ser codificada. La `start_image` se escalará automáticamente para que coincida con las dimensiones implícitas del `latent` de entrada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP. |
| `negative` | CONDITIONING | El condicionamiento negativo modificado, que ahora contiene el latente concatenado, el aumento de ruido y los datos opcionales de visión CLIP. |
| `latent` | LATENT | El latente de entrada se pasa sin cambios. |
