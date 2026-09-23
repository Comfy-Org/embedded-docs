# Anthropic Claude

Genera respuestas de texto a partir de los modelos Claude de Anthropic. Proporcione un prompt de texto y, opcionalmente, una o más imágenes para contexto multimodal; el nodo devuelve la respuesta de texto generada por el modelo.

## Entradas

Las entradas se agrupan en ajustes comunes, ajustes específicos del modelo que aparecen cuando se selecciona un modelo, e imágenes de referencia opcionales.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | El modelo Claude utilizado para generar la respuesta. Al seleccionar un modelo, se muestran a continuación los ajustes específicos de ese modelo. | DYNAMIC_COMBO | Sí | `"Opus 5.5"`<br>`"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5.1"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | Entrada de texto para el modelo. (predeterminado: cadena vacía) | STRING | Sí | N/A |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: cadena vacía) | STRING | No | N/A |

### Entradas de Opus 5.5, Opus 5, Fable 5.1 y Fable 5

Estos cuatro modelos comparten los mismos ajustes. No exponen un ajuste de temperatura, y el razonamiento siempre está habilitado.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando están habilitados). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. El razonamiento siempre está habilitado para este modelo. (predeterminado: "high") | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Entradas de Opus 4.8 y Sonnet 5

Estos dos modelos comparten los mismos ajustes. No exponen un ajuste de temperatura.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando están habilitados). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. `"off"` deshabilita el razonamiento. (predeterminado: "off") | COMBO | Sí | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |

### Entradas de Opus 4.7, Opus 4.6, Sonnet 4.6 y Sonnet 4.5

Estos cuatro modelos comparten los mismos ajustes.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando están habilitados). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, 1.0 es lo más aleatorio posible. Se ignora para Opus 4.7 y para cualquier modelo cuando `reasoning_effort` está establecido. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. `"off"` deshabilita el razonamiento. (predeterminado: "off") | COMBO | Sí | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

`reasoning_effort` ofrece `"off"`, `"low"`, `"medium"` y `"high"` en los cuatro modelos. Opus 4.7, Opus 4.6 y Sonnet 4.6 además aceptan `"max"`, y Opus 4.7 también acepta `"xhigh"`.

### Entradas de Haiku 4.5

Este modelo no expone un ajuste `reasoning_effort`.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando están habilitados). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, 1.0 es lo más aleatorio posible. Se ignora para Opus 4.7 y para cualquier modelo cuando `reasoning_effort` está establecido. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso: 0.01) |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `images` | Imagen(es) opcional(es) para usar como contexto del modelo. Hasta 20 imágenes. Ranura ampliable: conecte de 1 a 20 elementos (`image_1` ... `image_20`). | IMAGE | No | 0 a 20 imágenes |

### Restricciones de los parámetros

- **Límite de imágenes:** Se puede proporcionar un máximo de 20 imágenes por solicitud. Conectar más de 20 imágenes provoca un error.
- **Prompt obligatorio:** El prompt debe contener al menos un carácter que no sea un espacio en blanco. Un prompt vacío provoca un error de validación.
- **Manejo de la temperatura:** Cuando el pensamiento está habilitado, la API de Anthropic requiere que la temperatura no esté establecida (su valor predeterminado es 1.0). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5 y Sonnet 5 no exponen un ajuste de temperatura. Opus 4.7 ignora `temperature`, y cualquier modelo con `reasoning_effort` establecido en algo distinto de `"off"` también lo ignora.
- **Comportamiento del razonamiento/pensamiento:** El ajuste `reasoning_effort` controla si el pensamiento está habilitado. Opus 5.5, Opus 5, Fable 5.1 y Fable 5 siempre tienen el razonamiento habilitado. Haiku 4.5 no admite razonamiento. Cuando el pensamiento está habilitado, el nodo utiliza el modo de pensamiento adecuado para el modelo seleccionado, ya sea adaptativo o basado en presupuesto. En el modo de presupuesto, el presupuesto de tokens de razonamiento se limita para dejar al menos 1024 tokens para la respuesta real.
- **Rechazo por seguridad:** Si Claude se niega a responder la solicitud por motivos de seguridad, el nodo genera un error que le pide reformular el prompt o probar un modelo diferente.
- **Texto de salida:** Los bloques de pensamiento y razonamiento no se incluyen en la salida; solo se devuelve el texto generado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La respuesta de texto generada por el modelo Claude. No se incluyen los bloques de pensamiento/razonamiento. Si no se genera texto, devuelve "Empty response from Claude model." | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/es.md)

---
**Source fingerprint (SHA-256):** `f6d9353025598bbed1aca7bdeb56ac59f5e4c26dd5b8e29359e97ef29e35bee7`
