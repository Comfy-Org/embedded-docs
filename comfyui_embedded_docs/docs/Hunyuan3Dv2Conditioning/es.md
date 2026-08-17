# Hunyuan3Dv2Conditioning

El nodo Hunyuan3Dv2Conditioning procesa la salida de visión de CLIP para generar datos de condicionamiento para modelos 3D. Extrae las incrustaciones del último estado oculto de la salida de visión y crea pares de condicionamiento positivo y negativo. El condicionamiento positivo utiliza las incrustaciones reales, mientras que el condicionamiento negativo utiliza incrustaciones con valor cero de la misma forma.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | La salida de un modelo de visión CLIP que contiene incrustaciones visuales | CLIP_VISION_OUTPUT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
| --- | --- | --- |
| `positive` | Datos de condicionamiento positivo que contienen las incrustaciones de visión de CLIP | CONDITIONING |
| `negative` | Datos de condicionamiento negativo que contienen incrustaciones con valor cero que coinciden con la forma de las incrustaciones positivas | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
