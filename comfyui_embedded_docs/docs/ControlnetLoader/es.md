Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/controlnet`, y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml. A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo ControlNetLoader está diseñado para cargar un modelo ControlNet desde una ruta especificada. Desempeña un papel crucial en la inicialización de modelos ControlNet, que son esenciales para aplicar mecanismos de control sobre contenido generado o modificar contenido existente basado en señales de control.

## Entradas

| Campo             | Comfy dtype       | Descripción                                                                       |
|-------------------|-------------------|-----------------------------------------------------------------------------------|
| `control_net_name`| `COMBO[STRING]`    | Especifica el nombre del modelo ControlNet a cargar, utilizado para localizar el archivo del modelo dentro de una estructura de directorios predefinida. |

## Salidas

| Campo          | Comfy dtype   | Descripción                                                              |
|----------------|---------------|--------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Devuelve el modelo ControlNet cargado, listo para su uso en el control o modificación de procesos de generación de contenido. |
