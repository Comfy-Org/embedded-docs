> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/es.md)

El nodo LTXVLatentUpsampler aumenta la resolución espacial de una representación latente de video por un factor de dos. Utiliza un modelo especializado de aumento de escala para procesar los datos latentes, los cuales primero se desnormalizan y luego se renormalizan utilizando las estadísticas de canal del VAE proporcionado. Este nodo está diseñado para flujos de trabajo de video dentro del espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sí | | La representación latente de entrada del video que se va a aumentar de escala. |
| `upscale_model` | LATENT_UPSCALE_MODEL | Sí | | El modelo cargado utilizado para realizar el aumento de escala 2x en los datos latentes. |
| `vae` | VAE | Sí | | El modelo VAE utilizado para desnormalizar los latentes de entrada antes del aumento de escala y para normalizar los latentes de salida después. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | La representación latente aumentada de escala, con dimensiones espaciales duplicadas en comparación con la entrada. |
