# Recraft V4 Texto a Imagen

Este nodo genera imágenes a partir de descripciones de texto utilizando los modelos de IA Recraft V4 y V4.1. Envía tu prompt a una API externa y devuelve las imágenes generadas. Puedes controlar el resultado especificando el modelo, el tamaño de la imagen y el número de imágenes a crear.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo a utilizar para la generación. | DYNAMIC_COMBO | Sí | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para la generación de la imagen. Máximo 10,000 caracteres. | STRING | Sí | N/A |
| `prompt_negativo` | Esta entrada se ignora: el prompt negativo no es compatible con los modelos Recraft V4 y V4.1. | STRING | Sí | N/A |
| `n` | El número de imágenes a generar (por defecto: 1). | INT | Sí | 1 a 6 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionales opcionales sobre la generación mediante el nodo Recraft Controls. | CUSTOM | No | N/A |

### Entradas de recraftv4_1, recraftv4_1_utility y recraftv4

Compartidas por `recraftv4_1`, `recraftv4_1_utility` y `recraftv4`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (por defecto: "1024x1024"). | COMBO | Sí | Múltiples opciones disponibles (tamaños estándar de Recraft V4, incluye "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro y recraftv4_pro

Compartidas por `recraftv4_1_pro`, `recraftv4_1_utility_pro` y `recraftv4_pro`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `size` | El tamaño de la imagen generada (por defecto: "2048x2048"). | COMBO | Sí | Múltiples opciones disponibles (tamaños pro de Recraft V4, incluye "2048x2048") |

**Nota:** El parámetro `size` es una entrada dinámica cuyas opciones disponibles cambian según el `model` seleccionado. El valor de `seed` no garantiza resultados de imagen reproducibles. Si utiliza un ID de estilo de la Infinite Style Library, asegúrese de que no sea un estilo de arte vectorial, ya que esto puede devolver datos SVG en lugar de una imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | La imagen generada o el lote de imágenes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
