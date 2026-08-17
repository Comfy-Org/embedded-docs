# OpenRouter LLM

El nodo LLM de OpenRouter envía un prompt de texto (y opcionalmente imágenes o videos) a un conjunto seleccionado de modelos de lenguaje disponibles a través del servicio OpenRouter y devuelve la respuesta de texto generada. Admite modelos de Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) y Perplexity Sonar, y muestra opciones específicas del modelo, como el esfuerzo de razonamiento y el contexto de búsqueda web, cuando el modelo seleccionado las admite.

## Entradas

El selector `model` es dinámico: al elegir un modelo se muestran widgets específicos del modelo (esfuerzo de razonamiento, contexto de búsqueda web, ranuras de imagen y video) además de las entradas comunes que se muestran a continuación.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo de OpenRouter utilizado para generar la respuesta. Al seleccionar un modelo se muestran sus entradas específicas (consulte las secciones de modelos a continuación). | DYNAMIC_COMBO | Sí | 34 opciones seleccionadas de modelos OpenRouter |
| `prompt` | Entrada de texto para el modelo. Debe contener al menos un carácter que no sea un espacio en blanco. | STRING | Sí | Texto multilínea |
| `seed` | Semilla para el muestreo. Establézcala en 0 para omitirla. La mayoría de los modelos la tratan solo como una sugerencia. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: "") | STRING | No | Texto multilínea |

**Nota sobre `seed`:** Este parámetro tiene un comportamiento de "control_after_generate", lo que significa que se puede configurar para que cambie automáticamente (por ejemplo, aleatorizar, incrementar o fijar) después de cada ejecución del nodo, según la configuración de los widgets del usuario.

**Nota sobre `system_prompt`:** Este parámetro es opcional y está marcado como parámetro avanzado en la interfaz de usuario.

### Entradas de Anthropic Claude

Compartido por `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` y `anthropic/claude-haiku-4.5`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de OpenAI GPT

Compartido por `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` y `openai/gpt-5.5`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de Google Gemini 3.5 Flash

Se aplica a `google/gemini-3.5-flash`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de xAI Grok

Compartido por `x-ai/grok-4.5`, `x-ai/grok-4.20` y `x-ai/grok-4.3`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de DeepSeek

Compartido por `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` y `deepseek/deepseek-v3.2`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de Qwen 3.6 Plus y Flash

Compartido por `qwen/qwen3.6-plus` y `qwen/qwen3.6-flash`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de Mistral Large 2512

Se aplica a `mistralai/mistral-large-2512`. Este modelo no añade widgets de parámetros específicos; solo se aplican las entradas comunes y la ranura de referencia `images`.

### Entradas de Mistral Medium 3.5

Se aplica a `mistralai/mistral-medium-3-5`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de Moonshot Kimi K3 y K2.6

Compartido por `moonshotai/kimi-k3` y `moonshotai/kimi-k2.6`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de Perplexity Sonar Pro

Se aplica a `perplexity/sonar-pro`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Cuánto contexto de búsqueda web recuperar. Cuanto mayor, más fundamentado, pero más lento y costoso. (predeterminado: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |

### Entradas de Perplexity Sonar Reasoning Pro y Deep Research

Compartido por `perplexity/sonar-reasoning-pro` y `perplexity/sonar-deep-research`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | Cuánto contexto de búsqueda web recuperar. Cuanto mayor, más fundamentado, pero más lento y costoso. (predeterminado: "medium") | COMBO | No | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Modelos solo de razonamiento

Compartido por `qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5` y `moonshotai/kimi-k2-thinking`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esfuerzo de razonamiento. 'off' desactiva el razonamiento por completo. (predeterminado: "off") | COMBO | No | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagen(es) de referencia opcionales — enviadas como URL. Ranura ampliable: conecte `image_1` hasta `image_N`, donde N depende del modelo seleccionado. | IMAGE | No | 0 a N imágenes (N = 8, 10 o 20 según el modelo) |
| `videos` | Video(s) de referencia opcionales — enviados como URL. Ranura ampliable: conecte `video_1` hasta `video_N`. Solo disponible en modelos con soporte de video. | VIDEO | No | 0 a 4 videos |

**Nota sobre las capacidades y límites de los modelos:**

- Soporte de imágenes: hasta 20 imágenes para los modelos Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash y xAI Grok; hasta 10 imágenes para Qwen 3.6 Plus/Flash y Moonshot Kimi K3/K2.6; hasta 8 imágenes para Mistral Large 2512 y Mistral Medium 3.5. Los modelos DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking y Perplexity Sonar no aceptan imágenes.
- Soporte de video: solo `google/gemini-3.5-flash`, `qwen/qwen3.6-plus` y `qwen/qwen3.6-flash` aceptan videos, con un máximo de 4 videos.
- El nodo genera un error si se conectan más imágenes o videos de los que admite el modelo seleccionado.
- Cuando `reasoning_effort` se establece en "low", "medium" o "high", el modelo razona internamente pero no devuelve la traza de razonamiento; "off" desactiva el razonamiento por completo.
- El widget `search_context_size` solo aparece para los modelos Perplexity Sonar. Los widgets `reasoning_effort` y `search_context_size` están marcados como parámetros avanzados.
- El nodo muestra una insignia de precio aproximado (USD por 1K tokens) según el modelo seleccionado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | La respuesta de texto generada por el modelo OpenRouter seleccionado. | STRING |

**Nota sobre errores:** el nodo genera un error si OpenRouter devuelve un error de API, una respuesta vacía (sin opciones) o una negativa del modelo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/es.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
