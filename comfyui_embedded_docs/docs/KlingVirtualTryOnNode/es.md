> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/es.md)

Nodo Kling Virtual Try On. Ingresa una imagen humana y una imagen de ropa para probar la prenda en la persona. Puedes combinar múltiples imágenes de artículos de ropa en una sola imagen con fondo blanco.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | Sí | - | La imagen humana sobre la que se probará la ropa |
| `cloth_image` | IMAGE | Sí | - | La imagen de la prenda que se probará en la persona |
| `model_name` | STRING | Sí | `"kolors-virtual-try-on-v1"` | El modelo de prueba virtual que se utilizará (predeterminado: "kolors-virtual-try-on-v1") |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen resultante que muestra a la persona con el artículo de ropa probado |
