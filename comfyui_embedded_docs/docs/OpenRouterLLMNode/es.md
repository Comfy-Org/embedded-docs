> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/es.md)

## Descripción general

El nodo LLM de OpenRouter envía un prompt de texto a un conjunto seleccionado de modelos de lenguaje populares disponibles a través del servicio OpenRouter y devuelve la respuesta de texto generada. Admite modelos de proveedores como xAI, DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) y Perplexity Sonar, y puede incluir opcionalmente imágenes o videos en la solicitud.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Entrada de texto para el modelo. |
| `model` | STRING | Sí | Múltiples opciones disponibles (ver nota a continuación) | El modelo de OpenRouter utilizado para generar la respuesta. |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla para el muestreo. Establecer en 0 para omitir. La mayoría de los modelos tratan esto solo como una sugerencia. (valor predeterminado: 0) |
| `system_prompt` | STRING | No | N/A | Instrucciones fundamentales que determinan el comportamiento del modelo. (valor predeterminado: "") |

**Nota sobre el parámetro `model`:** Las opciones de modelo disponibles se construyen dinámicamente y pueden incluir modelos con diferentes capacidades. Algunos modelos admiten funciones adicionales como esfuerzo de razonamiento, búsqueda web o entrada de imágenes/videos. El nodo validará que la cantidad de imágenes o videos proporcionados no exceda el número máximo admitido por el modelo.

**Nota sobre el parámetro `seed`:** El parámetro `seed` tiene un comportamiento de "control_después_de_generar", lo que significa que se puede configurar para que cambie automáticamente (por ejemplo, aleatorizar, incrementar o fijar) después de cada ejecución del nodo, según la configuración del widget del usuario.

**Nota sobre `system_prompt`:** Este parámetro es opcional y está marcado como un parámetro avanzado en la interfaz de usuario.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `output` | STRING | La respuesta de texto generada por el modelo de OpenRouter. |

---
**Source fingerprint (SHA-256):** `24757e36bf2356cc1805a6f071db88ca455e17944695672f19845a4cd1826c8a`
