> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomCropImages/es.md)

El nodo Random Crop Images selecciona aleatoriamente una sección rectangular de cada imagen de entrada y la recorta a un ancho y alto especificados. Esto se utiliza comúnmente para aumentar datos y crear variaciones de imágenes de entrenamiento. La posición aleatoria para el recorte se determina mediante un valor de semilla, lo que garantiza que el mismo recorte pueda reproducirse.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen que se va a recortar. |
| `width` | INT | No | 1 - 8192 | El ancho del área de recorte (predeterminado: 512). |
| `height` | INT | No | 1 - 8192 | La altura del área de recorte (predeterminado: 512). |
| `seed` | INT | No | 0 - 18446744073709551615 | Un número utilizado para controlar la posición aleatoria del recorte (predeterminado: 0). |

**Nota:** Los parámetros `width` y `height` deben ser menores o iguales a las dimensiones de la imagen de entrada. Si una dimensión especificada es mayor que la imagen, el recorte se limitará al borde de la imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen resultante después de aplicar el recorte aleatorio. |
