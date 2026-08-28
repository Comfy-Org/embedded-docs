# Latente de Referencia

Este nodo establece el latente de guía para un modelo de edición. Toma datos de condicionamiento y una entrada latente opcional, luego modifica el condicionamiento para incluir información latente de referencia. Si el modelo lo admite, puedes encadenar múltiples nodos ReferenceLatent para establecer múltiples imágenes de referencia.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `condicionamiento` | Los datos de condicionamiento que se modificarán con información latente de referencia | CONDITIONING | Sí | - |
| `latente` | Datos latentes opcionales para usar como referencia para el modelo de edición. Si no se proporcionan, el condicionamiento se devuelve sin cambios | LATENT | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | Los datos de condicionamiento modificados que contienen información latente de referencia | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/es.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
