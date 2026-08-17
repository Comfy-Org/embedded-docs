# MaskPreview

El nodo MaskPreview muestra una vista previa visual de los datos de máscara directamente en la interfaz de ComfyUI, para que puedas inspeccionar las máscaras durante tu flujo de trabajo. Muestra la vista previa sin guardarla en el directorio de salida de ComfyUI y pasa la máscara como salida.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `mask` | Los datos de máscara que se van a previsualizar | MASK | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo de salida (predeterminado: "ComfyUI") | STRING | No | - |
| `prompt` | Información de prompt para metadatos (proporcionada automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Información PNG adicional para metadatos (proporcionada automáticamente) | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
|-------------|-------------|-----------|
| `mask` | Los datos de máscara que se previsualizaron, pasados sin cambios | MASK |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/es.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
