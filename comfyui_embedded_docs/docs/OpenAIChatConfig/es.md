> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/es.md)

El nodo OpenAIChatConfig permite configurar opciones adicionales para el nodo OpenAI Chat. Proporciona configuraciones avanzadas que controlan cómo el modelo genera respuestas, incluyendo el comportamiento de truncamiento, límites de longitud de salida e instrucciones personalizadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | Sí | `"auto"`<br>`"disabled"` | La estrategia de truncamiento a utilizar para la respuesta del modelo. auto: Si el contexto de esta respuesta y las anteriores excede el tamaño de la ventana de contexto del modelo, el modelo truncará la respuesta para ajustarse a la ventana de contexto eliminando elementos de entrada en medio de la conversación. disabled: Si una respuesta del modelo excederá el tamaño de la ventana de contexto para un modelo, la solicitud fallará con un error 400 (por defecto: "auto") |
| `max_output_tokens` | INT | No | 16-16384 | Un límite superior para el número de tokens que pueden generarse para una respuesta, incluyendo tokens de salida visibles (por defecto: 4096) |
| `instructions` | STRING | No | - | Instrucciones adicionales para la respuesta del modelo (admite entrada multilínea) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | Objeto de configuración que contiene los ajustes especificados para usar con nodos OpenAI Chat |
