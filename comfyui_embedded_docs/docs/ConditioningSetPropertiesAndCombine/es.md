> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/es.md)

El nodo ConditioningSetPropertiesAndCombine modifica los datos de condicionamiento aplicando propiedades de una nueva entrada de condicionamiento a una entrada de condicionamiento existente. Combina los dos conjuntos de condicionamiento mientras controla la fuerza del nuevo condicionamiento y especifica cómo debe aplicarse el área de condicionamiento.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `cond` | CONDITIONING | Requerido | - | - | Los datos de condicionamiento originales que se modificarán |
| `cond_NEW` | CONDITIONING | Requerido | - | - | Los nuevos datos de condicionamiento que proporcionan las propiedades a aplicar |
| `fuerza` | FLOAT | Requerido | 1.0 | 0.0 - 10.0 | Controla la intensidad de las nuevas propiedades de condicionamiento |
| `establecer_area_cond` | STRING | Requerido | default | ["default", "mask bounds"] | Determina cómo se aplica el área de condicionamiento |
| `máscara` | MASK | Opcional | - | - | Máscara opcional para definir áreas específicas para el condicionamiento |
| `ganchos` | HOOKS | Opcional | - | - | Funciones de hook opcionales para procesamiento personalizado |
| `pasos_de_tiempo` | TIMESTEPS_RANGE | Opcional | - | - | Rango de pasos de tiempo opcional para controlar cuándo se aplica el condicionamiento |

**Nota:** Cuando se proporciona `mask`, el parámetro `set_cond_area` puede usar "mask bounds" para restringir la aplicación del condicionamiento a las regiones enmascaradas.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento combinados con propiedades modificadas |