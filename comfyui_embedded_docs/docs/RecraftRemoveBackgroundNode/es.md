> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/en.md)

Este nodo elimina el fondo de las imágenes utilizando el servicio API de Recraft. Procesa cada imagen del lote de entrada y devuelve tanto las imágenes procesadas con fondos transparentes como las máscaras alfa correspondientes que indican las áreas de fondo eliminadas.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La(s) imagen(es) de entrada para procesar la eliminación del fondo |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | Imágenes procesadas con fondos transparentes |
| `mask` | MASK | Máscaras del canal alfa que indican las áreas de fondo eliminadas |

---
**Source fingerprint (SHA-256):** `9e3f1a0471da3afda6b8de26de3b7e78c1070c49ab49e4fc8b6b79bb10ff77de`
