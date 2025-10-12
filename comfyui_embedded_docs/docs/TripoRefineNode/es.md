> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/es.md)

El TripoRefineNode refina modelos 3D preliminares creados específicamente por modelos Tripo v1.4. Toma un ID de tarea de modelo y lo procesa a través de la API de Tripo para generar una versión mejorada del modelo. Este nodo está diseñado para trabajar exclusivamente con modelos preliminares producidos por modelos Tripo v1.4.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sí | - | Debe ser un modelo Tripo v1.4 |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para la API de Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | No | - | Clave API para servicios de Comfy.org |
| `unique_id` | UNIQUE_ID | No | - | Identificador único para la operación |

**Nota:** Este nodo solo acepta modelos preliminares creados por modelos Tripo v1.4. El uso de modelos de otras versiones puede resultar en errores.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | La ruta de archivo o referencia al modelo refinado |
| `model task_id` | MODEL_TASK_ID | El identificador de tarea para la operación del modelo refinado |
