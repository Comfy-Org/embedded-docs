> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/es.md)

El nodo TextEncodeHunyuanVideo_ImageToVideo crea datos de condicionamiento para la generación de videos combinando prompts de texto con incrustaciones de imagen. Utiliza un modelo CLIP para procesar tanto la entrada de texto como la información visual de una salida de visión CLIP, luego genera tokens que mezclan estas dos fuentes según la configuración de intercalado de imagen especificada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para la tokenización y codificación |
| `salida_de_clip_vision` | CLIP_VISION_OUTPUT | Sí | - | Las incrustaciones visuales de un modelo de visión CLIP que proporcionan contexto de imagen |
| `indicación` | STRING | Sí | - | La descripción textual para guiar la generación del video, admite entrada multilínea y prompts dinámicos |
| `entrelazado_de_imagen` | INT | Sí | 1-512 | Cuánto influye la imagen frente al prompt de texto. Un número más alto significa mayor influencia del prompt de texto. (valor por defecto: 2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento que combinan información de texto e imagen para la generación de video |