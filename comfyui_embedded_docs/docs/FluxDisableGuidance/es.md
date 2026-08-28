# FluxDisableGuidance

Este nodo desactiva por completo la incrustación de guía en modelos Flux y similares. Toma datos de condicionamiento como entrada y elimina el componente de guía estableciéndolo en None, desactivando efectivamente el condicionamiento basado en guía para el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento que se procesarán y a los que se les eliminará la guía | CONDITIONING | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados con la guía desactivada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/es.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
