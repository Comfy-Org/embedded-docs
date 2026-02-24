> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/es.md)

Este nodo genera un video interpolando entre un fotograma inicial y un final proporcionados, guiado por un texto descriptivo. Utiliza el modelo Vidu Q3 para crear una transición fluida entre las dos imágenes, produciendo un video de una duración y resolución específicas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` | El modelo a utilizar para la generación del video. Seleccionar una opción revela parámetros de configuración adicionales para `resolution`, `duration` y `audio`. |
| `model.resolution` | COMBO | Sí | `"720p"`<br>`"1080p"` | Resolución del video de salida. Este parámetro se revela después de seleccionar un `model`. |
| `model.duration` | INT | Sí | 1 a 16 | Duración del video de salida en segundos (por defecto: 5). Este parámetro se revela después de seleccionar un `model`. |
| `model.audio` | BOOLEAN | Sí | `True` / `False` | Cuando está habilitado, genera un video con sonido (incluyendo diálogo y efectos de sonido) (por defecto: False). Este parámetro se revela después de seleccionar un `model`. |
| `first_frame` | IMAGE | Sí | - | La imagen inicial para la secuencia de video. |
| `end_frame` | IMAGE | Sí | - | La imagen final para la secuencia de video. |
| `prompt` | STRING | Sí | - | Una descripción textual que guía la generación del video (máximo 2000 caracteres). |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla para controlar la aleatoriedad de la generación (por defecto: 1). |

**Nota:** Las imágenes `first_frame` y `end_frame` deben tener proporciones de aspecto similares para obtener resultados óptimos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado. |