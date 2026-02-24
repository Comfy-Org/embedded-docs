> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/es.md)

Este nodo elimina el fondo de un video utilizando el servicio de IA Bria. Procesa el video de entrada y reemplaza el fondo original con un color sólido de su elección. La operación se realiza a través de una API externa y el resultado se devuelve como un nuevo archivo de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | N/A | El archivo de video de entrada del cual se eliminará el fondo. |
| `background_color` | STRING | Sí | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` | El color sólido que se utilizará como nuevo fondo para el video de salida. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla que controla si el nodo debe volver a ejecutarse. Los resultados no son deterministas independientemente del valor de la semilla. (por defecto: 0) |

**Nota:** El video de entrada debe tener una duración de 60 segundos o menos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video procesado con el fondo eliminado y reemplazado por el color seleccionado. |