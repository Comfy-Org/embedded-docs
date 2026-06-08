El nodo TripoRigNode genera un modelo 3D riggeado a partir del ID de tarea de un modelo original. Envía una solicitud a la API de Tripo para crear un rig animado en formato GLB utilizando la especificación de Tripo, y luego consulta la API hasta que la tarea de generación del rig se complete.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `ID_de_tarea_del_modelo_original` | El ID de tarea del modelo 3D original al que se le aplicará el rig | MODEL_TASK_ID | Sí | - |
| `auth_token` | Token de autenticación para acceso a la API de Comfy.org | AUTH_TOKEN_COMFY_ORG | No | - |
| `comfy_api_key` | Clave API para autenticación en el servicio de Comfy.org | API_KEY_COMFY_ORG | No | - |
| `unique_id` | Identificador único para rastrear la operación | UNIQUE_ID | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `id_de_tarea_de_rig` | El archivo del modelo 3D riggeado generado (se mantiene por compatibilidad hacia atrás) | STRING |
| `GLB` | El ID de tarea para rastrear el proceso de generación del rig | RIG_TASK_ID |
| `GLB` | El modelo 3D riggeado generado en formato GLB | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/es.md)

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
