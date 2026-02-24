> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/es.md)

El nodo WanMoveVisualizeTracks superpone datos de seguimiento de movimiento sobre una secuencia de imágenes o fotogramas de video. Dibuja representaciones visuales de los puntos rastreados, incluyendo sus trayectorias de movimiento y posiciones actuales, haciendo que los datos de movimiento sean visibles y más fáciles de analizar.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | - | La secuencia de imágenes de entrada o fotogramas de video sobre los que visualizar las trayectorias. |
| `tracks` | TRACKS | No | - | Los datos de seguimiento de movimiento que contienen las trayectorias de puntos e información de visibilidad. Si no se proporciona, las imágenes de entrada se pasan sin cambios. |
| `line_resolution` | INT | Sí | 1 - 1024 | El número de fotogramas anteriores a utilizar al dibujar la línea de trayectoria para cada seguimiento (valor por defecto: 24). |
| `circle_size` | INT | Sí | 1 - 128 | El tamaño del círculo dibujado en la posición actual de cada seguimiento (valor por defecto: 12). |
| `opacity` | FLOAT | Sí | 0.0 - 1.0 | La opacidad de las superposiciones de trayectorias dibujadas (valor por defecto: 0.75). |
| `line_width` | INT | Sí | 1 - 128 | El ancho de las líneas utilizadas para dibujar las trayectorias de seguimiento (valor por defecto: 16). |

**Nota:** Si el número de imágenes de entrada no coincide con el número de fotogramas en los datos de `tracks` proporcionados, la secuencia de imágenes se repetirá para igualar la longitud del seguimiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La secuencia de imágenes con los datos de seguimiento de movimiento visualizados como superposiciones. Si no se proporcionaron `tracks`, se devuelven las imágenes de entrada originales. |
