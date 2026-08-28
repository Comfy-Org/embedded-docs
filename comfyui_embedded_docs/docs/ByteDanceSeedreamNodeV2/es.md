# ByteDance Seedream 4.5 & 5.0

Este nodo genera o edita imágenes mediante los modelos Seedream de ByteDance (versiones 4.0, 4.5, 5.0 Lite y 5.0 Pro). Ofrece generación unificada de texto a imagen y edición precisa de imágenes con una sola frase, con una resolución de hasta 4K. Esta es la versión heredada (V2) del nodo Seedream.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `modelo` | La versión del modelo Seedream que se utilizará para la generación. Cada modelo tiene diferentes capacidades y precios. | DYNAMIC_COMBO | Sí | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Indicación de texto para crear o editar una imagen (por defecto: cadena vacía). | STRING | Sí | N/A |
| `semilla` | Semilla que se utilizará para la generación (por defecto: 0). | INT | Sí | 0 a 2147483647 |
| `marca de agua` | Indica si se debe añadir una marca de agua de "generado por IA" a la imagen (por defecto: False). | BOOLEAN | Sí | True / False |
| `thinking` | Habilita el razonamiento de optimización de la indicación del modelo ('thinking') para un mejor seguimiento. Puede aumentar sustancialmente el tiempo de generación, especialmente en Seedream 5.0 Pro. Solo se puede deshabilitar para texto a imagen (no cuando se proporcionan imágenes de referencia) (por defecto: True). | BOOLEAN | No | True / False |

### Entradas de `seedream 5.0 pro`

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `size_preset` | Seleccione un tamaño recomendado. Seleccione Custom para usar el ancho y el alto que se indican a continuación. | COMBO | Sí | Hay múltiples preajustes específicos del modelo disponibles, incluido `Custom` |
| `width` | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 3136 (paso 2) |
| `height` | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 2496 (paso 2) |

### Entradas de `seedream 5.0 lite`

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `size_preset` | Seleccione un tamaño recomendado. Seleccione Custom para usar el ancho y el alto que se indican a continuación. | COMBO | Sí | Hay múltiples preajustes específicos del modelo disponibles, incluido `Custom` |
| `width` | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (entrada + generadas) no puede superar 15. (por defecto: 1) | INT | Sí | 1 a 14 |
| `fail_on_partial` | Si está habilitado, interrumpe la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (por defecto: False) | BOOLEAN | Sí | True / False |

### Entradas de `seedream-4-5-251128`

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `size_preset` | Seleccione un tamaño recomendado. Seleccione Custom para usar el ancho y el alto que se indican a continuación. | COMBO | Sí | Hay múltiples preajustes específicos del modelo disponibles, incluido `Custom` |
| `width` | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (entrada + generadas) no puede superar 15. (por defecto: 1) | INT | Sí | 1 a 10 |
| `fail_on_partial` | Si está habilitado, interrumpe la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (por defecto: False) | BOOLEAN | Sí | True / False |

### Entradas de `seedream-4-0-250828`

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `size_preset` | Seleccione un tamaño recomendado. Seleccione Custom para usar el ancho y el alto que se indican a continuación. | COMBO | Sí | Hay múltiples preajustes específicos del modelo disponibles, incluido `Custom` |
| `width` | Ancho personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 6240 (paso 2) |
| `height` | Alto personalizado para la imagen. El valor solo funciona si `size_preset` está establecido en `Custom` (por defecto: 2048). | INT | Sí | 1024 a 4992 (paso 2) |
| `max_images` | Número máximo de imágenes a generar. Con 1, se produce exactamente una imagen. Con >1, el modelo genera entre 1 y max_images imágenes relacionadas (p. ej., escenas de una historia, variaciones de personajes). El total de imágenes (entrada + generadas) no puede superar 15. (por defecto: 1) | INT | Sí | 1 a 10 |
| `fail_on_partial` | Si está habilitado, interrumpe la ejecución si falta alguna de las imágenes solicitadas o si se devuelve un error. (por defecto: False) | BOOLEAN | Sí | True / False |

### Entradas de referencia

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `images` | Entrada ampliable: conecte de 1 a N elementos (p. ej., `image_1`, `image_2`, ...); el límite de cantidad depende del modelo seleccionado (consulte las secciones de los modelos). Imagen(es) de referencia opcional(es) para generación de imagen a imagen o con múltiples referencias. Sin imágenes de referencia, el nodo funciona en modo texto a imagen. | IMAGE | No | 0 a 10 imágenes (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>0 a 14 imágenes (`seedream 5.0 lite`) |

### Notas sobre las restricciones

- `width` y `height` solo tienen efecto cuando `size_preset` está establecido en `Custom`.
- El número total de imágenes de referencia más las imágenes generadas no puede superar 15.
- `thinking` solo se puede deshabilitar para la generación de texto a imagen, no cuando se proporcionan imágenes de referencia.
- Seedream 5.0 Pro no admite la generación por lotes: siempre produce una sola imagen, por lo que `max_images` y `fail_on_partial` no están disponibles para este modelo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `image` | La imagen generada o editada como tensor. Si se solicitaron varias imágenes, se concatenan en un solo lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`
