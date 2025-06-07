Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/upscale_models`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo UpscaleModelLoader está diseñado para cargar modelos de escalado desde un directorio especificado. Facilita la recuperación y preparación de modelos de escalado para tareas de escalado de imágenes, asegurando que los modelos se carguen y configuren correctamente para su evaluación.

## Entradas

| Campo         | Comfy dtype       | Descripción                                                                       |
|---------------|-------------------|-----------------------------------------------------------------------------------|
| `model_name`  | `COMBO[STRING]`   | Especifica el nombre del modelo de escalado a cargar, identificando y recuperando el archivo de modelo correcto del directorio de modelos de escalado. |

## Salidas

| Campo           | Comfy dtype         | Descripción                                                              |
|-----------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model` | `UPSCALE_MODEL`     | Devuelve el modelo de escalado cargado y preparado, listo para su uso en tareas de escalado de imágenes. |
