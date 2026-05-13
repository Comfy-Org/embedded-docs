> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/es.md)

Este nodo establece el latente guía para un modelo de edición. Toma datos de condicionamiento y una entrada latente opcional, luego modifica el condicionamiento para incluir información de latente de referencia. Si el modelo lo admite, puedes encadenar múltiples nodos ReferenceLatent para establecer múltiples imágenes de referencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento que se modificarán con información de latente de referencia |
| `latent` | LATENT | No | - | Datos latentes opcionales para usar como referencia para el modelo de edición |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | CONDITIONING | Los datos de condicionamiento modificados que contienen información de latente de referencia |

---
**Source fingerprint (SHA-256):** `d233778cfa7d6f057509f93f8445a0bbf151308e430fc50e28577f48cf136b53`
