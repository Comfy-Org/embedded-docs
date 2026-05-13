> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/es.md)

El nodo `PairConditioningSetPropertiesAndCombine` modifica y combina pares de condicionamiento aplicando nuevos datos de condicionamiento a las entradas de condicionamiento positivo y negativo existentes. Permite ajustar la intensidad del condicionamiento aplicado y controlar cómo se establece el área de condicionamiento. Este nodo es particularmente útil en flujos de trabajo avanzados de manipulación de condicionamiento donde se necesita fusionar múltiples fuentes de condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo original |
| `negativo` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo original |
| `positivo_NUEVO` | CONDITIONING | Sí | - | El nuevo condicionamiento positivo a aplicar |
| `negativo_NUEVO` | CONDITIONING | Sí | - | El nuevo condicionamiento negativo a aplicar |
| `fuerza` | FLOAT | Sí | 0.0 a 10.0 | Factor de intensidad para aplicar el nuevo condicionamiento (predeterminado: 1.0) |
| `set_area_cond` | STRING | Sí | "default"<br>"mask bounds" | Controla cómo se aplica el área de condicionamiento (predeterminado: "default") |
| `máscara` | MASK | No | - | Máscara opcional para restringir el área de aplicación del condicionamiento |
| `ganchos` | HOOKS | No | - | Grupo de hooks opcional para control avanzado |
| `pasos_de_tiempo` | TIMESTEPS_RANGE | No | - | Especificación opcional de rango de pasos de tiempo |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | La salida de condicionamiento positivo combinado |
| `negativo` | CONDITIONING | La salida de condicionamiento negativo combinado |

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
