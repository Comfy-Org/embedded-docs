El nodo `ConditioningSetAreaPercentageVideo` modifica los datos de condicionamiento definiendo un área específica y una región temporal para la generación de video. Permite establecer la posición, el tamaño y la duración del área donde se aplicará el condicionamiento, utilizando valores porcentuales relativos a las dimensiones generales. Esto es útil para enfocar la generación en partes específicas de una secuencia de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango |
| --- | --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento a modificar | CONDITIONING | Requerido | - | - |
| `ancho` | El ancho del área como porcentaje del ancho total | FLOAT | Requerido | 1.0 | 0.0 - 1.0 |
| `alto` | La altura del área como porcentaje de la altura total | FLOAT | Requerido | 1.0 | 0.0 - 1.0 |
| `temporal` | La duración temporal del área como porcentaje de la duración total del video | FLOAT | Requerido | 1.0 | 0.0 - 1.0 |
| `x` | La posición horizontal inicial del área como porcentaje | FLOAT | Requerido | 0.0 | 0.0 - 1.0 |
| `y` | La posición vertical inicial del área como porcentaje | FLOAT | Requerido | 0.0 | 0.0 - 1.0 |
| `z` | La posición temporal inicial del área como porcentaje de la línea de tiempo del video | FLOAT | Requerido | 0.0 | 0.0 - 1.0 |
| `fuerza` | El multiplicador de intensidad aplicado al condicionamiento dentro del área definida | FLOAT | Requerido | 1.0 | 0.0 - 10.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento modificados con el área y la configuración de intensidad especificadas aplicadas | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/es.md)

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
