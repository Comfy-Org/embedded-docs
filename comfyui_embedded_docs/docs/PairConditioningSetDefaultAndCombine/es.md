> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/es.md)

El nodo **PairConditioningSetDefaultAndCombine** establece valores de condicionamiento predeterminados y los combina con los datos de condicionamiento de entrada. Toma entradas de condicionamiento positivo y negativo junto con sus contrapartes predeterminadas, luego las procesa a través del sistema de hooks de ComfyUI para producir salidas de condicionamiento finales que incorporan los valores predeterminados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo principal a procesar |
| `negative` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo principal a procesar |
| `positive_DEFAULT` | CONDITIONING | Sí | - | Los valores de condicionamiento positivo predeterminados a utilizar como respaldo |
| `negative_DEFAULT` | CONDITIONING | Sí | - | Los valores de condicionamiento negativo predeterminados a utilizar como respaldo |
| `hooks` | HOOKS | No | - | Grupo opcional de hooks para lógica de procesamiento personalizada |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo procesado con valores predeterminados incorporados |
| `negative` | CONDITIONING | El condicionamiento negativo procesado con valores predeterminados incorporados |

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
