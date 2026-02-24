> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/es.md)

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v2-6"` | El modelo de IA específico a utilizar para la generación de video. |
| `prompt` | STRING | Sí | - | Prompt de texto positivo. La descripción utilizada para generar el video. Debe tener entre 1 y 2500 caracteres. |
| `mode` | COMBO | Sí | `"pro"` | El modo operativo para la generación del video. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación de aspecto (ancho a alto) deseada para el video generado. |
| `duration` | COMBO | Sí | `5`<br>`10` | La duración del video en segundos. |
| `generate_audio` | BOOLEAN | No | - | Controla si se genera audio para el video. Cuando está habilitado, la IA creará sonido basado en el prompt. (valor por defecto: `True`) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |
