> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/es.md)

Este nodo aplica una animación específica a un modelo de personaje 3D que ya ha sido riggeado utilizando el servicio Meshy. Toma un ID de tarea de una operación de rigging anterior y un ID de acción para seleccionar la animación deseada de la biblioteca. Luego, el nodo procesa la solicitud y devuelve el modelo animado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `rig_task_id` | STRING | Sí | N/A | El ID de tarea único de una operación de rigging de personajes Meshy completada previamente. |
| `action_id` | INT | Sí | 0 a 696 | El número de ID de la acción de animación a aplicar. Visita <https://docs.meshy.ai/en/api/animation-library> para obtener una lista de valores disponibles. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `GLB` | STRING | Un identificador de cadena para el modelo animado. Esta salida se proporciona solo por compatibilidad con versiones anteriores. |
| `FBX` | FILE3DGLB | El archivo de modelo 3D animado en formato GLB. |
| `FBX` | FILE3DFBX | El archivo de modelo 3D animado en formato FBX. |

---
**Source fingerprint (SHA-256):** `3b7610b5f6f763dde86a52f9212b3fc98f41e54bda30097fcb8f5f0bd020899e`
