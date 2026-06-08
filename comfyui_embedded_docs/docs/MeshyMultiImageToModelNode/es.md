Este nodo utiliza la API de Meshy para generar un modelo 3D a partir de múltiples imágenes de entrada. Carga las imágenes proporcionadas, envía una tarea de procesamiento y devuelve los archivos del modelo 3D resultante (GLB y FBX) junto con el ID de la tarea para referencia.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Especifica la versión del modelo de IA a utilizar. | COMBO | Sí | `"latest"` |
| `imágenes` | Un conjunto de imágenes utilizado para generar el modelo 3D. Debes proporcionar entre 2 y 4 imágenes. | IMAGE | Sí | 2 a 4 imágenes |
| `remallar` | Determina si la malla generada debe procesarse. Cuando se establece en `"false"`, el nodo devuelve una malla triangular sin procesar. | COMBO | Sí | `"true"`<br>`"false"` |
| `topology` | El tipo de polígono objetivo para la salida remallada. Este parámetro solo está disponible y es requerido cuando `remallar` está configurado en `"true"`. | COMBO | No | `"triangle"`<br>`"quad"` |
| `target_polycount` | El número objetivo de polígonos para el modelo remallado (predeterminado: 300000). Este parámetro solo está disponible cuando `remallar` está configurado en `"true"`. | INT | No | 100 a 300000 |
| `modo de simetría` | Controla si se aplica simetría al modelo generado. | COMBO | Sí | `"auto"`<br>`"on"`<br>`"off"` |
| `texturizar` | Determina si se generan texturas. Configurarlo en `"false"` omite la fase de texturizado y devuelve una malla sin texturas. | COMBO | Sí | `"true"`<br>`"false"` |
| `enable_pbr` | Cuando `texturizar` es `"true"`, esta opción genera mapas PBR (metálico, rugosidad, normal) además del color base (predeterminado: False). | BOOLEAN | No | True / False |
| `texture_prompt` | Un prompt de texto para guiar el proceso de texturizado (máximo 600 caracteres). No se puede usar al mismo tiempo que `texture_image`. Este parámetro solo está disponible cuando `texturizar` está configurado en `"true"`. | STRING | No | - |
| `texture_image` | Una imagen para guiar el proceso de texturizado. Solo se puede usar uno de `texture_image` o `texture_prompt` al mismo tiempo. Este parámetro solo está disponible cuando `texturizar` está configurado en `"true"`. | IMAGE | No | - |
| `modo de pose` | Especifica el modo de pose para el modelo generado. | COMBO | Sí | `""` (vacío)<br>`"A-pose"`<br>`"T-pose"` |
| `semilla` | Un valor de semilla para el proceso de generación (predeterminado: 0). Los resultados no son deterministas independientemente de la semilla, pero cambiar la semilla puede hacer que el nodo se vuelva a ejecutar. | INT | Sí | 0 a 2147483647 |

**Restricciones de Parámetros:**

* Debes proporcionar entre 2 y 4 imágenes para la entrada `images`.
* Los parámetros `topology` y `target_polycount` solo están activos cuando `should_remesh` está configurado en `"true"`.
* Los parámetros `enable_pbr`, `texture_prompt` y `texture_image` solo están activos cuando `should_texture` está configurado en `"true"`.
* No puedes usar `texture_prompt` y `texture_image` al mismo tiempo; son mutuamente excluyentes.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `meshy_task_id` | El nombre del archivo del modelo GLB generado. Esta salida se proporciona para compatibilidad con versiones anteriores. | STRING |
| `GLB` | El identificador único para la tarea de la API de Meshy. | MESHY_TASK_ID |
| `FBX` | El modelo 3D generado en formato GLB. | FILE3DGLB |
| `FBX` | El modelo 3D generado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `e6f75f50645c8b2cf5ebbe037edb077ef1eb0ea1baf67c581d60ac0033686d00`
