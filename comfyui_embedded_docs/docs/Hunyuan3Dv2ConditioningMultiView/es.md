# Hunyuan3Dv2ConditioningMultiView

El nodo `Hunyuan3Dv2ConditioningMultiView` procesa embeddings de visión CLIP multivista para la generación de video 3D. Acepta embeddings opcionales de las vistas frontal, izquierda, trasera y derecha, y añade codificación posicional a cada vista proporcionada antes de combinarlos en una secuencia de condicionamiento única. El nodo produce tanto un condicionamiento positivo a partir de los embeddings combinados como un condicionamiento negativo con valores cero.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `front` | Salida de visión CLIP para la vista frontal | CLIP_VISION_OUTPUT | No | - |
| `left` | Salida de visión CLIP para la vista izquierda | CLIP_VISION_OUTPUT | No | - |
| `back` | Salida de visión CLIP para la vista trasera | CLIP_VISION_OUTPUT | No | - |
| `right` | Salida de visión CLIP para la vista derecha | CLIP_VISION_OUTPUT | No | - |

**Nota:** Debe proporcionarse al menos una entrada de vista para que el nodo funcione. El nodo solo procesa las vistas que contienen datos válidos de salida de visión CLIP. Cada vista proporcionada recibe una codificación posicional según su posición (frontal, izquierda, trasera, derecha), y las vistas codificadas se concatenan en ese mismo orden.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo que contiene los embeddings multivista combinados con codificación posicional | CONDITIONING |
| `negative` | Condicionamiento negativo que contiene valores cero con la misma forma que el condicionamiento positivo | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/es.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
