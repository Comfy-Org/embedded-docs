> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompare/es.md)

El nodo Image Compare proporciona una interfaz visual para comparar dos imágenes lado a lado mediante un control deslizante. Está diseñado como un nodo de salida, lo que significa que no transfiere datos a otros nodos, sino que muestra las imágenes directamente en la interfaz de usuario para su inspección.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen_a` | IMAGE | No | - | La primera imagen a comparar. |
| `imagen_b` | IMAGE | No | - | La segunda imagen a comparar. |
| `vista_comparar` | IMAGECOMPARE | Sí | - | El control que habilita la vista de comparación con deslizador en la interfaz de usuario. |

**Nota:** Este nodo es un nodo de salida. Aunque `image_a` y `image_b` son opcionales, se debe proporcionar al menos una imagen para que el nodo tenga un efecto visible. El nodo mostrará un área vacía para cualquier entrada de imagen que no esté conectada.

## Salidas

Este nodo es un nodo de salida y no produce ninguna salida de datos para usar en otros nodos. Su función es mostrar las imágenes proporcionadas en la interfaz de ComfyUI.

---
**Source fingerprint (SHA-256):** `2bc980cd20aad3cf60300868599bbce8eaba1cdb21880d2b3f4cd628108d8139`
