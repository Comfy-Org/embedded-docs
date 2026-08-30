# Meshy: Texto a Modelo

El nodo Meshy: Text to Model utiliza la API de Meshy para generar un modelo 3D a partir de una descripción de texto. Envía una solicitud a la API con tu prompt y configuración, luego espera a que se complete la generación y descarga los archivos de modelo resultantes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Especifica la versión del modelo de IA a utilizar para la generación. | COMBO | Sí | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `prompt` | La descripción de texto del modelo 3D que deseas generar. Debe tener entre 1 y 600 caracteres. | STRING | Sí | 1 - 600 caracteres |
| `estilo` | El estilo artístico para el modelo 3D generado. | COMBO | Sí | `"realistic"` |
| `debe_remallar` | Cuando se establece en false, devuelve una malla triangular sin procesar. Seleccionar "true" revela parámetros adicionales para la topología y la cantidad de polígonos objetivo. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `topology` | El tipo de polígono objetivo para el modelo remallado. Este parámetro solo está disponible cuando `should_remesh` está establecido en "true". | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado. El valor predeterminado es 300000. Este parámetro solo está disponible cuando `should_remesh` está establecido en "true". | INT | No* | 100 - 300000 |
| `modo_simetría` | Controla la simetría en el modelo generado. Este es un parámetro avanzado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `modo_pose` | Especifica el modo de pose para el modelo generado. Una cadena vacía significa que no se solicita ninguna pose específica. Este es un parámetro avanzado. | COMBO | Sí | `""`<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. El valor predeterminado es 0. | INT | Sí | 0 - 2147483647 |
| `modo ultra` | Ejecuta una pasada de refinamiento adicional para una geometría de mayor fidelidad con un detalle de superficie más fino. El valor predeterminado es false. | BOOLEAN | Sí | true<br>false |

*Nota: Los parámetros `topology` y `target_polycount` están disponibles condicionalmente. Solo aparecen cuando el parámetro `should_remesh` está establecido en "true".

Cuando `ultra_mode` está habilitado, el parámetro `model` debe establecerse en `"meshy-7"` o `"latest"`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `archivo_modelo` | El nombre del archivo del modelo GLB generado. Esta salida se proporciona para compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único de la tarea de la API de Meshy. | MESHY_TASK_ID |
| `GLB` | El archivo de modelo 3D generado en formato GLB. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D generado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `131f17bfb788f206e15c1d48c877e822114902fadf073a6f9fb25e8340421122`
