# Meshy: Riggear Modelo

El nodo Meshy: Rig Model toma un modelo 3D de una tarea Meshy anterior y crea automáticamente un esqueleto para él, produciendo un personaje con rig que puede ser posado y animado. El nodo genera el modelo con rig en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `meshy_task_id` | El ID de tarea único de una operación Meshy anterior (p. ej., texto a 3D o imagen a 3D) que generó el modelo al que se aplicará el rig. | STRING | Sí | N/A |
| `altura_metros` | La altura aproximada del modelo de personaje en metros. Esto ayuda a la precisión del escalado y del rig (predeterminado: 1.7). | FLOAT | Sí | 0.1 a 15.0 |
| `imagen_de_textura` | La imagen de textura de color base del modelo con UV desplegados. | IMAGE | No | N/A |

**Nota:** El proceso de rigging automático actualmente no es adecuado para mallas sin textura, recursos no humanoides o recursos humanoides con una estructura de extremidades y cuerpo poco clara.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | Una salida heredada para compatibilidad hacia atrás, que contiene el nombre de archivo del modelo GLB. | STRING |
| `rig_task_id` | El ID de tarea único para esta operación de rigging, que se puede usar para hacer referencia al resultado. | STRING |
| `GLB` | El modelo de personaje 3D con rig guardado en el formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo de personaje 3D con rig guardado en el formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/es.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
