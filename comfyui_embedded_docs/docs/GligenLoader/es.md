Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/gligen`, y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml. A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo `GLIGENLoader` está diseñado para cargar modelos GLIGEN, que son modelos generativos especializados. Facilita el proceso de recuperación e inicialización de estos modelos desde rutas especificadas, haciéndolos listos para tareas generativas adicionales.

## Entradas

| Campo         | Comfy dtype       | Descripción                                                                       |
|---------------|-------------------|-----------------------------------------------------------------------------------|
| `gligen_name` | `COMBO[STRING]`   | El nombre del modelo GLIGEN a cargar, especificando qué archivo de modelo recuperar y cargar, crucial para la inicialización del modelo GLIGEN. |

## Salidas

| Campo   | Data Type | Descripción                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `gligen`| `GLIGEN`    | El modelo GLIGEN cargado, listo para su uso en tareas generativas, representando el modelo completamente inicializado cargado desde la ruta especificada. |
