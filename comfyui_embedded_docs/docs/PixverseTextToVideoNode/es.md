> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/es.md)

Genera videos basados en el prompt y el tamaño de salida. Este nodo crea contenido de video utilizando descripciones de texto y varios parámetros de generación, produciendo salida de video a través de la API de PixVerse.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación del video (por defecto: "") |
| `relación_de_aspecto` | COMBO | Sí | Opciones de PixverseAspectRatio | Relación de aspecto para el video generado |
| `calidad` | COMBO | Sí | Opciones de PixverseQuality | Configuración de calidad de video (por defecto: PixverseQuality.res_540p) |
| `duración_segundos` | COMBO | Sí | Opciones de PixverseDuration | Duración del video generado en segundos |
| `modo_de_movimiento` | COMBO | Sí | Opciones de PixverseMotionMode | Estilo de movimiento para la generación del video |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla para la generación de video (por defecto: 0) |
| `prompt_negativo` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen (por defecto: "") |
| `plantilla_pixverse` | CUSTOM | No | - | Una plantilla opcional para influir en el estilo de generación, creada por el nodo PixVerse Template |

**Nota:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas a 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |