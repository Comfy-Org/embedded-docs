# Grok Image Edit

Modifica una imagen existente según una indicación de texto. Este nodo envía tus imágenes y una descripción de texto a la API de Grok, que edita las imágenes de acuerdo con tus instrucciones y devuelve el resultado.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo de imagen de Grok que se va a utilizar. Los subparámetros que se muestran a continuación cambian según el modelo seleccionado. | MODEL | Sí | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | La indicación de texto utilizada para generar la imagen. (por defecto: "") | STRING | Sí | N/A |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (por defecto: 0) | INT | Sí | 0 a 2147483647 |

### Entradas de grok-imagine-image-2.0

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Imagen(es) de referencia para editar. Hasta 3 imágenes. | IMAGE | Sí | 1 a 3 imágenes |
| `resolution` | Resolución de salida de las imágenes editadas. | STRING | Sí | "1K"<br>"2K" |
| `number_of_images` | Número de imágenes editadas a generar. (por defecto: 1) | INT | Sí | 1 a 10 |
| `quality` | Nivel de calidad de las imágenes generadas. | STRING | Sí | "medium"<br>"low" |
| `aspect_ratio` | Relación de aspecto de la imagen editada. (por defecto: "auto") | STRING | Sí | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas de grok-imagine-image-quality y grok-imagine-image

Compartidas por grok-imagine-image-quality y grok-imagine-image.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Imagen(es) de referencia para editar. Hasta 3 imágenes. | IMAGE | Sí | 1 a 3 imágenes |
| `resolution` | Resolución de salida de las imágenes editadas. | STRING | Sí | "1K"<br>"2K" |
| `number_of_images` | Número de imágenes editadas a generar. (por defecto: 1) | INT | Sí | 1 a 10 |
| `aspect_ratio` | Solo se permite cuando hay múltiples imágenes conectadas. (por defecto: "auto") | STRING | Sí | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Entradas de grok-imagine-image-pro

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Imagen de referencia para editar. | IMAGE | Sí | 1 imagen |
| `resolution` | Resolución de salida de las imágenes editadas. | STRING | Sí | "1K"<br>"2K" |
| `number_of_images` | Número de imágenes editadas a generar. (por defecto: 1) | INT | Sí | 1 a 10 |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `images` | Ranura ampliable: conecta 1 o más imágenes de referencia para editar. Se pueden añadir ranuras numeradas como `image_1`, `image_2`, `image_3`. El número máximo de imágenes depende del modelo seleccionado (consulta las secciones de modelos más arriba). | IMAGE | Sí | 1 a 3 imágenes, según el modelo |

**Nota sobre las restricciones:**

- `prompt` debe contener al menos 1 carácter que no sea un espacio en blanco.
- Se requiere al menos una imagen de referencia para editar; el nodo genera un error si no hay ninguna imagen conectada.
- El número máximo de imágenes de entrada es 1 para `grok-imagine-image-pro` y 3 para `grok-imagine-image-2.0`, `grok-imagine-image-quality` y `grok-imagine-image`. Conectar más imágenes de las que el modelo admite genera un error.
- Para `grok-imagine-image-quality` y `grok-imagine-image`, un valor personalizado de `aspect_ratio` (cualquier valor distinto de "auto") solo se permite cuando hay múltiples imágenes conectadas. Con una sola imagen, `aspect_ratio` debe ser "auto".
- Para `grok-imagine-image-2.0`, `aspect_ratio` puede establecerse libremente incluso con una sola imagen.
- El subparámetro `quality` solo está disponible con `grok-imagine-image-2.0`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | La(s) imagen(es) editada(s) devuelta(s) por la API de Grok. Si se genera una sola imagen, se devuelve directamente. Si se generan múltiples imágenes, se concatenan en un único tensor por lotes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
