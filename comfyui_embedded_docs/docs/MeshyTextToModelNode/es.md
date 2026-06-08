# Meshy: Texto a Modelo

El nodo Meshy: Texto a Modelo utiliza la API de Meshy para generar un modelo 3D a partir de una descripción textual. Envía una solicitud a la API con tu indicación y configuración, luego espera a que se complete la generación y descarga los archivos del modelo resultante.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA a utilizar. Actualmente, solo está disponible la versión "latest". | COMBO | Sí | `"latest"` |
| `prompt` | La descripción textual del modelo 3D que deseas generar. Debe tener entre 1 y 600 caracteres. | STRING | Sí | - |
| `estilo` | El estilo artístico para el modelo 3D generado. | COMBO | Sí | `"realistic"`<br>`"sculpture"` |
| `debe_remallar` | Controla si la malla generada se procesa. Cuando se establece en "false", el nodo devuelve una malla triangular sin procesar. Seleccionar "true" revela parámetros adicionales para topología y recuento de polígonos. | DYNAMIC COMBO | Sí | `"true"`<br>`"false"` |
| `topology` | El tipo de polígono objetivo para el modelo remallado. Este parámetro solo está disponible y es requerido cuando `debe_remallar` está establecido en "true". | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado. El valor predeterminado es 300000. Este parámetro solo está disponible y es requerido cuando `debe_remallar` está establecido en "true". | INT | No* | 100 - 300000 |
| `modo_simetría` | Controla la simetría en el modelo generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `modo_pose` | Especifica el modo de pose para el modelo generado. Una cadena vacía significa que no se solicita ninguna pose específica. | COMBO | Sí | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | Un valor de semilla para la generación. Configurar esto controla si el nodo debe re-ejecutarse, pero los resultados no son deterministas independientemente del valor de la semilla. El valor predeterminado es 0. | INT | Sí | 0 - 2147483647 |

*Nota: Los parámetros `topology` y `target_polycount` son condicionalmente requeridos. Solo aparecen y deben configurarse cuando el parámetro `should_remesh` está establecido en "true".

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `meshy_task_id` | El nombre del archivo del modelo GLB generado. Esta salida se proporciona para compatibilidad hacia atrás. | STRING |
| `GLB` | El identificador único para la tarea de la API de Meshy. | MESHY_TASK_ID |
| `FBX` | El archivo de modelo 3D generado en formato GLB. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D generado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
