Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/en.md)

## Resumen

Este nodo edita una imagen existente utilizando un mensaje de texto, impulsado por el modelo Luma UNI-1. Toma una imagen de origen y una descripción del cambio deseado, luego genera una nueva versión editada de la imagen.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `source` | Imagen de origen a editar. | IMAGE | Sí | - |
| `prompt` | Descripción de la edición deseada. Valor predeterminado: "" (cadena vacía). | STRING | Sí | 1–6000 caracteres |
| `model` | Modelo a utilizar para la edición. | MODEL | Sí | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. Valor predeterminado: 0. | INT | Sí | 0 a 2147483647 |

**Restricciones de Parámetros:**
- El `prompt` debe tener entre 1 y 6000 caracteres de longitud.
- El parámetro `model` es un combo dinámico que, cuando se establece en `"uni-1"` o `"uni-1-max"`, proporciona subparámetros adicionales (como `style`, `web_search` e `image_ref`). El subparámetro `image_ref` acepta un máximo de 8 referencias de imagen.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen editada generada por el modelo Luma UNI-1. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/es.md)

---
**Source fingerprint (SHA-256):** `7026e3ce818b0a9710624bd071fc2049950290f89c7d0365ff44236e9ad5eaed`
