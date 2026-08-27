# ReferenciaDeEstiloUSO

El nodo USOStyleReference aplica una referencia de estilo a un modelo combinando las características de visión de CLIP con un parche de modelo, y devuelve una copia parcheada del modelo de entrada. Está diseñado para modelos Flux y está marcado como experimental. La información de estilo visual se combina con el condicionamiento de texto del modelo para que pueda influir en la generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base al que se le aplica el parche de referencia de estilo. | MODEL | Sí | - |
| `parche_del_modelo` | El parche de modelo que contiene el modelo de proyección utilizado para codificar las características de la imagen de referencia. | MODEL_PATCH | Sí | - |
| `salida_de_visión_clip` | Las características visuales codificadas extraídas del procesamiento de visión CLIP de la imagen de referencia. | CLIP_VISION_OUTPUT | Sí | - |

Nota: El `clip_vision_output` debe provenir de un modelo de visión CLIP que proporcione los estados ocultos completos y el penúltimo estado oculto. El nodo combina los estados ocultos vigésimo desde el último, undécimo desde el último y penúltimo en la incrustación de estilo. El `model_patch` debe exponer un modelo de proyección a través de su atributo `model` que convierta estas características de imagen en la incrustación de estilo. Durante el muestreo, la incrustación de estilo se antepone al condicionamiento de texto para que pueda influir en la generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el parche de referencia de estilo aplicado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/es.md)

---
**Source fingerprint (SHA-256):** `9033dddb76fafb388c67dcd09d96102a7ab3e5bc416cec61bf18d088da37a0f0`
