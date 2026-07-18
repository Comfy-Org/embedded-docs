Este nodo aplica una animación específica a un modelo de personaje 3D que ya ha sido riggeado utilizando el servicio Meshy. Toma un ID de tarea de una operación de rigging anterior y un ID de acción para seleccionar la animación deseada de la biblioteca. Luego, el nodo procesa la solicitud y devuelve el modelo animado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `rig_task_id` | El ID de tarea único de una operación de rigging de personajes Meshy completada previamente. | STRING | Sí | N/A |
| `action_id` | El número de ID de la acción de animación a aplicar. Visita <https://docs.meshy.ai/en/api/animation-library> para obtener una lista de valores disponibles. (predeterminado: 0) | INT | Sí | 0 a 696 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model_file` | Un identificador de cadena para el modelo animado. Esta salida se proporciona solo por compatibilidad con versiones anteriores. | STRING |
| `GLB` | El archivo de modelo 3D animado en formato GLB. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D animado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/es.md)

---
**Source fingerprint (SHA-256):** `3b7610b5f6f763dde86a52f9212b3fc98f41e54bda30097fcb8f5f0bd020899e`
