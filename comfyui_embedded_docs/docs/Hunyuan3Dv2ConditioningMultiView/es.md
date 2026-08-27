# Hunyuan3Dv2ConditioningMultiView

El nodo Hunyuan3Dv2ConditioningMultiView combina las salidas de visión CLIP de hasta cuatro vistas (frontal, izquierda, trasera y derecha) en un único acondicionamiento multivista. Cada vista proporcionada tiene una codificación posicional añadida a su embedding de visión CLIP, y los embeddings resultantes se concatenan. El nodo genera un acondicionamiento positivo basado en los embeddings combinados y un acondicionamiento negativo lleno de ceros de la misma forma.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `frente` | Salida de visión CLIP para la vista frontal. Entrada de vista opcional. | CLIP_VISION_OUTPUT | No | - |
| `izquierda` | Salida de visión CLIP para la vista izquierda. Entrada de vista opcional. | CLIP_VISION_OUTPUT | No | - |
| `atrás` | Salida de visión CLIP para la vista trasera. Entrada de vista opcional. | CLIP_VISION_OUTPUT | No | - |
| `derecha` | Salida de visión CLIP para la vista derecha. Entrada de vista opcional. | CLIP_VISION_OUTPUT | No | - |

**Nota:** Al menos una entrada de vista debe proporcionarse para que el nodo funcione. El nodo solo procesa las vistas que contienen datos válidos de salida de visión CLIP y omite las vistas que no están conectadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Acondicionamiento positivo que contiene los embeddings multivista combinados con codificación posicional. | CONDITIONING |
| `negative` | Acondicionamiento negativo con valores cero que coinciden con la forma del acondicionamiento positivo. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/es.md)

---
**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`
