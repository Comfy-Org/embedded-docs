> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/es.md)

El nodo ConditioningSetProperties modifica las propiedades de los datos de condicionamiento ajustando la intensidad, configuraciones de área y aplicando máscaras opcionales o rangos de pasos temporales. Permite controlar cómo el condicionamiento influye en el proceso de generación estableciendo parámetros específicos que afectan la aplicación de los datos de condicionamiento durante la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `cond_NEW` | CONDITIONING | Requerido | - | - | Los datos de condicionamiento a modificar |
| `fuerza` | FLOAT | Requerido | 1.0 | 0.0-10.0 | Controla la intensidad del efecto de condicionamiento |
| `establecer_area_cond` | STRING | Requerido | default | ["default", "mask bounds"] | Determina cómo se aplica el área de condicionamiento |
| `máscara` | MASK | Opcional | - | - | Máscara opcional para restringir dónde se aplica el condicionamiento |
| `ganchos` | HOOKS | Opcional | - | - | Funciones de hook opcionales para procesamiento personalizado |
| `pasos_de_tiempo` | TIMESTEPS_RANGE | Opcional | - | - | Rango de pasos temporales opcional para limitar cuándo está activo el condicionamiento |

**Nota:** Cuando se proporciona una `mask`, el parámetro `set_cond_area` puede establecerse en "mask bounds" para restringir la aplicación del condicionamiento únicamente a la región enmascarada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados con propiedades actualizadas |