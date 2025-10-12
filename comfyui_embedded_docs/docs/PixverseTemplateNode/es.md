> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/es.md)

El nodo Plantilla de PixVerse te permite seleccionar entre las plantillas disponibles para la generación de videos de PixVerse. Convierte el nombre de plantilla seleccionado en el ID de plantilla correspondiente que la API de PixVerse requiere para la creación de videos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `plantilla` | STRING | Sí | Múltiples opciones disponibles | La plantilla a utilizar para la generación de videos de PixVerse. Las opciones disponibles corresponden a plantillas predefinidas en el sistema PixVerse. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `pixverse_template` | INT | El ID de plantilla correspondiente al nombre de plantilla seleccionado, que puede ser utilizado por otros nodos de PixVerse para la generación de videos. |