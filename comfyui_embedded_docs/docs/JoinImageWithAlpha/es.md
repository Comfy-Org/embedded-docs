Este nodo está diseñado para operaciones de composición, específicamente para unir una imagen con su máscara alfa correspondiente para producir una sola imagen de salida. Combina eficazmente el contenido visual con la información de transparencia, permitiendo la creación de imágenes donde ciertas áreas son transparentes o semitransparentes.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | El contenido visual principal que se combinará con una máscara alfa. Representa la imagen sin información de transparencia. |
| `alpha`   | `MASK`      | La máscara alfa que define la transparencia de la imagen correspondiente. Se utiliza para determinar qué partes de la imagen deben ser transparentes o semitransparentes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | La salida es una sola imagen que combina la imagen de entrada con la máscara alfa, incorporando información de transparencia en el contenido visual. |
