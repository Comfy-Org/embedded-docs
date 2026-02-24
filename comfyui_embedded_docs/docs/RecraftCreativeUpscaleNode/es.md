> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreativeUpscaleNode/es.md)

El nodo Recraft Creative Upscale Image mejora una imagen rasterizada aumentando su resolución. Utiliza un proceso de "escalado creativo" que se centra en mejorar los pequeños detalles y los rostros dentro de la imagen. Esta operación se realiza de forma síncrona a través de una API externa.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | | La imagen de entrada que se va a escalar. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen escalada resultante con detalles mejorados. |
