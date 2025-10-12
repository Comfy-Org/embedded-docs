> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultAndCombine/es.md)

El nodo PairConditioningSetDefaultAndCombine establece valores de condicionamiento predeterminados y los combina con datos de condicionamiento de entrada. Toma entradas de condicionamiento positivo y negativo junto con sus contrapartes predeterminadas, luego las procesa a través del sistema de hooks de ComfyUI para producir salidas de condicionamiento finales que incorporan los valores predeterminados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada principal de condicionamiento positivo a procesar |
| `negative` | CONDITIONING | Sí | - | La entrada principal de condicionamiento negativo a procesar |
| `positive_DEFAULT` | CONDITIONING | Sí | - | Los valores predeterminados de condicionamiento positivo a usar como respaldo |
| `negative_DEFAULT` | CONDITIONING | Sí | - | Los valores predeterminados de condicionamiento negativo a usar como respaldo |
| `hooks` | HOOKS | No | - | Grupo de hooks opcional para lógica de procesamiento personalizada |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | El condicionamiento positivo procesado con valores predeterminados incorporados |
| `negative` | CONDITIONING | El condicionamiento negativo procesado con valores predeterminados incorporados |
