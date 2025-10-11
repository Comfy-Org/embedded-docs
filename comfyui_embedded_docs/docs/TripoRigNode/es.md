> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/es.md)

El TripoRigNode genera un modelo 3D con rig a partir de un ID de tarea de modelo original. Envía una solicitud a la API de Tripo para crear un rig animado en formato GLB utilizando la especificación Tripo, luego sondea la API hasta que la tarea de generación del rig esté completa.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | MODEL_TASK_ID | Sí | - | El ID de tarea del modelo 3D original que se va a riggear |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para acceso a la API de Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | No | - | Clave API para autenticación del servicio Comfy.org |
| `unique_id` | UNIQUE_ID | No | - | Identificador único para rastrear la operación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo del modelo 3D con rig generado |
| `rig task_id` | RIG_TASK_ID | El ID de tarea para rastrear el proceso de generación del rig |