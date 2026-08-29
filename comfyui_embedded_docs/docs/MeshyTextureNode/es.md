# Meshy: Modelo de Textura

El nodo Meshy: Texture aplica texturas generadas por IA a un modelo 3D. Toma un ID de tarea de un nodo anterior de generación o conversión 3D de Meshy y utiliza una descripción de texto o una imagen de referencia para crear nuevas texturas para el modelo. El nodo genera el modelo texturizado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | La versión del modelo de IA que se usará para el texturizado. | COMBO | Sí | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | El identificador único (ID de tarea) de una tarea anterior de generación o conversión 3D de Meshy. Este proporciona el modelo 3D base que se va a texturizar. | MESHY_TASK_ID | Sí | - |
| `habilitar_uv_original` | Utiliza la UV original del modelo en lugar de generar nuevas UV. Cuando está habilitado (predeterminado: `True`), Meshy conserva las texturas existentes del modelo cargado. Si el modelo no tiene UV original, la calidad del resultado podría no ser tan buena. Esta es una opción avanzada. | BOOLEAN | No | true / false |
| `pbr` | Habilita la salida de materiales de renderizado basado en física (PBR) para el modelo texturizado (predeterminado: `False`). Esta es una opción avanzada. | BOOLEAN | No | true / false |
| `estilo_texto` | Describe con texto el estilo de textura deseado para el objeto. Máximo 600 caracteres. No se puede usar al mismo tiempo que `image_style`. | STRING | No | - |
| `estilo_imagen` | Una imagen 2D para guiar el proceso de texturizado. No se puede usar al mismo tiempo que `text_style_prompt`. | IMAGE | No | - |
| `resolución de textura` | Resolución de la textura de color base. Las resoluciones más altas capturan más detalle de superficie. | COMBO | Sí | `"2k"`<br>`"4k"`<br>`"8k"` |

**Restricciones de parámetros:**

* Debe proporcionar un `text_style_prompt` o una `image_style`, pero no puede proporcionar ambos al mismo tiempo.
* El `text_style_prompt` está limitado a un máximo de 600 caracteres.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `archivo_modelo` | El nombre de archivo del modelo GLB generado. Esta salida se proporciona solo por compatibilidad con versiones anteriores. | STRING |
| `meshy_task_id` | El identificador único de tarea para este trabajo de texturizado, que puede usarse para hacer referencia al resultado. | MESHY_TASK_ID |
| `GLB` | El modelo 3D texturizado guardado en el formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo 3D texturizado guardado en el formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
