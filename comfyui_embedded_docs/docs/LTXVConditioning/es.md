> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/es.md)

El nodo LTXVConditioning agrega información de tasa de cuadros (frame rate) tanto a las entradas de condicionamiento positivo como negativo para modelos de generación de video. Toma los datos de condicionamiento existentes y aplica el valor de tasa de cuadros especificado a ambos conjuntos de condicionamiento, haciéndolos adecuados para el procesamiento de modelos de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo que recibirá la información de tasa de cuadros |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo que recibirá la información de tasa de cuadros |
| `frame_rate` | FLOAT | No | 0.0 - 1000.0 | El valor de tasa de cuadros a aplicar a ambos conjuntos de condicionamiento (valor por defecto: 25.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo con la información de tasa de cuadros aplicada |
| `negative` | CONDITIONING | El condicionamiento negativo con la información de tasa de cuadros aplicada |