> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningZeroOut/es.md)

Este nodo pone a cero elementos específicos dentro de la estructura de datos de condicionamiento, neutralizando efectivamente su influencia en pasos posteriores del procesamiento. Está diseñado para operaciones avanzadas de condicionamiento donde se requiere la manipulación directa de la representación interna del condicionamiento.

## Entradas

| Parámetro | Tipo Comfy                | Descripción |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | La estructura de datos de condicionamiento que se modificará. Este nodo pone a cero los elementos 'pooled_output' dentro de cada entrada de condicionamiento, si están presentes. |

## Salidas

| Parámetro | Tipo Comfy                | Descripción |
|-----------|----------------------------|-------------|
| `CONDITIONING` | CONDITIONING | La estructura de datos de condicionamiento modificada, con los elementos 'pooled_output' establecidos en cero cuando corresponda. |