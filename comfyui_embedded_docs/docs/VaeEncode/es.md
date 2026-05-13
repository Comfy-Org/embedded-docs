> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/es.md)

Este nodo está diseñado para codificar imágenes en una representación de espacio latente utilizando un modelo VAE específico. Abstrae la complejidad del proceso de codificación, proporcionando una forma directa de transformar imágenes en sus representaciones latentes.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | El parámetro 'pixels' representa los datos de la imagen que se codificarán en el espacio latente. Desempeña un papel crucial en la determinación de la representación latente de salida al servir como entrada directa para el proceso de codificación. |
| `vae`     | VAE       | El parámetro 'vae' especifica el modelo de Autoencoder Variacional que se utilizará para codificar los datos de la imagen en el espacio latente. Es esencial para definir el mecanismo de codificación y las características de la representación latente generada. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una representación del espacio latente de la imagen de entrada, que encapsula sus características esenciales en una forma comprimida. |