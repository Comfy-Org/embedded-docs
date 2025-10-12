> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/es.md)

Genera videos basados en prompts y tamaño de salida. Este nodo crea videos de transición entre dos imágenes de entrada utilizando la API de PixVerse, permitiéndole especificar la calidad del video, duración, estilo de movimiento y parámetros de generación.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `primer fotograma` | IMAGE | Sí | - | La imagen inicial para la transición de video |
| `último fotograma` | IMAGE | Sí | - | La imagen final para la transición de video |
| `prompt` | STRING | Sí | - | Prompt para la generación del video (valor por defecto: cadena vacía) |
| `calidad` | COMBO | Sí | Opciones de calidad disponibles del enum PixverseQuality<br>Por defecto: res_540p | Configuración de calidad de video |
| `duración en segundos` | COMBO | Sí | Opciones de duración disponibles del enum PixverseDuration | Duración del video en segundos |
| `modo de movimiento` | COMBO | Sí | Opciones de modo de movimiento disponibles del enum PixverseMotionMode | Estilo de movimiento para la transición |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla para la generación de video (valor por defecto: 0) |
| `prompt negativo` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen (valor por defecto: cadena vacía) |

**Nota:** Al utilizar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas a 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video de transición generado |