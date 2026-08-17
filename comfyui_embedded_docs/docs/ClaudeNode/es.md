# Anthropic Claude

Genera respuestas de texto a partir de un modelo Anthropic Claude. Este nodo envía un prompt de texto e imágenes opcionales a un modelo Claude y devuelve la respuesta de texto generada.

## Entradas

El parámetro `model` es un selector dinámico: cuando eliges un modelo, aparecen debajo ajustes adicionales específicos del modelo, como límite de tokens, temperatura y esfuerzo de razonamiento.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Entrada de texto al modelo. Debe ser no vacía después de eliminar espacios en blanco. (predeterminado: cadena vacía) | STRING | Sí | N/A |
| `model` | El modelo Claude utilizado para generar la respuesta. | DYNAMIC_COMBO | Sí | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | El parámetro `seed` controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `images` | Imagen(es) opcional(es) para usar como contexto para el modelo. Ranura ampliable: conecte `image_1` a `image_20`; hasta 20 imágenes. (predeterminado: ninguna) | IMAGE | No | 0 a 20 imágenes |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (predeterminado: cadena vacía) | STRING | No | N/A |

### Opus 5 y Fable 5 Entradas

Compartidas por Opus 5 y Fable 5. Estos modelos siempre usan pensamiento extendido y no ofrecen un ajuste de temperatura.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando está habilitado). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. El razonamiento está siempre habilitado para este modelo. (predeterminado: "high") | COMBO | Sí | `"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.8 y Sonnet 5 Entradas

Compartidas por Opus 4.8 y Sonnet 5. Estos modelos no ofrecen un ajuste de temperatura.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando está habilitado). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. "off" deshabilita el razonamiento. (predeterminado: "off") | COMBO | Sí | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Opus 4.7, Opus 4.6, Sonnet 4.6 y Sonnet 4.5 Entradas

Compartidas por Opus 4.7, Opus 4.6, Sonnet 4.6 y Sonnet 4.5. Para Opus 4.7, la entrada de temperatura se muestra pero se ignora, y la API usa el valor predeterminado de 1.0.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando está habilitado). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, 1.0 es lo más aleatorio. Se ignora para Opus 4.7 y cualquier modelo cuando se establece `reasoning_effort`. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.01) |
| `reasoning_effort` | Esfuerzo de pensamiento extendido. "off" deshabilita el razonamiento. (predeterminado: "off") | COMBO | Sí | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Haiku 4.5 Entradas

Este modelo no admite pensamiento extendido, por lo que no hay configuración de `reasoning_effort` disponible.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `max_tokens` | Número máximo de tokens a generar (incluye tokens de razonamiento cuando está habilitado). (predeterminado: 32768) | INT | Sí | 4096 a 64000 |
| `temperature` | Controla la aleatoriedad. 0.0 es determinista, 1.0 es lo más aleatorio. (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.01) |

### Restricciones de parámetros

- Se pueden proporcionar hasta 20 imágenes por solicitud. El recuento total de píxeles de las imágenes cargadas está limitado a 1568 × 1568 píxeles.
- La temperatura no es configurable para Opus 5, Fable 5, Opus 4.8 y Sonnet 5. Cuando hay una entrada de temperatura disponible, se ignora para Opus 4.7 y para cualquier modelo cuando `reasoning_effort` se establece a un valor distinto de "off".
- El razonamiento está siempre habilitado para Opus 5 y Fable 5, por lo que las opciones de `reasoning_effort` para estos modelos no incluyen "off". El modelo Haiku 4.5 no admite pensamiento extendido y, por lo tanto, no tiene configuración de `reasoning_effort`.
- Si Claude se niega a responder una solicitud por razones de seguridad, el nodo genera un error en lugar de devolver texto.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La respuesta de texto generada por el modelo Claude. Si no se genera texto visible, la salida es `"Empty response from Claude model."`. Los bloques de pensamiento o razonamiento no se incluyen en la salida. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/es.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
