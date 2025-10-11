> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/es.md)

El nodo USOStyleReference aplica parches de referencia de estilo a modelos utilizando características de imagen codificadas desde la salida de visión CLIP. Crea una versión modificada del modelo de entrada incorporando información de estilo extraída de entradas visuales, permitiendo capacidades de transferencia de estilo o generación basada en referencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base al que se aplicará el parche de referencia de estilo |
| `model_patch` | MODEL_PATCH | Sí | - | El parche del modelo que contiene la información de referencia de estilo |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sí | - | Las características visuales codificadas extraídas del procesamiento de visión CLIP |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con los parches de referencia de estilo aplicados |