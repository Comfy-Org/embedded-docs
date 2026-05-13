> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/es.md)

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/checkpoints`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para permitir que lea los archivos de modelo desde la carpeta correspondiente.

Este nodo se especializa en cargar puntos de control específicamente para modelos basados en imágenes dentro de flujos de trabajo de generación de video. Recupera y configura de manera eficiente los componentes necesarios de un punto de control determinado, centrándose en los aspectos relacionados con imágenes del modelo.

## Entradas

| Campo        | Tipo de Dato | Descripción                                                                                     |
|--------------|---------------|-------------------------------------------------------------------------------------------------|
| `ckpt_name`  | COMBO[STRING] | Especifica el nombre del punto de control a cargar, crucial para identificar y recuperar el archivo de punto de control correcto de una lista predefinida. |

## Salidas

| Campo         | Tipo de Dato | Descripción                                                                                                   |
|---------------|---------------|---------------------------------------------------------------------------------------------------------------|
| `model`       | MODEL         | Devuelve el modelo principal cargado desde el punto de control, configurado para el procesamiento de imágenes en contextos de generación de video. |
| `clip_vision` | `CLIP_VISION` | Proporciona el componente de visión CLIP del punto de control, adaptado para la comprensión de imágenes y la extracción de características. |
| `vae`         | VAE           | Entrega el componente de Autoencoder Variacional (VAE), esencial para tareas de manipulación y generación de imágenes. |