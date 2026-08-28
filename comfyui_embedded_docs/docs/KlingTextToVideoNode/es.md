# Kling Texto a Video

El nodo Kling Text to Video genera videos a partir de descripciones de texto utilizando la API de generación de videos de Kling. Envía el prompt y la configuración (relación de aspecto, modo de generación y escala CFG) a la API, espera a que se complete la tarea de generación y luego devuelve el video resultante junto con su ID y duración.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt de texto positivo que describe el contenido deseado del video | STRING | Sí | Máximo 2500 caracteres |
| `negative_prompt` | Prompt de texto negativo que describe lo que se debe evitar en el video | STRING | No | Máximo 2500 caracteres |
| `cfg_scale` | Valor de escala de configuración que controla qué tan cerca sigue el video al prompt (predeterminado: 1.0) | FLOAT | No | 0.0 a 1.0 |
| `aspect_ratio` | Configuración de la relación de aspecto del video (predeterminado: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuración a utilizar para la generación del video siguiendo el formato: modo / duración / nombre_del_modelo (predeterminado: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | No | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

Nota: El parámetro `prompt` es obligatorio y no debe estar vacío. Tanto `prompt` como `negative_prompt` están limitados a un máximo de 2500 caracteres.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La salida de video generada | VIDEO |
| `video_id` | Identificador único del video generado | STRING |
| `duration` | Información de duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
