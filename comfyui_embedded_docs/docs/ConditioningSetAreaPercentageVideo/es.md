> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/es.md)

El nodo ConditioningSetAreaPercentageVideo modifica los datos de condicionamiento definiendo un área específica y una región temporal para la generación de video. Permite establecer la posición, tamaño y duración del área donde se aplicará el condicionamiento utilizando valores porcentuales relativos a las dimensiones generales. Esto es útil para enfocar la generación en partes específicas de una secuencia de video.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `conditioning` | CONDITIONING | Requerido | - | - | Los datos de condicionamiento que serán modificados |
| `width` | FLOAT | Requerido | 1.0 | 0.0 - 1.0 | El ancho del área como porcentaje del ancho total |
| `height` | FLOAT | Requerido | 1.0 | 0.0 - 1.0 | La altura del área como porcentaje de la altura total |
| `temporal` | FLOAT | Requerido | 1.0 | 0.0 - 1.0 | La duración temporal del área como porcentaje de la longitud total del video |
| `x` | FLOAT | Requerido | 0.0 | 0.0 - 1.0 | La posición horizontal inicial del área como porcentaje |
| `y` | FLOAT | Requerido | 0.0 | 0.0 - 1.0 | La posición vertical inicial del área como porcentaje |
| `z` | FLOAT | Requerido | 0.0 | 0.0 - 1.0 | La posición temporal inicial del área como porcentaje de la línea de tiempo del video |
| `strength` | FLOAT | Requerido | 1.0 | 0.0 - 10.0 | El multiplicador de fuerza aplicado al condicionamiento dentro del área definida |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Los datos de condicionamiento modificados con la configuración de área y fuerza especificada aplicada |