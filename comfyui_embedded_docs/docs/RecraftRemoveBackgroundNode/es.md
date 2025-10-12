> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/es.md)

Este nodo elimina el fondo de imágenes utilizando el servicio API de Recraft. Procesa cada imagen en el lote de entrada y devuelve tanto las imágenes procesadas con fondos transparentes como las máscaras alfa correspondientes que indican las áreas del fondo eliminadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La(s) imagen(es) de entrada a procesar para eliminación de fondo |
| `auth_token` | STRING | No | - | Token de autenticación para acceso a la API de Recraft |
| `comfy_api_key` | STRING | No | - | Clave API para integración con el servicio Comfy.org |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | Imágenes procesadas con fondos transparentes |
| `mask` | MASK | Máscaras de canal alfa que indican las áreas del fondo eliminadas |