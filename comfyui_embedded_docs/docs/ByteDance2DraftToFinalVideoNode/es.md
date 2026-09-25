# ByteDance Seedance 2.5 Draft to Final Video

This node renders the 1080p final video of a Seedance 2.5 Draft. A draft is a fast 480p preview: in a Seedance 2.5 video node (text to video, first-last-frame to video, or reference to video), set `model` to `Seedance 2.5 Draft`, run it, and connect its `draft_task_id` output here. The final keeps the draft's scene and motion, and reuses the prompt, references, duration, aspect ratio, and audio setting that produced the draft.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `draft_task_id` | La salida `draft_task_id` de un nodo de Seedance 2.5 ejecutado con el modelo Seedance 2.5 Draft, o un ID de tarea de borrador pegado. Establece el control de semilla de ese nodo en fijo; de lo contrario, la siguiente ejecución generará un nuevo borrador en lugar de reutilizar el que revisaste. | STRING | Sí | - |
| `watermark` | Indica si se debe agregar una marca de agua al video. El valor predeterminado es False. Esta es una configuración avanzada. | BOOLEAN | No | True / False |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video` | El video final renderizado en 1080p, descargado del proveedor una vez que se completa la tarea de renderizado. | VIDEO |

**Nota:** Un borrador se puede renderizar durante 7 días después de su creación. El ID de tarea del borrador identifica al borrador por sí solo, por lo que el prompt, las referencias, la duración, la relación de aspecto y la configuración de audio no necesitan pasarse de nuevo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
