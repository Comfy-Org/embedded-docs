> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/es.md)

El nodo `ConditioningSetAreaPercentage` está especializado en ajustar el área de influencia de los elementos de condicionamiento basándose en valores porcentuales. Permite especificar las dimensiones y la posición del área como porcentajes del tamaño total de la imagen, junto con un parámetro de intensidad para modular la potencia del efecto de condicionamiento.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Representa los elementos de condicionamiento que se modificarán, sirviendo como base para aplicar ajustes de área e intensidad. |
| `width`   | `FLOAT`     | Especifica el ancho del área como un porcentaje del ancho total de la imagen, influyendo en la extensión horizontal del condicionamiento sobre la imagen. |
| `height`  | `FLOAT`     | Determina la altura del área como un porcentaje de la altura total de la imagen, afectando la extensión vertical de la influencia del condicionamiento. |
| `x`       | `FLOAT`     | Indica el punto de inicio horizontal del área como un porcentaje del ancho total de la imagen, posicionando el efecto de condicionamiento. |
| `y`       | `FLOAT`     | Especifica el punto de inicio vertical del área como un porcentaje de la altura total de la imagen, posicionando el efecto de condicionamiento. |
| `strength`| `FLOAT`     | Controla la intensidad del efecto de condicionamiento dentro del área especificada, permitiendo un ajuste preciso de su impacto. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Devuelve los elementos de condicionamiento modificados con los parámetros de área e intensidad actualizados, listos para su posterior procesamiento o aplicación. |