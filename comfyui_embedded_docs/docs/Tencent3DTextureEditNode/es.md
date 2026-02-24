> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/es.md)

Este nodo utiliza la API Tencent Hunyuan3D para editar las texturas de un modelo 3D. Proporcionas un modelo 3D y una descripción textual de los cambios deseados, y el nodo devuelve una nueva versión del modelo con sus texturas redibujadas según tu indicación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sí | FBX, Cualquiera | Modelo 3D en formato FBX. El modelo debe tener menos de 100000 caras. |
| `prompt` | STRING | Sí | | Describe la edición de texturas. Admite hasta 1024 caracteres UTF-8. |
| `seed` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla. (por defecto: 0) |

**Nota:** La entrada `model_3d` debe ser un archivo en formato FBX. Este nodo no admite otros formatos de archivo 3D.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `GLB` | FILE3D | El modelo 3D procesado en formato GLB. |
| `FBX` | FILE3D | El modelo 3D procesado en formato FBX. |