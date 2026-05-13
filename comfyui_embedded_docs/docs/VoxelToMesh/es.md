> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/es.md)

El nodo VoxelToMeshBasic convierte datos de vóxeles 3D en una geometría de malla extrayendo una superficie en un valor de umbral especificado. Procesa cada cuadrícula de vóxeles en la entrada y genera vértices y caras que forman una representación de malla 3D.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `voxel` | VOXEL | Sí | - | Datos de vóxeles de entrada para convertir en geometría de malla |
| `umbral` | FLOAT | Sí | -1.0 a 1.0 | Valor de umbral para la extracción de superficie (predeterminado: 0.6) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MESH` | MESH | Malla 3D generada que contiene vértices y caras apilados de todas las cuadrículas de vóxeles de entrada |

---
**Source fingerprint (SHA-256):** `36df962c84c99a83f243a59b6387874e42e7d05323bd84079dbab112d2f1b67c`
