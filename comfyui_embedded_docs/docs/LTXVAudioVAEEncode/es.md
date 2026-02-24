> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/es.md)

El nodo LTXV Audio VAE Encode toma una entrada de audio y la comprime en una representación latente más pequeña utilizando un modelo de Audio VAE especificado. Este proceso es esencial para generar o manipular audio dentro de un flujo de trabajo de espacio latente, ya que convierte los datos de audio sin procesar en un formato que otros nodos en la canalización pueden entender y procesar.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | El audio que se va a codificar. |
| `audio_vae` | VAE | Sí | - | El modelo de Audio VAE que se utilizará para la codificación. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `Audio Latent` | LATENT | La representación latente comprimida del audio de entrada. La salida incluye las muestras latentes, la frecuencia de muestreo del modelo VAE y un identificador de tipo. |
