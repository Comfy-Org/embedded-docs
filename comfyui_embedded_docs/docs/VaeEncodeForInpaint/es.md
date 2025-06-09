
Este nodo está diseñado para codificar imágenes en una representación latente adecuada para tareas de relleno, incorporando pasos de preprocesamiento adicionales para ajustar la imagen de entrada y la máscara para una codificación óptima por el modelo VAE.

## Entradas

| Parámetro      | Data Type | Descripción |
|----------------|-------------|-------------|
| `pixels`       | `IMAGE`     | La imagen de entrada a codificar. Esta imagen se somete a preprocesamiento y redimensionamiento para coincidir con las dimensiones de entrada esperadas por el modelo VAE antes de la codificación. |
| `vae`          | `VAE`       | El modelo VAE utilizado para codificar la imagen en su representación latente. Juega un papel crucial en el proceso de transformación, determinando la calidad y las características del espacio latente de salida. |
| `mask`         | `MASK`      | Una máscara que indica las regiones de la imagen de entrada que se rellenarán. Se utiliza para modificar la imagen antes de la codificación, asegurando que el VAE se enfoque en las áreas relevantes. |
| `grow_mask_by` | `INT`       | Especifica cuánto expandir la máscara de relleno para asegurar transiciones fluidas en el espacio latente. Un valor mayor incrementa el área afectada por el relleno. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida incluye la representación latente codificada de la imagen y una máscara de ruido, ambas cruciales para tareas de relleno posteriores. |
