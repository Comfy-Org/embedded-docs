# Meshy: Imagen a Modelo

El nodo Meshy: Image to Model utiliza la API de Meshy para generar un modelo 3D a partir de una sola imagen de entrada. Carga su imagen, envía una tarea de procesamiento y devuelve los archivos del modelo 3D generado (GLB y FBX), junto con el ID de la tarea como referencia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA que se utilizará para la generación. | COMBO | Sí | `"latest"` |
| `imagen` | La imagen de entrada que se convertirá en un modelo 3D. | IMAGE | Sí | - |
| `remallar` | Cuando se establece en `"false"`, devuelve una malla triangular sin procesar. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `topology` | La topología de polígonos objetivo para el modelo remallado. Esta entrada solo está disponible cuando `should_remesh` se establece en `"true"`. | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado. Esta entrada solo está disponible cuando `should_remesh` se establece en `"true"`. Valor predeterminado: 300000. | INT | No* | 100 - 300000 |
| `modo de simetría` | Controla la simetría aplicada al modelo 3D generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas. Establecerlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `enable_pbr` | Genera mapas PBR (metálico, rugosidad, normal) además del color base. Esta entrada solo está disponible cuando `should_texture` se establece en `"true"`. Valor predeterminado: `False`. | BOOLEAN | No* | - |
| `texture_prompt` | Proporcione un prompt de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No se puede utilizar al mismo tiempo que `texture_image`. Esta entrada solo está disponible cuando `should_texture` se establece en `"true"`. Valor predeterminado: cadena vacía. | STRING | No* | - |
| `texture_image` | Solo se puede utilizar uno de `texture_image` o `texture_prompt` al mismo tiempo. Esta entrada solo está disponible cuando `should_texture` se establece en `"true"`. | IMAGE | No* | - |
| `modo de pose` | Especifique el modo de pose para el modelo generado. Este es un parámetro avanzado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. Valor predeterminado: 0. | INT | Sí | 0 - 2147483647 |

**Nota sobre las restricciones de parámetros:**

* Las entradas `topology` y `target_polycount` solo están disponibles cuando `should_remesh` se establece en `"true"`.
* Las entradas `enable_pbr`, `texture_prompt` y `texture_image` solo están disponibles cuando `should_texture` se establece en `"true"`.
* Cuando `should_texture` se establece en `"true"`, `texture_prompt` y `texture_image` no se pueden utilizar al mismo tiempo. Si se proporcionan ambos, el nodo genera un error.
* `texture_prompt` tiene una longitud máxima de 600 caracteres.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model_file` | El nombre de archivo del modelo GLB generado. Se mantiene solo por compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único para la tarea de la API de Meshy, que se puede utilizar como referencia o para la resolución de problemas. | MESHY_TASK_ID |
| `GLB` | El modelo 3D generado en el formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en el formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `9f7abcb0db3c78715e4ba7370efe294caf186590f7ab62da8568778848fc838c`
