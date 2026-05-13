> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/es.md)

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/gligen`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente.

El nodo `GLIGENLoader` está diseñado para cargar modelos GLIGEN, que son modelos generativos especializados. Facilita el proceso de recuperación e inicialización de estos modelos desde rutas especificadas, preparándolos para tareas generativas posteriores.

## Entradas

| Campo         | Tipo Comfy        | Descripción                                                                       |
|---------------|-------------------|-----------------------------------------------------------------------------------|
| `nombre_gligen` | `COMBO[STRING]`   | El nombre del modelo GLIGEN que se va a cargar, especificando qué archivo de modelo recuperar y cargar, crucial para la inicialización del modelo GLIGEN. |

## Salidas

| Campo     | Tipo de Dato | Descripción                                                              |
|-----------|--------------|--------------------------------------------------------------------------|
| `gligen`  | `GLIGEN`     | El modelo GLIGEN cargado, listo para su uso en tareas generativas, representando el modelo completamente inicializado cargado desde la ruta especificada. |