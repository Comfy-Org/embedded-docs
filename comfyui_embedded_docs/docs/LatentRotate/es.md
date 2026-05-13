> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/es.md)

El nodo LatentRotate está diseñado para rotar representaciones latentes de imágenes según ángulos específicos. Abstrae la complejidad de manipular el espacio latente para lograr efectos de rotación, permitiendo a los usuarios transformar fácilmente imágenes en el espacio latente de un modelo generativo.

## Entradas

| Parámetro  | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `muestras` | `LATENT`    | El parámetro 'samples' representa las representaciones latentes de las imágenes a rotar. Es crucial para determinar el punto de inicio de la operación de rotación. |
| `rotación` | COMBO[STRING] | El parámetro 'rotation' especifica el ángulo con el que deben rotarse las imágenes latentes. Influye directamente en la orientación de las imágenes resultantes. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es una versión modificada de las representaciones latentes de entrada, rotadas según el ángulo especificado. |