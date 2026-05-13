> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/es.md)

El nodo Hunyuan3Dv2Conditioning procesa la salida de CLIP vision para generar datos de condicionamiento para modelos 3D. Extrae las incrustaciones del último estado oculto de la salida visual y crea pares de condicionamiento tanto positivos como negativos. El condicionamiento positivo utiliza las incrustaciones reales, mientras que el condicionamiento negativo utiliza incrustaciones con valor cero de la misma forma.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `salida_vision_clip` | CLIP_VISION_OUTPUT | Sí | - | La salida de un modelo CLIP vision que contiene incrustaciones visuales |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negative` | CONDITIONING | Datos de condicionamiento positivo que contienen las incrustaciones de CLIP vision |
| `negative` | CONDITIONING | Datos de condicionamiento negativo que contienen incrustaciones con valor cero que coinciden con la forma de las incrustaciones positivas |

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
