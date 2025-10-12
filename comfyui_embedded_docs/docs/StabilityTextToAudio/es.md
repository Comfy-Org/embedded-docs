> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/es.md)

Genera música y efectos de sonido de alta calidad a partir de descripciones de texto. Este nodo utiliza la tecnología de generación de audio de Stability AI para crear contenido de audio basado en tus indicaciones de texto.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"stable-audio-2.5"` | El modelo de generación de audio a utilizar (predeterminado: "stable-audio-2.5") |
| `prompt` | STRING | Sí | - | La descripción de texto utilizada para generar el contenido de audio (predeterminado: cadena vacía) |
| `duration` | INT | No | 1-190 | Controla la duración en segundos del audio generado (predeterminado: 190) |
| `seed` | INT | No | 0-4294967294 | La semilla aleatoria utilizada para la generación (predeterminado: 0) |
| `steps` | INT | No | 4-8 | Controla el número de pasos de muestreo (predeterminado: 8) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El archivo de audio generado basado en la indicación de texto |
