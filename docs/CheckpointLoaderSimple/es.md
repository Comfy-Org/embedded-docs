Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, 
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml. 
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.


El nodo CheckpointLoaderSimple está diseñado para cargar checkpoints de modelos sin necesidad de especificar una configuración. Simplifica el proceso de carga de checkpoints al requerir solo el nombre del checkpoint, haciéndolo más accesible para usuarios que pueden no estar familiarizados con los detalles de configuración.
## Tipos de entrada

| Campo     | Comfy dtype | Descripción                                                                       |
|-----------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]` | Especifica el nombre del checkpoint a cargar, determinando qué archivo de checkpoint intentará cargar el nodo y afectando la ejecución del nodo y el modelo que se carga. |

## Tipos de salida

| Campo | Comfy dtype | Descripción                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL` | Devuelve el modelo cargado, permitiendo que se utilice para procesamiento o inferencia adicional. |
| `clip`  | `CLIP`     | Devuelve el modelo CLIP asociado con el checkpoint cargado, si está disponible. |
| `vae`   | `VAE`      | Devuelve el modelo VAE asociado con el checkpoint cargado, si está disponible. |