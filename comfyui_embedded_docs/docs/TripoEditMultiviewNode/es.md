# TripoEditMultiviewNode

Tripo: Edit Multiview edita las cuatro vistas de un resultado de Tripo: Image to Multiview, utilizando una instrucción de texto independiente para cada vista. Las vistas sin instrucción permanecen sin cambios. Las imágenes editadas están pensadas para conectarse a Tripo: Multiview to Model para crear un modelo 3D.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `multiview_task_id` | ID de tarea del resultado de Tripo: Image to Multiview cuyas vistas se editarán. | MULTIVIEW_TASK_ID | Sí | ID de tarea |
| `front_prompt` | Instrucción de texto que describe la edición que se aplicará a la vista frontal. Cuando está vacía, la vista frontal permanece sin cambios. Por defecto: vacío. | STRING | No | Texto multilínea |
| `left_prompt` | Instrucción de texto que describe la edición que se aplicará a la vista izquierda. Cuando está vacía, la vista izquierda permanece sin cambios. Por defecto: vacío. | STRING | No | Texto multilínea |
| `back_prompt` | Instrucción de texto que describe la edición que se aplicará a la vista trasera. Cuando está vacía, la vista trasera permanece sin cambios. Por defecto: vacío. | STRING | No | Texto multilínea |
| `right_prompt` | Instrucción de texto que describe la edición que se aplicará a la vista derecha. Cuando está vacía, la vista derecha permanece sin cambios. Por defecto: vacío. | STRING | No | Texto multilínea |

Nota: Al menos una de las cuatro instrucciones (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) debe contener texto no vacío; de lo contrario, el nodo genera un error. El `multiview_task_id` debe provenir del nodo Tripo: Image to Multiview. Un conjunto multivista editado no puede editarse de nuevo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `front` | Imagen editada de la vista frontal. | IMAGE |
| `izquierda` | Imagen editada de la vista izquierda. | IMAGE |
| `atrás` | Imagen editada de la vista trasera. | IMAGE |
| `derecha` | Imagen editada de la vista derecha. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/es.md)

---
**Source fingerprint (SHA-256):** `7a25f3867776c01ab606d43a988b5491e543b72d3eedac1779fa170453c1ca21`
