> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/es.md)

Este nodo utiliza la API Tencent Hunyuan3D para analizar automáticamente un modelo 3D y generar o identificar sus componentes en función de su estructura. Procesa el modelo y devuelve un nuevo archivo FBX.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_3d` | FILE3D | Sí | FBX, Cualquiera | El modelo 3D a procesar. El modelo debe estar en formato FBX y tener menos de 30000 caras. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla para controlar si el nodo debe volver a ejecutarse. Los resultados son no deterministas independientemente del valor de la semilla. (por defecto: 0) |

**Nota:** La entrada `model_3d` solo admite archivos en formato FBX. Si se proporciona un formato de archivo 3D diferente, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `FBX` | FILE3DFBX | El modelo 3D procesado, devuelto como un archivo FBX. |
