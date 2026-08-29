# Meshy: Multi-Imagen a Modelo

Este nodo utiliza la API de Meshy para generar un modelo 3D a partir de múltiples imágenes de entrada. Carga las imágenes proporcionadas, envía una tarea de procesamiento y devuelve los archivos del modelo 3D resultante (GLB y FBX) junto con el ID de la tarea como referencia.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA a utilizar. | COMBO | Sí | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `remallar` | Determina si la malla generada se procesa. Cuando se establece en `"false"`, el nodo devuelve una malla triangular sin procesar. Cuando se establece en `"true"`, se muestran los ajustes de remallado siguientes. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `modo de simetría` | Controla si se aplica simetría al modelo generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas. Establecerlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. Cuando se establece en `"true"`, se muestran los ajustes de texturizado siguientes. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `modo de pose` | Especifica el modo de pose para el modelo generado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 0) | INT | Sí | 0 a 2147483647 |

### Configuración de remallado (visible cuando `should_remesh` es `"true"`)

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `topology` | El tipo de polígono objetivo para la salida remallada. | COMBO | No | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado (predeterminado: 300000). | INT | No | 100 a 300000 |

### Configuración de texturas (visible cuando `should_texture` es `"true"`)

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Generar mapas PBR (metálico, rugosidad, normal) además del color base. (predeterminado: False) | BOOLEAN | No | True / False |
| `texture_prompt` | Proporciona una instrucción de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No puede usarse al mismo tiempo que `texture_image`. (predeterminado: vacío) | STRING | No | Hasta 600 caracteres |
| `texture_image` | Solo se puede usar uno de `texture_image` o `texture_prompt` al mismo tiempo. | IMAGE | No | - |
| `texture_resolution` | Resolución de la textura de color base. Las resoluciones más altas capturan más detalle de superficie. | COMBO | No | `"2k"`<br>`"4k"`<br>`"8k"` |

### Entradas de imagen

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Ranura ampliable: conecte de 2 a 4 imágenes de entrada (`image_1`, `image_2`, `image_3`, `image_4`). Estas imágenes se utilizan para generar el modelo 3D. | IMAGE | Sí | 2 a 4 imágenes |

**Notas**

* Debe proporcionar entre 2 y 4 imágenes para la entrada `images`.
* Los parámetros `topology` y `target_polycount` solo están activos cuando `should_remesh` está establecido en `"true"`.
* Los parámetros `enable_pbr`, `texture_prompt`, `texture_image` y `texture_resolution` solo están activos cuando `should_texture` está establecido en `"true"`.
* `texture_prompt` y `texture_image` son mutuamente excluyentes; no se pueden usar ambos al mismo tiempo. `texture_prompt` está limitado a 600 caracteres.
* El valor de `seed` no hace que los resultados sean deterministas; cambiarlo simplemente hace que el nodo vuelva a ejecutar la tarea de generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model_file` | El nombre de archivo del modelo GLB generado. Esta salida se proporciona únicamente por compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único para la tarea de la API de Meshy. | MESHY_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `a8b2fc23ef8a8a4af097489c15beb3e0ed205dfdc8309afc95207d7a5616d37a`
