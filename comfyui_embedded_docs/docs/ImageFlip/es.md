> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/es.md)

El nodo ImageFlip voltea imágenes a lo largo de diferentes ejes. Puede voltear imágenes verticalmente a lo largo del eje x u horizontalmente a lo largo del eje y. El nodo utiliza operaciones torch.flip para realizar el volteo según el método seleccionado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a voltear |
| `flip_method` | STRING | Sí | "x-axis: vertically"<br>"y-axis: horizontally" | La dirección de volteo a aplicar |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen de salida volteada |
