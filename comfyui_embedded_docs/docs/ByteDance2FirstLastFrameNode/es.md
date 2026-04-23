> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2FirstLastFrameNode/es.md)

Este nodo utiliza el modelo Seedance 2.0 de ByteDance para generar un vídeo. Crea el vídeo basándose en un texto descriptivo (prompt) y en una imagen de primer fotograma obligatoria. Opcionalmente, se puede proporcionar una imagen de último fotograma para guiar el final de la secuencia de vídeo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | El modelo a utilizar para la generación de vídeo. Seedance 2.0 es para la máxima calidad, mientras que Seedance 2.0 Fast está optimizado para velocidad. Al seleccionar un modelo, se revelarán entradas adicionales para `prompt`, `resolution`, `ratio`, `duration` y `generate_audio`. |
| `first_frame` | IMAGE | No | - | La imagen a utilizar como primer fotograma del vídeo. |
| `last_frame` | IMAGE | No | - | La imagen a utilizar como último fotograma del vídeo. |
| `first_frame_asset_id` | STRING | No | - | Un asset_id de Seedance para usar como primer fotograma. No se puede utilizar al mismo tiempo que la entrada de imagen `first_frame`. El valor por defecto es una cadena vacía. |
| `last_frame_asset_id` | STRING | No | - | Un asset_id de Seedance para usar como último fotograma. No se puede utilizar al mismo tiempo que la entrada de imagen `last_frame`. El valor por defecto es una cadena vacía. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla. Cambiar esta semilla hará que el nodo se vuelva a ejecutar, pero los resultados no son deterministas. El valor por defecto es 0. |
| `watermark` | BOOLEAN | No | - | Indica si se debe añadir una marca de agua al vídeo generado. El valor por defecto es Falso. |

**Restricciones de Parámetros:**
*   Debes proporcionar **ya sea** una imagen `first_frame` **o** un `first_frame_asset_id`. Proporcionar ambos causará un error.
*   No puedes proporcionar tanto una imagen `last_frame` como un `last_frame_asset_id` para el mismo fotograma.
*   La entrada `model` es un combo dinámico. Después de seleccionar un modelo, también debes completar el campo `prompt` que se revela (una descripción de texto) y configurar los otros parámetros revelados (`resolution`, `ratio`, `duration`, `generate_audio`).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El vídeo generado. |