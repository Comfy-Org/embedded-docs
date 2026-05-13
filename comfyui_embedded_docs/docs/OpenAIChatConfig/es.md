> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/es.md)

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

El nodo OpenAIChatConfig permite establecer opciones de configuración adicionales para el Nodo de Chat OpenAI. Proporciona ajustes avanzados que controlan cómo el modelo genera respuestas, incluyendo el comportamiento de truncamiento, los límites de longitud de salida y las instrucciones personalizadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `truncation` | COMBO | Sí | `"auto"`<br>`"disabled"` | La estrategia de truncamiento a utilizar para la respuesta del modelo. auto: Si el contexto de esta respuesta y las anteriores supera el tamaño de la ventana de contexto del modelo, el modelo truncará la respuesta para ajustarse a la ventana de contexto eliminando elementos de entrada en medio de la conversación. disabled: Si una respuesta del modelo supera el tamaño de la ventana de contexto para un modelo, la solicitud fallará con un error 400 (valor predeterminado: "auto") |
| `max_output_tokens` | INT | No | 16 a 16384 | Un límite superior para la cantidad de tokens que se pueden generar para una respuesta, incluyendo los tokens de salida visibles (valor predeterminado: 4096) |
| `instructions` | STRING | No | - | Instrucciones para el modelo sobre cómo generar la respuesta (se admite entrada multilínea) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | Objeto de configuración que contiene los ajustes especificados para su uso con Nodos de Chat OpenAI |

---
**Source fingerprint (SHA-256):** `6d956aa1bc7f822c18ddaa55cd2345dad947fd93833de25a957f49878484af97`
