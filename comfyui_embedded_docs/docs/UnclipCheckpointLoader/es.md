Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo unCLIPCheckpointLoader está diseñado para cargar checkpoints específicamente adaptados para modelos unCLIP. Facilita la recuperación e inicialización de modelos, módulos de visión CLIP y VAEs desde un checkpoint especificado, agilizando el proceso de configuración para operaciones o análisis posteriores.

## Entradas

| Campo      | Comfy dtype       | Descripción                                                                       |
|------------|-------------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]`    | Especifica el nombre del checkpoint a cargar, identificando y recuperando el archivo de checkpoint correcto desde un directorio predefinido, determinando la inicialización de modelos y configuraciones. |

## Salidas

| Campo       | Comfy dtype   | Descripción                                                              | Python dtype         |
|-------------|---------------|--------------------------------------------------------------------------|---------------------|
| `model`     | `MODEL`       | Representa el modelo principal cargado desde el checkpoint.                   | `torch.nn.Module`   |
| `clip`      | `CLIP`        | Representa el módulo CLIP cargado desde el checkpoint, si está disponible.      | `torch.nn.Module`   |
| `vae`       | `VAE`         | Representa el módulo VAE cargado desde el checkpoint, si está disponible.        | `torch.nn.Module`   |
| `clip_vision`| `CLIP_VISION` | Representa el módulo de visión CLIP cargado desde el checkpoint, si está disponible.| `torch.nn.Module`   |
