# Bria Quitar Fondo de Video

Este nodo elimina el fondo de un video utilizando el servicio de IA de Bria. Procesa el video de entrada y reemplaza el fondo original con un color sólido de su elección. La operación se realiza a través de una API externa, y el resultado se devuelve como un nuevo archivo de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El archivo de video de entrada del cual se eliminará el fondo. | VIDEO | Sí | N/A |
| `color de fondo` | El color sólido que se usará como nuevo fondo para el video de salida. | STRING | Sí | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `semilla` | Un valor de semilla que controla si el nodo debe volver a ejecutarse. Los resultados no son deterministas independientemente del valor de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Nota:** El video de entrada debe tener una duración de 60 segundos o menos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video procesado con el fondo eliminado y reemplazado por el color seleccionado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/es.md)

---
**Source fingerprint (SHA-256):** `51499fc006d3fd3fd45f8aad686d92537d399255b3a583fd54b77c5a0698a068`
