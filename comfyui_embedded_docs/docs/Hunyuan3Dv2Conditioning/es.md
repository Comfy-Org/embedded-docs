El nodo Hunyuan3Dv2Conditioning procesa la salida de CLIP vision para generar datos de condicionamiento para modelos 3D. Extrae las incrustaciones del último estado oculto de la salida visual y crea pares de condicionamiento tanto positivos como negativos. El condicionamiento positivo utiliza las incrustaciones reales, mientras que el condicionamiento negativo utiliza incrustaciones con valor cero de la misma forma.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `salida_vision_clip` | La salida de un modelo CLIP vision que contiene incrustaciones visuales | CLIP_VISION_OUTPUT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negative` | Datos de condicionamiento positivo que contienen las incrustaciones de CLIP vision | CONDITIONING |
| `negative` | Datos de condicionamiento negativo que contienen incrustaciones con valor cero que coinciden con la forma de las incrustaciones positivas | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
