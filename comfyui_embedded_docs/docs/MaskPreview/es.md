# MaskPreview

El nodo MaskPreview muestra una vista previa visual de los datos de máscara directamente en la interfaz de ComfyUI, sin guardarlos en el directorio de salida. Esto le permite inspeccionar los valores exactos de la máscara en cualquier punto de su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `mask` | Los datos de máscara para previsualizar | MASK | Sí | - |
| `filename_prefix` | Prefijo para el nombre de archivo de la vista previa (predeterminado: "ComfyUI") | STRING | No | - |
| `prompt` | Información de prompt para metadatos (proporcionada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Información PNG adicional para metadatos (proporcionada automáticamente) | EXTRA_PNGINFO | No | - |

Las entradas `prompt` y `extra_pnginfo` están ocultas y son proporcionadas automáticamente por el sistema de ComfyUI; no necesita conectarlas manualmente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `mask` | Los datos de máscara que se previsualizaron, devueltos sin cambios para su uso posterior en el flujo de trabajo | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/es.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
