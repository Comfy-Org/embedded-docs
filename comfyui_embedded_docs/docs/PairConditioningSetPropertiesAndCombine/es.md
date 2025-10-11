> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/es.md)

El nodo PairConditioningSetPropertiesAndCombine modifica y combina pares de condicionamiento aplicando nuevos datos de condicionamiento a entradas existentes de condicionamiento positivo y negativo. Permite ajustar la fuerza del condicionamiento aplicado y controlar cómo se establece el área de condicionamiento. Este nodo es particularmente útil para flujos de trabajo avanzados de manipulación de condicionamiento donde se necesita mezclar múltiples fuentes de condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | La entrada original de condicionamiento positivo |
| `negative` | CONDITIONING | Sí | - | La entrada original de condicionamiento negativo |
| `positive_NEW` | CONDITIONING | Sí | - | El nuevo condicionamiento positivo a aplicar |
| `negative_NEW` | CONDITIONING | Sí | - | El nuevo condicionamiento negativo a aplicar |
| `strength` | FLOAT | Sí | 0.0 a 10.0 | El factor de fuerza para aplicar el nuevo condicionamiento (valor por defecto: 1.0) |
| `set_cond_area` | STRING | Sí | "default"<br>"mask bounds" | Controla cómo se aplica el área de condicionamiento |
| `mask` | MASK | No | - | Máscara opcional para restringir el área de aplicación del condicionamiento |
| `hooks` | HOOKS | No | - | Grupo de hooks opcional para control avanzado |
| `timesteps` | TIMESTEPS_RANGE | No | - | Especificación opcional del rango de pasos de tiempo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | La salida combinada de condicionamiento positivo |
| `negative` | CONDITIONING | La salida combinada de condicionamiento negativo |