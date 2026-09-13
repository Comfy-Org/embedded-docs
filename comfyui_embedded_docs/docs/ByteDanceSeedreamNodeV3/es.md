# ByteDance Seedream 4.5 y 5.0

ByteDance Seedream 4.5 y 5.0 genera imágenes a partir de un prompt de texto (texto a imagen) o genera/edita imágenes guiadas por imágenes de referencia opcionales, utilizando los modelos ByteDance Seedream 4.0, 4.5 y 5.0 con una resolución de hasta 4K. El nodo envía el prompt y las imágenes de referencia, si las hay, a la API de ByteDance, espera a que se complete la tarea de generación y devuelve el tensor o los tensores de imagen resultantes.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para crear o editar una imagen. No debe estar vacío después de recortar los espacios en blanco. | STRING | Sí | Texto multilínea |
| `modelo` | Selecciona el modelo Seedream a usar. Cada modelo expone su propio conjunto de subparámetros y límites a continuación. | DYNAMIC_COMBO | Sí | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Entradas de Seedream 5.0 Pro (seedream 5.0 pro)

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Elige un tamaño recomendado. Selecciona Custom para usar el ancho y el alto indicados a continuación. Predeterminado: el primer ajuste preestablecido recomendado para este modelo. | COMBO | No | Ajustes preestablecidos de tamaño recomendados específicos del modelo<br>"Custom" |
| `width` | Ancho personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 3136 (paso 2) |
| `height` | Alto personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 2496 (paso 2) |
| `prompt_optimization` | Modo de optimización del prompt cuando se proporcionan imágenes de referencia: 'standard' ofrece mayor calidad, 'fast' un tiempo de generación más corto. Predeterminado: "standard". | COMBO | No | "standard"<br>"fast" |
| `seed` | Semilla que se usará para la generación. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Indica si se debe añadir una marca de agua "AI generated" a la imagen. Predeterminado: false. | BOOLEAN | No | true / false |
| `thinking` | Activa el razonamiento de optimización del prompt del modelo ('thinking') para lograr una mejor adherencia. Puede aumentar considerablemente el tiempo de generación, sobre todo en Seedream 5.0 Pro. Solo puede desactivarse para texto a imagen (no cuando se proporcionan imágenes de referencia). Predeterminado: true. | BOOLEAN | No | true / false |

### Entradas de Seedream 5.0 Lite (seedream 5.0 lite)

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Elige un tamaño recomendado. Selecciona Custom para usar el ancho y el alto indicados a continuación. Predeterminado: el primer ajuste preestablecido recomendado para este modelo. | COMBO | No | Ajustes preestablecidos de tamaño recomendados específicos del modelo<br>"Custom" |
| `width` | Ancho personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (de entrada + generadas) no puede superar 15. Predeterminado: 1. | INT | No | 1 a 14 |
| `fail_on_partial` | Si está activado, aborta la ejecución si falta alguna de las imágenes solicitadas o si alguna devuelve un error. Predeterminado: false. | BOOLEAN | No | true / false |
| `seed` | Semilla que se usará para la generación. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Indica si se debe añadir una marca de agua "AI generated" a la imagen. Predeterminado: false. | BOOLEAN | No | true / false |
| `thinking` | Activa el razonamiento de optimización del prompt del modelo ('thinking') para lograr una mejor adherencia. Puede aumentar considerablemente el tiempo de generación, sobre todo en Seedream 5.0 Pro. Solo puede desactivarse para texto a imagen (no cuando se proporcionan imágenes de referencia). Predeterminado: true. | BOOLEAN | No | true / false |

### Entradas de Seedream 4.5 (seedream-4-5-251128)

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Elige un tamaño recomendado. Selecciona Custom para usar el ancho y el alto indicados a continuación. Predeterminado: el primer ajuste preestablecido recomendado para este modelo. | COMBO | No | Ajustes preestablecidos de tamaño recomendados específicos del modelo<br>"Custom" |
| `width` | Ancho personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (de entrada + generadas) no puede superar 15. Predeterminado: 1. | INT | No | 1 a 10 |
| `fail_on_partial` | Si está activado, aborta la ejecución si falta alguna de las imágenes solicitadas o si alguna devuelve un error. Predeterminado: false. | BOOLEAN | No | true / false |
| `seed` | Semilla que se usará para la generación. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Indica si se debe añadir una marca de agua "AI generated" a la imagen. Predeterminado: false. | BOOLEAN | No | true / false |
| `thinking` | Activa el razonamiento de optimización del prompt del modelo ('thinking') para lograr una mejor adherencia. Puede aumentar considerablemente el tiempo de generación, sobre todo en Seedream 5.0 Pro. Solo puede desactivarse para texto a imagen (no cuando se proporcionan imágenes de referencia). Predeterminado: true. | BOOLEAN | No | true / false |

### Entradas de Seedream 4.0 (seedream-4-0-250828)

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | Elige un tamaño recomendado. Selecciona Custom para usar el ancho y el alto indicados a continuación. Predeterminado: el primer ajuste preestablecido recomendado para este modelo. | COMBO | No | Ajustes preestablecidos de tamaño recomendados específicos del modelo<br>"Custom" |
| `width` | Ancho personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado de la imagen. El valor solo se aplica si `size_preset` está establecido en `Custom`. Predeterminado: 2048. | INT | No | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (de entrada + generadas) no puede superar 15. Predeterminado: 1. | INT | No | 1 a 10 |
| `fail_on_partial` | Si está activado, aborta la ejecución si falta alguna de las imágenes solicitadas o si alguna devuelve un error. Predeterminado: false. | BOOLEAN | No | true / false |
| `seed` | Semilla que se usará para la generación. Predeterminado: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Indica si se debe añadir una marca de agua "AI generated" a la imagen. Predeterminado: false. | BOOLEAN | No | true / false |
| `thinking` | Activa el razonamiento de optimización del prompt del modelo ('thinking') para lograr una mejor adherencia. Puede aumentar considerablemente el tiempo de generación, sobre todo en Seedream 5.0 Pro. Solo puede desactivarse para texto a imagen (no cuando se proporcionan imágenes de referencia). Predeterminado: true. | BOOLEAN | No | true / false |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `images` | Ranura ampliable: imagen o imágenes de referencia opcionales para la generación de imagen a imagen o con múltiples referencias. Conecta de 1 a N imágenes (p. ej., `image_1`, `image_2`, ...); el límite de cantidad depende de cada modelo (consulta las notas a continuación). Si una imagen conectada contiene un lote de imágenes, cada imagen del lote cuenta para el límite. | IMAGE | No | 0 a 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 a 14 (Seedream 5.0 Lite) |

**Notas:**

- El `prompt` no debe estar vacío después de recortar los espacios en blanco.
- Número máximo de imágenes de referencia: 10 para Seedream 5.0 Pro, Seedream 4.5 y Seedream 4.0; 14 para Seedream 5.0 Lite.
- Cada imagen de referencia debe tener una relación de aspecto entre 1:3 y 3:1.
- Cuando `max_images` es mayor que 1 (no disponible en Seedream 5.0 Pro), el número total de imágenes de referencia más las imágenes generadas no puede superar 15.
- `thinking` solo puede desactivarse para la generación de texto a imagen. Cuando se proporcionan imágenes de referencia, `thinking` debe estar activado.
- `width` y `height` solo se usan cuando `size_preset` está establecido en "Custom".
- `prompt_optimization` solo está disponible en Seedream 5.0 Pro.
- `max_images` y `fail_on_partial` solo están disponibles en Seedream 5.0 Lite, Seedream 4.5 y Seedream 4.0; Seedream 5.0 Pro siempre solicita una sola imagen.
- Requisitos de resolución (ancho x alto):
  - Seedream 5.0 Pro: entre 0.92MP (921,600 píxeles) y 4.19MP (4,194,304 píxeles).
  - Seedream 5.0 Lite y Seedream 4.5: al menos 3.68MP (3,686,400 píxeles).
  - Seedream 4.0: al menos 0.92MP (921,600 píxeles).
  - Todos los modelos que no son Pro: como máximo 16.78MP (16,777,216 píxeles).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `image` | El tensor de imagen generado. Cuando se generan varias imágenes, se concatenan en un único tensor IMAGE por lotes. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/es.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
