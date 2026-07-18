El nodo Meshy: Rig Model toma un modelo 3D de una tarea previa de Meshy y crea automáticamente un esqueleto para él, produciendo un personaje riggeado que puede ser posado y animado. El nodo genera el modelo riggeado en formatos de archivo GLB y FBX.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `meshy_task_id` | El ID único de tarea de una operación previa de Meshy (ej., texto a 3D o imagen a 3D) que generó el modelo a riggear. | STRING | Sí | N/A |
| `altura_metros` | La altura aproximada del modelo del personaje en metros. Esto ayuda a la precisión del escalado y riggeado (valor predeterminado: 1.7). | FLOAT | Sí | 0.1 a 15.0 |
| `imagen_de_textura` | La imagen de textura de color base del modelo con mapeado UV. | IMAGE | No | N/A |

**Nota:** El proceso de riggeado automático actualmente no es adecuado para mallas sin textura, activos no humanoides o activos humanoides con estructura corporal y de extremidades poco clara.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model_file` | Una salida heredada para compatibilidad hacia atrás, que contiene el nombre del archivo del modelo GLB. | STRING |
| `rig_task_id` | El ID único de tarea para esta operación de riggeado, que puede usarse para hacer referencia al resultado. | STRING |
| `GLB` | El modelo de personaje 3D riggeado guardado en formato de archivo GLB. | FILE3DGLB |
| `FBX` | El modelo de personaje 3D riggeado guardado en formato de archivo FBX. | FILE3DFBX |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/es.md)

---
**Source fingerprint (SHA-256):** `91e06e3465d3d309d2267ae307ec5a704af3903b7a6d7fb6011217dd58a63973`
