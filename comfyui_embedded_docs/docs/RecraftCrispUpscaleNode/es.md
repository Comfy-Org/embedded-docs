> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/es.md)

Escala imágenes de forma síncrona. Mejora una imagen rasterizada dada utilizando la herramienta 'crisp upscale', aumentando la resolución de la imagen y haciendo que esta sea más nítida y limpia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a escalar |
| `auth_token` | STRING | No | - | Token de autenticación para la API de Recraft |
| `comfy_api_key` | STRING | No | - | Clave API para los servicios de Comfy.org |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen escalada con resolución y claridad mejoradas |