
El nodo VAEDecode está diseñado para decodificar representaciones latentes en imágenes utilizando un Autoencoder Variacional (VAE) especificado. Sirve para generar imágenes a partir de representaciones de datos comprimidos, facilitando la reconstrucción de imágenes desde sus codificaciones en el espacio latente.
## Tipos de entrada

| Parámetro | Comfy dtype | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes que se decodificarán en imágenes. Es crucial para el proceso de decodificación ya que proporciona los datos comprimidos a partir de los cuales se reconstruyen las imágenes. |
| `vae`     | `VAE`       | El parámetro 'vae' especifica el modelo de Autoencoder Variacional que se utilizará para decodificar las representaciones latentes en imágenes. Es esencial para determinar el mecanismo de decodificación y la calidad de las imágenes reconstruidas. |

## Tipos de salida

| Parámetro | Comfy dtype | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una imagen reconstruida a partir de la representación latente proporcionada utilizando el modelo VAE especificado. |