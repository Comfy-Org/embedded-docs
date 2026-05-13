> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/es.md)

El nodo ConditioningSetProperties modifica las propiedades de los datos de condicionamiento ajustando la intensidad, la configuración del área y aplicando máscaras, ganchos o rangos de pasos de tiempo opcionales. Permite controlar cómo el condicionamiento influye en el proceso de generación estableciendo parámetros específicos que afectan la aplicación de los datos de condicionamiento durante la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `cond_NEW` | CONDITIONING | Requerido | - | - | Los datos de condicionamiento a modificar |
| `strength` | FLOAT | Requerido | 1.0 | 0.0 - 10.0 (paso: 0.01) | Controla la intensidad del efecto de condicionamiento |
| `set_cond_area` | STRING | Requerido | default | ["default", "mask bounds"] | Determina cómo se aplica el área de condicionamiento. Seleccione "default" para el comportamiento estándar o "mask bounds" para restringir al área de la máscara |
| `mask` | MASK | Opcional | - | - | Máscara opcional para restringir dónde se aplica el condicionamiento |
| `hooks` | HOOKS | Opcional | - | - | Funciones de gancho opcionales para procesamiento personalizado |
| `timesteps` | TIMESTEPS_RANGE | Opcional | - | - | Rango de pasos de tiempo opcional para limitar cuándo está activo el condicionamiento |

**Nota:** Cuando se proporciona una `mask`, el parámetro `set_cond_area` se puede establecer en "mask bounds" para restringir la aplicación del condicionamiento únicamente al área enmascarada. El parámetro `hooks` permite el procesamiento personalizado mediante funciones de gancho, y `timesteps` limita el efecto de condicionamiento a un rango específico de pasos de tiempo durante la generación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento modificados con propiedades actualizadas |

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
