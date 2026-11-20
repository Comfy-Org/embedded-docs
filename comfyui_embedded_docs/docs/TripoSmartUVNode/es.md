# Tripo: Smart UV

Tripo: Smart UV re-desenvuelve las UV de un modelo y reasigna sus texturas, rig y animación al nuevo diseño. Úsalo cuando el diseño UV original de un modelo no sea utilizable, por ejemplo, después de una retopología o cuando sea necesario rehacer las costuras de textura. El modelo de entrada no debe superar los 80 000 triángulos (un cuadrilátero cuenta como dos), así que reduce los modelos más grandes con Tripo: Retopology o un `face_limit` primero.

> **Nota:** Tripo conserva los registros de tareas en sus servidores durante 7 días (vigente a partir del 1 de diciembre de 2026). Un ID de tarea más antiguo que ese ya no se puede resolver, por lo que volver a ejecutar un flujo de trabajo guardado después de ese período falla en este nodo. Vuelve a ejecutar el nodo Tripo anterior para crear un nuevo ID de tarea, o vuelve a importar el modelo descargado con **Tripo: Import Model**.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `model_task_id` | ID de tarea del modelo a re-desenvolver. Acepta un ID de tarea de modelo de un nodo de generación de Tripo, o un ID de tarea de rig, retarget o segmentación. | MODEL_TASK_ID | Sí | ID de tarea de Tripo |
| `bake` | Hornear las texturas existentes en el nuevo diseño UV. Desactivado omite el horneado y devuelve el modelo sin sus texturas de color (predeterminado: True). | BOOLEAN | Sí | `True`<br>`False` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model task_id` | ID de tarea de la tarea UV finalizada. Se puede pasar a otros nodos de Tripo, por ejemplo, Tripo: Texture. | MODEL_TASK_ID |
| `GLB` | El modelo re-desenvuelto en formato GLB. Vacío cuando el modelo de origen es FBX. | FILE_3D_GLB |
| `FBX` | El modelo re-desenvuelto en formato FBX. Solo se completa cuando el modelo de origen es FBX, por ejemplo, una malla de cuadriláteros. | FILE_3D_FBX |
| `UV atlas` | El diseño UV renderizado del modelo como una imagen. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartUVNode/es.md)

---
**Source fingerprint (SHA-256):** `55c9352c7c8129fa7a4f99f803bdc6db112830454e7d9566fa734063cb283532`
