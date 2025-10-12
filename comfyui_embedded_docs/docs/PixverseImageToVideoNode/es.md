> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/es.md)

Genera videos basados en una imagen de entrada y un texto descriptivo. Este nodo toma una imagen y crea un video animado aplicando los ajustes de movimiento y calidad especificados para transformar la imagen estática en una secuencia en movimiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen de entrada para transformar en video |
| `prompt` | STRING | Sí | - | Texto descriptivo para la generación del video |
| `calidad` | COMBO | Sí | `res_540p`<br>`res_1080p` | Configuración de calidad de video (por defecto: res_540p) |
| `duración_en_segundos` | COMBO | Sí | `dur_2`<br>`dur_5`<br>`dur_10` | Duración del video generado en segundos |
| `modo_de_movimiento` | COMBO | Sí | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Estilo de movimiento aplicado a la generación del video |
| `semilla` | INT | Sí | 0-2147483647 | Semilla para la generación del video (por defecto: 0) |
| `prompt_negativo` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen |
| `plantilla_pixverse` | CUSTOM | No | - | Una plantilla opcional para influir en el estilo de generación, creada por el nodo PixVerse Template |

**Nota:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas a 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | Video generado basado en la imagen de entrada y los parámetros |
