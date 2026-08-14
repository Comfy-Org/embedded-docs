# BriaEraser

Bria Eraser elimina objetos o áreas de una imagen mediante la API de Bria. Proporcionas una imagen y una máscara que delinea las regiones a eliminar; el nodo sube ambas a Bria, ejecuta el trabajo de borrado, espera a que se complete y devuelve la imagen editada con las áreas enmascaradas borradas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `image` | La imagen de entrada que contiene los objetos o áreas a eliminar. | IMAGE | Sí | - |
| `mask` | Las áreas blancas se borran, las áreas negras se conservan. La máscara se binariza antes de enviarse, por lo que las áreas parcialmente pintadas cuentan como blancas. Debe tener la misma relación de aspecto que la imagen. | MASK | Sí | - |
| `mask_type` | Selecciona cómo se creó la máscara. "manual" es para máscaras dibujadas a mano o con pincel; "automatic" es para máscaras producidas por modelos de segmentación como SAM. | STRING | Sí | "manual"<br>"automatic" |
| `moderation` | Configuración de moderación. Establece el valor "true" para habilitar la moderación de contenido en las imágenes de entrada y/o salida. | STRING | Sí | "false"<br>"true" |

Nota: cuando `moderation` se establece en "true", dos ajustes booleanos adicionales están disponibles:

- `visual_input_moderation` — aplica la moderación visual de contenido a la imagen de entrada (valor predeterminado: false)
- `visual_output_moderation` — aplica la moderación visual de contenido a la imagen de salida (valor predeterminado: false)

La máscara debe coincidir con la relación de aspecto de la imagen; de lo contrario, la solicitud falla. La máscara se convierte en una máscara binaria (blanco y negro) antes de enviarse a la API, por lo que las áreas parcialmente pintadas se tratan como blancas y se borrarán.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `image` | La imagen editada con los objetos o áreas enmascarados eliminados. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/es.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
