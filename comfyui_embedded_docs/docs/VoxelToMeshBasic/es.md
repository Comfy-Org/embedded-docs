> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/es.md)

El nodo VoxelToMeshBasic convierte datos de vóxeles 3D en geometría de malla. Procesa volúmenes de vóxeles aplicando un valor de umbral para determinar qué partes del volumen se convierten en superficies sólidas en la malla resultante. El nodo genera una estructura de malla completa con vértices y caras que puede utilizarse para renderizado y modelado 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `voxel` | VOXEL | Sí | - | Los datos de vóxeles 3D a convertir en una malla |
| `umbral` | FLOAT | Sí | -1.0 a 1.0 | El valor de umbral utilizado para determinar qué vóxeles forman parte de la superficie de la malla (valor por defecto: 0.6) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MESH` | MESH | La malla 3D generada que contiene vértices y caras |
