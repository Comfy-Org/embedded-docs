> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/es.md)

Transforma muestras de audio existentes en nuevas composiciones de alta calidad utilizando instrucciones de texto. Este nodo toma un archivo de audio de entrada y lo modifica basándose en tu indicación textual para crear nuevo contenido de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "stable-audio-2.5"<br> | El modelo de IA a utilizar para la transformación de audio |
| `prompt` | STRING | Sí |  | Instrucciones de texto que describen cómo transformar el audio (valor por defecto: vacío) |
| `audio` | AUDIO | Sí |  | El audio debe tener una duración entre 6 y 190 segundos |
| `duration` | INT | No | 1-190 | Controla la duración en segundos del audio generado (valor por defecto: 190) |
| `seed` | INT | No | 0-4294967294 | La semilla aleatoria utilizada para la generación (valor por defecto: 0) |
| `steps` | INT | No | 4-8 | Controla el número de pasos de muestreo (valor por defecto: 8) |
| `strength` | FLOAT | No | 0.01-1.0 | Este parámetro controla cuánta influencia tiene el parámetro de audio en el audio generado (valor por defecto: 1.0) |

**Nota:** El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El audio transformado generado basándose en el audio de entrada y la indicación textual |
