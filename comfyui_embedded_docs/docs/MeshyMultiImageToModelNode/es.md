# Meshy: Multi-Imagen a Modelo

Este nodo utiliza la API de Meshy para generar un modelo 3D a partir de varias imágenes de entrada. Sube las imágenes proporcionadas, envía una tarea de procesamiento y devuelve los archivos del modelo 3D resultante (GLB y FBX) junto con el ID de la tarea para referencia.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA a utilizar. | COMBO | Sí | `"latest"` |
| `remallar` | Determina si la malla generada debe procesarse. Cuando se establece en `"false"`, el nodo devuelve una malla triangular sin procesar. Cuando se establece en `"true"`, se muestran los ajustes de remallado a continuación. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `modo de simetría` | Controla si se aplica simetría al modelo generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas. Establecerlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. Cuando se establece en `"true"`, se muestran los ajustes de textura a continuación. | DYNAMIC_COMBO | Sí | `"true"`<br>`"false"` |
| `modo de pose` | Especifica el modo de pose para el modelo generado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (por defecto: 0) | INT | Sí | 0 a 2147483647 |

### Ajustes de remallado (visibles cuando `should_remesh` se establece en `"true"`)

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `topology` | El tipo de polígono objetivo para la salida remallada. | COMBO | No | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado (por defecto: 300000). | INT | No | 100 a 300000 |

### Ajustes de textura (visibles cuando `should_texture` se establece en `"true"`)

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Genera mapas PBR (metálico, rugosidad, normal) además del color base. (por defecto: False) | BOOLEAN | No | True / False |
| `texture_prompt` | Proporciona un mensaje de texto para guiar el proceso de texturizado. Máximo 600 caracteres. No puede usarse al mismo tiempo que `texture_image`. (por defecto: vacío) | STRING | No | - |
| `texture_image` | Solo uno de `texture_image` o `texture_prompt` puede usarse al mismo tiempo. | IMAGE | No | - |

### Entradas de imagen

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Ranura ampliable: conecta de 2 a 4 imágenes de entrada (`image_1`, `image_2`, `image_3`, `image_4`). Estas imágenes se utilizan para generar el modelo 3D. | IMAGE | Sí | 2 a 4 imágenes |

**Notas**

* Debes proporcionar entre 2 y 4 imágenes para la entrada `images`.
* Los parámetros `topology` y `target_polycount` solo están activos cuando `should_remesh` se establece en `"true"`.
* Los parámetros `enable_pbr`, `texture_prompt` y `texture_image` solo están activos cuando `should_texture` se establece en `"true"`.
* `texture_prompt` y `texture_image` son mutuamente excluyentes; no puedes usar ambos al mismo tiempo. `texture_prompt` está limitado a 600 caracteres.
* El valor de `seed` no hace que los resultados sean deterministas; cambiarlo simplemente hace que el nodo vuelva a ejecutar la tarea de generación.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model_file` | El nombre del archivo del modelo GLB generado. Esta salida se proporciona únicamente por compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único para la tarea de la API de Meshy. | MESHY_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `c2282cad611bbbc8c0a618df6a68fcd9f6e3c29c6d08b2c96a117c29765d8a7a`
