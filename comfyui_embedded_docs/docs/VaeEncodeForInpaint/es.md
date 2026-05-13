> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeForInpaint/es.md)

Este nodo está diseñado para codificar imágenes en una representación latente adecuada para tareas de inpainting, incorporando pasos de preprocesamiento adicionales para ajustar la imagen de entrada y la máscara, logrando una codificación óptima por parte del modelo VAE.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `píxeles`  | `IMAGE`     | La imagen de entrada que se va a codificar. Esta imagen se somete a un preprocesamiento y redimensionamiento para que coincida con las dimensiones de entrada esperadas por el modelo VAE antes de la codificación. |
| `vae`     | VAE       | El modelo VAE utilizado para codificar la imagen en su representación latente. Desempeña un papel crucial en el proceso de transformación, determinando la calidad y las características del espacio latente de salida. |
| `máscara`    | `MASK`      | Una máscara que indica las regiones de la imagen de entrada que se van a inpaint. Se utiliza para modificar la imagen antes de la codificación, asegurando que el VAE se centre en las áreas relevantes. |
| `crecer_máscara_por` | `INT` | Especifica cuánto expandir la máscara de inpainting para garantizar transiciones sin fisuras en el espacio latente. Un valor mayor aumenta el área afectada por el inpainting. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida incluye la representación latente codificada de la imagen y una máscara de ruido, ambas cruciales para las tareas posteriores de inpainting. |