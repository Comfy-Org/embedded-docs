> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/es.md)

El nodo TripoRigNode genera un modelo 3D riggeado a partir del ID de tarea de un modelo original. Envía una solicitud a la API de Tripo para crear un rig animado en formato GLB utilizando la especificación de Tripo, y luego consulta la API hasta que la tarea de generación del rig se complete.

## Entradas

| Parámetro | Tipo de dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `ID_de_tarea_del_modelo_original` | MODEL_TASK_ID | Sí | - | El ID de tarea del modelo 3D original al que se le aplicará el rig |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para acceso a la API de Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | No | - | Clave API para autenticación en el servicio de Comfy.org |
| `unique_id` | UNIQUE_ID | No | - | Identificador único para rastrear la operación |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `id_de_tarea_de_rig` | STRING | El archivo del modelo 3D riggeado generado (se mantiene por compatibilidad hacia atrás) |
| `GLB` | RIG_TASK_ID | El ID de tarea para rastrear el proceso de generación del rig |
| `GLB` | FILE3DGLB | El modelo 3D riggeado generado en formato GLB |

---
**Source fingerprint (SHA-256):** `621a4d08f3b8a349c3afff3dbf888b20d524eb3337685769b7a7badcb28986e4`
