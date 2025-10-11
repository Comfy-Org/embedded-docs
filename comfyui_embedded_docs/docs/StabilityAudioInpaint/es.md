> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/es.md)

Transforma parte de una muestra de audio existente utilizando instrucciones de texto. Este nodo permite modificar secciones específicas del audio proporcionando prompts descriptivos, efectivamente "reparando" o regenerando porciones seleccionadas mientras se preserva el resto del audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "stable-audio-2.5"<br> | El modelo de IA a utilizar para la reparación de audio. |
| `prompt` | STRING | Sí |  | Descripción textual que guía cómo debe transformarse el audio (valor por defecto: vacío). |
| `audio` | AUDIO | Sí |  | Archivo de audio de entrada a transformar. El audio debe tener una duración entre 6 y 190 segundos. |
| `duration` | INT | No | 1-190 | Controla la duración en segundos del audio generado (valor por defecto: 190). |
| `seed` | INT | No | 0-4294967294 | La semilla aleatoria utilizada para la generación (valor por defecto: 0). |
| `steps` | INT | No | 4-8 | Controla el número de pasos de muestreo (valor por defecto: 8). |
| `mask_start` | INT | No | 0-190 | Posición inicial en segundos para la sección de audio a transformar (valor por defecto: 30). |
| `mask_end` | INT | No | 0-190 | Posición final en segundos para la sección de audio a transformar (valor por defecto: 190). |

**Nota:** El valor de `mask_end` debe ser mayor que el valor de `mask_start`. El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | La salida de audio transformada con la sección especificada modificada según el prompt. |