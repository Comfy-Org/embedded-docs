El nodo **Meshy: Texture** aplica texturas generadas por IA a un modelo 3D. Toma un ID de tarea de un nodo anterior de generación o conversión 3D de Meshy y utiliza una descripción de texto o una imagen de referencia para crear nuevas texturas para el modelo. El nodo genera el modelo texturizado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | La versión del modelo de IA a utilizar para texturizar. Actualmente, solo está disponible la versión "latest". | COMBO | Sí | `"latest"` |
| `meshy_task_id` | El identificador único (ID de tarea) de una tarea anterior de generación o conversión 3D de Meshy. Esto proporciona el modelo 3D base que se va a texturizar. | MESHY_TASK_ID | Sí | - |
| `habilitar_uv_original` | Utiliza el UV original del modelo en lugar de generar nuevos UV. Cuando está habilitado (predeterminado: `True`), Meshy conserva las texturas existentes del modelo cargado. Si el modelo no tiene UV original, la calidad del resultado podría no ser óptima. | BOOLEAN | No | - |
| `pbr` | Habilita la salida de material de Renderizado Basado en Física (PBR) para el modelo texturizado (predeterminado: `False`). | BOOLEAN | No | - |
| `estilo_texto` | Describe el estilo de textura deseado del objeto usando texto. Máximo 600 caracteres. No puede usarse al mismo tiempo que `estilo_imagen`. | STRING | No | - |
| `estilo_imagen` | Una imagen 2D para guiar el proceso de texturizado. No puede usarse al mismo tiempo que `estilo_texto`. | IMAGE | No | - |

**Restricciones de parámetros:**

* Debes proporcionar ya sea un `text_style_prompt` o un `image_style`, pero no puedes proporcionar ambos al mismo tiempo.
* El `text_style_prompt` está limitado a un máximo de 600 caracteres.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `meshy_task_id` | El nombre del archivo del modelo GLB generado. Esta salida se proporciona para compatibilidad con versiones anteriores. | STRING |
| `GLB` | El identificador único de la tarea para este trabajo de texturizado, que puede usarse para hacer referencia al resultado. | MODEL_TASK_ID |
| `FBX` | El modelo 3D texturizado guardado en el formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo 3D texturizado guardado en el formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `380b682a8290c69e71a204c8c3d6c2d4fb2c15f4bc1679b98c7fc4fd9ec9e1b3`
