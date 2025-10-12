> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMesh/es.md)

El nodo VoxelToMesh convierte datos de vóxeles 3D en geometría de malla utilizando diferentes algoritmos. Procesa cuadrículas de vóxeles y genera vértices y caras que forman una representación de malla 3D. El nodo admite múltiples algoritmos de conversión y permite ajustar el valor de umbral para controlar la extracción de superficie.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Sí | - | Los datos de vóxeles de entrada para convertir en geometría de malla |
| `algoritmo` | COMBO | Sí | "surface net"<br>"basic" | El algoritmo utilizado para la conversión de malla a partir de datos de vóxeles |
| `umbral` | FLOAT | Sí | -1.0 a 1.0 | El valor de umbral para la extracción de superficie (valor por defecto: 0.6) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MESH` | MESH | La malla 3D generada que contiene vértices y caras |