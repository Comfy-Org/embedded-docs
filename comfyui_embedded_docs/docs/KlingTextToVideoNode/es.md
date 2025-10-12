> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

El nodo Kling Text to Video convierte descripciones de texto en contenido de video. Toma indicaciones de texto y genera secuencias de video correspondientes basadas en la configuración especificada. El nodo admite diferentes relaciones de aspecto y modos de generación para producir videos de duración y calidad variables.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Indicación de texto positiva (predeterminado: ninguno) |
| `negative_prompt` | STRING | Sí | - | Indicación de texto negativa (predeterminado: ninguno) |
| `cfg_scale` | FLOAT | No | 0.0-1.0 | Valor de escala de configuración (predeterminado: 1.0) |
| `aspect_ratio` | COMBO | No | Opciones de KlingVideoGenAspectRatio | Configuración de relación de aspecto del video (predeterminado: "16:9") |
| `mode` | COMBO | No | Múltiples opciones disponibles | La configuración a utilizar para la generación de video siguiendo el formato: modo / duración / nombre_modelo. (predeterminado: modes[4]) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La salida de video generada |
| `duration` | STRING | Identificador único para el video generado |
| `duration` | STRING | Información de duración para el video generado |