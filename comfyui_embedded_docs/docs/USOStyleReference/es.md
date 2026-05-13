> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/es.md)

El nodo USOStyleReference aplica parches de referencia de estilo a modelos utilizando características de imagen codificadas provenientes de la salida de CLIP vision. Crea una versión modificada del modelo de entrada incorporando información de estilo extraída de entradas visuales, lo que permite capacidades de transferencia de estilo o generación basada en referencias.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base al que se le aplicará el parche de referencia de estilo |
| `model_patch` | MODEL_PATCH | Sí | - | El parche de modelo que contiene la información de referencia de estilo |
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sí | - | Las características visuales codificadas extraídas del procesamiento de CLIP vision |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con los parches de referencia de estilo aplicados |

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
