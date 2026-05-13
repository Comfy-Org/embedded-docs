> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageInvert/es.md)

El nodo `ImageInvert` está diseñado para invertir los colores de una imagen, transformando efectivamente el valor de color de cada píxel a su color complementario en el círculo cromático. Esta operación es útil para crear imágenes en negativo o para efectos visuales que requieran inversión de color.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El parámetro `image` representa la imagen de entrada que se va a invertir. Es fundamental para especificar la imagen objetivo cuyos colores se invertirán, afectando la ejecución del nodo y el resultado visual del proceso de inversión. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una versión invertida de la imagen de entrada, donde el valor de color de cada píxel se transforma a su color complementario. |