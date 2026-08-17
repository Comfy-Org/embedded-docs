# ByteDance Seedream 4.5 & 5.0

Este nodo crea o edita imágenes utilizando los modelos ByteDance Seedream (4.0, 4.5, 5.0 Lite y 5.0 Pro). Genera nuevas imágenes a partir de un prompt de texto y puede editar imágenes existentes basándose en imágenes de referencia y una instrucción de una sola frase. Admite resoluciones de hasta 4K.

## Entradas

El selector `model` determina qué entradas específicas del modelo están disponibles. Las tablas siguientes enumeran las entradas comunes, las entradas de cada modelo y las ranuras ampliables de imágenes de referencia.

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model` | La versión del modelo Seedream que se utilizará para la generación. Cada modelo tiene diferentes capacidades, límites y precios. | DYNAMIC_COMBO | Sí | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt de texto para crear o editar una imagen. | STRING | Sí | Cualquier texto (no vacío) |
| `seed` | Semilla para la generación (predeterminado: 0). | INT | Sí | de 0 a 2147483647 |
| `watermark` | Si se debe añadir una marca de agua «generado por IA» a la imagen (predeterminado: False). | BOOLEAN | Sí | True / False |
| `thinking` | Habilita el razonamiento de optimización del prompt del modelo («thinking») para una mejor adherencia. Puede aumentar sustancialmente el tiempo de generación, especialmente en Seedream 5.0 Pro. Solo se puede deshabilitar para la generación de texto a imagen (no cuando se proporcionan imágenes de referencia). (predeterminado: True) | BOOLEAN | No | True / False |

### Entradas de seedream 5.0 pro

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size_preset` | Elija un tamaño recomendado. Seleccione Custom para usar el ancho y la altura indicados a continuación. | COMBO | Sí | Preajustes específicos del modelo (incluye Custom) |
| `width` | Ancho personalizado de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 3136 (paso 2) |
| `height` | Altura personalizada de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 2496 (paso 2) |

### Entradas de seedream 5.0 lite

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size_preset` | Elija un tamaño recomendado. Seleccione Custom para usar el ancho y la altura indicados a continuación. | COMBO | Sí | Preajustes específicos del modelo (incluye Custom) |
| `width` | Ancho personalizado de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 6240 (paso 2) |
| `height` | Altura personalizada de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personaje). El total de imágenes (entrada + generadas) no puede superar 15. (predeterminado: 1) | INT | Sí | de 1 a 14 |
| `fail_on_partial` | Si está habilitado, aborta la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (predeterminado: False) | BOOLEAN | Sí | True / False |

### Entradas de seedream-4-5-251128

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size_preset` | Elija un tamaño recomendado. Seleccione Custom para usar el ancho y la altura indicados a continuación. | COMBO | Sí | Preajustes específicos del modelo (incluye Custom) |
| `width` | Ancho personalizado de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 6240 (paso 2) |
| `height` | Altura personalizada de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personaje). El total de imágenes (entrada + generadas) no puede superar 15. (predeterminado: 1) | INT | Sí | de 1 a 10 |
| `fail_on_partial` | Si está habilitado, aborta la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (predeterminado: False) | BOOLEAN | Sí | True / False |

### Entradas de seedream-4-0-250828

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `size_preset` | Elija un tamaño recomendado. Seleccione Custom para usar el ancho y la altura indicados a continuación. | COMBO | Sí | Preajustes específicos del modelo (incluye Custom) |
| `width` | Ancho personalizado de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 6240 (paso 2) |
| `height` | Altura personalizada de la imagen. El valor solo tiene efecto si `size_preset` está configurado como Custom (predeterminado: 2048). | INT | Sí | de 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personaje). El total de imágenes (entrada + generadas) no puede superar 15. (predeterminado: 1) | INT | Sí | de 1 a 10 |
| `fail_on_partial` | Si está habilitado, aborta la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (predeterminado: False) | BOOLEAN | Sí | True / False |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `images` | Imagen(es) de referencia opcional(es) para la generación de imagen a imagen o con múltiples referencias. Ranura ampliable: conecte de 1 a N elementos (`image_1`, `image_2`, ..., `image_N`); el número máximo depende del modelo seleccionado (10 para seedream 5.0 pro, seedream-4-5-251128 y seedream-4-0-250828; 14 para seedream 5.0 lite). | IMAGE | No | de 0 a 10<br>de 0 a 14 (seedream 5.0 lite) |

### Notas

- Los valores personalizados de `width` y `height` solo tienen efecto cuando `size_preset` está configurado como Custom.
- Límites de resolución (según ancho × altura):
  - seedream 5.0 pro: mínimo 0.92 MP, máximo 4.19 MP.
  - seedream 5.0 lite y seedream-4-5-251128: mínimo 3.68 MP.
  - seedream-4-0-250828: mínimo 0.92 MP.
  - seedream 5.0 lite, seedream-4-5-251128 y seedream-4-0-250828: máximo 16.78 MP.
- Las imágenes de referencia deben tener una relación de aspecto entre 1:3 y 3:1.
- Cuando `max_images` es mayor que 1 (disponible en seedream 5.0 lite, seedream-4-5-251128 y seedream-4-0-250828), el número total de imágenes (imágenes de referencia más imágenes generadas) no puede superar 15.
- `thinking` solo se puede deshabilitar para la generación de texto a imagen; debe estar habilitado cuando se proporcionan imágenes de referencia.
- seedream 5.0 pro siempre genera una única imagen y no muestra las entradas `max_images` ni `fail_on_partial`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen generada o editada. Si se solicitaron varias imágenes con `max_images`, se devuelven concatenadas en un único lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
