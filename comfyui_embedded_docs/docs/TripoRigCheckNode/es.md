# TripoRigCheckNode

Este nodo envía el ID de una tarea de modelo 3D de Tripo completada a la API de Tripo y comprueba si a ese modelo se le puede aplicar rigging. Espera a que finalice la comprobación y, a continuación, devuelve un resultado de sí/no junto con el tipo de esqueleto que Tripo recomienda para el modelo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model_task_id` | El ID de la tarea de Tripo del modelo a analizar. Identifica un modelo que fue previamente generado, importado o creado de otra manera mediante una tarea de Tripo. | STRING | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `riggable` | Si el modelo puede recibir rigging. | BOOLEAN |
| `rig_type` | Esqueleto recomendado: biped, quadruped, hexapod, octopod, avian, serpentine o aquatic; 'others' cuando el modelo no puede recibir rigging. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/es.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
