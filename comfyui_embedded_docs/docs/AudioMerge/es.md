> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/es.md)

El nodo AudioMerge combina dos pistas de audio superponiendo sus formas de onda. Automáticamente iguala las frecuencias de muestreo de ambas entradas de audio y ajusta sus duraciones para que sean iguales antes de la fusión. El nodo proporciona varios métodos matemáticos para combinar las señales de audio y garantiza que la salida se mantenga dentro de niveles de volumen aceptables.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio1` | AUDIO | Sí | - | Primera entrada de audio a fusionar |
| `audio2` | AUDIO | Sí | - | Segunda entrada de audio a fusionar |
| `método_combinación` | COMBO | Sí | `"add"`<br>`"mean"`<br>`"subtract"`<br>`"multiply"` | Método utilizado para combinar las formas de onda de audio. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `AUDIO` | AUDIO | La salida de audio fusionada que contiene la forma de onda combinada y la frecuencia de muestreo |

---
**Source fingerprint (SHA-256):** `2a4a7da42835efd03cc67002e617a70c0514524a0ac0ed61d57e499c1283be95`
