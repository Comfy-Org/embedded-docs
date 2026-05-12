> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/es.md)

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/en.md)

## Resumen

Este nodo edita una imagen existente utilizando un prompt de texto, impulsado por el modelo Luma UNI-1. Toma una imagen de origen y una descripción del cambio deseado, luego genera una nueva versión editada de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `source` | IMAGE | Sí | - | Imagen de origen a editar. |
| `prompt` | STRING | Sí | 1–6000 caracteres | Descripción de la edición deseada. Valor predeterminado: "" (cadena vacía). |
| `model` | MODEL | Sí | `"uni-1"`<br>`"uni-1-max"` | Modelo a utilizar para la edición. |
| `seed` | INT | Sí | 0 a 2147483647 | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. Valor predeterminado: 0. |

**Restricciones de Parámetros:**
- El `prompt` debe tener entre 1 y 6000 caracteres de longitud.
- El parámetro `model` es un combo dinámico que, cuando se establece en `"uni-1"` o `"uni-1-max"`, proporciona subparámetros adicionales (como `style`, `web_search` e `image_ref`). El subparámetro `image_ref` acepta un máximo de 8 referencias de imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen editada generada por el modelo Luma UNI-1. |