> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/es.md)

El nodo GeminiImage genera respuestas de texto e imagen a partir de los modelos de IA Gemini de Google. Permite proporcionar entradas multimodales que incluyen indicaciones de texto, imágenes y archivos para crear resultados coherentes de texto e imagen. El nodo gestiona toda la comunicación con la API y el análisis de respuestas con los modelos Gemini más recientes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor Predeterminado | Rango | Descripción |
|-----------|--------------|-----------------|----------------------|-------|-------------|
| `prompt` | STRING | obligatorio | "" | - | Indicación de texto para la generación |
| `model` | COMBO | obligatorio | gemini_2_5_flash_image_preview | Modelos Gemini disponibles<br>Opciones extraídas de la enumeración GeminiImageModel | El modelo Gemini que se utilizará para generar respuestas |
| `seed` | INT | obligatorio | 42 | 0 a 18446744073709551615 | Cuando la semilla se fija en un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. No se garantiza un resultado determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede provocar variaciones en la respuesta incluso cuando se utiliza el mismo valor de semilla. De forma predeterminada, se utiliza un valor de semilla aleatorio |
| `images` | IMAGE | opcional | Ninguno | - | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir varias imágenes, puede usar el nodo de Agrupación de Imágenes |
| `files` | GEMINI_INPUT_FILES | opcional | Ninguno | - | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo de Archivos de Entrada de Generación de Contenido Gemini |

*Nota: El nodo incluye parámetros ocultos (`auth_token`, `comfy_api_key`, `unique_id`) que son gestionados automáticamente por el sistema y no requieren entrada del usuario.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La respuesta de imagen generada por el modelo Gemini |
| `STRING` | STRING | La respuesta de texto generada por el modelo Gemini |