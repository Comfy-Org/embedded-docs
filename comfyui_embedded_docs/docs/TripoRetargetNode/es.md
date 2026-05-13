> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/es.md)

El nodo TripoRetargetNode aplica animaciones predefinidas a modelos de personajes 3D mediante la reorientación de datos de movimiento. Toma un modelo 3D previamente riggeado y aplica una de varias animaciones preestablecidas, generando como salida un archivo de modelo 3D animado. El nodo se comunica con la API de Tripo para procesar la operación de reorientación de animación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `original_model_task_id` | RIG_TASK_ID | Sí | - | El ID de tarea del modelo 3D riggeado previamente procesado al que se le aplicará la animación |
| `animation` | STRING | Sí | "preset:idle"<br>"preset:walk"<br>"preset:run"<br>"preset:dive"<br>"preset:climb"<br>"preset:jump"<br>"preset:slash"<br>"preset:shoot"<br>"preset:hurt"<br>"preset:fall"<br>"preset:turn"<br>"preset:quadruped:walk"<br>"preset:hexapod:walk"<br>"preset:octopod:walk"<br>"preset:serpentine:march"<br>"preset:aquatic:march" | La animación preestablecida a aplicar al modelo 3D. Las opciones incluyen animaciones humanoides (inactivo, caminar, correr, bucear, escalar, saltar, cortar, disparar, herido, caer, girar) y animaciones de criaturas (caminar cuadrúpedo, caminar hexápodo, caminar octópodo, marcha serpentina, marcha acuática). |
| `auth_token_comfy_org` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para acceso a la API de Comfy.org (parámetro oculto) |
| `api_key_comfy_org` | API_KEY_COMFY_ORG | No | - | Clave API para acceso al servicio de Comfy.org (parámetro oculto) |
| `unique_id` | UNIQUE_ID | No | - | Identificador único para el seguimiento de la operación (parámetro oculto) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model_file` | STRING | El archivo de modelo 3D animado generado (solo para compatibilidad hacia atrás) |
| `retarget task_id` | RETARGET_TASK_ID | El ID de tarea para el seguimiento de la operación de reorientación |
| `GLB` | FILE3DGLB | El modelo 3D animado en formato GLB |

---
**Source fingerprint (SHA-256):** `304326afdc1fa3e8c3593f151f771f93520e061802c831838c58ebc401b9e9e2`
