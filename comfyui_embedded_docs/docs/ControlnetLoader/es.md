> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/es.md)

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/controlnet`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, puede ser necesario **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente.

El nodo ControlNetLoader está diseñado para cargar un modelo ControlNet desde una ruta específica. Desempeña un papel fundamental en la inicialización de modelos ControlNet, los cuales son esenciales para aplicar mecanismos de control sobre el contenido generado o modificar contenido existente basándose en señales de control.

## Entradas

| Campo              | Tipo Comfy        | Descripción                                                                       |
|--------------------|-------------------|-----------------------------------------------------------------------------------|
| `control_net_name` | `COMBO[STRING]`   | Especifica el nombre del modelo ControlNet a cargar, utilizado para localizar el archivo del modelo dentro de una estructura de directorios predefinida. |

## Salidas

| Campo         | Tipo Comfy     | Descripción                                                              |
|---------------|----------------|--------------------------------------------------------------------------|
| `control_net` | `CONTROL_NET`  | Devuelve el modelo ControlNet cargado, listo para usarse en el control o modificación de procesos de generación de contenido. |