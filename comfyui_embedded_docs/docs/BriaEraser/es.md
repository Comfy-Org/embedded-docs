# Borrador Bria

Bria Eraser elimina objetos o áreas de una imagen utilizando la API de Bria. Usted proporciona una imagen y una máscara que delimita las regiones a eliminar; el nodo carga ambas a Bria, ejecuta el trabajo de borrado, espera a que se complete y devuelve la imagen editada con las áreas enmascaradas borradas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `image` | La imagen de entrada que contiene los objetos o áreas a eliminar. | IMAGE | Sí | - |
| `mask` | Las áreas blancas se borran, las áreas negras se conservan. La máscara se binariza antes de enviarla, por lo que las áreas parcialmente pintadas cuentan como blancas. Debe tener la misma relación de aspecto que la imagen. | MASK | Sí | - |
| `mask_type` | El tipo de origen de la máscara. "manual" es para máscaras dibujadas a mano o con pincel; "automatic" es para máscaras producidas por modelos de segmentación como SAM. | COMBO | Sí | "manual"<br>"automatic" |
| `moderation` | Configuración de moderación. Establezca en "true" para habilitar la moderación de contenido visual en las imágenes de entrada y/o salida. | DYNAMIC_COMBO | Sí | "false"<br>"true" |

Cuando `moderation` se establece en "true", dos configuraciones booleanas adicionales están disponibles:

- `visual_input_moderation` — aplica moderación de contenido visual a la imagen de entrada (predeterminado: false)
- `visual_output_moderation` — aplica moderación de contenido visual a la imagen de salida (predeterminado: false)

Nota: La máscara debe coincidir con la relación de aspecto de la imagen, de lo contrario la solicitud fallará. La máscara se convierte en una máscara binaria (blanco y negro) antes de enviarla a la API: las áreas pintadas con menos de la mitad de opacidad se ignoran, y las áreas parcialmente pintadas se tratan como blancas y se borrarán. La máscara debe contener al menos algo de área blanca; una máscara vacía hace que la solicitud falle porque no hay nada que borrar.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|-------------|-------------|-----------|
| `image` | La imagen editada con los objetos o áreas enmascaradas eliminados. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/es.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
