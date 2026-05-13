> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/es.md)

Este nodo está diseñado para operaciones de composición, específicamente para unir una imagen con su máscara alfa correspondiente y producir una única imagen de salida. Combina eficazmente el contenido visual con la información de transparencia, permitiendo la creación de imágenes donde ciertas áreas son transparentes o semitransparentes.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El contenido visual principal que se combinará con una máscara alfa. Representa la imagen sin información de transparencia. |
| `alpha`   | `MASK`      | La máscara alfa que define la transparencia de la imagen correspondiente. Se utiliza para determinar qué partes de la imagen deben ser transparentes o semitransparentes. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una única imagen que combina la imagen de entrada con la máscara alfa, incorporando información de transparencia en el contenido visual. |