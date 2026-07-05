# ReferenciaDeEstiloUSO

El nodo USOStyleReference aplica parches de referencia de estilo a modelos utilizando características de imagen codificadas provenientes de la salida de CLIP vision. Crea una versión modificada del modelo de entrada incorporando información de estilo extraída de entradas visuales, lo que permite capacidades de transferencia de estilo o generación basada en referencias.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base al que se le aplicará el parche de referencia de estilo | MODEL | Sí | - |
| `parche_del_modelo` | El parche de modelo que contiene la información de referencia de estilo | MODEL_PATCH | Sí | - |
| `salida_de_visión_clip` | Las características visuales codificadas extraídas del procesamiento de CLIP vision | CLIP_VISION_OUTPUT | Sí | - |


| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con los parches de referencia de estilo aplicados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/es.md)

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
