El nodo Guardar Checkpoint está diseñado para guardar el estado de varios componentes del modelo, incluyendo modelos, CLIP y VAE, en un archivo de checkpoint. Esta funcionalidad es crucial para preservar el progreso de entrenamiento o la configuración de los modelos para su uso posterior o para compartir.

## Entradas

| Parámetro | Tipo Comfy | Descripción |
|-----------|-------------|-------------|
| `model`   | `MODEL`     | El parámetro del modelo representa el modelo principal cuyo estado se va a guardar. Es esencial para capturar el estado actual del modelo para su futura restauración o análisis. |
| `clip`    | `CLIP`      | El parámetro clip está destinado al modelo CLIP asociado con el modelo principal, permitiendo que su estado se guarde junto con el modelo principal. |
| `vae`     | `VAE`       | El parámetro vae es para el modelo de Autoencoder Variacional (VAE), permitiendo que su estado se guarde para su uso o análisis futuro junto con el modelo principal y CLIP. |
| `filename_prefix` | `STRING` | Este parámetro especifica el prefijo para el nombre del archivo bajo el cual se guardará el checkpoint, proporcionando un medio para organizar e identificar los checkpoints guardados. |

## Salidas

Este nodo generará un archivo de checkpoint, y la ruta del archivo de salida correspondiente es el directorio `output/checkpoints/`.
