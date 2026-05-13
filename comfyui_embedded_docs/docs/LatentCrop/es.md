> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/es.md)

El nodo LatentCrop está diseñado para realizar operaciones de recorte en representaciones latentes de imágenes. Permite especificar las dimensiones y la posición del recorte, posibilitando modificaciones dirigidas en el espacio latente.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `muestras` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes que se recortarán. Es fundamental para definir los datos sobre los cuales se realizará la operación de recorte. |
| `ancho`   | `INT`       | Especifica el ancho del área de recorte. Influye directamente en las dimensiones de la representación latente de salida. |
| `altura`  | `INT`       | Especifica la altura del área de recorte, afectando el tamaño de la representación latente recortada resultante. |
| `x`       | `INT`       | Determina la coordenada x inicial del área de recorte, influyendo en la posición del recorte dentro de la representación latente original. |
| `y`       | `INT`       | Determina la coordenada y inicial del área de recorte, estableciendo la posición del recorte dentro de la representación latente original. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una representación latente modificada con el recorte especificado aplicado. |