
Este nodo está diseñado para codificar imágenes en una representación de espacio latente utilizando un modelo VAE especificado. Abstrae la complejidad del proceso de codificación, proporcionando una forma sencilla de transformar imágenes en sus representaciones latentes.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `pixels`  | `IMAGE`     | El parámetro 'pixels' representa los datos de la imagen que se codificarán en el espacio latente. Juega un papel crucial en la determinación de la representación latente de salida al servir como la entrada directa para el proceso de codificación. |
| `vae`     | VAE       | El parámetro 'vae' especifica el modelo de Autoencoder Variacional que se utilizará para codificar los datos de la imagen en el espacio latente. Es esencial para definir el mecanismo de codificación y las características de la representación latente generada. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una representación de espacio latente de la imagen de entrada, encapsulando sus características esenciales en una forma comprimida. |
