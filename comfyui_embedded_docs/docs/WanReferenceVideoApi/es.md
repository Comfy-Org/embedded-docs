> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/es.md)

El nodo Wan Reference to Video utiliza la apariencia visual y la voz de uno o más videos de referencia de entrada, junto con un texto descriptivo, para generar un nuevo video. Mantiene la coherencia con los personajes del material de referencia mientras crea contenido nuevo basado en tu descripción.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"wan2.6-r2v"` | El modelo de IA específico a utilizar para la generación de video. |
| `prompt` | STRING | Sí | - | Una descripción de los elementos y características visuales para el nuevo video. Admite inglés y chino. Usa identificadores como `character1` y `character2` para referirte a los personajes de los videos de referencia. |
| `negative_prompt` | STRING | No | - | Una descripción de elementos o características a evitar en el video generado. |
| `reference_videos` | AUTOGROW | Sí | - | Una lista de entradas de video utilizadas como referencia para la apariencia y voz de los personajes. Debes proporcionar al menos un video. A cada video se le puede asignar un nombre como `character1`, `character2` o `character3`. |
| `size` | COMBO | Sí | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` | La resolución y relación de aspecto para el video de salida. |
| `duration` | INT | Sí | 5 a 10 | La duración del video generado en segundos. El valor debe ser un múltiplo de 5 (por defecto: 5). |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla aleatoria para resultados reproducibles. Un valor de 0 generará una semilla aleatoria. |
| `shot_type` | COMBO | Sí | `"single"`<br>`"multi"` | Especifica si el video generado es una toma continua única o contiene múltiples tomas con cortes. |
| `watermark` | BOOLEAN | No | - | Cuando está habilitado, se añade una marca de agua generada por IA al video final (por defecto: Falso). |

**Restricciones:**

* Cada video proporcionado en `reference_videos` debe tener una duración entre 2 y 30 segundos.
* El parámetro `duration` está limitado a valores específicos (5 o 10 segundos).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video recién generado. |
