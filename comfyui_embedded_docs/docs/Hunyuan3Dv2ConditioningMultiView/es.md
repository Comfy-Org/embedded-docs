> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/es.md)

El nodo Hunyuan3Dv2ConditioningMultiView procesa incrustaciones de visión CLIP multivista para la generación de vídeos 3D. Toma incrustaciones opcionales de vista frontal, izquierda, posterior y derecha y las combina con codificación posicional para crear datos de condicionamiento para modelos de vídeo. El nodo genera tanto condicionamiento positivo a partir de las incrustaciones combinadas como condicionamiento negativo con valores cero.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP para la vista frontal |
| `left` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP para la vista izquierda |
| `back` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP para la vista posterior |
| `right` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP para la vista derecha |

**Nota:** Se debe proporcionar al menos una entrada de vista para que el nodo funcione. El nodo solo procesará las vistas que contengan datos válidos de salida de visión CLIP.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo que contiene las incrustaciones multivista combinadas con codificación posicional |
| `negative` | CONDITIONING | Condicionamiento negativo con valores cero para aprendizaje contrastivo |