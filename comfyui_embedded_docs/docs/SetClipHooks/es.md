> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/es.md)

El nodo `SetClipHooks` permite aplicar hooks personalizados a un modelo CLIP, posibilitando modificaciones avanzadas en su comportamiento. Puede aplicar hooks a las salidas de condicionamiento y habilitar opcionalmente la funcionalidad de programación de CLIP. Este nodo crea una copia clonada del modelo CLIP de entrada con las configuraciones de hooks especificadas aplicadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP al que se le aplicarán los hooks |
| `apply_to_conds` | BOOLEAN | Sí | - | Si se aplican hooks a las salidas de condicionamiento (predeterminado: True) |
| `schedule_clip` | BOOLEAN | Sí | - | Si se habilita la programación de CLIP (predeterminado: False) |
| `hooks` | HOOKS | No | - | Grupo de hooks opcional para aplicar al modelo CLIP |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `clip` | CLIP | Un modelo CLIP clonado con los hooks especificados aplicados |

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`
