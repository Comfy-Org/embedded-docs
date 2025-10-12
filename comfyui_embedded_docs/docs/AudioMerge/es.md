> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/es.md)

El nodo AudioMerge combina dos pistas de audio superponiendo sus formas de onda. Coincide automáticamente las tasas de muestreo de ambas entradas de audio y ajusta sus longitudes para que sean iguales antes de la fusión. El nodo proporciona varios métodos matemáticos para combinar las señales de audio y garantiza que la salida se mantenga dentro de niveles de volumen aceptables.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | requerida | - | - | Primera entrada de audio a fusionar |
| `audio2` | AUDIO | requerida | - | - | Segunda entrada de audio a fusionar |
| `merge_method` | COMBO | requerida | - | ["add", "mean", "subtract", "multiply"] | El método utilizado para combinar las formas de onda de audio. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | La salida de audio fusionada que contiene la forma de onda combinada y la tasa de muestreo |
