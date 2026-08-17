# ReferenciaDeEstiloUSO

El nodo USOStyleReference aplica información de estilo de una imagen de referencia a un modelo Flux. Construye un embedding de estilo a partir de la salida de visión de CLIP y luego parchea un clon del modelo para que, durante la generación, el embedding de estilo se inserte delante del condicionamiento del prompt de texto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo base al que se le aplica el parche de referencia de estilo | MODEL | Sí | - |
| `model_patch` | El parche del modelo que contiene la información de referencia de estilo | MODEL_PATCH | Sí | - |
| `clip_vision_output` | Las características visuales codificadas extraídas del procesamiento de visión de CLIP. El nodo combina los estados ocultos de las capas -20 y -11 junto con los estados ocultos penúltimos para construir el embedding de estilo | CLIP_VISION_OUTPUT | Sí | - |

Nota: Las tres entradas son requeridas. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el parche de referencia de estilo aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/es.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
