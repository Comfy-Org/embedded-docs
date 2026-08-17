# Hunyuan3D: Parte 3D

Este nodo utiliza la API Tencent Hunyuan3D para analizar automáticamente un modelo 3D e identificar o generar sus componentes según la estructura del modelo. Procesa el modelo y devuelve un nuevo archivo FBX.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Modelo 3D en formato FBX. El modelo debe tener menos de 30000 caras. | FILE3D | Sí | FBX, Any |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla. (predeterminado: 0) | INT | No | 0 to 2147483647 |

**Nota:** La entrada `model_3d` solo admite archivos en formato FBX. Si se proporciona un formato de archivo 3D diferente, el nodo generará un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `FBX` | El modelo 3D procesado, devuelto como un archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DPartNode/es.md)

---
**Source fingerprint (SHA-256):** `827b42559f4b2c341f08c58f53778d27c1c6afce607c36c8d1eae7c208c6a738`
