> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/es.md)

El nodo **Meshy: Imagen a Modelo** utiliza la API de Meshy para generar un modelo 3D a partir de una sola imagen de entrada. Carga tu imagen, envía una tarea de procesamiento y devuelve los archivos del modelo 3D generado (GLB y FBX) junto con el ID de la tarea para referencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"latest"` | Especifica la versión del modelo de IA a utilizar para la generación. |
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se convertirá en un modelo 3D. |
| `remallar` | COMBO DINÁMICO | Sí | `"true"`<br>`"false"` | Determina si la malla generada debe procesarse. Cuando se establece en `"false"`, el nodo devuelve una malla triangular sin procesar. |
| `topology` | COMBO | No* | `"triangle"`<br>`"quad"` | La topología de polígonos objetivo para el modelo remallado. Esta entrada solo está disponible cuando `remallar` está configurado en `"true"`. |
| `target_polycount` | INT | No* | 100 - 300000 | El número objetivo de polígonos para el modelo remallado. Esta entrada solo está disponible cuando `remallar` está configurado en `"true"`. El valor predeterminado es 300000. |
| `modo de simetría` | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` | Controla la simetría aplicada al modelo 3D generado. |
| `texturizar` | COMBO DINÁMICO | Sí | `"true"`<br>`"false"` | Determina si se generan texturas para el modelo. Configurarlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. |
| `enable_pbr` | BOOLEAN | No* | - | Cuando `texturizar` es `"true"`, esta opción genera mapas PBR (metálico, rugosidad, normal) además del color base. El valor predeterminado es `False`. |
| `texture_prompt` | STRING | No* | - | Un prompt de texto para guiar el proceso de texturizado (máximo 600 caracteres). Esta entrada solo está disponible cuando `texturizar` está configurado en `"true"`. No se puede usar al mismo tiempo que `texture_image`. |
| `texture_image` | IMAGE | No* | - | Una imagen para guiar el proceso de texturizado. Esta entrada solo está disponible cuando `texturizar` está configurado en `"true"`. No se puede usar al mismo tiempo que `texture_prompt`. |
| `modo de pose` | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` | Especifica el modo de pose para el modelo generado. Este es un parámetro avanzado. |
| `semilla` | INT | Sí | 0 - 2147483647 | Un valor de semilla para el proceso de generación. Los resultados no son deterministas independientemente del valor de la semilla. El valor predeterminado es 0. |

**Nota sobre las restricciones de parámetros:**

* Las entradas `topology` y `target_polycount` solo están disponibles cuando `should_remesh` está configurado en `"true"`.
* Las entradas `enable_pbr`, `texture_prompt` y `texture_image` solo están disponibles cuando `should_texture` está configurado en `"true"`.
* No se pueden usar `texture_prompt` y `texture_image` al mismo tiempo. Si ambos se proporcionan cuando `should_texture` es `"true"`, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `meshy_task_id` | STRING | El nombre del archivo del modelo GLB generado. (Se mantiene para compatibilidad hacia atrás). |
| `GLB` | MESHY_TASK_ID | El identificador único para la tarea de la API de Meshy, que se puede usar como referencia o para solucionar problemas. |
| `FBX` | FILE3DGLB | El modelo 3D generado en formato de archivo GLB. |
| `FBX` | FILE3DFBX | El modelo 3D generado en formato de archivo FBX. |

---
**Source fingerprint (SHA-256):** `134d9250d8b447bbbd2905f827e81b67f491ba355ebb93d4d256324b644100a2`
