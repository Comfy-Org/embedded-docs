Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/controlnet`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

El nodo DiffControlNetLoader está diseñado para cargar redes de control diferenciales, que son modelos especializados que pueden modificar el comportamiento de otro modelo basado en especificaciones de redes de control. Este nodo permite el ajuste dinámico de comportamientos de modelos aplicando redes de control diferenciales, facilitando la creación de salidas de modelos personalizadas.

## Entradas

| Campo               | Comfy dtype       | Descripción                                                                                 |
|---------------------|-------------------|---------------------------------------------------------------------------------------------|
| `model`             | `MODEL`           | El modelo base al que se aplicará la red de control diferencial, permitiendo la personalización del comportamiento del modelo. |
| `control_net_name`  | `COMBO[STRING]`    | Identifica la red de control diferencial específica que se cargará y aplicará al modelo base para modificar su comportamiento. |

## Salidas

| Campo          | Comfy dtype   | Descripción                                                                   |
|----------------|---------------|-------------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET` | Una red de control diferencial que ha sido cargada y está lista para ser aplicada a un modelo base para la modificación de su comportamiento. |
