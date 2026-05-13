> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/es.md)

# Meshy: Texto a Modelo

El nodo Meshy: Texto a Modelo utiliza la API de Meshy para generar un modelo 3D a partir de una descripción textual. Envía una solicitud a la API con tu indicación y configuración, luego espera a que se complete la generación y descarga los archivos del modelo resultante.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `modelo` | COMBO | Sí | `"latest"` | Especifica la versión del modelo de IA a utilizar. Actualmente, solo está disponible la versión "latest". |
| `prompt` | STRING | Sí | - | La descripción textual del modelo 3D que deseas generar. Debe tener entre 1 y 600 caracteres. |
| `estilo` | COMBO | Sí | `"realistic"`<br>`"sculpture"` | El estilo artístico para el modelo 3D generado. |
| `debe_remallar` | DYNAMIC COMBO | Sí | `"true"`<br>`"false"` | Controla si la malla generada se procesa. Cuando se establece en "false", el nodo devuelve una malla triangular sin procesar. Seleccionar "true" revela parámetros adicionales para topología y recuento de polígonos. |
| `topology` | COMBO | No* | `"triangle"`<br>`"quad"` | El tipo de polígono objetivo para el modelo remallado. Este parámetro solo está disponible y es requerido cuando `debe_remallar` está establecido en "true". |
| `target_polycount` | INT | No* | 100 - 300000 | El número objetivo de polígonos para el modelo remallado. El valor predeterminado es 300000. Este parámetro solo está disponible y es requerido cuando `debe_remallar` está establecido en "true". |
| `modo_simetría` | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` | Controla la simetría en el modelo generado. |
| `modo_pose` | COMBO | Sí | `""`<br>`"A-pose"`<br>`"T-pose"` | Especifica el modo de pose para el modelo generado. Una cadena vacía significa que no se solicita ninguna pose específica. |
| `semilla` | INT | Sí | 0 - 2147483647 | Un valor de semilla para la generación. Configurar esto controla si el nodo debe re-ejecutarse, pero los resultados no son deterministas independientemente del valor de la semilla. El valor predeterminado es 0. |

*Nota: Los parámetros `topology` y `target_polycount` son condicionalmente requeridos. Solo aparecen y deben configurarse cuando el parámetro `should_remesh` está establecido en "true".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `meshy_task_id` | STRING | El nombre del archivo del modelo GLB generado. Esta salida se proporciona para compatibilidad hacia atrás. |
| `GLB` | MESHY_TASK_ID | El identificador único para la tarea de la API de Meshy. |
| `FBX` | FILE3DGLB | El archivo de modelo 3D generado en formato GLB. |
| `FBX` | FILE3DFBX | El archivo de modelo 3D generado en formato FBX. |

---
**Source fingerprint (SHA-256):** `122eee5488a89433bd1f3bf79ccd8e9c51fd23cc1dfb208c39a0628c2ad3d817`
