# Recraft V4 Texto a Vector

El nodo Recraft V4 Text to Vector genera imágenes de gráficos vectoriales escalables (SVG) a partir de una descripción de texto. Se conecta a una API externa para generar imágenes utilizando los modelos Recraft V4 y V4.1. El nodo produce una o más imágenes SVG según su indicación.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo a utilizar para la generación. Seleccionar un modelo cambia las opciones de `size` disponibles. | DYNAMIC_COMBO | Sí | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Indicación para la generación de la imagen. Máximo 10.000 caracteres. | STRING | Sí | N/A |
| `negative_prompt` | Esta entrada se ignora: las indicaciones negativas no son compatibles con los modelos Recraft V4 y V4.1. | STRING | Sí | N/A |
| `n` | El número de imágenes a generar (predeterminado: 1). | INT | Sí | 1 a 6 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | CUSTOM | No | N/A |

### Entradas de recraftv4_1_vector, recraftv4_1_utility_vector y recraftv4

Estos tres modelos comparten las mismas opciones de `size`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: `"1024x1024"`). | COMBO | Sí | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entradas de recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector y recraftv4_pro

Estos tres modelos comparten las mismas opciones de `size`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (predeterminado: `"2048x2048"`). | COMBO | Sí | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza resultados reproducibles desde la API externa. La entrada `negative_prompt` se ignora porque los modelos Recraft V4 y V4.1 no admiten indicaciones negativas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | Las imágenes de gráficos vectoriales escalables (SVG) generadas. | SVG |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/es.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
