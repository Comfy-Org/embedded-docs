> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftVectorizeImageNode/es.md)

Genera SVG de forma síncrona a partir de una imagen de entrada. Este nodo convierte imágenes rasterizadas a formato de gráficos vectoriales procesando cada imagen en el lote de entrada y combinando los resultados en una única salida SVG.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a convertir a formato SVG |
| `auth_token` | AUTH_TOKEN_COMFY_ORG | No | - | Token de autenticación para acceso a la API |
| `comfy_api_key` | API_KEY_COMFY_ORG | No | - | Clave API para servicios de Comfy.org |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `SVG` | SVG | La salida de gráficos vectoriales generada que combina todas las imágenes procesadas |