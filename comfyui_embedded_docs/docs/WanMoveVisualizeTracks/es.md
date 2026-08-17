# WanMoveVisualizeTracks

```markdown
El nodo WanMoveVisualizeTracks dibuja datos de seguimiento de movimiento sobre una secuencia de imágenes o fotogramas de video. Coloca un círculo en la posición actual de cada punto rastreado y dibuja una línea de trayectoria desvaneciente que muestra hacia dónde se ha movido el punto en los fotogramas recientes. Si no se proporcionan datos de seguimiento, las imágenes de entrada se devuelven sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | La secuencia de imágenes de entrada o fotogramas de video sobre la que se visualizarán los seguimientos. | IMAGE | Sí | - |
| `tracks` | Los datos de seguimiento de movimiento que contienen las posiciones de los puntos e información de visibilidad. Si no se proporcionan, las imágenes de entrada pasan sin cambios. | TRACKS | No | - |
| `line_resolution` | El número de fotogramas anteriores a utilizar al dibujar la línea de trayectoria para cada seguimiento (por defecto: 24). | INT | Sí | 1 - 1024 |
| `circle_size` | El tamaño del círculo dibujado en la posición actual de cada punto rastreado (por defecto: 12). | INT | Sí | 1 - 128 |
| `opacity` | La opacidad de las superposiciones de seguimiento dibujadas (por defecto: 0.75). | FLOAT | Sí | 0.0 - 1.0 |
| `line_width` | El ancho de las líneas utilizadas para dibujar las trayectorias de seguimiento (por defecto: 16). | INT | Sí | 1 - 128 |

**Nota:** Si el número de imágenes de entrada no coincide con el número de fotogramas de los datos `tracks` proporcionados, la secuencia de imágenes de entrada se repite para alinearse con los datos de seguimiento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | La secuencia de imágenes con los datos de seguimiento de movimiento dibujados como superposiciones. Si no se proporcionaron `tracks`, las imágenes de entrada originales se devuelven sin cambios. | IMAGE |
```

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/es.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
