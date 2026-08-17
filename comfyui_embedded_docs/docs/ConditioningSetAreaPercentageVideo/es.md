# AcondicionamientoEstablecerAreaPorcentajeVideo

El nodo ConditioningSetAreaPercentageVideo modifica los datos de acondicionamiento al definir un área específica y una región temporal para la generación de video. Permite establecer la posición, el tamaño y la duración del área donde se aplicará el acondicionamiento utilizando valores porcentuales relativos a las dimensiones generales. Esto es útil para enfocar la generación en partes específicas de una secuencia de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `conditioning` | Los datos de acondicionamiento que se modificarán | CONDITIONING | Sí | - |
| `width` | El ancho del área como porcentaje del ancho total (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `height` | El alto del área como porcentaje del alto total (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `temporal` | La duración temporal del área como porcentaje de la longitud total del video (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x` | La posición inicial horizontal del área como porcentaje (predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `y` | La posición inicial vertical del área como porcentaje (predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `z` | La posición inicial temporal del área como porcentaje de la línea de tiempo del video (predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |
| `strength` | El multiplicador de fuerza aplicado al acondicionamiento dentro del área definida (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 10.0 |

Nota: Todos los valores de tamaño y posición son porcentajes normalizados (0.0 a 1.0) relativos a las dimensiones generales del video y su línea de tiempo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `conditioning` | Los datos de acondicionamiento modificados con el área y los ajustes de fuerza especificados aplicados | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/es.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
