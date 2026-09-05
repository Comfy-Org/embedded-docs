# TripoMeshCompleteNode

Completa las partes faltantes o incompletas de un modelo 3D ya segmentado y repara las regiones dañadas de la malla. Toma el ID de tarea de un resultado de segmentación de malla de Tripo y solicita a Tripo que complete el modelo, y luego espera a que finalice el trabajo. Las partes completadas se devuelven como un archivo GLB, y opcionalmente puedes limitar el trabajo a nombres de partes específicos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `segment_task_id` | ID de tarea de una tarea de segmentación de malla de Tripo. Se completan las partes del modelo segmentado de esta tarea. Conecta la salida SEGMENT_TASK_ID de un nodo anterior de segmentación de malla de Tripo. | SEGMENT_TASK_ID | Sí | ID de tarea única |
| `part_names` | Nombres de partes separados por comas para completar. Vacío completa todas las partes. Valor por defecto: cadena vacía. Los espacios alrededor de los nombres se eliminan y los nombres duplicados se ignoran. | STRING | No | Texto libre o vacío |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | Nombre del archivo del modelo completado. Esta salida existe solo para compatibilidad con versiones anteriores. | STRING |
| `task_id de modelo` | ID de tarea de la tarea de completado de malla de Tripo finalizada. Puede utilizarse como entrada de otros nodos de Tripo que esperan un ID de tarea de modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D completado con las partes reparadas, descargado como archivo GLB. | GLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/es.md)

---
**Source fingerprint (SHA-256):** `aa7173f25f54d9fca9605e246a93fe319cf46c07d8d3aacc214a24a60c92e611`
