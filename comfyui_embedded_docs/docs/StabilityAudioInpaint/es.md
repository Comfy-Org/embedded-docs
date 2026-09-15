# StabilityAudioInpaint

Transforma parte de una muestra de audio existente mediante instrucciones de texto. Este nodo permite modificar secciones específicas de audio proporcionando indicaciones descriptivas, efectivamente haciendo "inpainting" o regenerando porciones seleccionadas mientras se preserva el resto del audio.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo de IA que se usará para el inpainting de audio. | STRING | Sí | `"stable-audio-2.5"` |
| `prompt` | Descripción de texto que guía cómo debe transformarse el audio (predeterminado: vacío). La longitud máxima es de 10,000 caracteres. | STRING | Sí |  |
| `audio` | Archivo de audio de entrada que se va a transformar. El audio debe durar entre 6 y 190 segundos. | AUDIO | Sí |  |
| `duration` | Controla la duración en segundos del audio generado (predeterminado: 190). | INT | No | 1 a 190 |
| `seed` | Semilla aleatoria utilizada para la generación (predeterminado: 0). | INT | No | 0 a 4294967294 |
| `steps` | Controla el número de pasos de muestreo (predeterminado: 8). | INT | No | 4 a 8 |
| `mask_start` | Posición inicial en segundos de la sección de audio que se va a transformar (predeterminado: 30). | INT | No | 0 a 190 |
| `mask_end` | Posición final en segundos de la sección de audio que se va a transformar (predeterminado: 190). | INT | No | 0 a 190 |

**Nota:** El valor de `mask_end` debe ser mayor que el valor de `mask_start`. El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `audio` | La salida de audio transformada con la sección especificada modificada según la indicación. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/es.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`
