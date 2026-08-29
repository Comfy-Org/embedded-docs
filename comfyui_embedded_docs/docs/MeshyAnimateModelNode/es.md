# Meshy: Animar Modelo

Este nodo aplica una acción de animación específica a un personaje 3D previamente riggeado mediante el servicio Meshy. Toma un ID de tarea de una operación de rigging anterior y un ID de acción para seleccionar la animación deseada de la biblioteca, y luego devuelve el modelo animado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `rig_task_id` | El ID de tarea único de una operación de rigging de personaje de Meshy completada previamente. | STRING | Sí | N/A |
| `action_id` | El número de ID de la acción de animación que se va a aplicar. Visite https://docs.meshy.ai/en/api/animation-library para obtener una lista de valores disponibles. (valor predeterminado: 0) | INT | Sí | 0 a 696 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | Un identificador de cadena para el modelo animado. Esta salida se proporciona únicamente por compatibilidad con versiones anteriores. | STRING |
| `GLB` | El archivo de modelo 3D animado en formato GLB. | FILE3DGLB |
| `FBX` | El archivo de modelo 3D animado en formato FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/es.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
