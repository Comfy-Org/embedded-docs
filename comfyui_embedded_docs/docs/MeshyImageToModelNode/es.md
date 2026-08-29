# Meshy: Imagen a Modelo

El nodo **Meshy: Image to Model** utiliza la API de Meshy para generar un modelo 3D a partir de una única imagen de entrada. Carga su imagen, envía una tarea de procesamiento y devuelve los archivos del modelo 3D generado (GLB y FBX) junto con el ID de la tarea como referencia.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA que se usará para la generación. | COMBO | Sí | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `imagen` | La imagen de entrada para convertir en un modelo 3D. | IMAGE | Sí | - |
| `remallar` | Cuando se establece en `"false"`, devuelve una malla triangular sin procesar. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `topology` | La topología de polígonos objetivo para el modelo remallado. Esta entrada solo está disponible cuando `should_remesh` está establecido en `"true"`. | COMBO | No* | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado. Esta entrada solo está disponible cuando `should_remesh` está establecido en `"true"`. Valor predeterminado: 300000. | INT | No* | 100 - 300000 |
| `modo de simetría` | Controla la simetría aplicada al modelo 3D generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas. Establecerlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `enable_pbr` | Genera mapas PBR (metallic, roughness, normal) además del color base. Esta entrada solo está disponible cuando `should_texture` está establecido en `"true"`. Valor predeterminado: `False`. | BOOLEAN | No* | - |
| `texture_prompt` | Proporciona un prompt de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No se puede usar al mismo tiempo que `texture_image`. Esta entrada solo está disponible cuando `should_texture` está establecido en `"true"`. Valor predeterminado: cadena vacía. | STRING | No* | - |
| `texture_image` | Solo se puede usar uno de `texture_image` o `texture_prompt` al mismo tiempo. Esta entrada solo está disponible cuando `should_texture` está establecido en `"true"`. | IMAGE | No* | - |
| `texture_resolution` | Resolución de la textura de color base. Las resoluciones más altas capturan más detalle de superficie. Esta entrada solo está disponible cuando `should_texture` está establecido en `"true"`. | COMBO | No* | `"2k"`<br>`"4k"`<br>`"8k"` |
| `modo de pose` | Especifica el modo de pose para el modelo generado. Este es un parámetro avanzado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. Valor predeterminado: 0. | INT | Sí | 0 - 2147483647 |
| `modo ultra` | Ejecuta una pasada de refinamiento adicional para una geometría de mayor fidelidad con un detalle de superficie más fino. Valor predeterminado: `False`. | BOOLEAN | Sí | - |

**Nota sobre las restricciones de parámetros:**

* Las entradas `topology` y `target_polycount` solo están disponibles cuando `should_remesh` está establecido en `"true"`.
* Las entradas `enable_pbr`, `texture_prompt`, `texture_image` y `texture_resolution` solo están disponibles cuando `should_texture` está establecido en `"true"`.
* Cuando `should_texture` está establecido en `"true"`, `texture_prompt` y `texture_image` no pueden usarse al mismo tiempo. Si se proporcionan ambos, el nodo genera un error.
* `texture_prompt` tiene una longitud máxima de 600 caracteres.
* `ultra_mode` requiere el modelo `"meshy-7"` o `"latest"`. Si `ultra_mode` está habilitado con el modelo `"meshy-6"`, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model_file` | El nombre de archivo del modelo GLB generado. Se mantiene solo por compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único de la tarea de la API de Meshy, que se puede utilizar como referencia o para solucionar problemas. | MESHY_TASK_ID |
| `GLB` | El modelo 3D generado en el formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en el formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `689828ad52de4493e1039aecc408e18af4122d2c0e2511fd254ba0f1d56bad14`
