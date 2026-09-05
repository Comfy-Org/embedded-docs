# TripoSegmentNode

Este nodo divide un modelo 3D en partes individuales. Envía el modelo al servicio de segmentación de Tripo, espera a que el trabajo finalice y devuelve el modelo segmentado en formato GLB con una lista de nombres de partes separados por comas. Estos nombres de partes alimentan pasos posteriores, como Tripo: Complete Mesh Parts, Tripo: Retopology y Tripo: Convert model.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_task_id` | El ID de tarea del modelo 3D que se segmentará en partes. | MODEL_TASK_ID | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_file` | Nombre del archivo de salida del modelo GLB segmentado. Se mantiene solo por compatibilidad hacia atrás. | STRING |
| `segment task_id` | El ID de tarea del trabajo de segmentación que produjo el resultado. | SEGMENT_TASK_ID |
| `GLB` | El modelo 3D segmentado, como archivo GLB. | GLB |
| `part_names` | Nombres de las partes separados por comas. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/es.md)

---
**Source fingerprint (SHA-256):** `d27580a7f2118e76cecff5e1d682c7605f966bf657d7a02b2d2ddf764d9b72d0`
