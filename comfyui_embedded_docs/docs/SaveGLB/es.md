> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/es.md)

El nodo SaveGLB guarda datos de malla 3D o archivos 3D en el directorio de salida. Acepta datos de malla o varios formatos de archivo 3D (GLB, GLTF, OBJ, FBX, STL, USDZ) y los exporta con un prefijo de nombre de archivo especificado. Al guardar datos de malla, puede manejar múltiples mallas y agrega automáticamente metadatos del flujo de trabajo a los archivos cuando los metadatos están habilitados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `malla` | MESH o FILE3D | Sí | - | Malla o archivo 3D a guardar. Acepta datos de malla o formatos de archivo 3D, incluyendo GLB, GLTF, OBJ, FBX, STL y USDZ |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el nombre del archivo de salida (predeterminado: "3d/ComfyUI") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `ui` | UI | Muestra los archivos 3D guardados en la interfaz de usuario con información de nombre de archivo, subcarpeta y tipo |

---
**Source fingerprint (SHA-256):** `bd36600185aeb793cd4e9f37f3b4464267cb36f451fdcf71aff83077bb8c3f53`
