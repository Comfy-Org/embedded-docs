El nodo WanMoveVisualizeTracks superpone datos de seguimiento de movimiento sobre una secuencia de imágenes o fotogramas de video. Dibuja representaciones visuales de los puntos rastreados, incluyendo sus trayectorias de movimiento y posiciones actuales, haciendo que los datos de movimiento sean visibles y más fáciles de analizar.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | La secuencia de imágenes de entrada o fotogramas de video sobre los cuales visualizar las trayectorias. | IMAGE | Sí | - |
| `pistas` | Los datos de seguimiento de movimiento que contienen las trayectorias de los puntos e información de visibilidad. Si no se proporcionan, las imágenes de entrada se pasan sin cambios. | TRACKS | No | - |
| `resolución_de_línea` | El número de fotogramas anteriores a utilizar al dibujar la línea de trayectoria posterior para cada seguimiento (predeterminado: 24). | INT | Sí | 1 - 1024 |
| `tamaño_círculo` | El tamaño del círculo dibujado en la posición actual de cada seguimiento (predeterminado: 12). | INT | Sí | 1 - 128 |
| `opacidad` | La opacidad de las superposiciones de seguimiento dibujadas (predeterminado: 0.75). | FLOAT | Sí | 0.0 - 1.0 |
| `ancho_de_línea` | El ancho de las líneas utilizadas para dibujar las trayectorias de seguimiento (predeterminado: 16). | INT | Sí | 1 - 128 |

**Nota:** Si el número de imágenes de entrada no coincide con el número de fotogramas en los datos de `tracks` proporcionados, la secuencia de imágenes se repetirá para igualar la longitud de las trayectorias.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La secuencia de imágenes con los datos de seguimiento de movimiento visualizados como superposiciones. Si no se proporcionaron `pistas`, se devuelven las imágenes de entrada originales. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/es.md)

---
**Source fingerprint (SHA-256):** `b32169a8c9d3a2dd74463c81f6bd7d9a4bc66486af156843f32b0874f0eaeb8f`
