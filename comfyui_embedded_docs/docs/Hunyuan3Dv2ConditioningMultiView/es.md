# Hunyuan3Dv2ConditioningMultiView

El nodo `Hunyuan3Dv2ConditioningMultiView` procesa embeddings de visión CLIP multivista para la generación de video 3D. Toma embeddings opcionales de las vistas frontal, izquierda, trasera y derecha, y los combina con codificación posicional para crear datos de condicionamiento para modelos de video. El nodo genera tanto condicionamiento positivo a partir de los embeddings combinados como condicionamiento negativo con valores cero.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `frente` | Salida de visión CLIP para la vista frontal | CLIP_VISION_OUTPUT | No | - |
| `izquierda` | Salida de visión CLIP para la vista izquierda | CLIP_VISION_OUTPUT | No | - |
| `atrás` | Salida de visión CLIP para la vista trasera | CLIP_VISION_OUTPUT | No | - |
| `derecha` | Salida de visión CLIP para la vista derecha | CLIP_VISION_OUTPUT | No | - |

**Nota:** Se debe proporcionar al menos una entrada de vista para que el nodo funcione. El nodo solo procesará las vistas que contengan datos válidos de salida de visión CLIP.


| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo que contiene los embeddings multivista combinados con codificación posicional | CONDITIONING |
| `negative` | Condicionamiento negativo con valores cero para aprendizaje contrastivo | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/es.md)

---
**Source fingerprint (SHA-256):** `01998ae9ba7d2ae9a2f6a0b5aee4c03168f935fb9769317cd80d93a7a4b96f13`
