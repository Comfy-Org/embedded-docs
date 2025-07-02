Este nodo detecta automáticamente los modelos ubicados en la carpeta `ComfyUI/models/clip_vision`, así como cualquier ruta adicional configurada en el archivo `extra_model_paths.yaml`. Si agregas modelos después de iniciar ComfyUI, por favor **actualiza la interfaz de ComfyUI** para asegurarte de que la lista de archivos de modelos esté actualizada.

## Entradas

| Campo      | Data Type      | Descripción |
|------------|---------------|-------------|
| clip_name  | COMBO[STRING]  | Muestra todos los archivos de modelos compatibles en la carpeta `ComfyUI/models/clip_vision`. |

## Salidas

| Campo        | Data Type    | Descripción |
|--------------|--------------|-------------|
| clip_vision  | CLIP_VISION  | Modelo CLIP Vision cargado, listo para codificar imágenes u otras tareas relacionadas con la visión. |
