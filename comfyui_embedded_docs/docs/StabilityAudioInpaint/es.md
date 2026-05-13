> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/es.md)

Transforma parte de una muestra de audio existente utilizando instrucciones de texto. Este nodo permite modificar secciones específicas de audio proporcionando descripciones indicativas, efectivamente "inpainting" o regenerando porciones seleccionadas mientras se preserva el resto del audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | "stable-audio-2.5" | El modelo de IA a utilizar para el inpainting de audio. |
| `prompt` | STRING | Sí | | Descripción textual que guía cómo debe transformarse el audio (por defecto: vacío). |
| `audio` | AUDIO | Sí | | Archivo de audio de entrada a transformar. El audio debe tener una duración entre 6 y 190 segundos. |
| `duración` | INT | No | 1-190 | Controla la duración en segundos del audio generado (por defecto: 190). |
| `semilla` | INT | No | 0-4294967294 | La semilla aleatoria utilizada para la generación (por defecto: 0). |
| `pasos` | INT | No | 4-8 | Controla el número de pasos de muestreo (por defecto: 8). |
| `máscara_inicio` | INT | No | 0-190 | Posición de inicio en segundos para la sección de audio a transformar (por defecto: 30). |
| `máscara_fin` | INT | No | 0-190 | Posición de finalización en segundos para la sección de audio a transformar (por defecto: 190). |

**Nota:** El valor de `mask_end` debe ser mayor que el valor de `mask_start`. El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `audio` | AUDIO | La salida de audio transformada con la sección especificada modificada según el prompt. |

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
