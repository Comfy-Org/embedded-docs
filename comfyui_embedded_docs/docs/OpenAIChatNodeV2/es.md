# OpenAI ChatGPT

Este nodo genera respuestas de texto con los modelos GPT de OpenAI. Envía un prompt de texto y, opcionalmente, imágenes o archivos como contexto, y devuelve la respuesta como una cadena. Todos los ajustes viven dentro del selector `model`: al elegir un modelo se muestran los niveles propios de `reasoning_effort`, el límite de tokens, la semilla y el prompt de sistema de ese modelo, por lo que no se necesita un nodo de configuración separado. Este nodo reemplaza al nodo anterior OpenAI ChatGPT, que el código fuente ahora marca como obsoleto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo usado para generar la respuesta. Cada modelo expone los niveles de `reasoning_effort` que admite (predeterminado: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Sí | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Entrada de texto para el modelo (predeterminado: cadena vacía). | STRING | Sí | - |
| `images` | Ranura ampliable: conecte de 1 a 16 elementos (`image_1`, `image_2`, ...). Imágenes opcionales usadas como contexto para el modelo. | IMAGE | No | 0 a 16 imágenes |
| `files` | Archivo o archivos opcionales usados como contexto para el modelo. Acepta entradas del nodo OpenAI ChatGPT Input Files. | OPENAI_INPUT_FILES | No | - |
| `reasoning_effort` | Cuánto razona el modelo antes de responder. Los niveles más altos usan más tokens y tardan más. Los niveles ofrecidos dependen del modelo seleccionado (predeterminado: `"medium"`, `"high"` para `gpt-5.5-pro`). | COMBO | Sí | Consulte la lista por modelo a continuación |
| `max_output_tokens` | Máximo de tokens a generar, incluidos los tokens de razonamiento. Un valor bajo junto con un `reasoning_effort` alto puede no dejar espacio para la respuesta (predeterminado: 32768). | INT | Sí | 16 a 128000 |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 42). | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que dictan el comportamiento del modelo (predeterminado: cadena vacía). | STRING | No | - |

### Niveles de esfuerzo de razonamiento por modelo

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, predeterminado `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, predeterminado `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, predeterminado `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, predeterminado `"medium"`.

### Notas sobre el comportamiento

- Solo se devuelve el texto de la respuesta. Se omiten los mensajes que el modelo emite en su fase de comentarios mientras piensa.
- Si el presupuesto de tokens se agota antes de que se escriba la respuesta, el nodo genera un error que indica que se debe aumentar `max_output_tokens`.
- Las imágenes se envían con su propia resolución y con el nivel de detalle automático de la API, por lo que las imágenes grandes usan más tokens.
- Cada solicitud se almacena del lado de OpenAI, y el texto devuelto une las partes de la respuesta con saltos de línea.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La respuesta de texto generada por el modelo de OpenAI. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
