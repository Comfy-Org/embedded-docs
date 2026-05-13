> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/es.md)

El nodo **PairConditioningSetProperties** permite modificar propiedades de pares de condicionamiento tanto positivos como negativos al mismo tiempo. Aplica ajustes de intensidad, configuraciones de área de condicionamiento y controles opcionales de máscara o temporización a ambas entradas de condicionamiento, devolviendo los datos de condicionamiento positivo y negativo modificados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `positivo_NUEVO` | CONDITIONING | Sí | - | La entrada de condicionamiento positivo a modificar |
| `negativo_NUEVO` | CONDITIONING | Sí | - | La entrada de condicionamiento negativo a modificar |
| `fuerza` | FLOAT | Sí | 0.0 a 10.0 | El multiplicador de intensidad aplicado al condicionamiento (predeterminado: 1.0) |
| `establecer_area_cond` | STRING | Sí | "default"<br>"mask bounds" | Determina cómo se calcula el área de condicionamiento (predeterminado: "default") |
| `mascara` | MASK | No | - | Máscara opcional para restringir el área de condicionamiento |
| `ganchos` | HOOKS | No | - | Grupo de ganchos opcional para modificaciones avanzadas de condicionamiento |
| `pasos_de_tiempo` | TIMESTEPS_RANGE | No | - | Rango de pasos de tiempo opcional para limitar cuándo se aplica el condicionamiento |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `negativo` | CONDITIONING | El condicionamiento positivo modificado con las propiedades aplicadas |
| `negative` | CONDITIONING | El condicionamiento negativo modificado con las propiedades aplicadas |

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
