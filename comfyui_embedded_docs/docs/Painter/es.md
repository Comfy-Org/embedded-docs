> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/es.md)

El nodo Painter proporciona un lienzo interactivo para crear o editar imágenes y máscaras directamente dentro de ComfyUI. Permite comenzar con un lienzo en blanco o una imagen existente, pintar sobre ella utilizando una herramienta de pincel, y genera tanto la imagen resultante como una máscara alfa correspondiente. La máscara define las áreas pintadas, que luego se componen sobre la imagen base o el color de fondo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | No | - | Imagen base opcional sobre la que pintar. Si no se proporciona, se crea un lienzo en blanco utilizando el color de fondo, ancho y alto especificados. |
| `mask` | STRING | Sí | - | Los datos de pintura, típicamente generados por el widget interactivo integrado del nodo. Este parámetro es gestionado por la herramienta de pintura de la interfaz de usuario y no está destinado a conectarse a un socket estándar. |
| `width` | INT | Sí | 64 a 4096 | El ancho del lienzo en píxeles, utilizado cuando no se proporciona una `image` base. El valor debe ser un múltiplo de 64. El valor por defecto es 512. |
| `height` | INT | Sí | 64 a 4096 | La altura del lienzo en píxeles, utilizada cuando no se proporciona una `image` base. El valor debe ser un múltiplo de 64. El valor por defecto es 512. |
| `bg_color` | COLOR | Sí | - | El color de fondo para el lienzo, especificado como un código hexadecimal (por ejemplo, #000000). Solo se utiliza cuando no se proporciona una `image` base. El valor por defecto es negro (#000000). |

**Nota:** La entrada `mask` está diseñada para funcionar con el widget especializado de la interfaz de usuario del nodo. Cuando se pinta en el lienzo, el widget rellena automáticamente este valor. Las entradas `width` y `height` están ocultas en la interfaz de usuario estándar pero definen las dimensiones del lienzo al crear una nueva imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen final compuesta. Este es el resultado de mezclar las áreas pintadas (de la `mask`) sobre la `image` base proporcionada o el fondo coloreado. |
| `MASK` | MASK | La máscara del canal alfa (transparencia) extraída de la pintura. Las áreas blancas representan las regiones pintadas y las áreas negras representan el fondo no tocado. |