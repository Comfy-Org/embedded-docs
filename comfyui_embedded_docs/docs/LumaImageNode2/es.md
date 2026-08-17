# Luma UNI-1 Image

## Descripción general

Este nodo genera imágenes a partir de descripciones de texto utilizando el modelo Luma UNI-1. Toma un prompt de texto y ajustes opcionales como la relación de aspecto y el estilo, y luego envía la solicitud a la API de Luma para crear una imagen. Hay dos variantes de modelo disponibles: `uni-1` y `uni-1-max`.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo a utilizar para la generación. Seleccionar un modelo revela ajustes adicionales para ese modelo. | DYNAMIC_COMBO | Sí | `"uni-1"`<br>`"uni-1-max"` |
| `prompt` | Descripción de texto de la imagen deseada. 1–6000 caracteres. | STRING | Sí | 1 a 6000 caracteres |
| `seed` | El seed controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente del seed. (por defecto: 0) | INT | Sí | 0 a 2147483647 |

### Entradas de uni-1 y uni-1-max

Compartidas por las opciones de modelo `uni-1` y `uni-1-max`. Estos ajustes aparecen cuando se selecciona cualquiera de los dos modelos.

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Relación de aspecto de la imagen de salida. `"auto"` permite que el modelo elija según el prompt. (por defecto: `"auto"`) | COMBO | Sí | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Ajuste preestablecido de estilo. `"auto"` elige según el prompt; `"manga"` aplica una estética de manga/anime y requiere una relación de aspecto vertical (2:3, 9:16, 1:2, 1:3). (por defecto: `"auto"`) | COMBO | Sí | `"auto"`<br>`"manga"` |
| `web_search` | Buscar referencias visuales en la web antes de generar. (por defecto: False) | BOOLEAN | Sí | True / False |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image_ref` | Ranura ampliable: conecte de 1 a 9 elementos (ej. `image_1` a `image_9`). Hasta 9 imágenes de referencia para guiar el estilo/contenido. | IMAGE | No | Hasta 9 imágenes |

**Nota:** Si `style` está configurado en `"manga"`, `aspect_ratio` debe ser `"auto"` o una de las relaciones verticales `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. El uso de cualquier otra relación con el estilo `"manga"` provocará un error. El número máximo de imágenes de referencia es 9 tanto para `uni-1` como para `uni-1-max`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `image` | La imagen generada como tensor. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/es.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
