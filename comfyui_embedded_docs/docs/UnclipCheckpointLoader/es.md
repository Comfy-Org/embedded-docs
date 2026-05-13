> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPCheckpointLoader/es.md)

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para permitir que lea los archivos de modelo desde la carpeta correspondiente.

El nodo unCLIPCheckpointLoader está diseñado para cargar puntos de control (checkpoints) específicamente adaptados para modelos unCLIP. Facilita la recuperación e inicialización de modelos, módulos CLIP vision y VAEs desde un punto de control especificado, optimizando el proceso de configuración para operaciones o análisis posteriores.

## Entradas

| Campo        | Tipo Comfy        | Descripción                                                                       |
|--------------|-------------------|-----------------------------------------------------------------------------------|
| `ckpt_name`  | `COMBO[STRING]`   | Especifica el nombre del punto de control a cargar, identificando y recuperando el archivo de punto de control correcto desde un directorio predefinido, determinando la inicialización de modelos y configuraciones. |

## Salidas

| Campo         | Tipo Comfy    | Descripción                                                              | Tipo Python          |
|---------------|---------------|--------------------------------------------------------------------------|----------------------|
| `model`       | `MODEL`       | Representa el modelo principal cargado desde el punto de control.        | `torch.nn.Module`    |
| `clip`        | `CLIP`        | Representa el módulo CLIP cargado desde el punto de control, si está disponible. | `torch.nn.Module`    |
| `vae`         | `VAE`         | Representa el módulo VAE cargado desde el punto de control, si está disponible.   | `torch.nn.Module`    |
| `clip_vision` | `CLIP_VISION` | Representa el módulo CLIP vision cargado desde el punto de control, si está disponible. | `torch.nn.Module`    |