> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/es.md)

El nodo GeminiImage genera respuestas de texto e imagen a partir de los modelos de IA Gemini de Google. Permite proporcionar entradas multimodales que incluyen prompts de texto, imágenes y archivos para crear salidas coherentes de texto e imagen. El nodo maneja toda la comunicación con la API y el análisis de respuestas con los últimos modelos Gemini.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `prompt` | STRING | requerido | "" | - | Prompt de texto para la generación |
| `model` | COMBO | requerido | gemini_2_5_flash_image_preview | Modelos Gemini disponibles<br>Opciones extraídas del enum GeminiImageModel | El modelo Gemini a utilizar para generar las respuestas. |
| `seed` | INT | requerido | 42 | 0 a 18446744073709551615 | Cuando la semilla se fija a un valor específico, el modelo hace un esfuerzo por proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se utiliza el mismo valor de semilla. Por defecto, se utiliza un valor de semilla aleatorio. |
| `images` | IMAGE | opcional | None | - | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puede utilizar el nodo Batch Images. |
| `files` | GEMINI_INPUT_FILES | opcional | None | - | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas desde el nodo Gemini Generate Content Input Files. |

**Nota:** El nodo incluye parámetros ocultos (`auth_token`, `comfy_api_key`, `unique_id`) que son manejados automáticamente por el sistema y no requieren entrada del usuario.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La respuesta de imagen generada por el modelo Gemini |
| `STRING` | STRING | La respuesta de texto generada por el modelo Gemini |