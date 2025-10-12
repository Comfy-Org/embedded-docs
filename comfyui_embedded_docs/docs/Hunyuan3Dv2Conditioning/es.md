> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/es.md)

El nodo Hunyuan3Dv2Conditioning procesa la salida de visión CLIP para generar datos de condicionamiento para modelos de video. Extrae las incrustaciones del último estado oculto de la salida de visión y crea pares de condicionamiento tanto positivos como negativos. El condicionamiento positivo utiliza las incrustaciones reales mientras que el condicionamiento negativo utiliza incrustaciones de valor cero con la misma forma.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `salida_vision_clip` | CLIP_VISION_OUTPUT | Sí | - | La salida de un modelo de visión CLIP que contiene incrustaciones visuales |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Datos de condicionamiento positivo que contienen las incrustaciones de visión CLIP |
| `negative` | CONDITIONING | Datos de condicionamiento negativo que contienen incrustaciones de valor cero que coinciden con la forma de las incrustaciones positivas |
