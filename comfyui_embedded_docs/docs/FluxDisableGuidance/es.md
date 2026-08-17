# FluxDisableGuidance

Este nodo desactiva por completo la funcionalidad de incorporación de guía para Flux y modelos similares a Flux. Toma datos de condicionamiento como entrada, elimina el componente de guía estableciéndolo en None y devuelve los datos de condicionamiento modificados, desactivando eficazmente el condicionamiento basado en guía para el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `conditioning` | Los datos de condicionamiento que se procesarán y de los que se eliminará la guía | CONDITIONING | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados con la guía desactivada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/es.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
