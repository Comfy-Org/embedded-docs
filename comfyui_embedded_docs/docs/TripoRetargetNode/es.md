> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/es.md)

El TripoRetargetNode aplica animaciones predefinidas a modelos de personajes 3D mediante la reorientación de datos de movimiento. Toma un modelo 3D previamente procesado y aplica una de varias animaciones preestablecidas, generando un archivo de modelo 3D animado como salida. El nodo se comunica con la API de Tripo para procesar la operación de reorientación de animación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Sí | - | El ID de tarea del modelo 3D previamente procesado al que se aplicará la animación |
| `animation` | STRING | Sí | "preset:idle"<br>"preset:walk"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn" | La animación preestablecida que se aplicará al modelo 3D |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para acceso a la API de Comfy.org |
| `comfy_api_key` | API_KEY_COMFY_ORG | No | - | Clave API para acceso al servicio de Comfy.org |
| `unique_id` | UNIQUE_ID | No | - | Identificador único para rastrear la operación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo de modelo 3D animado generado |
| `retarget task_id` | RETARGET_TASK_ID | El ID de tarea para rastrear la operación de reorientación |