> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/es.md)

El nodo DualCLIPLoader está diseñado para cargar dos modelos CLIP simultáneamente, facilitando operaciones que requieren la integración o comparación de características de ambos modelos.

Este nodo detectará los modelos ubicados en la carpeta `ComfyUI/models/text_encoders`.

## Entradas

| Parámetro     | Tipo Comfy      | Descripción                                                                                                                                                                                         |
| ------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clip_name1`  | COMBO[STRING]   | Especifica el nombre del primer modelo CLIP a cargar. Este parámetro es crucial para identificar y recuperar el modelo correcto de una lista predefinida de modelos CLIP disponibles.               |
| `clip_name2`  | COMBO[STRING]   | Especifica el nombre del segundo modelo CLIP a cargar. Este parámetro permite cargar un segundo modelo CLIP distinto para realizar análisis comparativos o integradores junto con el primer modelo. |
| `type`        | `option`        | Elija entre "sdxl", "sd3", "flux" para adaptarse a diferentes modelos.                                                                                                                              |

* El orden de carga no afecta el resultado de salida

## Salidas

| Parámetro | Tipo de Dato | Descripción                                                                                                                       |
| --------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `clip`    | CLIP         | La salida es un modelo CLIP combinado que integra las características o funcionalidades de los dos modelos CLIP especificados.    |