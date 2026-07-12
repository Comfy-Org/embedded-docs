# Crear Cajas Delimitadoras

Dibuja cajas delimitadoras en un lienzo. Genera elementos de prompt Ideogram, cajas delimitadoras en espacio de píxeles y una imagen de vista previa.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `fondo` | Imagen opcional utilizada como fondo en el lienzo y la vista previa. | IMAGE | No | - |
| `bboxes` | Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `ancho` | Ancho del lienzo y de la cuadrícula de píxeles para las cajas delimitadoras. | INT | Yes | 64 to 16384 (step: 16) |
| `alto` | Alto del lienzo y de la cuadrícula de píxeles para las cajas delimitadoras. | INT | Yes | 64 to 16384 (step: 16) |
| `estado_del_editor` | Dibuja cajas delimitadoras y asigna a cada caja su tipo, texto, descripción y paleta de colores. Comienza con el elemento de fondo y termina con el primer plano. | BOUNDING_BOXES | Yes | - |
| `last_incoming` | Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run. | BOUNDING_BOXES | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `preview` | An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text. | IMAGE |
| `bboxes` | A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values. | BOUNDING_BOX |
| `elements` | A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette. | ARRAY |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/es.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
