> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/es.md)

Escala rápidamente una imagen mediante una llamada a la API de Stability hasta 4 veces su tamaño original. Este nodo está específicamente diseñado para escalar imágenes de baja calidad o comprimidas enviándolas al servicio de escalado rápido de Stability AI.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a escalar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen escalada devuelta por la API de Stability AI |