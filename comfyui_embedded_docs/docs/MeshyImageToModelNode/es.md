# Meshy: Imagen a Modelo

El nodo **Meshy: Imagen a Modelo** utiliza la API de Meshy para generar un modelo 3D a partir de una sola imagen de entrada. Carga tu imagen, envía una tarea de procesamiento y devuelve los archivos del modelo 3D generado (GLB y FBX) junto con el ID de la tarea para referencia.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA a utilizar para la generación. | COMBO | Sí | `"latest"` |
| `imagen` | La imagen de entrada que se convertirá en un modelo 3D. | IMAGE | Sí | - |
| `remallar` | Determina si la malla generada debe procesarse. Cuando se establece en `"false"`, el nodo devuelve una malla triangular sin procesar. | COMBO DINÁMICO | Sí | `"true"`<br>`"false"` |
| `topology` | La topología de polígonos objetivo para el modelo remallado. Esta entrada solo está disponible cuando `remallar` está configurado en `"true"`. | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado. Esta entrada solo está disponible cuando `remallar` está configurado en `"true"`. El valor predeterminado es 300000. | INT | No* | 100 - 300000 |
| `modo de simetría` | Controla la simetría aplicada al modelo 3D generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas para el modelo. Configurarlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. | COMBO DINÁMICO | Sí | `"true"`<br>`"false"` |
| `enable_pbr` | Cuando `texturizar` es `"true"`, esta opción genera mapas PBR (metálico, rugosidad, normal) además del color base. El valor predeterminado es `False`. | BOOLEAN | No* | - |
| `texture_prompt` | Un prompt de texto para guiar el proceso de texturizado (máximo 600 caracteres). Esta entrada solo está disponible cuando `texturizar` está configurado en `"true"`. No se puede usar al mismo tiempo que `texture_image`. | STRING | No* | - |
| `texture_image` | Una imagen para guiar el proceso de texturizado. Esta entrada solo está disponible cuando `texturizar` está configurado en `"true"`. No se puede usar al mismo tiempo que `texture_prompt`. | IMAGE | No* | - |
| `modo de pose` | Especifica el modo de pose para el modelo generado. Este es un parámetro avanzado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | Un valor de semilla para el proceso de generación. Los resultados no son deterministas independientemente del valor de la semilla. El valor predeterminado es 0. | INT | Sí | 0 - 2147483647 |

**Nota sobre las restricciones de parámetros:**

* Las entradas `topology` y `target_polycount` solo están disponibles cuando `should_remesh` está configurado en `"true"`.
* Las entradas `enable_pbr`, `texture_prompt` y `texture_image` solo están disponibles cuando `should_texture` está configurado en `"true"`.
* No se pueden usar `texture_prompt` y `texture_image` al mismo tiempo. Si ambos se proporcionan cuando `should_texture` es `"true"`, el nodo generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model_file` | El nombre del archivo del modelo GLB generado. (Se mantiene para compatibilidad hacia atrás). | STRING |
| `meshy_task_id` | El identificador único para la tarea de la API de Meshy, que se puede usar como referencia o para solucionar problemas. | MESHY_TASK_ID |
| `GLB` | El modelo 3D generado en formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
