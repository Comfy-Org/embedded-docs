> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/es.md)

El nodo TripoRefineNode refina modelos 3D preliminares creados específicamente por modelos Tripo v1.4. Toma un ID de tarea de modelo y lo procesa a través de la API de Tripo para generar una versión mejorada del modelo. Este nodo está diseñado para funcionar exclusivamente con modelos preliminares producidos por modelos Tripo v1.4.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sí | - | Debe ser un modelo Tripo v1.4 |

**Nota:** Este nodo solo acepta modelos preliminares creados por modelos Tripo v1.4. El uso de modelos de otras versiones puede provocar errores.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model_file` | STRING | La ruta de archivo o referencia al modelo refinado (solo para compatibilidad hacia atrás) |
| `model task_id` | MODEL_TASK_ID | El identificador de tarea para la operación del modelo refinado |
| `GLB` | FILE3DGLB | El modelo 3D refinado en formato GLB |

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
