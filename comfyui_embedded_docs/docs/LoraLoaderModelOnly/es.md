Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/loras`,
y también leerá los modelos de las rutas adicionales que hayas configurado en el archivo extra_model_paths.yaml.
A veces, es posible que necesites **refrescar la interfaz de ComfyUI** para que pueda leer los archivos de modelo en la carpeta correspondiente.

Este nodo se especializa en cargar un modelo LoRA sin requerir un modelo CLIP, enfocándose en mejorar o modificar un modelo dado basado en parámetros LoRA. Permite el ajuste dinámico de la intensidad del modelo a través de parámetros LoRA, facilitando un control preciso sobre el comportamiento del modelo.

## Entradas

| Campo             | Comfy dtype       | Descripción                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | El modelo base para modificaciones, al cual se aplicarán los ajustes LoRA.                   |
| `lora_name`       | `COMBO[STRING]`   | El nombre del archivo LoRA a cargar, especificando los ajustes a aplicar al modelo.      |
| `strength_model`  | `FLOAT`           | Determina la intensidad de los ajustes LoRA, con valores más altos indicando modificaciones más fuertes. |

## Salidas

| Campo   | Data Type | Descripción                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | El modelo modificado con ajustes LoRA aplicados, reflejando cambios en el comportamiento o capacidades del modelo. |
