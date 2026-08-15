# Luma UNI-1 Image Edit

Este nodo edita una imagen existente utilizando un prompt de texto, impulsado por el modelo Luma UNI-1. Toma una imagen de origen y una descripción del cambio deseado, y luego genera una nueva versión editada de la imagen. Puede elegir entre los modelos `uni-1` y `uni-1-max`, ajustar el estilo, habilitar la búsqueda web y, opcionalmente, proporcionar hasta 8 imágenes de referencia.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | Modelo a utilizar para la edición. Al seleccionar un modelo, se muestran las opciones específicas de ese modelo a continuación. | MODEL | Sí | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Imagen de origen a editar. | IMAGE | Sí | - |
| `prompt` | Descripción de la edición deseada. De 1 a 6000 caracteres. Predeterminado: "" (cadena vacía). | STRING | Sí | 1 a 6000 caracteres |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Predeterminado: 0. | INT | Sí | 0 a 2147483647 |

### Entradas de uni-1 y uni-1-max

Estas opciones son compartidas por los modelos `uni-1` y `uni-1-max`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `style` | Preajuste de estilo. `"auto"` elige según el prompt; `"manga"` aplica una estética manga/anime y requiere una relación de aspecto vertical (2:3, 9:16, 1:2, 1:3). Predeterminado: `"auto"`. | STRING | Sí | `"auto"`<br>`"manga"` |
| `web_search` | Busca referencias visuales en la web antes de generar. Predeterminado: false. | BOOLEAN | Sí | `true`<br>`false` |

### Entradas de referencia

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image_ref` | Ranura ampliable: conecta hasta 8 imágenes de referencia (`image_1` a `image_8`) para guiar el estilo/contenido. Opcional. | IMAGE | No | 1 a 8 imágenes |

**Notas:**
- El parámetro `prompt` debe tener entre 1 y 6000 caracteres.
- Las entradas `style`, `web_search` e `image_ref` aparecen cuando `model` se establece en `"uni-1"` o `"uni-1-max"`.
- Ambos modelos admiten las mismas opciones específicas del modelo, incluidas hasta 8 imágenes de referencia.
- El estilo `"manga"` requiere una relación de aspecto vertical (2:3, 9:16, 1:2 o 1:3).
- Conectar más de 8 imágenes de referencia provoca un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen editada generada por el modelo Luma UNI-1. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/es.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`
