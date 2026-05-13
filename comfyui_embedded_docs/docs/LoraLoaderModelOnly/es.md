> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/es.md)

Este nodo detecta los modelos ubicados en la carpeta `ComfyUI/models/loras`, y también leerá modelos desde rutas adicionales configuradas en el archivo extra_model_paths.yaml. En ocasiones, es posible que necesites **actualizar la interfaz de ComfyUI** para que pueda leer los archivos de modelo desde la carpeta correspondiente.

Este nodo se especializa en cargar un modelo LoRA sin requerir un modelo CLIP, enfocándose en mejorar o modificar un modelo determinado según los parámetros de LoRA. Permite el ajuste dinámico de la intensidad del modelo mediante parámetros LoRA, facilitando un control preciso sobre el comportamiento del modelo.

## Entradas

| Campo             | Tipo Comfy        | Descripción                                                                                   |
|-------------------|-------------------|-----------------------------------------------------------------------------------------------|
| `model`           | `MODEL`           | El modelo base para las modificaciones, al cual se aplicarán los ajustes de LoRA.              |
| `lora_name`       | `COMBO[STRING]`   | El nombre del archivo LoRA que se cargará, especificando los ajustes a aplicar al modelo.      |
| `strength_model`  | `FLOAT`           | Determina la intensidad de los ajustes de LoRA; valores más altos indican modificaciones más fuertes. |

## Salidas

| Campo   | Tipo de Dato | Descripción                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | El modelo modificado con los ajustes de LoRA aplicados, reflejando cambios en el comportamiento o las capacidades del modelo. |