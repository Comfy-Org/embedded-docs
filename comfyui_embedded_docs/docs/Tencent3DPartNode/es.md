Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/en.md)

Este nodo utiliza la API de Tencent Hunyuan3D para analizar automáticamente un modelo 3D y generar o identificar sus componentes según su estructura. Procesa el modelo y devuelve un nuevo archivo FBX.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo_3d` | El modelo 3D a procesar. El modelo debe estar en formato FBX y tener menos de 30000 caras. | FILE3D | Sí | FBX, Cualquiera |
| `semilla` | Un valor de semilla para controlar si el nodo debe re-ejecutarse. Los resultados no son deterministas independientemente del valor de la semilla. (predeterminado: 0) | INT | No | 0 a 2147483647 |

**Nota:** La entrada `model_3d` solo admite archivos en formato FBX. Si se proporciona un formato de archivo 3D diferente, el nodo generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `FBX` | El modelo 3D procesado, devuelto como un archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/es.md)

---
**Source fingerprint (SHA-256):** `eae7d0197d4391af1f5f24f120c64f1045649182108affad10b9a00f329310fe`
