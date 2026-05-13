> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/es.md)

El nodo VAEDecode está diseñado para decodificar representaciones latentes en imágenes utilizando un Autoencoder Variacional (VAE) específico. Su propósito es generar imágenes a partir de representaciones de datos comprimidos, facilitando la reconstrucción de imágenes desde sus codificaciones en el espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes que se decodificarán en imágenes. Es crucial para el proceso de decodificación, ya que proporciona los datos comprimidos a partir de los cuales se reconstruyen las imágenes. |
| `vae`     | VAE         | El parámetro 'vae' especifica el modelo de Autoencoder Variacional que se utilizará para decodificar las representaciones latentes en imágenes. Es esencial para determinar el mecanismo de decodificación y la calidad de las imágenes reconstruidas. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una imagen reconstruida a partir de la representación latente proporcionada, utilizando el modelo VAE especificado. |