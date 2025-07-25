El nodo EmptyImage se utiliza para crear imágenes en blanco con dimensiones y colores especificados. Puede generar imágenes de fondo de color sólido, comúnmente utilizadas como puntos de partida o imágenes de fondo para flujos de trabajo de procesamiento de imágenes.


## Entradas

| Nombre del Parámetro | Tipo de Datos | Descripción |
|---------------------|---------------|-------------|
| `ancho` | INT | Establece el ancho de la imagen generada (en píxeles), determinando las dimensiones horizontales del lienzo |
| `altura` | INT | Establece la altura de la imagen generada (en píxeles), determinando las dimensiones verticales del lienzo |
| `tamaño_del_lote` | INT | El número de imágenes a generar a la vez, utilizado para la creación en lote de imágenes con las mismas especificaciones |
| `color` | INT | El color de fondo de la imagen. Puedes ingresar configuraciones de color hexadecimal, que se convertirán automáticamente a decimal |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | El tensor de imagen en blanco generado, formateado como [tamaño_del_lote, altura, ancho, 3], que contiene tres canales de color RGB |

## Valores de Referencia de Colores Comunes

Dado que la entrada de color actual para este nodo no es amigable para el usuario, con todos los valores de color siendo convertidos a decimal, aquí hay algunos valores de color comunes que se pueden usar directamente para aplicación rápida.

| Nombre del Color | Valor Hexadecimal |
|------------------|-------------------|
| Negro            | 0x000000         |
| Blanco           | 0xFFFFFF         |
| Rojo             | 0xFF0000         |
| Verde            | 0x00FF00         |
| Azul             | 0x0000FF         |
| Amarillo         | 0xFFFF00         |
| Cian             | 0x00FFFF         |
| Magenta          | 0xFF00FF         |
| Naranja          | 0xFF8000         |
| Púrpura          | 0x8000FF         |
| Rosa             | 0xFF80C0         |
| Marrón           | 0x8B4513         |
| Gris Oscuro      | 0x404040         |
| Gris Claro       | 0xC0C0C0         |
| Azul Marino      | 0x000080         |
| Verde Oscuro     | 0x008000         |
| Rojo Oscuro      | 0x800000         |
| Dorado           | 0xFFD700         |
| Plateado         | 0xC0C0C0         |
| Beige            | 0xF5F5DC         |
