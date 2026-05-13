> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/es.md)

Este nodo combina una entrada de condicionamiento primaria con una entrada de condicionamiento predeterminada mediante un sistema basado en hooks. Fusiona las dos fuentes de condicionamiento en una única salida, permitiendo que el condicionamiento predeterminado sirva como respaldo o base cuando el condicionamiento primario está incompleto.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Predeterminado | Rango | Descripción |
|-----------|--------------|-----------------|----------------|-------|-------------|
| `cond` | CONDITIONING | Requerido | - | - | La entrada de condicionamiento primaria que se procesará y combinará |
| `cond_DEFAULT` | CONDITIONING | Requerido | - | - | Los datos de condicionamiento predeterminados que se combinarán con el condicionamiento primario |
| `hooks` | HOOKS | Opcional | - | - | Configuración opcional de hooks que controla cómo se procesan y combinan los datos de condicionamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento combinados resultantes de la fusión de las entradas de condicionamiento primaria y predeterminada |

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
