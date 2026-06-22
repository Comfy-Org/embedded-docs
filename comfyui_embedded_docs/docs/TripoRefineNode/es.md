# Tripo: Refinar modelo borrador

El nodo TripoRefineNode refina modelos 3D preliminares creados específicamente por modelos Tripo v1.4. Toma un ID de tarea de modelo y lo procesa a través de la API de Tripo para generar una versión mejorada del modelo. Este nodo está diseñado para funcionar exclusivamente con modelos preliminares producidos por modelos Tripo v1.4.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ID_de_tarea_del_modelo` | Debe ser un modelo Tripo v1.4 | MODEL_TASK_ID | Sí | - |

**Nota:** Este nodo solo acepta modelos preliminares creados por modelos Tripo v1.4. El uso de modelos de otras versiones puede provocar errores.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_de_tarea_de_modelo` | La ruta de archivo o referencia al modelo refinado (solo para compatibilidad hacia atrás) | STRING |
| `GLB` | El identificador de tarea para la operación del modelo refinado | MODEL_TASK_ID |
| `GLB` | El modelo 3D refinado en formato GLB | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/es.md)

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
