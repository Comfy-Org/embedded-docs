> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/en.md)

## Resumen

Este nodo genera imágenes a partir de descripciones textuales utilizando el modelo Luma UNI-1. Toma un prompt de texto y configuraciones opcionales como la relación de aspecto y el estilo, luego envía la solicitud a la API de Luma para crear una imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | 1–6000 caracteres | Descripción textual de la imagen deseada. |
| `model` | COMBO | Sí | `"uni-1"`<br>`"uni-1-max"` | Modelo a utilizar para la generación. Seleccionar un modelo revela configuraciones adicionales para ese modelo. |
| `seed` | INT | Sí | 0 a 2147483647 | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (por defecto: 0) |

### Entradas Específicas del Modelo

Cuando se selecciona `"uni-1"` o `"uni-1-max"` para el parámetro `model`, las siguientes entradas estarán disponibles:

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `aspect_ratio` | COMBO | Sí | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` | Relación de aspecto de la imagen de salida. `"auto"` permite que el modelo elija según el prompt. (por defecto: `"auto"`) |
| `style` | COMBO | Sí | `"auto"`<br>`"manga"` | El estilo visual para la imagen generada. (por defecto: `"auto"`) |
| `web_search` | BOOLEAN | Sí | Verdadero / Falso | Si se permite que el modelo busque en la web contexto adicional. (por defecto: Falso) |
| `image_ref` | IMAGE | No | Hasta 9 imágenes | Imágenes de referencia para guiar la generación. |

**Nota sobre restricciones de `style` y `aspect_ratio`:** Si `style` está configurado en `"manga"`, el `aspect_ratio` debe ser `"auto"` o una de las siguientes relaciones de retrato: `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Usar una relación de paisaje o cuadrada con el estilo `"manga"` causará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | La imagen generada como un tensor. |