> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/en.md)

Nodo de Prueba Virtual Kling. Ingresa una imagen de una persona y una imagen de una prenda para probar la prenda en la persona. Puedes fusionar varias imágenes de prendas de vestir en una sola imagen con fondo blanco.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `human_image` | IMAGE | Sí | - | La imagen de la persona para probar la ropa |
| `cloth_image` | IMAGE | Sí | - | La imagen de la prenda para probar en la persona |
| `model_name` | STRING | Sí | `"kolors-virtual-try-on-v1"` | El modelo de prueba virtual a utilizar (predeterminado: "kolors-virtual-try-on-v1") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | IMAGE | La imagen resultante que muestra a la persona con la prenda de vestir probada |

---
**Source fingerprint (SHA-256):** `bfd0da440d3ad85e15ce16851313f2e75421a8a3eb5e4c651350432955afc731`
