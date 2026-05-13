> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/es.md)

# Descripción General

Modifica una imagen existente basándose en un mensaje de texto. Este nodo envía tus imágenes y una descripción textual a la API de Grok, que edita las imágenes según tus instrucciones y devuelve el resultado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | El mensaje de texto utilizado para generar la imagen. Debe tener al menos 1 carácter después de eliminar espacios en blanco. |
| `modelo` | MODEL | Sí | Ver Descripción | El modelo de imagen Grok a utilizar. Este parámetro tiene múltiples subopciones que aparecen después de seleccionar un modelo. Modelos disponibles: `grok-imagine-image-quality`, `grok-imagine-image-pro`, `grok-imagine-image`. Cada modelo tiene capacidades diferentes (ver nota a continuación). |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla. (predeterminado: 0) |

**Nota sobre las restricciones del parámetro `model`:**
- El parámetro `model` es un combo dinámico que incluye subopciones para `resolution`, `number_of_images`, `images` y `aspect_ratio`.
- **`grok-imagine-image-quality`**: Admite hasta 3 imágenes de entrada y permite relación de aspecto personalizada.
- **`grok-imagine-image-pro`**: Admite solo 1 imagen de entrada y no permite relación de aspecto personalizada.
- **`grok-imagine-image`**: Admite hasta 3 imágenes de entrada y permite relación de aspecto personalizada.
- **Se requiere al menos una imagen de entrada** para la edición. El nodo generará un error si no se proporcionan imágenes.
- **La relación de aspecto personalizada** (subopción `aspect_ratio`) solo está permitida cuando múltiples imágenes están conectadas a la entrada de imagen. Si solo se proporciona una imagen, la relación de aspecto debe establecerse en "auto".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) editada(s) devuelta(s) por la API de Grok. Si se genera una sola imagen, se devuelve directamente. Si se generan múltiples imágenes, se concatenan en un único tensor por lotes. |

---
**Source fingerprint (SHA-256):** `b041b40bb5712a67b09dcb0c841f00cbdd9ef77b9e4f3fdc6b2c4038be447ba5`
