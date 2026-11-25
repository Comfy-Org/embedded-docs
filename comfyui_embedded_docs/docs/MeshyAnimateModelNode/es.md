# Meshy: Animar Modelo

Este nodo aplica una acción de animación específica a un personaje 3D previamente riggeado mediante el servicio Meshy. Toma un ID de tarea de una operación de rigging anterior y un ID de acción para seleccionar la animación deseada de la biblioteca, y luego devuelve el modelo animado tanto en formato de archivo GLB como FBX.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `id_de_tarea_de_rig` | El ID de tarea único de una operación de rigging de personaje de Meshy completada previamente. | MESHY_RIGGED_TASK_ID, STRING | Sí | N/A |
| `id_de_acción` | El número de ID de la acción de animación que se aplicará. Visite https://docs.meshy.ai/en/api/animation-library para obtener una lista de los valores disponibles. (predeterminado: 0) | INT | Sí | 0 a 696 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | Un identificador de cadena para el modelo animado. Esta salida se proporciona únicamente por compatibilidad con versiones anteriores. | STRING |
| `GLB` | El archivo de modelo 3D animado en formato GLB. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D animado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/es.md)

---
**Source fingerprint (SHA-256):** `d2fe5e62d8261880fe55cf305bc8bac4cb85367914d9ddfe2308ad1b43c85a16`
