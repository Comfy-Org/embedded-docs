> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2TextToVideoNode/es.md)

Este nodo utiliza la API Seedance 2.0 de ByteDance para generar un vídeo a partir de una descripción de texto. Envía su *prompt* al modelo seleccionado, espera a que se procese el vídeo y devuelve el resultado final.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | El modelo a utilizar para la generación de vídeo. Al seleccionar un modelo, se mostrarán entradas adicionales obligatorias para el *prompt*, la resolución, la relación de aspecto, la duración y la generación de audio. "Seedance 2.0" es para máxima calidad; "Seedance 2.0 Fast" está optimizado para velocidad. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla (por defecto: 0). El nodo se volverá a ejecutar si este valor cambia, pero los resultados no son deterministas independientemente de la semilla. |
| `watermark` | BOOLEAN | No | `True` / `False` | Indica si se debe añadir una marca de agua al vídeo (por defecto: False). Esta es una configuración avanzada. |

**Nota:** El parámetro `model` es un combo dinámico. Cuando selecciona un modelo, se mostrarán varios subparámetros obligatorios que deben completarse, incluyendo el *prompt* de texto, la resolución, la relación de aspecto, la duración y si se debe generar audio. El texto del *prompt* debe tener al menos 1 carácter de longitud después de eliminar los espacios en blanco.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de vídeo generado. |