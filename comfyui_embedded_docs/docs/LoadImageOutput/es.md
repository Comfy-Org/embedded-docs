> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/es.md)

El nodo LoadImageOutput carga imágenes desde la carpeta de salida. Al hacer clic en el botón de actualizar, actualiza la lista de imágenes disponibles y selecciona automáticamente la primera, facilitando la iteración a través de las imágenes generadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | COMBO | Sí | Múltiples opciones disponibles | Carga una imagen desde la carpeta de salida. Incluye una opción de carga y un botón de actualizar para renovar la lista de imágenes. Al hacer clic en el botón de actualizar, el nodo actualizará la lista de imágenes y seleccionará automáticamente la primera, permitiendo una iteración sencilla. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | La imagen cargada desde la carpeta de salida |
| `mask` | MASK | La máscara asociada a la imagen cargada |

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
