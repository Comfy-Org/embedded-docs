Transforma muestras de audio existentes en nuevas composiciones de alta calidad utilizando instrucciones de texto. Este nodo toma un archivo de audio de entrada y lo modifica según tu indicación de texto para crear nuevo contenido de audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la transformación de audio | COMBO | Sí | "stable-audio-2.5"<br> |
| `prompt` | Instrucciones de texto que describen cómo transformar el audio (predeterminado: vacío) | STRING | Sí |  |
| `audio` | El audio debe tener una duración entre 6 y 190 segundos | AUDIO | Sí |  |
| `duración` | Controla la duración en segundos del audio generado (predeterminado: 190) | INT | No | 1-190 |
| `semilla` | La semilla aleatoria utilizada para la generación (predeterminado: 0) | INT | No | 0-4294967294 |
| `pasos` | Controla el número de pasos de muestreo (predeterminado: 8) | INT | No | 4-8 |
| `intensidad` | El parámetro controla cuánta influencia tiene el parámetro de audio sobre el audio generado (predeterminado: 1.0) | FLOAT | No | 0.01-1.0 |

**Nota:** El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio` | El audio transformado generado a partir del audio de entrada y la indicación de texto | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/es.md)

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`
