# Reconstrucción de audio Stability AI

Transforma parte de una muestra de audio existente utilizando instrucciones de texto. Este nodo permite modificar secciones específicas de audio proporcionando descripciones indicativas, efectivamente "inpainting" o regenerando porciones seleccionadas mientras se preserva el resto del audio.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para el inpainting de audio. | COMBO | Sí | "stable-audio-2.5" |
| `prompt` | Descripción textual que guía cómo debe transformarse el audio (por defecto: vacío). | STRING | Sí |  |
| `audio` | Archivo de audio de entrada a transformar. El audio debe tener una duración entre 6 y 190 segundos. | AUDIO | Sí |  |
| `duración` | Controla la duración en segundos del audio generado (por defecto: 190). | INT | No | 1-190 |
| `semilla` | La semilla aleatoria utilizada para la generación (por defecto: 0). | INT | No | 0-4294967294 |
| `pasos` | Controla el número de pasos de muestreo (por defecto: 8). | INT | No | 4-8 |
| `máscara_inicio` | Posición de inicio en segundos para la sección de audio a transformar (por defecto: 30). | INT | No | 0-190 |
| `máscara_fin` | Posición de finalización en segundos para la sección de audio a transformar (por defecto: 190). | INT | No | 0-190 |

**Nota:** El valor de `mask_end` debe ser mayor que el valor de `mask_start`. El audio de entrada debe tener una duración entre 6 y 190 segundos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `audio` | La salida de audio transformada con la sección especificada modificada según el prompt. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/es.md)

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
