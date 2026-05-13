> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/es.md)

El nodo Painter proporciona un lienzo interactivo para crear o editar imágenes y máscaras directamente dentro de ComfyUI. Permite comenzar con un lienzo en blanco o una imagen existente, pintar sobre ella usando una herramienta de pincel, y genera tanto la imagen resultante como una máscara alfa correspondiente. La máscara define las áreas pintadas, que luego se componen sobre la imagen base o el color de fondo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | No | - | Imagen base opcional sobre la que pintar. Si no se proporciona, se crea un lienzo en blanco usando el color de fondo, ancho y alto especificados. |
| `mask` | STRING | Sí | - | Los datos de pintura, generados típicamente por el widget interactivo integrado del nodo. Este parámetro es gestionado por la herramienta de pintura de la interfaz de usuario y no está diseñado para conectarse a un conector estándar. |
| `ancho` | INT | Sí | 64 a 4096 | El ancho del lienzo en píxeles, utilizado cuando no se proporciona una `imagen` base. El valor debe ser múltiplo de 64. Valor predeterminado: 512. |
| `alto` | INT | Sí | 64 a 4096 | La altura del lienzo en píxeles, utilizada cuando no se proporciona una `imagen` base. El valor debe ser múltiplo de 64. Valor predeterminado: 512. |
| `color_de_fondo` | COLOR | Sí | - | El color de fondo del lienzo, especificado como código hexadecimal (ej. #000000). Solo se usa cuando no se proporciona una `imagen` base. Valor predeterminado: negro (#000000). |

**Nota:** La entrada `mask` está diseñada para funcionar con el widget especializado de la interfaz del nodo. Cuando pintas en el lienzo, el widget completa automáticamente este valor. Las entradas `width` y `height` están ocultas en la interfaz estándar, pero definen las dimensiones del lienzo al crear una nueva imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La imagen final compuesta. Es el resultado de fusionar las áreas pintadas (de la `mask`) sobre la `imagen` base proporcionada o el fondo de color. |
| `MASK` | MASK | La máscara de canal alfa (transparencia) extraída de la pintura. Las áreas blancas representan las regiones pintadas, y las áreas negras representan el fondo no modificado. |

---
**Source fingerprint (SHA-256):** `ae926b6d30aab65737bd99a58cb7de5a71fa36e61a677dbc97fc30b8ef8d2418`
