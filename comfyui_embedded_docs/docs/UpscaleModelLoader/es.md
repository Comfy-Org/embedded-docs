> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/es.md)

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/upscale_models`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente.

El nodo UpscaleModelLoader está diseñado para cargar modelos de escalado desde un directorio específico. Facilita la recuperación y preparación de modelos de escalado para tareas de ampliación de imágenes, asegurando que los modelos se carguen y configuren correctamente para su evaluación.

## Entradas

| Campo          | Tipo Comfy         | Descripción                                                                       |
|----------------|-------------------|-----------------------------------------------------------------------------------|
| `model_name`   | `COMBO[STRING]`    | Especifica el nombre del modelo de escalado a cargar, identificando y recuperando el archivo de modelo correcto desde el directorio de modelos de escalado. |

## Salidas

| Campo            | Tipo Comfy         | Descripción                                                              |
|-------------------|---------------------|--------------------------------------------------------------------------|
| `upscale_model`  | `UPSCALE_MODEL`     | Devuelve el modelo de escalado cargado y preparado, listo para su uso en tareas de ampliación de imágenes. |