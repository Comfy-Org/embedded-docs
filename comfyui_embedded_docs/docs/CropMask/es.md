> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/es.md)

El nodo CropMask está diseñado para recortar un área específica de una máscara determinada. Permite a los usuarios definir la región de interés especificando coordenadas y dimensiones, extrayendo eficazmente una porción de la máscara para su posterior procesamiento o análisis.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `máscara`    | MASK        | La entrada de máscara representa la imagen de máscara que se va a recortar. Es esencial para definir el área a extraer según las coordenadas y dimensiones especificadas. |
| `x`       | INT         | La coordenada x especifica el punto de inicio en el eje horizontal desde el cual debe comenzar el recorte. |
| `y`       | INT         | La coordenada y determina el punto de inicio en el eje vertical para la operación de recorte. |
| `ancho`   | INT         | El ancho define la extensión horizontal del área de recorte desde el punto de inicio. |
| `altura`  | INT         | La altura especifica la extensión vertical del área de recorte desde el punto de inicio. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `máscara`    | MASK        | La salida es una máscara recortada, que es una porción de la máscara original definida por las coordenadas y dimensiones especificadas. |