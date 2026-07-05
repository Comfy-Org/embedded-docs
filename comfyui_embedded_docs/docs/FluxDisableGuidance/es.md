# FluxDisableGuidance

Este nodo desactiva por completo la funcionalidad de guía integrada para Flux y modelos similares. Toma datos de condicionamiento como entrada y elimina el componente de guía estableciéndolo en None, desactivando efectivamente el condicionamiento basado en guía para el proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento a procesar y de los cuales eliminar la guía | CONDITIONING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento modificados con la guía desactivada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/es.md)

---
**Source fingerprint (SHA-256):** `37e544460d5e50542cebb451997c0320f16d822cc5695cb34825d2038866a455`
