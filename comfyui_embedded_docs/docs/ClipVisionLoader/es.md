> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionLoader/es.md)

Este nodo detecta automáticamente los modelos ubicados en la carpeta `ComfyUI/models/clip_vision`, así como cualquier ruta de modelo adicional configurada en el archivo `extra_model_paths.yaml`. Si agregas modelos después de iniciar ComfyUI, **actualiza la interfaz de ComfyUI** para asegurarte de que los archivos de modelo más recientes aparezcan listados.

## Entradas

| Campo       | Tipo de dato   | Descripción |
|-------------|---------------|-------------|
| `clip_name` | COMBO[STRING]  | Lista todos los archivos de modelo compatibles en la carpeta `ComfyUI/models/clip_vision`. |

## Salidas

| Campo         | Tipo de dato   | Descripción |
|--------------|--------------|-------------|
| `clip_vision` | CLIP_VISION  | Modelo CLIP Vision cargado, listo para codificar imágenes u otras tareas relacionadas con la visión. |