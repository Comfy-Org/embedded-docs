Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias para mejorar, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/en.md)

## Descripción general

Este nodo genera imágenes a partir de descripciones textuales utilizando el modelo Luma UNI-1. Toma un texto de entrada (prompt) y configuraciones opcionales como la relación de aspecto y el estilo, y luego envía la solicitud a la API de Luma para crear una imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Descripción textual de la imagen deseada. | STRING | Sí | 1–6000 caracteres |
| `model` | Modelo a utilizar para la generación. Seleccionar un modelo revela configuraciones adicionales para ese modelo. | COMBO | Sí | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (por defecto: 0) | INT | Sí | 0 a 2147483647 |

### Entradas Específicas del Modelo

Cuando se selecciona `"uni-1"` o `"uni-1-max"` para el parámetro `model`, las siguientes entradas estarán disponibles:

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Relación de aspecto de la imagen de salida. `"auto"" permite que el modelo elija según el prompt. (por defecto: `"auto"`) | COMBO | Sí | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | El estilo visual para la imagen generada. (por defecto: `"auto"`) | COMBO | Sí | `"auto"`<br>`"manga"` |
| `web_search` | Si se permite que el modelo busque en la web para obtener contexto adicional. (por defecto: Falso) | BOOLEAN | Sí | Verdadero / Falso |
| `image_ref` | Imágenes de referencia para guiar la generación. | IMAGE | No | Hasta 9 imágenes |

**Nota sobre las restricciones de `style` y `aspect_ratio`:** Si `style` se establece en `"manga"`, el `aspect_ratio` debe ser `"auto"` o una de las siguientes relaciones de retrato: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar una relación de aspecto apaisada o cuadrada con el estilo `"manga"` causará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen generada como un tensor. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/es.md)

---
**Source fingerprint (SHA-256):** `0a71bcd7c68c3610c162601b4c3f700034e47af8f16cf7853606753ad270c96e`
