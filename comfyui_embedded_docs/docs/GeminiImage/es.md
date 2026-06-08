Eres un experto en traducción técnica especializado en documentación de nodos ComfyUI del inglés al español.

## Reglas de Traducción

1. **Contenido que NO debe traducirse:**
   - Nombres de parámetros entre comillas invertidas: `image`, `seed`, `model`
   - Tipos de datos en MAYÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores en columna Range: números, "auto", nombres de opciones
   - Código, rutas de archivos

2. **Contenido que SÍ debe traducirse:**
   - Títulos de secciones: ## Descripción general, ## Entradas, ## Salidas
   - Todo el texto descriptivo y explicativo
   - Descripciones de parámetros

3. **Calidad de traducción:**
   - Usar español estándar y neutral
   - Mantener tono profesional pero accesible
   - Asegurar precisión técnica
   - Usar terminología técnica estándar en español

4. **Formato:**
   - Mantener todo el formato Markdown
   - Preservar estructura de tablas
   - No agregar ninguna nota o enlace al inicio del documento (será agregado automáticamente)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

El nodo GeminiImage genera respuestas de texto e imagen a partir de los modelos de IA Gemini de Google. Permite proporcionar entradas multimodales que incluyen indicaciones de texto, imágenes y archivos para crear resultados coherentes de texto e imagen. El nodo gestiona toda la comunicación con la API y el análisis de respuestas con los modelos Gemini más recientes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Indicación de texto para la generación | STRING | requerido | "" | - |
| `model` | El modelo Gemini a utilizar para generar respuestas. | COMBO | requerido | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | Cuando la semilla se fija en un valor específico, el modelo hace el mejor esfuerzo para proporcionar la misma respuesta para solicitudes repetidas. No se garantiza una salida determinista. Además, cambiar el modelo o la configuración de parámetros, como la temperatura, puede causar variaciones en la respuesta incluso cuando se usa el mismo valor de semilla. De forma predeterminada, se utiliza un valor de semilla aleatorio. | INT | requerido | 42 | 0 a 18446744073709551615 |
| `images` | Imagen(es) opcional(es) para usar como contexto para el modelo. Para incluir múltiples imágenes, puedes usar el nodo Batch Images. | IMAGE | opcional | None | - |
| `files` | Archivo(s) opcional(es) para usar como contexto para el modelo. Acepta entradas del nodo Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | opcional | None | - |

**Nota:** El nodo incluye parámetros ocultos (`auth_token`, `comfy_api_key`, `unique_id`) que son gestionados automáticamente por el sistema y no requieren entrada del usuario.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La respuesta de imagen generada por el modelo Gemini | IMAGE |
| `STRING` | La respuesta de texto generada por el modelo Gemini | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/es.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
