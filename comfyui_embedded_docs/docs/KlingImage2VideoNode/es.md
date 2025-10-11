> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImage2VideoNode/es.md)

El nodo Kling Image to Video genera contenido de video a partir de una imagen inicial utilizando prompts de texto. Toma una imagen de referencia y crea una secuencia de video basada en las descripciones de texto positivas y negativas proporcionadas, con varias opciones de configuración para la selección del modelo, duración y relación de aspecto.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `start_frame` | IMAGE | Sí | - | La imagen de referencia utilizada para generar el video. |
| `prompt` | STRING | Sí | - | Prompt de texto positivo. |
| `negative_prompt` | STRING | Sí | - | Prompt de texto negativo. |
| `model_name` | COMBO | Sí | Múltiples opciones disponibles | Selección del modelo para la generación de video (por defecto: "kling-v2-master"). |
| `cfg_scale` | FLOAT | Sí | 0.0-1.0 | Parámetro de escala de configuración (por defecto: 0.8). |
| `mode` | COMBO | Sí | Múltiples opciones disponibles | Selección del modo de generación de video (por defecto: std). |
| `aspect_ratio` | COMBO | Sí | Múltiples opciones disponibles | Relación de aspecto para el video generado (por defecto: field_16_9). |
| `duration` | COMBO | Sí | Múltiples opciones disponibles | Duración del video generado (por defecto: field_5). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La salida de video generada. |
| `video_id` | STRING | Identificador único para el video generado. |
| `duration` | STRING | Información de duración para el video generado. |